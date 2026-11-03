# -*- coding: utf-8 -*-
import urllib.request
import re
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from articles_data import ARTICLES

used_urls = set(a.get("source_url") for a in ARTICLES)

dates = ['2026/nov/02', '2026/nov/01']

candidate_links = []

for d in dates:
    url = f"https://www.theguardian.com/theguardian/{d}/all"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    try:
        with urllib.request.urlopen(req, timeout=10) as r:
            html = r.read().decode('utf-8', errors='ignore')
            found = set(re.findall(r'href=[\'"](https://www\.theguardian\.com/[a-zA-Z0-9\-]+/\d{4}/[a-z]{3}/\d{1,2}/[a-zA-Z0-9\-]+)[\'"]', html))
            print(f"=== {d} (Total found {len(found)}) ===")
            fresh = [x for x in sorted(list(found)) if x not in used_urls]
            print(f"Fresh unused: {len(fresh)}")
            for item in fresh[:20]:
                print("  ", item)
                candidate_links.append(item)
    except Exception as e:
        print(f"Error {d}: {e}")

import json
with open("news_portal/pipeline/nov02_fresh_candidates.json", "w", encoding="utf-8") as f:
    json.dump(candidate_links, f, indent=2)
print("Saved nov02_fresh_candidates.json")
