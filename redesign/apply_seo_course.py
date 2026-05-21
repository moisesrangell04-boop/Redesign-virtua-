#!/usr/bin/env python3
"""
Implementa melhorias do curso Next SEO (Conversion Academy) em todas as páginas.

Módulos implementados:
- Módulo 8 (SEO Técnico): Twitter Cards, og:image:alt, correção de títulos longos
- Módulo 5 (E-A-T): Seção de autor/especialista em conteúdo de saúde
- Módulo 6 (SEO On-Page): BreadcrumbList schema + nav visual
- Schema: InsuranceAgency nas subpáginas
"""

import os
import re
import glob

BASE_URL = "https://www.virtuacorretora.com.br"
OG_IMAGE = "https://www.virtuacorretora.com.br/wp-content/uploads/2023/11/cropped-virtua-corretora-de-planos-de-saude-1.webp"
WHATSAPP = "https://wa.me/5522999404840"
PHONE_DISPLAY = "(22) 99940-4840"

ORG_SCHEMA = '''    <script type="application/ld+json">
    {
        "@context": "https://schema.org",
        "@type": "InsuranceAgency",
        "name": "Virtua Corretora de Seguros",
        "url": "https://www.virtuacorretora.com.br",
        "logo": "https://www.virtuacorretora.com.br/wp-content/uploads/2023/11/cropped-virtua-corretora-de-planos-de-saude-1.webp",
        "description": "Corretora de Seguros especializada em Planos de Saúde, Seguro Auto, Vida e Odontológico no Rio de Janeiro.",
        "telephone": ["+5522999404840", "+5522998811541"],
        "email": "contato@virtuacorretora.com.br",
        "areaServed": "BR",
        "address": {
            "@type": "PostalAddress",
            "addressRegion": "RJ",
            "addressCountry": "BR"
        },
        "sameAs": [
            "https://www.instagram.com/virtuacorretora",
            "https://www.facebook.com/virtuacorretora"
        ]
    }
    </script>'''

# E-A-T: bloco de autor/especialista — obrigatório para conteúdo YMYL (saúde)
AUTHOR_BLOCK = '''    <!-- E-A-T: Autor Especialista (obrigatório para conteúdo de saúde - YMYL) -->
    <section class="eat-author-section" style="background:#f8fafc; border-top:1px solid #e2e8f0; padding:32px 0;">
        <div class="container" style="max-width:900px; margin:0 auto; padding:0 24px;">
            <div style="display:flex; align-items:flex-start; gap:20px; flex-wrap:wrap;">
                <div style="flex-shrink:0; width:56px; height:56px; background:linear-gradient(135deg,#0066cc,#004d99); border-radius:50%; display:flex; align-items:center; justify-content:center;">
                    <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>
                </div>
                <div style="flex:1; min-width:220px;">
                    <p style="font-size:13px; color:#64748b; margin:0 0 4px; text-transform:uppercase; letter-spacing:.05em; font-weight:600;">Conteúdo verificado por especialista</p>
                    <p style="font-weight:700; font-size:16px; color:#1e293b; margin:0 0 4px;">Equipe de Corretores Virtua</p>
                    <p style="font-size:14px; color:#475569; margin:0; line-height:1.6;">Corretores certificados pela SUSEP (nº 15414.901434/2015-19) com mais de 10 anos de experiência em planos de saúde no Brasil. Todas as informações são revisadas periodicamente para garantir precisão e conformidade com as regulamentações da ANS.</p>
                    <p style="font-size:12px; color:#94a3b8; margin:8px 0 0;">Última atualização: <time datetime="2026-01-01">Janeiro de 2026</time></p>
                </div>
                <div style="flex-shrink:0; display:flex; align-items:center; gap:8px; background:white; border:1px solid #e2e8f0; border-radius:10px; padding:10px 16px;">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#0066cc" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
                    <span style="font-size:13px; font-weight:600; color:#1e293b;">SUSEP Autorizado</span>
                </div>
            </div>
        </div>
    </section>'''

