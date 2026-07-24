import os
import shutil
import re

source_img = r"C:\Users\harsh\.gemini\antigravity-ide\brain\143518b1-cd6b-4c39-9cc0-c454ac4deac4\social_preview_1784906645429.png"
dest_img = r"c:\Users\harsh\Downloads\0014niti\social_preview.png"
if os.path.exists(source_img):
    shutil.copy2(source_img, dest_img)

files_to_update = ['index.html', 'mededu.html', 'nnotes.html', 'nnotes-privacy.html']

og_tags = """    <!-- Open Graph / Social Sharing -->
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://drnitz.github.io/">
    <meta property="og:title" content="Dr.N | Medicine &amp; Code">
    <meta property="og:description" content="Bridging the gap between clinical medicine and software engineering.">
    <meta property="og:image" content="https://drnitz.github.io/social_preview.png">
    
    <!-- Twitter -->
    <meta property="twitter:card" content="summary_large_image">
    <meta property="twitter:url" content="https://drnitz.github.io/">
    <meta property="twitter:title" content="Dr.N | Medicine &amp; Code">
    <meta property="twitter:description" content="Bridging the gap between clinical medicine and software engineering.">
    <meta property="twitter:image" content="https://drnitz.github.io/social_preview.png">"""

for file in files_to_update:
    if os.path.exists(file):
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Remove old og: tags
        content = re.sub(r'<meta property="og:.*?">\n?', '', content)
        
        if 'twitter:card' not in content:
            new_content = content.replace('</head>', og_tags + '\n</head>')
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f'Updated {file}')
