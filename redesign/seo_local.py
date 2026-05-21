#!/usr/bin/env python3
"""
SEO local avançado para as páginas do Rio de Janeiro, Campos dos Goytacazes,
Região dos Lagos e Macaé.

Implementa:
1. LocalBusiness + GeoCoordinates schema por cidade
2. Meta keywords locais expandidas
3. Meta description e og:title otimizados por cidade
4. Seção HTML "Cidades e Regiões Atendidas" com bairros e municípios
5. Seção de hospitais/clínicas locais enriquecida
6. FAQs locais adicionais
7. Texto de apoio local (Módulo 7 - Next SEO)
"""
import os, re

BASE = os.path.dirname(os.path.abspath(__file__))

# ── DADOS LOCAIS ────────────────────────────────────────────────────────────────

LOCAL_DATA = {

    # ── RIO DE JANEIRO ──────────────────────────────────────────────────────────
    "plano-de-saude-rj": {
        "title": "Plano de Saúde RJ | Cotação Grátis 2026 | Virtua",
        "description": "Plano de saúde no Rio de Janeiro: compare Amil, Bradesco, SulAmérica, Unimed, Hapvida e mais. Individual, familiar e empresarial. Atendemos todos os bairros do RJ.",
        "h1": "Plano de Saúde<br>Rio de Janeiro",
        "keywords_extra": [
            # Cidades da Grande Rio
            "plano de saúde Rio de Janeiro", "plano de saúde RJ",
            "plano de saúde Niterói", "plano de saúde São Gonçalo",
            "plano de saúde Duque de Caxias", "plano de saúde Nova Iguaçu",
            "plano de saúde Belford Roxo", "plano de saúde São João de Meriti",
            "plano de saúde Nilópolis", "plano de saúde Mesquita",
            "plano de saúde Petrópolis", "plano de saúde Teresópolis",
            "plano de saúde Volta Redonda", "plano de saúde Angra dos Reis",
            "plano de saúde Itaboraí", "plano de saúde Maricá",
            # Bairros do Rio
            "plano de saúde Barra da Tijuca", "plano de saúde Ipanema",
            "plano de saúde Copacabana", "plano de saúde Botafogo",
            "plano de saúde Tijuca", "plano de saúde Méier",
            "plano de saúde Campo Grande", "plano de saúde Jacarepaguá",
            "plano de saúde Recreio dos Bandeirantes", "plano de saúde Zona Sul",
            "plano de saúde Zona Norte", "plano de saúde Zona Oeste",
            "plano de saúde Centro RJ", "plano de saúde Flamengo",
            "plano de saúde Leblon", "plano de saúde Grajaú",
            # Long tails
            "melhor plano de saúde RJ 2026", "plano de saúde barato Rio de Janeiro",
            "cotação plano de saúde RJ online", "plano de saúde RJ individual",
            "plano de saúde RJ empresarial", "plano de saúde RJ MEI",
            "convênio médico Rio de Janeiro", "corretor de plano de saúde RJ",
            "corretora de seguros Rio de Janeiro", "operadoras de saúde RJ",
            # Hospitais
            "rede D'Or plano de saúde", "Copa D'Or plano de saúde",
            "Hospital Samaritano plano", "Rede D'Or São Luiz",
            "Copa Star plano", "Barra D'Or plano", "plano de saúde hospitais RJ",
        ],
        "geo": {"lat": -22.9068, "lng": -43.1729, "city": "Rio de Janeiro", "state": "RJ"},
        "area_served": [
            "Rio de Janeiro", "Niterói", "São Gonçalo", "Duque de Caxias",
            "Nova Iguaçu", "Belford Roxo", "São João de Meriti",
            "Nilópolis", "Mesquita", "Itaguaí", "Maricá", "Petrópolis",
        ],
        "local_hospitals": [
            "Copa D'Or", "Copa Star", "Barra D'Or", "Norte D'Or", "Quinta D'Or",
            "Rios D'Or", "Caxias D'Or", "Niterói D'Or", "Glória D'Or",
            "Hospital Samaritano", "Pró-Cardíaco", "Casa de Saúde Santa Lúcia",
            "Hospital Pasteur", "Hospital Espanhol", "Americas Medical City",
            "Hospital Municipal Miguel Couto", "Hospital Souza Aguiar",
        ],
        "local_section_title": "Bairros e Regiões Atendidas no Rio de Janeiro",
        "local_tags": [
            "Zona Sul RJ", "Zona Norte RJ", "Zona Oeste RJ", "Centro RJ",
            "Barra da Tijuca", "Ipanema", "Copacabana", "Botafogo", "Flamengo",
            "Tijuca", "Méier", "Campo Grande", "Jacarepaguá", "Recreio",
            "Grande Niterói", "São Gonçalo", "Duque de Caxias", "Nova Iguaçu",
            "Baixada Fluminense", "Serra Fluminense", "Sul Fluminense",
        ],
        "faq_extra": [
            {
                "q": "Qual operadora tem a maior rede credenciada no Rio de Janeiro?",
                "a": "A Rede D'Or São Luiz, Copa D'Or e Copa Star são referências no RJ. As operadoras Amil, Bradesco Saúde e SulAmérica têm os maiores índices de credenciamento na cidade, incluindo hospitais como Samaritano, Americas Medical City e Copa D'Or."
            },
            {
                "q": "Tem plano de saúde para quem mora em Niterói ou São Gonçalo?",
                "a": "Sim! Amil, SulAmérica, Bradesco Saúde, Unimed Rio, Assim Saúde e Leve Saúde oferecem cobertura em Niterói, São Gonçalo, Maricá e toda a região metropolitana. Fale com a Virtua para comparar as melhores opções para sua cidade."
            },
            {
                "q": "Como contratar plano de saúde empresarial para empresa no RJ?",
                "a": "Empresas com CNPJ ativo no RJ podem contratar planos coletivos empresariais a partir de 2 vidas. Temos parceria com as principais operadoras e negociamos as melhores tabelas para sua empresa. Solicite cotação gratuita."
            },
        ],
        "texto_apoio": """O Rio de Janeiro conta com uma das maiores redes de saúde do Brasil, com hospitais de referência como a Rede D'Or (Copa D'Or, Barra D'Or, Norte D'Or), Hospital Samaritano, Americas Medical City e Pró-Cardíaco. As principais operadoras com forte presença no RJ são Amil, Bradesco Saúde, SulAmérica, Unimed Rio, Porto Seguro Saúde, Hapvida NotreDame Intermédica, Assim Saúde, Klini Saúde e Golden Cross.

A Virtua Corretora de Seguros atende <strong>todos os bairros do Rio de Janeiro</strong> e toda a região metropolitana: Niterói, São Gonçalo, Duque de Caxias, Nova Iguaçu, Belford Roxo, São João de Meriti e mais. Nossa assessoria é gratuita — comparamos os planos disponíveis para o seu CEP e perfil, garantindo o melhor custo-benefício.""",
    },

    # ── CAMPOS DOS GOYTACAZES ────────────────────────────────────────────────────
    "amil-campos": {
        "title": "Plano de Saúde Amil Campos dos Goytacazes 2026 | Virtua",
        "description": "Amil em Campos dos Goytacazes: planos individual, familiar e empresarial com rede credenciada local. Corretor autorizado Amil norte fluminense. Cotação grátis.",
        "keywords_extra": [
            # Campos e arredores
            "plano de saúde Campos dos Goytacazes", "plano de saúde Campos RJ",
            "convênio médico Campos dos Goytacazes", "Amil Campos dos Goytacazes",
            "corretor Amil Campos", "plano de saúde norte fluminense",
            "plano de saúde São João da Barra", "plano de saúde Quissamã",
            "plano de saúde Cardoso Moreira", "plano de saúde São Fidélis",
            "plano de saúde Italva", "plano de saúde Cambuci",
            "plano de saúde Bom Jesus do Itabapoana",
            # Bairros de Campos
            "plano de saúde Guarus Campos", "plano de saúde Travessão Campos",
            "plano de saúde Centro Campos", "plano de saúde Jockey Club Campos",
            "plano de saúde Parque Leopoldina Campos",
            # Long tails
            "cotação plano de saúde Campos dos Goytacazes 2026",
            "plano de saúde Campos norte fluminense barato",
            "Amil individual Campos dos Goytacazes",
            "Amil empresarial Campos dos Goytacazes",
            "plano de saúde MEI Campos dos Goytacazes",
            "plano de saúde Petrobras Campos", "plano saúde trabalhador petróleo Campos",
            # Hospitais locais
            "Hospital São Miguel Campos", "ACEPRAN Campos",
            "Ceplin Campos dos Goytacazes", "Hospital Geral de Guarus",
            "Hospital Dr. Beda Campos", "UPA Campos dos Goytacazes",
            "Santa Casa Campos dos Goytacazes",
        ],
        "geo": {"lat": -21.7545, "lng": -41.3244, "city": "Campos dos Goytacazes", "state": "RJ"},
        "area_served": [
            "Campos dos Goytacazes", "São João da Barra", "Quissamã",
            "Cardoso Moreira", "São Fidélis", "Italva", "Cambuci",
            "Bom Jesus do Itabapoana", "Miracema", "Santo Antônio de Pádua",
        ],
        "local_hospitals": [
            "Hospital São Miguel", "Santa Casa de Misericórdia de Campos",
            "ACEPRAN", "Ceplin", "Hospital Geral de Guarus",
            "Hospital Dr. Beda", "UPA Campos dos Goytacazes",
            "Hospital Ferreira Machado (HFERJ)", "Policlínica Campos",
        ],
        "local_section_title": "Cidades Atendidas — Norte Fluminense",
        "local_tags": [
            "Campos dos Goytacazes", "São João da Barra", "Quissamã",
            "Cardoso Moreira", "São Fidélis", "Italva", "Cambuci",
            "Miracema", "Bom Jesus do Itabapoana", "Santo Antônio de Pádua",
            "Guarus", "Centro Campos", "Travessão", "Jockey Club",
        ],
        "faq_extra": [
            {
                "q": "A Amil tem hospitais credenciados em Campos dos Goytacazes?",
                "a": "Sim. A rede Amil em Campos dos Goytacazes inclui hospitais, clínicas especializadas e laboratórios como Hospital São Miguel, Ceplin, ACEPRAN e Hospital Geral de Guarus. Consulte a lista completa pelo app Amil ou pelo site da operadora."
            },
            {
                "q": "Qual o plano de saúde mais completo para quem trabalha com petróleo em Campos?",
                "a": "Para trabalhadores do setor de petróleo e gás em Campos dos Goytacazes, recomendamos planos com cobertura nacional como o Amil 400 ou Amil 750, que permitem atendimento em qualquer cidade do Brasil. Ideal para quem viaja com frequência a trabalho."
            },
            {
                "q": "Qual a área de cobertura da Amil na região norte fluminense?",
                "a": "A Amil cobre toda a região norte fluminense: Campos dos Goytacazes, São João da Barra, Quissamã, Cardoso Moreira, São Fidélis e municípios vizinhos. Planos nacionais também garantem atendimento em todo o Brasil."
            },
        ],
        "texto_apoio": """Campos dos Goytacazes é o maior município do interior fluminense e possui uma infraestrutura de saúde sólida, com hospitais como o Hospital São Miguel, Santa Casa de Misericórdia, ACEPRAN, Ceplin e o Hospital Ferreira Machado (HFERJ). A cidade tem grande demanda por planos de saúde devido ao polo petrolífero — muitos trabalhadores do setor de óleo e gás buscam planos com <strong>cobertura nacional</strong> para atendimento mesmo durante deslocamentos.

A Virtua Corretora é <strong>corretor autorizado Amil em Campos dos Goytacazes</strong> e em toda a região norte fluminense. Atendemos também São João da Barra, Quissamã, Cardoso Moreira, São Fidélis e municípios vizinhos. Solicite sua cotação sem sair de casa.""",
    },

    # ── REGIÃO DOS LAGOS ────────────────────────────────────────────────────────
    "amil-lagos": {
        "title": "Plano de Saúde Amil Região dos Lagos RJ 2026 | Virtua",
        "description": "Amil na Região dos Lagos: Cabo Frio, Búzios, Arraial do Cabo, São Pedro da Aldeia, Iguaba Grande e Araruama. Corretor autorizado. Cotação grátis.",
        "keywords_extra": [
            # Cidades dos Lagos
            "plano de saúde Cabo Frio", "plano de saúde Búzios",
            "plano de saúde Arraial do Cabo", "plano de saúde São Pedro da Aldeia",
            "plano de saúde Iguaba Grande", "plano de saúde Araruama",
            "plano de saúde Saquarema", "plano de saúde Maricá",
            "plano de saúde Armação dos Búzios", "plano de saúde Silva Jardim",
            "Amil Cabo Frio", "Amil Búzios", "Amil Arraial do Cabo",
            "Amil São Pedro da Aldeia", "Amil Iguaba Grande",
            "convênio médico Cabo Frio", "convênio médico Búzios",
            "convênio médico Região dos Lagos",
            # Long tails
            "cotação plano de saúde Cabo Frio 2026",
            "cotação plano de saúde Búzios 2026",
            "plano de saúde Região dos Lagos barato",
            "plano de saúde individual Cabo Frio",
            "plano de saúde empresarial Cabo Frio",
            "plano de saúde MEI Região dos Lagos",
            "plano de saúde turismo Búzios", "plano de saúde morador Cabo Frio",
            # Hospitais locais
            "Hospital Nossa Senhora da Conceição Cabo Frio",
            "UPA Cabo Frio", "Hospital de Búzios",
            "CRSF São Pedro da Aldeia", "UPA Arraial do Cabo",
        ],
        "geo": {"lat": -22.8794, "lng": -42.0191, "city": "Cabo Frio", "state": "RJ"},
        "area_served": [
            "Cabo Frio", "Búzios", "Arraial do Cabo",
            "São Pedro da Aldeia", "Iguaba Grande", "Araruama",
            "Saquarema", "Maricá", "Silva Jardim", "Casimiro de Abreu",
        ],
        "local_hospitals": [
            "Hospital Nossa Senhora da Conceição (Cabo Frio)",
            "UPA Cabo Frio", "Hospital Regional de Cabo Frio",
            "Hospital Icaraí (São Pedro da Aldeia)",
            "UPA São Pedro da Aldeia", "Hospital de Búzios",
            "UPA Arraial do Cabo", "Clínicas Especializadas Cabo Frio",
        ],
        "local_section_title": "Cidades da Região dos Lagos Atendidas",
        "local_tags": [
            "Cabo Frio", "Armação dos Búzios", "Arraial do Cabo",
            "São Pedro da Aldeia", "Iguaba Grande", "Araruama",
            "Saquarema", "Maricá", "Silva Jardim", "Casimiro de Abreu",
            "Praia do Forte", "Ogiva", "Tamoios", "Braga",
        ],
        "faq_extra": [
            {
                "q": "Qual o melhor plano de saúde em Cabo Frio?",
                "a": "Em Cabo Frio, as operadoras com maior rede credenciada são Amil, Assim Saúde e Unimed. Para planos com cobertura nacional — ideal para quem viaja — recomendamos Amil 400 ou SulAmérica. Faça uma cotação gratuita com a Virtua para comparar as opções disponíveis para o seu CEP."
            },
            {
                "q": "Tem plano de saúde para moradores de Búzios?",
                "a": "Sim! Em Búzios (Armação dos Búzios) estão disponíveis planos Amil, Assim Saúde e outros com cobertura local e regional. Muitos moradores optam por planos nacionais pela praticidade de atendimento tanto em Búzios quanto quando estão em outras cidades."
            },
            {
                "q": "Como contratar plano de saúde em Arraial do Cabo ou São Pedro da Aldeia?",
                "a": "A Virtua Corretora realiza cotações online para toda a Região dos Lagos — Arraial do Cabo, São Pedro da Aldeia, Iguaba Grande e cidades vizinhas. Não é necessário ir a um escritório: atendemos por WhatsApp e toda a contratação pode ser feita digitalmente."
            },
        ],
        "texto_apoio": """A Região dos Lagos do Rio de Janeiro — que inclui Cabo Frio, Armação dos Búzios, Arraial do Cabo, São Pedro da Aldeia, Iguaba Grande e Araruama — tem grande demanda por planos de saúde tanto de <strong>moradores fixos</strong> quanto de <strong>veranistas</strong> que residem parte do ano na região.

A infraestrutura de saúde local conta com o Hospital Nossa Senhora da Conceição em Cabo Frio, além de UPAs e clínicas especializadas nas principais cidades. Planos com cobertura nacional como Amil 400 e Amil 750 são especialmente indicados para quem transita entre a Região dos Lagos e o Rio de Janeiro.

A Virtua Corretora é <strong>corretor autorizado Amil na Região dos Lagos</strong> e oferece atendimento digital para toda a região. Compare planos, preços e coberturas sem sair de casa.""",
    },

    # ── MACAÉ ────────────────────────────────────────────────────────────────────
    "amil-macae": {
        "title": "Plano de Saúde Amil Macaé RJ 2026 | Corretor Autorizado | Virtua",
        "description": "Amil em Macaé: planos para trabalhadores de petróleo, MEI, empresas e famílias. Rede credenciada local. Corretor autorizado. Cotação grátis pelo WhatsApp.",
        "keywords_extra": [
            # Macaé e arredores
            "plano de saúde Macaé", "convênio médico Macaé",
            "Amil Macaé", "corretor Amil Macaé", "plano de saúde Macaé RJ",
            "plano de saúde Rio das Ostras", "plano de saúde Carapebus",
            "plano de saúde Quissamã", "plano de saúde Conceição de Macabu",
            # Petróleo
            "plano de saúde petróleo Macaé", "plano de saúde offshore Macaé",
            "plano de saúde trabalhador petróleo Macaé",
            "plano de saúde Petrobras Macaé", "plano de saúde setor energético",
            "plano de saúde técnico petróleo", "plano de saúde engenheiro petróleo",
            # Long tails
            "cotação plano de saúde Macaé 2026",
            "melhor plano de saúde Macaé RJ",
            "plano de saúde individual Macaé",
            "plano de saúde empresarial Macaé",
            "plano de saúde MEI Macaé RJ",
            "plano de saúde familiar Macaé",
            "rede credenciada Amil Macaé",
            # Hospitais locais
            "Hospital Rocha Faria Macaé", "UPA Macaé",
            "Hospital Alberto Torres Macaé", "Instituto Oncológico Macaé",
            "Hospital Central de Macaé", "SAMS Macaé",
        ],
        "geo": {"lat": -22.3706, "lng": -41.7869, "city": "Macaé", "state": "RJ"},
        "area_served": [
            "Macaé", "Rio das Ostras", "Carapebus", "Quissamã",
            "Conceição de Macabu", "Casimiro de Abreu",
        ],
        "local_hospitals": [
            "Hospital Rocha Faria (Macaé)", "Hospital Central de Macaé",
            "UPA Macaé", "Hospital Alberto Torres",
            "Instituto Oncológico de Macaé", "SAMS Macaé",
            "Hospital Municipal Rodolpho Perissé", "Clínicas Especializadas Macaé",
        ],
        "local_section_title": "Cidades Atendidas — Macaé e Região",
        "local_tags": [
            "Macaé", "Rio das Ostras", "Carapebus",
            "Quissamã", "Conceição de Macabu", "Casimiro de Abreu",
            "Campos dos Goytacazes", "Farol de São Tomé", "Imboassica",
            "Granja dos Cavaleiros", "Miramar",
        ],
        "faq_extra": [
            {
                "q": "Qual o melhor plano de saúde para trabalhadores de petróleo em Macaé?",
                "a": "Para trabalhadores do setor de petróleo e gás offshore em Macaé, recomendamos planos com cobertura nacional (como Amil 400 e Amil 750), pois permitem atendimento em qualquer cidade durante deslocamentos. É importante verificar coberturas de urgência e emergência, já que muitos trabalhadores atuam em plataformas."
            },
            {
                "q": "A Amil cobre Rio das Ostras além de Macaé?",
                "a": "Sim. A cobertura Amil em Macaé se estende para Rio das Ostras, Carapebus, Quissamã e municípios vizinhos da região norte fluminense. Alguns planos regionais têm cobertura específica para essas cidades; planos nacionais cobrem todo o Brasil."
            },
            {
                "q": "Como contratar Amil empresarial para empresa de petróleo em Macaé?",
                "a": "Empresas do setor de óleo e gás em Macaé podem contratar planos coletivos empresariais Amil a partir de 2 vidas. A Virtua Corretora negocia diretamente com a operadora as melhores condições de tabela para o seu segmento. Fale pelo WhatsApp para uma proposta personalizada."
            },
        ],
        "texto_apoio": """Macaé é conhecida como a <strong>capital brasileira do petróleo</strong>, e isso se reflete na alta demanda por planos de saúde de qualidade na cidade. Trabalhadores offshore, engenheiros, técnicos e prestadores de serviço do setor de óleo e gás buscam planos com <strong>cobertura nacional</strong> e ampla rede de urgência e emergência.

A infraestrutura de saúde de Macaé inclui o Hospital Rocha Faria, Hospital Central, UPA e diversas clínicas especializadas. As principais operadoras com rede credenciada na cidade são Amil, Assim Saúde, Unimed e Intermédica.

A Virtua Corretora é <strong>corretor autorizado Amil em Macaé</strong> e atende toda a região: Rio das Ostras, Carapebus, Quissamã e municípios vizinhos. Atendimento 100% digital pelo WhatsApp.""",
    },

    # ── UNIMED CAMPOS ────────────────────────────────────────────────────────────
    "plano-de-saude-unimed-campos": {
        "title": "Unimed Campos dos Goytacazes | Plano de Saúde 2026 | Virtua",
        "description": "Unimed Campos dos Goytacazes: planos individual, familiar e empresarial com médicos cooperados locais. Cotação grátis com corretor autorizado norte fluminense.",
        "keywords_extra": [
            "Unimed Campos dos Goytacazes", "Unimed Campos RJ",
            "plano de saúde Unimed Campos", "Unimed norte fluminense",
            "convênio Unimed Campos", "cooperativa Unimed Campos",
            "médicos Unimed Campos", "rede Unimed Campos",
            "Unimed individual Campos", "Unimed empresarial Campos",
            "Unimed familiar Campos", "Unimed intercâmbio Campos",
            "cotação Unimed Campos 2026", "tabela Unimed Campos 2026",
            "plano de saúde Campos dos Goytacazes norte fluminense",
            "plano de saúde São João da Barra Unimed",
            "plano de saúde Quissamã Unimed",
            "plano de saúde São Fidélis Unimed",
            "corretor Unimed Campos dos Goytacazes",
            "Hospital São Miguel Unimed Campos",
        ],
        "geo": {"lat": -21.7545, "lng": -41.3244, "city": "Campos dos Goytacazes", "state": "RJ"},
        "area_served": [
            "Campos dos Goytacazes", "São João da Barra", "Quissamã",
            "São Fidélis", "Cardoso Moreira", "Italva", "Cambuci",
        ],
        "local_hospitals": [
            "Hospital São Miguel", "Santa Casa de Misericórdia de Campos",
            "ACEPRAN", "Ceplin", "Hospital Geral de Guarus",
            "Hospital Dr. Beda", "Policlínica de Campos",
            "Clínicas Cooperadas Unimed Campos",
        ],
        "local_section_title": "Cidades com Cobertura Unimed — Norte Fluminense",
        "local_tags": [
            "Campos dos Goytacazes", "São João da Barra", "Quissamã",
            "Cardoso Moreira", "São Fidélis", "Italva", "Cambuci",
            "Miracema", "Santo Antônio de Pádua", "Bom Jesus do Itabapoana",
            "Centro Campos", "Guarus", "Jockey Club", "Travessão",
        ],
        "faq_extra": [
            {
                "q": "A Unimed Campos cobre São João da Barra e Quissamã?",
                "a": "Sim. A Unimed Campos dos Goytacazes tem cobertura em São João da Barra, Quissamã e municípios da região norte fluminense. Para atendimento fora dessa área, planos com intercâmbio Unimed permitem uso da rede de outras cooperativas em todo o Brasil."
            },
            {
                "q": "Como funciona o intercâmbio Unimed para quem mora em Campos?",
                "a": "O intercâmbio Unimed permite que beneficiários de Campos dos Goytacazes utilizem a rede credenciada de qualquer cooperativa Unimed no Brasil, quando estiverem em outra cidade. É ideal para quem viaja a trabalho ou estudo com frequência."
            },
        ],
        "texto_apoio": """A Unimed Campos dos Goytacazes é a principal cooperativa médica da região norte fluminense, com uma ampla rede de médicos cooperados, clínicas e hospitais credenciados na cidade e arredores. Seus planos são indicados para quem deseja atendimento com médicos de confiança da própria comunidade.

Para quem precisa de atendimento em outras cidades, os planos Unimed Campos com <strong>intercâmbio</strong> garantem acesso à rede de 350+ cooperativas em todo o Brasil. A Virtua Corretora faz a cotação gratuita e auxilia na escolha do plano ideal para você, sua família ou sua empresa em Campos dos Goytacazes.""",
    },

    # ── UNIMED MACAÉ ─────────────────────────────────────────────────────────────
    "plano-saude-unimed-macae": {
        "title": "Unimed Macaé | Plano de Saúde 2026 | Virtua Corretora",
        "description": "Unimed Macaé: planos de saúde com médicos cooperados locais. Individual, familiar, empresarial e para trabalhadores de petróleo. Cotação grátis.",
        "keywords_extra": [
            "Unimed Macaé", "plano de saúde Unimed Macaé",
            "Unimed Macaé RJ", "convênio Unimed Macaé",
            "Unimed individual Macaé", "Unimed empresarial Macaé",
            "Unimed intercâmbio Macaé", "cotação Unimed Macaé 2026",
            "tabela Unimed Macaé 2026", "médicos Unimed Macaé",
            "rede credenciada Unimed Macaé",
            "plano de saúde Rio das Ostras Unimed",
            "plano de saúde petróleo Macaé Unimed",
            "plano saúde offshore Macaé",
            "corretor Unimed Macaé autorizado",
        ],
        "geo": {"lat": -22.3706, "lng": -41.7869, "city": "Macaé", "state": "RJ"},
        "area_served": [
            "Macaé", "Rio das Ostras", "Carapebus",
            "Quissamã", "Casimiro de Abreu",
        ],
        "local_hospitals": [
            "Hospital Rocha Faria (Macaé)", "Hospital Central de Macaé",
            "UPA Macaé", "Clínicas Cooperadas Unimed Macaé",
            "Hospital Alberto Torres", "Instituto Oncológico de Macaé",
        ],
        "local_section_title": "Cidades com Cobertura Unimed — Macaé e Região",
        "local_tags": [
            "Macaé", "Rio das Ostras", "Carapebus",
            "Quissamã", "Casimiro de Abreu", "Conceição de Macabu",
            "Granja dos Cavaleiros", "Imboassica", "Miramar",
        ],
        "faq_extra": [
            {
                "q": "A Unimed Macaé cobre Rio das Ostras?",
                "a": "Sim. A Unimed Macaé tem cobertura em Rio das Ostras, Carapebus e municípios vizinhos. Com o intercâmbio Unimed, você pode utilizar a rede de qualquer cooperativa em todo o Brasil."
            },
            {
                "q": "A Unimed Macaé é indicada para trabalhadores offshore?",
                "a": "Para trabalhadores offshore e do setor de petróleo, recomendamos planos com cobertura nacional e intercâmbio. A Unimed Macaé com intercâmbio é uma boa opção, assim como planos Amil ou SulAmérica com cobertura nacional. Nossa equipe orienta na melhor escolha para o seu perfil."
            },
        ],
        "texto_apoio": """A Unimed Macaé oferece atendimento médico de qualidade com uma rede de médicos cooperados locais, sendo uma das operadoras mais valorizadas pelos moradores da cidade. Indicada especialmente para quem busca médicos da comunidade e continuidade no atendimento.

Para trabalhadores do setor de petróleo e gás, o <strong>intercâmbio Unimed</strong> é um diferencial importante, permitindo atendimento em qualquer cooperativa do Brasil. A Virtua Corretora compara Unimed Macaé com outras operadoras disponíveis na cidade para ajudá-lo a fazer a melhor escolha.""",
    },

    # ── MEDSENIOR RJ ─────────────────────────────────────────────────────────────
    "medsenior-rj": {
        "title": "MedSênior RJ | Plano de Saúde para Idosos 2026 | Virtua",
        "description": "MedSênior no Rio de Janeiro: plano de saúde especializado para idosos acima de 60 anos. Rede credenciada RJ, preços acessíveis. Cotação grátis.",
        "keywords_extra": [
            "MedSênior Rio de Janeiro", "MedSênior RJ",
            "plano de saúde idosos RJ", "plano de saúde terceira idade RJ",
            "plano de saúde aposentados Rio de Janeiro",
            "plano de saúde 60 anos RJ", "plano de saúde 65 anos RJ",
            "plano de saúde 70 anos RJ", "plano de saúde 80 anos RJ",
            "plano para idosos Rio de Janeiro 2026",
            "MedSênior Barra da Tijuca", "MedSênior Ipanema",
            "MedSênior Niterói", "MedSênior Tijuca",
            "plano de saúde sênior Rio de Janeiro",
            "plano de saúde pensionista Rio de Janeiro",
            "plano de saúde INSS Rio de Janeiro",
            "convênio médico idoso RJ barato",
            "melhor plano de saúde para idosos RJ",
            "plano de saúde geriatria Rio de Janeiro",
            "MedSênior cardiologia", "MedSênior ortopedia",
            "MedSênior oncologia RJ",
        ],
        "geo": {"lat": -22.9068, "lng": -43.1729, "city": "Rio de Janeiro", "state": "RJ"},
        "area_served": [
            "Rio de Janeiro", "Niterói", "São Gonçalo",
            "Duque de Caxias", "Nova Iguaçu",
        ],
        "local_hospitals": [
            "Hospital Samaritano RJ", "Copa D'Or", "Hospital Pro-Cardíaco",
            "Casa de Saúde São José", "Hospital Pedro Ernesto (UERJ)",
            "Hospital Universitário Clementino Fraga Filho (UFRJ)",
            "Clinicas Especializadas em Geriatria RJ",
        ],
        "local_section_title": "Bairros e Regiões com Cobertura MedSênior no RJ",
        "local_tags": [
            "Zona Sul RJ", "Ipanema", "Leblon", "Copacabana", "Botafogo",
            "Flamengo", "Glória", "Catete", "Barra da Tijuca", "Recreio",
            "Tijuca", "Méier", "Madureira", "Campo Grande",
            "Niterói", "São Gonçalo", "Duque de Caxias",
            "Icaraí (Niterói)", "Ingá (Niterói)",
        ],
        "faq_extra": [
            {
                "q": "O MedSênior cobre cirurgias e internações no Rio de Janeiro?",
                "a": "Sim. Os planos MedSênior cobrem internações, cirurgias, exames, consultas e urgências conforme o rol de procedimentos da ANS. No RJ, a rede credenciada inclui hospitais de qualidade indicados para o perfil sênior."
            },
            {
                "q": "O MedSênior tem cobertura em Niterói além do Rio de Janeiro?",
                "a": "Sim, o MedSênior tem cobertura na Região Metropolitana do Rio de Janeiro, incluindo Niterói e São Gonçalo. Verifique a rede credenciada disponível para o seu bairro ao solicitar a cotação."
            },
            {
                "q": "Qual a diferença do MedSênior para outros planos de idosos no RJ?",
                "a": "O MedSênior foi desenvolvido exclusivamente para a terceira idade, com preços ajustados para a faixa 60+ e programas de prevenção voltados às necessidades do público sênior, como acompanhamento de doenças crônicas, cardiologia e ortopedia. Compare com Prevent Senior e outros planos para idosos na Virtua."
            },
        ],
        "texto_apoio": """O Rio de Janeiro tem uma das maiores populações de idosos do Brasil, com alta demanda por <strong>planos de saúde especializados para a terceira idade</strong>. O MedSênior foi criado para atender esse público, com preços ajustados e uma rede credenciada focada em especialidades como cardiologia, ortopedia, geriatria e oncologia.

Outras opções de planos para idosos no RJ incluem o <strong>Prevent Senior</strong>, Bradesco Saúde, SulAmérica e Amil. A Virtua Corretora compara todas as opções disponíveis para o seu bairro e faixa etária, garantindo a melhor relação custo-benefício para você ou seu familiar.""",
    },
}


