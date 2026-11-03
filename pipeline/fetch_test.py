import urllib.request
import re

urls_to_test = [
    'https://www.theguardian.com/theguardian/2026/nov/03/all',
    'https://www.theguardian.com/theguardian/2026/nov/04/all',
    'https://www.theguardian.com/world/2026/nov/03/all',
    'https://www.theguardian.com/science/2026/nov/03/all',
    'https://www.theguardian.com/uk-news/2026/nov/03/all'
]

headers = {'User-Agent': 'Mozilla/5.0'}
for u in urls_to_test:
    try:
        req = urllib.request.Request(u, headers=headers)
        with urllib.request.urlopen(req, timeout=5) as res:
            print(f'{u} -> {res.status}')
            html = res.read().decode('utf-8', errors='ignore')
            links = set(re.findall(r'href="(https://www.theguardian.com/[a-z0-9\-]+/\d{4}/[a-z]{3}/\d{2}/[^"#]+)"', html))
            print(f'Found {len(links)} dated links.')
            for l in sorted(links)[:5]:
                print('  ', l)
    except Exception as e:
        print(f'{u} -> {e}')
