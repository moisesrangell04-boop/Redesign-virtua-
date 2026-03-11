#!/usr/bin/env python3
"""
Gerador de páginas de operadoras para o novo site da Virtua Corretora.
Gera páginas HTML estáticas no estilo do redesign, mantendo as mesmas URLs do WordPress.
"""
import os

# ============================================================
# TEMPLATE HTML
# ============================================================
TEMPLATE = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{meta_description}">
    <link rel="canonical" href="https://www.virtuacorretora.com.br/{slug}/">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="../style.css">
    {schema_markup}
    <style>
        .op-hero {{
            background: {hero_gradient};
            padding: 120px 0 80px;
            color: white;
            text-align: center;
            position: relative;
            overflow: hidden;
        }}
        .op-hero::before {{
            content: '';
            position: absolute;
            top: -40%;
            right: -20%;
            width: 600px;
            height: 600px;
            background: rgba(255,255,255,0.05);
            border-radius: 50%;
        }}
        .op-hero h1 {{
            font-size: clamp(32px, 4.5vw, 52px);
            margin-bottom: 20px;
            font-weight: 800;
            line-height: 1.15;
        }}
        .op-hero .subtitle {{
            font-size: 18px;
            opacity: 0.92;
            max-width: 680px;
            margin: 0 auto 36px;
            line-height: 1.7;
        }}
        .op-hero .hero-badges {{
            display: flex;
            gap: 16px;
            justify-content: center;
            flex-wrap: wrap;
            margin-bottom: 36px;
        }}
        .op-hero .badge {{
            background: rgba(255,255,255,0.18);
            backdrop-filter: blur(8px);
            border: 1px solid rgba(255,255,255,0.25);
            padding: 8px 20px;
            border-radius: 100px;
            font-size: 14px;
            font-weight: 600;
        }}
        .op-hero .hero-ctas {{
            display: flex;
            gap: 16px;
            justify-content: center;
            flex-wrap: wrap;
        }}
        .op-hero .btn-hero {{
            padding: 16px 36px;
            border-radius: 12px;
            font-weight: 700;
            font-size: 16px;
            text-decoration: none;
            transition: all 0.3s;
        }}
        .op-hero .btn-hero-primary {{
            background: white;
            color: {hero_text_color};
        }}
        .op-hero .btn-hero-primary:hover {{ transform: translateY(-2px); box-shadow: 0 8px 24px rgba(0,0,0,0.2); }}
        .op-hero .btn-hero-outline {{
            border: 2px solid rgba(255,255,255,0.6);
            color: white;
            background: transparent;
        }}
        .op-hero .btn-hero-outline:hover {{ background: rgba(255,255,255,0.15); }}

        .section {{ padding: 80px 0; }}
        .section-alt {{ background: var(--gray-50); }}
        .section-title {{ font-size: clamp(26px, 3vw, 36px); font-weight: 800; margin-bottom: 16px; color: var(--gray-900); }}
        .section-subtitle {{ color: var(--gray-600); font-size: 17px; max-width: 640px; margin: 0 auto 48px; line-height: 1.7; }}

        .benefits-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 24px;
            max-width: 1000px;
            margin: 0 auto;
        }}
        .benefit-card {{
            background: white;
            border-radius: 16px;
            padding: 32px;
            border: 1px solid var(--gray-200);
            transition: all 0.3s;
        }}
        .benefit-card:hover {{ transform: translateY(-4px); box-shadow: 0 12px 32px rgba(0,0,0,0.08); }}
        .benefit-icon {{ font-size: 36px; margin-bottom: 16px; }}
        .benefit-card h3 {{ font-size: 18px; font-weight: 700; margin-bottom: 10px; color: var(--gray-900); }}
        .benefit-card p {{ color: var(--gray-600); font-size: 15px; line-height: 1.65; }}

        .plans-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 24px;
            max-width: 1000px;
            margin: 0 auto;
        }}
        .plan-card {{
            background: white;
            border-radius: 16px;
            padding: 36px;
            border: 1px solid var(--gray-200);
            position: relative;
            overflow: hidden;
        }}
        .plan-card.featured {{
            border-color: {accent_color};
            box-shadow: 0 0 0 1px {accent_color};
        }}
        .plan-card.featured::before {{
            content: 'Mais Popular';
            position: absolute;
            top: 16px;
            right: -32px;
            background: {accent_color};
            color: white;
            font-size: 12px;
            font-weight: 700;
            padding: 4px 40px;
            transform: rotate(45deg);
        }}
        .plan-card h3 {{ font-size: 20px; font-weight: 700; margin-bottom: 8px; color: var(--gray-900); }}
        .plan-card .plan-type {{ font-size: 14px; color: var(--gray-500); margin-bottom: 16px; }}
        .plan-card ul {{ list-style: none; padding: 0; margin-bottom: 24px; }}
        .plan-card li {{ padding: 8px 0; padding-left: 28px; position: relative; color: var(--gray-600); font-size: 15px; }}
        .plan-card li::before {{ content: "✓"; position: absolute; left: 0; color: {accent_color}; font-weight: bold; }}

        .network-section {{ text-align: center; }}
        .network-logos {{
            display: flex;
            flex-wrap: wrap;
            gap: 20px;
            justify-content: center;
            margin-top: 32px;
        }}
        .network-tag {{
            background: white;
            border: 1px solid var(--gray-200);
            padding: 12px 24px;
            border-radius: 12px;
            font-weight: 600;
            color: var(--gray-700);
            font-size: 14px;
        }}

        .op-faq {{ max-width: 800px; margin: 0 auto; }}
        .op-faq-item {{ background: white; border-radius: 12px; margin-bottom: 12px; border: 1px solid var(--gray-200); overflow: hidden; }}
        .op-faq-question {{
            padding: 20px 24px;
            font-weight: 600;
            cursor: pointer;
            display: flex;
            justify-content: space-between;
            align-items: center;
            color: var(--gray-800);
        }}
        .op-faq-question:hover {{ color: {accent_color}; }}
        .op-faq-question::after {{ content: '+'; font-size: 24px; color: var(--gray-400); transition: transform 0.3s; }}
        .op-faq-item.active .op-faq-question::after {{ transform: rotate(45deg); }}
        .op-faq-answer {{ padding: 0 24px; max-height: 0; overflow: hidden; transition: all 0.3s; }}
        .op-faq-item.active .op-faq-answer {{ padding: 0 24px 20px; max-height: 500px; }}
        .op-faq-answer p {{ color: var(--gray-600); line-height: 1.7; }}

        .cta-banner {{
            background: {hero_gradient};
            padding: 80px 0;
            text-align: center;
            color: white;
        }}
        .cta-banner h2 {{ font-size: clamp(28px, 3.5vw, 40px); font-weight: 800; margin-bottom: 16px; }}
        .cta-banner p {{ font-size: 18px; opacity: 0.9; margin-bottom: 36px; max-width: 540px; margin-left: auto; margin-right: auto; }}

        @media (max-width: 768px) {{
            .op-hero {{ padding: 100px 0 60px; }}
            .plans-grid {{ grid-template-columns: 1fr; }}
        }}
    </style>
