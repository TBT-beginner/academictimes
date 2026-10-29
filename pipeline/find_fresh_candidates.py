import glob
import json
import re
import urllib.request

all_used_urls = set()
for f in glob.glob("news_portal/pipeline/data_batch*.py"):
    with open(f, "r", encoding="utf-8") as fh:
        text = fh.read()
    urls = re.findall(r'"source_url":\s*"([^"]+)"', text)
    all_used_urls.update(urls)

with open("news_portal/pipeline/candidates_oct28.json", "r", encoding="utf-8") as f:
    cand = json.load(f)

fresh = [u for u in cand if u not in all_used_urls and not any(x in u for x in ['/video/', '/audio/', '/gallery/', '/live/'])]
print(f"Total used URLs in existing batches: {len(all_used_urls)}")
print(f"Completely fresh candidates from pool: {len(fresh)}")

for idx, u in enumerate(sorted(fresh)[:20]):
    print(f"{idx+1}: {u}")
