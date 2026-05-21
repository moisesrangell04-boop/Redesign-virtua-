#!/usr/bin/env python3
"""
Script para substituir logos genéricas das operadoras por logos reais em SVG.
Usa SVGs inline baseados nas logos oficiais de cada operadora.
O estilo CSS segue o padrão da Bradesco (que está correto).
"""
import os
import re
import base64

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Estilo padrão da Bradesco (referência)
LOGO_STYLE = 'height:72px;max-width:220px;width:auto;border-radius:16px;box-shadow:0 6px 24px rgba(0,0,0,0.22);background:white;padding:12px 20px;object-fit:contain;'

# SVGs das logos reais das operadoras
# Baseados nas logos oficiais com cores e formas corretas

LOGOS_SVG = {}

# ========== UNIMED ==========
# Logo verde com texto "unimed" e símbolo da árvore/folha
LOGOS_SVG["unimed"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 120">
  <defs>
    <style>
      .unimed-green { fill: #00995D; }
      .unimed-text { font-family: Arial, Helvetica, sans-serif; font-weight: bold; font-size: 54px; fill: #00995D; }
    </style>
  </defs>
  <!-- Unimed leaf/tree symbol -->
  <g transform="translate(15, 10)">
    <path class="unimed-green" d="M45,5 C50,5 55,8 58,12 C65,5 75,5 80,12 C85,19 82,28 75,33 L50,55 L25,33 C18,28 15,19 20,12 C25,5 35,5 42,12 C43,8 44,5 45,5 Z" />
    <path class="unimed-green" d="M35,58 C35,58 45,75 50,90 C55,75 65,58 65,58" stroke="#00995D" stroke-width="3" fill="none"/>
    <path class="unimed-green" d="M30,70 C35,65 45,68 50,75" stroke="#00995D" stroke-width="2.5" fill="none"/>
    <path class="unimed-green" d="M70,70 C65,65 55,68 50,75" stroke="#00995D" stroke-width="2.5" fill="none"/>
  </g>
  <text class="unimed-text" x="110" y="75">unimed</text>
</svg>'''

# ========== SULAMERICA ==========
# Logo azul/laranja com ondas
LOGOS_SVG["sulamerica"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 120">
  <defs>
    <style>
      .sa-blue { fill: #003B71; }
      .sa-orange { fill: #F37021; }
      .sa-text { font-family: Arial, Helvetica, sans-serif; font-weight: bold; font-size: 36px; fill: #003B71; }
    </style>
  </defs>
  <g transform="translate(10, 15)">
    <!-- S symbol with waves -->
    <path class="sa-blue" d="M10,50 Q25,20 50,35 Q75,50 50,65 Q25,80 40,90" stroke="#003B71" stroke-width="8" fill="none" stroke-linecap="round"/>
    <path class="sa-orange" d="M15,55 Q30,25 55,40 Q80,55 55,70 Q30,85 45,95" stroke="#F37021" stroke-width="4" fill="none" stroke-linecap="round"/>
  </g>
  <text class="sa-text" x="85" y="55">SulAmérica</text>
  <text style="font-family: Arial, sans-serif; font-size: 16px; fill: #003B71;" x="85" y="80">Saúde</text>
</svg>'''

# ========== HAPVIDA ==========
# Logo verde com coração/folha
LOGOS_SVG["hapvida"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 120">
  <defs>
    <style>
      .hap-green { fill: #009045; }
      .hap-text { font-family: Arial, Helvetica, sans-serif; font-weight: bold; font-size: 42px; fill: #009045; }
      .hap-sub { font-family: Arial, Helvetica, sans-serif; font-size: 14px; fill: #666; }
    </style>
  </defs>
  <g transform="translate(10, 12)">
    <!-- Heart symbol -->
    <path class="hap-green" d="M40,25 C40,15 50,5 60,5 C70,5 80,15 80,25 C80,45 60,60 60,70 C60,60 40,45 40,25 Z" />
    <path fill="#fff" d="M55,22 C55,18 60,14 65,18 C68,20 65,28 60,32 C55,28 52,20 55,22 Z" opacity="0.4"/>
  </g>
  <text class="hap-text" x="100" y="60">hapvida</text>
  <text class="hap-sub" x="100" y="82">NotreDame Intermédica</text>
</svg>'''

# ========== INTERMEDICA ==========
# Logo laranja NotreDame Intermédica
LOGOS_SVG["intermedica"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 440 120">
  <defs>
    <style>
      .ndi-orange { fill: #F58220; }
      .ndi-blue { fill: #003B71; }
      .ndi-text { font-family: Arial, Helvetica, sans-serif; font-weight: bold; font-size: 32px; fill: #003B71; }
      .ndi-sub { font-family: Arial, Helvetica, sans-serif; font-weight: bold; font-size: 24px; fill: #F58220; }
    </style>
  </defs>
  <g transform="translate(15, 18)">
    <!-- Cross symbol -->
    <rect class="ndi-orange" x="25" y="5" width="20" height="60" rx="4"/>
    <rect class="ndi-orange" x="5" y="25" width="60" height="20" rx="4"/>
    <!-- Circle around -->
    <circle cx="35" cy="35" r="38" fill="none" stroke="#003B71" stroke-width="3"/>
  </g>
  <text class="ndi-text" x="105" y="48">NotreDame</text>
  <text class="ndi-sub" x="105" y="80">Intermédica</text>
</svg>'''

# ========== PREVENT SENIOR ==========
# Logo azul com pessoa estilizada
LOGOS_SVG["prevent_senior"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 120">
  <defs>
    <style>
      .ps-blue { fill: #003366; }
      .ps-green { fill: #7AB648; }
      .ps-text { font-family: Arial, Helvetica, sans-serif; font-weight: bold; font-size: 36px; fill: #003366; }
      .ps-sub { font-family: Arial, Helvetica, sans-serif; font-weight: bold; font-size: 28px; fill: #7AB648; }
    </style>
  </defs>
  <g transform="translate(15, 10)">
    <!-- Person with outstretched arms -->
    <circle class="ps-green" cx="35" cy="18" r="12"/>
    <path class="ps-green" d="M35,30 L35,65 M20,42 L35,35 L50,42 M25,85 L35,65 L45,85" stroke="#7AB648" stroke-width="5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
  </g>
  <text class="ps-text" x="80" y="48">Prevent</text>
  <text class="ps-sub" x="80" y="82">Senior</text>
</svg>'''

# ========== PORTO SEGURO SAÚDE ==========
# Logo azul com âncora/vela
LOGOS_SVG["porto_seguro"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 120">
  <defs>
    <style>
      .porto-blue { fill: #003399; }
      .porto-yellow { fill: #FFD700; }
      .porto-text { font-family: Arial, Helvetica, sans-serif; font-weight: bold; font-size: 38px; fill: #003399; }
      .porto-sub { font-family: Arial, Helvetica, sans-serif; font-size: 18px; fill: #003399; }
    </style>
  </defs>
  <g transform="translate(12, 10)">
    <!-- Sail/shield symbol -->
    <path class="porto-blue" d="M30,5 L30,75 L65,75 Z" opacity="0.8"/>
    <path class="porto-yellow" d="M35,20 L35,70 L58,70 Z" opacity="0.6"/>
    <line x1="30" y1="5" x2="30" y2="80" stroke="#003399" stroke-width="3"/>
    <line x1="20" y1="80" x2="70" y2="80" stroke="#003399" stroke-width="3"/>
  </g>
  <text class="porto-text" x="90" y="55">Porto</text>
  <text class="porto-sub" x="90" y="80">Seguro Saúde</text>
</svg>'''

# ========== SAMP ==========
# Logo SAMP/São Bernardo
LOGOS_SVG["samp"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 120">
  <defs>
    <style>
      .samp-green { fill: #00A650; }
      .samp-blue { fill: #003B71; }
      .samp-text { font-family: Arial, Helvetica, sans-serif; font-weight: 800; font-size: 48px; fill: #003B71; }
      .samp-sub { font-family: Arial, Helvetica, sans-serif; font-size: 16px; fill: #00A650; }
    </style>
  </defs>
  <g transform="translate(15, 15)">
    <!-- Heart/health symbol -->
    <path class="samp-green" d="M30,20 C30,10 40,2 48,10 C56,2 66,10 66,20 C66,35 48,48 48,48 C48,48 30,35 30,20 Z"/>
    <path fill="white" d="M42,22 L54,22 L54,18 L42,18 Z M46,14 L50,14 L50,26 L46,26 Z"/>
  </g>
  <text class="samp-text" x="90" y="60">SAMP</text>
  <text class="samp-sub" x="90" y="82">São Bernardo Saúde</text>
</svg>'''

# ========== CABERJ / INTEGRAL SAÚDE ==========
LOGOS_SVG["caberj"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 420 120">
  <defs>
    <style>
      .cab-blue { fill: #1B3C87; }
      .cab-green { fill: #00A651; }
      .cab-text { font-family: Arial, Helvetica, sans-serif; font-weight: bold; font-size: 34px; fill: #1B3C87; }
      .cab-sub { font-family: Arial, Helvetica, sans-serif; font-size: 20px; fill: #00A651; font-weight: bold; }
    </style>
  </defs>
  <g transform="translate(10, 15)">
    <!-- Cross/health symbol -->
    <rect class="cab-blue" x="15" y="5" width="50" height="50" rx="8"/>
    <rect fill="white" x="30" y="12" width="20" height="36" rx="2"/>
    <rect fill="white" x="22" y="22" width="36" height="16" rx="2"/>
    <circle class="cab-green" cx="58" cy="48" r="12"/>
    <path fill="white" d="M53,48 L63,48 M58,43 L58,53" stroke="white" stroke-width="2.5"/>
  </g>
  <text class="cab-text" x="90" y="42">Integral</text>
  <text class="cab-sub" x="90" y="72">Saúde</text>
</svg>'''


# Mapeamento de operadora -> diretórios
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
}


def svg_to_data_uri(svg_string):
    """Converte SVG para data URI base64."""
    b64 = base64.b64encode(svg_string.strip().encode('utf-8')).decode('utf-8')
    return f"data:image/svg+xml;base64,{b64}"


def update_html_logo(html_path, new_src, operator):
    """Substitui a src da logo no HTML mantendo o mesmo estilo."""
    if not os.path.exists(html_path):
        print(f"  ⚠️  Arquivo não encontrado: {os.path.basename(html_path)}")
        return False

    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Padrão para encontrar a img dentro de op-hero-logo
    pattern = r'(<div class="op-hero-logo"[^>]*>)\s*<img\s+src="[^"]*"\s+alt="([^"]*)"\s+style="[^"]*">'

    match = re.search(pattern, content)
    if match:
        div_tag = match.group(1)
        alt_text = match.group(2)

        new_tag = f'{div_tag}<img src="{new_src}" alt="{alt_text}" style="{LOGO_STYLE}">'
        new_content = content[:match.start()] + new_tag + content[match.end():]

        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"  ✅ Atualizado: {os.path.basename(os.path.dirname(html_path))}/index.html")
        return True
    else:
        print(f"  ⚠️  Padrão de logo não encontrado em: {os.path.basename(os.path.dirname(html_path))}")
        return False


def main():
    print("=" * 60)
    print("🔄 Atualizando logos das operadoras (SVG vetorial)")
    print("=" * 60)

    updated = 0
    failed = 0

    for operator, dirs in OPERATOR_DIRS.items():
        if operator not in LOGOS_SVG:
            print(f"\n⏭️  Pulando {operator} (sem SVG definido)")
            continue

        data_uri = svg_to_data_uri(LOGOS_SVG[operator])
        print(f"\n🔧 Atualizando {operator} ({len(dirs)} página(s)):")

        for d in dirs:
            html_path = os.path.join(BASE_DIR, d, "index.html")
            if update_html_logo(html_path, data_uri, operator):
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
