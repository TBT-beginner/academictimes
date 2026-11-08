# -*- coding: utf-8 -*-
junior_py = "news_portal/pipeline/build_junior_data_js.py"
with open(junior_py, "r", encoding="utf-8") as f:
    content = f.read()

target = """    "2026-11-06": {
        "dateStr": "Friday November 6 2026",
        "editionLabel": "2026年11月6日 (金) 号 【本日・最新・全12記事】","""

replacement = """    "2026-11-09": {
        "dateStr": "Monday November 9 2026",
        "editionLabel": "2026年11月9日 (月) 号 【本日・最新・全12記事】",
        "tagline": "特集：エヌビディアCEO監視疑惑・負傷兵ドローン救出・中国BYD家宅捜索・効率性の罠・プレミア4-4死闘",
        "topLeadSlug": "nvidia-jensen-huang-investigation-foreign-intelligence-targeting",
        "subLeadSlugs": [
            "ukraine-drone-casualty-evacuation-frontline-medical-rescue",
            "chinese-carmaker-byd-offices-raided-netherlands-copycat-claim",
            "the-efficiency-trap-why-optimising-everything-can-backfire"
        ],
        "leftDispatches": [
            "ai-home-energy-optimisation-heating-bills-smart-thermostats",
            "trump-signals-hardline-pivot-following-midterm-election-setbacks",
            "israel-coalition-negotiations-eisenkot-netanyahu-allies",
            "abdul-el-sayed-public-health-epidemiology-politics"
        ],
        "rightDigestSlugs": [
            "cruise-ship-pianist-maritime-survival-nine-hours-open-ocean",
            "willie-nelson-reflections-on-longevity-country-music-memoir",
            "influencer-combat-sports-civil-disorder-dublin-ireland",
            "premier-league-thriller-manchester-united-aston-villa-dorgu"
        ]
    },
    "2026-11-06": {
        "dateStr": "Friday November 6 2026",
        "editionLabel": "2026年11月6日 (金) 号 【全12記事・アーカイブ】","""

if target in content:
    content = content.replace(target, replacement, 1)
    with open(junior_py, "w", encoding="utf-8") as f:
        f.write(content)
    print("Updated build_junior_data_js.py successfully!")
else:
    print("Target not found in build_junior_data_js.py!")