# ── FUNÇÕES AUXILIARES ──────────────────────────────────────────────────────────

def build_local_business_schema(data, page_slug):
    geo = data["geo"]
    area = ", ".join(f'"{c}"' for c in data["area_served"])
    return f"""    <!-- LocalBusiness + GeoCoordinates Schema (SEO Local) -->
    <script type="application/ld+json">
    {{
        "@context": "https://schema.org",
        "@type": ["InsuranceAgency", "LocalBusiness"],
        "name": "Virtua Corretora de Seguros",
        "url": "https://www.virtuacorretora.com.br/{page_slug}/",
        "telephone": "+5522999404840",
        "email": "contato@virtuacorretora.com.br",
        "logo": "https://www.virtuacorretora.com.br/wp-content/uploads/2023/11/cropped-virtua-corretora-de-planos-de-saude-1.webp",
        "image": "https://www.virtuacorretora.com.br/wp-content/uploads/2023/11/cropped-virtua-corretora-de-planos-de-saude-1.webp",
        "description": "Corretora de planos de saúde em {geo['city']}, {geo['state']}. Especializada em planos individuais, familiares e empresariais.",
        "address": {{
            "@type": "PostalAddress",
            "addressLocality": "{geo['city']}",
            "addressRegion": "{geo['state']}",
            "addressCountry": "BR"
        }},
        "geo": {{
            "@type": "GeoCoordinates",
            "latitude": {geo['lat']},
            "longitude": {geo['lng']}
        }},
        "areaServed": [{area}],
        "openingHours": "Mo-Fr 08:00-18:00",
        "priceRange": "$$",
        "currenciesAccepted": "BRL",
        "paymentAccepted": "PIX, Cartão de Crédito, Boleto",
        "sameAs": [
            "https://www.instagram.com/virtuacorretora",
            "https://www.facebook.com/virtuacorretora"
        ]
    }}
    </script>"""


