import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]
for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    pattern = r'(<h1[^>]*>Já tentou vender sem estoque e travou\?</h1>)'
    replacement = r'\1\n      <img src="./comparativo.jpg" alt="Comparativo Sem Fornecedor vs Com Fornecedor" style="width:100%;max-width:800px;border-radius:12px;margin:24px 0;box-shadow:0 20px 40px rgba(0,0,0,0.5);display:block;">'
    
    content = re.sub(pattern, replacement, content)
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