def get_title(html):
    m = re.search(r'<title>(.*?)</title>', html, re.IGNORECASE | re.DOTALL)
    return m.group(1).strip() if m else ''

def get_canonical(html):
    m = re.search(r'<link rel="canonical" href="([^"]+)"', html)
    return m.group(1) if m else ''

def get_h1(html):
    m = re.search(r'<h1[^>]*>(.*?)</h1>', html, re.DOTALL)
    if m:
        inner = m.group(1)
        inner = re.sub(r'<br\s*/?>', ' ', inner, flags=re.IGNORECASE)
        return re.sub(r'<[^>]+>', '', inner).strip()
    return ''

def get_og_description(html):
    m = re.search(r'<meta property="og:description" content="([^"]+)"', html)
    return m.group(1) if m else ''

def get_og_title(html):
    m = re.search(r'<meta property="og:title" content="([^"]+)"', html)
    return m.group(1) if m else ''

def slug_to_label(slug):
    """Converte slug de URL para label legível."""
    labels = {
        'plano-de-saude-amil': 'Plano de Saúde Amil',
        'plano-de-saude-sulamerica': 'Plano SulAmérica',
        'plano-de-saude-bradesco': 'Plano Bradesco Saúde',
        'plano-de-saude-unimed': 'Plano Unimed',
        'plano-de-saude-hapvida': 'Plano Hapvida',
        'plano-de-saude-intermedica': 'Plano Intermédica',
        'plano-de-saude-porto-seguro-saude': 'Porto Seguro Saúde',
        'plano-de-saude-prevent-senior': 'Prevent Senior',
        'plano-de-saude-bradesco': 'Bradesco Saúde',
        'bradesco-dental': 'Bradesco Dental',
        'plano-de-saude-para-idosos': 'Plano para Idosos',
        'plano-de-saude-rj': 'Plano de Saúde RJ',
        'plano-odonto-empresarial': 'Odonto Empresarial',
        'simulacao-seguro-de-vida': 'Seguro de Vida',
        'bradesco-seguro-de-vida': 'Bradesco Seguro de Vida',
        'reembolso-amil': 'Reembolso Amil',
        'reembolso-sulamerica': 'Reembolso SulAmérica',
        'reembolso-intermedica': 'Reembolso Intermédica',
    }
    label = labels.get(slug)
    if label:
        return label
    # fallback: capitalize words
    return slug.replace('-', ' ').title()

def build_twitter_cards(og_title, og_description):
    return f'''    <!-- Twitter Cards (Módulo 8 - SEO Técnico: Next SEO) -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:site" content="@virtuacorretora">
    <meta name="twitter:title" content="{og_title}">
    <meta name="twitter:description" content="{og_description}">
    <meta name="twitter:image" content="{OG_IMAGE}">
    <meta name="twitter:image:alt" content="Virtua Corretora de Seguros - Planos de Saúde">'''

def build_breadcrumb_schema(page_label, canonical_url):
    return f'''    <!-- BreadcrumbList Schema (Módulo 6 - SEO On-Page: Next SEO) -->
    <script type="application/ld+json">
    {{
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {{
                "@type": "ListItem",
                "position": 1,
                "name": "Home",
                "item": "https://www.virtuacorretora.com.br/"
            }},
            {{
                "@type": "ListItem",
                "position": 2,
                "name": "{page_label}",
                "item": "{canonical_url}"
            }}
        ]
    }}
    </script>'''

def build_breadcrumb_html(page_label, canonical_url):
    """Navegação breadcrumb visual (SEO On-Page + acessibilidade)."""
    return f'''    <!-- Breadcrumb navegação visual -->
    <nav aria-label="Breadcrumb" style="background:#f8fafc; border-bottom:1px solid #e2e8f0; padding:10px 0;">
        <div class="container" style="max-width:1200px; margin:0 auto; padding:0 24px;">
            <ol style="list-style:none; margin:0; padding:0; display:flex; align-items:center; gap:6px; flex-wrap:wrap; font-size:13px; color:#64748b;">
                <li><a href="../index.html" style="color:#0066cc; text-decoration:none; font-weight:500;">Home</a></li>
                <li aria-hidden="true" style="color:#cbd5e1;">›</li>
                <li aria-current="page" style="color:#1e293b; font-weight:500;">{page_label}</li>
            </ol>
        </div>
    </nav>'''

