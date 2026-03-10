<?php
/**
 * Snippet: Organization Schema + LocalBusiness Schema
 * Descrição: Structured data para a empresa aparecer melhor no Google
 * Onde executar: Somente no front-end
 * 
 * INSTRUÇÕES:
 * 1. WP Admin → Snippets → Adicionar Novo
 * 2. Nome: "Organization Schema - Virtua Corretora"
 * 3. Cole este código
 * 4. Em "Executar apenas": selecione "Somente no front-end"
 * 5. Salvar e Ativar
 * 
 * BÔNUS: Este snippet é adicional ao FAQ Schema e ajuda o Google
 * a entender melhor a empresa, exibindo informações no painel de conhecimento.
 */

add_action('wp_head', function() {
?>
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "InsuranceAgency",
    "name": "Virtua Corretora de Seguros",
    "url": "https://www.virtuacorretora.com.br",
    "logo": "https://www.virtuacorretora.com.br/wp-content/uploads/2023/11/cropped-virtua-corretora-de-planos-de-saude-1.webp",
    "description": "Corretora de Seguros e Planos de Saúde no Rio de Janeiro. Especializada em Plano de Saúde, Plano Odontológico, Seguro de Vida, Seguro Auto e mais.",
    "telephone": ["+5522999404840", "+5522998811541"],
    "email": "contato@virtuacorretora.com.br",
    "sameAs": [],
    "address": [
        {
            "@type": "PostalAddress",
            "streetAddress": "Av. das Américas, 3443 - Condomínio Américas Corporate, Bloco 3B, 2º Andar",
            "addressLocality": "Rio de Janeiro",
            "addressRegion": "RJ",
            "postalCode": "",
            "addressCountry": "BR",
            "name": "Escritório Barra da Tijuca"
        },
        {
            "@type": "PostalAddress",
            "streetAddress": "Rua Barão da Lagoa Dourada, 237, sala 19, Condomínio Alto do Liceu",
            "addressLocality": "Campos dos Goytacazes",
            "addressRegion": "RJ",
            "postalCode": "28035-211",
            "addressCountry": "BR",
            "name": "Escritório Campos dos Goytacazes"
        }
    ],
    "areaServed": {
        "@type": "State",
        "name": "Rio de Janeiro"
    },
    "priceRange": "$$",
    "openingHoursSpecification": {
        "@type": "OpeningHoursSpecification",
        "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
        "opens": "09:00",
        "closes": "18:00"
    },
    "hasOfferCatalog": {
        "@type": "OfferCatalog",
        "name": "Seguros e Planos de Saúde",
        "itemListElement": [
            {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Plano de Saúde"}},
            {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Plano Odontológico"}},
            {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Seguro de Vida"}},
            {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Seguro Auto"}},
            {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Seguro Viagem"}},
            {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Seguro Residencial"}},
            {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Previdência Privada"}},
            {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Plano de Saúde Pet"}}
        ]
    }
}
</script>
<?php
});
