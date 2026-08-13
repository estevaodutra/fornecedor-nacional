import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]
for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # We look for the exact video div string
    pattern = r'style="position:relative;border:1px solid #2A2A2A;border-radius:18px;overflow:hidden;background:#000;box-shadow:0 30px 80px rgba\(0,0,0,\.6\);aspect-ratio:16/9;"'
    replacement = r'style="position:relative;border:1px solid #2A2A2A;border-radius:18px;overflow:hidden;background:#000;box-shadow:0 30px 80px rgba(0,0,0,.6);aspect-ratio:9/16;max-width:380px;margin:0 auto;"'
    
    if re.search(pattern, content):
        content = re.sub(pattern, replacement, content)
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
