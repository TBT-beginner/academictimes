# -*- coding: utf-8 -*-
"""Update build_portal_data_js.py and build_junior_data_js.py for 2026-11-12"""

portal_py = "news_portal/pipeline/build_portal_data_js.py"
with open(portal_py, "r", encoding="utf-8") as f:
    p_content = f.read()

p_target = """        "2026-11-10": {
            "dateStr": "Tuesday November 10 2026",
            "editionLabel": "2026年11月10日 (火) 号 【本日・最新・全12記事】","""

p_replacement = """        "2026-11-12": {
            "dateStr": "Thursday November 12 2026",
            "editionLabel": "2026年11月12日 (木) 号 【本日・最新・全12記事】",
            "tagline": "特集：大学課題AI採点の限界・沈みゆく環礁国COP直訴・スペイン家賃ゼネスト・サウジ鞭打ち判決・車椅子2年待ち危機",
            "topLeadSlug": "ai-close-to-impossible-assess-university-coursework-regulator",
            "subLeadSlugs": [
                "the-world-we-know-is-over-marshall-islands-president-cop31",
                "spain-general-strike-housing-costs",
                "woman-in-saudi-arabia-sentenced-to-100-lashes-for-giving-birth-outside-marriage"
            ],
            "leftDispatches": [
                "one-flowered-wintergreen-rescue-eroding-coast-scotland",
                "tories-raise-state-pension-age-70-triple-lock-torsten-bell",
                "disabled-people-in-england-have-to-wait-up-to-two-years-for-wheelchairs",
                "bank-of-england-inflation-response-risks-higher-interest-rates-for-longer"
            ],
            "rightDigestSlugs": [
                "democrats-hegseth-impeachment-vote",
                "russell-brand-david-walliams-noughties-culture-girls-women",
                "aldi-cuts-hundreds-of-uk-head-office-and-logistics-roles-global-cost-trimming",
                "mini-record-player-on-track-for-no-1-in-christmas-toy-parade"
            ]
        },
        "2026-11-10": {
            "dateStr": "Tuesday November 10 2026",
            "editionLabel": "2026年11月10日 (火) 号 【全12記事・アーカイブ】","""

if p_target in p_content:
    p_content = p_content.replace(p_target, p_replacement, 1)
    with open(portal_py, "w", encoding="utf-8") as f:
        f.write(p_content)
    print("Updated build_portal_data_js.py successfully!")
else:
    print("Target not found in build_portal_data_js.py!")

junior_py = "news_portal/pipeline/build_junior_data_js.py"
with open(junior_py, "r", encoding="utf-8") as f:
    j_content = f.read()

j_target = """    "2026-11-10": {
        "dateStr": "Tuesday November 10 2026",
        "editionLabel": "2026年11月10日 (火) 号 【本日・最新・全12記事】","""

j_replacement = """    "2026-11-12": {
        "dateStr": "Thursday November 12 2026",
        "editionLabel": "2026年11月12日 (木) 号 【本日・最新・全12記事】",
        "tagline": "特集：大学課題AI採点の限界・沈みゆく環礁国COP直訴・スペイン家賃ゼネスト・サウジ鞭打ち判決・車椅子2年待ち危機",
        "topLeadSlug": "ai-close-to-impossible-assess-university-coursework-regulator",
        "subLeadSlugs": [
            "the-world-we-know-is-over-marshall-islands-president-cop31",
            "spain-general-strike-housing-costs",
            "woman-in-saudi-arabia-sentenced-to-100-lashes-for-giving-birth-outside-marriage"
        ],
        "leftDispatches": [
            "one-flowered-wintergreen-rescue-eroding-coast-scotland",
            "tories-raise-state-pension-age-70-triple-lock-torsten-bell",
            "disabled-people-in-england-have-to-wait-up-to-two-years-for-wheelchairs",
            "bank-of-england-inflation-response-risks-higher-interest-rates-for-longer"
        ],
        "rightDigestSlugs": [
            "democrats-hegseth-impeachment-vote",
            "russell-brand-david-walliams-noughties-culture-girls-women",
            "aldi-cuts-hundreds-of-uk-head-office-and-logistics-roles-global-cost-trimming",
            "mini-record-player-on-track-for-no-1-in-christmas-toy-parade"
        ]
    },
    "2026-11-10": {
        "dateStr": "Tuesday November 10 2026",
        "editionLabel": "2026年11月10日 (火) 号 【全12記事・アーカイブ】","""

if j_target in j_content:
    j_content = j_content.replace(j_target, j_replacement, 1)
    with open(junior_py, "w", encoding="utf-8") as f:
        f.write(j_content)
    print("Updated build_junior_data_js.py successfully!")
else:
    print("Target not found in build_junior_data_js.py!")
