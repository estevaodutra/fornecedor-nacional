import os

html_files = [f for f in os.listdir('.') if f.endswith('.html')]
for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    old_html = '<div style="display:flex;align-items:center;gap:10px;flex-wrap:wrap;margin:22px 0 0;"><span style="font-size:11px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:#A7A7A7;">Venda nos marketplaces</span><span style="display: inline-flex; align-items: center; border: 1px solid rgba(238,77,45,.45); color: #FFFFFF; font-weight: 800; font-size: 13px; letter-spacing: .01em; padding: 7px 13px; border-radius: 8px; background-color: #ED4D2D">Shopee</span><span style="display:inline-flex;align-items:center;background:#FFE600;color:#2D3277;font-weight:800;font-size:13px;letter-spacing:.01em;padding:7px 13px;border-radius:8px;">Mercado Livre</span></div>'
    
    new_html = '<div style="display:flex;flex-direction:column;align-items:flex-start;gap:10px;margin:22px 0 0;"><span style="font-size:11px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:#A7A7A7;">Venda no automático em todos marketplaces</span><div style="display:flex;align-items:center;gap:10px;flex-wrap:wrap;"><span style="display: inline-flex; align-items: center; border: 1px solid rgba(238,77,45,.45); color: #FFFFFF; font-weight: 800; font-size: 13px; letter-spacing: .01em; padding: 7px 13px; border-radius: 8px; background-color: #ED4D2D">Shopee</span><span style="display:inline-flex;align-items:center;background:#FFE600;color:#2D3277;font-weight:800;font-size:13px;letter-spacing:.01em;padding:7px 13px;border-radius:8px;">Mercado Livre</span></div></div>'
    
    if old_html in content:
        content = content.replace(old_html, new_html)
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
