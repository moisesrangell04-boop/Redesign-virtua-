import os
import glob
import re

DIRECTORY = r"C:\Users\growt\OneDrive\Documentos\Virtua Corretora\redesign"

def update_footer_logos():
    html_files = glob.glob(os.path.join(DIRECTORY, "*.html"))
    py_files = glob.glob(os.path.join(DIRECTORY, "*.py"))
    
    target_pattern = r'<div class="footer-logo">\s*<span class="logo-icon">V</span>\s*<span class="logo-text">virtua<small>CORRETORA DE SEGUROS</small></span>\s*</div>'
    replacement = '''<a href="index.html" class="footer-logo" style="text-decoration: none;">
                        <img src="https://www.virtuacorretora.com.br/wp-content/uploads/2023/11/cropped-virtua-corretora-de-planos-de-saude-1.webp" alt="Virtua Logo" style="height: 40px; width: auto; object-fit: contain;">
                    </a>'''

    # Ensure we catch variations where the a tag is used instead of div for the footer logo text (e.g. if we partially modified it)
    target_pattern_a = r'<a href="index\.html" class="footer-logo">\s*<span class="logo-icon">V</span>\s*<span class="logo-text">virtua<small>CORRETORA DE SEGUROS</small></span>\s*</a>'
                    
    updated_files = 0
    
    for file in html_files + py_files:
        if file.endswith('fix_footer_logos.py') or file.endswith('fix_all_logos.py') or file.endswith('fix_logos_again.py') or file.endswith('update_missing_logos.py'):
            continue
            
        with open(file, "r", encoding="utf-8") as f:
            content = f.read()

        original_content = content
        
        # Replace the text-based footer logo
        content = re.sub(target_pattern, replacement, content, flags=re.DOTALL)
        content = re.sub(target_pattern_a, replacement, content, flags=re.DOTALL)
        
        if content != original_content:
            with open(file, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Updated {os.path.basename(file)}")
            updated_files += 1
            
    print(f"Updated {updated_files} files.")

if __name__ == "__main__":
    update_footer_logos()
