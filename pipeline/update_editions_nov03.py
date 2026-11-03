# -*- coding: utf-8 -*-
"""Add 2026-11-03 edition to build_portal_data_js.py and build_junior_data_js.py."""

import re

# 1. Update build_portal_data_js.py
with open("news_portal/pipeline/build_portal_data_js.py", "r", encoding="utf-8") as f:
    portal_text = f.read()

portal_target = '    editions_dict = {\n        "2026-11-02": {\n            "dateStr": "Monday November 2 2026",\n            "editionLabel": "2026年11月2日 (月) 号 【本日・最新・全12記事】",'

portal_replacement = '''    editions_dict = {
        "2026-11-03": {
            "dateStr": "Tuesday November 3 2026",
            "editionLabel": "2026年11月3日 (火) 号 【本日・最新・全12記事】",
            "tagline": "特集：金星・月・スピカ三重整列・ロバと雄牛の異種間愛着・北極極渦分裂寒波・豪州16歳未満SNS禁止違憲訴訟",
            "topLeadSlug": "starwatch-catch-the-striking-trifecta-of-venus-the-moon-and-spica-at-break-of-dawn",
            "subLeadSlugs": [
                "tender-bond-male-donkey-bull-baffles-scientists",
                "polar-vortex-disruption-colder-weather-europe",
                "australia-social-media-ban-high-court-challenge-reddit-digital-freedom-project"
            ],
            "leftDispatches": [
                "british-gas-resume-force-fitting-prepayment-meters-months-after-112m-settlement",
                "nhs-early-warning-system-child-illness-england",
                "counsellors-psychotherapists-statutory-regulation-uk-professional-bodies",
                "nine-of-world-biggest-oil-firms-95bn-profit-third-quarter-iran-war"
            ],
            "rightDigestSlugs": [
                "hackers-fake-nuclear-chemical-threat-alert-kyiv-ukraine-emergency-app",
                "uk-making-up-china-policy-as-it-goes-along-mps",
                "bbc-young-musician-teenage-violinist-sofia-demetriades",
                "john-lewis-christmas-advert-kristin-scott-thomas-glamorous-granny-gift-hunt"
            ]
        },
        "2026-11-02": {
            "dateStr": "Monday November 2 2026",
            "editionLabel": "2026年11月2日 (月) 号 【全12記事・アーカイブ】",'''

portal_norm = portal_text.replace('\r\n', '\n')
if portal_target in portal_norm:
    portal_norm = portal_norm.replace(portal_target, portal_replacement, 1)
    with open("news_portal/pipeline/build_portal_data_js.py", "w", encoding="utf-8") as f:
        f.write(portal_norm)
    print("Updated build_portal_data_js.py for 2026-11-03.")
else:
    print("Could not find target in build_portal_data_js.py")

# 2. Update build_junior_data_js.py
with open("news_portal/pipeline/build_junior_data_js.py", "r", encoding="utf-8") as f:
    junior_text = f.read()

junior_target = 'EDITIONS_DATA = {\n    "2026-11-02": {\n        "dateStr": "Monday November 2 2026",\n        "editionLabel": "2026年11月2日 (月) 号 【本日・最新・全12記事】",'

junior_replacement = '''EDITIONS_DATA = {
    "2026-11-03": {
        "dateStr": "Tuesday November 3 2026",
        "editionLabel": "2026年11月3日 (火) 号 【本日・最新・全12記事】",
        "tagline": "特集：明け方の金星と三日月・ロバと雄牛の友情・北極の寒波・豪州SNS禁止令の裁判",
        "topLeadSlug": "starwatch-catch-the-striking-trifecta-of-venus-the-moon-and-spica-at-break-of-dawn",
        "subLeadSlugs": [
            "tender-bond-male-donkey-bull-baffles-scientists",
            "polar-vortex-disruption-colder-weather-europe",
            "australia-social-media-ban-high-court-challenge-reddit-digital-freedom-project"
        ],
        "leftDispatches": [
            "british-gas-resume-force-fitting-prepayment-meters-months-after-112m-settlement",
            "nhs-early-warning-system-child-illness-england",
            "counsellors-psychotherapists-statutory-regulation-uk-professional-bodies",
            "nine-of-world-biggest-oil-firms-95bn-profit-third-quarter-iran-war"
        ],
        "rightDigestSlugs": [
            "hackers-fake-nuclear-chemical-threat-alert-kyiv-ukraine-emergency-app",
            "uk-making-up-china-policy-as-it-goes-along-mps",
            "bbc-young-musician-teenage-violinist-sofia-demetriades",
            "john-lewis-christmas-advert-kristin-scott-thomas-glamorous-granny-gift-hunt"
        ]
    },
    "2026-11-02": {
        "dateStr": "Monday November 2 2026",
        "editionLabel": "2026年11月2日 (月) 号 【全12記事・アーカイブ】",'''

junior_norm = junior_text.replace('\r\n', '\n')
if junior_target in junior_norm:
    junior_norm = junior_norm.replace(junior_target, junior_replacement, 1)
    with open("news_portal/pipeline/build_junior_data_js.py", "w", encoding="utf-8") as f:
        f.write(junior_norm)
    print("Updated build_junior_data_js.py for 2026-11-03.")
else:
    print("Could not find target in build_junior_data_js.py")
