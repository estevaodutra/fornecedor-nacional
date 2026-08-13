import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]
for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Remove autoplay, muted, loop, but keep controls and playsinline
    pattern = r'<video id="vsl-video" src="\./video1\.mp4" autoplay muted loop playsinline controls style="width:100%;height:100%;object-fit:cover;"></video>'
    replacement = r'<video id="vsl-video" src="./video1.mp4" playsinline controls style="width:100%;height:100%;object-fit:cover;"></video>'
    
    if re.search(pattern, content):
        content = re.sub(pattern, replacement, content)
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
