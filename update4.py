import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]
for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    pattern = r'<div style="display:grid;grid-template-columns:repeat\(2,1fr\);gap:12px;margin:20px 0 0;max-width:520px;">\s*<div style="border:1px solid #2A2A2A;background:#151515;border-radius:12px;padding:14px 16px;"><div style="font-size:clamp\(18px,2\.4vw,22px\);font-weight:800;color:#fff;">\+150 produtos</div></div>\s*<div style="border:1px solid #2A2A2A;background:#151515;border-radius:12px;padding:14px 16px;"><div style="font-size:clamp\(18px,2\.4vw,22px\);font-weight:800;color:#fff;">Sem estoque próprio</div></div>\s*<div style="border:1px solid #2A2A2A;background:#151515;border-radius:12px;padding:14px 16px;"><div style="font-size:clamp\(18px,2\.4vw,22px\);font-weight:800;color:#fff;">Fornecedor no Brasil</div></div>\s*<div style="border:1px solid #2A2A2A;background:#151515;border-radius:12px;padding:14px 16px;"><div style="font-size:clamp\(18px,2\.4vw,22px\);font-weight:800;color:#fff;">Envio em até 24h<span style="color:#16C784;">\*</span></div></div>\s*</div>'
    
    content = re.sub(pattern, '', content, flags=re.DOTALL)
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
