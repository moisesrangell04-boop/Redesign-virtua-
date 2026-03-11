import os
import glob
import re

DIRECTORY = r"C:\Users\growt\OneDrive\Documentos\Virtua Corretora\redesign"

def fix_logos():
    html_files = glob.glob(os.path.join(DIRECTORY, "*.html"))
    py_files = glob.glob(os.path.join(DIRECTORY, "*.py"))
    
    # 1. Fix Headers (different variations exist)
    # Variation 1: href="#"
    pattern1 = r'<a href="#" class="logo">.*?</a>'
    replacement1 = '''<a href="#" class="logo" style="text-decoration: none;">
                <img src="https://virtuacorretora.com.br/wp-content/uploads/2024/05/Logo-Virtua-1-1.png" alt="Virtua Logo" style="height: 40px; width: auto; object-fit: contain;">
            </a>'''
            
    # Variation 2: href="index.html"
    pattern2 = r'<a href="index\.html" class="logo">.*?</a>'
    replacement2 = '''<a href="index.html" class="logo" style="text-decoration: none;">
                <img src="https://virtuacorretora.com.br/wp-content/uploads/2024/05/Logo-Virtua-1-1.png" alt="Virtua Logo" style="height: 40px; width: auto; object-fit: contain;">
            </a>'''

    # Variation 3: <div class="footer-logo"> in index.html already fixed, but we should make sure
    pattern3 = r'<div class="footer-logo">\s*<span class="logo-icon">V</span>\s*<span class="logo-text">virtua<small>CORRETORA DE SEGUROS</small></span>\s*</div>'
    replacement3 = '''<a href="index.html" class="footer-logo" style="text-decoration: none;">
                        <img src="https://virtuacorretora.com.br/wp-content/uploads/2024/05/Logo-Virtua-1-1.png" alt="Virtua Logo" style="height: 40px; width: auto; object-fit: contain;">
                    </a>'''
                    
    updated_files = 0
    
    for file in html_files + py_files:
        if file.endswith('fix_all_logos.py') or file.endswith('update_missing_logos.py'):
            continue
            
        with open(file, "r", encoding="utf-8") as f:
            content = f.read()

        original_content = content
        
        # Replace header logos using dotall to match across newlines
        content = re.sub(pattern1, replacement1, content, flags=re.DOTALL)
        content = re.sub(pattern2, replacement2, content, flags=re.DOTALL)
        content = re.sub(pattern3, replacement3, content, flags=re.DOTALL)
        
        if content != original_content:
            with open(file, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Updated {os.path.basename(file)}")
            updated_files += 1
            
    print(f"Updated {updated_files} files.")

if __name__ == "__main__":
    fix_logos()
