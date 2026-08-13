import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Replace in lp-short.html (products array)
    if 'const products = [' in content:
        # We find the products array and keep only the first 6
        # A simple way is to match the first 6 object literals and drop the rest before ];
        pattern = r"(const products = \[\s*(?:\{[^}]+\},\s*){6})(?:\{[^}]+\},\s*)*(?=\s*\];)"
        content = re.sub(pattern, r"\1", content)
    
    # Replace in index.html and lp-full.html (catTags and catNames arrays)
    if 'const catTags = [' in content:
        # Reduce catTags to 6 elements
        pattern_tags = r"(const catTags = \['[^']+', '[^']+', '[^']+', '[^']+', '[^']+', '[^']+')([^\]]*)(\];)"
        content = re.sub(pattern_tags, r"\1\3", content)
        
        # Reduce catNames to 6 elements
        pattern_names = r"(const catNames = \['[^']+', '[^']+', '[^']+', '[^']+', '[^']+', '[^']+')([^\]]*)(\];)"
        content = re.sub(pattern_names, r"\1\3", content)
        
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
