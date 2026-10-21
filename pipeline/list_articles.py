import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('pipeline/oct21_22_articles.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

for i in range(15, 45):
    it = items[i]
    print(f"{i:2d}: [{it['pubDate'][:16]}] {it['title']}")
    print(f"    {it['link']}")
