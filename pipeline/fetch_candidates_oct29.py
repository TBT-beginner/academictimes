import urllib.request
import re
import json

urls_to_check = [
    "https://www.theguardian.com/theguardian/2026/oct/29/all",
    "https://www.theguardian.com/world/2026/oct/29/all",
    "https://www.theguardian.com/environment/2026/oct/29/all",
    "https://www.theguardian.com/science/2026/oct/29/all",
    "https://www.theguardian.com/technology/2026/oct/29/all",
    "https://www.theguardian.com/business/2026/oct/29/all",
    "https://www.theguardian.com/culture/2026/oct/29/all",
    "https://www.theguardian.com/theguardian/2026/oct/28/all",
]

found = set()
for archive_url in urls_to_check:
    try:
        req = urllib.request.Request(archive_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            links = re.findall(r'href=["\'](https://www\.theguardian\.com/[a-z0-9\-/]+/2026/oct/2[89]/[a-z0-9\-]+)["\']', html)
            for l in links:
                if not any(x in l for x in ['/all', '/live/', '/gallery/', '/audio/', '/video/']):
                    found.add(l)
    except Exception as e:
        print(f"Failed {archive_url}: {e}")

print(f"Total unique article candidates: {len(found)}")
with open("news_portal/pipeline/candidates_oct29.json", "w", encoding="utf-8") as f:
    json.dump(sorted(list(found)), f, indent=2)
