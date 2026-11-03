# -*- coding: utf-8 -*-
import urllib.request
import re
import json
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from articles_data import ARTICLES

used_urls = set(a.get("source_url") for a in ARTICLES)

urls_to_check = [
    "https://www.theguardian.com/theguardian/2026/nov/02/all",
    "https://www.theguardian.com/theguardian/2026/nov/01/all",
    "https://www.theguardian.com/world/all",
    "https://www.theguardian.com/uk-news/all",
    "https://www.theguardian.com/environment/all",
    "https://www.theguardian.com/science/all",
    "https://www.theguardian.com/technology/all"
]

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

found_links = set()
for archive_url in urls_to_check:
    try:
        req = urllib.request.Request(archive_url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode("utf-8", errors="ignore")
            links = re.findall(r'href=["\'](https://www.theguardian.com/[a-z0-9\-]+/\d{4}/[a-z]{3}/\d{1,2}/[a-z0-9\-]+)["\']', html)
            for l in links:
                found_links.add(l)
    except Exception as e:
        print(f"Err {archive_url}: {e}")

print(f"Total links found: {len(found_links)}")
fresh = [l for l in found_links if l not in used_urls]
print(f"Fresh unused links: {len(fresh)}")

# Verify HTTP 200 OK
verified = []
for url in fresh[:50]:
    try:
        req = urllib.request.Request(url, headers=headers, method="HEAD")
        with urllib.request.urlopen(req, timeout=5) as resp:
            if resp.status == 200:
                verified.append(url)
    except Exception:
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=5) as resp:
                if resp.status == 200:
                    verified.append(url)
        except Exception:
            pass

print(f"Verified 200 OK links: {len(verified)}")
with open("news_portal/pipeline/verified_nov03_candidates.json", "w", encoding="utf-8") as f:
    json.dump(verified, f, indent=2)

for i, u in enumerate(verified[:25]):
    print(f"{i+1}: {u}")
