# -*- coding: utf-8 -*-
import urllib.request
import re

sections = ["science", "environment", "technology", "books", "artanddesign", "world", "society", "business"]
more_arts = set()

for s in sections:
    # try section archive / pagination
    url = f"https://www.theguardian.com/{s}?page=2"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode("utf-8", errors="ignore")
            arts = re.findall(r'href="https://www.theguardian.com/([a-z-]+/2026/oct/(?:26|27|28)/[^"#]+)"', html)
            for a in arts:
                more_arts.add("https://www.theguardian.com/" + a)
    except Exception as e:
        pass

import sys
sys.path.insert(0, "news_portal/pipeline")
import articles_data
used_urls = set(a.get("source_url") for a in articles_data.ARTICLES if a.get("source_url"))

fresh_more = [u for u in more_arts if u not in used_urls]
print(f"Additional fresh articles found: {len(fresh_more)}")
for m in fresh_more[:25]:
    print(" -", m)
