# -*- coding: utf-8 -*-
with open("news_portal/pipeline/fetch_guardian_27.py", "w", encoding="utf-8") as f:
    f.write('''# -*- coding: utf-8 -*-
import urllib.request
import re

url = "https://www.theguardian.com/theguardian/2026/oct/27/all"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
try:
    with urllib.request.urlopen(req, timeout=10) as response:
        html = response.read().decode("utf-8", errors="ignore")
        # Look for anchor hrefs
        links = re.findall(r'href="(https://www.theguardian.com/[^"#]+)"', html)
        print("Total full links:", len(links))
        sample_links = [l for l in links if not any(x in l for x in ["/preferences/", "/signin", "/terms", "/privacy", "/profile/"])]
        for s in set(sample_links)[:30]:
            print(" -", s)
except Exception as e:
    print("Error:", e)
''')
