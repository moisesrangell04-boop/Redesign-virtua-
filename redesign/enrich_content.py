#!/usr/bin/env python3
"""
Enriquece o corpo principal de cada página com seções completas de conteúdo SEO.

Seções adicionadas por página de operadora:
1. Sobre a Operadora
2. Cobertura Completa (ANS + diferenciais)
3. Tabela de Preços por Faixa Etária 2026
4. Carência e Portabilidade
5. Como Contratar (passo a passo)
6. Vantagens e Desvantagens

Meta: levar cada página de ~1.400 para ~2.800+ palavras.
"""

import os, re, glob

BASE = os.path.dirname(os.path.abspath(__file__))

# ── ESTILOS COMPARTILHADOS ──────────────────────────────────────────────────────
SHARED_STYLES = """
    <style>
    .content-section { padding: 72px 0; }
    .content-section.alt { background: #f8fafc; }
    .content-section .container { max-width: 1100px; margin: 0 auto; padding: 0 24px; }
    .cs-title { font-size: clamp(22px, 2.5vw, 30px); font-weight: 800; color: #1e293b; margin: 0 0 12px; }
    .cs-lead { font-size: 16px; color: #475569; line-height: 1.8; margin: 0 0 32px; }
    .cs-body { font-size: 15px; color: #374151; line-height: 1.85; }
    .cs-body p { margin: 0 0 18px; }
    .cs-body strong { color: #1e293b; }
    .coverage-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(260px,1fr)); gap: 16px; margin-top: 28px; }
    .coverage-item { background: white; border: 1px solid #e2e8f0; border-radius: 12px; padding: 20px 22px; }
    .coverage-item h4 { font-size: 14px; font-weight: 700; color: #1e293b; margin: 0 0 6px; }
    .coverage-item p { font-size: 13px; color: #64748b; margin: 0; line-height: 1.6; }
    .price-table { width: 100%; border-collapse: collapse; margin-top: 24px; font-size: 14px; }
    .price-table th { background: #1e40af; color: white; padding: 12px 16px; text-align: left; font-weight: 600; }
    .price-table td { padding: 11px 16px; border-bottom: 1px solid #e2e8f0; color: #374151; }
    .price-table tr:nth-child(even) td { background: #f8fafc; }
    .price-table tr:hover td { background: #eff6ff; }
    .steps-list { list-style: none; padding: 0; margin: 24px 0 0; counter-reset: steps; }
    .steps-list li { counter-increment: steps; display: flex; gap: 18px; align-items: flex-start; margin-bottom: 20px; }
    .steps-list li::before { content: counter(steps); min-width: 36px; height: 36px; border-radius: 50%; background: #1e40af; color: white; font-weight: 700; font-size: 15px; display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
    .steps-list li div h4 { font-size: 15px; font-weight: 700; color: #1e293b; margin: 0 0 4px; }
    .steps-list li div p { font-size: 14px; color: #475569; margin: 0; line-height: 1.6; }
    .pros-cons { display: grid; grid-template-columns: 1fr 1fr; gap: 24px; margin-top: 28px; }
    .pros-cons > div { border-radius: 14px; padding: 24px 26px; }
    .pros { background: #f0fdf4; border: 1px solid #bbf7d0; }
    .cons { background: #fff7ed; border: 1px solid #fed7aa; }
    .pros h4 { color: #15803d; font-size: 16px; font-weight: 700; margin: 0 0 14px; }
    .cons h4 { color: #c2410c; font-size: 16px; font-weight: 700; margin: 0 0 14px; }
    .pros ul, .cons ul { list-style: none; padding: 0; margin: 0; }
    .pros li, .cons li { font-size: 14px; padding: 5px 0; padding-left: 22px; position: relative; color: #374151; line-height: 1.5; }
    .pros li::before { content: "✓"; position: absolute; left: 0; color: #16a34a; font-weight: 700; }
    .cons li::before { content: "✗"; position: absolute; left: 0; color: #ea580c; font-weight: 700; }
    .carencia-table { width: 100%; border-collapse: collapse; margin-top: 20px; font-size: 14px; }
    .carencia-table th { background: #0f172a; color: white; padding: 11px 16px; text-align: left; font-weight: 600; }
    .carencia-table td { padding: 10px 16px; border-bottom: 1px solid #e2e8f0; }
    .carencia-table tr:nth-child(even) td { background: #f8fafc; }
    .highlight-box { background: #eff6ff; border-left: 4px solid #2563eb; border-radius: 0 12px 12px 0; padding: 20px 24px; margin: 24px 0; }
    .highlight-box p { margin: 0; font-size: 14px; color: #1e3a8a; line-height: 1.7; }
    @media(max-width:768px){ .pros-cons { grid-template-columns:1fr; } .price-table { font-size:12px; } }
    </style>"""

# ── DADOS DE CONTEÚDO POR OPERADORA ────────────────────────────────────────────