# Títulos a corrigir (acima de 70 chars — curso: "acima de 60 deve ser feito com consciência")
TITLE_FIXES = {
    'plano-de-saude-amil': 'Plano de Saúde Amil | Preços 2026 | Virtua',
    'plano-de-saude-hapvida-recife': 'Hapvida Recife | Plano de Saúde 2026 | Virtua',
    'plano-de-saude-unimed': 'Plano de Saúde Unimed | Preços 2026 | Virtua',
    'medsenior-rj': 'MedSênior RJ | Plano para Idosos 2026 | Virtua',
    'plano-de-saude-hapvida': 'Hapvida | Plano de Saúde 2026 | Virtua Corretora',
    'plano-de-saude-samp-es': 'SAMP ES | Plano de Saúde 2026 | Virtua Corretora',
    'amil-macae': 'Amil Macaé | Plano de Saúde 2026 | Virtua Corretora',
    'plano-de-saude-para-idosos': 'Plano de Saúde para Idosos 2026 | Virtua',
    'plano-de-saude-sulamerica': 'Plano de Saúde SulAmérica | Preços 2026 | Virtua',
    'plano-de-saude-intermedica': 'Plano de Saúde Intermédica | Preços 2026 | Virtua',
    'amil-lagos': 'Amil Região dos Lagos | Plano de Saúde | Virtua',
    'amil-campos': 'Amil Campos dos Goytacazes | Plano de Saúde | Virtua',
}

def process_file(filepath):
    slug = os.path.basename(os.path.dirname(filepath))
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    original = html
    changed = False

    # ── 1. TWITTER CARDS ────────────────────────────────────────────────────────
    if 'twitter:card' not in html:
        og_title = get_og_title(html) or get_title(html)
        og_desc = get_og_description(html)
        twitter_block = build_twitter_cards(og_title, og_desc)
        # Insere após og:locale (última meta OG)
        html = re.sub(
            r'(<meta property="og:locale"[^>]*>)',
            r'\1\n' + twitter_block,
            html,
            count=1
        )
        changed = True
        print(f"  ✓ Twitter Cards adicionados")

    # ── 2. OG:IMAGE:ALT ────────────────────────────────────────────────────────
    if 'og:image:alt' not in html:
        html = re.sub(
            r'(<meta property="og:image:height"[^>]*>)',
            r'\1\n    <meta property="og:image:alt" content="Virtua Corretora de Seguros - Planos de Saúde">',
            html,
            count=1
        )
        changed = True
        print(f"  ✓ og:image:alt adicionado")

    # ── 3. CORRIGIR TÍTULO LONGO ────────────────────────────────────────────────
    if slug in TITLE_FIXES:
        new_title = TITLE_FIXES[slug]
        old_title = get_title(html)
        if len(old_title) > 60 and old_title != new_title:
            html = html.replace(f'<title>{old_title}</title>', f'<title>{new_title}</title>', 1)
            # Sincronizar og:title
            html = re.sub(
                r'(<meta property="og:title" content=")[^"]*(")',
                f'\\g<1>{new_title}\\2',
                html, count=1
            )
            # Sincronizar twitter:title (se já foi adicionado acima)
            html = re.sub(
                r'(<meta name="twitter:title" content=")[^"]*(")',
                f'\\g<1>{new_title}\\2',
                html, count=1
            )
            changed = True
            print(f"  ✓ Título encurtado: {len(old_title)} → {len(new_title)} chars")

    # ── 4. ORGANIZATION SCHEMA (subpáginas) ─────────────────────────────────────
    if 'InsuranceAgency' not in html:
        # Insere após </head> ou antes do primeiro <script type="application/ld+json">
        html = re.sub(
            r'(</head>)',
            ORG_SCHEMA + '\n\\1',
            html, count=1
        )
        changed = True
        print(f"  ✓ Organization/InsuranceAgency schema adicionado")

    # ── 5. BREADCRUMB SCHEMA ────────────────────────────────────────────────────
    if 'BreadcrumbList' not in html:
        canonical = get_canonical(html)
        h1 = get_h1(html)
        page_label = h1 or slug_to_label(slug)
        breadcrumb_schema = build_breadcrumb_schema(page_label, canonical)
        # Insere antes de </head>
        html = re.sub(
            r'(</head>)',
            breadcrumb_schema + '\n\\1',
            html, count=1
        )
        changed = True
        print(f"  ✓ BreadcrumbList schema adicionado: '{page_label}'")

    # ── 6. BREADCRUMB HTML VISUAL ───────────────────────────────────────────────
    # Insere após o header e antes da primeira section/div de conteúdo
    if 'aria-label="Breadcrumb"' not in html:
        canonical = get_canonical(html)
        h1 = get_h1(html)
        page_label = h1 or slug_to_label(slug)
        breadcrumb_html = build_breadcrumb_html(page_label, canonical)
        # Insere após </header>
        html = re.sub(
            r'(</header>)',
            r'\1\n' + breadcrumb_html,
            html, count=1
        )
        changed = True
        print(f"  ✓ Breadcrumb visual adicionado")

    # ── 7. BLOCO E-A-T (autor especialista) ────────────────────────────────────
    # Obrigatório para conteúdo de saúde (YMYL) — Módulo 5
    if 'eat-author-section' not in html:
        # Insere antes do footer
        html = re.sub(
            r'(<footer)',
            AUTHOR_BLOCK + '\n\n    \\1',
            html, count=1
        )
        changed = True
        print(f"  ✓ Bloco E-A-T autor/especialista adicionado")

    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        return True
    return False


