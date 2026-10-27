# -*- coding: utf-8 -*-
import urllib.request
import re

url = "https://www.theguardian.com/theguardian/2026/oct/26/all"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
try:
    with urllib.request.urlopen(req, timeout=10) as resp:
        html = resp.read().decode("utf-8", errors="ignore")
        arts = set(re.findall(r'href="https://www.theguardian.com/([a-z-]+/2026/oct/\d{1,2}/[^"#]+)"', html))
        print(f"Total articles on 2026/oct/26: {len(arts)}")
        for a in sorted(list(arts)):
            print(" -", a)
except Exception as e:
    print("Error:", e)
