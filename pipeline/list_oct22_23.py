import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('pipeline/oct22_23_articles.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

print(f"Total: {len(items)}")
for i, it in enumerate(items[:60]):
    print(f"{i:2d}: [{it['pubDate'][:16]}] {it['title']}")
    print(f"    {it['link']}")