</head>
<body>
    <!-- Top Bar -->
    <div class="top-bar">
        <div class="container top-bar-inner">
            <div class="top-bar-contact">
                <div class="top-bar-phones">
                    <a href="tel:+5522999404840" class="top-bar-link">
                        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"/></svg> (22) 99940-4840
                    </a>
                </div>
                <a href="https://wa.me/5522999404840" target="_blank" class="top-bar-link whatsapp-link">WhatsApp</a>
            </div>
            <div class="top-bar-info">
                <span><a href="../index.html" style="color:var(--white); opacity:0.9; text-decoration:none; display:flex; align-items:center; gap:6px; font-weight:500;">
                    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="19" y1="12" x2="5" y2="12"/><polyline points="12 19 5 12 12 5"/></svg>
                    Voltar para a Home
                </a></span>
            </div>
        </div>
    </div>

    <!-- Header -->
    <header class="header">
        <div class="container header-inner">
            <a href="../index.html" class="logo">
                <img src="https://www.virtuacorretora.com.br/wp-content/uploads/2023/11/cropped-virtua-corretora-de-planos-de-saude-1.webp" alt="Virtua Logo" style="height: 32px; width: auto; object-fit: contain;">
                <span class="logo-text">virtua<small>CORRETORA DE SEGUROS</small></span>
            </a>
            <a href="https://wa.me/5522999404840" target="_blank" class="btn btn-primary header-cta">Fale pelo WhatsApp</a>
        </div>
    </header>

    <!-- Hero Section -->
    <section class="op-hero">
        <div class="container">
            <div class="hero-badges">
                {hero_badges}
            </div>
            <h1>{h1}</h1>
            <p class="subtitle">{hero_subtitle}</p>
            <div class="hero-ctas">
                <a href="https://wa.me/5522999404840?text={whatsapp_msg}" target="_blank" class="btn-hero btn-hero-primary">Solicitar Cotação pelo WhatsApp →</a>
                <a href="tel:+5522999404840" class="btn-hero btn-hero-outline">Ligar: (22) 99940-4840</a>
            </div>
        </div>
    </section>

    <!-- Benefits -->
    <section class="section">
        <div class="container" style="text-align:center;">
            <h2 class="section-title">{benefits_title}</h2>
            <p class="section-subtitle">{benefits_subtitle}</p>
            <div class="benefits-grid">
                {benefits_html}
            </div>
        </div>
    </section>

    <!-- Plans -->
    <section class="section section-alt">
        <div class="container" style="text-align:center;">
            <h2 class="section-title">{plans_title}</h2>
            <p class="section-subtitle">{plans_subtitle}</p>
            <div class="plans-grid">
                {plans_html}
            </div>
        </div>
    </section>

    <!-- Network -->
    <section class="section network-section">
        <div class="container">
            <h2 class="section-title">{network_title}</h2>
            <p class="section-subtitle">{network_subtitle}</p>
            <div class="network-logos">
                {network_html}
            </div>
        </div>
    </section>

    <!-- FAQ -->
    <section class="section section-alt">
        <div class="container" style="text-align:center;">
            <h2 class="section-title">Perguntas Frequentes</h2>
            <p class="section-subtitle">Tire suas dúvidas sobre {operator_name}</p>
            <div class="op-faq">
                {faq_html}
            </div>
        </div>
    </section>

    <!-- CTA Final -->
    <section class="cta-banner">
        <div class="container">
            <h2>Solicite sua cotação {operator_name}</h2>
            <p>Fale com um corretor especializado e receba uma proposta personalizada sem compromisso.</p>
            <div style="display:flex; gap:16px; justify-content:center; flex-wrap:wrap;">
                <a href="https://wa.me/5522999404840?text={whatsapp_msg}" target="_blank" class="btn-hero btn-hero-primary" style="background:white; color:#1a1a2e;">Falar no WhatsApp →</a>
                <a href="tel:+5522999404840" class="btn-hero btn-hero-outline">Ligar Agora</a>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="footer" style="margin-top: 0;">
        <div class="container text-center">
            <p style="color: var(--gray-500);">© 2026 Virtua Corretora de Seguros. Todos os direitos reservados. SUSEP nº {susep}</p>
        </div>
    </footer>

    <script>
    document.querySelectorAll('.op-faq-question').forEach(q => {{
        q.addEventListener('click', () => {{
            q.parentElement.classList.toggle('active');
        }});
    }});
    </script>
