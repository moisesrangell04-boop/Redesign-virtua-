#!/usr/bin/env python3
"""
Adiciona palavras-chave estratégicas em todas as páginas.
Baseado em pesquisa de palavras-chave para o nicho de planos de saúde e corretoras de seguros no Brasil.

3 camadas de implementação (curso Next SEO - Módulos 6, 7 e 8):
1. <meta name="keywords"> — sinal para motores de busca
2. Seção "Termos Relacionados" — captura long tails, melhora indexação (Módulo 7: texto de apoio)
3. Melhoria de alt text em imagens — sinais on-page (Módulo 6)
"""

import os, re, glob

# ── BANCO DE PALAVRAS-CHAVE ────────────────────────────────────────────────────

GLOBAL_KEYWORDS = [
    "plano de saúde", "planos de saúde", "convênio médico", "seguro saúde",
    "corretora de seguros", "corretora de planos de saúde",
    "cotação plano de saúde", "tabela de preços plano de saúde",
    "plano de saúde individual", "plano de saúde familiar",
    "plano de saúde empresarial", "plano de saúde MEI",
    "plano de saúde 2026", "melhor plano de saúde",
    "plano de saúde barato", "plano de saúde com cobertura nacional",
    "plano de saúde sem carência", "plano de saúde com reembolso",
    "rede credenciada", "carência plano de saúde",
    "portabilidade plano de saúde", "cobertura hospitalar",
    "coparticipação plano de saúde", "ANS plano de saúde",
    "corretor autorizado plano de saúde", "Virtua Corretora",
]

