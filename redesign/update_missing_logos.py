import os
import glob
import re

DIRECTORY = r"C:\Users\growt\OneDrive\Documentos\Virtua Corretora\redesign"

def update_missing():
    html_files = glob.glob(os.path.join(DIRECTORY, "*.html"))
    updated_count = 0
    
    target_pattern = r'<a href="index\.html" class="logo">\s*<span class="logo-icon">V</span>\s*<span class="logo-text">virtua<small>CORRETORA DE SEGUROS</small></span>\s*</a>'
    replacement = '''<a href="index.html" class="logo">
                <img src="https://virtuacorretora.com.br/wp-content/uploads/2024/05/Logo-Virtua-1-1.png" alt="Virtua Logo" style="height: 32px; width: auto; object-fit: contain;">
                <div class="logo-fallback" style="display: flex;">
                    <span class="logo-icon">V</span>
                    <span class="logo-text">virtua<small>CORRETORA DE SEGUROS</small></span>
                </div>
            </a>'''
            
    for file in html_files:
        with open(file, "r", encoding="utf-8") as f:
            content = f.read()

        original_content = content
        
        if 'Logo-Virtua-1-1.png' not in content:
            content = re.sub(target_pattern, replacement, content)
            
        if content != original_content:
            with open(file, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Updated missing logos in {os.path.basename(file)}")
            updated_count += 1
            
    print(f"Updated {updated_count} files.")

if __name__ == "__main__":
    update_missing()
