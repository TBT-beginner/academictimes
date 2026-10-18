# -*- coding: utf-8 -*-
import urllib.request
import re
import json

sections = ['science', 'environment', 'technology', 'world', 'society', 'books', 'culture', 'business', 'law', 'education']
dates = ['16', '17', '18', '19']
headers = {'User-Agent': 'Mozilla/5.0'}

all_verified = {d: [] for d in dates}

for d in dates:
    print(f"=== Scanning date: 2026-10-{d} ===")
    seen_links = set()
    for sec in sections:
        url = f'https://www.theguardian.com/{sec}/2026/oct/{d}/all'
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=10) as resp:
                html = resp.read().decode('utf-8', errors='ignore')
                pattern = re.compile(rf'href=["\'](https://www\.theguardian\.com/[^"\']+/2026/oct/{d}/[^"\']+)["\']')
                links = pattern.findall(html)
                for l in links:
                    if any(skip in l for skip in ['/live/', '/gallery/', '/audio/', '/video/', '/football/', '/sport/']):
                        continue
                    clean_l = l.split('?')[0].split('#')[0]
                    if clean_l not in seen_links:
                        seen_links.add(clean_l)
                        all_verified[d].append((sec, clean_l))
        except Exception as e:
            # Section might not have /all or 404
            pass

    print(f"Total collected for {d}: {len(all_verified[d])}")

# Verify HTTP 200 for collected links
results = {}
for d in dates:
    results[d] = []
    print(f"--- Verifying HTTP 200 for 2026-10-{d} ---")
    for sec, url in all_verified[d]:
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=8) as resp:
                if resp.status == 200:
                    results[d].append({'section': sec, 'url': url})
                    print(f"[200 OK] {sec}: {url}")
        except Exception as e:
            print(f"[FAIL] {url}: {e}")

with open('pipeline/verified_oct16_19.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print("\nSummary of 200 OK links by date:")
for d, lst in results.items():
    print(f"2026-10-{d}: {len(lst)} articles verified")
