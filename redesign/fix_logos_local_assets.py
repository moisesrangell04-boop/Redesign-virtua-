#!/usr/bin/env python3
import os
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Estilo padrão da Bradesco (referência) modificado para object-fit adequado e etc
LOGO_STYLE = 'height:72px;max-width:220px;width:auto;border-radius:16px;box-shadow:0 6px 24px rgba(0,0,0,0.22);background:white;padding:12px 20px;object-fit:contain;'

# Estilos específicos caso alguma imagem venha com bordas cortadas ou muito grande
# Para Amil, diminuímos a altura utilizável do conteúdo (de 72px para 56px) 
# e aumentamos o padding (de 12px para 20px top/bottom) garantindo que a caixa final
# tenha exatamente o mesmo tamanho (56 + 20 + 20 = 96px de box height total) das outras.
CUSTOM_STYLES = {
    "amil": 'height:56px;max-width:220px;width:auto;border-radius:16px;box-shadow:0 6px 24px rgba(0,0,0,0.22);background:white;padding:20px 28px;object-fit:contain;',
}

OPERATOR_DIRS = {
    "unimed": [
        "plano-de-saude-unimed",
        "plano-de-saude-unimed-campos",
        "plano-saude-unimed-macae",
    ],
    "sulamerica": [
        "plano-de-saude-sulamerica",
        "plano-de-saude-sulamerica-direto-brasilia",
        "plano-de-saude-sulamerica-direto-salvador",
        "plano-de-saude-sulamerica-direto-sampa",
        "plano-de-saude-sulamerica-recife",
        "plano-de-saude-bh-sulamerica-saude-direto",
        "plano-de-saude-joao-pessoa-sulamerica",
        "reembolso-sulamerica",
    ],
    "hapvida": [
        "plano-de-saude-hapvida",
        "plano-de-saude-hapvida-brasilia",
        "plano-de-saude-hapvida-manaus",
        "plano-de-saude-hapvida-recife",
        "plano-de-saude-hapvida-salvador",
    ],
    "intermedica": [
        "plano-de-saude-intermedica",
        "reembolso-intermedica",
    ],
    "prevent_senior": [
        "plano-de-saude-prevent-senior",
    ],
    "porto_seguro": [
        "plano-de-saude-porto-seguro-saude",
    ],
    "samp": [
        "plano-de-saude-samp-es",
    ],
    "caberj": [
        "plano-de-saude-caberj-integral-saude",
    ],
    "amil": [
        "plano-de-saude-amil",
        "reembolso-amil",
    ],
    "bradesco": [
        "plano-de-saude-bradesco",
    ]
}

FILES = {
    "unimed": "unimed.png",
    "sulamerica": "sulamerica.png",
    "hapvida": "hapvida.png",
    "intermedica": "intermedica.png",
    "prevent_senior": "prevent-senior.png",
    "porto_seguro": "porto-seguro.png",
    "samp": "samp.png",
    "caberj": "caberj.png",
    "amil": "amil.png",
    "bradesco": "bradesco.png",
}

def update_html_logo(html_path, relative_src, operator):
    if not os.path.exists(html_path):
        print(f"  ⚠️  Arquivo não encontrado: {os.path.basename(html_path)}")
        return False

    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()

    pattern = r'(<div class="op-hero-logo"[^>]*>)\s*<img\s+src="[^"]*"\s+alt="([^"]*)"[^>]*>'

    match = re.search(pattern, content)
    if match:
        div_tag = match.group(1)
        alt_text = match.group(2)

        # Aplicar estilo customizado se existir, caso não, aplicar o padrão
        style_to_apply = CUSTOM_STYLES.get(operator, LOGO_STYLE)

        new_tag = f'{div_tag}<img src="{relative_src}" alt="{alt_text}" style="{style_to_apply}">'
        new_content = content[:match.start()] + new_tag + content[match.end():]

        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"  ✅ Atualizado: {os.path.basename(os.path.dirname(html_path))}/index.html -> {relative_src}")
        return True
    else:
        print(f"  ⚠️  Padrão de logo não encontrado em: {os.path.basename(os.path.dirname(html_path))}")
        return False

def main():
    print("=" * 60)
    print("🔄 Atualizando logos das operadoras (Arquivos Assets Locais)")
    print("=" * 60)

    updated = 0
    failed = 0

    for operator, dirs in OPERATOR_DIRS.items():
        if operator not in FILES:
            continue
        
        filename = FILES[operator]
        # Como as páginas estão dentro de subdiretórios tipo 'plano-de-saude-x', 
        # o caminho relativo pras logos é '../assets/logos/nome'
        relative_src = f"../assets/logos/{filename}"
        
        print(f"\n🔧 Atualizando {operator} ({len(dirs)} página(s)):")

        for d in dirs:
            html_path = os.path.join(BASE_DIR, d, "index.html")
            if update_html_logo(html_path, relative_src, operator):
                updated += 1
            else:
                failed += 1

    print(f"\n{'=' * 60}")
    print(f"📊 Resultado final:")
    print(f"  ✅ Atualizados: {updated}")
    print(f"  ❌ Falhas: {failed}")
    print(f"{'=' * 60}")

if __name__ == '__main__':
    main()