# Keywords específicas por página
PAGE_KEYWORDS = {
    "plano-de-saude-amil": [
        "Amil", "plano de saúde Amil", "Amil individual", "Amil familiar",
        "Amil empresarial", "Amil 400", "Amil 500", "Amil 750",
        "Amil Fácil", "Amil Clínica Digital", "Amil dental",
        "rede credenciada Amil", "telefone Amil", "SAC Amil 0800",
        "reembolso Amil", "Amil MEI", "cotação Amil", "preço plano Amil",
        "Amil telemedicina", "tabela Amil 2026", "plano Amil barato",
        "Amil nacional", "corretor Amil autorizado", "Amil Rio de Janeiro",
        "Amil hospitais", "Copa D'Or Amil", "Samaritano Amil",
    ],
    "plano-de-saude-sulamerica": [
        "SulAmérica", "plano de saúde SulAmérica", "SulAmérica individual",
        "SulAmérica familiar", "SulAmérica empresarial",
        "SulAmérica Saúde Direto", "SulAmérica Top", "SulAmérica Clássico",
        "SulAmérica Especial", "SulAmérica Executivo",
        "rede credenciada SulAmérica", "reembolso SulAmérica",
        "cotação SulAmérica", "tabela SulAmérica 2026",
        "SulAmérica dental", "odonto SulAmérica",
        "SulAmérica telemedicina", "SulAmérica MEI",
        "SulAmérica São Paulo", "SulAmérica Rio de Janeiro",
        "corretor SulAmérica autorizado", "telefone SulAmérica",
    ],
    "plano-de-saude-bradesco": [
        "Bradesco Saúde", "plano de saúde Bradesco", "Bradesco individual",
        "Bradesco familiar", "Bradesco empresarial",
        "Bradesco Top Nacional", "Bradesco Nacional Flex",
        "Bradesco Efetivo", "Bradesco Preferencial Plus",
        "rede credenciada Bradesco", "rede Bradesco hospitais",
        "Albert Einstein Bradesco", "Sírio-Libanês Bradesco",
        "reembolso Bradesco", "cotação Bradesco", "tabela Bradesco 2026",
        "Bradesco dental", "Bradesco Dental Empresarial",
        "corretor Bradesco autorizado", "telefone Bradesco Saúde",
        "Bradesco MEI", "Bradesco telemedicina", "Bradesco odonto",
    ],
    "plano-de-saude-unimed": [
        "Unimed", "plano de saúde Unimed", "Unimed individual",
        "Unimed familiar", "Unimed empresarial", "convênio Unimed",
        "cooperativa Unimed", "rede Unimed", "rede credenciada Unimed",
        "Unimed Nacional", "Unimed Apartamento", "Unimed Enfermaria",
        "Unimed MEI", "cotação Unimed", "tabela Unimed 2026",
        "Unimed dental", "Unimed telemedicina", "Unimed RJ",
        "reembolso Unimed", "corretor Unimed autorizado",
        "telefone Unimed", "Unimed intercâmbio",
    ],
    "plano-de-saude-hapvida": [
        "Hapvida", "plano de saúde Hapvida", "Hapvida individual",
        "Hapvida familiar", "Hapvida empresarial", "Hapvida Nordeste",
        "Hapvida rede própria", "NotreDame Intermédica Hapvida",
        "GNDI Hapvida", "rede Hapvida", "hospitais Hapvida",
        "cotação Hapvida", "tabela Hapvida 2026", "Hapvida barato",
        "Hapvida MEI", "Hapvida dental", "Hapvida telemedicina",
        "reembolso Hapvida", "telefone Hapvida", "SAC Hapvida",
        "corretor Hapvida autorizado", "Hapvida Norte Nordeste",
    ],
    "plano-de-saude-intermedica": [
        "Intermédica", "NotreDame Intermédica", "GNDI",
        "plano de saúde Intermédica", "Intermédica individual",
        "Intermédica familiar", "Intermédica empresarial",
        "rede credenciada Intermédica", "hospitais Intermédica",
        "cotação Intermédica", "tabela Intermédica 2026",
        "reembolso Intermédica", "telefone Intermédica",
        "Intermédica MEI", "Intermédica dental",
        "corretor Intermédica autorizado", "Intermédica São Paulo",
        "Intermédica plano barato",
    ],
    "plano-de-saude-hapvida-brasilia": [
        "Hapvida Brasília", "plano de saúde Brasília", "plano de saúde DF",
        "Hapvida DF", "Hapvida Distrito Federal", "plano saúde Brasília",
        "cotação plano de saúde Brasília", "convenio medico Brasília",
        "plano de saúde Taguatinga", "plano de saúde Ceilândia",
        "plano de saúde Gama DF", "rede credenciada Brasília",
    ],
    "plano-de-saude-hapvida-recife": [
        "Hapvida Recife", "plano de saúde Recife", "plano de saúde Pernambuco",
        "Hapvida Pernambuco", "cotação plano de saúde Recife",
        "convênio médico Recife", "plano saúde Recife barato",
        "rede credenciada Recife", "plano de saúde Olinda",
        "plano de saúde Caruaru", "plano de saúde PE",
    ],
    "plano-de-saude-hapvida-salvador": [
        "Hapvida Salvador", "plano de saúde Salvador", "plano de saúde Bahia",
        "Hapvida Bahia", "cotação plano de saúde Salvador",
        "convênio médico Salvador", "plano saúde Salvador",
        "rede credenciada Salvador", "plano de saúde Feira de Santana",
        "plano de saúde BA",
    ],
    "plano-de-saude-hapvida-manaus": [
        "Hapvida Manaus", "plano de saúde Manaus", "plano de saúde Amazonas",
        "Hapvida Amazonas", "cotação plano de saúde Manaus",
        "convênio médico Manaus", "plano saúde Manaus",
        "rede credenciada Manaus", "plano de saúde AM",
    ],
    "plano-de-saude-bh-sulamerica-saude-direto": [
        "SulAmérica Direto BH", "plano de saúde Belo Horizonte",
        "SulAmérica BH", "plano saúde BH", "cotação plano saúde BH",
        "convênio médico Belo Horizonte", "rede credenciada BH",
        "plano de saúde Minas Gerais", "plano saúde MG",
    ],
    "plano-de-saude-sulamerica-direto-sampa": [
        "SulAmérica Direto São Paulo", "plano de saúde São Paulo",
        "SulAmérica SP", "plano saúde SP", "cotação plano saúde SP",
        "convênio médico São Paulo", "rede credenciada São Paulo",
        "plano de saúde capital SP", "plano saúde Grande São Paulo",
    ],
    "plano-de-saude-sulamerica-direto-brasilia": [
        "SulAmérica Direto Brasília", "SulAmérica DF",
        "plano de saúde Brasília SulAmérica", "cotação SulAmérica Brasília",
        "rede credenciada SulAmérica DF",
    ],
    "plano-de-saude-sulamerica-direto-salvador": [
        "SulAmérica Direto Salvador", "SulAmérica Bahia",
        "plano de saúde Salvador SulAmérica", "cotação SulAmérica Salvador",
    ],
    "plano-de-saude-sulamerica-recife": [
        "SulAmérica Recife", "SulAmérica Pernambuco",
        "plano de saúde Recife SulAmérica", "cotação SulAmérica Recife",
    ],
    "plano-de-saude-joao-pessoa-sulamerica": [
        "SulAmérica João Pessoa", "plano de saúde João Pessoa",
        "plano de saúde Paraíba", "SulAmérica PB",
        "cotação plano saúde João Pessoa",
    ],
    "plano-de-saude-rj": [
        "plano de saúde RJ", "plano de saúde Rio de Janeiro",
        "melhor plano de saúde Rio de Janeiro",
        "cotação plano de saúde Rio de Janeiro",
        "convênio médico Rio de Janeiro", "plano saúde Niterói",
        "plano saúde Zona Sul RJ", "plano saúde Zona Norte RJ",
        "plano saúde Barra da Tijuca", "plano saúde Botafogo",
        "plano saúde Copacabana", "plano saúde Ipanema",
        "rede credenciada Rio de Janeiro",
    ],
    "plano-de-saude-para-idosos": [
        "plano de saúde para idosos", "plano de saúde terceira idade",
        "plano de saúde 60 anos", "plano de saúde acima de 65 anos",
        "plano de saúde senior", "plano de saúde aposentado",
        "plano de saúde idoso barato", "MedSênior idosos",
        "plano de saúde acima de 70 anos", "Prevent Senior idosos",
        "cotação plano de saúde idoso", "plano de saúde pensionista",
    ],
    "medsenior-rj": [
        "MedSênior", "MedSênior RJ", "MedSênior Rio de Janeiro",
        "plano de saúde para idosos RJ", "MedSênior preços",
        "cotação MedSênior", "MedSênior terceira idade",
        "tabela MedSênior 2026", "MedSênior rede credenciada",
        "plano saúde idosos Rio de Janeiro",
    ],
    "plano-de-saude-porto-seguro-saude": [
        "Porto Seguro Saúde", "plano Porto Seguro",
        "Porto Seguro individual", "Porto Seguro familiar",
        "Porto Seguro empresarial", "rede credenciada Porto Seguro",
        "cotação Porto Seguro Saúde", "tabela Porto Seguro 2026",
        "reembolso Porto Seguro", "Porto Seguro dental",
        "corretor Porto Seguro autorizado",
    ],
    "plano-de-saude-prevent-senior": [
        "Prevent Senior", "plano Prevent Senior",
        "Prevent Senior individual", "Prevent Senior familiar",
        "Prevent Senior idosos", "Prevent Senior Rio de Janeiro",
        "cotação Prevent Senior", "tabela Prevent Senior 2026",
        "rede credenciada Prevent Senior", "Prevent Senior hospitais",
        "Prevent Senior médicos", "Prevent Senior cobertura",
    ],
    "plano-de-saude-caberj-integral-saude": [
        "CABERJ", "Integral Saúde", "CABERJ plano de saúde",
        "Integral Saúde RJ", "plano de saúde servidores",
        "CABERJ Rio de Janeiro", "cotação CABERJ",
        "tabela CABERJ 2026", "rede credenciada CABERJ",
    ],
    "plano-de-saude-unimed-campos": [
        "Unimed Campos", "plano de saúde Campos dos Goytacazes",
        "Unimed Campos dos Goytacazes", "plano saúde norte fluminense",
        "cotação Unimed Campos", "rede credenciada Campos",
        "convenio medico Campos dos Goytacazes",
    ],
    "plano-saude-unimed-macae": [
        "Unimed Macaé", "plano de saúde Macaé",
        "Unimed Macaé RJ", "plano saúde Macaé",
        "cotação plano saúde Macaé", "rede credenciada Macaé",
        "convenio medico Macaé", "plano saúde Região dos Lagos",
    ],
    "amil-macae": [
        "Amil Macaé", "plano de saúde Amil Macaé",
        "Amil Região dos Lagos RJ", "cotação Amil Macaé",
        "corretor Amil Macaé", "convenio medico Macaé Amil",
    ],
    "amil-lagos": [
        "Amil Região dos Lagos", "plano saúde Região dos Lagos",
        "Amil Cabo Frio", "Amil Búzios", "Amil Arraial do Cabo",
        "plano saúde Cabo Frio", "cotação Amil Lagos",
        "corretor Amil Região dos Lagos",
    ],
    "amil-campos": [
        "Amil Campos dos Goytacazes", "plano saúde Campos RJ",
        "Amil norte fluminense", "cotação Amil Campos",
        "corretor Amil Campos dos Goytacazes",
        "convenio medico Campos dos Goytacazes",
    ],
    "plano-de-saude-samp-es": [
        "SAMP", "plano de saúde SAMP", "SAMP Espírito Santo",
        "SAMP ES", "plano saúde ES", "plano saúde Vitória",
        "cotação SAMP", "rede credenciada SAMP",
        "SAMP individual", "SAMP empresarial",
    ],
    "santa-helena-saude": [
        "Santa Helena Saúde", "plano Santa Helena",
        "Santa Helena individual", "Santa Helena familiar",
        "Santa Helena empresarial", "rede credenciada Santa Helena",
        "cotação Santa Helena", "tabela Santa Helena 2026",
        "Santa Helena São Paulo", "Santa Helena SP",
    ],
    "plano-klini-saude": [
        "Klini Saúde", "plano Klini", "Klini individual",
        "Klini familiar", "cotação Klini", "tabela Klini 2026",
        "rede credenciada Klini", "Klini RJ",
    ],
    "bradesco-dental": [
        "Bradesco Dental", "plano odontológico Bradesco",
        "Bradesco dental individual", "Bradesco dental empresarial",
        "Bradesco odonto", "rede credenciada Bradesco Dental",
        "cotação Bradesco Dental", "tabela Bradesco Dental 2026",
        "dentista Bradesco", "ortodontia Bradesco Dental",
        "implante dentário Bradesco", "plano odonto barato Bradesco",
    ],
    "plano-odonto-empresarial": [
        "plano odontológico empresarial", "plano dental empresarial",
        "odonto empresarial", "plano odonto para empresa",
        "plano odonto MEI", "plano dental para funcionários",
        "cotação plano odonto empresarial", "Bradesco Dental empresarial",
        "OdontoPrev empresarial", "Amil Dental empresarial",
        "plano dental coletivo", "preço plano odonto empresa",
    ],
    "rede-credenciada-sulamerica-odonto": [
        "rede credenciada SulAmérica Odonto", "dentistas SulAmérica",
        "clínicas odontológicas SulAmérica", "SulAmérica Odonto rede",
        "buscar dentista SulAmérica", "rede credenciada odonto SulAmérica",
    ],
    "telefones-amil-dental": [
        "telefone Amil Dental", "SAC Amil Dental", "0800 Amil Dental",
        "atendimento Amil Dental", "contato Amil Dental",
        "central de atendimento Amil Dental", "Amil Dental ouvidoria",
    ],
    "telefones-assim-saude": [
        "telefone Assim Saúde", "SAC Assim Saúde", "0800 Assim Saúde",
        "atendimento Assim Saúde", "contato Assim Saúde",
        "central Assim Saúde", "Assim Saúde ouvidoria",
    ],
    "telefones-intermedica": [
        "telefone Intermédica", "SAC Intermédica", "0800 Intermédica",
        "atendimento NotreDame Intermédica", "contato GNDI",
        "central Intermédica", "ouvidoria Intermédica",
    ],
    "telefones-odontoprev": [
        "telefone OdontoPrev", "SAC OdontoPrev", "0800 OdontoPrev",
        "atendimento OdontoPrev", "contato OdontoPrev",
        "central OdontoPrev", "ouvidoria OdontoPrev",
    ],
    "reembolso-amil": [
        "reembolso Amil", "como funciona reembolso Amil",
        "solicitar reembolso Amil", "prazo reembolso Amil",
        "reembolso Amil online", "reembolso consulta Amil",
        "reembolso exame Amil", "reembolso cirurgia Amil",
        "app Amil reembolso", "Amil área do cliente reembolso",
    ],
    "reembolso-sulamerica": [
        "reembolso SulAmérica", "como funciona reembolso SulAmérica",
        "solicitar reembolso SulAmérica", "prazo reembolso SulAmérica",
        "reembolso SulAmérica online", "SulAmérica área do cliente",
        "reembolso consulta SulAmérica", "reembolso exame SulAmérica",
    ],
    "reembolso-intermedica": [
        "reembolso Intermédica", "como funciona reembolso Intermédica",
        "solicitar reembolso GNDI", "prazo reembolso NotreDame",
        "reembolso Intermédica online", "Intermédica área do cliente",
    ],
    "simulacao-seguro-de-vida": [
        "simulação seguro de vida", "cotação seguro de vida",
        "seguro de vida online", "calcular seguro de vida",
        "quanto custa seguro de vida", "seguro de vida barato",
        "seguro de vida individual", "seguro de vida familiar",
        "seguro de vida empresarial", "seguro de vida Bradesco",
        "seguro de vida Porto Seguro", "seguro de vida SulAmérica",
        "cobertura morte acidental", "seguro de vida com invalidez",
        "seguro de vida MEI", "seguro de vida autônomo",
    ],
    "bradesco-seguro-de-vida": [
        "Bradesco Seguro de Vida", "seguro de vida Bradesco",
        "cotação Bradesco Seguro de Vida", "Bradesco Vida individual",
        "Bradesco Vida empresarial", "tabela Bradesco Vida 2026",
        "cobertura Bradesco Seguro de Vida", "Bradesco Vida morte",
        "Bradesco Vida invalidez", "sinistro Bradesco Vida",
        "corretor Bradesco Vida autorizado",
    ],
}

