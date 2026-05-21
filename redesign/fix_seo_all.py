#!/usr/bin/env python3
"""
Fix SEO for all redesign pages:
- Add <meta name="robots" content="index, follow"> to all pages
- Add Open Graph tags (og:title, og:description, og:url, og:image, og:type, og:site_name)
- Fix/add canonical URLs (correct external canonicals in amil-*, add missing to root)
- Improve short meta descriptions (< 120 chars)
- Add JSON-LD FAQPage to amil-campos, amil-lagos, amil-macae
"""
import os
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_URL = "https://www.virtuacorretora.com.br"
OG_IMAGE = "https://www.virtuacorretora.com.br/wp-content/uploads/2023/11/cropped-virtua-corretora-de-planos-de-saude-1.webp"

# Improved/expanded meta descriptions for pages with < 120 chars
IMPROVED_DESCRIPTIONS = {
    "reembolso-amil": "Saiba como solicitar reembolso Amil em 2026: prazos, documentos necessários, valores e quais planos têm essa cobertura. Guia completo da Virtua Corretora.",
    "telefones-assim-saude": "Todos os telefones Assim Saúde atualizados em 2026: SAC, ouvidoria, emergência 24h, atendimento médico e contato comercial. Virtua Corretora.",
    "plano-de-saude-hapvida-manaus": "Plano de Saúde Hapvida em Manaus e Amazonas com preços 2026. Rede própria com hospitais e clínicas. Individual, familiar e empresarial. Cotação grátis.",
    "plano-de-saude-sulamerica-direto-salvador": "Plano SulAmérica Direto em Salvador e Bahia com preços 2026. O plano mais acessível da SulAmérica com rede regional. Individual e empresarial. Cotação grátis.",
    "rede-credenciada-sulamerica-odonto": "Rede credenciada SulAmérica Odonto 2026: encontre dentistas, clínicas e especialistas credenciados em todo o Brasil. Cobertura nacional. Virtua Corretora.",
    "plano-de-saude-bh-sulamerica-saude-direto": "Plano SulAmérica Direto em Belo Horizonte e Minas Gerais com preços 2026. Rede regional em BH, Contagem e RMBH. Individual e empresarial. Cotação grátis.",
    "plano-de-saude-sulamerica-direto-brasilia": "Plano SulAmérica Direto em Brasília e Distrito Federal com preços 2026. O plano mais acessível da SulAmérica com rede no DF. Cotação grátis.",
    "plano-de-saude-sulamerica-direto-sampa": "Plano SulAmérica Direto em São Paulo com preços 2026. Rede regional em SP com hospitais e laboratórios. Individual, familiar e empresarial. Cotação grátis.",
    "reembolso-intermedica": "Como solicitar reembolso Intermédica (GNDI) em 2026: prazos, documentos, valores por especialidade e quais planos têm cobertura. Guia completo.",
    "plano-de-saude-caberj-integral-saude": "Plano de Saúde CABERJ Integral no Rio de Janeiro com preços 2026. Individual, familiar e empresarial. Rede credenciada no RJ. Cotação grátis com corretor.",
    "plano-de-saude-hapvida-brasilia": "Plano de Saúde Hapvida em Brasília e Distrito Federal com preços 2026. Rede própria no DF. Individual, familiar e empresarial. Cotação grátis.",
    "plano-de-saude-hapvida-salvador": "Plano de Saúde Hapvida em Salvador e Bahia com preços 2026. Rede própria com hospitais e clínicas no estado. Individual e empresarial. Cotação grátis.",
    "plano-odonto-empresarial": "Plano odontológico empresarial 2026. Compare Bradesco Dental, Amil Dental, SulAmérica Odonto, OdontoPrev e mais. A partir de 2 vidas. Cotação grátis.",
    "telefones-amil-dental": "Telefones Amil Dental atualizados 2026: SAC, ouvidoria, emergência odontológica, rede credenciada e atendimento ao beneficiário. Virtua Corretora.",
    "telefones-intermedica": "Todos os telefones Intermédica GNDI atualizados 2026: SAC, ouvidoria, emergência 24h, boleto e contato comercial. Números para todo o Brasil.",
    "telefones-odontoprev": "Telefones OdontoPrev atualizados 2026: SAC, ouvidoria, emergência odontológica, rede credenciada e contato comercial para todo o Brasil.",
    "santa-helena-saude": "Plano de Saúde Santa Helena em Campos dos Goytacazes e Norte Fluminense com preços 2026. Individual, familiar e empresarial. Cotação grátis.",
    "plano-saude-unimed-macae": "Plano de Saúde Unimed em Macaé e região norte fluminense com preços 2026. Maior cooperativa médica do Brasil. Individual e empresarial. Cotação grátis.",
    "plano-de-saude-unimed-campos": "Plano de Saúde Unimed em Campos dos Goytacazes com preços 2026. Rede local com hospitais e clínicas na cidade. Individual e empresarial. Cotação grátis.",
    "simulacao-seguro-de-vida": "Faça uma simulação gratuita de seguro de vida 2026. Compare Bradesco, Porto Seguro, SulAmérica e outras seguradoras. Encontre o melhor custo-benefício.",
    "plano-de-saude-joao-pessoa-sulamerica": "Plano de Saúde SulAmérica em João Pessoa e Paraíba com preços 2026. Plano Direto com rede regional. Individual, familiar e empresarial. Cotação grátis.",
    "plano-de-saude-sulamerica-recife": "Plano de Saúde SulAmérica em Recife e Pernambuco com preços 2026. Plano Direto com rede regional. Individual, familiar e empresarial. Cotação grátis.",
    "rede-credenciada-sulamerica-odonto": "Rede credenciada SulAmérica Odonto 2026: encontre dentistas e clínicas credenciados em todo o Brasil. Saiba como acessar a rede. Cotação grátis.",
}

