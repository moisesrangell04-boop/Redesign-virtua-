# Guia de Migração SEO-Safe: WordPress → HTML Estático (Hostinger)

## Situação Atual

O site `virtuacorretora.com.br` roda em WordPress + Elementor com Yoast SEO. Ele possui:
- **50+ páginas indexadas** (home, blog, produtos, páginas de operadoras, FAQs)
- **Schema Markup** (Organization, FAQ)
- **Sitemaps XML** gerados pelo Yoast
- **Backlinks e autoridade de domínio** acumulados

> [!CAUTION]
> A Virtua depende 100% de leads orgânicos. Qualquer erro nessa migração pode causar **queda imediata de tráfego**. Siga cada etapa com cuidado.

---

## Estratégia Recomendada: Migração em Fases

### Fase 1 — Antes da Troca (Preparação)

#### 1.1 Backup Completo do Site Atual
- Exporte todo o conteúdo WordPress (Ferramentas → Exportar → Todo conteúdo)
- Baixe backup completo dos arquivos e banco de dados via cPanel/hPanel
- Salve uma cópia do `robots.txt` e de todos os sitemaps XML

#### 1.2 Mapear Todas as URLs do Site Atual
O site atual tem **dezenas de páginas indexadas** com URLs no formato WordPress. Cada uma precisa de redirecionamento 301. As principais categorias:

| Tipo | Exemplo de URL Atual | Página no Novo Site |
|------|---------------------|---------------------|
| Home | `/` | [index.html](file:///c:/Users/growt/OneDrive/Documentos/Virtua%20Corretora/redesign/index.html) |
| Simulação | `/simulation/` | `index.html#contato` |
| Blog | `/blog/` | [institucional-blog.html](file:///c:/Users/growt/OneDrive/Documentos/Virtua%20Corretora/redesign/institucional-blog.html) |
| Política Privacidade | `/politica-de-privacidade/` | [institucional-privacidade.html](file:///c:/Users/growt/OneDrive/Documentos/Virtua%20Corretora/redesign/institucional-privacidade.html) |
| Seguro Transporte | `/seguro-transporte-de-cargas/` | [index.html](file:///c:/Users/growt/OneDrive/Documentos/Virtua%20Corretora/redesign/index.html) (ou criar página) |
| Rede Credenciada Assim | `/rede-credenciada-assim/` | [index.html](file:///c:/Users/growt/OneDrive/Documentos/Virtua%20Corretora/redesign/index.html) |
| Rede Credenciada Odontoprev | `/rede-credenciada-odontoprev/` | [produto-odonto.html](file:///c:/Users/growt/OneDrive/Documentos/Virtua%20Corretora/redesign/produto-odonto.html) |
| Rede Credenciada SulAmérica | `/rede-credenciada-sulamerica-odonto/` | [produto-odonto.html](file:///c:/Users/growt/OneDrive/Documentos/Virtua%20Corretora/redesign/produto-odonto.html) |
| Telefones Assim | `/telefones-assim-saude/` | `index.html#contato` |
| Telefones SulAmérica Odonto | `/telefones-sulamerica-odonto/` | `index.html#contato` |
| Telefones Seguro Vida | `/telefones-seguro-de-vida/` | [produto-vida.html](file:///c:/Users/growt/OneDrive/Documentos/Virtua%20Corretora/redesign/produto-vida.html) |
| FAQs SulAmérica Odonto | `/perguntas-frequentes-sulamerica-odonto/` | [institucional-faq.html](file:///c:/Users/growt/OneDrive/Documentos/Virtua%20Corretora/redesign/institucional-faq.html) |
| FAQs Assim | `/perguntas-frequentes-assim/` | [institucional-faq.html](file:///c:/Users/growt/OneDrive/Documentos/Virtua%20Corretora/redesign/institucional-faq.html) |
| Pagina do Autor | `/pagina-do-autor/` | [institucional-quem-somos.html](file:///c:/Users/growt/OneDrive/Documentos/Virtua%20Corretora/redesign/institucional-quem-somos.html) |
| Telemedicina SulAmérica | `/telemedicina-medico-na-tela-sulamerica/` | [produto-saude.html](file:///c:/Users/growt/OneDrive/Documentos/Virtua%20Corretora/redesign/produto-saude.html) |
| 2ª Via Boleto Assim | `/2a-via-boleto-assim/` | [index.html](file:///c:/Users/growt/OneDrive/Documentos/Virtua%20Corretora/redesign/index.html) |
| Estágio Supervisionado | `/estagio-supervisionado/` | [empresa-estagio.html](file:///c:/Users/growt/OneDrive/Documentos/Virtua%20Corretora/redesign/empresa-estagio.html) |
| Estágio Psicologia | `/estagio-psicologia/` | [empresa-estagio.html](file:///c:/Users/growt/OneDrive/Documentos/Virtua%20Corretora/redesign/empresa-estagio.html) |
| Amil Fácil RJ | `/novo-plano-amil-facil-rj/` | [produto-saude.html](file:///c:/Users/growt/OneDrive/Documentos/Virtua%20Corretora/redesign/produto-saude.html) |
| Amil Dental | `/5-vantagens-do-plano-amil-dental/` | [produto-odonto.html](file:///c:/Users/growt/OneDrive/Documentos/Virtua%20Corretora/redesign/produto-odonto.html) |
| Plano cobre parto | `/plano-de-saude-cobre-parto/` | [produto-saude.html](file:///c:/Users/growt/OneDrive/Documentos/Virtua%20Corretora/redesign/produto-saude.html) |
| Cirurgia Bariátrica | `/cirurgia-bariatrica/` | [produto-saude.html](file:///c:/Users/growt/OneDrive/Documentos/Virtua%20Corretora/redesign/produto-saude.html) |
| Reajuste 2022 | `/reajuste-plano-de-saude-2022/` | [produto-saude.html](file:///c:/Users/growt/OneDrive/Documentos/Virtua%20Corretora/redesign/produto-saude.html) |
| Vitamina D | `/vitamina-d/` | [institucional-blog.html](file:///c:/Users/growt/OneDrive/Documentos/Virtua%20Corretora/redesign/institucional-blog.html) |
| Posts blog (todos) | `/5-alimentos-*`, `/fotos-de-perfil/`, etc. | [institucional-blog.html](file:///c:/Users/growt/OneDrive/Documentos/Virtua%20Corretora/redesign/institucional-blog.html) |
| Odonto 2022 RJ | `/melhores-planos-odontologicos-2022-no-rio-de-janeiro/` | [produto-odonto.html](file:///c:/Users/growt/OneDrive/Documentos/Virtua%20Corretora/redesign/produto-odonto.html) |
| Suspensão Unimed CLINERP | `/suspensao-unimed-na-clinerp/` | [produto-saude.html](file:///c:/Users/growt/OneDrive/Documentos/Virtua%20Corretora/redesign/produto-saude.html) |

> [!IMPORTANT]
> Cada URL acima gera tráfego orgânico. Se alguém buscar "rede credenciada assim saúde" ou "amil fácil rj" e clicar no resultado do Google, ele precisa chegar a uma página válida — senão perde o lead E o Google penaliza o site.

#### 1.3 Verificar Rankings Atuais
- Acesse o **Google Search Console** do domínio e exporte:
  - Todas as queries que geram impressões e cliques
  - Todas as páginas indexadas
  - Core Web Vitals
- Isso será sua baseline para comparação pós-migração

#### 1.4 Registrar no Google Search Console (se ainda não tem acesso)
- Você PRECISA ter acesso ao Search Console para o pós-migração
- Método: verificação via DNS TXT record na Hostinger

---

### Fase 2 — Preparação Técnica do Novo Site

#### 2.1 Criar o arquivo `.htaccess` com redirects 301
Na Hostinger (Apache), crie um `.htaccess` na raiz com TODOS os redirecionamentos:

```apache
RewriteEngine On

# Forçar www e HTTPS
RewriteCond %{HTTP_HOST} !^www\. [NC]
RewriteRule ^(.*)$ https://www.virtuacorretora.com.br/$1 [R=301,L]

RewriteCond %{HTTPS} off
RewriteRule ^(.*)$ https://www.virtuacorretora.com.br/$1 [R=301,L]

# ===== REDIRECTS 301 =====
# Páginas de operadoras (rede credenciada, telefones, FAQs)
Redirect 301 /simulation/ /index.html
Redirect 301 /rede-credenciada-assim/ /index.html
Redirect 301 /rede-credenciada-odontoprev/ /produto-odonto.html
Redirect 301 /rede-credenciada-sulamerica-odonto/ /produto-odonto.html
Redirect 301 /telefones-assim-saude/ /index.html
Redirect 301 /telefones-sulamerica-odonto/ /index.html
Redirect 301 /telefones-seguro-de-vida/ /produto-vida.html
Redirect 301 /perguntas-frequentes-sulamerica-odonto/ /institucional-faq.html
Redirect 301 /perguntas-frequentes-assim/ /institucional-faq.html
Redirect 301 /telemedicina-medico-na-tela-sulamerica/ /produto-saude.html
Redirect 301 /2a-via-boleto-assim/ /index.html

# Páginas institucionais
Redirect 301 /politica-de-privacidade/ /institucional-privacidade.html
Redirect 301 /pagina-do-autor/ /institucional-quem-somos.html
Redirect 301 /blog/ /institucional-blog.html

# Páginas de produtos/serviços
Redirect 301 /seguro-transporte-de-cargas/ /index.html
Redirect 301 /estagio-supervisionado/ /empresa-estagio.html
Redirect 301 /estagio-psicologia/ /empresa-estagio.html

# Blog posts → redirecionar para blog ou página mais relevante
Redirect 301 /novo-plano-amil-facil-rj/ /produto-saude.html
Redirect 301 /5-vantagens-do-plano-amil-dental/ /produto-odonto.html
Redirect 301 /plano-de-saude-cobre-parto/ /produto-saude.html
Redirect 301 /cirurgia-bariatrica/ /produto-saude.html
Redirect 301 /reajuste-plano-de-saude-2022/ /produto-saude.html
Redirect 301 /melhores-planos-odontologicos-2022-no-rio-de-janeiro/ /produto-odonto.html
Redirect 301 /suspensao-unimed-na-clinerp/ /produto-saude.html
Redirect 301 /vitamina-d/ /institucional-blog.html
Redirect 301 /5-alimentos-para-deixar-sua-pela-mais-bonita/ /institucional-blog.html
Redirect 301 /fotos-de-perfil/ /institucional-blog.html

# Catch-all: qualquer URL antiga do WordPress vai para a home
ErrorDocument 404 /index.html
```

> [!TIP]
> Após o go-live, monitore o Search Console por 2-4 semanas e adicione novos redirects conforme erros 404 aparecerem.

#### 2.2 Criar `sitemap.xml`
Crie um novo sitemap na raiz do novo site listando todas as páginas:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>https://www.virtuacorretora.com.br/</loc><priority>1.0</priority></url>
  <url><loc>https://www.virtuacorretora.com.br/produto-saude.html</loc></url>
  <url><loc>https://www.virtuacorretora.com.br/produto-odonto.html</loc></url>
  <url><loc>https://www.virtuacorretora.com.br/produto-vida.html</loc></url>
  <url><loc>https://www.virtuacorretora.com.br/produto-auto.html</loc></url>
  <url><loc>https://www.virtuacorretora.com.br/produto-viagem.html</loc></url>
  <url><loc>https://www.virtuacorretora.com.br/produto-residencial.html</loc></url>
  <url><loc>https://www.virtuacorretora.com.br/empresa-saude.html</loc></url>
  <url><loc>https://www.virtuacorretora.com.br/empresa-odonto.html</loc></url>
  <url><loc>https://www.virtuacorretora.com.br/empresa-vida.html</loc></url>
  <url><loc>https://www.virtuacorretora.com.br/empresa-frota.html</loc></url>
  <url><loc>https://www.virtuacorretora.com.br/empresa-garantia.html</loc></url>
  <url><loc>https://www.virtuacorretora.com.br/empresa-estagio.html</loc></url>
  <url><loc>https://www.virtuacorretora.com.br/institucional-quem-somos.html</loc></url>
  <url><loc>https://www.virtuacorretora.com.br/institucional-blog.html</loc></url>
  <url><loc>https://www.virtuacorretora.com.br/institucional-faq.html</loc></url>
  <url><loc>https://www.virtuacorretora.com.br/institucional-privacidade.html</loc></url>
  <url><loc>https://www.virtuacorretora.com.br/institucional-lgpd.html</loc></url>
</urlset>
```

#### 2.3 Criar `robots.txt`
```
User-agent: *
Disallow:

Sitemap: https://www.virtuacorretora.com.br/sitemap.xml
```

#### 2.4 Verificar SEO On-Page do Novo Site
Isso já está parcialmente feito, mas é importante confirmar:
- [x] `<title>` em todas as páginas
- [x] `<meta name="description">` na [index.html](file:///c:/Users/growt/OneDrive/Documentos/Virtua%20Corretora/redesign/index.html)
- [ ] Adicionar `<meta name="description">` nas subpáginas
- [x] Schema Markup (Organization, FAQ) na [index.html](file:///c:/Users/growt/OneDrive/Documentos/Virtua%20Corretora/redesign/index.html)
- [x] Heading hierarchy (`<h1>` único por página)
- [ ] Canonical tag em todas as páginas
- [ ] Open Graph tags para compartilhamento social

#### 2.5 Adicionar Tags Canonical
Em cada página HTML, adicione no `<head>`:
```html
<link rel="canonical" href="https://www.virtuacorretora.com.br/[nome-da-pagina].html">
```

---

### Fase 3 — Dia da Migração (Checklist)

1. **Aponte o domínio para a Hostinger** (alterar DNS/Nameservers)
2. **Configure SSL** (Let's Encrypt gratuito na Hostinger)
3. **Faça upload de todos os arquivos** para `public_html`
4. **Verifique o `.htaccess`** — os redirects 301 estão funcionando?
5. **Teste as URLs antigas** — cada URL do WordPress deve redirecionar corretamente
6. **Teste SSL** — `https://www.virtuacorretora.com.br` e `https://virtuacorretora.com.br` devem funcionar
7. **Submeta o novo sitemap** no Google Search Console
8. **Peça a indexação** das páginas principais no Search Console

---

### Fase 4 — Pós-Migração (Monitoramento)

#### Primeiras 48h
- Verifique se o SSL está ativo e redirecionando HTTP → HTTPS
- Teste todas as URLs antigas manualmente
- Monitore erros 404 no Search Console → adicione redirects para cada um

#### Primeira Semana
- Monitore impressões e cliques no Search Console diariamente
- Verifique se o Google está indexando as novas páginas
- Uma **pequena queda temporária** (5-15%) é normal nos primeiros dias

#### Primeiro Mês
- Compare métricas com a baseline (impressões, cliques, posições médias)
- Resolva todos os erros de cobertura no Search Console
- Verifique Core Web Vitals (o site estático DEVE ser mais rápido que WordPress)

> [!NOTE]
> O site estático tende a ter **Performance muito superior** ao WordPress, o que beneficia o ranking. A velocidade de carregamento pode melhorar significativamente, o que é um fator positivo de SEO.

---

## Resumo dos Riscos e Mitigações

| Risco | Impacto | Mitigação |
|-------|---------|-----------|
| URLs antigas retornando 404 | **Alto** — perda de tráfego orgânico | Redirects 301 + catch-all 404 → home |
| Perda de conteúdo indexado (blog posts) | **Médio** — Google pode desindexar | Redirects 301 para página mais relevante |
| SSL mal configurado | **Alto** — mixed content, warnings | Configurar Let's Encrypt antes do go-live |
| Sitemap apontando para URLs erradas | **Médio** — indexação lenta | Novo sitemap.xml limpo + submissão |
| Perda de Schema Markup | **Baixo** — já implementado no novo site | Verificar com Rich Results Test |
| DNS lento para propagar | **Baixo** — indisponibilidade temporária | Reduzir TTL 24h antes da migração |

---

## Ação Imediata Recomendada

> [!IMPORTANT]
> **Antes de trocar qualquer coisa**, peça ao seu cliente acesso ao Google Search Console do domínio. Sem isso, você não terá como monitorar o impacto da migração e corrigir problemas rapidamente.

A migração de WordPress para site estático é **segura para SEO** desde que:
1. Todos os redirects 301 sejam implementados
2. O conteúdo principal seja equivalente ou melhor
3. Schema markup e meta tags estejam presentes
4. O monitoramento pós-migração seja rigoroso nas primeiras 2-4 semanas