# Keywords para seção de termos relacionados (long tails de alta conversão)
RELATED_SEARCHES = {
    "plano-de-saude-amil": [
        ("Tabela de Preços Amil 2026", "#"),
        ("Amil Individual – Cotação Online", "#"),
        ("Rede Credenciada Amil RJ", "#"),
        ("Amil MEI – Plano para Autônomos", "#"),
        ("Plano Amil Familiar – Dependentes", "#"),
        ("Amil 400 vs Amil 750 – Comparativo", "#"),
    ],
    "plano-de-saude-sulamerica": [
        ("Tabela SulAmérica 2026", "#"),
        ("SulAmérica Direto – Plano Individual", "#"),
        ("Reembolso SulAmérica – Como Solicitar", "#"),
        ("SulAmérica Odonto Empresarial", "#"),
        ("SulAmérica MEI – Plano para Autônomos", "#"),
    ],
    "plano-de-saude-bradesco": [
        ("Tabela Bradesco Saúde 2026", "#"),
        ("Bradesco Top Nacional – Cobertura Premium", "#"),
        ("Bradesco Dental – Plano Odontológico", "bradesco-dental/index.html"),
        ("Bradesco MEI – Plano para Microempresários", "#"),
        ("Rede Bradesco – Hospitais de Referência", "#"),
    ],
    "plano-de-saude-unimed": [
        ("Tabela Unimed 2026", "#"),
        ("Unimed Individual – Cotação Grátis", "#"),
        ("Intercâmbio Unimed – Como Funciona", "#"),
        ("Unimed Campos dos Goytacazes", "plano-de-saude-unimed-campos/index.html"),
        ("Unimed Macaé", "plano-saude-unimed-macae/index.html"),
    ],
    "plano-de-saude-para-idosos": [
        ("MedSênior RJ – Plano para Idosos", "medsenior-rj/index.html"),
        ("Prevent Senior – Plano para 60+", "plano-de-saude-prevent-senior/index.html"),
        ("Plano de Saúde para Aposentados", "#"),
        ("Plano de Saúde Acima de 70 Anos", "#"),
        ("Carência Reduzida para Idosos", "#"),
    ],
}

