# -*- coding: utf-8 -*-
"""Update build_portal_data_js.py and build_junior_data_js.py with 2026-10-30 edition."""
import os

PORTAL_BUILDER = os.path.join(os.path.dirname(__file__), "build_portal_data_js.py")
JUNIOR_BUILDER = os.path.join(os.path.dirname(__file__), "build_junior_data_js.py")

senior_edition_snippet = """        "2026-10-30": {
            "dateStr": "Friday October 30 2026",
            "editionLabel": "2026年10月30日 (金) 号 【本日・最新・全12記事】",
            "tagline": "特集：海鳥の時差ボケ航法・英賃金開示権・トブラローネ商標訴訟・湾岸和平協定・CD復権",
            "topLeadSlug": "seabird-jet-lag-navigation-nature-study",
            "subLeadSlugs": [
                "uk-workers-right-to-know-pay-gender-disparities-ehrc",
                "gulf-states-multipart-peace-deal-us-iran-tensions",
                "toblerone-trademark-shape-lawsuit-vegan-chocolate"
            ],
            "leftDispatches": [
                "queen-of-spain-butterfly-climate-migration-britain",
                "africa-ebola-outbreak-global-surveillance-uk-health",
                "music-streaming-fatigue-cd-sales-revival-gen-z",
                "datacenter-acoustic-pollution-lawsuit-mississippi"
            ],
            "rightDigestSlugs": [
                "us-electric-ferries-maritime-decarbonization-transit",
                "thames-water-emergency-debt-financing-insolvency-crisis",
                "gullivers-travels-tercentenary-satire-modern-relevance",
                "doordash-instacart-grocery-delivery-merger-antitrust"
            ]
        },
"""

junior_edition_snippet = """    "2026-10-30": {
        "dateStr": "Friday October 30 2026",
        "editionLabel": "2026年10月30日 (金) 号 【本日・最新・全12記事】",
        "tagline": "特集：海鳥の時差ボケ航法・職場の給与開示権・チョコの形をめぐる裁判・レコードやCDの復活",
        "topLeadSlug": "seabird-jet-lag-navigation-nature-study",
        "subLeadSlugs": [
            "uk-workers-right-to-know-pay-gender-disparities-ehrc",
            "gulf-states-multipart-peace-deal-us-iran-tensions",
            "toblerone-trademark-shape-lawsuit-vegan-chocolate"
        ],
        "leftDispatches": [
            "queen-of-spain-butterfly-climate-migration-britain",
            "africa-ebola-outbreak-global-surveillance-uk-health",
            "music-streaming-fatigue-cd-sales-revival-gen-z",
            "datacenter-acoustic-pollution-lawsuit-mississippi"
        ],
        "rightDigestSlugs": [
            "us-electric-ferries-maritime-decarbonization-transit",
            "thames-water-emergency-debt-financing-insolvency-crisis",
            "gullivers-travels-tercentenary-satire-modern-relevance",
            "doordash-instacart-grocery-delivery-merger-antitrust"
        ]
    },
"""

# 1. Update Portal JS Builder
with open(PORTAL_BUILDER, "r", encoding="utf-8") as f:
    portal_text = f.read()

# Update 10-29 edition label to archive
portal_text = portal_text.replace('2026年10月29日 (木) 号 【本日・最新・全12記事】', '2026年10月29日 (木) 号 【全12記事・アーカイブ】')
# Also handle potential mojibake string if present
import re
portal_text = re.sub(r'("2026-10-29":\s*\{\s*"dateStr":\s*"Thursday October 29 2026",\s*"editionLabel":\s*")[^"]+(")', r'\g<1>2026年10月29日 (木) 号 【全12記事・アーカイブ】\g<2>', portal_text)

if '"2026-10-30": {' not in portal_text:
    target = 'editions_dict = {\n'
    idx = portal_text.find(target)
    if idx != -1:
        portal_text = portal_text[:idx + len(target)] + senior_edition_snippet + portal_text[idx + len(target):]
        with open(PORTAL_BUILDER, "w", encoding="utf-8") as f:
            f.write(portal_text)
        print("[OK] Updated build_portal_data_js.py")
    else:
        print("[ERR] Could not find editions_dict in build_portal_data_js.py")
else:
    print("[SKIP] 2026-10-30 already in build_portal_data_js.py")

# 2. Update Junior JS Builder
with open(JUNIOR_BUILDER, "r", encoding="utf-8") as f:
    junior_text = f.read()

junior_text = junior_text.replace('2026年10月29日 (木) 号 【本日・最新・全12記事】', '2026年10月29日 (木) 号 【全12記事・アーカイブ】')
junior_text = re.sub(r'("2026-10-29":\s*\{\s*"dateStr":\s*"Thursday October 29 2026",\s*"editionLabel":\s*")[^"]+(")', r'\g<1>2026年10月29日 (木) 号 【全12記事・アーカイブ】\g<2>', junior_text)

if '"2026-10-30": {' not in junior_text:
    target = 'EDITIONS_DATA = {\n'
    idx = junior_text.find(target)
    if idx != -1:
        junior_text = junior_text[:idx + len(target)] + junior_edition_snippet + junior_text[idx + len(target):]
        with open(JUNIOR_BUILDER, "w", encoding="utf-8") as f:
            f.write(junior_text)
        print("[OK] Updated build_junior_data_js.py")
    else:
        print("[ERR] Could not find EDITIONS_DATA in build_junior_data_js.py")
else:
    print("[SKIP] 2026-10-30 already in build_junior_data_js.py")
