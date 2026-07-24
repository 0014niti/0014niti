import os
import re

def inject_seo(filepath, title, desc, keywords, canonical, json_ld=""):
    if not os.path.exists(filepath): return
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Update title
    content = re.sub(r'<title>.*?</title>', f'<title>{title}</title>', content)
    
    # Remove existing description and keywords to avoid duplicates
    content = re.sub(r'<meta name="description" content=".*?">\n?', '', content)
    content = re.sub(r'<meta name="keywords" content=".*?">\n?', '', content)
    
    seo_tags = f"""
    <!-- SEO Meta Tags -->
    <meta name="description" content="{desc}">
    <meta name="keywords" content="{keywords}">
    <link rel="canonical" href="{canonical}">
"""
    if json_ld:
        seo_tags += f"""
    <!-- JSON-LD Structured Data -->
    <script type="application/ld+json">
    {json_ld}
    </script>
"""
    
    content = content.replace('</head>', seo_tags + '</head>')
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

# Index.html
inject_seo(
    'index.html',
    'Dr.N | General Practitioner & Software Developer Portfolio',
    'Portfolio of Dr.N - A General Practitioner (GP) and tech enthusiast bridging the gap between clinical medicine and software engineering.',
    'medical doctor developer, general practitioner software, GP coding, clinical medicine tech, healthcare software, Dr.N portfolio, medical UI designer',
    'https://drnitz.github.io/',
    '''{
      "@context": "https://schema.org",
      "@type": "Person",
      "name": "Dr.N",
      "url": "https://drnitz.github.io/",
      "jobTitle": [
        "General Practitioner",
        "Software Developer"
      ],
      "sameAs": [
        "https://github.com/drnitz"
      ]
    }'''
)

# mededu.html
inject_seo(
    'mededu.html',
    'Clinical MedEdu by Dr.N | Free Medical Notes for GPs',
    'Bridging the knowledge gap with free, unified clinical notes and video breakdowns on diseases designed for General Practitioners, medical students, and patients.',
    'free clinical medical notes, GP study resources, pathophysiology lectures, open clinic initiative, Dr.N MedEdu, medical education',
    'https://drnitz.github.io/mededu.html'
)

# nnotes.html
inject_seo(
    'nnotes.html',
    'Nnotes App | Infinite Canvas & Auto-Beautify Note-Taking',
    'The ultimate Android handwriting app by Dr.N. Infinite canvas, Auto-Beautify handwriting to text, 3D companions, and a beautiful Claymorphism UI.',
    'android handwriting app, infinite canvas notes, auto-beautify handwriting, kotlin jetpack compose note app, Nnotes, student planner app',
    'https://drnitz.github.io/nnotes.html',
    '''{
      "@context": "https://schema.org",
      "@type": "SoftwareApplication",
      "name": "Nnotes",
      "operatingSystem": "Android",
      "applicationCategory": "ProductivityApplication",
      "offers": {
        "@type": "Offer",
        "price": "0",
        "priceCurrency": "USD"
      },
      "description": "Infinite canvas handwriting app with Auto-Beautify."
    }'''
)

# nnotes-privacy.html
inject_seo(
    'nnotes-privacy.html',
    'Privacy Policy | Nnotes App',
    'Official Privacy Policy and Terms of Service for the Nnotes Android application. Transparent, local-first data storage policies.',
    'nnotes privacy policy, nnotes terms of service',
    'https://drnitz.github.io/nnotes-privacy.html'
)
print("SEO optimization injected.")
