import os

files_to_update = ['index.html', 'mededu.html', 'nnotes.html', 'nnotes-privacy.html']
cf_script = "    <!-- Cloudflare Web Analytics --><script type='module' src='https://static.cloudflareinsights.com/beacon.min.js' data-cf-beacon='{\"token\": \"1447bf27ee144931ae324db6be9a9942\"}'></script><!-- End Cloudflare Web Analytics -->\n</head>"

for file in files_to_update:
    if os.path.exists(file):
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if 'Cloudflare Web Analytics' not in content:
            new_content = content.replace('</head>', cf_script)
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f'Updated {file}')
