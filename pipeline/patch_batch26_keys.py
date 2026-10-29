# -*- coding: utf-8 -*-
"""Patch missing source_name and headline_ja in Batch 26 files."""
import os

P1 = os.path.join(os.path.dirname(__file__), "data_batch26_part1.py")
JP1 = os.path.join(os.path.dirname(__file__), "data_batch26_junior_part1.py")
JP2 = os.path.join(os.path.dirname(__file__), "data_batch26_junior_part2.py")

# 1. Patch data_batch26_part1.py
with open(P1, "r", encoding="utf-8") as f:
    text = f.read()

target = '"slug": "queen-of-spain-butterfly-climate-migration-britain",'
replacement = '"slug": "queen-of-spain-butterfly-climate-migration-britain",\n        "source_name": "The Guardian",'

if '"source_name": "The Guardian"' not in text[text.find(target):text.find(target)+400]:
    text = text.replace(target, replacement, 1)
    with open(P1, "w", encoding="utf-8") as f:
        f.write(text)
    print("[OK] Patched source_name in data_batch26_part1.py")

# 2. Patch data_batch26_junior_part1.py
junior_headlines_p1 = {
    "africa-ebola-outbreak-global-surveillance-uk-health": "エボラ流行への警戒：世界の空港と医療の連携",
    "queen-of-spain-butterfly-climate-migration-britain": "英南部で熱帯性チョウが増加：温暖化と自然の変化",
    "us-electric-ferries-maritime-decarbonization-transit": "米西海岸で進む電動フェリー：海の脱炭素化",
    "uk-workers-right-to-know-pay-gender-disparities-ehrc": "職場の給与差をなくす新ルール：同僚の賃金開示案",
    "music-streaming-fatigue-cd-sales-revival-gen-z": "配信疲れからCDやレコードへ：Z世代が楽しむ実物音楽"
}

with open(JP1, "r", encoding="utf-8") as f:
    text = f.read()

for slug, hj in junior_headlines_p1.items():
    slug_target = f'"slug": "{slug}",'
    if slug_target in text:
        # Check if headline_ja is already in this dict
        idx = text.find(slug_target)
        next_dict = text.find('},\n    {', idx)
        if next_dict == -1: next_dict = text.find('}\n]', idx)
        snippet = text[idx:next_dict]
        if '"headline_ja":' not in snippet:
            text = text[:idx] + f'"slug": "{slug}",\n        "headline_ja": "{hj}",' + text[idx+len(slug_target):]
            print(f"[OK] Added headline_ja for {slug}")

with open(JP1, "w", encoding="utf-8") as f:
    f.write(text)

# 3. Patch data_batch26_junior_part2.py
junior_headlines_p2 = {
    "gulf-states-multipart-peace-deal-us-iran-tensions": "中東の緊張緩和へ：湾岸諸国による安全保障の新たな提案",
    "thames-water-emergency-debt-financing-insolvency-crisis": "英最大の水道会社が経営危機：巨額債務と市民の生活",
    "toblerone-trademark-shape-lawsuit-vegan-chocolate": "トブラローネがヴィーガンチョコを提訴：伝統の三角錐の形をめぐって",
    "datacenter-acoustic-pollution-lawsuit-mississippi": "AIデータセンターの騒音問題：米ミシシッピ州で住民が提訴",
    "gullivers-travels-tercentenary-satire-modern-relevance": "『ガリヴァー旅行記』出版300周年：現代社会を風刺する名作",
    "doordash-instacart-grocery-delivery-merger-antitrust": "フード配達大手の統合計画：米巨大企業の合併と独占への懸念"
}

with open(JP2, "r", encoding="utf-8") as f:
    text = f.read()

for slug, hj in junior_headlines_p2.items():
    slug_target = f'"slug": "{slug}",'
    if slug_target in text:
        idx = text.find(slug_target)
        next_dict = text.find('},\n    {', idx)
        if next_dict == -1: next_dict = text.find('}\n]', idx)
        snippet = text[idx:next_dict]
        if '"headline_ja":' not in snippet:
            text = text[:idx] + f'"slug": "{slug}",\n        "headline_ja": "{hj}",' + text[idx+len(slug_target):]
            print(f"[OK] Added headline_ja for {slug}")

with open(JP2, "w", encoding="utf-8") as f:
    f.write(text)
print("Done patching.")
