# -*- coding: utf-8 -*-
with open("news_portal/pipeline/articles_data.py", "r", encoding="utf-8") as f:
    text = f.read()

lines = text.split("\n")
for idx, l in enumerate(lines):
    if "data_batch" in l or "batch" in l.lower():
        print(f"Line {idx+1}: {l.strip()[:100]}")
