# -*- coding: utf-8 -*-
import urllib.request
import re

dates = ['2026/oct/30', '2026/oct/31', '2026/nov/01', '2026/nov/02']

for d in dates:
    url = f"https://www.theguardian.com/theguardian/{d}/all"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    try:
        with urllib.request.urlopen(req, timeout=10) as r:
            html = r.read().decode('utf-8', errors='ignore')
            # Extract links matching guardian article pattern
            found = set(re.findall(r'href=[\'"](https://www\.theguardian\.com/[a-zA-Z0-9\-]+/\d{4}/[a-z]{3}/\d{1,2}/[a-zA-Z0-9\-]+)[\'"]', html))
            print(f"=== {d} (Total {len(found)}) ===")
            for item in sorted(list(found))[:15]:
                print("  ", item)
    except Exception as e:
        print(f"Error {d}: {e}")
