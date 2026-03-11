import os

TEMPLATE = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | Virtua Corretora de Seguros</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="style.css">
    <style>
        .page-header {{
            background: var(--gradient-primary);
            padding: 120px 0 60px;
            color: white;
            text-align: center;
        }}
        .page-header h1 {{
            font-size: clamp(32px, 4vw, 48px);
            margin-bottom: 20px;
            font-weight: 800;
        }}
        .page-header p {{
            font-size: 18px;
            opacity: 0.9;
            max-width: 600px;
            margin: 0 auto;
        }}
        .page-content {{
            padding: 80px 0;
            background: var(--gray-50);
        }}
        .content-card {{
            background: white;
            border-radius: var(--radius-lg);
            padding: 50px;
            box-shadow: var(--shadow);
            max-width: 800px;
            margin: 0 auto;
            border: 1px solid var(--gray-200);
        }}
        .content-card h2 {{
            color: var(--primary);
            margin-bottom: 24px;
            font-size: 32px;
            font-weight: 800;
        }}
        .content-card p {{
            color: var(--gray-600);
            margin-bottom: 24px;
            font-size: 16px;
            line-height: 1.8;
        }}
        .content-card h3 {{
            color: var(--gray-800);
            margin-bottom: 20px;
            font-size: 20px;
            font-weight: 700;
        }}
        .content-card ul {{
            margin-bottom: 32px;
            padding-left: 0;
        }}
        .content-card li {{
            color: var(--gray-600);
            margin-bottom: 12px;
            position: relative;
            padding-left: 32px;
            list-style: none;
            font-size: 16px;
        }}
        .content-card li::before {{
            content: "✓";
            position: absolute;
            left: 0;
            color: var(--white);
            background: var(--green);
            border-radius: 50%;
            width: 20px;
            height: 20px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 12px;
            font-weight: bold;
            top: 2px;
        }}
        .cta-section {{
            text-align: center;
            margin-top: 48px;
            padding-top: 48px;
            border-top: 1px solid var(--gray-200);
        }}
        .cta-section .btn {{
            margin: 8px;
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
                        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 22 16.92z" />
                        </svg> (22) 99940-4840
                    </a>
                </div>
                <a href="https://wa.me/5522999404840" target="_blank" class="top-bar-link whatsapp-link">
                    WhatsApp
                </a>
            </div>
            <div class="top-bar-info">
                <span><a href="index.html" style="color:var(--white); opacity:0.9; text-decoration:none; display:flex; align-items:center; gap:6px; font-weight:500;">
                    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="19" y1="12" x2="5" y2="12"></line><polyline points="12 19 5 12 12 5"></polyline></svg>
                    Voltar para a Home
                </a></span>
            </div>
        </div>
    </div>

    <!-- Header -->
    <header class="header">
        <div class="container header-inner">
            <a href="index.html" class="logo">
                <img src="https://www.virtuacorretora.com.br/wp-content/uploads/2023/11/cropped-virtua-corretora-de-planos-de-saude-1.webp" alt="Virtua Logo" style="height: 32px; width: auto; object-fit: contain;">
                <span class="logo-text">virtua<small>CORRETORA DE SEGUROS</small></span>
            </a>
            <a href="index.html#contato" class="btn btn-primary header-cta">Fazer Simulação</a>
        </div>
    </header>

    <!-- Page Header -->
    <section class="page-header">
        <div class="container">
            <div style="font-size: 56px; margin-bottom: 24px;">{icon}</div>
            <h1>{title}</h1>
            <p>{subtitle}</p>
        </div>
    </section>

    <!-- Content -->
    <section class="page-content">
        <div class="container">
            <div class="content-card">
                <h2>O que este plano oferece?</h2>
                <p>{description}</p>
                
                <h3>Principais Benefícios:</h3>
                <ul>
                    {benefits_html}
                </ul>

                <div class="cta-section">
                    <h3 style="margin-bottom: 12px; color: var(--gray-900);">Pronto para garantir sua proteção?</h3>
                    <p style="margin-bottom: 32px; color: var(--gray-600);">Fale com um corretor agora e receba uma cotação personalizada sem compromisso.</p>
                    <div style="display:flex; justify-content:center; gap: 16px; flex-wrap: wrap;">
                        <a href="index.html#contato" class="btn btn-primary btn-lg">Solicitar Cotação →</a>
                        <a href="https://wa.me/5522999404840" target="_blank" class="btn btn-outline btn-lg" style="color: var(--green); border-color: var(--green); background: rgba(16, 185, 129, 0.1);">Via WhatsApp</a>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="footer" style="margin-top: 0;">
        <div class="container text-center">
            <p style="color: var(--gray-500);">© 2026 Virtua Corretora de Seguros. Todos os direitos reservados.</p>
        </div>
    </footer>
</body>
</html>
"""

pages = [
    {
        "filename": "produto-saude.html",
        "title": "Plano de Saúde",
        "icon": "🏥",
        "subtitle": "Amil, Bradesco, SulAmérica, Unimed e mais. Planos regionais e nacionais com os melhores custos.",
        "description": "Cuidar da saúde é o melhor investimento que você pode fazer. Oferecemos planos de saúde individuais, familiares e empresariais com as principais operadoras do mercado, garantindo rede credenciada de excelência, hospitais de ponta e atendimento humanizado.",
        "benefits": [
            "Ampla rede credenciada com os melhores hospitais.",
            "Opções com e sem coparticipação.",
            "Planos regionais ou com abrangência nacional.",
            "Cobertura para exames, cirurgias e internações."
        ]
    },
    {
        "filename": "produto-odonto.html",
        "title": "Plano Odontológico",
        "icon": "🦷",
        "subtitle": "Cobertura completa: consultas, limpeza, restaurações, canal e ortodontia.",
        "description": "Um sorriso saudável abre portas e melhora a qualidade de vida. Com o plano odontológico, você e sua família têm acesso a dentistas qualificados para tratamentos preventivos e corretivos, sem surpresas no orçamento.",
        "benefits": [
            "Ampla rede nacional de dentistas credenciados.",
            "Cobertura para emergências 24h.",
            "Tratamentos preventivos: limpeza, aplicação de flúor e raio-x.",
            "Opções com cobertura para prótese e ortodontia (aparelho)."
        ]
    },
    {
        "filename": "produto-vida.html",
        "title": "Seguro de Vida",
        "icon": "❤️",
        "subtitle": "Individual ou em grupo. Coberturas para invalidez, doenças graves e mais.",
        "description": "O seguro de vida é a garantia de tranquilidade financeira para você e as pessoas que você mais ama, caso algum imprevisto aconteça. Ele pode ser acionado em vida ou em caso de luto, oferecendo suporte no momento exato em que for necessário.",
        "benefits": [
            "Indenização por invalidez temporária ou permanente.",
            "Cobertura para diagnóstico de doenças graves (câncer, infarto, AVC).",
            "Assistência funeral familiar.",
            "Proteção financeira para os dependentes em caso de falecimento."
        ]
    },
    {
        "filename": "produto-auto.html",
        "title": "Seguro Auto",
        "icon": "🚗",
        "subtitle": "Cotamos nas maiores seguradoras. Descontos de 10 a 40% na renovação.",
        "description": "Dirija com tranquilidade sabendo que seu veículo está protegido contra roubos, furtos, acidentes e danos a terceiros. Encontramos a apólice com as coberturas ideais para o seu perfil e o melhor custo-benefício.",
        "benefits": [
            "Assistência 24h: guincho, chaveiro, pane elétrica/seca.",
            "Cobertura contra colisão e perda total.",
            "Indenização por roubo, furto e incêndio.",
            "Carro reserva."
        ]
    },
    {
        "filename": "produto-viagem.html",
        "title": "Seguro Viagem",
        "icon": "✈️",
        "subtitle": "Nacional e internacional. Proteção completa para sua viagem.",
        "description": "Vai viajar? Seja a negócios ou lazer, o seguro viagem garante a assistência necessária em qualquer lugar do mundo. Não deixe que imprevistos médicos ou com bagagem estraguem a sua viagem dos sonhos.",
        "benefits": [
            "Assistência médica e odontológica internacional.",
            "Indenização por extravio ou perda de bagagem.",
            "Cobertura para atraso ou cancelamento de voo.",
            "Auxílio em caso de perda de documentos."
        ]
    },
    {
        "filename": "produto-residencial.html",
        "title": "Seguro Residencial",
        "icon": "🏠",
        "subtitle": "Proteção para sua casa: incêndio, roubo, danos elétricos e mais.",
        "description": "Sua casa é o seu porto seguro. Com o seguro residencial, além da proteção contra grandes sinistros, você conta com um pacote de serviços assistenciais para resolver pequenos problemas do dia a dia de forma rápida.",
        "benefits": [
            "Cobertura básica contra incêndio, queda de raio e explosão.",
            "Assistência 24h (chaveiro, encanador, eletricista).",
            "Proteção contra danos elétricos em eletrodomésticos.",
            "Cobertura para roubo ou furto de bens."
        ]
    }
]

for p in pages:
    b_html = "\n                    ".join(f"<li>{b}</li>" for b in p["benefits"])
    content = TEMPLATE.format(
        title=p["title"],
        icon=p["icon"],
        subtitle=p["subtitle"],
        description=p["description"],
        benefits_html=b_html
    )
    with open(p["filename"], "w", encoding="utf-8") as f:
        f.write(content)

print("Created 6 pages!")
