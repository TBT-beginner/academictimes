import urllib.request
import re

url = 'https://www.theguardian.com/theguardian/2026/nov/04/all'
headers = {'User-Agent': 'Mozilla/5.0'}
req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req, timeout=10) as res:
    html = res.read().decode('utf-8', errors='ignore')

links = set(re.findall(r'href="(https://www.theguardian.com/[a-z0-9\-]+/\d{4}/[a-z]{3}/\d{2}/[^"#]+)"', html))
print(f'Total links on {url}: {len(links)}')

verified = []
for l in sorted(links):
    if l.endswith('/all'):
        continue
    try:
        r = urllib.request.Request(l, headers=headers)
        with urllib.request.urlopen(r, timeout=5) as res:
            if res.status == 200:
                print(f'[200 OK] {l}')
                verified.append(l)
    except Exception as e:
        print(f'[{e}] {l}')

print(f'\nTotal verified 200 OK: {len(verified)}')
