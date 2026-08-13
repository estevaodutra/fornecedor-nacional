import re

with open('lp-short.html', 'r', encoding='utf-8') as file:
    content = file.read()

pattern = r'<div style="position:relative;border:1px solid #2A2A2A;border-radius:18px;overflow:hidden;background:#000;box-shadow:0 30px 80px rgba\(0,0,0,\.6\);">\s*<div style="position:relative;width:100%;aspect-ratio:16/9;background:repeating-linear-gradient\(135deg,#141414 0 14px,#101010 14px 28px\);display:flex;align-items:center;justify-content:center;">\s*<div style="display:flex;flex-direction:column;align-items:center;gap:14px;">\s*<div style="width: 76px; height: 76px; border-radius: 50%; display: flex; align-items: center; justify-content: center; animation: fnPulse 2\.4s ease-out infinite; background-color: #4CB73D">\s*<span style="display:block;border-style:solid;border-width:15px 0 15px 24px;border-color:transparent transparent transparent #07110D;margin-left:6px;"></span>\s*</div>\s*<span style="font-family:ui-monospace,\'SF Mono\',Menlo,monospace;font-size:12px;color:#A7A7A7;letter-spacing:\.04em;">VSL — cole o embed do seu vídeo aqui</span>\s*</div>\s*</div>\s*</div>'

replacement = '''<div style="position:relative;border:1px solid #2A2A2A;border-radius:18px;overflow:hidden;background:#000;box-shadow:0 30px 80px rgba(0,0,0,.6);aspect-ratio:16/9;">
        <video id="vsl-video" src="./video1.mp4" autoplay muted loop playsinline style="width:100%;height:100%;object-fit:cover;"></video>
        <button id="unmute-btn" onclick="document.getElementById('vsl-video').muted = false; document.getElementById('vsl-video').volume = 1; this.style.display='none';" style="position:absolute;bottom:20px;right:20px;background:rgba(0,0,0,0.6);color:#fff;border:1px solid rgba(255,255,255,0.2);padding:10px 16px;border-radius:999px;font-size:14px;font-weight:700;cursor:pointer;display:flex;align-items:center;gap:8px;z-index:10;transition: background 0.2s;" onmouseover="this.style.background='rgba(0,0,0,0.8)'" onmouseout="this.style.background='rgba(0,0,0,0.6)'">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon><line x1="23" y1="9" x2="17" y2="15"></line><line x1="17" y1="9" x2="23" y2="15"></line></svg>
          Toque para ouvir
        </button>
      </div>'''

content = re.sub(pattern, replacement, content)
with open('lp-short.html', 'w', encoding='utf-8') as file:
    file.write(content)
