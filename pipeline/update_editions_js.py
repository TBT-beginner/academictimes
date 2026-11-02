# -*- coding: utf-8 -*-
"""Update build_portal_data_js.py and build_junior_data_js.py with 2026-10-31, 2026-11-01, 2026-11-02 editions."""

import re

new_portal_editions = '''    editions_dict = {
        "2026-11-02": {
            "dateStr": "Monday November 2 2026",
            "editionLabel": "2026年11月2日 (月) 号 【本日・最新・全12記事】",
            "tagline": "特集：半世紀ぶりツチハンミョウ再発見・巨額AI投資への市場懸念・北欧データセンター森林伐採捜査・ロンドン自動運転規制",
            "topLeadSlug": "rare-short-necked-oil-beetle-rediscovered-wales",
            "subLeadSlugs": [
                "tech-stocks-drop-earnings-report",
                "finland-criminal-investigation-google-clearing-forest-datacentre",
                "sadiq-khan-calls-cap-numbers-robotaxis-london-streets"
            ],
            "leftDispatches": [
                "indonesia-protests-fire-haze-economy",
                "chancellor-fails-to-guarantee-minimum-wage-pledge-younger-workers-kuenssberg",
                "investors-take-out-36bn-from-binance-after-record-hack-that-stole-billions",
                "uk-willing-to-spend-450m-a-year-on-eu-students-if-it-can-join-made-in-europe-scheme"
            ],
            "rightDigestSlugs": [
                "police-detain-325-people-at-pro-palestine-action-protest-at-us-embassy-in-london",
                "home-secretary-shabana-mahmood-immigration-leave-to-remain-windrush",
                "bedouin-women-success-arab-parties-israel-election",
                "hello-kitty-japanese-spy-show-vivant-china-outcry"
            ]
        },
        "2026-11-01": {
            "dateStr": "Sunday November 1 2026",
            "editionLabel": "2026年11月1日 (日) 号 【全12記事・アーカイブ】",
            "tagline": "特集：野鳥共生農法の大成功・野生動植物取引の実態暴落・ギリシャトルコ大洪水警報・英水質汚染深刻化",
            "topLeadSlug": "this-is-a-robust-recipe-the-experimental-farm-bucking-the-decline-in-uk-birds",
            "subLeadSlugs": [
                "twice-as-many-plants-and-animals-sold-in-wildlife-trade-as-previously-thought-says-report",
                "severe-rainfall-flood-warnings-greece-turkey",
                "ministers-water-bosses-report-performance-worse"
            ],
            "leftDispatches": [
                "fireworks-uk-consultation-campaigners-noise-animal-welfare",
                "poundland-brink-administration-12000-jobs-at-risk",
                "binance-crypto-exchange-hack",
                "how-did-the-spain-train-crash-happen-what-will-investigators-be-asking"
            ],
            "rightDigestSlugs": [
                "erin-patterson-mushroom-murders-appeal-ruling-ntwnfb",
                "mercury-lead-methanol-counterfeit-beauty-products-seized-uk",
                "john-smedley-knitwear-brand-innovating-fashion-tradition-tough-market-manufacturing",
                "basketweavers-get-in-a-twist-over-alexander-skarsgard-wicker-husband"
            ]
        },
        "2026-10-31": {
            "dateStr": "Saturday October 31 2026",
            "editionLabel": "2026年10月31日 (土) 号 【全12記事・アーカイブ】",
            "tagline": "特集：英肥満対策破綻警告・ネット女性蔑視の公衆衛生危機・緑の前庭と猛暑緩和・英豪雨貯水池渇水・スロット賭博税制",
            "topLeadSlug": "uk-government-obesity-plan-doomed-mps-warn",
            "subLeadSlugs": [
                "manosphere-online-misogyny-public-health-policy-lancet-report",
                "greener-front-gardens-air-pollution-summer-heat",
                "shell-profits-double-iran-war-pushes-up-profit-margin-on-oil"
            ],
            "leftDispatches": [
                "haywards-heath-ardingly-reservoir-water-level-drought-england",
                "inside-the-slot-farms-targeted-in-budget-gambling",
                "tuc-leader-union-recognition-private-sector",
                "jd-vance-letter-may-offer-last-chance-to-avert-fresh-conflict-between-us-and-iran"
            ],
            "rightDigestSlugs": [
                "metropolitan-police-refers-itself-to-watchdog-over-meghan-warning-letter",
                "albania-protest-attendance-fine-law",
                "rare-love-letters-french-aristocrat-la-perouse-maritime-mystery",
                "bryan-adams-donald-trump-song"
            ]
        },
        "2026-10-30": {
            "dateStr": "Friday October 30 2026",
            "editionLabel": "2026年10月30日 (金) 号 【全12記事・アーカイブ】",'''

with open("news_portal/pipeline/build_portal_data_js.py", "r", encoding="utf-8") as f:
    portal_code = f.read()

portal_target = re.compile(r'    editions_dict = \{\s*"2026-10-30": \{\s*"dateStr": "Friday October 30 2026",\s*"editionLabel": "[^"]+",')
if portal_target.search(portal_code):
    portal_code = portal_target.sub(new_portal_editions, portal_code, count=1)
    with open("news_portal/pipeline/build_portal_data_js.py", "w", encoding="utf-8") as f:
        f.write(portal_code)
    print("Updated build_portal_data_js.py successfully.")
