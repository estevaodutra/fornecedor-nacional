import os
import re

head_snippet = """<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-M6PMJ6FM');</script>
<!-- End Google Tag Manager -->
"""

body_snippet = """<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-M6PMJ6FM"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->
"""

html_files = [f for f in os.listdir('.') if f.endswith('.html')]
for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Avoid duplicate insertion
    if 'GTM-M6PMJ6FM' not in content:
        content = content.replace('</head>', head_snippet + '</head>')
        content = re.sub(r'(<body[^>]*>)', r'\1\n' + body_snippet, content, count=1)
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
