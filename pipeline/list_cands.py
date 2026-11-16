import json
d = json.load(open("news_portal/pipeline/nov13_16_candidates.json", encoding="utf-8"))
for i, x in enumerate(sorted(d, key=lambda r: (r["day"], r.get("section", "")))):
    print(f"{x['day']} | {x.get('section','?'):11s} | {x['slug']} | {x['title'][:68]}")
