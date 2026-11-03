# -*- coding: utf-8 -*-
import urllib.request

test_urls = [
    ("science", "starwatch-catch-the-striking-trifecta-of-venus-the-moon-and-spica-at-break-of-dawn", "https://www.theguardian.com/science/2026/nov/02/starwatch-catch-the-striking-trifecta-of-venus-the-moon-and-spica-at-break-of-dawn"),
    ("science", "tender-bond-male-donkey-bull-baffles-scientists", "https://www.theguardian.com/science/2026/nov/02/tender-bond-male-donkey-bull-baffles-scientists"),
    ("environment", "polar-vortex-disruption-colder-weather-europe", "https://www.theguardian.com/environment/2026/nov/02/polar-vortex-disruption-colder-weather-europe"),
    ("environment", "british-gas-resume-force-fitting-prepayment-meters-months-after-112m-settlement", "https://www.theguardian.com/money/2026/nov/02/british-gas-resume-force-fitting-prepayment-meters-months-after-112m-settlement"),
    ("society", "nhs-early-warning-system-child-illness-england", "https://www.theguardian.com/society/2026/nov/02/nhs-early-warning-system-child-illness-england"),
    ("society", "counsellors-psychotherapists-statutory-regulation-uk-professional-bodies", "https://www.theguardian.com/society/2026/nov/02/counsellors-psychotherapists-statutory-regulation-uk-professional-bodies"),
    ("world", "nine-of-world-biggest-oil-firms-95bn-profit-third-quarter-iran-war", "https://www.theguardian.com/business/2026/nov/02/nine-of-world-biggest-oil-firms-95bn-profit-third-quarter-iran-war"),
    ("world", "hackers-fake-nuclear-chemical-threat-alert-kyiv-ukraine-emergency-app", "https://www.theguardian.com/world/2026/nov/02/hackers-fake-nuclear-chemical-threat-alert-kyiv-ukraine-emergency-app"),
    ("law", "australia-social-media-ban-high-court-challenge-reddit-digital-freedom-project", "https://www.theguardian.com/australia-news/2026/nov/03/australia-social-media-ban-high-court-challenge-reddit-digital-freedom-project"),
    ("law", "uk-making-up-china-policy-as-it-goes-along-mps", "https://www.theguardian.com/politics/2026/nov/02/uk-making-up-china-policy-as-it-goes-along-mps"),
    ("culture", "bbc-young-musician-teenage-violinist-sofia-demetriades", "https://www.theguardian.com/music/2026/nov/01/bbc-young-musician-teenage-violinist-sofia-demetriades"),
    ("entertainment", "john-lewis-christmas-advert-kristin-scott-thomas-glamorous-granny-gift-hunt", "https://www.theguardian.com/media/2026/nov/03/john-lewis-christmas-advert-kristin-scott-thomas-glamorous-granny-gift-hunt")
]

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

print(f"Testing {len(test_urls)} candidate URLs...")
all_ok = True
for cat, slug, url in test_urls:
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=8) as resp:
            print(f"[{resp.status} OK] {cat} / {slug}")
    except Exception as e:
        print(f"[FAIL] {cat} / {slug}: {e}")
        all_ok = False

print(f"All 12 URLs verified: {all_ok}")
