# -*- coding: utf-8 -*-
import urllib.request
import re

headers = {'User-Agent': 'Mozilla/5.0'}
sections = ['world', 'science', 'environment', 'technology', 'culture', 'business', 'society', 'lifeandstyle']
found = set()

for sec in sections:
    try:
        url = f'https://www.theguardian.com/{sec}'
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            matches = re.findall(r'href=["\'](https://www\.theguardian\.com/[^"\'?#]+/2026/oct/(?:19|20)/[^"\'?#]+)["\']', html)
            for m in matches:
                if not any(x in m for x in ['/live/', '/gallery/', '/audio/', '/video/']):
                    found.add(m)
    except Exception as e:
        print(sec, e)

print(f"Total unique links found on section fronts: {len(found)}")
for u in sorted(found):
    print(u)