# Keywords globais por tipo de página
PAGE_TYPE_KEYWORDS = {
    "reembolso": [
        "reembolso plano de saúde", "como funciona reembolso",
        "solicitar reembolso plano", "prazo reembolso ANS",
        "reembolso consulta médica", "reembolso exame",
        "livre escolha médica", "reembolso fora da rede",
    ],
    "telefones": [
        "telefone plano de saúde", "SAC plano de saúde",
        "0800 plano de saúde", "central de atendimento",
        "ouvidoria plano de saúde", "cancelar plano de saúde",
        "2ª via boleto plano de saúde", "app plano de saúde",
    ],
    "hapvida": [
        "Hapvida rede própria", "Hapvida hospitais próprios",
        "Hapvida Nordeste", "Hapvida Norte", "Hapvida GNDI",
        "NotreDame Hapvida", "Hapvida plano barato",
    ],
    "sulamerica": [
        "SulAmérica Saúde", "SulAmérica Seguros",
        "SulAmérica Direto", "plano SulAmérica",
        "rede SulAmérica", "reembolso SulAmérica",
    ],
}

def get_keywords_for_page(slug, html):
    """Compila lista de keywords para uma página específica."""
    kws = list(GLOBAL_KEYWORDS)

    # Keywords específicas da página
    if slug in PAGE_KEYWORDS:
        kws.extend(PAGE_KEYWORDS[slug])

    # Keywords por tipo
    for tipo, tipo_kws in PAGE_TYPE_KEYWORDS.items():
        if tipo in slug:
            kws.extend(tipo_kws)

    # Deduplicar preservando ordem
    seen = set()
    result = []
    for k in kws:
        if k.lower() not in seen:
            seen.add(k.lower())
            result.append(k)

    return result[:40]  # máximo 40 keywords