def build_cities_section(data):
    tags_html = "\n".join([
        f'                <span style="display:inline-flex;align-items:center;gap:5px;background:white;'
        f'border:1px solid #e2e8f0;padding:6px 14px;border-radius:8px;font-size:13px;'
        f'font-weight:500;color:#374151;">'
        f'<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="#0066cc" stroke-width="2">'
        f'<path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/>'
        f'<circle cx="12" cy="10" r="3"/></svg>{t}</span>'
        for t in data["local_tags"]
    ])
    hospitals_html = "\n".join([
        f'                <li style="padding:6px 0;border-bottom:1px solid #f1f5f9;'
        f'display:flex;align-items:center;gap:8px;font-size:14px;color:#374151;">'
        f'<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#0066cc" stroke-width="2">'
        f'<path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/>'
        f'<polyline points="9 22 9 12 15 12 15 22"/></svg>{h}</li>'
        for h in data["local_hospitals"]
    ])
    return f"""    <!-- Seção Local: Cidades e Hospitais (SEO Local Avançado) -->
    <section style="background:#f8fafc;padding:56px 0;border-top:1px solid #e2e8f0;">
        <div class="container" style="max-width:1100px;margin:0 auto;padding:0 24px;">
            <div style="display:grid;grid-template-columns:1fr 1fr;gap:48px;align-items:start;">

                <!-- Cidades/Bairros -->
                <div>
                    <h2 style="font-size:22px;font-weight:800;color:#1e293b;margin:0 0 8px;">{data['local_section_title']}</h2>
                    <p style="color:#64748b;font-size:14px;margin:0 0 20px;line-height:1.6;">Atendemos clientes em todos esses municípios e bairros com cotação 100% online.</p>
                    <div style="display:flex;flex-wrap:wrap;gap:8px;">
{tags_html}
                    </div>
                </div>

                <!-- Hospitais Locais -->
                <div>
                    <h2 style="font-size:22px;font-weight:800;color:#1e293b;margin:0 0 8px;">Hospitais e Clínicas da Rede</h2>
                    <p style="color:#64748b;font-size:14px;margin:0 0 20px;line-height:1.6;">Principais estabelecimentos credenciados na região.</p>
                    <ul style="list-style:none;padding:0;margin:0;">
{hospitals_html}
                    </ul>
                </div>
            </div>
        </div>
    </section>"""


