#!/usr/bin/env python3
"""
Script para baixar logos reais das operadoras e substituir nos HTMLs.
Mantém o mesmo estilo CSS que a Bradesco (padrão correto).
"""
import urllib.request
import base64
import os
import re
import ssl

# Desabilitar verificação SSL para downloads
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# URLs das logos reais das operadoras
LOGO_URLS = {
    # Unimed
    "unimed": "https://logodownload.org/wp-content/uploads/2014/06/unimed-logo-0.png",
    # SulAmérica
    "sulamerica": "https://logodownload.org/wp-content/uploads/2014/12/sulamerica-logo.png",
    # Hapvida
    "hapvida": "https://logodownload.org/wp-content/uploads/2021/06/hapvida-logo-0.png",
    # Intermédica / NotreDame
    "intermedica": "https://logodownload.org/wp-content/uploads/2021/02/notredame-intermedica-logo-0.png",
    # Prevent Senior
    "prevent_senior": "https://logodownload.org/wp-content/uploads/2020/10/prevent-senior-logo.png",
    # Porto Seguro
    "porto_seguro": "https://logodownload.org/wp-content/uploads/2014/05/porto-seguro-logo-0.png",
    # SAMP
    "samp": "https://logodownload.org/wp-content/uploads/2020/03/samp-logo-0.png",
    # Caberj / Integral Saúde - tentativas alternativas
    "caberj": "https://www.integralsaude.com.br/favicon.ico",
    # Amil  
    "amil": "https://logodownload.org/wp-content/uploads/2014/05/amil-logo-0.png",
}

# Mapeamento: nome da operadora -> diretórios que usam essa logo
OPERATOR_DIRS = {
    "unimed": [
        "plano-de-saude-unimed",
        "plano-de-saude-unimed-campos",
        "plano-saude-unimed-macae",
    ],
    "sulamerica": [
        "plano-de-saude-sulamerica",
        "plano-de-saude-sulamerica-direto-brasilia",
        "plano-de-saude-sulamerica-direto-salvador", 
        "plano-de-saude-sulamerica-direto-sampa",
        "plano-de-saude-sulamerica-recife",
        "plano-de-saude-bh-sulamerica-saude-direto",
        "plano-de-saude-joao-pessoa-sulamerica",
    ],
    "hapvida": [
        "plano-de-saude-hapvida",
        "plano-de-saude-hapvida-brasilia",
        "plano-de-saude-hapvida-manaus",
        "plano-de-saude-hapvida-recife",
        "plano-de-saude-hapvida-salvador",
    ],
    "intermedica": [
        "plano-de-saude-intermedica",
    ],
    "prevent_senior": [
        "plano-de-saude-prevent-senior",
    ],
    "porto_seguro": [
        "plano-de-saude-porto-seguro-saude",
    ],
    "samp": [
        "plano-de-saude-samp-es",
    ],
    "caberj": [
        "plano-de-saude-caberj-integral-saude",
    ],
    "amil": [
        "plano-de-saude-amil",
    ],
}


def download_logo(url, operator_name):
    """Baixa a logo e retorna em base64."""
    try:
        req = urllib.request.Request(url, headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
        })
        response = urllib.request.urlopen(req, context=ctx, timeout=15)
        data = response.read()
        content_type = response.headers.get('Content-Type', 'image/png')
        
        if 'svg' in content_type or url.endswith('.svg'):
            mime = 'image/svg+xml'
        elif 'png' in content_type or url.endswith('.png'):
            mime = 'image/png'
        elif 'jpeg' in content_type or 'jpg' in content_type:
            mime = 'image/jpeg'
        elif 'webp' in content_type or url.endswith('.webp'):
            mime = 'image/webp'
        elif 'ico' in content_type or url.endswith('.ico'):
            mime = 'image/x-icon'
        else:
            mime = 'image/png'
        
        b64 = base64.b64encode(data).decode('utf-8')
        data_uri = f"data:{mime};base64,{b64}"
        print(f"  ✅ Baixado {operator_name}: {len(data)} bytes ({mime})")
        return data_uri
    except Exception as e:
        print(f"  ❌ Erro ao baixar {operator_name} de {url}: {e}")
        return None


def update_html_logo(html_path, new_src):
    """Substitui a src da logo no HTML mantendo o mesmo estilo."""
    if not os.path.exists(html_path):
        print(f"  ⚠️  Arquivo não encontrado: {html_path}")
        return False
    
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Padrão para encontrar a div op-hero-logo com a img dentro
    # Captura: <div class="op-hero-logo" style="margin-bottom:28px;"><img src="QUALQUER_COISA" alt="..."  style="...">
    pattern = r'(<div class="op-hero-logo"[^>]*>)\s*<img\s+src="[^"]*"\s+alt="([^"]*)"\s+style="([^"]*)">'
    
    match = re.search(pattern, content)
    if match:
        div_tag = match.group(1)
        alt_text = match.group(2)
        # Usar o mesmo estilo da Bradesco
        style = 'height:72px;max-width:220px;width:auto;border-radius:16px;box-shadow:0 6px 24px rgba(0,0,0,0.22);background:white;padding:12px 20px;object-fit:contain;'
        
        new_tag = f'{div_tag}<img src="{new_src}" alt="{alt_text}" style="{style}">'
        new_content = content[:match.start()] + new_tag + content[match.end():]
        
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"  ✅ Atualizado: {html_path}")
        return True
    else:
        print(f"  ⚠️  Padrão de logo não encontrado em: {html_path}")
        return False


def main():
    print("=" * 60)
    print("🔄 Atualizando logos das operadoras")
    print("=" * 60)
    
    # Passo 1: Baixar todas as logos
    logos_b64 = {}
    for name, url in LOGO_URLS.items():
        print(f"\n📥 Baixando logo: {name}")
        result = download_logo(url, name)
        if result:
            logos_b64[name] = result
    
    print(f"\n{'=' * 60}")
    print(f"📊 Logos baixadas: {len(logos_b64)}/{len(LOGO_URLS)}")
    print(f"{'=' * 60}")
    
    # Passo 2: Atualizar os HTMLs
    updated = 0
    failed = 0
    skipped = 0
    
    for operator, dirs in OPERATOR_DIRS.items():
        if operator not in logos_b64:
            print(f"\n⏭️  Pulando {operator} (logo não disponível)")
            skipped += len(dirs)
            continue
        
        print(f"\n🔧 Atualizando {operator} ({len(dirs)} página(s)):")
        for d in dirs:
            html_path = os.path.join(BASE_DIR, d, "index.html")
            if update_html_logo(html_path, logos_b64[operator]):
                updated += 1
            else:
                failed += 1
    
    print(f"\n{'=' * 60}")
    print(f"📊 Resultado final:")
    print(f"  ✅ Atualizados: {updated}")
    print(f"  ❌ Falhas: {failed}")
    print(f"  ⏭️  Pulados: {skipped}")
    print(f"{'=' * 60}")


if __name__ == '__main__':
    main()
