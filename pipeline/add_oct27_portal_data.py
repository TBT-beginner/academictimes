# -*- coding: utf-8 -*-
with open("news_portal/pipeline/build_portal_data_js.py", "r", encoding="utf-8") as f:
    text = f.read()

target = '''    editions_dict = {
        "2026-10-26": {'''

addition = '''    editions_dict = {
        "2026-10-27": {
            "dateStr": "Tuesday October 27 2026",
            "editionLabel": "2026年10月27日 (火) 号 【本日付・最新・全12記事】",
            "tagline": "特集：iPhone Duo折りたたみ画面亀裂・ボルソナロ旅券没収・ネタニヤフ先制圧力・中世タペストリー熱狂・南アブドウ園歴史復権",
            "topLeadSlug": "iphone-duo-foldable-handset-display-cracks-hardware",
            "subLeadSlugs": [
                "brazil-supreme-court-flavio-bolsonaro-passport-seizure",
                "israel-netanyahu-military-pressure-iran-election-strategy",
                "bayeux-tapestry-british-museum-youth-culture-pop-hit"
            ],
            "leftDispatches": [
                "stage-michael-gambon-biography-pranks-theatrical-craft",
                "south-africa-vineyards-slavery-legacy-land-reclamation",
                "uk-apprenticeship-funding-overhaul-youth-jobs-crisis-neet",
                "uk-foreign-aid-budget-shortfall-gni-target-missed"
            ],
            "rightDigestSlugs": [
                "astronomy-starwatch-pegasus-great-square-celestial-navigation",
                "england-ethnic-minorities-breast-cancer-screening-disparities",
                "manchester-burnham-homelessness-funding-rough-sleeping-budget",
                "france-macron-vandals-pay-law-protest-rights-democracy"
            ]
        },
        "2026-10-26": {'''

norm_text = text.replace("\r\n", "\n")
norm_target = target.replace("\r\n", "\n")
norm_addition = addition.replace("\r\n", "\n")

assert norm_target in norm_text, "target not found in build_portal_data_js.py"
new_text = norm_text.replace(norm_target, norm_addition, 1)

# Also update 2026-10-26 editionLabel to be archive
new_text = new_text.replace(
    '"editionLabel": "2026年10月26日 (月) 号 【本日付・最新・全12記事】"',
    '"editionLabel": "2026年10月26日 (月) 号 【全12記事・アーカイブ】"'
)

with open("news_portal/pipeline/build_portal_data_js.py", "w", encoding="utf-8", newline="\n") as f:
    f.write(new_text)

print("Successfully added 2026-10-27 to build_portal_data_js.py")
