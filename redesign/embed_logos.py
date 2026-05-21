#!/usr/bin/env python3
"""
Embute as logos como base64 data-URI diretamente no HTML de cada operadora.
Elimina problemas de MIME type e caminhos relativos.
"""

import os, re, base64, mimetypes

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOGOS_DIR = os.path.join(BASE_DIR, "assets", "logos")

# Mapeamento operadora → arquivo de logo
LOGO_MAP = {
    "amil":                     "amil.png",
    "bradesco":                 "bradesco.png",
    "sulamerica":               "sulamerica.png",
    "bh-sulamerica":            "sulamerica.png",
    "joao-pessoa-sulamerica":   "sulamerica.png",
    "sulamerica-direto":        "sulamerica.png",
    "sulamerica-recife":        "sulamerica.png",
    "porto-seguro":             "porto-seguro.png",
    "unimed":                   "unimed.svg",
    "unimed-campos":            "unimed.svg",
    "intermedica":              "intermedica.png",
    "hapvida":                  "hapvida.png",
    "hapvida-brasilia":         "hapvida.png",
    "hapvida-manaus":           "hapvida.png",
    "hapvida-recife":           "hapvida.png",
    "hapvida-salvador":         "hapvida.png",
    "prevent-senior":           "prevent-senior.png",
    "caberj":                   "caberj.png",
    "samp-es":                  "samp.png",
}

def to_data_uri(logo_path):
    """Converte arquivo de logo para data URI base64."""
    mime, _ = mimetypes.guess_type(logo_path)
    if not mime:
        mime = "image/png"
    with open(logo_path, "rb") as f:
        data = f.read()
    b64 = base64.b64encode(data).decode("ascii")
    return f"data:{mime};base64,{b64}"

def get_logo_key(folder_name):
    """Extrai a chave do operador a partir do nome da pasta."""
    name = folder_name.replace("plano-de-saude-", "").replace("reembolso-", "")
    # Tenta match exato primeiro
    if name in LOGO_MAP:
        return name
    # Tenta match por prefixo
    for key in LOGO_MAP:
        if name.startswith(key) or key.startswith(name):
            return key
    return None

def process_folder(folder_path):
    folder_name = os.path.basename(folder_path)
    html_file = os.path.join(folder_path, "index.html")
    if not os.path.exists(html_file):
        return False

    with open(html_file, "r", encoding="utf-8") as f:
        content = f.read()

    # Verifica se tem a div de logo
    if 'class="op-hero-logo"' not in content:
        print(f"  ⚠️  {folder_name} — sem bloco op-hero-logo, pulando")
        return False

    # Descobre qual logo usar
    logo_key = get_logo_key(folder_name)
    if not logo_key:
        print(f"  ⚠️  {folder_name} — operadora não mapeada")
        return False

    logo_file = os.path.join(LOGOS_DIR, LOGO_MAP[logo_key])
    if not os.path.exists(logo_file):
        print(f"  ❌ {folder_name} — arquivo não existe: {logo_file}")
        return False

    # Verifica se o arquivo é realmente uma imagem (não HTML de erro)
    with open(logo_file, "rb") as f:
        header = f.read(16)
    is_image = (
        header[:8] == b'\x89PNG\r\n\x1a\n' or
        header[:3] == b'\xff\xd8\xff' or
        b'<svg' in header or b'<?xml' in header or
        header[:6] in (b'GIF87a', b'GIF89a') or
        (header[:4] == b'RIFF' and header[8:12] == b'WEBP')
    )
    if not is_image:
        print(f"  ❌ {folder_name} — logo corrompido (HTML de erro?): {LOGO_MAP[logo_key]}")
        return False

    data_uri = to_data_uri(logo_file)
    op_name = folder_name.replace("plano-de-saude-", "").replace("-", " ").title()

    new_logo_html = (
        f'<div class="op-hero-logo" style="margin-bottom:28px;">'
        f'<img src="{data_uri}" alt="Logo {op_name}" '
        f'style="height:72px;max-width:220px;width:auto;border-radius:16px;'
        f'box-shadow:0 6px 24px rgba(0,0,0,0.22);background:white;'
        f'padding:12px 20px;object-fit:contain;">'
        f'</div>'
    )

    # Substitui o bloco op-hero-logo existente
    new_content = re.sub(
        r'<div class="op-hero-logo"[^>]*>.*?</div>',
        new_logo_html,
        content,
        flags=re.DOTALL
    )

    if new_content == content:
        print(f"  ⚠️  {folder_name} — nenhuma substituição feita")
        return False

    with open(html_file, "w", encoding="utf-8") as f:
        f.write(new_content)

    size_kb = os.path.getsize(logo_file) // 1024
    print(f"  ✅ {folder_name} ← {LOGO_MAP[logo_key]} ({size_kb}KB embutido)")
    return True

def main():
    folders = sorted([
        os.path.join(BASE_DIR, d)
        for d in os.listdir(BASE_DIR)
        if os.path.isdir(os.path.join(BASE_DIR, d)) and
        (d.startswith("plano-de-saude-") or d.startswith("reembolso-"))
    ])

    ok = 0
    for folder in folders:
        if process_folder(folder):
            ok += 1

    print(f"\n{'─'*50}")
    print(f"Páginas atualizadas: {ok}/{len(folders)}")

if __name__ == "__main__":
    main()
