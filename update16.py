import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]
for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # We want to replace the placeholder div with an image tag wrapper
    pattern = r'<div style="width:100%;aspect-ratio:1/1;background:repeating-linear-gradient\(135deg,#ececea 0 10px,#f4f4f2 10px 20px\);display:flex;align-items:center;justify-content:center;">\s*<span style="font-family:ui-monospace,\'SF Mono\',Menlo,monospace;font-size:10px;color:#9a9a96;">\{\{\s*p\.tag\s*\}\}</span>\s*</div>'
    
    replacement = '''<div style="width:100%;aspect-ratio:1/1;position:relative;background:repeating-linear-gradient(135deg,#ececea 0 10px,#f4f4f2 10px 20px);display:flex;align-items:center;justify-content:center;overflow:hidden;">
            <sc-if value="{{ p.image }}">
              <img src="{{ p.image }}" style="width:100%;height:100%;object-fit:cover;position:absolute;inset:0;" alt="{{ p.name }}">
            </sc-if>
            <sc-if value="{{ !p.image }}">
              <span style="font-family:ui-monospace,'SF Mono',Menlo,monospace;font-size:10px;color:#9a9a96;">{{ p.tag }}</span>
            </sc-if>
          </div>'''
    
    if re.search(pattern, content):
        content = re.sub(pattern, replacement, content)
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
