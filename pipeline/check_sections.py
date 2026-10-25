import urllib.request
import re

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

urls = [
    'https://www.theguardian.com/science/2026/oct/24/all',
    'https://www.theguardian.com/technology/2026/oct/24/all',
    'https://www.theguardian.com/environment/2026/oct/24/all',
    'https://www.theguardian.com/law/2026/oct/24/all',
    'https://www.theguardian.com/culture/2026/oct/24/all',
    'https://www.theguardian.com/society/2026/oct/24/all',
    'https://www.theguardian.com/world/2026/oct/24/all',
    'https://www.theguardian.com/theguardian/2026/oct/24/all'
]

for u in urls:
    try:
        req = urllib.request.Request(u, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8')
            matches = re.findall(r'href="(https://www.theguardian.com/[^"]+/(?:2026/oct/24|2026/oct/25)/[^"]+)"', html)
            print(f"{u} matches: {len(set(matches))}")
            for m in list(set(matches))[:3]:
                print(f"   {m}")
    except Exception as e:
        print(f"{u} error: {e}")
