#!/usr/bin/env python3
"""Corrige labels de breadcrumb que ficaram sem espaço (por causa de <br> no H1)."""
import os, re, glob

def get_h1_fixed(html):
    m = re.search(r'<h1[^>]*>(.*?)</h1>', html, re.DOTALL)
    if m:
        inner = m.group(1)
        inner = re.sub(r'<br\s*/?>', ' ', inner, flags=re.IGNORECASE)
        return re.sub(r'<[^>]+>', '', inner).strip()
    return ''

def get_canonical(html):
    m = re.search(r'<link rel="canonical" href="([^"]+)"', html)
    return m.group(1) if m else ''

def fix_breadcrumb(filepath):
    slug = os.path.basename(os.path.dirname(filepath))
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    h1 = get_h1_fixed(html)
    canonical = get_canonical(html)
    if not h1:
        return False

    # Fix BreadcrumbList schema — replace "name": "..." for position 2
    old_schema = re.search(
        r'("position": 2,\s*"name": ")([^"]+)(")',
        html
    )
    if old_schema and old_schema.group(2) != h1:
        html = html.replace(
            old_schema.group(0),
            f'"position": 2,\n                "name": "{h1}"'
        )
        print(f"  ✓ Schema: '{old_schema.group(2)}' → '{h1}'")

    # Fix breadcrumb visual — replace aria-current="page" text
    html = re.sub(
        r'(aria-current="page"[^>]*>)[^<]*(</li>)',
        lambda m: f'{m.group(1)}{h1}{m.group(2)}',
        html
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    return True

base = os.path.dirname(os.path.abspath(__file__))
files = sorted(glob.glob(os.path.join(base, '*/index.html')))
for f in files:
    slug = os.path.basename(os.path.dirname(f))
    print(f"[{slug}]")
    fix_breadcrumb(f)

print("\n✅ Labels de breadcrumb corrigidos")
