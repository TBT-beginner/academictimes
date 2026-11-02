# -*- coding: utf-8 -*-
import os, sys, re, urllib.request, json
from concurrent.futures import ThreadPoolExecutor

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "pipeline"))
from articles_data import ARTICLES

used_urls = set(a.get("source_url") for a in ARTICLES if a.get("source_url"))
used_slugs = set(a.get("slug") for a in ARTICLES if a.get("slug"))

dates = ['2026/oct/30', '2026/oct/31', '2026/nov/01', '2026/nov/02']
candidates = []

for d in dates:
    url = f"https://www.theguardian.com/theguardian/{d}/all"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    try:
        with urllib.request.urlopen(req, timeout=8) as r:
            html = r.read().decode('utf-8', errors='ignore')
            found = set(re.findall(r'href=[\'"](https://www\.theguardian\.com/([a-zA-Z0-9\-]+)/\d{4}/[a-z]{3}/\d{1,2}/([a-zA-Z0-9\-]+))[\'"]', html))
            for full_url, section, slug_part in found:
                if full_url not in used_urls and slug_part not in used_slugs:
                    candidates.append((d, section, slug_part, full_url))
    except Exception as e:
        print(f"Error {d}: {e}", flush=True)

# Deduplicate candidates by URL
seen_url = set()
unique_candidates = []
for item in candidates:
    if item[3] not in seen_url:
        seen_url.add(item[3])
        unique_candidates.append(item)

print(f"Total unique candidates to verify: {len(unique_candidates)}", flush=True)

def verify_candidate(item):
    d, sec, slug_part, full_url = item
    try:
        req = urllib.request.Request(full_url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        with urllib.request.urlopen(req, timeout=6) as r:
            if r.status == 200:
                html_snippet = r.read(12000).decode('utf-8', errors='ignore')
                m = re.search(r'<title>(.*?)</title>', html_snippet)
                title = m.group(1).replace('| The Guardian', '').replace('&amp;', '&').strip() if m else slug_part
                return {
                    "archive_date": d,
                    "section": sec,
                    "slug": slug_part,
                    "url": full_url,
                    "title": title
                }
    except Exception:
        pass
    return None

verified = []
with ThreadPoolExecutor(max_workers=16) as pool:
    results = pool.map(verify_candidate, unique_candidates)
    for r in results:
        if r:
            verified.append(r)

print(f"Verified {len(verified)} fresh articles with HTTP 200 OK!", flush=True)

out_file = os.path.join(os.path.dirname(__file__), "verified_oct31_nov02_candidates.json")
with open(out_file, "w", encoding="utf-8") as f:
    json.dump(verified, f, ensure_ascii=False, indent=2)
print("Saved to", out_file, flush=True)
