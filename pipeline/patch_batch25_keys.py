# -*- coding: utf-8 -*-
import sys

HEADLINES = {
    "uk-sizewell-nuclear-plant-deal-taxpayer-mps-warning": "英サイズウェルC原発計画、巨額の国民負担に議員団が強い懸念表明",
    "venice-lagoon-rising-seas-dry-land-submergence": "堆積物コア分析で解明：古代の陸地が海面上昇でヴェネツィア潟に変貌",
    "uk-homes-low-interest-loans-solar-heat-pumps": "英政府、太陽光パネル・ヒートポンプ導入支援で無利子ローン制度を発表",
    "ferritin-face-social-media-claims-iron-deficiency-risks": "「フェリチン・フェイス」の俗説に医師警告：検査なしの鉄分過剰摂取にリスク",
    "uk-emergency-stockpile-advice-bottled-water-food-surge": "英政府の緊急備蓄アドバイスを受け、ミネラルウォーターと缶詰の売上が急増",
    "gen-z-digital-detox-apps-dumbphones-screen-time": "Z世代に広がる「ガラケー回帰」：中毒的アルゴリズムに対抗するデジタルデトックス",
    "spain-high-speed-train-crash-investigation-toledo": "スペイン・トレド近郊で高速列車衝突：数十人負傷、信号システムの検証へ",
    "israel-election-results-netanyahu-eisenkot-deadlock": "イスラエル総選挙の出口調査：ネタニヤフ陣営と野党が互角、政局膠着へ",
    "king-charles-commonwealth-summit-slavery-legacy-reparations": "チャールズ国王、サモアの英連邦首脳会議で大西洋奴隷貿易の歴史的遺産に言及",
    "bafta-trustees-charity-law-free-guest-tickets-scrutiny": "英国映画賞Baftaの理事ら、VIPチケット受領で慈善事業委員会が調査へ",
    "rolling-stones-charlie-watts-letter-brian-jones-auction": "チャーリー・ワッツの未公開直筆書簡が出品へ：ブライアン・ジョーンズの死への苦悩",
    "bluey-copyright-dispute-abc-australia-one-nation-cartoon": "豪公共放送ABC、政党が人気アニメ『ブルーイ』を政治宣伝に無断流用したとして提訴"
}

IMAGES = {
    "science": "https://images.unsplash.com/photo-1507668077129-56e32842fceb?w=1000&auto=format&fit=crop&q=80",
    "environment": "https://images.unsplash.com/photo-1470071459604-3b5ec3a7fe05?w=1000&auto=format&fit=crop&q=80",
    "society": "https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=1000&auto=format&fit=crop&q=80",
    "world": "https://images.unsplash.com/photo-1526304640581-d334cdbbf45e?w=1000&auto=format&fit=crop&q=80",
    "law": "https://images.unsplash.com/photo-1589829545856-d10d557cf95f?w=1000&auto=format&fit=crop&q=80",
    "culture": "https://images.unsplash.com/photo-1457369804613-52c61a468e7d?w=1000&auto=format&fit=crop&q=80",
    "entertainment": "https://images.unsplash.com/photo-1511512578047-dfb367046420?w=1000&auto=format&fit=crop&q=80"
}

import data_batch25_part1
import data_batch25_part2
import data_batch25_junior_part1
import data_batch25_junior_part2

for part in [data_batch25_part1.SENIOR_PART1, data_batch25_part2.SENIOR_PART2, data_batch25_junior_part1.JUNIOR_PART1, data_batch25_junior_part2.JUNIOR_PART2]:
    for art in part:
        slug = art["slug"]
        cat = art["category"]
        if not art.get("headline_ja"):
            art["headline_ja"] = HEADLINES.get(slug, art.get("title", ""))
        if not art.get("subhead"):
            art["subhead"] = art.get("lead_ja", "")
        if not art.get("lead_snippet"):
            art["lead_snippet"] = art.get("lead_ja", "")
        if not art.get("source_attribution"):
            art["source_attribution"] = "The Guardian (Oct 28, 2026)"
        if not art.get("image"):
            art["image"] = IMAGES.get(cat, IMAGES["world"])

# Now re-serialize files cleanly
import pprint

def save_part(path, var_name, data):
    with open(path, "w", encoding="utf-8") as f:
        f.write("# -*- coding: utf-8 -*-\n")
        f.write(f'"""Batch 25 Data: {var_name}"""\n\n')
        f.write(f"{var_name} = ")
        f.write(pprint.pformat(data, indent=4, width=120, sort_dicts=False))
        f.write("\n")
    print(f"Saved {path}")

save_part("news_portal/pipeline/data_batch25_part1.py", "SENIOR_PART1", data_batch25_part1.SENIOR_PART1)
save_part("news_portal/pipeline/data_batch25_part2.py", "SENIOR_PART2", data_batch25_part2.SENIOR_PART2)
save_part("news_portal/pipeline/data_batch25_junior_part1.py", "JUNIOR_PART1", data_batch25_junior_part1.JUNIOR_PART1)
save_part("news_portal/pipeline/data_batch25_junior_part2.py", "JUNIOR_PART2", data_batch25_junior_part2.JUNIOR_PART2)
