# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, "news_portal/pipeline")
import articles_data

used_urls = set()
for a in articles_data.ARTICLES:
    u = a.get("source_url")
    if u:
        used_urls.add(u)

print(f"Total existing articles in portal: {len(articles_data.ARTICLES)}")
print(f"Total used source URLs: {len(used_urls)}")

# Check candidate URLs against used_urls
with open("news_portal/pipeline/list_oct26_all.py", "r", encoding="utf-8") as f:
    pass

import urllib.request

candidates = [
    "https://www.theguardian.com/technology/2026/oct/26/iphone-duo-owners-cracks-apple-first-foldable-handset",
    "https://www.theguardian.com/world/2026/oct/26/flavio-bolsonaro-brazil-lula-election",
    "https://www.theguardian.com/world/2026/oct/26/netanyahu-reportedly-pressured-israel-military-attack-iran-runup-to-election",
    "https://www.theguardian.com/world/2026/oct/26/audi-boss-under-fire-in-germany-for-trump-rally-appearance",
    "https://www.theguardian.com/stage/2026/oct/26/michael-gambon-pranks-revealed-biography",
    "https://www.theguardian.com/world/2026/oct/26/young-britons-bayeux-tapestry-tickets-british-museum-hollywood-blockbusters",
    "https://www.theguardian.com/world/2026/oct/26/we-built-this-land-descendants-of-enslaved-people-are-reclaiming-their-history-across-south-africas-vineyards",
    "https://www.theguardian.com/education/2026/oct/26/training-costs-apprenticeships-older-workers-youth-jobs-crisis-neet",
    "https://www.theguardian.com/politics/2026/oct/26/uk-international-aid-target-spending-shortfall-budget-research",
    "https://www.theguardian.com/science/2026/oct/26/starwatch-bright-stars-pegasus-distinctive-constellation",
    "https://www.theguardian.com/society/2026/oct/25/ethnic-minorities-england-breast-cancer-screening-disparity",
    "https://www.theguardian.com/society/2026/oct/25/homelessness-rough-sleeping-double-spending-burnham",
    "https://www.theguardian.com/business/2026/oct/25/cutting-red-tape-is-nothing-but-a-red-herring-and-arguably-counterproductive",
    "https://www.theguardian.com/business/2026/oct/25/volkswagen-to-build-4bn-audi-suv-factory-in-us-despite-job-cuts-at-home",
    "https://www.theguardian.com/world/2026/oct/25/macrons-vandals-pay-bill-puts-right-to-protest-at-risk",
    "https://www.theguardian.com/politics/2026/oct/25/burnham-rayner-labour-eu-free-movement-brexit",
    "https://www.theguardian.com/us-news/2026/oct/25/elvis-presley-anthropic-lawsuit-ai-models-music"
]

print("\nCandidate verification:")
for c in candidates:
    req = urllib.request.Request(c, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            is_new = c not in used_urls
            print(f"[{resp.status}] New:{is_new} -> {c}")
    except Exception as e:
        print(f"[ERR] {e} -> {c}")