def build_texto_apoio_section(data):
    return f"""    <!-- Texto de Apoio Local (SEO Local — Módulo 7 Next SEO) -->
    <section style="background:white;padding:48px 0;border-top:1px solid #e2e8f0;">
        <div class="container" style="max-width:860px;margin:0 auto;padding:0 24px;">
            <div style="background:#eff6ff;border-left:4px solid #0066cc;padding:24px 28px;border-radius:0 12px 12px 0;">
                <p style="font-size:15px;color:#1e293b;line-height:1.8;margin:0;">
                    {data['texto_apoio']}
                </p>
            </div>
        </div>
    </section>"""


def build_local_faq_items(faqs):
    items = []
    for faq in faqs:
        items.append(f"""<div class="op-faq-item">
    <div class="op-faq-question">{faq['q']}</div>
    <div class="op-faq-answer"><p>{faq['a']}</p></div>
</div>""")
    return "\n".join(items)


def build_local_faq_schema(faqs):
    entities = []
    for faq in faqs:
        entities.append(f"""{{
                "@type": "Question",
                "name": "{faq['q']}",
                "acceptedAnswer": {{
                    "@type": "Answer",
                    "text": "{faq['a']}"
                }}
            }}""")
    return ",\n            ".join(entities)


def process_page(slug, data):
    filepath = os.path.join(BASE, slug, "index.html")
    if not os.path.exists(filepath):
        print(f"  ⚠ Arquivo não encontrado: {filepath}")
        return False

    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()

    changed = False

    # ── 1. TITLE ─────────────────────────────────────────────────────────────────
    old_title = re.search(r'<title>(.*?)</title>', html).group(1)
    if old_title != data["title"]:
        html = html.replace(f'<title>{old_title}</title>', f'<title>{data["title"]}</title>', 1)
        # Sync og:title e twitter:title
        html = re.sub(r'(<meta property="og:title" content=")[^"]*(")', f'\\g<1>{data["title"]}\\2', html, count=1)
        html = re.sub(r'(<meta name="twitter:title" content=")[^"]*(")', f'\\g<1>{data["title"]}\\2', html, count=1)
        changed = True
        print(f"  ✓ Title: {len(data['title'])} chars → {data['title'][:55]}...")

    # ── 2. META DESCRIPTION ──────────────────────────────────────────────────────
    html = re.sub(
        r'(<meta name="description" content=")[^"]*(")',
        f'\\g<1>{data["description"]}\\2',
        html, count=1
    )
    html = re.sub(r'(<meta property="og:description" content=")[^"]*(")', f'\\g<1>{data["description"]}\\2', html, count=1)
    html = re.sub(r'(<meta name="twitter:description" content=")[^"]*(")', f'\\g<1>{data["description"]}\\2', html, count=1)
    changed = True
    print(f"  ✓ Meta description atualizada")

    # ── 3. KEYWORDS LOCAIS EXPANDIDAS ────────────────────────────────────────────
    extra = data["keywords_extra"]
    current_kw = re.search(r'<meta name="keywords" content="([^"]+)"', html)
    if current_kw:
        existing = [k.strip() for k in current_kw.group(1).split(",")]
        seen = {k.lower() for k in existing}
        for k in extra:
            if k.lower() not in seen:
                existing.append(k)
                seen.add(k.lower())
        new_kw = ", ".join(existing[:60])  # max 60 keywords
        html = re.sub(
            r'<meta name="keywords" content="[^"]*"',
            f'<meta name="keywords" content="{new_kw}"',
            html, count=1
        )
        changed = True
        print(f"  ✓ Keywords: {len(existing[:60])} termos ({len(extra)} locais adicionados)")

    # ── 4. LocalBusiness SCHEMA ──────────────────────────────────────────────────
    if "LocalBusiness" not in html:
        local_schema = build_local_business_schema(data, slug)
        html = re.sub(r'(</head>)', local_schema + '\n\\1', html, count=1)
        changed = True
        print(f"  ✓ LocalBusiness + GeoCoordinates schema adicionado ({data['geo']['city']})")

    # ── 5. SEÇÃO CIDADES + HOSPITAIS ─────────────────────────────────────────────
    if "Seção Local: Cidades e Hospitais" not in html:
        cities_section = build_cities_section(data)
        # Insere antes da seção E-A-T
        if "eat-author-section" in html:
            html = re.sub(r'(<!-- E-A-T: Autor)', cities_section + '\n\n    \\1', html, count=1)
        else:
            html = re.sub(r'(<footer)', cities_section + '\n\n    \\1', html, count=1)
        changed = True
        print(f"  ✓ Seção de cidades e hospitais adicionada ({len(data['local_tags'])} locais, {len(data['local_hospitals'])} hospitais)")

    # ── 6. TEXTO DE APOIO LOCAL ──────────────────────────────────────────────────
    if "Texto de Apoio Local" not in html:
        texto = build_texto_apoio_section(data)
        if "Seção Local: Cidades e Hospitais" in html:
            html = html.replace("    <!-- Seção Local: Cidades e Hospitais", texto + "\n\n    <!-- Seção Local: Cidades e Hospitais", 1)
        elif "eat-author-section" in html:
            html = re.sub(r'(<!-- E-A-T: Autor)', texto + '\n\n    \\1', html, count=1)
        else:
            html = re.sub(r'(<footer)', texto + '\n\n    \\1', html, count=1)
        changed = True
        print(f"  ✓ Texto de apoio local adicionado")

    # ── 7. FAQs LOCAIS (HTML + Schema) ────────────────────────────────────────────
    if data["faq_extra"] and "faq_extra_local" not in html:
        faq_html = build_local_faq_items(data["faq_extra"])
        faq_html_marked = f'<!-- faq_extra_local -->\n{faq_html}'
        # Insere dentro do op-faq div (antes do último </div> do faq)
        html = re.sub(
            r'(</div>\s*</div>\s*</section>\s*<!-- CTA Final)',
            faq_html_marked + '\n\n            </div>\n        </div>\n    </section>\n    <!-- CTA Final',
            html, count=1
        )
        # Adiciona ao FAQPage schema
        new_schema_items = build_local_faq_schema(data["faq_extra"])
        html = re.sub(
            r'(\]\s*\}\s*</script>)',
            f',\n            {new_schema_items}\n        ]\n    }}\n    </script>',
            html, count=1
        )
        changed = True
        print(f"  ✓ {len(data['faq_extra'])} FAQs locais adicionadas")

    if changed:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html)
    return changed


def main():
    print(f"Aplicando SEO local em {len(LOCAL_DATA)} páginas...\n")
    updated = 0
    for slug, data in LOCAL_DATA.items():
        print(f"[{slug}]")
        if process_page(slug, data):
            updated += 1
        print()
    print(f"✅ {updated} páginas atualizadas com SEO local")

if __name__ == "__main__":
    main()