CONTENT = {

# ══════════════════════════════════════════════════════════════════════════════
"plano-de-saude-amil": {
"anchor": "<!-- Plans -->",  # insere DEPOIS desta seção
"sections": """
    <!-- SEÇÃO: Sobre a Amil -->
    <section class="content-section alt">
      <div class="container">
        <h2 class="cs-title">Sobre a Amil: Uma das Maiores Operadoras do Brasil</h2>
        <p class="cs-lead">Fundada em 1972, a Amil é hoje uma das maiores e mais reconhecidas operadoras de planos de saúde do Brasil, parte do grupo <strong>UnitedHealth Group</strong> — maior empresa de saúde do mundo. Com mais de 50 anos de história, atende mais de 2 milhões de beneficiários em todo o país.</p>
        <div class="cs-body">
          <p>A Amil possui uma das maiores <strong>redes credenciadas do Brasil</strong>, com mais de 15.000 prestadores entre hospitais, clínicas, laboratórios e médicos. Destaque para hospitais premium como <strong>Copa D'Or</strong>, <strong>Copa Star</strong>, <strong>Hospital Samaritano</strong>, <strong>Americas Medical City</strong> e toda a <strong>Rede D'Or São Luiz</strong>.</p>
          <p>Além dos planos tradicionais, a Amil investe fortemente em <strong>saúde digital</strong>: o aplicativo Amil permite agendamento de consultas, acesso a resultados de exames, segunda opinião médica e consultas de telemedicina pela <strong>Amil Clínica Digital</strong>, disponível 24 horas por dia.</p>
          <p>Para empresas, a Amil oferece planos coletivos com excelente custo-benefício a partir de <strong>2 vidas (MEI)</strong>, com economia de até 40% em relação ao plano individual. O corretor autorizado Virtua negocia diretamente com a operadora as melhores tabelas para o seu perfil.</p>
          <div class="highlight-box"><p>💡 <strong>Dica Virtua:</strong> A Amil é indicada para quem busca uma rede premium e cobertura nacional. Se você mora em cidades como Rio de Janeiro, São Paulo, Belo Horizonte ou Curitiba e quer acesso aos melhores hospitais, a Amil é uma das melhores escolhas do mercado em 2026.</p></div>
        </div>
      </div>
    </section>

    <!-- SEÇÃO: Cobertura -->
    <section class="content-section">
      <div class="container">
        <h2 class="cs-title">O Que o Plano de Saúde Amil Cobre?</h2>
        <p class="cs-lead">A Amil segue obrigatoriamente o <strong>rol de procedimentos da ANS</strong> (Agência Nacional de Saúde Suplementar), que garante cobertura mínima a todos os beneficiários. Além disso, oferece coberturas adicionais dependendo do plano contratado.</p>
        <div class="coverage-grid">
          <div class="coverage-item"><h4>🏥 Internações Hospitalares</h4><p>Internações clínicas, cirúrgicas e em UTI, com cobertura em enfermaria ou apartamento conforme o plano.</p></div>
          <div class="coverage-item"><h4>🔬 Exames e Diagnósticos</h4><p>Hemograma, raio-X, tomografia, ressonância magnética, ecocardiograma, ultrassom e mais de 3.000 procedimentos diagnósticos.</p></div>
          <div class="coverage-item"><h4>👨‍⚕️ Consultas Médicas</h4><p>Consultas em todas as especialidades da rede credenciada: cardiologia, ortopedia, neurologia, ginecologia, pediatria e mais.</p></div>
          <div class="coverage-item"><h4>🚑 Urgência e Emergência</h4><p>Pronto-socorro 24h em toda a rede credenciada nacional. Cobertura de emergência em qualquer localidade do Brasil.</p></div>
          <div class="coverage-item"><h4>💊 Procedimentos Ambulatoriais</h4><p>Quimioterapia, radioterapia, hemodiálise, fisioterapia e todos os procedimentos ambulatoriais previstos pela ANS.</p></div>
          <div class="coverage-item"><h4>🤱 Maternidade</h4><p>Pré-natal, parto normal e cesárea, UTI neonatal e acompanhamento do recém-nascido nos primeiros 30 dias.</p></div>
          <div class="coverage-item"><h4>🧠 Saúde Mental</h4><p>Consultas com psiquiatra e psicólogo, internações em clínicas psiquiátricas conforme regulamentação ANS.</p></div>
          <div class="coverage-item"><h4>📱 Telemedicina</h4><p>Consultas online pelo app Amil Clínica Digital, disponível 24h para clínicos gerais e especialistas selecionados.</p></div>
          <div class="coverage-item"><h4>🦷 Odontologia (opcional)</h4><p>Plano dental Amil pode ser contratado junto ao plano médico com cobertura para prevenção, restaurações e mais.</p></div>
        </div>
      </div>
    </section>

    <!-- SEÇÃO: Tabela de Preços -->
    <section class="content-section alt">
      <div class="container">
        <h2 class="cs-title">Tabela de Preços Amil 2026 por Faixa Etária</h2>
        <p class="cs-lead">Os valores dos planos de saúde Amil variam conforme a <strong>faixa etária</strong>, o <strong>tipo de acomodação</strong> (enfermaria ou apartamento), a <strong>abrangência</strong> (regional ou nacional) e a <strong>coparticipação</strong>. Abaixo, uma estimativa de preços para planos individuais:</p>
        <div style="overflow-x:auto;">
          <table class="price-table">
            <thead><tr><th>Faixa Etária</th><th>Amil Fácil (Regional)</th><th>Amil 400 (Nacional)</th><th>Amil 750 (Premium)</th></tr></thead>
            <tbody>
              <tr><td>0 a 18 anos</td><td>R$ 180 – R$ 280</td><td>R$ 280 – R$ 420</td><td>R$ 420 – R$ 680</td></tr>
              <tr><td>19 a 23 anos</td><td>R$ 190 – R$ 290</td><td>R$ 300 – R$ 450</td><td>R$ 440 – R$ 700</td></tr>
              <tr><td>24 a 28 anos</td><td>R$ 200 – R$ 320</td><td>R$ 320 – R$ 480</td><td>R$ 460 – R$ 730</td></tr>
              <tr><td>29 a 33 anos</td><td>R$ 230 – R$ 360</td><td>R$ 360 – R$ 540</td><td>R$ 510 – R$ 820</td></tr>
              <tr><td>34 a 38 anos</td><td>R$ 270 – R$ 420</td><td>R$ 420 – R$ 630</td><td>R$ 590 – R$ 950</td></tr>
              <tr><td>39 a 43 anos</td><td>R$ 320 – R$ 510</td><td>R$ 510 – R$ 760</td><td>R$ 710 – R$ 1.140</td></tr>
              <tr><td>44 a 48 anos</td><td>R$ 420 – R$ 670</td><td>R$ 670 – R$ 1.000</td><td>R$ 930 – R$ 1.490</td></tr>
              <tr><td>49 a 53 anos</td><td>R$ 580 – R$ 930</td><td>R$ 930 – R$ 1.390</td><td>R$ 1.290 – R$ 2.070</td></tr>
              <tr><td>54 a 58 anos</td><td>R$ 760 – R$ 1.220</td><td>R$ 1.220 – R$ 1.820</td><td>R$ 1.690 – R$ 2.710</td></tr>
              <tr><td>59 anos ou mais</td><td>R$ 1.080 – R$ 1.730</td><td>R$ 1.730 – R$ 2.590</td><td>R$ 2.400 – R$ 3.840</td></tr>
            </tbody>
          </table>
        </div>
        <div class="highlight-box" style="margin-top:20px;"><p>⚠️ <strong>Atenção:</strong> Os valores acima são estimativas de referência para 2026. O preço exato depende da cidade, do plano específico, da coparticipação e das condições negociadas. <strong>Solicite uma cotação gratuita</strong> com a Virtua para o valor exato para seu perfil.</p></div>
      </div>
    </section>

    <!-- SEÇÃO: Carência -->
    <section class="content-section">
      <div class="container">
        <h2 class="cs-title">Carência do Plano Amil: O Que Saber Antes de Contratar</h2>
        <p class="cs-lead">A <strong>carência</strong> é o período mínimo que o beneficiário precisa aguardar após a contratação antes de utilizar determinados serviços. A ANS estabelece prazos máximos que todas as operadoras devem respeitar.</p>
        <div style="overflow-x:auto;">
          <table class="carencia-table">
            <thead><tr><th>Tipo de Atendimento</th><th>Carência Máxima (ANS)</th><th>Amil (Média Praticada)</th></tr></thead>
            <tbody>
              <tr><td>Urgência e emergência</td><td>24 horas</td><td>24 horas</td></tr>
              <tr><td>Consultas e exames simples</td><td>30 dias</td><td>30 dias</td></tr>
              <tr><td>Internações e cirurgias</td><td>180 dias</td><td>180 dias</td></tr>
              <tr><td>Parto a termo (normal ou cesárea)</td><td>300 dias</td><td>300 dias</td></tr>
              <tr><td>Doenças e lesões preexistentes</td><td>24 meses*</td><td>24 meses*</td></tr>
              <tr><td>Tratamentos odontológicos (se incluso)</td><td>até 180 dias</td><td>até 60 dias</td></tr>
            </tbody>
          </table>
        </div>
        <p style="font-size:13px;color:#94a3b8;margin-top:10px;">*Para doenças ou lesões preexistentes declaradas, pode-se optar pela cobertura parcial temporária (CPT) ou aguardar 24 meses. A portabilidade de carências elimina esse prazo se você já tiver plano ativo.</p>
        <div class="highlight-box"><p>💡 <strong>Portabilidade de Carências:</strong> Se você já tem um plano de saúde ativo há pelo menos 2 anos, pode fazer a portabilidade para a Amil <strong>sem cumprir novas carências</strong> para os mesmos procedimentos. Consulte a Virtua para verificar sua elegibilidade.</p></div>
      </div>
    </section>

    <!-- SEÇÃO: Como Contratar -->
    <section class="content-section alt">
      <div class="container">
        <h2 class="cs-title">Como Contratar Plano de Saúde Amil em 2026</h2>
        <p class="cs-lead">Contratar um plano Amil pela Virtua Corretora é simples, rápido e 100% gratuito. Veja o passo a passo:</p>
        <ul class="steps-list">
          <li><div><h4>Solicite sua cotação gratuita</h4><p>Entre em contato pelo WhatsApp <strong>(22) 99940-4840</strong> ou preencha o formulário. Informe sua cidade, idade, número de dependentes e tipo de plano desejado.</p></div></li>
          <li><div><h4>Receba a proposta personalizada</h4><p>Nossa equipe envia uma comparação de planos Amil disponíveis para o seu perfil, com preços, coberturas e rede credenciada em até 24h.</p></div></li>
          <li><div><h4>Escolha o plano ideal</h4><p>Tiramos todas as suas dúvidas sobre cobertura, carência, coparticipação e rede. Você decide sem pressão.</p></div></li>
          <li><div><h4>Envio da documentação</h4><p>Documentos exigidos: RG, CPF, comprovante de residência e declaração de saúde (para planos individuais). Para empresas: CNPJ e lista de beneficiários.</p></div></li>
          <li><div><h4>Assinatura e ativação</h4><p>Contrato assinado digitalmente. Após confirmação do pagamento da 1ª mensalidade, a carteirinha digital fica disponível em 24–48h pelo app Amil.</p></div></li>
        </ul>
      </div>
    </section>

    <!-- SEÇÃO: Vantagens e Desvantagens -->
    <section class="content-section">
      <div class="container">
        <h2 class="cs-title">Plano de Saúde Amil Vale a Pena? Vantagens e Desvantagens</h2>
        <p class="cs-lead">Para ajudá-lo a tomar a melhor decisão, listamos os principais pontos positivos e negativos da Amil em 2026, com base na experiência dos nossos clientes e avaliações do setor.</p>
        <div class="pros-cons">
          <div class="pros"><h4>✅ Vantagens da Amil</h4><ul>
            <li>Uma das maiores redes credenciadas do Brasil</li>
            <li>Hospitais premium: Copa D'Or, Samaritano, Rede D'Or</li>
            <li>Cobertura nacional em todos os planos (exceto Amil Fácil)</li>
            <li>Amil Clínica Digital: telemedicina 24h</li>
            <li>App completo para agendamentos e exames</li>
            <li>Planos para MEI a partir de 2 vidas</li>
            <li>Cobertura internacional em planos premium</li>
            <li>Ampla rede de laboratórios (Dasa, Labs a+)</li>
          </ul></div>
          <div class="cons"><h4>⚠️ Pontos de Atenção</h4><ul>
            <li>Preço mais elevado que operadoras regionais</li>
            <li>Coparticipação em alguns modelos de plano</li>
            <li>Amil Fácil tem cobertura apenas regional</li>
            <li>Reajustes anuais conforme tabela ANS</li>
            <li>Planos individuais mais limitados que coletivos</li>
          </ul></div>
        </div>
      </div>
    </section>
"""},

# ══════════════════════════════════════════════════════════════════════════════
"plano-de-saude-bradesco": {
"anchor": "<!-- Plans -->",
"sections": """
    <section class="content-section alt">
      <div class="container">
        <h2 class="cs-title">Sobre o Bradesco Saúde: Tradição e Excelência no Brasil</h2>
        <p class="cs-lead">O <strong>Bradesco Saúde</strong> é um dos líderes do mercado de planos de saúde no Brasil, parte do <strong>Grupo Bradesco Seguros</strong>, o maior conglomerado de seguros da América Latina. Com mais de 60 anos de atuação, atende mais de 4 milhões de beneficiários e é reconhecido pela qualidade da rede credenciada e solidez financeira.</p>
        <div class="cs-body">
          <p>A grande diferença do Bradesco Saúde está no acesso a hospitais de referência nacional como <strong>Hospital Albert Einstein</strong>, <strong>Hospital Sírio-Libanês</strong>, <strong>Copa D'Or</strong> e <strong>Hospital Israelita Albert Einstein</strong> — os mais conceituados do país. Essa rede premium é exclusiva dos planos de maior cobertura.</p>
          <p>Para empresas, o Bradesco Saúde é uma das operadoras mais contratadas por grandes corporações, com condições especiais para grupos a partir de 2 vidas (MEI e PME). Oferece ainda o programa <strong>Bradesco Saúde Empresas</strong> com gestão de saúde corporativa e relatórios de sinistralidade.</p>
          <p>Os planos <strong>Bradesco Top Nacional</strong> e <strong>Bradesco Preferencial Plus</strong> são os mais completos do mercado, com reembolso diferenciado, livre escolha de médico e cobertura internacional.</p>
          <div class="highlight-box"><p>💡 <strong>Dica Virtua:</strong> O Bradesco Saúde é ideal para quem prioriza acesso aos melhores hospitais do Brasil e qualidade comprovada. A Virtua é corretora autorizada Bradesco e garante as melhores tabelas disponíveis para seu perfil.</p></div>
        </div>
      </div>
    </section>

    <section class="content-section">
      <div class="container">
        <h2 class="cs-title">Cobertura do Plano de Saúde Bradesco em 2026</h2>
        <p class="cs-lead">O Bradesco Saúde cobre todos os procedimentos do rol da ANS, com coberturas adicionais nos planos mais completos.</p>
        <div class="coverage-grid">
          <div class="coverage-item"><h4>🏥 Internação e UTI</h4><p>Internações clínicas e cirúrgicas em enfermaria ou apartamento, com acesso a UTI nas principais redes.</p></div>
          <div class="coverage-item"><h4>🔬 Exames de Alta Complexidade</h4><p>Tomografia, PET-CT, ressonância magnética, cateterismo, densitometria óssea e procedimentos de alta complexidade.</p></div>
          <div class="coverage-item"><h4>👨‍⚕️ Consultas Especializadas</h4><p>Acesso a especialistas renomados em cardiologia, oncologia, neurologia, ortopedia e mais de 50 especialidades.</p></div>
          <div class="coverage-item"><h4>🎗️ Oncologia</h4><p>Tratamento completo do câncer: quimioterapia, radioterapia, cirurgia oncológica e medicamentos oncológicos.</p></div>
          <div class="coverage-item"><h4>👶 Maternidade Completa</h4><p>Pré-natal, parto, UTI neonatal e acompanhamento do bebê nos primeiros 30 dias de vida.</p></div>
          <div class="coverage-item"><h4>🧠 Saúde Mental</h4><p>Consultas com psiquiatra e psicólogo, internações em clínicas especializadas conforme ANS.</p></div>
          <div class="coverage-item"><h4>🌎 Cobertura Internacional</h4><p>Planos top incluem cobertura de urgência e emergência no exterior, com reembolso em dólar.</p></div>
          <div class="coverage-item"><h4>💊 Medicamentos (internação)</h4><p>Medicamentos utilizados durante internações hospitalares estão cobertos pelo plano.</p></div>
          <div class="coverage-item"><h4>🦷 Bradesco Dental</h4><p>Possibilidade de incluir plano odontológico Bradesco Dental com cobertura para prevenção, restaurações e ortodontia.</p></div>
        </div>
      </div>
    </section>

    <section class="content-section alt">
      <div class="container">
        <h2 class="cs-title">Tabela de Preços Bradesco Saúde 2026</h2>
        <p class="cs-lead">Os preços do Bradesco Saúde variam por faixa etária, produto, abrangência e modalidade. Estimativas para planos individuais:</p>
        <div style="overflow-x:auto;">
          <table class="price-table">
            <thead><tr><th>Faixa Etária</th><th>Bradesco Efetivo</th><th>Bradesco Nacional Flex</th><th>Bradesco Top Nacional</th></tr></thead>
            <tbody>
              <tr><td>0 a 18 anos</td><td>R$ 160 – R$ 260</td><td>R$ 290 – R$ 440</td><td>R$ 500 – R$ 780</td></tr>
              <tr><td>19 a 23 anos</td><td>R$ 175 – R$ 275</td><td>R$ 310 – R$ 470</td><td>R$ 530 – R$ 820</td></tr>
              <tr><td>24 a 28 anos</td><td>R$ 195 – R$ 305</td><td>R$ 340 – R$ 510</td><td>R$ 580 – R$ 900</td></tr>
              <tr><td>29 a 33 anos</td><td>R$ 230 – R$ 360</td><td>R$ 390 – R$ 590</td><td>R$ 670 – R$ 1.040</td></tr>
              <tr><td>34 a 38 anos</td><td>R$ 275 – R$ 430</td><td>R$ 460 – R$ 700</td><td>R$ 790 – R$ 1.230</td></tr>
              <tr><td>39 a 43 anos</td><td>R$ 330 – R$ 520</td><td>R$ 560 – R$ 850</td><td>R$ 960 – R$ 1.490</td></tr>
              <tr><td>44 a 48 anos</td><td>R$ 435 – R$ 685</td><td>R$ 730 – R$ 1.110</td><td>R$ 1.250 – R$ 1.950</td></tr>
              <tr><td>49 a 53 anos</td><td>R$ 605 – R$ 950</td><td>R$ 1.010 – R$ 1.540</td><td>R$ 1.730 – R$ 2.700</td></tr>
              <tr><td>54 a 58 anos</td><td>R$ 790 – R$ 1.245</td><td>R$ 1.320 – R$ 2.010</td><td>R$ 2.260 – R$ 3.530</td></tr>
              <tr><td>59 anos ou mais</td><td>R$ 1.125 – R$ 1.770</td><td>R$ 1.880 – R$ 2.860</td><td>R$ 3.210 – R$ 5.020</td></tr>
            </tbody>
          </table>
        </div>
        <div class="highlight-box" style="margin-top:20px;"><p>⚠️ Valores estimados para 2026. Preço final varia conforme cidade, coparticipação e condições do plano. Solicite cotação exata com a Virtua.</p></div>
      </div>
    </section>

    <section class="content-section">
      <div class="container">
        <h2 class="cs-title">Carência do Bradesco Saúde</h2>
        <p class="cs-lead">O Bradesco Saúde segue os prazos máximos estabelecidos pela ANS. Veja os principais:</p>
        <div style="overflow-x:auto;">
          <table class="carencia-table">
            <thead><tr><th>Tipo de Atendimento</th><th>Prazo de Carência</th></tr></thead>
            <tbody>
              <tr><td>Urgência e emergência</td><td>24 horas</td></tr>
              <tr><td>Consultas médicas e exames simples</td><td>30 dias</td></tr>
              <tr><td>Internações clínicas e cirúrgicas</td><td>180 dias</td></tr>
              <tr><td>Parto (normal ou cesárea)</td><td>300 dias</td></tr>
              <tr><td>Doenças preexistentes (CPT)</td><td>24 meses ou cobertura parcial</td></tr>
            </tbody>
          </table>
        </div>
        <div class="highlight-box"><p>💡 Com a <strong>portabilidade de carências</strong>, quem já tem plano de saúde ativo pode migrar para o Bradesco sem cumprir novas carências. Consulte a Virtua para verificar sua elegibilidade.</p></div>
      </div>
    </section>

    <section class="content-section alt">
      <div class="container">
        <h2 class="cs-title">Como Contratar Plano de Saúde Bradesco</h2>
        <p class="cs-lead">Processo simples, 100% digital e sem custo pela Virtua Corretora:</p>
        <ul class="steps-list">
          <li><div><h4>Solicite cotação pelo WhatsApp</h4><p>Informe cidade, idade e perfil (individual, familiar ou empresarial) para receber as opções disponíveis.</p></div></li>
          <li><div><h4>Compare os planos disponíveis</h4><p>Apresentamos as opções do Bradesco Saúde com preços, coberturas, redes credenciadas e comparativo com outras operadoras.</p></div></li>
          <li><div><h4>Envie os documentos</h4><p>RG, CPF, comprovante de residência e declaração de saúde. Empresas: CNPJ, contrato social e relação de beneficiários.</p></div></li>
          <li><div><h4>Assinatura digital e ativação</h4><p>Proposta assinada digitalmente. Carteirinha disponível no app Bradesco Saúde após confirmação do pagamento.</p></div></li>
        </ul>
      </div>
    </section>

    <section class="content-section">
      <div class="container">
        <h2 class="cs-title">Vantagens e Desvantagens do Bradesco Saúde</h2>
        <div class="pros-cons">
          <div class="pros"><h4>✅ Vantagens</h4><ul>
            <li>Acesso ao Albert Einstein e Sírio-Libanês (planos top)</li>
            <li>Sólida reputação e tradição no mercado</li>
            <li>Ampla rede nacional em todas as capitais</li>
            <li>Planos para MEI e PME a partir de 2 vidas</li>
            <li>Cobertura internacional nos planos premium</li>
            <li>App Bradesco Saúde completo e intuitivo</li>
          </ul></div>
          <div class="cons"><h4>⚠️ Pontos de Atenção</h4><ul>
            <li>Preço elevado nos planos top</li>
            <li>Coparticipação nos planos básicos</li>
            <li>Albert Einstein apenas nos planos mais caros</li>
            <li>Reajuste anual vinculado à tabela Bradesco</li>
          </ul></div>
        </div>
      </div>
    </section>
"""},

# ══════════════════════════════════════════════════════════════════════════════
"plano-de-saude-sulamerica": {
"anchor": "<!-- Plans -->",
"sections": """
    <section class="content-section alt">
      <div class="container">
        <h2 class="cs-title">Sobre a SulAmérica Saúde: Inovação e Cobertura Nacional</h2>
        <p class="cs-lead">A <strong>SulAmérica Saúde</strong> é uma das maiores operadoras de saúde do Brasil, parte do <strong>Grupo Caixa Seguradora</strong> desde 2022. Com mais de 125 anos de história no mercado de seguros, a SulAmérica atende milhões de beneficiários com planos individuais, familiares e empresariais em todo o país.</p>
        <div class="cs-body">
          <p>Reconhecida pela <strong>inovação digital</strong>, a SulAmérica oferece o aplicativo <strong>Saúde SulAmérica</strong>, com telemedicina, agendamentos, carteirinha digital e gestão completa do plano. O programa <strong>Saúde em Dia</strong> promove prevenção e bem-estar com descontos em academias, farmácias e exames preventivos.</p>
          <p>A linha <strong>SulAmérica Saúde Direto</strong> é uma das mais procuradas por oferecer planos individuais e familiares com boa relação custo-benefício e cobertura em todo o Brasil. Já os planos <strong>SulAmérica Especial</strong> e <strong>SulAmérica Executivo</strong> oferecem coberturas premium com reembolso diferenciado e livre escolha de médico.</p>
          <p>Para empresas, a SulAmérica tem soluções para todos os portes: de MEI (a partir de 1 vida) a grandes corporações, com gestão de saúde populacional e programas de RH integrados.</p>
          <div class="highlight-box"><p>💡 <strong>Dica Virtua:</strong> A SulAmérica Saúde Direto é excelente para quem busca plano individual ou familiar com preço competitivo e cobertura nacional. Ideal para trabalhadores autônomos, MEI e profissionais liberais.</p></div>
        </div>
      </div>
    </section>

    <section class="content-section">
      <div class="container">
        <h2 class="cs-title">Cobertura do Plano SulAmérica em 2026</h2>
        <div class="coverage-grid">
          <div class="coverage-item"><h4>🏥 Internações</h4><p>Internações clínicas, cirúrgicas e em UTI, em enfermaria ou apartamento conforme o plano.</p></div>
          <div class="coverage-item"><h4>🔬 Diagnóstico por Imagem</h4><p>Tomografia, ressonância magnética, ultrassom, raio-X e medicina nuclear.</p></div>
          <div class="coverage-item"><h4>👨‍⚕️ Consultas e Especialistas</h4><p>Acesso a médicos especialistas em toda a rede credenciada nacional.</p></div>
          <div class="coverage-item"><h4>🏃 Fisioterapia</h4><p>Sessões de fisioterapia ambulatorial prescritas por médico credenciado.</p></div>
          <div class="coverage-item"><h4>🎗️ Oncologia</h4><p>Tratamento oncológico completo: quimioterapia, radioterapia e procedimentos cirúrgicos.</p></div>
          <div class="coverage-item"><h4>🧠 Saúde Mental</h4><p>Consultas psiquiátricas, psicoterapia e internações em saúde mental.</p></div>
          <div class="coverage-item"><h4>👶 Maternidade</h4><p>Pré-natal, parto e UTI neonatal, com acompanhamento do recém-nascido.</p></div>
          <div class="coverage-item"><h4>💊 Reembolso</h4><p>Planos com reembolso permitem atendimento fora da rede com ressarcimento conforme tabela.</p></div>
          <div class="coverage-item"><h4>📱 Telemedicina</h4><p>Consultas online pelo app Saúde SulAmérica disponíveis 24 horas por dia.</p></div>
        </div>
      </div>
    </section>

    <section class="content-section alt">
      <div class="container">
        <h2 class="cs-title">Tabela de Preços SulAmérica 2026</h2>
        <p class="cs-lead">Estimativas de valores para planos individuais SulAmérica por faixa etária:</p>
        <div style="overflow-x:auto;">
          <table class="price-table">
            <thead><tr><th>Faixa Etária</th><th>SulAmérica Direto</th><th>SulAmérica Especial</th><th>SulAmérica Executivo</th></tr></thead>
            <tbody>
              <tr><td>0 a 18 anos</td><td>R$ 170 – R$ 270</td><td>R$ 310 – R$ 470</td><td>R$ 490 – R$ 760</td></tr>
              <tr><td>19 a 28 anos</td><td>R$ 185 – R$ 295</td><td>R$ 330 – R$ 500</td><td>R$ 520 – R$ 810</td></tr>
              <tr><td>29 a 38 anos</td><td>R$ 250 – R$ 400</td><td>R$ 450 – R$ 680</td><td>R$ 700 – R$ 1.090</td></tr>
              <tr><td>39 a 48 anos</td><td>R$ 380 – R$ 600</td><td>R$ 670 – R$ 1.020</td><td>R$ 1.050 – R$ 1.640</td></tr>
              <tr><td>49 a 58 anos</td><td>R$ 680 – R$ 1.080</td><td>R$ 1.200 – R$ 1.820</td><td>R$ 1.880 – R$ 2.940</td></tr>
              <tr><td>59 anos ou mais</td><td>R$ 1.100 – R$ 1.750</td><td>R$ 1.940 – R$ 2.950</td><td>R$ 3.040 – R$ 4.750</td></tr>
            </tbody>
          </table>
        </div>
        <div class="highlight-box" style="margin-top:20px;"><p>⚠️ Valores estimados para 2026. Solicite cotação personalizada com a Virtua.</p></div>
      </div>
    </section>

    <section class="content-section">
      <div class="container">
        <h2 class="cs-title">Vantagens e Desvantagens da SulAmérica</h2>
        <div class="pros-cons">
          <div class="pros"><h4>✅ Vantagens</h4><ul>
            <li>SulAmérica Direto: plano individual com bom custo-benefício</li>
            <li>App Saúde SulAmérica completo e moderno</li>
            <li>Reembolso em planos premium com livre escolha</li>
            <li>Programa Saúde em Dia (prevenção e bem-estar)</li>
            <li>Cobertura nacional abrangente</li>
            <li>Telemedicina 24h disponível</li>
          </ul></div>
          <div class="cons"><h4>⚠️ Pontos de Atenção</h4><ul>
            <li>Planos individuais com custo elevado para 50+ anos</li>
            <li>Rede credenciada menor em cidades do interior</li>
            <li>Coparticipação nos planos básicos</li>
          </ul></div>
        </div>
      </div>
    </section>
"""},

# ══════════════════════════════════════════════════════════════════════════════
"plano-de-saude-unimed": {
"anchor": "<!-- Plans -->",
"sections": """
    <section class="content-section alt">
      <div class="container">
        <h2 class="cs-title">Sobre a Unimed: A Maior Cooperativa Médica do Mundo</h2>
        <p class="cs-lead">A <strong>Unimed</strong> é o maior sistema cooperativista de saúde do mundo, presente em mais de <strong>83% dos municípios brasileiros</strong> com 360+ cooperativas independentes. Fundada em 1967 em Santos (SP), hoje atende mais de 18 milhões de beneficiários em todo o Brasil.</p>
        <div class="cs-body">
          <p>O diferencial da Unimed está nos <strong>médicos cooperados</strong>: são os próprios médicos que gerem a cooperativa, garantindo alinhamento entre qualidade assistencial e sustentabilidade financeira. Isso se traduz em atendimento humanizado e vínculos de longo prazo com os beneficiários.</p>
          <p>O sistema de <strong>intercâmbio Unimed</strong> permite que beneficiários de uma cooperativa utilizem a rede de qualquer outra cooperativa Unimed no Brasil, ideal para quem viaja ou estuda em outra cidade. Em emergências, o atendimento é garantido em qualquer unidade Unimed do país.</p>
          <p>Para empresas, a Unimed oferece planos coletivos empresariais com gestão de saúde populacional, programas de prevenção e excelente custo-benefício. A Unimed é a operadora mais contratada por pequenas e médias empresas em muitas regiões do Brasil.</p>
          <div class="highlight-box"><p>💡 <strong>Dica Virtua:</strong> A Unimed é ideal para quem valoriza relacionamento com o médico de confiança e atendimento humanizado. Se há uma cooperativa Unimed na sua cidade, é sempre uma das melhores opções a considerar.</p></div>
        </div>
      </div>
    </section>

    <section class="content-section">
      <div class="container">
        <h2 class="cs-title">Cobertura do Plano Unimed em 2026</h2>
        <div class="coverage-grid">
          <div class="coverage-item"><h4>👨‍⚕️ Médicos Cooperados</h4><p>Acesso à rede de médicos cooperados com atendimento personalizado e continuidade de cuidado.</p></div>
          <div class="coverage-item"><h4>🏥 Hospitais e Clínicas</h4><p>Rede hospitalar própria e credenciada com unidades em todo o Brasil.</p></div>
          <div class="coverage-item"><h4>🔄 Intercâmbio Nacional</h4><p>Utilize a rede de qualquer cooperativa Unimed no Brasil quando estiver viajando.</p></div>
          <div class="coverage-item"><h4>🔬 Exames Diagnósticos</h4><p>Tomografia, ressonância, raio-X, ultrassom, endoscopia e mais de 3.000 procedimentos.</p></div>
          <div class="coverage-item"><h4>🎗️ Oncologia</h4><p>Tratamento completo de câncer conforme rol ANS: quimio, radio, cirurgia e medicamentos.</p></div>
          <div class="coverage-item"><h4>👶 Maternidade</h4><p>Pré-natal, parto e acompanhamento neonatal completo.</p></div>
          <div class="coverage-item"><h4>🧠 Saúde Mental</h4><p>Psiquiatria, psicologia e internações em saúde mental.</p></div>
          <div class="coverage-item"><h4>📱 Unimed Digital</h4><p>App Unimed com carteirinha digital, agendamentos e telemedicina.</p></div>
          <div class="coverage-item"><h4>🏃 Programas de Prevenção</h4><p>Programas de saúde preventiva, check-up e acompanhamento de doenças crônicas.</p></div>
        </div>
      </div>
    </section>

    <section class="content-section alt">
      <div class="container">
        <h2 class="cs-title">Tabela de Preços Unimed 2026</h2>
        <p class="cs-lead">Os preços da Unimed variam por cooperativa regional. Estimativas médias para planos individuais:</p>
        <div style="overflow-x:auto;">
          <table class="price-table">
            <thead><tr><th>Faixa Etária</th><th>Unimed Enfermaria</th><th>Unimed Apartamento</th><th>Unimed Nacional</th></tr></thead>
            <tbody>
              <tr><td>0 a 18 anos</td><td>R$ 160 – R$ 280</td><td>R$ 220 – R$ 380</td><td>R$ 300 – R$ 480</td></tr>
              <tr><td>19 a 28 anos</td><td>R$ 180 – R$ 300</td><td>R$ 240 – R$ 410</td><td>R$ 320 – R$ 510</td></tr>
              <tr><td>29 a 38 anos</td><td>R$ 250 – R$ 420</td><td>R$ 330 – R$ 560</td><td>R$ 440 – R$ 700</td></tr>
              <tr><td>39 a 48 anos</td><td>R$ 380 – R$ 640</td><td>R$ 500 – R$ 840</td><td>R$ 660 – R$ 1.060</td></tr>
              <tr><td>49 a 58 anos</td><td>R$ 680 – R$ 1.140</td><td>R$ 900 – R$ 1.510</td><td>R$ 1.190 – R$ 1.900</td></tr>
              <tr><td>59 anos ou mais</td><td>R$ 1.100 – R$ 1.840</td><td>R$ 1.450 – R$ 2.430</td><td>R$ 1.920 – R$ 3.070</td></tr>
            </tbody>
          </table>
        </div>
        <div class="highlight-box" style="margin-top:20px;"><p>⚠️ Preços variam significativamente entre cooperativas regionais. Solicite cotação para sua cidade com a Virtua.</p></div>
      </div>
    </section>

    <section class="content-section">
      <div class="container">
        <h2 class="cs-title">Vantagens e Desvantagens da Unimed</h2>
        <div class="pros-cons">
          <div class="pros"><h4>✅ Vantagens</h4><ul>
            <li>Maior sistema cooperativista de saúde do mundo</li>
            <li>Médicos cooperados: atendimento humanizado</li>
            <li>Intercâmbio em todo o Brasil (360+ cooperativas)</li>
            <li>Presente em 83% dos municípios brasileiros</li>
            <li>Forte presença no interior do país</li>
            <li>Programas robustos de prevenção</li>
          </ul></div>
          <div class="cons"><h4>⚠️ Pontos de Atenção</h4><ul>
            <li>Cada cooperativa tem autonomia: qualidade varia por região</li>
            <li>Rede menor em algumas capitais vs. Amil ou Bradesco</li>
            <li>Processo de autorização pode ser mais lento em algumas cooperativas</li>
          </ul></div>
        </div>
      </div>
    </section>
"""},

# ══════════════════════════════════════════════════════════════════════════════
"plano-de-saude-hapvida": {
"anchor": "<!-- Plans -->",
"sections": """
    <section class="content-section alt">
      <div class="container">
        <h2 class="cs-title">Sobre a Hapvida: Maior Operadora de Rede Própria do Brasil</h2>
        <p class="cs-lead">A <strong>Hapvida NotreDame Intermédica (GNDI)</strong> é hoje a maior operadora de saúde do Brasil em número de beneficiários, resultado da fusão entre Hapvida e NotreDame Intermédica em 2022. Com mais de 15 milhões de beneficiários e uma vasta rede própria, a Hapvida se destaca pelo modelo verticalizado de saúde.</p>
        <div class="cs-body">
          <p>O grande diferencial da Hapvida é a <strong>rede própria de hospitais, clínicas, laboratórios e centros diagnósticos</strong>. Com mais de 80 hospitais próprios, 300+ clínicas e 100+ centros de diagnóstico, a operadora controla toda a cadeia de atendimento, o que resulta em <strong>preços mais acessíveis</strong> e agilidade na autorização de procedimentos.</p>
          <p>Forte especialmente no <strong>Norte e Nordeste do Brasil</strong>, a Hapvida tem presença consolidada em estados como Ceará, Pernambuco, Bahia, Amazonas, Pará e Goiás. Nos últimos anos, expandiu significativamente para o Sudeste com a incorporação da NotreDame Intermédica.</p>
          <p>Para empresas, o modelo Hapvida oferece planos com <strong>excelente custo-benefício</strong>, especialmente para grupos com base no Norte e Nordeste. Os planos Hapvida Mix combinam rede própria com rede credenciada para maior flexibilidade.</p>
          <div class="highlight-box"><p>💡 <strong>Dica Virtua:</strong> A Hapvida é a melhor opção de custo-benefício para quem mora no Norte e Nordeste do Brasil. No Sudeste, os planos Hapvida GNDI oferecem boa cobertura com preços competitivos.</p></div>
        </div>
      </div>
    </section>

    <section class="content-section">
      <div class="container">
        <h2 class="cs-title">Cobertura do Plano Hapvida em 2026</h2>
        <div class="coverage-grid">
          <div class="coverage-item"><h4>🏥 Hospitais Próprios</h4><p>Mais de 80 hospitais próprios em todo o Brasil, com foco no Norte e Nordeste.</p></div>
          <div class="coverage-item"><h4>🔬 Centros Diagnósticos</h4><p>Mais de 100 centros diagnósticos próprios com exames de imagem e laboratório.</p></div>
          <div class="coverage-item"><h4>👨‍⚕️ Clínicas Próprias</h4><p>Mais de 300 clínicas próprias com consultas em diversas especialidades médicas.</p></div>
          <div class="coverage-item"><h4>🚑 Pronto-Socorro 24h</h4><p>Atendimento de urgência e emergência nas unidades próprias Hapvida 24 horas.</p></div>
          <div class="coverage-item"><h4>🎗️ Oncologia</h4><p>Tratamento oncológico completo na rede própria Hapvida com quimioterapia e radioterapia.</p></div>
          <div class="coverage-item"><h4>👶 Maternidade</h4><p>Pré-natal, parto e UTI neonatal nos hospitais maternidade Hapvida.</p></div>
          <div class="coverage-item"><h4>📱 Telemedicina</h4><p>Consultas online pelo app Hapvida com médicos disponíveis 24h por dia.</p></div>
          <div class="coverage-item"><h4>🧠 Saúde Mental</h4><p>Psiquiatria e psicologia na rede própria com agendamento pelo app.</p></div>
          <div class="coverage-item"><h4>💊 Farmácias Parceiras</h4><p>Descontos em medicamentos em farmácias parceiras da rede Hapvida.</p></div>
        </div>
      </div>
    </section>

    <section class="content-section alt">
      <div class="container">
        <h2 class="cs-title">Tabela de Preços Hapvida 2026</h2>
        <p class="cs-lead">A Hapvida oferece alguns dos preços mais competitivos do mercado, especialmente no Norte e Nordeste:</p>
        <div style="overflow-x:auto;">
          <table class="price-table">
            <thead><tr><th>Faixa Etária</th><th>Hapvida Essencial</th><th>Hapvida Mix</th><th>Hapvida Nacional</th></tr></thead>
            <tbody>
              <tr><td>0 a 18 anos</td><td>R$ 80 – R$ 160</td><td>R$ 140 – R$ 240</td><td>R$ 200 – R$ 320</td></tr>
              <tr><td>19 a 28 anos</td><td>R$ 90 – R$ 175</td><td>R$ 155 – R$ 260</td><td>R$ 215 – R$ 345</td></tr>
              <tr><td>29 a 38 anos</td><td>R$ 130 – R$ 250</td><td>R$ 220 – R$ 370</td><td>R$ 305 – R$ 490</td></tr>
              <tr><td>39 a 48 anos</td><td>R$ 195 – R$ 380</td><td>R$ 335 – R$ 560</td><td>R$ 460 – R$ 740</td></tr>
              <tr><td>49 a 58 anos</td><td>R$ 345 – R$ 680</td><td>R$ 595 – R$ 1.000</td><td>R$ 820 – R$ 1.320</td></tr>
              <tr><td>59 anos ou mais</td><td>R$ 560 – R$ 1.100</td><td>R$ 960 – R$ 1.610</td><td>R$ 1.320 – R$ 2.130</td></tr>
            </tbody>
          </table>
        </div>
        <div class="highlight-box" style="margin-top:20px;"><p>⚠️ Valores variam por cidade e estado. A Hapvida tem preços mais baixos no Norte/Nordeste e mais elevados no Sudeste. Consulte a Virtua para cotação exata.</p></div>
      </div>
    </section>

    <section class="content-section">
      <div class="container">
        <h2 class="cs-title">Vantagens e Desvantagens da Hapvida</h2>
        <div class="pros-cons">
          <div class="pros"><h4>✅ Vantagens</h4><ul>
            <li>Preços mais competitivos do mercado</li>
            <li>Rede própria: sem necessidade de autorização prévia</li>
            <li>Mais de 80 hospitais próprios no Brasil</li>
            <li>Agilidade na autorização de procedimentos</li>
            <li>Líder em beneficiários no Brasil</li>
            <li>Forte no Norte e Nordeste</li>
          </ul></div>
          <div class="cons"><h4>⚠️ Pontos de Atenção</h4><ul>
            <li>Rede credenciada menor que Amil ou Bradesco</li>
            <li>Rede mais limitada no Sudeste e Sul</li>
            <li>Cobertura restrita à rede própria nos planos básicos</li>
            <li>Menor acesso a hospitais privados de alto padrão</li>
          </ul></div>
        </div>
      </div>
    </section>
"""},

# ══════════════════════════════════════════════════════════════════════════════
"plano-de-saude-intermedica": {
"anchor": "<!-- Plans -->",
"sections": """
    <section class="content-section alt">
      <div class="container">
        <h2 class="cs-title">Sobre a NotreDame Intermédica: Referência em Saúde no Sudeste</h2>
        <p class="cs-lead">A <strong>NotreDame Intermédica (GNDI)</strong>, hoje parte do grupo <strong>Hapvida NotreDame Intermédica</strong>, é uma das maiores operadoras de saúde do Brasil, com forte presença no <strong>Sudeste do país</strong>. Com décadas de história e mais de 5 milhões de beneficiários, é conhecida pela qualidade da rede e pelo modelo verticalizado de saúde.</p>
        <div class="cs-body">
          <p>A Intermédica opera um modelo <strong>verticalmente integrado</strong>, com hospitais próprios, clínicas, centros diagnósticos e farmácias. Seus hospitais em São Paulo — como o <strong>Hospital Maternidade São Luiz</strong> e unidades da rede GNDI — são referências em qualidade assistencial.</p>
          <p>A linha de produtos oferece desde planos econômicos (<strong>Smart</strong>) com rede própria até planos completos com rede credenciada ampla. O app <strong>GNDI</strong> permite agendamento de consultas, solicitação de reembolso, telemedicina e acesso a resultados de exames.</p>
          <div class="highlight-box"><p>💡 <strong>Dica Virtua:</strong> A Intermédica GNDI é excelente para quem mora em São Paulo, Rio de Janeiro e Minas Gerais, onde a rede própria é mais densa. Para planos econômicos no Sudeste, é uma das melhores relações custo-benefício.</p></div>
        </div>
      </div>
    </section>

    <section class="content-section">
      <div class="container">
        <h2 class="cs-title">Cobertura do Plano Intermédica em 2026</h2>
        <div class="coverage-grid">
          <div class="coverage-item"><h4>🏥 Hospitais Próprios GNDI</h4><p>Rede hospitalar própria em São Paulo, Rio de Janeiro e principais cidades do Sudeste.</p></div>
          <div class="coverage-item"><h4>🔬 Diagnóstico por Imagem</h4><p>Tomografia, ressonância, PET-CT, ultrassom e laboratório próprio.</p></div>
          <div class="coverage-item"><h4>👨‍⚕️ Clínicas Especializadas</h4><p>Clínicas próprias com especialidades médicas em diversas cidades do Sudeste.</p></div>
          <div class="coverage-item"><h4>🚑 Urgência 24h</h4><p>Pronto-socorro 24 horas nas unidades próprias GNDI.</p></div>
          <div class="coverage-item"><h4>🎗️ Oncologia</h4><p>Centros oncológicos próprios com tratamento completo de câncer.</p></div>
          <div class="coverage-item"><h4>👶 Maternidade</h4><p>Maternidades próprias com estrutura completa para pré-natal e parto.</p></div>
          <div class="coverage-item"><h4>📱 Telemedicina GNDI</h4><p>Consultas online disponíveis pelo app GNDI com especialistas.</p></div>
          <div class="coverage-item"><h4>💊 Farmácias Parceiras</h4><p>Descontos em medicamentos em farmácias parceiras da rede GNDI.</p></div>
          <div class="coverage-item"><h4>🧠 Saúde Mental</h4><p>Consultas com psiquiatra e psicólogo, internações em clínicas especializadas.</p></div>
        </div>
      </div>
    </section>

    <section class="content-section alt">
      <div class="container">
        <h2 class="cs-title">Tabela de Preços Intermédica 2026</h2>
        <div style="overflow-x:auto;">
          <table class="price-table">
            <thead><tr><th>Faixa Etária</th><th>Smart (Rede Própria)</th><th>Smart Plus</th><th>Nacional</th></tr></thead>
            <tbody>
              <tr><td>0 a 18 anos</td><td>R$ 100 – R$ 190</td><td>R$ 180 – R$ 300</td><td>R$ 260 – R$ 400</td></tr>
              <tr><td>19 a 28 anos</td><td>R$ 110 – R$ 205</td><td>R$ 195 – R$ 320</td><td>R$ 275 – R$ 430</td></tr>
              <tr><td>29 a 38 anos</td><td>R$ 160 – R$ 295</td><td>R$ 275 – R$ 455</td><td>R$ 390 – R$ 615</td></tr>
              <tr><td>39 a 48 anos</td><td>R$ 240 – R$ 445</td><td>R$ 415 – R$ 690</td><td>R$ 590 – R$ 930</td></tr>
              <tr><td>49 a 58 anos</td><td>R$ 425 – R$ 795</td><td>R$ 740 – R$ 1.235</td><td>R$ 1.050 – R$ 1.655</td></tr>
              <tr><td>59 anos ou mais</td><td>R$ 690 – R$ 1.290</td><td>R$ 1.195 – R$ 1.995</td><td>R$ 1.695 – R$ 2.670</td></tr>
            </tbody>
          </table>
        </div>
        <div class="highlight-box" style="margin-top:20px;"><p>⚠️ Valores estimados para 2026. Consulte a Virtua para cotação exata no seu CEP.</p></div>
      </div>
    </section>

    <section class="content-section">
      <div class="container">
        <h2 class="cs-title">Vantagens e Desvantagens da Intermédica</h2>
        <div class="pros-cons">
          <div class="pros"><h4>✅ Vantagens</h4><ul>
            <li>Forte rede própria no Sudeste</li>
            <li>Preços competitivos nos planos Smart</li>
            <li>Hospitais maternidade próprios de qualidade</li>
            <li>App GNDI completo com telemedicina</li>
            <li>Ágil na autorização de procedimentos</li>
          </ul></div>
          <div class="cons"><h4>⚠️ Pontos de Atenção</h4><ul>
            <li>Rede mais limitada fora do Sudeste</li>
            <li>Planos básicos com rede própria restrita</li>
            <li>Menor cobertura nacional que Amil ou Bradesco</li>
          </ul></div>
        </div>
      </div>
    </section>
"""},

# ══════════════════════════════════════════════════════════════════════════════
"plano-de-saude-para-idosos": {
"anchor": "<!-- Plans -->",
"sections": """
    <section class="content-section alt">
      <div class="container">
        <h2 class="cs-title">Como Escolher o Melhor Plano de Saúde para Idosos em 2026</h2>
        <p class="cs-lead">Escolher um plano de saúde para quem tem <strong>60 anos ou mais</strong> exige atenção especial. Os critérios mais importantes são: cobertura de especialidades geriátricas, preço por faixa etária, rede de hospitais próximos à residência e facilidade de acesso ao atendimento.</p>
        <div class="cs-body">
          <p>Pela regulamentação da ANS, os planos de saúde seguem a <strong>tabela de faixas etárias</strong> com reajuste máximo de 6 vezes do valor inicial entre a 1ª e a última faixa. Isso significa que um plano que custa R$ 300 na primeira faixa pode custar até R$ 1.800 para um beneficiário acima de 59 anos — por isso é fundamental comparar os valores de saída antes de contratar.</p>
          <p>As operadoras mais indicadas para idosos no Brasil são: <strong>MedSênior</strong> (especializada em 3ª idade), <strong>Prevent Senior</strong> (focada em idosos acima de 60), <strong>Bradesco Saúde</strong>, <strong>SulAmérica</strong> e <strong>Amil</strong> (com planos premium).</p>
          <p>Pontos essenciais para avaliar: <strong>cobertura oncológica</strong>, <strong>cardiologia</strong>, <strong>ortopedia</strong>, <strong>neurologia</strong>, <strong>home care</strong> e <strong>programas de prevenção para doenças crônicas</strong>.</p>
          <div class="highlight-box"><p>💡 <strong>Dica Virtua:</strong> Para idosos a partir de 60 anos, recomendamos sempre comparar pelo menos 3 operadoras antes de decidir. A Virtua faz essa comparação gratuitamente e sem compromisso.</p></div>
        </div>
      </div>
    </section>

    <section class="content-section">
      <div class="container">
        <h2 class="cs-title">Tabela de Preços para Idosos por Operadora (2026)</h2>
        <p class="cs-lead">Estimativas de mensalidade para beneficiários a partir de 59 anos em planos individuais:</p>
        <div style="overflow-x:auto;">
          <table class="price-table">
            <thead><tr><th>Operadora</th><th>59 a 63 anos</th><th>64 a 68 anos</th><th>69 anos ou mais</th></tr></thead>
            <tbody>
              <tr><td>MedSênior (Básico)</td><td>R$ 850 – R$ 1.100</td><td>R$ 980 – R$ 1.280</td><td>R$ 1.100 – R$ 1.450</td></tr>
              <tr><td>Prevent Senior</td><td>R$ 900 – R$ 1.200</td><td>R$ 1.040 – R$ 1.380</td><td>R$ 1.170 – R$ 1.550</td></tr>
              <tr><td>Hapvida/GNDI</td><td>R$ 700 – R$ 1.000</td><td>R$ 810 – R$ 1.160</td><td>R$ 910 – R$ 1.310</td></tr>
              <tr><td>SulAmérica Direto</td><td>R$ 1.100 – R$ 1.500</td><td>R$ 1.270 – R$ 1.730</td><td>R$ 1.430 – R$ 1.950</td></tr>
              <tr><td>Amil 400</td><td>R$ 1.300 – R$ 1.800</td><td>R$ 1.500 – R$ 2.080</td><td>R$ 1.690 – R$ 2.340</td></tr>
              <tr><td>Bradesco Top Nacional</td><td>R$ 1.900 – R$ 2.700</td><td>R$ 2.190 – R$ 3.120</td><td>R$ 2.460 – R$ 3.500</td></tr>
            </tbody>
          </table>
        </div>
        <div class="highlight-box" style="margin-top:20px;"><p>⚠️ Valores são estimativas de referência. O preço exato depende da cidade, do plano e das condições da operadora. Solicite cotação gratuita.</p></div>
      </div>
    </section>

    <section class="content-section alt">
      <div class="container">
        <h2 class="cs-title">O Que Avaliar ao Contratar Plano para Idosos</h2>
        <div class="coverage-grid">
          <div class="coverage-item"><h4>❤️ Cardiologia</h4><p>Doenças cardiovasculares são a principal causa de internação em idosos. Verifique os hospitais cardiológicos da rede.</p></div>
          <div class="coverage-item"><h4>🦴 Ortopedia</h4><p>Fraturas, artroplastia de quadril e joelho são procedimentos frequentes. A rede ortopédica deve ser avaliada.</p></div>
          <div class="coverage-item"><h4>🧠 Neurologia</h4><p>AVC, Parkinson e Alzheimer requerem acompanhamento especializado. Verifique a cobertura neurológica.</p></div>
          <div class="coverage-item"><h4>🎗️ Oncologia</h4><p>Cobertura oncológica completa é fundamental: quimio, radio, imunoterapia e cirurgia oncológica.</p></div>
          <div class="coverage-item"><h4>🏠 Home Care</h4><p>Alguns planos cobrem cuidados domiciliares (home care) para pacientes com dificuldade de locomoção.</p></div>
          <div class="coverage-item"><h4>🔬 Check-up Anual</h4><p>Programas de prevenção com check-up anual reduzem custos e detectam doenças cedo.</p></div>
        </div>
      </div>
    </section>

    <section class="content-section">
      <div class="container">
        <h2 class="cs-title">Plano de Saúde para Idosos: Perguntas Frequentes</h2>
        <div class="cs-body">
          <p><strong>Pode haver recusa de contratação por idade?</strong> Não. Pela regulamentação da ANS, nenhuma operadora pode recusar a contratação de um plano por conta da idade do beneficiário. O que muda é apenas o valor da mensalidade, que segue a tabela de faixas etárias.</p>
          <p><strong>É possível contratar plano para idoso com doença preexistente?</strong> Sim. O beneficiário pode declarar a doença preexistente (DPS) e optar pela cobertura parcial temporária (CPT) por até 24 meses, ou aguardar o cumprimento do período. Outra opção é a portabilidade se já tiver plano ativo.</p>
          <p><strong>Qual o melhor plano para idosos no Rio de Janeiro?</strong> No RJ, as melhores opções são MedSênior RJ, Prevent Senior, Amil e SulAmérica. A Virtua compara todas as opções disponíveis no seu bairro gratuitamente.</p>
        </div>
      </div>
    </section>
"""},

# ══════════════════════════════════════════════════════════════════════════════
"bradesco-dental": {
"anchor": "<!-- Plans -->",
"sections": """
    <section class="content-section alt">
      <div class="container">
        <h2 class="cs-title">Sobre o Bradesco Dental: Líder em Planos Odontológicos no Brasil</h2>
        <p class="cs-lead">O <strong>Bradesco Dental</strong> é um dos maiores e mais respeitados planos odontológicos do Brasil, parte do <strong>Grupo Bradesco Seguros</strong>. Com uma das maiores redes de dentistas credenciados do país — mais de 30.000 dentistas e 10.000 clínicas —, o Bradesco Dental oferece planos para pessoas físicas, famílias e empresas de todos os portes.</p>
        <div class="cs-body">
          <p>A grande vantagem do Bradesco Dental está na <strong>amplitude da rede credenciada</strong>: clínicas odontológicas de qualidade em capitais, interior e regiões de difícil acesso, garantindo que o beneficiário sempre tenha um dentista próximo à sua residência ou trabalho.</p>
          <p>Os planos vão do básico — com consultas de rotina, profilaxia e restaurações — até o completo, com <strong>ortodontia</strong> (aparelho), <strong>implantes</strong>, <strong>próteses</strong> e <strong>endodontia</strong> (tratamento de canal). O plano <strong>Dental Premium</strong> inclui tratamentos estéticos como clareamento dental.</p>
          <p>Para empresas, o Bradesco Dental Empresarial é uma das melhores escolhas do mercado, com preços escalonados por número de vidas e programas de saúde bucal corporativa.</p>
          <div class="highlight-box"><p>💡 <strong>Dica Virtua:</strong> O Bradesco Dental pode ser contratado isoladamente (apenas odonto) ou junto com o plano de saúde Bradesco. A contratação combinada geralmente oferece desconto especial.</p></div>
        </div>
      </div>
    </section>

    <section class="content-section">
      <div class="container">
        <h2 class="cs-title">O Que o Plano Odontológico Bradesco Cobre?</h2>
        <div class="coverage-grid">
          <div class="coverage-item"><h4>🦷 Consultas e Avaliação</h4><p>Consultas de avaliação, triagem e diagnóstico odontológico.</p></div>
          <div class="coverage-item"><h4>🧹 Prevenção e Profilaxia</h4><p>Limpeza dental (profilaxia), aplicação de flúor, selantes e orientação de higiene bucal.</p></div>
          <div class="coverage-item"><h4>🔧 Restaurações</h4><p>Restaurações com amálgama e resina composta em todos os dentes.</p></div>
          <div class="coverage-item"><h4>🦠 Endodontia</h4><p>Tratamento de canal (endodontia) em dentes anteriores, pré-molares e molares.</p></div>
          <div class="coverage-item"><h4>✂️ Extrações</h4><p>Extrações simples e cirúrgicas, incluindo dentes do siso (sisos).</p></div>
          <div class="coverage-item"><h4>🦴 Periodontia</h4><p>Tratamento de gengiva, raspagem e alisamento radicular para doença periodontal.</p></div>
          <div class="coverage-item"><h4>🔩 Implantes (Planos Plus)</h4><p>Implantes dentários cobertos nos planos de maior abrangência do Bradesco Dental.</p></div>
          <div class="coverage-item"><h4>😁 Ortodontia</h4><p>Aparelho ortodôntico (fixo e removível) coberto nos planos Completo e Premium.</p></div>
          <div class="coverage-item"><h4>🌟 Próteses</h4><p>Próteses unitárias, parciais e totais conforme o plano contratado.</p></div>
        </div>
      </div>
    </section>

    <section class="content-section alt">
      <div class="container">
        <h2 class="cs-title">Tabela de Preços Bradesco Dental 2026</h2>
        <p class="cs-lead">Os planos Bradesco Dental têm preços acessíveis, especialmente para empresas:</p>
        <div style="overflow-x:auto;">
          <table class="price-table">
            <thead><tr><th>Plano</th><th>Individual</th><th>Empresarial (por vida)</th><th>Cobertura</th></tr></thead>
            <tbody>
              <tr><td>Bradesco Dental Essencial</td><td>R$ 35 – R$ 55</td><td>R$ 25 – R$ 40</td><td>Prevenção + restaurações</td></tr>
              <tr><td>Bradesco Dental Completo</td><td>R$ 60 – R$ 95</td><td>R$ 45 – R$ 70</td><td>+ Endodontia + periodontia</td></tr>
              <tr><td>Bradesco Dental Premium</td><td>R$ 110 – R$ 170</td><td>R$ 80 – R$ 130</td><td>+ Ortodontia + implantes</td></tr>
              <tr><td>Bradesco Dental Família</td><td>R$ 120 – R$ 190</td><td>—</td><td>Até 4 dependentes inclusos</td></tr>
            </tbody>
          </table>
        </div>
        <div class="highlight-box" style="margin-top:20px;"><p>💡 Planos odontológicos têm carência de até <strong>60 dias</strong> para tratamentos básicos e até <strong>180 dias</strong> para ortodontia e implantes. Procedimentos de urgência têm cobertura imediata.</p></div>
      </div>
    </section>

    <section class="content-section">
      <div class="container">
        <h2 class="cs-title">Vantagens e Desvantagens do Bradesco Dental</h2>
        <div class="pros-cons">
          <div class="pros"><h4>✅ Vantagens</h4><ul>
            <li>Maior rede odontológica do Brasil: 30.000+ dentistas</li>
            <li>Preços acessíveis, especialmente no plano empresarial</li>
            <li>Cobertura em todo o território nacional</li>
            <li>App com localização de dentistas próximos</li>
            <li>Planos com ortodontia e implantes disponíveis</li>
            <li>Marca consolidada e de confiança</li>
          </ul></div>
          <div class="cons"><h4>⚠️ Pontos de Atenção</h4><ul>
            <li>Implantes apenas nos planos mais caros</li>
            <li>Carência de até 180 dias para ortodontia</li>
            <li>Qualidade varia por dentista credenciado</li>
          </ul></div>
        </div>
      </div>
    </section>
"""},

# ══════════════════════════════════════════════════════════════════════════════
"plano-odonto-empresarial": {
"anchor": "<!-- Plans -->",
"sections": """
    <section class="content-section alt">
      <div class="container">
        <h2 class="cs-title">Por Que Ter Plano Odontológico na Sua Empresa?</h2>
        <p class="cs-lead">O plano odontológico empresarial é um dos <strong>benefícios mais valorizados pelos funcionários</strong> — e um dos mais baratos para o empregador. Por apenas R$ 25 a R$ 60 por vida, sua empresa oferece um benefício que impacta diretamente a qualidade de vida e a produtividade da equipe.</p>
        <div class="cs-body">
          <p>Segundo pesquisas do setor, <strong>72% dos trabalhadores</strong> listam o plano odontológico como um dos três benefícios mais importantes. Empresas que oferecem esse benefício têm menor rotatividade e maior engajamento dos colaboradores.</p>
          <p>Além disso, a <strong>saúde bucal impacta diretamente a saúde geral</strong>: doenças periodontais estão associadas a diabetes, doenças cardiovasculares e complicações na gravidez. Funcionários com bom acesso ao dentista faltam menos ao trabalho e têm menor incidência de doenças sistêmicas.</p>
          <p>As principais operadoras de plano odonto empresarial no Brasil são: <strong>OdontoPrev</strong> (maior), <strong>Bradesco Dental</strong>, <strong>Amil Dental</strong>, <strong>SulAmérica Odonto</strong>, <strong>Porto Seguro Odonto</strong> e <strong>MetLife Dental</strong>.</p>
          <div class="highlight-box"><p>💡 <strong>Dica Virtua:</strong> Para MEI e empresas com até 30 funcionários, os planos Bradesco Dental e OdontoPrev oferecem as melhores condições de custo-benefício. A Virtua negocia diretamente com as operadoras para garantir o melhor preço.</p></div>
        </div>
      </div>
    </section>

    <section class="content-section">
      <div class="container">
        <h2 class="cs-title">Comparativo de Planos Odontológicos Empresariais 2026</h2>
        <div style="overflow-x:auto;">
          <table class="price-table">
            <thead><tr><th>Operadora</th><th>Preço/vida (mínimo)</th><th>Rede (aprox.)</th><th>Ortodontia</th><th>Implante</th></tr></thead>
            <tbody>
              <tr><td>OdontoPrev Essencial</td><td>R$ 20 – R$ 35</td><td>28.000+ dentistas</td><td>Não</td><td>Não</td></tr>
              <tr><td>OdontoPrev Plus</td><td>R$ 45 – R$ 70</td><td>28.000+ dentistas</td><td>Sim</td><td>Parcial</td></tr>
              <tr><td>Bradesco Dental Emp.</td><td>R$ 25 – R$ 45</td><td>30.000+ dentistas</td><td>Planos premium</td><td>Planos premium</td></tr>
              <tr><td>Amil Dental Emp.</td><td>R$ 30 – R$ 50</td><td>20.000+ dentistas</td><td>Planos premium</td><td>Não</td></tr>
              <tr><td>SulAmérica Odonto</td><td>R$ 28 – R$ 48</td><td>22.000+ dentistas</td><td>Planos premium</td><td>Não</td></tr>
              <tr><td>Porto Seguro Odonto</td><td>R$ 32 – R$ 55</td><td>18.000+ dentistas</td><td>Planos premium</td><td>Parcial</td></tr>
            </tbody>
          </table>
        </div>
        <div class="highlight-box" style="margin-top:20px;"><p>⚠️ Valores mínimos para grupos a partir de 2 vidas (MEI). Empresas com mais funcionários têm acesso a tabelas mais vantajosas. Solicite cotação comparativa gratuita.</p></div>
      </div>
    </section>

    <section class="content-section alt">
      <div class="container">
        <h2 class="cs-title">Como Contratar Plano Odonto Empresarial</h2>
        <ul class="steps-list">
          <li><div><h4>Defina o número de vidas</h4><p>MEI: a partir de 1 vida. PME: a partir de 2 vidas. Grandes empresas: sem mínimo definido por operadora.</p></div></li>
          <li><div><h4>Escolha a cobertura necessária</h4><p>Básico (prevenção + restaurações), Completo (+ endodontia + extração) ou Premium (+ ortodontia + implantes).</p></div></li>
          <li><div><h4>Solicite cotação comparativa</h4><p>A Virtua compara as principais operadoras e apresenta tabela com preços, coberturas e rede credenciada próxima à sua empresa.</p></div></li>
          <li><div><h4>Documentação da empresa</h4><p>CNPJ ativo, contrato social, relação de beneficiários (nome, CPF e data de nascimento) e comprovante de endereço.</p></div></li>
          <li><div><h4>Ativação e carteirinhas</h4><p>Após a assinatura do contrato e pagamento da 1ª mensalidade, as carteirinhas digitais ficam disponíveis em 24–48h.</p></div></li>
        </ul>
      </div>
    </section>
"""},

# ══════════════════════════════════════════════════════════════════════════════
"simulacao-seguro-de-vida": {
"anchor": "<!-- Plans -->",
"sections": """
    <section class="content-section alt">
      <div class="container">
        <h2 class="cs-title">O Que é o Seguro de Vida e Por Que Você Precisa de Um?</h2>
        <p class="cs-lead">O <strong>seguro de vida</strong> é um contrato que garante proteção financeira para você e sua família em casos de <strong>morte</strong>, <strong>invalidez permanente</strong> ou <strong>doenças graves</strong>. É um dos instrumentos mais importantes de planejamento financeiro — e um dos mais acessíveis, custando a partir de R$ 30/mês.</p>
        <div class="cs-body">
          <p>Diferente do que muitos pensam, o seguro de vida não é apenas para quem tem dependentes. É indicado para <strong>qualquer pessoa que tenha obrigações financeiras</strong> — prestações, aluguel, pensão alimentícia — ou que queira garantir tranquilidade para sua família em caso de imprevisto.</p>
          <p>As coberturas mais comuns são: <strong>morte por qualquer causa</strong> (natural ou acidental), <strong>morte acidental</strong>, <strong>invalidez permanente por acidente</strong> (IPA), <strong>invalidez funcional</strong>, <strong>diagnóstico de doenças graves</strong> (câncer, infarto, AVC) e <strong>diária por incapacidade temporária</strong>.</p>
          <p>As principais seguradoras do Brasil são: <strong>Bradesco Vida e Previdência</strong>, <strong>Porto Seguro Vida</strong>, <strong>SulAmérica Vida</strong>, <strong>Icatu Seguros</strong>, <strong>Zurich Seguros</strong>, <strong>Prudential</strong> e <strong>Mongeral Aegon</strong>.</p>
          <div class="highlight-box"><p>💡 <strong>Dica Virtua:</strong> O momento ideal para contratar um seguro de vida é <strong>antes</strong> de precisar. Quanto mais jovem e saudável, menor é o prêmio mensal. Não deixe para depois.</p></div>
        </div>
      </div>
    </section>

    <section class="content-section">
      <div class="container">
        <h2 class="cs-title">Coberturas do Seguro de Vida</h2>
        <div class="coverage-grid">
          <div class="coverage-item"><h4>💀 Morte por Qualquer Causa</h4><p>Indenização ao(s) beneficiário(s) em caso de falecimento por doença ou acidente, pagando o capital segurado contratado.</p></div>
          <div class="coverage-item"><h4>🚗 Morte Acidental</h4><p>Indenização adicional ou exclusiva em caso de morte decorrente de acidente, geralmente com valor dobrado.</p></div>
          <div class="coverage-item"><h4>🦽 Invalidez Permanente (IPA)</h4><p>Indenização proporcional ou total em caso de invalidez permanente por acidente, garantindo renda quando você não pode mais trabalhar.</p></div>
          <div class="coverage-item"><h4>🏥 Doenças Graves</h4><p>Pagamento antecipado em caso de diagnóstico de câncer, infarto do miocárdio, AVC ou outras doenças graves listadas na apólice.</p></div>
          <div class="coverage-item"><h4>📅 Diária por Incapacidade</h4><p>Valor diário pago em caso de afastamento temporário por acidente ou doença, cobrindo despesas durante a recuperação.</p></div>
          <div class="coverage-item"><h4>🏡 Assistência Funeral</h4><p>Cobertura dos custos do serviço funerário para o segurado e, em alguns planos, para a família.</p></div>
          <div class="coverage-item"><h4>🎓 Educacional (dependentes)</h4><p>Alguns planos garantem mensalidade escolar para os filhos em caso de morte do segurado.</p></div>
          <div class="coverage-item"><h4>💊 Assistência Médica</h4><p>Cobertura de despesas médicas em caso de acidente, complementando o plano de saúde.</p></div>
        </div>
      </div>
    </section>

    <section class="content-section alt">
      <div class="container">
        <h2 class="cs-title">Tabela de Preços Seguro de Vida 2026</h2>
        <p class="cs-lead">O preço do seguro de vida é calculado com base na <strong>idade</strong>, <strong>capital segurado desejado</strong> e <strong>coberturas escolhidas</strong>. Veja estimativas:</p>
        <div style="overflow-x:auto;">
          <table class="price-table">
            <thead><tr><th>Faixa Etária</th><th>Capital R$ 100.000</th><th>Capital R$ 250.000</th><th>Capital R$ 500.000</th></tr></thead>
            <tbody>
              <tr><td>18 a 25 anos</td><td>R$ 25 – R$ 45</td><td>R$ 55 – R$ 95</td><td>R$ 100 – R$ 180</td></tr>
              <tr><td>26 a 35 anos</td><td>R$ 35 – R$ 65</td><td>R$ 80 – R$ 140</td><td>R$ 150 – R$ 265</td></tr>
              <tr><td>36 a 45 anos</td><td>R$ 60 – R$ 110</td><td>R$ 140 – R$ 250</td><td>R$ 265 – R$ 480</td></tr>
              <tr><td>46 a 55 anos</td><td>R$ 110 – R$ 210</td><td>R$ 260 – R$ 490</td><td>R$ 490 – R$ 940</td></tr>
              <tr><td>56 a 65 anos</td><td>R$ 210 – R$ 420</td><td>R$ 490 – R$ 980</td><td>R$ 940 – R$ 1.870</td></tr>
            </tbody>
          </table>
        </div>
        <div class="highlight-box" style="margin-top:20px;"><p>⚠️ Valores estimados. O prêmio real varia conforme a seguradora, profissão, hábitos de vida e coberturas escolhidas. Faça uma simulação gratuita com a Virtua.</p></div>
      </div>
    </section>

    <section class="content-section">
      <div class="container">
        <h2 class="cs-title">Como Contratar Seguro de Vida</h2>
        <ul class="steps-list">
          <li><div><h4>Defina o capital segurado</h4><p>Quanto sua família precisaria para manter o padrão de vida por 2 a 5 anos? Esse valor orienta o capital ideal.</p></div></li>
          <li><div><h4>Escolha as coberturas</h4><p>Morte, invalidez, doenças graves, diária por incapacidade. Nossa equipe orienta as coberturas mais adequadas para o seu perfil.</p></div></li>
          <li><div><h4>Receba cotações comparativas</h4><p>A Virtua compara as melhores seguradoras (Bradesco, Porto Seguro, SulAmérica, Icatu) para o mesmo perfil.</p></div></li>
          <li><div><h4>Preencha a proposta e declaração de saúde</h4><p>Para capitais acima de R$ 300.000 pode ser solicitado exame médico. Abaixo disso, geralmente apenas declaração.</p></div></li>
          <li><div><h4>Apólice emitida e vigência</h4><p>Após aprovação, a apólice é emitida e a cobertura inicia imediatamente (sem carência para morte acidental).</p></div></li>
        </ul>
      </div>
    </section>
"""},

# ══════════════════════════════════════════════════════════════════════════════
"reembolso-amil": {
"anchor": "<!-- Plans -->",
"sections": """
    <section class="content-section alt">
      <div class="container">
        <h2 class="cs-title">Como Funciona o Reembolso Amil: Guia Completo 2026</h2>
        <p class="cs-lead">O <strong>reembolso Amil</strong> permite que o beneficiário seja atendido por médico, clínica ou hospital fora da rede credenciada e depois solicite o reembolso das despesas à operadora. Nem todos os planos Amil têm essa modalidade — ela está disponível principalmente nos planos <strong>Amil 400</strong>, <strong>Amil 500</strong> e <strong>Amil 750</strong>.</p>
        <div class="cs-body">
          <p>O valor do reembolso é calculado com base na <strong>tabela de honorários Amil</strong>, que pode ser diferente do valor cobrado pelo prestador. Em geral, o reembolso cobre entre <strong>60% e 100%</strong> do valor da tabela Amil, dependendo do plano contratado.</p>
          <p>É importante entender que o reembolso <strong>não é igual ao valor da conta</strong>: se seu médico cobrou R$ 500 por uma consulta e a tabela Amil prevê R$ 200, o reembolso será baseado nos R$ 200. Por isso, é fundamental verificar os valores da tabela antes de usar o reembolso.</p>
          <div class="highlight-box"><p>💡 <strong>Dica Virtua:</strong> Antes de realizar um atendimento fora da rede, verifique no app Amil qual é o valor de reembolso previsto para aquele procedimento. Isso evita surpresas na hora do ressarcimento.</p></div>
        </div>
      </div>
    </section>

    <section class="content-section">
      <div class="container">
        <h2 class="cs-title">Passo a Passo: Como Solicitar Reembolso Amil</h2>
        <ul class="steps-list">
          <li><div><h4>Realize o atendimento e guarde os documentos</h4><p>Nota fiscal ou recibo do prestador, comprovante de pagamento e relatório/receituário médico com CRM do profissional.</p></div></li>
          <li><div><h4>Acesse o app Amil ou portal web</h4><p>Faça login no app Amil (disponível para iOS e Android) ou acesse amil.com.br/beneficiario. Selecione "Solicitar Reembolso".</p></div></li>
          <li><div><h4>Preencha o formulário de reembolso</h4><p>Informe o tipo de atendimento, data, prestador, valor pago e dados bancários para depósito do reembolso.</p></div></li>
          <li><div><h4>Anexe os documentos digitalizados</h4><p>Escaneie ou fotografe a nota fiscal, recibo e prescrição médica. Os documentos devem estar legíveis.</p></div></li>
          <li><div><h4>Acompanhe a análise</h4><p>A Amil tem até <strong>30 dias úteis</strong> para analisar e efetuar o pagamento do reembolso aprovado.</p></div></li>
        </ul>
      </div>
    </section>

    <section class="content-section alt">
      <div class="container">
        <h2 class="cs-title">Prazos e Valores do Reembolso Amil</h2>
        <div style="overflow-x:auto;">
          <table class="price-table">
            <thead><tr><th>Tipo de Atendimento</th><th>Prazo para Solicitar</th><th>Prazo para Pagamento</th></tr></thead>
            <tbody>
              <tr><td>Consultas médicas</td><td>Até 90 dias após o atendimento</td><td>Até 30 dias úteis</td></tr>
              <tr><td>Exames e diagnósticos</td><td>Até 90 dias após o atendimento</td><td>Até 30 dias úteis</td></tr>
              <tr><td>Internações hospitalares</td><td>Até 90 dias após a alta</td><td>Até 30 dias úteis</td></tr>
              <tr><td>Procedimentos ambulatoriais</td><td>Até 90 dias após o atendimento</td><td>Até 30 dias úteis</td></tr>
              <tr><td>Urgência e emergência</td><td>Até 90 dias após o atendimento</td><td>Até 30 dias úteis</td></tr>
            </tbody>
          </table>
        </div>
        <div class="highlight-box" style="margin-top:20px;"><p>⚠️ A Amil pode solicitar documentos adicionais durante a análise. Guarde todos os comprovantes de atendimento por pelo menos 6 meses.</p></div>
      </div>
    </section>

    <section class="content-section">
      <div class="container">
        <h2 class="cs-title">Reembolso Amil Negado: O Que Fazer?</h2>
        <div class="cs-body">
          <p>Se o reembolso foi negado, você tem direito a <strong>recurso</strong>. O primeiro passo é entender o motivo da negativa — normalmente comunicado por e-mail ou pelo app. As razões mais comuns são: documentação incompleta, procedimento não coberto pelo plano, ou valor acima da tabela Amil.</p>
          <p>Para recorrer: acesse o portal Amil e solicite revisão, apresentando a documentação complementar. Caso a negativa persista, você pode registrar uma reclamação na <strong>ANS</strong> (Agência Nacional de Saúde Suplementar) pelo site ans.gov.br ou pelo telefone <strong>0800 701 9656</strong>.</p>
          <p>A Virtua Corretora orienta nossos clientes em todo o processo de reembolso e recursos. Se você contratou seu plano Amil conosco, conte com nosso suporte pós-venda.</p>
        </div>
      </div>
    </section>
"""},

# ══════════════════════════════════════════════════════════════════════════════
"reembolso-sulamerica": {
"anchor": "<!-- Plans -->",
"sections": """
    <section class="content-section alt">
      <div class="container">
        <h2 class="cs-title">Reembolso SulAmérica: Como Funciona e Como Solicitar</h2>
        <p class="cs-lead">O <strong>reembolso SulAmérica</strong> permite que beneficiários dos planos com cobertura de livre escolha sejam atendidos fora da rede credenciada e recebam ressarcimento das despesas. Disponível nos planos <strong>SulAmérica Especial</strong>, <strong>SulAmérica Executivo</strong> e outros com essa modalidade.</p>
        <div class="cs-body">
          <p>O reembolso SulAmérica funciona com base na <strong>tabela de reembolso própria da operadora</strong>. O percentual de cobertura varia de <strong>50% a 100%</strong> do valor da tabela, dependendo do plano contratado. Planos premium como o SulAmérica Executivo oferecem reembolso mais generoso.</p>
          <div class="highlight-box"><p>💡 Consulte sua apólice para verificar se seu plano SulAmérica tem cobertura de reembolso e qual é o percentual de ressarcimento.</p></div>
        </div>
      </div>
    </section>

    <section class="content-section">
      <div class="container">
        <h2 class="cs-title">Como Solicitar Reembolso SulAmérica: Passo a Passo</h2>
        <ul class="steps-list">
          <li><div><h4>Realize o atendimento e solicite nota fiscal</h4><p>Peça nota fiscal ou recibo com dados do prestador (nome, CRM/CRO, CNPJ), procedimento realizado e valor cobrado.</p></div></li>
          <li><div><h4>Acesse o app Saúde SulAmérica</h4><p>Disponível gratuitamente para iOS e Android. Acesse "Serviços" → "Solicitar Reembolso".</p></div></li>
          <li><div><h4>Informe os dados do atendimento</h4><p>Tipo de atendimento, data, prestador, CNPJ/CPF do profissional, valor pago e dados bancários.</p></div></li>
          <li><div><h4>Anexe a documentação</h4><p>Nota fiscal ou recibo original, comprovante de pagamento, receita/relatório médico e resultado de exames (se aplicável).</p></div></li>
          <li><div><h4>Aguarde a análise</h4><p>A SulAmérica tem até <strong>30 dias úteis</strong> para analisar e efetuar o pagamento. Acompanhe pelo app.</p></div></li>
        </ul>
      </div>
    </section>

    <section class="content-section alt">
      <div class="container">
        <h2 class="cs-title">Documentos Necessários para Reembolso SulAmérica</h2>
        <div class="coverage-grid">
          <div class="coverage-item"><h4>📄 Nota Fiscal ou Recibo</h4><p>Com nome do prestador, CRM/CNPJ, procedimento, data e valor. Necessário para todos os tipos de atendimento.</p></div>
          <div class="coverage-item"><h4>💳 Comprovante de Pagamento</h4><p>Extrato bancário, comprovante de transferência ou recibo de pagamento confirmando o valor pago.</p></div>
          <div class="coverage-item"><h4>📋 Relatório Médico</h4><p>Relatório ou receituário do profissional com CRM, diagnóstico (CID) e justificativa do procedimento.</p></div>
          <div class="coverage-item"><h4>🔬 Resultados de Exames</h4><p>Para reembolso de exames diagnósticos, anexe o resultado completo junto à solicitação médica.</p></div>
          <div class="coverage-item"><h4>🏥 Para Internações</h4><p>Resumo de alta hospitalar, notas fiscais do hospital e anestesista, e relatório cirúrgico quando aplicável.</p></div>
          <div class="coverage-item"><h4>🆔 Dados Bancários</h4><p>Banco, agência, conta corrente e CPF do titular (deve ser o próprio beneficiário).</p></div>
        </div>
      </div>
    </section>
"""},

}  # fim de CONTENT


