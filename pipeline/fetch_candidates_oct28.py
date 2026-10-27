# -*- coding: utf-8 -*-
import urllib.request
import re

sections = [
    "world", "science", "technology", "environment", "society", "law",
    "education", "culture", "books", "business", "global-development"
]

all_arts = set()
for sec in sections:
    url = f"https://www.theguardian.com/{sec}"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode("utf-8", errors="ignore")
            arts = re.findall(r'href="https://www.theguardian.com/([a-z-]+/2026/oct/(?:26|27|28)/[^"#]+)"', html)
            for a in arts:
                all_arts.add(a)
    except Exception as e:
        print(f"Sec {sec} error:", e)

# Also check date archives
for d in ["2026/oct/27", "2026/oct/26"]:
    url = f"https://www.theguardian.com/theguardian/{d}/all"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode("utf-8", errors="ignore")
            arts = re.findall(r'href="https://www.theguardian.com/([a-z-]+/2026/oct/\d{1,2}/[^"#]+)"', html)
            for a in arts:
                all_arts.add(a)
    except Exception as e:
        print(f"Date {d} error:", e)

print(f"Total candidate articles fetched: {len(all_arts)}")

# Filter against existing
import sys
sys.path.insert(0, "news_portal/pipeline")
import articles_data
used_urls = set(a.get("source_url") for a in articles_data.ARTICLES if a.get("source_url"))

fresh_candidates = []
for a in sorted(list(all_arts)):
    full_url = "https://www.theguardian.com/" + a
    if full_url not in used_urls:
        fresh_candidates.append(full_url)

print(f"Fresh unused candidates: {len(fresh_candidates)}")
for c in fresh_candidates[:25]:
    print(" -", c)
