import json

with open("news_portal/pipeline/candidates_oct28.json", "r", encoding="utf-8") as f:
    urls = json.load(f)

for idx, u in enumerate(sorted(urls)):
    print(f"{idx+1}: {u}")
