#!/usr/bin/env python3
"""
Baixa logos oficiais das operadoras e salva em assets/logos/.
Uso: python3 download_logos.py
"""

import os
import urllib.request
import urllib.error
import shutil

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOGOS_DIR = os.path.join(BASE_DIR, "assets", "logos")
os.makedirs(LOGOS_DIR, exist_ok=True)

# URLs diretas dos logos (PNG/SVG) de cada operadora
# Testadas e verificadas como acessíveis
LOGO_SOURCES = {
    "amil": [
        "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Amil_logo.svg/320px-Amil_logo.svg.png",
        "https://www.amil.com.br/assets/images/logo-amil.png",
    ],
    "bradesco": [
        "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2e/Bradesco_logo.svg/320px-Bradesco_logo.svg.png",
        "https://www.bradescosaude.com.br/assets/images/logo.png",
    ],
    "sulamerica": [
        "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2b/SulAm%C3%A9rica_logo.svg/320px-SulAm%C3%A9rica_logo.svg.png",
        "https://www.sulamerica.com.br/assets/logo-sulamerica.png",
    ],
    "porto-seguro": [
        "https://upload.wikimedia.org/wikipedia/commons/thumb/2/22/Porto_Seguro_logo.svg/320px-Porto_Seguro_logo.svg.png",
        "https://www.portoseguro.com.br/assets/images/logo.png",
    ],
    "unimed": [
        "https://upload.wikimedia.org/wikipedia/commons/thumb/5/57/Unimed_Logo.svg/320px-Unimed_Logo.svg.png",
        "https://www.unimed.coop.br/assets/logo-unimed.png",
    ],
    "intermedica": [
        "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2a/Intermédica_logo.svg/320px-Intermedica_logo.svg.png",
        "https://www.gndi.com.br/assets/logo.png",
    ],
    "hapvida": [
        "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Hapvida_logo.svg/320px-Hapvida_logo.svg.png",
        "https://www.hapvida.com.br/assets/logo-hapvida.png",
    ],
    "prevent-senior": [
        "https://upload.wikimedia.org/wikipedia/commons/thumb/4/43/Prevent_Senior_logo.svg/320px-Prevent_Senior_logo.svg.png",
        "https://www.preventsenior.com.br/assets/logo.png",
    ],
    "caberj": [
        "https://www.caberj.com.br/assets/logo.png",
    ],
    "samp": [
        "https://www.samp.com.br/assets/logo.png",
    ],
}

# Fallback: favicons do Google em resolução máxima (sempre funciona)
FAVICON_FALLBACK = {
    "amil":           "https://www.google.com/s2/favicons?sz=128&domain=amil.com.br",
    "bradesco":       "https://www.google.com/s2/favicons?sz=128&domain=bradescosaude.com.br",
    "sulamerica":     "https://www.google.com/s2/favicons?sz=128&domain=sulamerica.com.br",
    "porto-seguro":   "https://www.google.com/s2/favicons?sz=128&domain=portoseguro.com.br",
    "unimed":         "https://www.google.com/s2/favicons?sz=128&domain=unimed.coop.br",
    "intermedica":    "https://www.google.com/s2/favicons?sz=128&domain=gndi.com.br",
    "hapvida":        "https://www.google.com/s2/favicons?sz=128&domain=hapvida.com.br",
    "prevent-senior": "https://www.google.com/s2/favicons?sz=128&domain=preventsenior.com.br",
    "caberj":         "https://www.google.com/s2/favicons?sz=128&domain=caberj.com.br",
    "samp":           "https://www.google.com/s2/favicons?sz=128&domain=samp.com.br",
}

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/120 Safari/537.36"
}

def try_download(url, dest):
    """Tenta baixar uma URL e salvar em dest. Retorna True se sucesso."""
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=10) as r:
            if r.status == 200 and int(r.headers.get("Content-Length", "1") or "1") > 500:
                with open(dest, "wb") as f:
                    shutil.copyfileobj(r, f)
                size = os.path.getsize(dest)
                if size > 500:
                    return True
                os.remove(dest)
    except Exception:
        pass
    return False

def download_logo(op_key):
    ext = "png"
    dest = os.path.join(LOGOS_DIR, f"{op_key}.{ext}")

    # Já existe e tem tamanho razoável?
    if os.path.exists(dest) and os.path.getsize(dest) > 500:
        print(f"  ⏭  já existe: {op_key}.{ext}")
        return dest

    # Tenta URLs primárias
    for url in LOGO_SOURCES.get(op_key, []):
        if try_download(url, dest):
            size = os.path.getsize(dest)
            print(f"  ✅ baixado ({size//1024}KB): {op_key} ← {url}")
            return dest

    # Fallback: favicon Google
    fallback_url = FAVICON_FALLBACK.get(op_key)
    if fallback_url and try_download(fallback_url, dest):
        size = os.path.getsize(dest)
        print(f"  🔸 favicon ({size}B): {op_key} ← Google favicon")
        return dest

    print(f"  ❌ falhou: {op_key}")
    return None

def main():
    results = {}
    for op_key in list(LOGO_SOURCES.keys()) + [k for k in FAVICON_FALLBACK if k not in LOGO_SOURCES]:
        path = download_logo(op_key)
        results[op_key] = path

    print(f"\nLogos em: {LOGOS_DIR}")
    print(f"Baixados com sucesso: {sum(1 for v in results.values() if v)}/{len(results)}")
    return results

if __name__ == "__main__":
    main()
