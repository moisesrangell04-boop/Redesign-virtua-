import os
import glob
import re

DIRECTORY = r"C:\Users\growt\OneDrive\Documentos\Virtua Corretora\redesign"

def fix_logos():
    html_files = glob.glob(os.path.join(DIRECTORY, "*.html"))
    py_files = glob.glob(os.path.join(DIRECTORY, "*.py"))
    
    bad_url = 'https://virtuacorretora.com.br/wp-content/uploads/2024/05/Logo-Virtua-1-1.png'
    good_url = 'https://www.virtuacorretora.com.br/wp-content/uploads/2023/11/cropped-virtua-corretora-de-planos-de-saude-1.webp'
    
    updated_files = 0
    
    for file in html_files + py_files:
        if file.endswith('fix_all_logos.py') or file.endswith('fix_logos_again.py') or file.endswith('update_missing_logos.py'):
            continue
            
        with open(file, "r", encoding="utf-8") as f:
            content = f.read()

        original_content = content
        
        # Replace the bad URL
        if bad_url in content:
            content = content.replace(bad_url, good_url)
        
        if content != original_content:
            with open(file, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Updated {os.path.basename(file)}")
            updated_files += 1
            
    print(f"Updated {updated_files} files.")

if __name__ == "__main__":
    fix_logos()
