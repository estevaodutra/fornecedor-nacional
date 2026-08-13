import os
import re

html_files = ['index.html', 'lp-full.html']
for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    pattern = r'<div style="display:flex;align-items:center;gap:10px;flex-wrap:wrap;margin:22px 0 0;"><span style="font-size:11px;font-weight:700;letter-spacing:\.12em;text-transform:uppercase;color:#A7A7A7;">Venda nos marketplaces</span>(.*?)</div>'
    
    replacement = r'<div style="display:flex;flex-direction:column;align-items:flex-start;gap:10px;margin:22px 0 0;"><span style="font-size:11px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:#A7A7A7;">Venda no automático em todos marketplaces</span><div style="display:flex;align-items:center;gap:10px;flex-wrap:wrap;">\1</div></div>'
    
    content = re.sub(pattern, replacement, content)
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