def inject_styles(html):
    """Injeta os estilos compartilhados antes de </head>."""
    if "content-section" not in html:
        html = html.replace("</head>", SHARED_STYLES + "\n</head>", 1)
    return html


def find_insert_point(html, anchor_comment):
    """Encontra o ponto de inserção DEPOIS da próxima </section> após o anchor."""
    idx = html.find(anchor_comment)
    if idx == -1:
        return -1
    # Acha o </section> mais próximo DEPOIS do anchor
    close = html.find("</section>", idx)
    if close == -1:
        return -1
    return close + len("</section>")


def process_page(slug, data):
    filepath = os.path.join(BASE, slug, "index.html")
    if not os.path.exists(filepath):
        print(f"  ⚠  Não encontrado: {filepath}")
        return 0

    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()

    if "content-section" in html:
        print(f"  ↩  Já enriquecido, pulando.")
        return 0

    # Injeta estilos
    html = inject_styles(html)

    # Acha ponto de inserção
    anchor = data["anchor"]
    insert_at = find_insert_point(html, anchor)
    if insert_at == -1:
        # Fallback: inserir antes da seção FAQ
        insert_at = html.find("<!-- FAQ -->")
        if insert_at == -1:
            insert_at = html.find("<!-- CTA Final -->")
        if insert_at == -1:
            print(f"  ⚠  Ponto de inserção não encontrado em {slug}")
            return 0

    html = html[:insert_at] + "\n" + data["sections"] + html[insert_at:]

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)

    # Contar palavras resultantes
    words = len(re.sub(r"<[^>]+>", " ", html).split())
    print(f"  ✓  Conteúdo adicionado → ~{words} palavras no total")
    return words


def main():
    pages = list(CONTENT.keys())
    print(f"Enriquecendo {len(pages)} páginas com conteúdo SEO completo...\n")

    total_words_before = 0
    total_words_after = 0

    for slug, data in CONTENT.items():
        print(f"[{slug}]")
        filepath = os.path.join(BASE, slug, "index.html")
        if os.path.exists(filepath):
            before = len(re.sub(r"<[^>]+>", " ", open(filepath).read()).split())
            total_words_before += before
            after = process_page(slug, data)
            if after:
                total_words_after += after
            else:
                total_words_after += before
        print()

    print(f"✅ Concluído!")
    print(f"   Palavras antes: ~{total_words_before:,}")
    print(f"   Palavras depois: ~{total_words_after:,}")
    if total_words_before:
        pct = ((total_words_after - total_words_before) / total_words_before) * 100
        print(f"   Aumento: +{pct:.0f}%")


if __name__ == "__main__":
    main()
