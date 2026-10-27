# -*- coding: utf-8 -*-
import urllib.request
import re

dates = ["2026/oct/26", "2026/oct/25", "2026/oct/24", "2026/oct/23"]
for d in dates:
    url = f"https://www.theguardian.com/theguardian/{d}/all"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode("utf-8", errors="ignore")
            # find all guardian article links
            arts = set(re.findall(r'href="https://www.theguardian.com/([a-z-]+/2026/oct/\d{1,2}/[^"#]+)"', html))
            print(f"Date {d}: {len(arts)} articles found")
            for a in list(arts)[:5]:
                print("  *", a)
    except Exception as e:
        print(f"Date {d} error:", e)
