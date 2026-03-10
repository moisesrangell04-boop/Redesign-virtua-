<?php
/**
 * Snippet: FAQ Schema Markup - Virtua Corretora Homepage
 * Descrição: Adiciona structured data JSON-LD para FAQ Schema na homepage
 * Onde executar: Somente no front-end
 * 
 * INSTRUÇÕES:
 * 1. WP Admin → Snippets → Adicionar Novo
 * 2. Nome: "FAQ Schema Markup - Homepage"
 * 3. Cole este código
 * 4. Em "Executar apenas": selecione "Somente no front-end"
 * 5. Salvar e Ativar
 */

add_action('wp_head', function() {
    if (is_front_page() || is_home()) {
?>
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
        {
            "@type": "Question",
            "name": "Quais são os tipos de contratações de planos de saúde empresariais?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "Os planos de saúde empresariais podem ser contratados para redução de custos para a família do titular da empresa (30 a 40% mais baratos), para funcionários da empresa, ou para categorias específicas como supervisores e gerentes na modalidade livre adesão ou CBO. A partir de 02 vidas é possível contratar um plano de saúde empresarial."
            }
        },
        {
            "@type": "Question",
            "name": "Quais são os planos de saúde da Amil?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "A Amil oferece planos nacionais (Amil S380, S450, S750) com cobertura nacional e benefícios como Telemedicina e descontos em farmácias, além de planos regionais como Amil Fácil S75 RJ (cobertura no Rio de Janeiro, Duque de Caxias, Niterói, São Gonçalo e Nova Iguaçu) e Amil Fácil S80 SP para as maiores cidades de 5 estados."
            }
        },
        {
            "@type": "Question",
            "name": "Quais são os planos de saúde do Bradesco?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "O Bradesco comercializa planos regionais no Grande Rio (TRME e TRMQ) e nacionais (TRWE/TRWQ, FCER/FCQR, TREN/TRQN). Os planos nacionais incluem direito a reembolso, rede credenciada premium e benefícios exclusivos como seguro viagem nacional e internacional."
            }
        },
        {
            "@type": "Question",
            "name": "Quais são os benefícios do Plano de Saúde SulAmérica?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "A SulAmérica oferece descontos de até 70% em mais de 25 mil farmácias, reembolso 100% online pelo aplicativo, Telemedicina para consultas imediatas e agendadas, Psicólogo na Tela, seguro viagem nacional e internacional, e remissão de custos por 2 anos em caso de falecimento do titular."
            }
        },
        {
            "@type": "Question",
            "name": "Quais são os Planos de Saúde SulAmérica disponíveis?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "Os principais planos SulAmérica são: Direto Rio II (regional no Grande Rio com hospitais como Quinta D'Or e Niterói D'Or), Direto Nacional (opção mais acessível com abrangência nacional e reembolso), Especial 100 (nacional com rede estendida incluindo Copa D'Or e Barra D'Or, mais seguro viagem internacional) e Prestige (cobertura premium com procedimentos sem limite de utilização)."
            }
        },
        {
            "@type": "Question",
            "name": "Quais são os Planos de Saúde Intermédica?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "A Intermédica oferece os planos Smart 200 RJ (regional com cobertura em Itaboraí, Maricá, Niterói e São Gonçalo), Smart 500 (grupo de municípios incluindo interior do RJ como Campos, Cabo Frio e Petrópolis) e Advance 600 (nacional com reembolso e programas de medicina preventiva)."
            }
        },
        {
            "@type": "Question",
            "name": "Quais são os planos de saúde Unimed Ferj?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "Os principais planos Unimed FERJ são: Unimed Estilo (estadual com atendimento para urgência e emergência em todo Brasil, com coparticipação parcial) e Unimed Prime (nacional, disponível em acomodação coletiva e apartamento com grandes hospitais no Brasil)."
            }
        },
        {
            "@type": "Question",
            "name": "Qual é o melhor plano de saúde Assim?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "A Assim Saúde oferece: MAX (Rio de Janeiro, São Gonçalo, Duque de Caxias, Mesquita e Niterói), Clássico (13 municípios), Ideal (27 municípios incluindo interior) e Superior (melhor rede credenciada, 27 municípios). Cada plano tem uma rede credenciada específica."
            }
        },
        {
            "@type": "Question",
            "name": "O que o plano odontológico Amil cobre?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "O plano Amil Dental Clássico (Dental 205) cobre integralmente: urgência, consultas, prevenção (limpeza e flúor), radiografias, tratamento de gengiva, tratamento para crianças, tratamento de canal, restaurações, cirurgias e extrações (incluindo siso), documentação ortodôntica e coroas."
            }
        },
        {
            "@type": "Question",
            "name": "Como funciona a contratação de um seguro auto?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "Contratar um seguro auto é simples: são necessários os dados do motorista principal, dados do veículo e local onde o veículo pernoita. A Virtua Corretora realiza cotações nas maiores seguradoras do Brasil para encontrar o melhor custo-benefício. Na renovação, conseguimos descontos de 10 a 40%."
            }
        }
    ]
}
</script>
<?php
    }
});
