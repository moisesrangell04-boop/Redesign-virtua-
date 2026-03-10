import os
import glob
import re

DIRECTORY = r"C:\Users\growt\OneDrive\Documentos\Virtua Corretora\redesign"
OLD_LOGO = 'https://virtuacorretora.com.br/wp-content/uploads/2024/05/Logo-Virtua-1-1.png'
NEW_LOGO = 'https://www.virtuacorretora.com.br/wp-content/uploads/2023/11/cropped-virtua-corretora-de-planos-de-saude-1.webp'

def update_html_files():
    html_files = glob.glob(os.path.join(DIRECTORY, "*.html"))
    updated_count = 0
    for file in html_files:
        with open(file, "r", encoding="utf-8") as f:
            content = f.read()

        original_content = content
        
        if OLD_LOGO in content:
            content = content.replace(OLD_LOGO, NEW_LOGO)
            print(f"Replaced broken logo URL in {os.path.basename(file)}")

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
    if OLD_LOGO in content:
        content = content.replace(OLD_LOGO, NEW_LOGO)
        print(f"Replaced broken logo in generate_pages.py")

    if content != original_content:
        with open(script_path, "w", encoding="utf-8") as f:
            f.write(content)

if __name__ == "__main__":
    update_html_files()
    update_generate_pages()
