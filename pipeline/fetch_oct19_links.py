# -*- coding: utf-8 -*-
import urllib.request
import re

urls = [
    'https://www.theguardian.com/uk',
    'https://www.theguardian.com/world',
    'https://www.theguardian.com/business',
    'https://www.theguardian.com/technology',
    'https://www.theguardian.com/environment',
    'https://www.theguardian.com/science',
    'https://www.theguardian.com/culture',
    'https://www.theguardian.com/society'
]

headers = {'User-Agent': 'Mozilla/5.0'}
found19 = set()

for u in urls:
    try:
        req = urllib.request.Request(u, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            matches = re.findall(r'href=["\'](https://www\.theguardian\.com/[^"\']+/2026/oct/19/[^"\']+)["\']', html)
            for m in matches:
                clean = m.split('?')[0].split('#')[0]
                if not any(skip in clean for skip in ['/live/', '/gallery/', '/audio/', '/video/', '/football/', '/sport/']):
                    found19.add(clean)
    except Exception as e:
        print(f"Error {u}: {e}")

print(f"Found {len(found19)} candidate links for Oct 19:")
verified19 = []
for l in sorted(found19):
    try:
        req = urllib.request.Request(l, headers=headers)
        with urllib.request.urlopen(req, timeout=8) as resp:
            if resp.status == 200:
                print(f"[200 OK] {l}")
                verified19.append(l)
    except Exception as e:
        print(f"[FAIL] {l}: {e}")

print(f"\nTotal verified 200 OK for Oct 19: {len(verified19)}")
