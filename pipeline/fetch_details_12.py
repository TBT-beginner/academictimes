# -*- coding: utf-8 -*-
import urllib.request
import re

urls = [
    ("tech_foldable", "https://www.theguardian.com/technology/2026/oct/26/iphone-duo-owners-cracks-apple-first-foldable-handset"),
    ("world_brazil", "https://www.theguardian.com/world/2026/oct/26/flavio-bolsonaro-brazil-lula-election"),
    ("world_israel_iran", "https://www.theguardian.com/world/2026/oct/26/netanyahu-reportedly-pressured-israel-military-attack-iran-runup-to-election"),
    ("stage_gambon", "https://www.theguardian.com/stage/2026/oct/26/michael-gambon-pranks-revealed-biography"),
    ("culture_bayeux", "https://www.theguardian.com/world/2026/oct/26/young-britons-bayeux-tapestry-tickets-british-museum-hollywood-blockbusters"),
    ("culture_south_africa", "https://www.theguardian.com/world/2026/oct/26/we-built-this-land-descendants-of-enslaved-people-are-reclaiming-their-history-across-south-africas-vineyards"),
    ("education_neet", "https://www.theguardian.com/education/2026/oct/26/training-costs-apprenticeships-older-workers-youth-jobs-crisis-neet"),
    ("politics_aid", "https://www.theguardian.com/politics/2026/oct/26/uk-international-aid-target-spending-shortfall-budget-research"),
    ("science_pegasus", "https://www.theguardian.com/science/2026/oct/26/starwatch-bright-stars-pegasus-distinctive-constellation"),
    ("society_cancer_screening", "https://www.theguardian.com/society/2026/oct/25/ethnic-minorities-england-breast-cancer-screening-disparity"),
    ("society_homelessness", "https://www.theguardian.com/society/2026/oct/25/homelessness-rough-sleeping-double-spending-burnham"),
    ("law_macron_protest", "https://www.theguardian.com/world/2026/oct/25/macrons-vandals-pay-bill-puts-right-to-protest-at-risk")
]

for tag, u in urls:
    req = urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode("utf-8", errors="ignore")
            title_m = re.search(r'<title>([^<]+)</title>', html)
            title = title_m.group(1).replace(" | The Guardian", "").strip() if title_m else ""
            # find first couple paragraphs
            paras = re.findall(r'<p>([^<]+)</p>', html)
            print(f"=== [{tag}] ===")
            print("Title:", title)
            print("Lead:", paras[0] if paras else "No lead")
            print()
    except Exception as e:
        print(f"Error {tag}: {e}")
