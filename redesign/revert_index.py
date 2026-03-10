import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace product blocks
html = re.sub(
    r'<div style=\"display: flex; gap: 12px; align-items: center; margin-top: auto;\">\s*<a href=\"(.*?\.html)\" target=\"_blank\" class=\"product-link\">Saiba mais →</a>\s*<button class=\"btn btn-primary open-quote-modal\".*?>Cotar Agora</button>\s*</div>',
    r'<a href="\1" target="_blank" class="product-link">Saiba mais →</a>',
    html
)

# Replace business blocks
html = re.sub(
    r'<div style=\"display: flex; gap: 12px; align-items: center; margin-top: auto;\">\s*<a href=\"(.*?\.html)\" target=\"_blank\" class=\"business-link\">Saiba mais →</a>\s*<button class=\"btn btn-primary open-quote-modal\".*?>Cotar Agora</button>\s*</div>',
    r'<a href="\1" target="_blank" class="business-link">Saiba mais →</a>',
    html
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
