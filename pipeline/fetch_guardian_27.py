# -*- coding: utf-8 -*-
import urllib.request
import re

url = "https://www.theguardian.com/theguardian/2026/oct/27/all"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
try:
    with urllib.request.urlopen(req, timeout=10) as response:
        html = response.read().decode("utf-8", errors="ignore")
        # Find all hrefs (relative or absolute)
        hrefs = re.findall(r'href=["\']([^"\']+)["\']', html)
        print("Total hrefs:", len(hrefs))
        article_links = []
        for h in hrefs:
            if re.search(r'/\d{4}/[a-z]{3}/\d{1,2}/', h):
                article_links.append(h)
        print("Dated article hrefs:", len(article_links))
        unique_arts = sorted(list(set(article_links)))
        print("Unique dated articles:", len(unique_arts))
        for u in unique_arts[:40]:
            print(" -", u)
except Exception as e:
    print("Error:", e)
