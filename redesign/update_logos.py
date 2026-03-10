import os
import glob
import re

DIRECTORY = r"C:\Users\growt\OneDrive\Documentos\Virtua Corretora\redesign"
OLD_LOGO = 'src="https://www.virtuacorretora.com.br/wp-content/uploads/2023/11/cropped-virtua-corretora-de-planos-de-saude-1.webp"'
NEW_LOGO = 'src="https://virtuacorretora.com.br/wp-content/uploads/2024/05/Logo-Virtua-1-1.png"'
NEW_IMG_TAG = '<img src="https://virtuacorretora.com.br/wp-content/uploads/2024/05/Logo-Virtua-1-1.png" alt="Virtua Logo" style="height: 32px; width: auto; object-fit: contain;">'

def update_html_files():
    html_files = glob.glob(os.path.join(DIRECTORY, "*.html"))
    updated_count = 0
    for file in html_files:
        with open(file, "r", encoding="utf-8") as f:
            content = f.read()

        original_content = content

        # 1. Replace old URL with new URL
        if OLD_LOGO in content:
            content = content.replace(OLD_LOGO, NEW_LOGO)
            print(f"Replaced old logo URL in {os.path.basename(file)}")

        # 2. Add logo if missing entirely
        if 'Logo-Virtua-1-1.png' not in content and '<div class="logo-fallback">' in content:
            content = content.replace(
                '<div class="logo-fallback">',
                f'{NEW_IMG_TAG}\n                <div class="logo-fallback" style="display: flex;">'
            )
            print(f"Added new logo img tag to {os.path.basename(file)}")

        if content != original_content:
            with open(file, "w", encoding="utf-8") as f:
                f.write(content)
            updated_count += 1

    print(f"Updated {updated_count} HTML files.")

def update_generate_pages():
    script_path = os.path.join(DIRECTORY, "generate_pages.py")
    if not os.path.exists(script_path):
        return
    with open(script_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    original_content = content
    if 'Logo-Virtua-1-1.png' not in content and '<div class="logo-fallback">' in content:
        content = content.replace(
            '<div class="logo-fallback">',
            f'{NEW_IMG_TAG}\n                <div class="logo-fallback" style="display: flex;">'
        )
        print(f"Added new logo to generate_pages.py")

    if content != original_content:
        with open(script_path, "w", encoding="utf-8") as f:
            f.write(content)

if __name__ == "__main__":
    update_html_files()
    update_generate_pages()
