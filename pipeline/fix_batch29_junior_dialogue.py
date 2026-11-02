# -*- coding: utf-8 -*-
"""Ensure dialogue in Batch 29 Junior has dialogue key and name/role/speaker keys."""

for fname in ['news_portal/pipeline/data_batch29_junior_part1.py', 'news_portal/pipeline/data_batch29_junior_part2.py']:
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace key
    content = content.replace('"dialog":', '"dialogue":')
    
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {fname}")

# Now load and enrich dialogue objects with name and role
import sys, os
sys.path.insert(0, 'news_portal/pipeline')
import data_batch29_junior_part1
import data_batch29_junior_part2
import json

def enrich(articles):
    for art in articles:
        dlgs = art.get("dialogue", [])
        for d in dlgs:
            spk = d.get("speaker", "")
            if "keita" in spk.lower() or "慶" in spk:
                d["name"] = "Keita先生"
                d["role"] = "英語講師"
                d["speaker"] = "Keita先生"
            else:
                d["name"] = "Nanami"
                d["role"] = "生徒・アシスタント"
                d["speaker"] = "Nanami"
    return articles

p1 = enrich(data_batch29_junior_part1.JUNIOR_PART1)
p2 = enrich(data_batch29_junior_part2.JUNIOR_PART2)

with open('news_portal/pipeline/data_batch29_junior_part1.py', 'w', encoding='utf-8') as f:
    f.write('# -*- coding: utf-8 -*-\n"""Batch 29 Part 1: Articles 1-6 (Junior) Date: 2026-11-02"""\n\nJUNIOR_PART1 = ')
    f.write(json.dumps(p1, ensure_ascii=False, indent=4))
    f.write('\n\n__all__ = ["JUNIOR_PART1"]\n')

with open('news_portal/pipeline/data_batch29_junior_part2.py', 'w', encoding='utf-8') as f:
    f.write('# -*- coding: utf-8 -*-\n"""Batch 29 Part 2: Articles 7-12 (Junior) Date: 2026-11-02"""\n\nJUNIOR_PART2 = ')
    f.write(json.dumps(p2, ensure_ascii=False, indent=4))
    f.write('\n\n__all__ = ["JUNIOR_PART2"]\n')

print("Batch 29 Junior files enriched successfully!")
