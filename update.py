import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]
for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Replace Element 1
    content = re.sub(
        r'<span style="display: inline-flex; align-items: center; gap: 8px; font-size: 12px; font-weight: 700; letter-spacing: \.12em; color: #4FBE3F; border: 1px solid #2A2A2A; background: #151515; padding: 8px 14px; border-radius: 999px; text-transform: uppercase">\s*<span style="width:7px;height:7px;border-radius:50%;background:#16C784;display:inline-block;"></span>Para quem já tentou vender online\s*</span>',
        '<span style="display: inline-flex; align-items: center; font-size: 14px; font-weight: 700; color: #027A48; border: 1px solid #D1FADF; background: #ECFDF3; padding: 8px 16px; border-radius: 999px;">Para quem já tentou vender online</span>',
        content, flags=re.DOTALL
    )
    
    # Replace Element 2
    content = re.sub(
        r'<span style="display:inline-flex;align-items:center;gap:10px;background:#151515;border:1px solid #16C784;color:#16C784;font-weight:800;font-size:clamp\(15px,2vw,19px\);letter-spacing:\.04em;padding:12px 24px;border-radius:999px;">✓ ENVIO EM ATÉ 24H<span style="color:#16C784;">\*</span></span>',
        '<span style="display:inline-flex;align-items:center;gap:10px;background:#ECFDF3;border:1px solid #D1FADF;color:#027A48;font-weight:800;font-size:clamp(15px,2vw,19px);padding:12px 24px;border-radius:999px;">✓ ENVIO EM ATÉ 24H *</span>',
        content, flags=re.DOTALL
    )
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