# Fixed/new canonical URLs (for pages with wrong or missing canonical)
CANONICAL_FIXES = {
    "amil-campos": f"{BASE_URL}/amil-campos/",
    "amil-lagos": f"{BASE_URL}/amil-lagos/",
    "amil-macae": f"{BASE_URL}/amil-macae/",
    "": f"{BASE_URL}/",  # root index.html
}

# JSON-LD FAQPage for pages that are missing it
JSONLD_ADDITIONS = {
    "amil-campos": '''<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [{
        "@type": "Question",
        "name": "Qual o telefone do corretor Amil em Campos dos Goytacazes?",
        "acceptedAnswer": {
            "@type": "Answer",
            "text": "Para contratar um plano Amil em Campos dos Goytacazes, ligue para (22) 99940-4840 (Virtua Corretora, corretor autorizado). Atendemos também pelo WhatsApp."
        }
    },{
        "@type": "Question",
        "name": "A Amil tem rede credenciada em Campos dos Goytacazes?",
        "acceptedAnswer": {
            "@type": "Answer",
            "text": "Sim. A Amil possui hospitais, clínicas e laboratórios credenciados em Campos dos Goytacazes e região norte fluminense. Consulte a rede completa no site da Amil."
        }
    },{
        "@type": "Question",
        "name": "Qual o plano Amil mais barato para Campos dos Goytacazes?",
        "acceptedAnswer": {
            "@type": "Answer",
            "text": "O Amil Fácil é a opção mais acessível, com rede regional e coparticipação. Solicite uma cotação para conhecer os valores atualizados para Campos dos Goytacazes."
        }
    },{
        "@type": "Question",
        "name": "Posso contratar Amil empresarial em Campos dos Goytacazes?",
        "acceptedAnswer": {
            "@type": "Answer",
            "text": "Sim. Planos empresariais e para MEI a partir de 2 vidas, com desconto de até 40% comparado ao plano individual. Entre em contato com a Virtua Corretora."
        }
    }]
}
</script>''',
    "amil-lagos": '''<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [{
        "@type": "Question",
        "name": "A Amil atende a Região dos Lagos do RJ?",
        "acceptedAnswer": {
            "@type": "Answer",
            "text": "Sim. A Amil possui rede credenciada em Cabo Frio, Búzios, Arraial do Cabo, Araruama, São Pedro da Aldeia e outras cidades da Região dos Lagos."
        }
    },{
        "@type": "Question",
        "name": "Qual o telefone do corretor Amil na Região dos Lagos?",
        "acceptedAnswer": {
            "@type": "Answer",
            "text": "Para contratar um plano Amil na Região dos Lagos, ligue para (22) 99940-4840 (Virtua Corretora, corretor autorizado). Atendemos pelo WhatsApp também."
        }
    },{
        "@type": "Question",
        "name": "Quais planos Amil estão disponíveis na Região dos Lagos?",
        "acceptedAnswer": {
            "@type": "Answer",
            "text": "A Amil oferece planos individuais, familiares, empresariais e para MEI na Região dos Lagos. Os planos variam por abrangência e cobertura. Solicite cotação grátis."
        }
    },{
        "@type": "Question",
        "name": "A Amil cobre Cabo Frio e Búzios?",
        "acceptedAnswer": {
            "@type": "Answer",
            "text": "Sim. Cabo Frio e Armação dos Búzios estão na área de cobertura da rede Amil para a Região dos Lagos. Consulte clínicas e hospitais disponíveis na área."
        }
    }]
}
</script>''',
    "amil-macae": '''<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [{
        "@type": "Question",
        "name": "A Amil tem cobertura em Macaé?",
        "acceptedAnswer": {
            "@type": "Answer",
            "text": "Sim. A Amil possui hospitais, clínicas e laboratórios credenciados em Macaé e na região norte fluminense do Rio de Janeiro."
        }
    },{
        "@type": "Question",
        "name": "Qual o telefone do corretor Amil em Macaé?",
        "acceptedAnswer": {
            "@type": "Answer",
            "text": "Para contratar um plano Amil em Macaé, ligue para (22) 99940-4840 (Virtua Corretora, corretor autorizado). Atendemos pelo WhatsApp também."
        }
    },{
        "@type": "Question",
        "name": "Quais planos Amil estão disponíveis em Macaé?",
        "acceptedAnswer": {
            "@type": "Answer",
            "text": "Em Macaé estão disponíveis planos individuais, familiares, para MEI e empresariais. O plano mais acessível é o Amil Fácil com rede regional."
        }
    },{
        "@type": "Question",
        "name": "Posso contratar Amil empresarial em Macaé?",
        "acceptedAnswer": {
            "@type": "Answer",
            "text": "Sim. Planos empresariais Amil a partir de 2 vidas, com economia de até 40% em relação ao plano individual. Entre em contato com a Virtua Corretora."
        }
    }]
}
</script>''',
}


