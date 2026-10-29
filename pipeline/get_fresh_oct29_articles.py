import glob
import re

all_used_urls = set()
for f in glob.glob("news_portal/pipeline/*.py"):
    with open(f, "r", encoding="utf-8") as fh:
        text = fh.read()
    urls = re.findall(r'https://www\.theguardian\.com/[^\s",\'\)]+', text)
    for u in urls:
        if any(x in u for x in ['/2026/oct/']):
            all_used_urls.add(u)

print(f"Total Guardian 2026/oct URLs previously referenced: {len(all_used_urls)}")

# Now let's fetch October 29 fresh articles from Guardian
import urllib.request

sections = [
    "https://www.theguardian.com/world/2026/oct/29/all",
    "https://www.theguardian.com/business/2026/oct/29/all",
    "https://www.theguardian.com/environment/2026/oct/29/all",
    "https://www.theguardian.com/science/2026/oct/29/all",
    "https://www.theguardian.com/technology/2026/oct/29/all",
    "https://www.theguardian.com/culture/2026/oct/29/all",
    "https://www.theguardian.com/music/2026/oct/29/all",
    "https://www.theguardian.com/theguardian/2026/oct/29/all",
    "https://www.theguardian.com/theguardian/2026/oct/28/all"
]

fresh_candidates = set()
for sec in sections:
    try:
        req = urllib.request.Request(sec, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        with urllib.request.urlopen(req, timeout=8) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            links = re.findall(r'href=["\'](https://www\.theguardian\.com/[a-z0-9\-/]+/2026/oct/2[89]/[a-z0-9\-]+)["\']', html)
            for l in links:
                if not any(x in l for x in ['/all', '/live/', '/gallery/', '/audio/', '/video/']):
                    if l not in all_used_urls:
                        fresh_candidates.add(l)
    except Exception as e:
        print(f"Failed {sec}: {e}")

print(f"Fresh verified candidates for Batch 26: {len(fresh_candidates)}")
for idx, u in enumerate(sorted(list(fresh_candidates))[:35]):
    print(f"{idx+1}: {u}")
