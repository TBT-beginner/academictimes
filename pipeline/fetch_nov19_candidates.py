# -*- coding: utf-8 -*-
"""Fetch fresh Guardian RSS candidates for 2026-11-18 and 2026-11-19."""

import urllib.request
import xml.etree.ElementTree as ET
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

rss_sections = [
    'world', 'science', 'environment', 'business', 'technology', 'culture',
    'law', 'society', 'education', 'books', 'music', 'film', 'stage',
    'uk-news', 'us-news', 'australia-news', 'sport'
]

candidates = {}
for sec in rss_sections:
    rss_url = f"https://www.theguardian.com/{sec}/rss"
    try:
        req = urllib.request.Request(rss_url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            xml_data = resp.read()
            root = ET.fromstring(xml_data)
            for item in root.findall('.//item'):
                link = item.findtext('link', '').strip()
                title = item.findtext('title', '').strip()
                desc = item.findtext('description', '').strip()
                desc = re.sub(r'<[^>]+>', '', desc).strip()
                if not link or link in existing_urls or link in candidates:
                    continue
                m = re.search(r'/2026/nov/(18|19)/', link)
                if not m:
                    continue
                if '/live/' in link or '/gallery/' in link or '/video/' in link or '/audio/' in link:
                    continue
                day = m.group(1)
                slug = link.rstrip('/').split('/')[-1]
                if slug in existing_slugs:
                    continue
                candidates[link] = {
                    'url': link,
                    'day': day,
                    'slug': slug,
                    'title': title,
                    'desc': desc[:250],
                    'section': sec
                }
    except Exception as e:
        print(f"Error {rss_url}: {e}")

all_list = list(candidates.values())
cand_path = os.path.join(PIPELINE_DIR, 'nov19_candidates.json')
with open(cand_path, 'w', encoding='utf-8') as f:
    json.dump(all_list, f, ensure_ascii=False, indent=2)

print(f"Total fresh candidates (Nov 18-19, excluding existing): {len(all_list)}")
for idx, c in enumerate(all_list, 1):
    print(f"[{idx:02d}] ({c['day']} | {c['section']}) {c['slug']} :: {c['title']}")
