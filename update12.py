import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]
for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Let's find the current video block
    pattern = r'<div style="position:relative;border:1px solid #2A2A2A;border-radius:18px;overflow:hidden;background:#000;box-shadow:0 30px 80px rgba\(0,0,0,\.6\);aspect-ratio:9/16;max-width:380px;margin:0 auto;cursor:pointer;" onclick=".*?">.*?</div>'
    
    replacement = '''<div style="position:relative;border:1px solid #2A2A2A;border-radius:18px;overflow:hidden;background:#000;box-shadow:0 30px 80px rgba(0,0,0,.6);aspect-ratio:9/16;max-width:380px;margin:0 auto;">
        <video id="vsl-video" src="./video1.mp4" autoplay muted loop playsinline style="width:100%;height:100%;object-fit:cover;cursor:pointer;" onclick="if(this.muted){this.muted=false;this.volume=1;document.getElementById('unmute-overlay').style.display='none';}else{this.paused?this.play():this.pause();}"></video>
        <div id="unmute-overlay" onclick="var v=document.getElementById('vsl-video');v.muted=false;v.volume=1;v.play();this.style.display='none';" style="position:absolute;inset:0;display:flex;align-items:flex-end;justify-content:flex-end;padding:20px;cursor:pointer;z-index:10;background:linear-gradient(0deg, rgba(0,0,0,0.3) 0%, transparent 30%);">
          <button style="background:rgba(0,0,0,0.6);color:#fff;border:1px solid rgba(255,255,255,0.2);padding:10px 16px;border-radius:999px;font-size:14px;font-weight:700;display:flex;align-items:center;gap:8px;pointer-events:none;">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon><line x1="23" y1="9" x2="17" y2="15"></line><line x1="17" y1="9" x2="23" y2="15"></line></svg>
            Toque para ouvir
          </button>
        </div>
      </div>'''
    
    if re.search(pattern, content, flags=re.DOTALL):
        content = re.sub(pattern, replacement, content, flags=re.DOTALL)
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
