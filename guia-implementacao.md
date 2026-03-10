# 🛠️ Guia de Implementação — Virtua Corretora

## Visão Geral do que será feito

| # | Correção | Método | Risco SEO |
|---|----------|--------|-----------|
| 1 | Erros de texto | Elementor | ✅ Zero |
| 2 | Telefone errado | Elementor | ✅ Zero |
| 3 | H1 duplicados (5→1) | Code Snippets | ✅ Zero (melhora SEO) |
| 4 | FAQ Schema | Code Snippets | ✅ Zero (melhora SEO) |
| 5 | Organization Schema | Code Snippets | ✅ Zero (melhora SEO) |
| 6 | Seção avaliações (Google + RA) | Elementor + Code Snippets | ✅ Zero (adiciona conteúdo) |

> [!IMPORTANT]
> **Faça backup antes!** WP Admin → Ferramentas → Exportar → Todo conteúdo (ou use plugin UpdraftPlus). Nenhuma dessas mudanças altera URLs ou remove conteúdo, mas backup é sempre bom.

---

## ETAPA 1 — Instalar o Plugin Code Snippets

1. WP Admin → **Plugins** → **Adicionar Novo**
2. Buscar: **"Code Snippets"**
3. Instalar o plugin de **Code Snippets Pro** (ícone azul com `</>`)
4. **Ativar**

---

## ETAPA 2 — Correções de Texto no Elementor

1. WP Admin → **Páginas** → **Home** → **Editar com Elementor**

### Correção 2A — "precisar" → "precisa"
- Localize a seção **"Qual sua necessidade hoje? Faça uma Simulação"**
- Clique no widget de texto abaixo do título
- Encontre: `Você não precisar perder tempo`
- Corrija para: `Você não precisa perder tempo`

### Correção 2B — Textos grudados (se visíveis nos cards)
- Se nos cards aparecer "Planode Saúde" ou "SeguroEstágio", corrija para "Plano de Saúde" e "Seguro Estágio"

> [!NOTE]
> Nos screenshots que capturei, os cards visuais pareciam corretos ("Plano de Saúde", "Seguro Estágio"). Pode ser que o erro esteja apenas no código HTML interno. Verifique no Elementor.

📸 **Seção onde está o erro "precisar":**
![Seção Simulação com erro de texto visível na parte inferior](C:\Users\growt\.gemini\antigravity\brain\80ccc67c-d940-47eb-a2c4-1670546a8bcc\desktop_section_3_1773064988807.png)

---

## ETAPA 3 — Correção do Telefone

1. Ainda no Elementor, localize o **Header** (topo azul escuro)
2. Clique no widget do telefone
3. No campo **Link**, verifique se está `tel:+5522999404840`
4. Repita para ambos os ícones (telefone e WhatsApp)
5. Se o WhatsApp abrir um popup, edite o popup também

📸 **Header com os telefones:**
![Header com números de telefone](C:\Users\growt\.gemini\antigravity\brain\80ccc67c-d940-47eb-a2c4-1670546a8bcc\desktop_hero_1773064976308.png)

---

## ETAPA 4 — Adicionar Snippets de Código

