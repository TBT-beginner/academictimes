# -*- coding: utf-8 -*-
"""Update build_portal_data_js.py and build_junior_data_js.py for 2026-11-10"""

portal_py = "news_portal/pipeline/build_portal_data_js.py"
with open(portal_py, "r", encoding="utf-8") as f:
    p_content = f.read()

p_target = """        "2026-11-09": {
            "dateStr": "Monday November 9 2026",
            "editionLabel": "2026年11月9日 (月) 号 【本日・最新・全12記事】","""

p_replacement = """        "2026-11-10": {
            "dateStr": "Tuesday November 10 2026",
            "editionLabel": "2026年11月10日 (火) 号 【本日・最新・全12記事】",
            "tagline": "特集：スティッフパーソン症候群新薬・英再エネ増税駆け込み・国防長官弾劾決議・露軍戦死データ・光害市民科学",
            "topLeadSlug": "medical-breakthrough-offers-hope-to-people-with-same-stiff-person-syndrome-as-celine-dion",
            "subLeadSlugs": [
                "uk-households-green-energy-installer-rush-april-vat-hike",
                "pete-hegseth-impeachment-thomas-massie",
                "russians-killed-ukraine-war-leaked-data"
            ],
            "leftDispatches": [
                "starwatch-count-stars-find-out-how-dark-sky-is",
                "burnham-homelessness-pledge-rough-sleeping-england",
                "uk-young-people-job-work-employment-crisis-paul-nowak-milburn-review",
                "donald-trump-humiliated-angry-europe"
            ],
            "rightDigestSlugs": [
                "russell-brand-sentenced-rape-sexual-assault",
                "judo-star-teddy-riner-plan-france-presidential-election",
                "u2-carnaval-de-luz-review",
                "nvidia-jensen-huang-affair-trump-musk"
            ]
        },
        "2026-11-09": {
            "dateStr": "Monday November 9 2026",
            "editionLabel": "2026年11月9日 (月) 号 【全12記事・アーカイブ】","""

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

j_target = """    "2026-11-09": {
        "dateStr": "Monday November 9 2026",
        "editionLabel": "2026年11月9日 (月) 号 【本日・最新・全12記事】","""

j_replacement = """    "2026-11-10": {
        "dateStr": "Tuesday November 10 2026",
        "editionLabel": "2026年11月10日 (火) 号 【本日・最新・全12記事】",
        "tagline": "特集：スティッフパーソン症候群新薬・英再エネ増税駆け込み・国防長官弾劾決議・露軍戦死データ・光害市民科学",
        "topLeadSlug": "medical-breakthrough-offers-hope-to-people-with-same-stiff-person-syndrome-as-celine-dion",
        "subLeadSlugs": [
            "uk-households-green-energy-installer-rush-april-vat-hike",
            "pete-hegseth-impeachment-thomas-massie",
            "russians-killed-ukraine-war-leaked-data"
        ],
        "leftDispatches": [
            "starwatch-count-stars-find-out-how-dark-sky-is",
            "burnham-homelessness-pledge-rough-sleeping-england",
            "uk-young-people-job-work-employment-crisis-paul-nowak-milburn-review",
            "donald-trump-humiliated-angry-europe"
        ],
        "rightDigestSlugs": [
            "russell-brand-sentenced-rape-sexual-assault",
            "judo-star-teddy-riner-plan-france-presidential-election",
            "u2-carnaval-de-luz-review",
            "nvidia-jensen-huang-affair-trump-musk"
        ]
    },
    "2026-11-09": {
        "dateStr": "Monday November 9 2026",
        "editionLabel": "2026年11月9日 (月) 号 【全12記事・アーカイブ】","""

if j_target in j_content:
    j_content = j_content.replace(j_target, j_replacement, 1)
    with open(junior_py, "w", encoding="utf-8") as f:
        f.write(j_content)
    print("Updated build_junior_data_js.py successfully!")
else:
    print("Target not found in build_junior_data_js.py!")