def main():
    base = os.path.dirname(os.path.abspath(__file__))
    files = glob.glob(os.path.join(base, '*/index.html'))
    files.sort()

    print(f"Processando {len(files)} páginas...\n")
    updated = 0
    for f in files:
        slug = os.path.basename(os.path.dirname(f))
        # Pula index raiz (já tem schema próprio)
        if slug == 'redesign':
            continue
        print(f"[{slug}]")
        if process_file(f):
            updated += 1
        print()

    # Processa também o index.html raiz
    root_index = os.path.join(base, 'index.html')
    if os.path.exists(root_index):
        print("[index.html — página principal]")
        with open(root_index, 'r', encoding='utf-8') as f:
            html = f.read()
        changed = False
        if 'twitter:card' not in html:
            og_title = get_og_title(html) or get_title(html)
            og_desc = get_og_description(html)
            twitter_block = build_twitter_cards(og_title, og_desc)
            html = re.sub(
                r'(<meta property="og:locale"[^>]*>)',
                r'\1\n' + twitter_block,
                html, count=1
            )
            changed = True
            print("  ✓ Twitter Cards adicionados")
        if 'og:image:alt' not in html:
            html = re.sub(
                r'(<meta property="og:image:height"[^>]*>)',
                r'\1\n    <meta property="og:image:alt" content="Virtua Corretora de Seguros - Planos de Saúde">',
                html, count=1
            )
            changed = True
            print("  ✓ og:image:alt adicionado")
        if 'BreadcrumbList' not in html:
            breadcrumb_schema = '''    <script type="application/ld+json">
    {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {
                "@type": "ListItem",
                "position": 1,
                "name": "Home",
                "item": "https://www.virtuacorretora.com.br/"
            }
        ]
    }
    </script>'''
            html = re.sub(r'(</head>)', breadcrumb_schema + '\n\\1', html, count=1)
            changed = True
            print("  ✓ BreadcrumbList schema adicionado")
        if changed:
            with open(root_index, 'w', encoding='utf-8') as f:
                f.write(html)
            updated += 1

    print(f"\n✅ {updated} páginas atualizadas com melhorias do curso Next SEO")

if __name__ == '__main__':
    main()