### Snippet 1: FAQ Schema Markup
1. WP Admin → **Snippets** → **Adicionar Novo**
2. **Título:** `FAQ Schema Markup - Homepage`
3. Copie o conteúdo de [snippet-1-faq-schema.php](file:///C:/Users/growt/.gemini/antigravity/scratch/virtua-corretora-fixes/snippet-1-faq-schema.php)
4. **Cole** no editor (remova as linhas de comentário do topo com `/**` se quiser)
5. Em **"Executar apenas"**: selecione **"Somente no front-end"**
6. **Salvar e Ativar**

### Snippet 2: Fix H1 Tags
1. **Snippets** → **Adicionar Novo**
2. **Título:** `Fix H1 Tags - Carousel Slides`
3. Copie o conteúdo de [snippet-2-fix-h1-tags.php](file:///C:/Users/growt/.gemini/antigravity/scratch/virtua-corretora-fixes/snippet-2-fix-h1-tags.php)
4. Cole, configure "Somente no front-end", **Salvar e Ativar**

### Snippet 3: Organization Schema (bônus)
1. **Snippets** → **Adicionar Novo**
2. **Título:** `Organization Schema - Virtua Corretora`
3. Copie o conteúdo de [snippet-3-organization-schema.php](file:///C:/Users/growt/.gemini/antigravity/scratch/virtua-corretora-fixes/snippet-3-organization-schema.php)
4. Cole, configure "Somente no front-end", **Salvar e Ativar**

> [!TIP]
> No snippet 3, verifique se a URL do logo está correta. Pode ser necessário pegar a URL real do logo no Media Library do WordPress.

### Snippet 4: CSS das Avaliações
1. **Snippets** → **Adicionar Novo**
2. **Título:** `CSS - Seção Avaliações Google e RA`
3. Copie o conteúdo de [snippet-4-avaliacoes-css.php](file:///C:/Users/growt/.gemini/antigravity/scratch/virtua-corretora-fixes/snippet-4-avaliacoes-css.php)
4. Cole, configure "Somente no front-end", **Salvar e Ativar**

---

## ETAPA 5 — Seção "Como somos avaliados" (Google + Reclame Aqui)

1. Volte ao **Elementor** na homepage
2. Localize a seção **"Como somos avaliados no mercado?"**
3. Adicione (ou substitua o conteúdo vazio por) um widget **HTML**
4. Copie o conteúdo de [html-avaliacoes-section.html](file:///C:/Users/growt/.gemini/antigravity/scratch/virtua-corretora-fixes/html-avaliacoes-section.html)
5. Cole dentro do widget HTML

> [!WARNING]
> **Antes de publicar**, confirme os dados reais:
> - **Google:** A nota encontrada foi **4.9/5.0** com **154 avaliações** — verifique se está atualizada
> - **Reclame Aqui:** Acesse [reclameaqui.com.br](https://www.reclameaqui.com.br) e busque "Virtua Corretora de Seguros" para ver a nota e reputação reais. Atualize no HTML!

---

## ETAPA 6 — Publicar e Verificar

### Publicar
1. No Elementor, clique **Preview** para conferir tudo
2. Se estiver tudo certo, clique **Publicar**
3. Abra o site em uma aba anônima para conferir

### Verificações

| Verificação | Como fazer |
|------------|-----------|
| Textos corrigidos | Visitar a página e conferir a seção de simulação |
| Telefone | Clicar no número pelo celular |
| H1 tags | F12 → Console → `document.querySelectorAll('h1').length` → deve ser **1** |
| FAQ Schema | [Google Rich Results Test](https://search.google.com/test/rich-results) → colar a URL |
| Org Schema | Mesmo teste acima, verificar se InsuranceAgency aparece |
| Avaliações | Visual — a seção deve exibir os cards do Google e Reclame Aqui |

### Monitoramento (7 dias após):
- **Google Search Console** → Performance → impressões e cliques devem se manter ou subir
- Se algo estiver errado, basta **desativar** o snippet no Code Snippets (sem deletar)

---

## Arquivos Criados

| Arquivo | Propósito |
|---------|-----------|
| [snippet-1-faq-schema.php](file:///C:/Users/growt/.gemini/antigravity/scratch/virtua-corretora-fixes/snippet-1-faq-schema.php) | FAQ Schema para rich snippets no Google |
| [snippet-2-fix-h1-tags.php](file:///C:/Users/growt/.gemini/antigravity/scratch/virtua-corretora-fixes/snippet-2-fix-h1-tags.php) | Corrige H1 duplicados (5→1) |
| [snippet-3-organization-schema.php](file:///C:/Users/growt/.gemini/antigravity/scratch/virtua-corretora-fixes/snippet-3-organization-schema.php) | Schema da empresa para Google |
| [snippet-4-avaliacoes-css.php](file:///C:/Users/growt/.gemini/antigravity/scratch/virtua-corretora-fixes/snippet-4-avaliacoes-css.php) | CSS dos cards de avaliação |
| [html-avaliacoes-section.html](file:///C:/Users/growt/.gemini/antigravity/scratch/virtua-corretora-fixes/html-avaliacoes-section.html) | HTML dos cards Google + Reclame Aqui |
