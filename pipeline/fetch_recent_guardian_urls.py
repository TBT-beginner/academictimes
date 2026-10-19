# -*- coding: utf-8 -*-
import urllib.request
import re

dates = ['19', '20']
headers = {'User-Agent': 'Mozilla/5.0'}

for d in dates:
    url = f'https://www.theguardian.com/theguardian/2026/oct/{d}/all'
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            pattern = re.compile(rf'href=["\'](https://www\.theguardian\.com/[^"\']+/2026/oct/{d}/[^"\']+)["\']')
            links = pattern.findall(html)
            # Filter out non-article links like audio/video if needed, keep clean article slugs
            clean_links = []
            for l in links:
                if not any(skip in l for skip in ['/live/', '/gallery/', '/audio/', '/video/']):
                    clean_links.append(l)
            clean_links = list(dict.fromkeys(clean_links))
            print(f'=== Date 2026-10-{d}: {len(clean_links)} clean links found ===')
            for l in clean_links[:25]:
                print('  ', l)
    except Exception as e:
        print(f'Error for {d}: {e}')