def build_meta_keywords(keywords):
    return f'    <meta name="keywords" content="{", ".join(keywords)}">'

def build_related_section(slug, html):
    """
    Seção 'Termos Relacionados' com links internos — Módulo 7 (Texto de Apoio).
    Captura long tails e melhora indexação de páginas irmãs.
    """
    # Links internos universais relevantes para todas as páginas
    universal_links = [
        ("Plano de Saúde Amil", "../plano-de-saude-amil/"),
        ("Plano de Saúde SulAmérica", "../plano-de-saude-sulamerica/"),
        ("Plano de Saúde Bradesco", "../plano-de-saude-bradesco/"),
        ("Plano de Saúde Unimed", "../plano-de-saude-unimed/"),
        ("Plano de Saúde Hapvida", "../plano-de-saude-hapvida/"),
        ("Plano de Saúde Intermédica", "../plano-de-saude-intermedica/"),
        ("Cotação Seguro de Vida", "../simulacao-seguro-de-vida/"),
        ("Plano Odontológico Empresarial", "../plano-odonto-empresarial/"),
    ]

    # Links específicos por slug (remove self-reference)
    links = [(label, url) for label, url in universal_links
             if slug not in url][:6]

    # Adiciona long tails específicas
    specific = PAGE_KEYWORDS.get(slug, [])
    long_tails_text = ""
    if specific:
        # Pega os 8 primeiros termos específicos como tags clicáveis
        tags = specific[:8]
        tag_html = " ".join([
            f'<span style="display:inline-flex;align-items:center;background:#eff6ff;color:#1d4ed8;'
            f'border:1px solid #bfdbfe;padding:5px 12px;border-radius:20px;font-size:13px;'
            f'font-weight:500;cursor:default;">{t}</span>'
            for t in tags
        ])
        long_tails_text = f'''
            <div style="margin-top:20px;">
                <p style="font-size:13px;color:#64748b;margin:0 0 10px;font-weight:600;text-transform:uppercase;letter-spacing:.04em;">Termos de busca relacionados</p>
                <div style="display:flex;flex-wrap:wrap;gap:8px;">{tag_html}</div>
            </div>'''

    links_html = "\n".join([
        f'<li><a href="{url}" style="color:#0066cc;text-decoration:none;font-weight:500;font-size:14px;'
        f'display:flex;align-items:center;gap:6px;">'
        f'<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">'
        f'<polyline points="9 18 15 12 9 6"/></svg>{label}</a></li>'
        for label, url in links
    ])

    return f'''    <!-- Seção de conteúdo relacionado (Módulo 7 - Texto de Apoio: Next SEO) -->
    <section style="background:#f8fafc;border-top:1px solid #e2e8f0;padding:40px 0;">
        <div class="container" style="max-width:1100px;margin:0 auto;padding:0 24px;">
            <h2 style="font-size:18px;font-weight:700;color:#1e293b;margin:0 0 20px;">Outros Planos e Seguros</h2>
            <ul style="list-style:none;padding:0;margin:0;display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:10px;">
{links_html}
            </ul>{long_tails_text}
            <div style="margin-top:24px;padding-top:20px;border-top:1px solid #e2e8f0;">
                <p style="font-size:13px;color:#64748b;margin:0;line-height:1.7;">
                    A <strong>Virtua Corretora de Seguros</strong> oferece <strong>cotação gratuita</strong> para planos de saúde das principais operadoras do Brasil: Amil, SulAmérica, Bradesco Saúde, Unimed, Hapvida, NotreDame Intermédica, Porto Seguro, Prevent Senior e muito mais. Atendemos clientes em todo o Brasil — <strong>plano individual, familiar, empresarial e MEI</strong>. Fale com um <strong>corretor autorizado pela SUSEP</strong> agora mesmo.
                </p>
            </div>
        </div>
    </section>'''

