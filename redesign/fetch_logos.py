#!/usr/bin/env python3
"""Baixa logos reais das operadoras fazendo scraping dos sites oficiais."""

import os, re, urllib.request, urllib.parse, html

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOGOS_DIR = os.path.join(BASE_DIR, "assets", "logos")
os.makedirs(LOGOS_DIR, exist_ok=True)

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "pt-BR,pt;q=0.9",
}

OPERATOR_LOGOS = {
    "amil":           {"scrape": "https://www.amil.com.br"},
    "bradesco":       {"scrape": "https://www.bradescosaude.com.br"},
    "sulamerica":     {"scrape": "https://www.sulamerica.com.br"},
    "porto-seguro":   {"scrape": "https://www.portoseguro.com.br"},
    "unimed":         {"scrape": "https://www.unimed.coop.br"},
    "intermedica":    {"scrape": "https://www.gndi.com.br"},
    "hapvida":        {"scrape": "https://www.hapvida.com.br"},
    "prevent-senior": {"scrape": "https://www.preventsenior.com.br"},
    "caberj":         {"scrape": "https://www.caberj.com.br"},
    "samp":           {"scrape": "https://www.samp.com.br"},
}

# Fallback: favicon Google 256px (sempre funciona)
FAVICON = {
    "amil":           "https://www.google.com/s2/favicons?sz=256&domain=amil.com.br",
    "bradesco":       "https://www.google.com/s2/favicons?sz=256&domain=bradescosaude.com.br",
    "sulamerica":     "https://www.google.com/s2/favicons?sz=256&domain=sulamerica.com.br",
    "porto-seguro":   "https://www.google.com/s2/favicons?sz=256&domain=portoseguro.com.br",
    "unimed":         "https://www.google.com/s2/favicons?sz=256&domain=unimed.coop.br",
    "intermedica":    "https://www.google.com/s2/favicons?sz=256&domain=gndi.com.br",
    "hapvida":        "https://www.google.com/s2/favicons?sz=256&domain=hapvida.com.br",
    "prevent-senior": "https://www.google.com/s2/favicons?sz=256&domain=preventsenior.com.br",
    "caberj":         "https://www.google.com/s2/favicons?sz=256&domain=caberj.com.br",
    "samp":           "https://www.google.com/s2/favicons?sz=256&domain=samp.com.br",
}

def fetch_url(url, timeout=12):
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=timeout) as r:
            if r.status == 200:
                return r.read()
    except Exception:
        pass
    return None

def is_valid_image(data):
    if not data or len(data) < 200:
        return False
    if data[:8] == b'\x89PNG\r\n\x1a\n': return True
    if data[:3] == b'\xff\xd8\xff': return True
    if b'<svg' in data[:500] or b'<?xml' in data[:200]: return True
    if data[:6] in (b'GIF87a', b'GIF89a'): return True
    if data[:4] == b'RIFF' and data[8:12] == b'WEBP': return True
    return False

def extract_logo_urls(page_data, base_url):
    text = page_data.decode("utf-8", errors="ignore")
    candidates = []
    # og:image
    for m in re.finditer(r'property=["\']og:image["\'][^>]*content=["\']([^"\']+)["\']', text, re.I):
        candidates.append(m.group(1))
    for m in re.finditer(r'content=["\']([^"\']+)["\'][^>]*property=["\']og:image["\']', text, re.I):
        candidates.append(m.group(1))
    # <img> com logo no src/class/alt
    for m in re.finditer(r'<img[^>]+>', text, re.I):
        tag = m.group(0)
        if not re.search(r'logo', tag, re.I):
            continue
        src_m = re.search(r'src=["\']([^"\']+)["\']', tag, re.I)
        if src_m:
            src = src_m.group(1)
            if not re.search(r'favicon|sprite|1x1|pixel|tracking', src, re.I):
                candidates.append(src)
    # Resolve URLs
    resolved = []
    for url in candidates:
        url = html.unescape(url)
        if url.startswith("//"):
            url = "https:" + url
        elif url.startswith("/"):
            p = urllib.parse.urlparse(base_url)
            url = f"{p.scheme}://{p.netloc}{url}"
        elif not url.startswith("http"):
            url = urllib.parse.urljoin(base_url, url)
        if any(ext in url.lower() for ext in ['.png', '.svg', '.jpg', '.jpeg', '.webp', '.gif']):
            resolved.append(url)
    return resolved

def save(op_key, data, url):
    ext = "svg" if ".svg" in url.lower() else "png"
    dest = os.path.join(LOGOS_DIR, f"{op_key}.{ext}")
    with open(dest, "wb") as f:
        f.write(data)
    return dest, ext

def process(op_key, info):
    scrape_url = info.get("scrape")
    if scrape_url:
        page = fetch_url(scrape_url, timeout=15)
        if page:
            for url in extract_logo_urls(page, scrape_url):
                data = fetch_url(url)
                if data and is_valid_image(data):
                    dest, ext = save(op_key, data, url)
                    print(f"  ✅ {op_key} ({len(data)//1024}KB .{ext}) ← {url.split('/')[2]}")
                    return dest

    # Fallback favicon
    fav_url = FAVICON.get(op_key, "")
    if fav_url:
        data = fetch_url(fav_url)
        if data and is_valid_image(data):
            dest, _ = save(op_key, data, fav_url)
            print(f"  🔸 {op_key} ({len(data)}B favicon) ← Google")
            return dest

    print(f"  ❌ {op_key}")
    return None

def main():
    for op_key, info in OPERATOR_LOGOS.items():
        process(op_key, info)

if __name__ == "__main__":
    main()
