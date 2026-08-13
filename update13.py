import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]
for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Match the current video block
    pattern = r'<div style="position:relative;border:1px solid #2A2A2A;border-radius:18px;overflow:hidden;background:#000;box-shadow:0 30px 80px rgba\(0,0,0,\.6\);aspect-ratio:9/16;max-width:380px;margin:0 auto;">.*?</button>\s*</div>\s*</div>'
    
    replacement = '''<div style="position:relative;border:1px solid #2A2A2A;border-radius:18px;overflow:hidden;background:#000;box-shadow:0 30px 80px rgba(0,0,0,.6);aspect-ratio:9/16;max-width:380px;margin:0 auto;">
        <video id="vsl-video" src="./video1.mp4" autoplay muted loop playsinline controls style="width:100%;height:100%;object-fit:cover;"></video>
      </div>'''
    
    if re.search(pattern, content, flags=re.DOTALL):
        content = re.sub(pattern, replacement, content, flags=re.DOTALL)
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