def process_file(filepath):
    slug = os.path.basename(os.path.dirname(filepath))
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    changed = False

    # ── 1. META KEYWORDS ────────────────────────────────────────────────────────
    if 'name="keywords"' not in html:
        kws = get_keywords_for_page(slug, html)
        meta_kw = build_meta_keywords(kws)
        # Insere após meta description
        html = re.sub(
            r'(<meta name="description"[^>]*>)',
            r'\1\n' + meta_kw,
            html, count=1
        )
        changed = True
        print(f"  ✓ meta keywords: {len(kws)} termos")

    # ── 2. SEÇÃO DE CONTEÚDO RELACIONADO ────────────────────────────────────────
    if 'Módulo 7 - Texto de Apoio' not in html:
        related = build_related_section(slug, html)
        # Insere antes da seção E-A-T (que já existe) ou antes do footer
        if 'eat-author-section' in html:
            html = re.sub(
                r'(<!-- E-A-T: Autor)',
                related + '\n\n    \\1',
                html, count=1
            )
        else:
            html = re.sub(
                r'(<footer)',
                related + '\n\n    \\1',
                html, count=1
            )
        changed = True
        print(f"  ✓ seção de conteúdo relacionado adicionada")

    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
    return changed


def main():
    base = os.path.dirname(os.path.abspath(__file__))
    files = sorted(glob.glob(os.path.join(base, '*/index.html')))
    files.append(os.path.join(base, 'index.html'))

    print(f"Processando {len(files)} páginas...\n")
    updated = 0
    for f in files:
        slug = os.path.basename(os.path.dirname(f))
        print(f"[{slug}]")
        if process_file(f):
            updated += 1
        print()

    print(f"✅ {updated} páginas atualizadas com palavras-chave")

if __name__ == '__main__':
    main()