</body>
</html>"""

# ============================================================
# Helper functions
# ============================================================
def make_badges(badges):
    return '\n'.join(f'<span class="badge">{b}</span>' for b in badges)

def make_benefits(benefits):
    html = ''
    for b in benefits:
        html += f"""<div class="benefit-card">
    <div class="benefit-icon">{b['icon']}</div>
    <h3>{b['title']}</h3>
    <p>{b['desc']}</p>
</div>\n"""
    return html

def make_plans(plans, accent):
    html = ''
    for p in plans:
        featured = ' featured' if p.get('featured') else ''
        items = '\n'.join(f'<li>{i}</li>' for i in p['items'])
        html += f"""<div class="plan-card{featured}">
    <h3>{p['name']}</h3>
    <p class="plan-type">{p['type']}</p>
    <ul>{items}</ul>
    <a href="https://wa.me/5522999404840?text=Olá, gostaria de uma cotação do plano {p['name']}" target="_blank" class="btn btn-primary" style="width:100%; text-align:center;">Solicitar Cotação</a>
</div>\n"""
    return html

def make_network(items):
    return '\n'.join(f'<span class="network-tag">{i}</span>' for i in items)

def make_faq(faqs):
    html = ''
    for f in faqs:
        html += f"""<div class="op-faq-item">
    <div class="op-faq-question">{f['q']}</div>
    <div class="op-faq-answer"><p>{f['a']}</p></div>
