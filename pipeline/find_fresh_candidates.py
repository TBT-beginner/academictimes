# -*- coding: utf-8 -*-
import os, sys, re, urllib.request

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "pipeline"))
from articles_data import ARTICLES

used_urls = set(a.get("source_url") for a in ARTICLES if a.get("source_url"))
used_slugs = set(a.get("slug") for a in ARTICLES if a.get("slug"))

print(f"Total existing articles: {len(ARTICLES)}")
print(f"Total existing URLs: {len(used_urls)}")
print(f"Total existing slugs: {len(used_slugs)}")

dates = ['2026/oct/30', '2026/oct/31', '2026/nov/01', '2026/nov/02']
all_candidates = []

for d in dates:
    url = f"https://www.theguardian.com/theguardian/{d}/all"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    try:
        with urllib.request.urlopen(req, timeout=10) as r:
            html = r.read().decode('utf-8', errors='ignore')
            found = set(re.findall(r'href=[\'"](https://www\.theguardian\.com/([a-zA-Z0-9\-]+)/\d{4}/[a-z]{3}/\d{1,2}/([a-zA-Z0-9\-]+))[\'"]', html))
            for full_url, section, slug_part in found:
                if full_url not in used_urls:
                    all_candidates.append((d, section, slug_part, full_url))
    except Exception as e:
        print(f"Error {d}: {e}")

print(f"Fresh unused candidates found: {len(all_candidates)}")

# Verify HTTP 200 for candidates and fetch title
verified = []
for d, sec, slug_part, full_url in all_candidates:
    try:
        req = urllib.request.Request(full_url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        with urllib.request.urlopen(req, timeout=8) as r:
            if r.status == 200:
                html_snippet = r.read(15000).decode('utf-8', errors='ignore')
                m = re.search(r'<title>(.*?)</title>', html_snippet)
                title = m.group(1).replace('| The Guardian', '').replace('&amp;', '&').strip() if m else slug_part
                verified.append({
                    "archive_date": d,
                    "section": sec,
                    "slug_part": slug_part,
                    "url": full_url,
                    "title": title
                })
                print(f"[200] [{sec}] {slug_part[:40]} | {title[:60]}")
    except Exception as e:
        pass

print(f"\nTotal verified fresh 200 OK articles: {len(verified)}")
import json
with open("news_portal/pipeline/verified_oct31_nov02_candidates.json", "w", encoding="utf-8") as f:
    json.dump(verified, f, ensure_ascii=False, indent=2)
