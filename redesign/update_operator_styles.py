#!/usr/bin/env python3
"""
Atualiza cores e logos das páginas de operadoras de saúde.
Uso: python3 update_operator_styles.py
"""

import os
import re
import glob

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Mapeamento: slug-da-pasta -> (gradiente, cor-do-texto-btn, favicon-domain, nome-display)
OPERATORS = {
    "amil": {
        "gradient": "linear-gradient(135deg, #E91E63 0%, #C2185B 100%)",
        "btn_color": "#C2185B",
        "logo_file": "amil.png",
        "name": "Amil",
    },
    "bradesco": {
        "gradient": "linear-gradient(135deg, #E62A43 0%, #B0001E 100%)",
        "btn_color": "#B0001E",
        "logo_file": "bradesco.png",
        "name": "Bradesco Saúde",
    },
    "sulamerica": {
        "gradient": "linear-gradient(135deg, #FF8C00 0%, #C85A00 100%)",
        "btn_color": "#C85A00",
        "logo_file": "sulamerica.png",
        "name": "SulAmérica",
    },
    "porto-seguro": {
        "gradient": "linear-gradient(135deg, #005AAB 0%, #003A7A 100%)",
        "btn_color": "#003A7A",
        "logo_file": "porto-seguro.png",
        "name": "Porto Seguro Saúde",
    },
    "unimed": {
        "gradient": "linear-gradient(135deg, #00B16A 0%, #007A4A 100%)",
        "btn_color": "#007A4A",
        "logo_file": "unimed.svg",
        "name": "Unimed",
    },
    "intermedica": {
        "gradient": "linear-gradient(135deg, #00B4DB 0%, #006FA6 100%)",
        "btn_color": "#006FA6",
        "logo_file": "intermedica.png",
        "name": "Intermédica",
    },
    "hapvida": {
        "gradient": "linear-gradient(135deg, #FFC107 0%, #FF8F00 100%)",
        "btn_color": "#E65100",
        "logo_file": "hapvida.png",
        "name": "Hapvida",
    },
    "prevent-senior": {
        "gradient": "linear-gradient(135deg, #1A3A6B 0%, #0D2247 100%)",
        "btn_color": "#0D2247",
        "logo_file": "prevent-senior.png",
        "name": "Prevent Senior",
    },
    "caberj": {
        "gradient": "linear-gradient(135deg, #1565C0 0%, #0D47A1 100%)",
        "btn_color": "#0D47A1",
        "logo_file": "caberj.png",
        "name": "Caberj",
    },
    "samp": {
        "gradient": "linear-gradient(135deg, #2E7D32 0%, #1B5E20 100%)",
        "btn_color": "#1B5E20",
        "logo_file": "samp.png",
        "name": "Samp",
    },
    "para-idosos": {
        "gradient": "linear-gradient(135deg, #6A1B9A 0%, #4A148C 100%)",
        "btn_color": "#4A148C",
        "logo_file": "",
        "name": "Plano para Idosos",
    },
    "rj": {
        "gradient": "linear-gradient(135deg, #1976D2 0%, #0D47A1 100%)",
        "btn_color": "#0D47A1",
        "logo_file": "",
        "name": "Plano de Saúde RJ",
    },
}

def detect_operator(folder_name):
    """Detecta a operadora pelo nome da pasta."""
    name = folder_name.replace("plano-de-saude-", "").replace("reembolso-", "").replace("dental-", "")
    # Tenta match exato primeiro
    for key in OPERATORS:
        if name == key:
            return key
    # Match por prefixo (ex: hapvida-recife -> hapvida)
    for key in OPERATORS:
        if name.startswith(key):
            return key
    # Match por conteúdo (ex: bh-sulamerica-saude-direto -> sulamerica)
    for key in OPERATORS:
        if key in name:
            return key
    return None

def build_logo_html(op, folder_path):
    """Gera o HTML da logo usando arquivo local."""
    logo_file = op.get("logo_file", "")
    if not logo_file:
        return ""
    # Caminho relativo: todas as pastas de operadoras estão um nível abaixo do BASE_DIR
    rel_path = os.path.relpath(os.path.join(BASE_DIR, "assets", "logos", logo_file), folder_path)
    logo_src = rel_path.replace(os.sep, "/")
    return (
        f'<div class="op-hero-logo" style="margin-bottom:28px;">'
        f'<img src="{logo_src}" alt="Logo {op["name"]}" '
        f'style="height:72px;max-width:220px;width:auto;border-radius:16px;'
        f'box-shadow:0 6px 24px rgba(0,0,0,0.22);background:white;padding:12px 20px;'
        f'object-fit:contain;">'
        f'</div>'
    )

def update_html(filepath, op_key):
    op = OPERATORS[op_key]
    folder_path = os.path.dirname(filepath)
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    changed = False

    # 1. Atualiza o gradiente do .op-hero
    new_gradient = op["gradient"]
    pattern_hero = r'(\.op-hero\s*\{[^}]*background:\s*)([^;]+)(;)'
    def replace_gradient(m):
        return m.group(1) + new_gradient + m.group(3)
    new_content = re.sub(pattern_hero, replace_gradient, content, count=1, flags=re.DOTALL)
    if new_content != content:
        changed = True
        content = new_content

    # 2. Atualiza a cor do texto do .btn-hero-primary (color: #XXXXXX)
    btn_color = op["btn_color"]
    pattern_btn = r'(\.op-hero \.btn-hero-primary\s*\{[^}]*color:\s*)(#[0-9a-fA-F]{3,6})(;)'
    def replace_btn_color(m):
        return m.group(1) + btn_color + m.group(3)
    new_content = re.sub(pattern_btn, replace_btn_color, content, count=1, flags=re.DOTALL)
    if new_content != content:
        changed = True
        content = new_content

    # 3. Insere/substitui a logo antes do <h1>
    logo_html = build_logo_html(op, folder_path)
    # Remove logo antiga se existir
    old_logo_pattern = r'<div class="op-hero-logo"[^>]*>.*?</div>'
    new_content = re.sub(old_logo_pattern, '', content, count=1, flags=re.DOTALL)
    if new_content != content:
        changed = True
        content = new_content
    # Insere logo nova (se houver URL definida)
    if logo_html:
        pattern_h1 = r'(<h1>)'
        new_content = re.sub(pattern_h1, logo_html + r'\1', content, count=1)
        if new_content != content:
            changed = True
            content = new_content

    if changed:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        return True
    return False

def main():
    folders = (
        glob.glob(os.path.join(BASE_DIR, "plano-de-saude-*")) +
        glob.glob(os.path.join(BASE_DIR, "reembolso-*")) +
        glob.glob(os.path.join(BASE_DIR, "dental-*"))
    )

    updated = 0
    skipped = 0
    not_found = []

    for folder in sorted(folders):
        if not os.path.isdir(folder):
            continue
        index_path = os.path.join(folder, "index.html")
        if not os.path.exists(index_path):
            continue

        folder_name = os.path.basename(folder)
        op_key = detect_operator(folder_name)

        if op_key is None:
            not_found.append(folder_name)
            skipped += 1
            continue

        result = update_html(index_path, op_key)
        status = "✅ atualizado" if result else "⏭  sem alterações"
        print(f"  {status}: {folder_name} → operadora: {op_key}")
        if result:
            updated += 1

    print(f"\n{'─'*50}")
    print(f"Total atualizado : {updated}")
    print(f"Sem alterações   : {skipped}")
    if not_found:
        print(f"Não mapeados ({len(not_found)}):")
        for n in not_found:
            print(f"    ⚠️  {n}")

if __name__ == "__main__":
    main()
