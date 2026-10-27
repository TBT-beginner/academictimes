# -*- coding: utf-8 -*-
import urllib.request
import re

candidates = [
    ("env_slovenia_glacier", "https://www.theguardian.com/environment/2026/oct/27/slovenia-mourns-loss-glacier-highest-peak-scorching-summer"),
    ("tech_grok_film", "https://www.theguardian.com/technology/2026/oct/27/reviewers-slate-musk-ai-grok-odyssey-film-nolan"),
    ("law_high_court", "https://www.theguardian.com/law/2026/oct/27/ppt-high-court-publication-sexual-offence-allegations"),
    ("world_bolsonaro_flight", "https://www.theguardian.com/world/2026/oct/27/flavio-bolsonaro-brazil-argentina-fled"),
    ("world_israel_exit_polls", "https://www.theguardian.com/world/2026/oct/27/israel-election-too-close-to-call-as-exit-polls-give-netanyahu-bloc-slightly-fewer-seats"),
    ("law_elvis_ai_anthropic", "https://www.theguardian.com/us-news/2026/oct/25/elvis-presley-anthropic-lawsuit-ai-models-music"),
    ("biz_red_tape_herring", "https://www.theguardian.com/business/2026/oct/25/cutting-red-tape-is-nothing-but-a-red-herring-and-arguably-counterproductive"),
    ("biz_boe_interest_rates", "https://www.theguardian.com/business/2026/oct/25/interest-rates-bank-of-england-rises-summer-2027"),
    ("society_retail_paternity", "https://www.theguardian.com/business/2026/oct/25/retail-leads-way-paternity-leave-government-urged-improve-offer"),
    ("world_vw_us_factory", "https://www.theguardian.com/business/2026/oct/25/volkswagen-to-build-4bn-audi-suv-factory-in-us-despite-job-cuts-at-home"),
    ("politics_brexit_movement", "https://www.theguardian.com/politics/2026/oct/25/burnham-rayner-labour-eu-free-movement-brexit"),
    ("culture_sam_fender_tickets", "https://www.theguardian.com/music/2026/oct/24/sam-fender-fans-high-ticket-prices-proper-massive-tour-getting-changed")
]

for tag, u in candidates:
    req = urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode("utf-8", errors="ignore")
            title_m = re.search(r'<title>([^<]+)</title>', html)
            title = title_m.group(1).replace(" | The Guardian", "").strip() if title_m else ""
            paras = re.findall(r'<p>([^<]+)</p>', html)
            lead = paras[0] if paras else "No lead"
            print(f"[{resp.status}] {tag}:")
            print("  Title:", title.encode("ascii", errors="replace").decode("ascii"))
            print("  Lead:", lead[:120].encode("ascii", errors="replace").decode("ascii"))
            print()
    except Exception as e:
        print(f"[ERR] {tag}: {e}")
