# -*- coding: utf-8 -*-
"""Update build_portal_data_js.py and build_junior_data_js.py with 2026-11-13..2026-11-16 editions."""

import os

PIPELINE_DIR = os.path.dirname(os.path.abspath(__file__))

NEW_EDITIONS = {
    "2026-11-16": {
        "dateStr": "Monday November 16 2026",
        "editionLabel": "2026年11月16日 (月) 号 【本日・最新・全12記事】",
        "tagline": "特集：ガザ冬期支援4カ国要請・GTA VI 13年ぶり発売・伊メタ社8.87億ユーロ制裁金・APEC/ASEAN首脳外交・偽CAPTCHA詐欺",
        "topLeadSlug": "australia-uk-canada-italy-urge-israel-critical-aid-gaza-winter-ntwnfb",
        "subLeadSlugs": [
            "grand-theft-auto-gta-vi-first-new-game-released-in-13-years",
            "italy-fines-meta-887m-for-accessing-android-users-photos-and-videos",
            "asia-diplomatic-summits-trump-xi-putin-apec-asean",
        ],
        "leftDispatches": [
            "captcha-scam-computer-malicious-software",
            "the-guardian-view-on-cop31-the-green-transition-must-not-be-derailed",
            "the-guardian-view-on-civil-service-reform-ai-cannot-conjure-a-capable-state-on-its-own",
            "gender-diverse-australian-sailors-barred-from-us-submarines-despite-aukus-deal-documents-reveal-ntwnfb",
        ],
        "rightDigestSlugs": [
            "us-judge-blocks-trumps-plan-to-renovate-historic-dc-golf-course",
            "vaccine-policy-rfk-jr-trump-administration",
            "stage-version-tv-series-its-a-sin-trailer",
            "philippines-carmelle-wins-first-eurovision-contest-in-asia",
        ],
    },
    "2026-11-15": {
        "dateStr": "Sunday November 15 2026",
        "editionLabel": "2026年11月15日 (日) 号 【全12記事・アーカイブ】",
        "tagline": "特集：スーパー・エルニーニョCOP31警告・韓国大学入試AI不正・プラハ報道自由デモ・ロヒンギャICJ審理・スコットランド天然カキ復活",
        "topLeadSlug": "el-nino-cop31-turkey-climate",
        "subLeadSlugs": [
            "ai-cheating-south-korea-college-entrance-exam",
            "czechia-protest-prague-media-freedom",
            "myanmar-rohingya-genocide-icj",
        ],
        "leftDispatches": [
            "ethnic-minorities-wales-police-facial-scans-data",
            "return-of-the-wild-oyster-conservationists-bring-shellfish-back-from-local-extinction-off-scottish-coast",
            "no-free-lunch-milburn-mcfadden-kuenssberg-uk-benefits-youth-unemployment-neet",
            "estonia-to-close-all-border-crossings-with-russia-after-attack-on-drone-maker",
        ],
        "rightDigestSlugs": [
            "women-pardoned-abortion-england-wales",
            "digital-finance-products-abuse-against-young-women-and-girls-report",
            "reclaiming-mary-cassatt-putting-overlooked-american-artist-back-at-heart-of-impressionism",
            "spain-england-nations-league-match-report",
        ],
    },
    "2026-11-14": {
        "dateStr": "Saturday November 14 2026",
        "editionLabel": "2026年11月14日 (土) 号 【全12記事・アーカイブ】",
        "tagline": "特集：新ヤルタ体制と米中露・SpaceXスターシップ同時回収・英国有機サーモン環境問題・スーダンドローン戦・AI文学界の衝撃",
        "topLeadSlug": "yalta-trump-xi-putin-china-apec",
        "subLeadSlugs": [
            "spacex-starship-double-catch",
            "salmon-organic-british-farmed-environmental-welfare",
            "ecuadorian-fishermen-lawsuit-trump-boat-strike",
        ],
        "leftDispatches": [
            "children-iengland-prescribed-weight-loss-jabs",
            "bristol-first-uk-wetland-city-flood",
            "nhs-england-62-day-cancer-treatment-target-by-10000-patients",
            "drones-redefining-warfare-sudan-massacring-civilians",
        ],
        "rightDigestSlugs": [
            "asylum-seekers-crowborough-torture-survivors-military-camp",
            "interest-rate-rises-inflation-bank-of-england-chief-economist",
            "its-like-the-wild-west-how-ai-has-rocked-the-literary-world",
            "u2-tickets-stubhub-bot-culture-secretary-resale",
        ],
    },
    "2026-11-13": {
        "dateStr": "Friday November 13 2026",
        "editionLabel": "2026年11月13日 (金) 号 【全12記事・アーカイブ】",
        "tagline": "特集：COP31電力時代と化石燃料・ゲーデル未発表ノートAI解読・ユークリッド宇宙望遠鏡9億銀河・薪ストーブ大気汚染・Microsoft障害",
        "topLeadSlug": "cop-31-electricity-energy-fossil-fuels-fatih-birol-iea",
        "subLeadSlugs": [
            "kurt-godel-notebooks-ai-helps-unlock-hidden-discoveries-man-who-transformed-maths",
            "iran-us-radar-bahrain-sirik-hormuz",
            "children-criminal-records-england-wales-labour",
        ],
        "leftDispatches": [
            "european-euclid-mission-reveals-900m-galaxies-secrets-dark-universe",
            "wood-burning-stoves-pollution-traffic-exhaust-children",
            "ai-uk-finance-jobs-bournemouth-tech",
            "storm-charles-floods-flight-cancellations-southern-europe-weather",
        ],
        "rightDigestSlugs": [
            "uk-ministers-look-at-quick-ways-to-limit-ndas-after-walliams-allegations",
            "how-microsoft-outage-has-affected-key-public-services-in-the-uk",
            "ireland-banned-books-room-censorship",
            "zimbabwean-author-simbarashe-kundizeza-cleared-ai-caine-prize-winning-story",
        ],
    },
}