</div>\n"""
    return html

def make_faq_schema(faqs, page_url):
    items = []
    for f in faqs:
        items.append(f'''{{
            "@type": "Question",
            "name": "{f['q']}",
            "acceptedAnswer": {{
                "@type": "Answer",
                "text": "{f['a'].replace('"', '\\"')}"
            }}
        }}''')
    return f'''<script type="application/ld+json">
{{
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [{','.join(items)}]
}}
</script>'''

# ============================================================
# PAGE DATA - Each dict defines one operator page
# ============================================================
PAGES = [
    {
        "slug": "plano-de-saude-intermedica",
        "title": "Plano de Saúde Intermédica | Tabela de Preços 2026 | Virtua Corretora",
        "meta_description": "Plano de Saúde NotreDame Intermédica com preços atualizados em 2026. Individual, empresarial e MEI. Cotação gratuita com corretor autorizado. Rede credenciada RJ e SP.",
        "h1": "Plano de Saúde<br>NotreDame Intermédica",
        "operator_name": "Intermédica",
        "hero_subtitle": "A Intermédica (GNDI) oferece planos individuais, empresariais e para MEI com ampla rede credenciada no Rio de Janeiro e em São Paulo. Solicite uma cotação e economize até 40% na contratação.",
        "hero_gradient": "linear-gradient(135deg, #1a1a3e 0%, #2d2d6b 50%, #4a3f8f 100%)",
        "hero_text_color": "#1a1a3e",
        "accent_color": "#4a3f8f",
        "badges": ["Corretor Autorizado", "Preços 2026", "RJ e SP", "Individual e Empresarial"],
        "whatsapp_msg": "Olá, gostaria de uma cotação do plano de saúde Intermédica",
        "benefits_title": "Por que escolher a Intermédica?",
        "benefits_subtitle": "A NotreDame Intermédica é uma das maiores operadoras de saúde do Brasil, com rede própria de hospitais e laboratórios.",
        "benefits": [
            {"icon": "🏥", "title": "31 Hospitais Próprios", "desc": "Rede própria com hospitais de alta complexidade no RJ e SP, além de centros clínicos e prontos-socorros."},
            {"icon": "💰", "title": "Economia de até 40%", "desc": "Planos empresariais e para MEI com valores até 40% menores que os planos individuais."},
            {"icon": "📱", "title": "Telemedicina GNDI Easy", "desc": "Consultas online em mais de 27 especialidades, incluindo atendimento psicológico, direto pelo app."},
            {"icon": "💊", "title": "Interclube Descontos", "desc": "Programa de descontos em farmácias, academias, clínicas estéticas e muito mais para todos os planos."},
            {"icon": "🛡️", "title": "Limitador COPAY", "desc": "Teto de coparticipação exclusivo: mesmo nos meses de maior uso, sua mensalidade não dispara."},
            {"icon": "🌍", "title": "Cobertura Nacional", "desc": "Planos com abrangência regional, estadual ou nacional com possibilidade de reembolso."},
        ],
        "plans_title": "Planos NotreDame Intermédica",
        "plans_subtitle": "Conheça as opções disponíveis para o Rio de Janeiro e São Paulo.",
        "plans": [
            {
                "name": "Smart 200",
                "type": "Regional · Enfermaria",
                "items": [
                    "Abrangência regional (Grande Rio ou regiões SP)",
                    "Acomodação em quarto coletivo",
                    "Coparticipação parcial",
                    "Rede credenciada regional",
                    "Programa de medicina preventiva",
                ],
            },
            {
                "name": "Smart 500",
                "type": "Estadual · Enfermaria ou Apartamento",
                "featured": True,
                "items": [
                    "Abrangência estadual (RJ ou SP completo)",
                    "Opção enfermaria ou apartamento",
                    "Inclui interior: Campos, Cabo Frio, Petrópolis",
                    "Rede credenciada ampla",
                    "Telemedicina GNDI Easy inclusa",
                ],
            },
            {
                "name": "Advance 600",
                "type": "Nacional · Apartamento",
                "items": [
                    "Abrangência nacional em todo Brasil",
                    "Acomodação em apartamento",
                    "Reembolso para atendimento fora da rede",
                    "Interclube com descontos exclusivos",
                    "Programas de medicina preventiva avançados",
                ],
            },
        ],
        "network_title": "Rede Credenciada Intermédica",
        "network_subtitle": "Destaques da rede credenciada no Rio de Janeiro e São Paulo, incluindo hospitais próprios.",
        "network": [
            "Hospital Caxias D'Or", "Hospital São Lucas", "Hospital GNDI Barra",
            "Hospital GNDI Penha", "Hospital GNDI São Bernardo", "Hospital GNDI Guarulhos",
            "Hospital GNDI Osasco", "Hospital GNDI Santo André", "Laboratórios próprios GNDI",
            "Centros Clínicos GNDI", "Prontos-Socorros 24h", "Clínicas especializadas"
        ],
        "faqs": [
            {"q": "Qual o telefone da Intermédica?", "a": "Para contratar, ligue para (22) 99940-4840. Para clientes, o SAC é 4090-1750 ou 0800 409 1750."},
            {"q": "A Intermédica atende no interior do RJ?", "a": "Sim! O plano Smart 500 atende em Campos, Cabo Frio, Volta Redonda, Petrópolis e Teresópolis."},
            {"q": "Empresas MEI podem contratar?", "a": "Sim. Com CNPJ ativo há mais de 6 meses, a partir de 2 vidas, com economia de até 40% vs. plano individual."},
            {"q": "Como funciona a coparticipação?", "a": "Nos planos coparticipativos, a mensalidade é em média 25% menor. Ao usar o plano, paga-se uma taxa por atendimento, com teto máximo mensal (COPAY)."},
            {"q": "A Intermédica tem telemedicina?", "a": "Sim, pelo app GNDI Easy com consultas em mais de 27 especialidades, incluindo psicologia, com receitas digitais válidas em todo Brasil."},
            {"q": "Como emitir 2ª via do boleto?", "a": "Acesse gndi.com.br na área do beneficiário. Para planos por adesão, use o site da Qualicorp informando o CPF do titular."},
        ],
    },
    {
        "slug": "plano-de-saude-amil",
        "title": "Plano de Saúde Amil | Tabela de Preços 2026 | Virtua Corretora",
        "meta_description": "Plano de Saúde Amil com preços atualizados 2026. Individual, familiar, empresarial e dental. Cotação grátis com corretor autorizado. Ampla rede credenciada.",
        "h1": "Plano de Saúde Amil",
        "operator_name": "Amil",
        "hero_subtitle": "A Amil é uma das maiores operadoras de saúde do Brasil, com planos para todos os perfis: individual, familiar, empresarial e dental. Rede credenciada premium com os melhores hospitais.",
        "hero_gradient": "linear-gradient(135deg, #003366 0%, #004d99 50%, #0066cc 100%)",
        "hero_text_color": "#003366",
        "accent_color": "#0066cc",
        "badges": ["Corretor Autorizado", "Preços 2026", "Nacional", "Dental Incluso"],
        "whatsapp_msg": "Olá, gostaria de uma cotação do plano de saúde Amil",
        "benefits_title": "Por que escolher a Amil?",
        "benefits_subtitle": "A Amil oferece uma das maiores redes credenciadas do país, com hospitais referência e atendimento de excelência.",
        "benefits": [
            {"icon": "🏥", "title": "Rede Credenciada Premium", "desc": "Acesso aos principais hospitais e clínicas do Brasil, incluindo Hospital Samaritano, Copa D'Or e Rede D'Or."},
            {"icon": "🦷", "title": "Amil Dental", "desc": "Opção de plano odontológico integrado com cobertura completa para prevenção e tratamentos."},
            {"icon": "📱", "title": "Amil Clínica Digital", "desc": "Telemedicina com consultas online, prescrição digital e agendamento pelo app."},
            {"icon": "🌍", "title": "Abrangência Nacional", "desc": "Planos com cobertura em todo o Brasil e possibilidade de utilização no exterior."},
            {"icon": "👨‍👩‍👧‍👦", "title": "Planos Familiares", "desc": "Opções para famílias com condições especiais e inclusão de dependentes até 24 anos."},
            {"icon": "🏢", "title": "PME e MEI", "desc": "Planos empresariais a partir de 2 vidas com economia significativa na mensalidade."},
        ],
        "plans_title": "Planos Amil Disponíveis",
        "plans_subtitle": "Conheça as principais opções de planos de saúde Amil.",
        "plans": [
            {
                "name": "Amil Fácil",
                "type": "Regional · Enfermaria",
                "items": [
                    "Plano acessível com rede própria Amil",
                    "Acomodação em enfermaria",
                    "Coparticipação parcial",
                    "Programa Saúde Ativa",
                    "Telemedicina inclusa",
                ],
            },
            {
                "name": "Amil 400",
                "type": "Nacional · Enfermaria ou Apartamento",
                "featured": True,
                "items": [
                    "Abrangência nacional completa",
                    "Rede credenciada ampla e premium",
                    "Opção de acomodação em apartamento",
                    "Amil Clínica Digital",
                    "Descontos em farmácias parceiras",
                ],
            },
            {
                "name": "Amil 750",
                "type": "Nacional · Apartamento Premium",
                "items": [
                    "Rede credenciada premium (Copa D'Or, Samaritano)",
                    "Acomodação em apartamento individual",
                    "Reembolso diferenciado",
                    "Cobertura internacional",
                    "Acesso a médicos renomados",
                ],
            },
        ],
        "network_title": "Rede Credenciada Amil",
        "network_subtitle": "Tenha acesso aos melhores hospitais e clínicas do Brasil.",
        "network": [
            "Hospital Samaritano", "Copa D'Or", "Rede D'Or São Luiz",
            "Hospital Vitória", "Hospital São Lucas", "Hospital Badim",
            "Americas Medical City", "Laboratórios Dasa", "Rede Labs a+",
            "Centros de Diagnóstico", "Clínicas Especializadas", "Rede Própria Amil"
        ],
        "faqs": [
            {"q": "Qual o telefone da Amil para contratação?", "a": "Para contratar um plano Amil, ligue para (22) 99940-4840 (corretor autorizado Virtua). SAC Amil: 0800 730 0099."},
            {"q": "A Amil tem plano dental?", "a": "Sim! A Amil Dental oferece planos odontológicos com cobertura completa, desde prevenção até tratamentos como ortodontia e prótese."},
            {"q": "Qual o plano Amil mais barato?", "a": "O Amil Fácil é a opção mais acessível, com rede regional e coparticipação. Solicite uma cotação para conhecer os valores atualizados."},
            {"q": "Posso contratar Amil para minha empresa?", "a": "Sim. Planos empresariais e para MEI a partir de 2 vidas, com economia de até 40% comparado ao plano individual."},
            {"q": "A Amil tem telemedicina?", "a": "Sim, através da Amil Clínica Digital com consultas online em diversas especialidades pelo app Amil."},
            {"q": "Como emitir 2ª via do boleto Amil?", "a": "Acesse amil.com.br na área do cliente ou pelo app Amil. Para planos por adesão, consulte a administradora do seu plano."},
        ],
    },
    {
        "slug": "plano-de-saude-sulamerica",
        "title": "Plano de Saúde SulAmérica | Tabela de Preços 2026 | Virtua Corretora",
        "meta_description": "Plano de Saúde SulAmérica com preços 2026. Planos Direto, Especial e Executivo. Individual e empresarial. Cotação grátis com corretor autorizado.",
        "h1": "Plano de Saúde<br>SulAmérica",
        "operator_name": "SulAmérica",
        "hero_subtitle": "A SulAmérica é referência em saúde, com planos completos e a melhor rede credenciada do mercado. Planos Direto, Especial e Executivo para pessoa física e empresas.",
        "hero_gradient": "linear-gradient(135deg, #003d7a 0%, #0057a8 50%, #0072d6 100%)",
        "hero_text_color": "#003d7a",
        "accent_color": "#0072d6",
        "badges": ["Corretor Autorizado", "Preços 2026", "Nacional", "Referência em Saúde"],
        "whatsapp_msg": "Olá, gostaria de uma cotação do plano de saúde SulAmérica",
        "benefits_title": "Por que escolher a SulAmérica?",
        "benefits_subtitle": "Líder em saúde suplementar no Brasil, a SulAmérica oferece planos com a mais ampla rede credenciada e atendimento de excelência.",
        "benefits": [
            {"icon": "⭐", "title": "Melhor Avaliação ANS", "desc": "Consistentemente entre as operadoras com melhor avaliação pela Agência Nacional de Saúde Suplementar."},
            {"icon": "🏥", "title": "Rede Premium", "desc": "Acesso aos melhores hospitais, como Albert Einstein, Sírio-Libanês e Rede D'Or."},
            {"icon": "💳", "title": "Reembolso Diferenciado", "desc": "Opções de reembolso para consultas e procedimentos fora da rede credenciada."},
            {"icon": "📱", "title": "SulAmérica Saúde Ativa", "desc": "App com telemedicina, psicólogo online, nutricionista e programas de bem-estar."},
            {"icon": "🔄", "title": "Portabilidade Facilitada", "desc": "Aceita portabilidade de outras operadoras sem carência para coberturas contratadas."},
            {"icon": "🏢", "title": "Planos Empresariais", "desc": "Opções para empresas de todos os portes com condições e preços diferenciados."},
        ],
        "plans_title": "Planos SulAmérica Saúde",
        "plans_subtitle": "Conheça os planos disponíveis para pessoa física e empresas.",
        "plans": [
            {
                "name": "SulAmérica Direto",
                "type": "Regional · Enfermaria",
                "items": [
                    "Plano econômico com rede regional",
                    "Acomodação em enfermaria",
                    "Disponível em RJ, SP, BSB, BH, Salvador e mais",
                    "Programa Saúde Ativa incluso",
                    "Telemedicina 24h",
                ],
            },
            {
                "name": "SulAmérica Especial",
                "type": "Nacional · Enfermaria ou Apartamento",
                "featured": True,
                "items": [
                    "Abrangência nacional",
                    "Rede credenciada ampla e qualificada",
                    "Opção enfermaria ou apartamento",
                    "Reembolso para livre escolha médica",
                    "Desconto em farmácias e programas preventivos",
                ],
            },
            {
                "name": "SulAmérica Executivo",
                "type": "Nacional · Apartamento Premium",
                "items": [
                    "Rede premium (Einstein, Sírio-Libanês)",
                    "Acomodação em apartamento individual",
                    "Reembolso diferenciado e elevado",
                    "Cobertura internacional",
                    "Assistente pessoal de saúde",
                ],
            },
        ],
        "network_title": "Rede Credenciada SulAmérica",
        "network_subtitle": "Uma das maiores e mais qualificadas redes credenciadas do país.",
        "network": [
            "Hospital Albert Einstein", "Hospital Sírio-Libanês", "Rede D'Or São Luiz",
            "Copa D'Or", "Hospital Samaritano", "Hospital São Lucas",
            "Rede Labs a+", "Dasa Diagnósticos", "Clínica São Vicente",
            "Hospital Barra D'Or", "Hospital Vitória", "Prontos-Socorros 24h"
        ],
        "faqs": [
            {"q": "Qual o telefone da SulAmérica?", "a": "Para contratar, ligue para (22) 99940-4840. SAC SulAmérica: 0800 970 0500."},
            {"q": "Qual a diferença entre Direto, Especial e Executivo?", "a": "O Direto é regional e econômico; o Especial é nacional com boa cobertura; o Executivo é premium com rede top e alto reembolso."},
            {"q": "SulAmérica tem plano para empresas?", "a": "Sim. Planos PME e empresariais a partir de 2 vidas com economia significativa e benefícios exclusivos."},
            {"q": "Como funciona o reembolso SulAmérica?", "a": "Nos planos Especial e Executivo, você pode consultar médicos fora da rede e solicitar reembolso conforme tabela do seu plano."},
            {"q": "A SulAmérica aceita portabilidade?", "a": "Sim! Se você já tem plano de saúde há mais de 2 anos (ou 3 para doenças pré-existentes), pode migrar sem carência."},
            {"q": "Como emitir 2ª via do boleto?", "a": "Acesse sulamerica.com.br na área do cliente ou pelo app SulAmérica Saúde. Para planos coletivos, entre em contato com a administradora."},
        ],
    },
    {
        "slug": "plano-de-saude-hapvida",
        "title": "Plano de Saúde Hapvida | Tabela de Preços 2026 | Virtua Corretora",
        "meta_description": "Plano de Saúde Hapvida com preços 2026. Individual e empresarial. Maior rede própria do Brasil. Cotação grátis com corretor autorizado.",
        "h1": "Plano de Saúde Hapvida",
        "operator_name": "Hapvida",
        "hero_subtitle": "A Hapvida é a maior operadora de saúde do Brasil em número de beneficiários, com a maior rede própria de hospitais, clínicas e laboratórios do país. Preços acessíveis e cobertura completa.",
        "hero_gradient": "linear-gradient(135deg, #004d00 0%, #006600 50%, #008800 100%)",
        "hero_text_color": "#004d00",
        "accent_color": "#008800",
        "badges": ["Corretor Autorizado", "Preços 2026", "Maior Rede Própria", "Cobertura Nacional"],
        "whatsapp_msg": "Olá, gostaria de uma cotação do plano de saúde Hapvida",
        "benefits_title": "Por que escolher a Hapvida?",
        "benefits_subtitle": "A maior operadora de saúde do Brasil, com a maior rede própria de hospitais, UPAs e laboratórios do país.",
        "benefits": [
            {"icon": "🏥", "title": "Maior Rede Própria do Brasil", "desc": "Mais de 80 hospitais próprios e centenas de clínicas e prontos-socorros em todo o país."},
            {"icon": "💰", "title": "Melhor Custo Benefício", "desc": "Planos acessíveis sem abrir mão da qualidade, com mensalidades competitivas para todos os perfis."},
            {"icon": "📱", "title": "Teleconsulta Hapvida", "desc": "Atendimento médico online pelo portal e app com rapidez e praticidade."},
            {"icon": "🔬", "title": "Laboratórios Próprios", "desc": "Rede de laboratórios próprios para exames com agilidade e tecnologia de ponta."},
            {"icon": "🌍", "title": "Presença Nacional", "desc": "Presente em todas as regiões do Brasil com forte presença no Norte, Nordeste e Centro-Oeste."},
            {"icon": "🏢", "title": "Planos Empresariais", "desc": "Opções para empresas de todos os portes com condições especiais a partir de 2 vidas."},
        ],
        "plans_title": "Planos Hapvida Disponíveis",
        "plans_subtitle": "Conheça as principais opções de planos Hapvida.",
        "plans": [
            {
                "name": "Hapvida Mix",
                "type": "Regional · Enfermaria",
                "items": [
                    "Rede própria + rede credenciada",
                    "Acomodação em enfermaria",
                    "Coparticipação para consultas e exames",
                    "Teleconsulta inclusa",
                    "Programa de prevenção",
                ],
            },
            {
                "name": "Hapvida Pleno",
                "type": "Regional · Enfermaria ou Apartamento",
                "featured": True,
                "items": [
                    "Rede própria completa + credenciada ampla",
                    "Opção enfermaria ou apartamento",
                    "Sem coparticipação na rede própria",
                    "Atendimento em UPAs 24h",
                    "Exames e internações cobertos",
                ],
            },
            {
                "name": "Hapvida Nacional",
                "type": "Nacional · Apartamento",
                "items": [
                    "Abrangência nacional em todo Brasil",
                    "Acomodação em apartamento",
                    "Rede própria + credenciada nacional",
                    "Teleconsulta em especialidades",
                    "Programas de medicina preventiva",
                ],
            },
        ],
        "network_title": "Rede Credenciada Hapvida",
        "network_subtitle": "A maior rede própria de hospitais e clínicas do Brasil.",
        "network": [
            "Hospitais Próprios Hapvida", "UPAs 24h Hapvida", "Laboratórios Próprios",
            "Centros de Diagnóstico", "Clínicas Especializadas", "Prontos-Socorros",
            "Maternidades", "Centros Oncológicos", "Reabilitação Física",
            "Clínicas Odontológicas", "Farmácias Parceiras", "Rede Credenciada Complementar"
        ],
        "faqs": [
            {"q": "Qual o telefone da Hapvida?", "a": "Para contratar, ligue para (22) 99940-4840. SAC Hapvida: 4020-3000 ou 0800 414 0508."},
            {"q": "A Hapvida atende em que cidades?", "a": "A Hapvida está presente em todo o Brasil, com forte presença no Norte, Nordeste, Centro-Oeste e cidades como Recife, Salvador, Brasília, Manaus, Goiânia e Feira de Santana."},
            {"q": "Hapvida aceita MEI?", "a": "Sim. Empresas MEI com CNPJ ativo podem contratar planos empresariais Hapvida a partir de 2 vidas."},
            {"q": "A Hapvida tem telemedicina?", "a": "Sim! A Teleconsulta Hapvida permite consultas médicas online pelo portal e aplicativo."},
            {"q": "Como funciona a coparticipação Hapvida?", "a": "Nos planos Mix, há coparticipação em consultas e exames. Nos planos Pleno, o atendimento na rede própria é sem coparticipação."},
            {"q": "Como emitir 2ª via do boleto Hapvida?", "a": "Acesse hapvida.com.br na área do cliente ou pelo app Hapvida."},
        ],
    },
    {
        "slug": "plano-de-saude-samp-es",
        "title": "Plano de Saúde SAMP ES | Tabela de Preços 2026 | Virtua Corretora",
        "meta_description": "Plano de Saúde SAMP no Espírito Santo com preços 2026. Individual e empresarial. Rede credenciada em Vitória, Vila Velha e todo ES. Cotação grátis.",
        "h1": "Plano de Saúde SAMP<br>Espírito Santo",
        "operator_name": "SAMP",
        "hero_subtitle": "A SAMP é a principal operadora de saúde do Espírito Santo, com ampla rede credenciada em Vitória, Vila Velha, Serra, Cachoeiro de Itapemirim e todo o estado. Planos individuais e empresariais.",
        "hero_gradient": "linear-gradient(135deg, #1a365d 0%, #2a4a7f 50%, #3b5998 100%)",
        "hero_text_color": "#1a365d",
        "accent_color": "#3b5998",
        "badges": ["Corretor Autorizado", "Preços 2026", "Espírito Santo", "Individual e Empresarial"],
        "whatsapp_msg": "Olá, gostaria de uma cotação do plano de saúde SAMP ES",
        "benefits_title": "Por que escolher a SAMP?",
        "benefits_subtitle": "Há mais de 40 anos cuidando da saúde dos capixabas, a SAMP é referência em qualidade no Espírito Santo.",
        "benefits": [
            {"icon": "🏥", "title": "Rede Credenciada ES", "desc": "Ampla rede de hospitais, clínicas e laboratórios em todo o Espírito Santo."},
            {"icon": "⭐", "title": "Melhor Avaliação do ES", "desc": "Consistentemente avaliada como uma das melhores operadoras do Espírito Santo pela ANS."},
            {"icon": "💰", "title": "Preços Competitivos", "desc": "Planos acessíveis com excelente relação custo benefício para o estado."},
            {"icon": "📱", "title": "Telemedicina", "desc": "Consultas médicas online para facilitar o acesso ao atendimento."},
            {"icon": "🏢", "title": "Planos Empresariais", "desc": "Opções para empresas capixabas de todos os portes."},
            {"icon": "🌍", "title": "Cobertura Estadual e Nacional", "desc": "Planos com abrangência estadual no ES e opções nacionais."},
        ],
        "plans_title": "Planos SAMP Disponíveis",
        "plans_subtitle": "Conheça as opções de planos SAMP para o Espírito Santo.",
        "plans": [
            {
                "name": "SAMP Estadual",
                "type": "Estadual ES · Enfermaria",
                "items": [
                    "Cobertura em todo o Espírito Santo",
                    "Acomodação em enfermaria",
                    "Rede credenciada estadual",
                    "Programa de medicina preventiva",
                    "Telemedicina inclusa",
                ],
            },
            {
                "name": "SAMP Vitória",
                "type": "Regional · Apartamento",
                "featured": True,
                "items": [
                    "Cobertura na Grande Vitória",
                    "Acomodação em apartamento",
                    "Rede credenciada premium regional",
                    "Sem coparticipação",
                    "Acesso a hospitais referência do ES",
                ],
            },
            {
                "name": "SAMP Nacional",
                "type": "Nacional · Apartamento",
                "items": [
                    "Abrangência nacional",
                    "Acomodação em apartamento",
                    "Rede credenciada em todo Brasil",
                    "Reembolso para livre escolha",
                    "Cobertura completa",
                ],
            },
        ],
        "network_title": "Rede Credenciada SAMP",
        "network_subtitle": "Principais hospitais e clínicas do Espírito Santo.",
        "network": [
            "Hospital Meridional", "Vitória Apart Hospital", "Hospital Santa Rita",
            "Hospital Metropolitano", "Hospital Estadual", "UDI Hospital",
            "Laboratório Tommasi", "Centro de Diagnóstico", "Clínicas Especializadas",
            "Maternidades", "Prontos-Socorros", "Rede em Cachoeiro"
        ],
        "faqs": [
            {"q": "Qual o telefone da SAMP?", "a": "Para contratar, ligue para (22) 99940-4840. SAC SAMP: (27) 2104-3333."},
            {"q": "A SAMP atende em que cidades do ES?", "a": "Vitória, Vila Velha, Serra, Cariacica, Cachoeiro de Itapemirim, Guarapari, Linhares e todo o estado."},
            {"q": "A SAMP tem plano individual?", "a": "Sim! A SAMP oferece planos individuais e familiares além dos empresariais."},
            {"q": "SAMP aceita empresas MEI?", "a": "Sim. MEIs com CNPJ ativo podem contratar planos empresariais a partir de 2 vidas."},
            {"q": "A SAMP tem plano com cobertura nacional?", "a": "Sim, a SAMP oferece opção de plano com abrangência nacional além dos planos estaduais."},
        ],
    },
]

# SUSEP number
SUSEP = "15414.901434/2015-19"

# ============================================================
# GENERATE PAGES
# ============================================================
def generate_page(page_data):
    slug = page_data["slug"]
    
    # Build HTML parts
    badges_html = make_badges(page_data["badges"])
    benefits_html = make_benefits(page_data["benefits"])
    plans_html = make_plans(page_data["plans"], page_data["accent_color"])
    network_html = make_network(page_data["network"])
    faq_html = make_faq(page_data["faqs"])
    schema = make_faq_schema(page_data["faqs"], f"https://www.virtuacorretora.com.br/{slug}/")
    
    html = TEMPLATE.format(
        title=page_data["title"],
        meta_description=page_data["meta_description"],
        slug=slug,
        h1=page_data["h1"],
        operator_name=page_data["operator_name"],
        hero_subtitle=page_data["hero_subtitle"],
        hero_gradient=page_data["hero_gradient"],
        hero_text_color=page_data["hero_text_color"],
        accent_color=page_data["accent_color"],
        hero_badges=badges_html,
        whatsapp_msg=page_data["whatsapp_msg"],
        benefits_title=page_data["benefits_title"],
        benefits_subtitle=page_data["benefits_subtitle"],
        benefits_html=benefits_html,
        plans_title=page_data["plans_title"],
        plans_subtitle=page_data["plans_subtitle"],
        plans_html=plans_html,
        network_title=page_data["network_title"],
        network_subtitle=page_data["network_subtitle"],
        network_html=network_html,
        faq_html=faq_html,
        schema_markup=schema,
        susep=SUSEP,
    )
    
    # Create directory
    os.makedirs(slug, exist_ok=True)
    filepath = os.path.join(slug, "index.html")
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    
    return filepath

if __name__ == "__main__":
    print(f"Generating {len(PAGES)} operator pages...")
    for page in PAGES:
        path = generate_page(page)
        print(f"  OK {path}")
    print(f"\nDone! {len(PAGES)} pages created successfully.")
