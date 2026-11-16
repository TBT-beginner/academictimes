# -*- coding: utf-8 -*-
import urllib.request
import re
import json
import os
import sys

PIPELINE_DIR = os.path.dirname(os.path.abspath(__file__))
if PIPELINE_DIR not in sys.path:
    sys.path.insert(0, PIPELINE_DIR)

from articles_data import ARTICLES
existing_urls = {a.get('source_url', '') for a in ARTICLES}
existing_slugs = {a.get('slug', '') for a in ARTICLES}

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

dates = ['2026/nov/12', '2026/nov/13', '2026/nov/14', '2026/nov/15', '2026/nov/16']
found_articles = []

for d in dates:
    archive_url = f"https://www.theguardian.com/theguardian/{d}/all"
    try:
        req = urllib.request.Request(archive_url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            urls = re.findall(rf'href="(https://www.theguardian.com/[a-z-]+/{d}/[^"#?]+)"', html)
            for u in urls:
                if u not in found_articles and u not in existing_urls and not u.endswith('/all'):
                    if '/live/' not in u and '/gallery/' not in u and '/video/' not in u and '/audio/' not in u:
                        found_articles.append(u)
    except Exception as e:
        print(f"Error {archive_url}: {e}")

sections = [
    'world', 'science', 'environment', 'business', 'technology', 'culture',
    'law', 'society', 'books', 'media', 'stage', 'sport', 'uk-news', 'us-news', 'education'
]
for sec in sections:
    url = f"https://www.theguardian.com/{sec}"
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            urls = re.findall(r'href="(https://www.theguardian.com/[a-z-]+/2026/nov/(?:12|13|14|15|16)/[^"#?]+)"', html)
            for u in urls:
                if u not in found_articles and u not in existing_urls and not u.endswith('/all'):
                    if '/live/' not in u and '/gallery/' not in u and '/video/' not in u and '/audio/' not in u:
                        found_articles.append(u)
    except Exception as e:
        print(f"Error {url}: {e}")

print(f"Total candidate URLs found (new): {len(found_articles)}")

verified = []
import concurrent.futures

def check_url(u):
    try:
        req = urllib.request.Request(u, headers=headers)
        with urllib.request.urlopen(req, timeout=8) as resp:
            if resp.status == 200:
                html = resp.read().decode('utf-8', errors='ignore')
                tm = re.search(r'<title>(.*?)</title>', html)
                title = tm.group(1).replace(' | The Guardian', '').strip() if tm else ''
                dm = re.search(r'<meta name="description" content="(.*?)"', html)
                desc = dm.group(1) if dm else ''
                m_date = re.search(r'/2026/nov/(\d{2})/', u)
                day = m_date.group(1) if m_date else ''
                slug = u.rstrip('/').split('/')[-1]
                if slug not in existing_slugs and title:
                    return {'url': u, 'day': day, 'slug': slug, 'title': title, 'desc': desc}
    except Exception:
        pass
    return None

with concurrent.futures.ThreadPoolExecutor(max_workers=16) as executor:
    for res in executor.map(check_url, found_articles[:250]):
        if res:
            verified.append(res)

by_day = {}
for v in verified:
    by_day.setdefault(v['day'], []).append(v)

for d in sorted(by_day.keys()):
    print(f"Day {d}: {len(by_day[d])} verified articles")

out_path = os.path.join(PIPELINE_DIR, 'nov13_16_candidates.json')
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(verified, f, ensure_ascii=False, indent=2)
print(f"Saved {len(verified)} verified candidates to {out_path}")