def format_editions_block(indent: int) -> str:
    pad = " " * indent
    pad1 = " " * (indent + 4)
    pad2 = " " * (indent + 8)
    lines = []
    for date_key, cfg in NEW_EDITIONS.items():
        lines.append(f'{pad}"{date_key}": {{')
        lines.append(f'{pad1}"dateStr": "{cfg["dateStr"]}",')
        lines.append(f'{pad1}"editionLabel": "{cfg["editionLabel"]}",')
        lines.append(f'{pad1}"tagline": "{cfg["tagline"]}",')
        lines.append(f'{pad1}"topLeadSlug": "{cfg["topLeadSlug"]}",')
        for list_key in ["subLeadSlugs", "leftDispatches", "rightDigestSlugs"]:
            lines.append(f'{pad1}"{list_key}": [')
            items = cfg[list_key]
            for idx, slug in enumerate(items):
                comma = "," if idx < len(items) - 1 else ""
                lines.append(f'{pad2}"{slug}"{comma}')
            trailing = "," if list_key != "rightDigestSlugs" else ""
            lines.append(f'{pad1}]{trailing}')
        lines.append(f'{pad}}},')
    return "\n".join(lines)


def patch_file(filename: str, anchor: str, indent: int):
    path = os.path.join(PIPELINE_DIR, filename)
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    if '"2026-11-16":' in text:
        print(f"Skipping {filename}: 2026-11-16 already present.")
        return

    assert anchor in text, f"Anchor not found in {filename}"
    new_block = format_editions_block(indent)
    text = text.replace(anchor, f"{anchor}\n{new_block}", 1)
    text = text.replace(
        '"2026年11月12日 (木) 号 【本日・最新・全12記事】"',
        '"2026年11月12日 (木) 号 【全12記事・アーカイブ】"',
    )
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print(f"Updated {filename} successfully.")


if __name__ == "__main__":
    patch_file("build_portal_data_js.py", "    editions_dict = {", 8)
    patch_file("build_junior_data_js.py", "EDITIONS_DATA = {", 4)
