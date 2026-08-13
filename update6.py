import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]
for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # We will look for <h1 style="..."> and replace the style string.
    # Specifically, the style is currently:
    # style="font-size:clamp(34px,5.2vw,58px);font-weight:800;line-height:1.03;letter-spacing:-.02em;margin:22px 0 0;"
    
    pattern = r'style="font-size:clamp\(34px,5\.2vw,58px\);font-weight:800;line-height:1\.03;letter-spacing:-\.02em;margin:22px 0 0;"'
    replacement = 'style="font-size:clamp(22px,4vw,48px);font-weight:800;line-height:1.1;letter-spacing:-.02em;margin:22px 0 0;text-align:justify;text-wrap:balance;"'
    
    content = re.sub(pattern, replacement, content)
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
