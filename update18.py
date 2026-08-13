import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

# The path to replace
old_path_pattern = r'C:\\[Uu]sers\\[^\\]+\\Desktop\\[^\\]+\\[^\\]+\\produt images\\'

# We want to replace it with './produtos/' and also make sure the filename uses forward slashes if there are any backslashes
for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # We will find all images that start with the old path and fix them
    # For a simple replace:
    # First, let's just do a string replace for the base path
    # Python raw string for exact match, but let's use regex to be safe about case and exact username
    def replace_path(match):
        return './produtos/'

    new_content = re.sub(old_path_pattern, replace_path, content, flags=re.IGNORECASE)
    
    # Also replace any stray backslashes inside the image property if needed, but since we replaced the base path, the filename should be just the file.
    
    if new_content != content:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)
