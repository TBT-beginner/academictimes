import json

with open("js/portal-data.js", "r", encoding="utf-8") as f:
    txt = f.read()

# Parse ARTICLES
start = txt.find("const ARTICLES = ") + len("const ARTICLES = ")
end = txt.find("const EDITIONS = ")
# or just run node to get articles data
import subprocess
out = subprocess.check_output(['node', '-e', """
const fs = require('fs');
const code = fs.readFileSync('js/portal-data.js', 'utf8');
eval(code.replace(/const /g, 'global.'));
console.log(JSON.stringify(global.ARTICLES.map(a => ({
  date: a.date,
  slug: a.slug,
  category: a.category,
  title: a.title,
  source_name: a.source_name,
  source_url: a.source_url
}))));
"""], encoding='utf-8')

arts = json.loads(out)
print(f"Total articles: {len(arts)}")
for idx, a in enumerate(arts):
    # Flag if URL has 2024 or earlier, or academic papers
    is_paper = "nature.com" in a['source_url'] or "science.org" in a['source_url'] or "doi" in a['source_url']
    has_year = any(y in a['source_url'] for y in ["2022", "2023", "2024", "2025"])
    if is_paper or has_year:
        print(f"[{a['date']}] {a['category']} | {a['slug']}")
        print(f"   Source: {a['source_name']} -> {a['source_url']}")