def get_slug(filepath):
    """Returns the URL slug from the file path."""
    parts = filepath.replace(BASE_DIR, "").split(os.sep)
    # parts[0] = '', parts[1] = subdir, parts[2] = 'index.html'
    if len(parts) == 3 and parts[2] == "index.html":
        return parts[1]
    if len(parts) == 2 and parts[1] == "index.html":
        return ""  # root
    return None


def extract_meta(content, name_attr, attr_name="name"):
    """Extract meta tag content."""
    pattern = rf'<meta\s+{attr_name}="{re.escape(name_attr)}"\s+content="([^"]*)"'
    m = re.search(pattern, content, re.IGNORECASE)
    if not m:
        pattern = rf'<meta\s+content="([^"]*)"\s+{attr_name}="{re.escape(name_attr)}"'
        m = re.search(pattern, content, re.IGNORECASE)
    return m.group(1) if m else ""


def extract_title(content):
    m = re.search(r"<title>([^<]+)</title>", content, re.IGNORECASE)
    return m.group(1).strip() if m else ""


def has_tag(content, pattern):
    return bool(re.search(pattern, content, re.IGNORECASE))


def fix_file(filepath):
    slug = get_slug(filepath)
    if slug is None:
        return False

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    original = content
    changed = False

    # ---------- 1. Fix/add canonical ----------
    canonical_url = CANONICAL_FIXES.get(slug)
    if canonical_url:
        # Replace existing canonical (any URL) with correct one
        new_canonical = f'<link rel="canonical" href="{canonical_url}">'
        if re.search(r'<link\s+rel="canonical"', content, re.IGNORECASE):
            content = re.sub(
                r'<link\s+rel="canonical"\s+href="[^"]*">',
                new_canonical,
                content,
                flags=re.IGNORECASE,
            )
        else:
            # Add after meta description or after viewport meta
            content = re.sub(
                r'(<meta\s+name="description"[^>]*>)',
                rf'\1\n    {new_canonical}',
                content,
                count=1,
                flags=re.IGNORECASE,
            )
    else:
        # Verify existing canonical has www (some may have non-www)
        existing_canonical = re.search(
            r'<link\s+rel="canonical"\s+href="([^"]*)"', content, re.IGNORECASE
        )
        if existing_canonical:
            existing_url = existing_canonical.group(1)
            # Normalize: ensure www prefix
            if "virtuacorretora.com.br" in existing_url and "//virtuacorretora" in existing_url:
                fixed_url = existing_url.replace("//virtuacorretora", "//www.virtuacorretora")
                content = content.replace(existing_url, fixed_url)

    # ---------- 2. Add robots meta if missing ----------
    if not has_tag(content, r'<meta\s+name="robots"'):
        robots_tag = '<meta name="robots" content="index, follow">'
        # Insert right after viewport meta
        content = re.sub(
            r'(<meta\s+name="viewport"[^>]*>)',
            rf'\1\n    {robots_tag}',
            content,
            count=1,
            flags=re.IGNORECASE,
        )
        if not has_tag(content, r'<meta\s+name="robots"'):
            # Fallback: insert after charset meta
            content = re.sub(
                r'(<meta\s+charset=[^>]*>)',
                rf'\1\n    {robots_tag}',
                content,
                count=1,
                flags=re.IGNORECASE,
            )

    # ---------- 3. Improve short meta descriptions ----------
    improved_desc = IMPROVED_DESCRIPTIONS.get(slug)
    if improved_desc:
        content = re.sub(
            r'(<meta\s+name="description"\s+content=")[^"]*(")',
            rf'\g<1>{improved_desc}\g<2>',
            content,
            count=1,
            flags=re.IGNORECASE,
        )

    # ---------- 4. Add Open Graph tags if missing ----------
    if not has_tag(content, r'<meta\s+property="og:title"'):
        title = extract_title(content)
        description = extract_meta(content, "description")
        # Determine canonical URL for this page
        if slug in CANONICAL_FIXES:
            page_url = CANONICAL_FIXES[slug]
        else:
            m = re.search(r'<link\s+rel="canonical"\s+href="([^"]*)"', content, re.IGNORECASE)
            page_url = m.group(1) if m else f"{BASE_URL}/{slug}/"

        og_tags = f"""
    <!-- Open Graph -->
    <meta property="og:type" content="website">
    <meta property="og:site_name" content="Virtua Corretora de Seguros">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{description}">
    <meta property="og:url" content="{page_url}">
    <meta property="og:image" content="{OG_IMAGE}">
    <meta property="og:image:width" content="1200">
    <meta property="og:image:height" content="630">
    <meta property="og:locale" content="pt_BR">"""

        # Insert before </head> or before first <style> or before first <link rel="stylesheet">
        inserted = False
        for pattern in [
            r'(<link\s+rel="stylesheet"[^>]*>)',
            r'(<style\b)',
            r'(</head>)',
        ]:
            m = re.search(pattern, content, re.IGNORECASE)
            if m:
                content = content[: m.start()] + og_tags + "\n" + content[m.start() :]
                inserted = True
                break
        if not inserted:
            content = content.replace("</head>", og_tags + "\n</head>")

    # ---------- 5. Add JSON-LD for amil-* pages missing it ----------
    if slug in JSONLD_ADDITIONS and not has_tag(content, r'application/ld\+json'):
        jsonld = JSONLD_ADDITIONS[slug]
        # Insert before </head>
        # Find first <style> or </head>
        m = re.search(r'(<style\b)', content, re.IGNORECASE)
        if m:
            content = content[: m.start()] + jsonld + "\n" + content[m.start() :]
        else:
            content = content.replace("</head>", jsonld + "\n</head>")

    if content != original:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        return True
    return False


def main():
    html_files = []

    # Root index.html
    root_index = os.path.join(BASE_DIR, "index.html")
    if os.path.exists(root_index):
        html_files.append(root_index)

    # All subdirectory index.html
    for entry in sorted(os.scandir(BASE_DIR), key=lambda e: e.name):
        if entry.is_dir():
            idx = os.path.join(entry.path, "index.html")
            if os.path.exists(idx):
                html_files.append(idx)

    fixed = []
    unchanged = []
    for f in html_files:
        if fix_file(f):
            rel = f.replace(BASE_DIR + os.sep, "")
            fixed.append(rel)
        else:
            rel = f.replace(BASE_DIR + os.sep, "")
            unchanged.append(rel)

    print(f"\n✅ FIXED ({len(fixed)} pages):")
    for p in fixed:
        print(f"   {p}")

    if unchanged:
        print(f"\n— Unchanged ({len(unchanged)} pages):")
        for p in unchanged:
            print(f"   {p}")


if __name__ == "__main__":
    main()