else:
    print("Could not find pattern in build_portal_data_js.py")

new_junior_editions = '''EDITIONS_DATA = {
    "2026-11-02": {
        "dateStr": "Monday November 2 2026",
        "editionLabel": "2026年11月2日 (月) 号 【本日・最新・全12記事】",
        "tagline": "特集：半世紀ぶりツチハンミョウ再発見・巨額AI投資への懸念・北欧データセンター森林伐採・ロンドン自動運転タクシー規制",
        "topLeadSlug": "rare-short-necked-oil-beetle-rediscovered-wales",
        "subLeadSlugs": [
            "tech-stocks-drop-earnings-report",
            "finland-criminal-investigation-google-clearing-forest-datacentre",
            "sadiq-khan-calls-cap-numbers-robotaxis-london-streets"
        ],
        "leftDispatches": [
            "indonesia-protests-fire-haze-economy",
            "chancellor-fails-to-guarantee-minimum-wage-pledge-younger-workers-kuenssberg",
            "investors-take-out-36bn-from-binance-after-record-hack-that-stole-billions",
            "uk-willing-to-spend-450m-a-year-on-eu-students-if-it-can-join-made-in-europe-scheme"
        ],
        "rightDigestSlugs": [
            "police-detain-325-people-at-pro-palestine-action-protest-at-us-embassy-in-london",
            "home-secretary-shabana-mahmood-immigration-leave-to-remain-windrush",
            "bedouin-women-success-arab-parties-israel-election",
            "hello-kitty-japanese-spy-show-vivant-china-outcry"
        ]
    },
    "2026-11-01": {
        "dateStr": "Sunday November 1 2026",
        "editionLabel": "2026年11月1日 (日) 号 【全12記事・アーカイブ】",
        "tagline": "特集：野鳥共生農法の大成功・野生動植物取引の実態・ギリシャトルコ大洪水警報・英水質汚染深刻化",
        "topLeadSlug": "this-is-a-robust-recipe-the-experimental-farm-bucking-the-decline-in-uk-birds",
        "subLeadSlugs": [
            "twice-as-many-plants-and-animals-sold-in-wildlife-trade-as-previously-thought-says-report",
            "severe-rainfall-flood-warnings-greece-turkey",
            "ministers-water-bosses-report-performance-worse"
        ],
        "leftDispatches": [
            "fireworks-uk-consultation-campaigners-noise-animal-welfare",
            "poundland-brink-administration-12000-jobs-at-risk",
            "binance-crypto-exchange-hack",
            "how-did-the-spain-train-crash-happen-what-will-investigators-be-asking"
        ],
        "rightDigestSlugs": [
            "erin-patterson-mushroom-murders-appeal-ruling-ntwnfb",
            "mercury-lead-methanol-counterfeit-beauty-products-seized-uk",
            "john-smedley-knitwear-brand-innovating-fashion-tradition-tough-market-manufacturing",
            "basketweavers-get-in-a-twist-over-alexander-skarsgard-wicker-husband"
        ]
    },
    "2026-10-31": {
        "dateStr": "Saturday October 31 2026",
        "editionLabel": "2026年10月31日 (土) 号 【全12記事・アーカイブ】",
        "tagline": "特集：英肥満対策破綻警告・ネット女性蔑視の公衆衛生危機・緑の前庭と猛暑緩和・英豪雨貯水池渇水・スロット賭博税制",
        "topLeadSlug": "uk-government-obesity-plan-doomed-mps-warn",
        "subLeadSlugs": [
            "manosphere-online-misogyny-public-health-policy-lancet-report",
            "greener-front-gardens-air-pollution-summer-heat",
            "shell-profits-double-iran-war-pushes-up-profit-margin-on-oil"
        ],
        "leftDispatches": [
            "haywards-heath-ardingly-reservoir-water-level-drought-england",
            "inside-the-slot-farms-targeted-in-budget-gambling",
            "tuc-leader-union-recognition-private-sector",
            "jd-vance-letter-may-offer-last-chance-to-avert-fresh-conflict-between-us-and-iran"
        ],
        "rightDigestSlugs": [
            "metropolitan-police-refers-itself-to-watchdog-over-meghan-warning-letter",
            "albania-protest-attendance-fine-law",
            "rare-love-letters-french-aristocrat-la-perouse-maritime-mystery",
            "bryan-adams-donald-trump-song"
        ]
    },
    "2026-10-30": {
        "dateStr": "Friday October 30 2026",
        "editionLabel": "2026年10月30日 (金) 号 【全12記事・アーカイブ】",'''

with open("news_portal/pipeline/build_junior_data_js.py", "r", encoding="utf-8") as f:
    junior_code = f.read()

junior_target = re.compile(r'EDITIONS_DATA = \{\s*"2026-10-30": \{\s*"dateStr": "Friday October 30 2026",\s*"editionLabel": "[^"]+",')
if junior_target.search(junior_code):
    junior_code = junior_target.sub(new_junior_editions, junior_code, count=1)
    with open("news_portal/pipeline/build_junior_data_js.py", "w", encoding="utf-8") as f:
        f.write(junior_code)
    print("Updated build_junior_data_js.py successfully.")
else:
    print("Could not find pattern in build_junior_data_js.py")
