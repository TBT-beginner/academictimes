# -*- coding: utf-8 -*-
import urllib.request
import re

sections = [
    "world", "science", "technology", "environment", "society", "law",
    "education", "culture", "books", "artanddesign", "business", "global-development"
]

all_arts = set()
for sec in sections:
    url = f"https://www.theguardian.com/{sec}"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode("utf-8", errors="ignore")
            arts = re.findall(r'href="https://www.theguardian.com/([a-z-]+/2026/oct/(?:26|27)/[^"#]+)"', html)
            for a in arts:
                all_arts.add(a)
    except Exception as e:
        print(f"Sec {sec} error:", e)

print(f"Total fresh articles from sections (Oct 26-27): {len(all_arts)}")
for a in sorted(list(all_arts)):
    print(" -", a)
