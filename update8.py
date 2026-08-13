import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]
for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # We want to replace the whole VSL placeholder div with our video div.
    # The div starts with: <div style="position:relative;border:1px solid #2A2A2A;border-radius:18px;overflow:hidden;background:#000;box-shadow:0 30px 80px rgba(0,0,0,.6);">
    # And ends before: <div style="margin:22px 0 0;text-align:center;">
    
    pattern = r'<div style="position:relative;border:1px solid #2A2A2A;border-radius:18px;overflow:hidden;background:#000;box-shadow:0 30px 80px rgba\(0,0,0,\.6\);">.*?</div>\s*</div>\s*(<div style="margin:22px 0 0;text-align:center;">)'
    
    replacement = r'''<div style="position:relative;border:1px solid #2A2A2A;border-radius:18px;overflow:hidden;background:#000;box-shadow:0 30px 80px rgba(0,0,0,.6);aspect-ratio:16/9;">
        <video id="vsl-video" src="./video1.mp4" autoplay muted loop playsinline style="width:100%;height:100%;object-fit:cover;"></video>
        <button id="unmute-btn" onclick="document.getElementById('vsl-video').muted = false; document.getElementById('vsl-video').volume = 1; this.style.display='none';" style="position:absolute;bottom:20px;right:20px;background:rgba(0,0,0,0.6);color:#fff;border:1px solid rgba(255,255,255,0.2);padding:10px 16px;border-radius:999px;font-size:14px;font-weight:700;cursor:pointer;display:flex;align-items:center;gap:8px;z-index:10;transition: background 0.2s;" onmouseover="this.style.background='rgba(0,0,0,0.8)'" onmouseout="this.style.background='rgba(0,0,0,0.6)'">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon><line x1="23" y1="9" x2="17" y2="15"></line><line x1="17" y1="9" x2="23" y2="15"></line></svg>
          Toque para ouvir
        </button>
      </div>
      \1'''
    
    if re.search(pattern, content, flags=re.DOTALL):
        content = re.sub(pattern, replacement, content, flags=re.DOTALL)
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
