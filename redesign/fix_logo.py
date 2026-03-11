"""
Fix all logos: add the "virtua CORRETORA DE SEGUROS" text back next to the image.
The webp image is only the shield icon, so we need the text beside it.
"""
import os, glob, re

DIRECTORY = r"C:\Users\growt\OneDrive\Documentos\Virtua Corretora\redesign"
LOGO_URL = "https://www.virtuacorretora.com.br/wp-content/uploads/2023/11/cropped-virtua-corretora-de-planos-de-saude-1.webp"

# The desired header logo block (image + text, NO logo-icon "V" since the image replaces it)
HEADER_LOGO_REPLACEMENT = '''<img src="{url}" alt="Virtua Logo" style="height: 32px; width: auto; object-fit: contain;">
                <span class="logo-text">virtua<small>CORRETORA DE SEGUROS</small></span>'''.format(url=LOGO_URL)

# For index.html header (href="#")
HEADER_LOGO_REPLACEMENT_HASH = '''<img src="{url}"
                    alt="Virtua Logo" style="height: 32px; width: auto; object-fit: contain;">
                <span class="logo-text">virtua<small>CORRETORA DE SEGUROS</small></span>'''.format(url=LOGO_URL)

# The desired footer logo block
FOOTER_LOGO_REPLACEMENT = '''<a href="index.html" class="footer-logo" style="text-decoration: none;">
                        <img src="{url}" alt="Virtua Logo" style="height: 40px; width: auto; object-fit: contain;">
                        <span class="logo-text">virtua<small>CORRETORA DE SEGUROS</small></span>
                    </a>'''.format(url=LOGO_URL)

def fix_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    original = content

    # ---- FIX HEADER LOGOS ----
    # Current state: <a href="..." class="logo">
    #                    <img src="..." ...>
    #                </a>
    # We need to add the logo-text span after the img, inside the <a>

    # Pattern for subpages (href="index.html")
    pattern_sub = (
        r'(<a\s+href="index\.html"\s+class="logo"[^>]*>)\s*'
        r'<img\s+src="[^"]*"[^/]*/?>\s*'
        r'(</a>)'
    )
    def repl_sub(m):
        return m.group(1) + '\n                ' + HEADER_LOGO_REPLACEMENT + '\n            ' + m.group(2)
    content = re.sub(pattern_sub, repl_sub, content, flags=re.DOTALL)

    # Pattern for index.html (href="#")
    pattern_index = (
        r'(<a\s+href="#"\s+class="logo"[^>]*>)\s*'
        r'<img\s+src="[^"]*"[^/]*/?>\s*'
        r'(</a>)'
    )
    def repl_index(m):
        return m.group(1) + '\n                ' + HEADER_LOGO_REPLACEMENT_HASH + '\n            ' + m.group(2)
    content = re.sub(pattern_index, repl_index, content, flags=re.DOTALL)

    # ---- FIX FOOTER LOGO (index.html) ----
    # Current: <a href="index.html" class="footer-logo" ...><img ...></a>
    # Need to add text span
    pattern_footer = (
        r'<a\s+href="index\.html"\s+class="footer-logo"[^>]*>\s*'
        r'<img\s+src="[^"]*"[^/]*/?>\s*'
        r'</a>'
    )
    content = re.sub(pattern_footer, FOOTER_LOGO_REPLACEMENT, content, flags=re.DOTALL)

    if content != original:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        return True
    return False

def fix_generate_pages():
    filepath = os.path.join(DIRECTORY, "generate_pages.py")
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    original = content

    # Same pattern for subpages
    pattern = (
        r'(<a\s+href="index\.html"\s+class="logo"[^>]*>)\s*'
        r'<img\s+src="[^"]*"[^/]*/?>\s*'
        r'(</a>)'
    )
    def repl(m):
        return m.group(1) + '\n                ' + HEADER_LOGO_REPLACEMENT + '\n            ' + m.group(2)
    content = re.sub(pattern, repl, content, flags=re.DOTALL)

    if content != original:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  Fixed: generate_pages.py")
        return True
    return False

if __name__ == "__main__":
    html_files = sorted(glob.glob(os.path.join(DIRECTORY, "*.html")))
    updated = 0
    for f in html_files:
        if fix_file(f):
            print(f"  Fixed: {os.path.basename(f)}")
            updated += 1
    if fix_generate_pages():
        updated += 1
    print(f"\nTotal files updated: {updated}")
