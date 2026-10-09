# -*- coding: utf-8 -*-
"""
Builds Senior Times Broadsheet HTML for newly ingested articles:
- entertainment/smart-glasses-ai-privacy
- science/japan-semiconductor-revival-rapidus
- society/digital-school-backpack-reform
"""

import os
import sys

PIPELINE_DIR = os.path.dirname(os.path.abspath(__file__))
PORTAL_DIR = os.path.abspath(os.path.join(PIPELINE_DIR, ".."))
sys.path.append(PIPELINE_DIR)

from auto_ingest_articles import INGESTED_SENIOR_ARTICLES
from generate_all_articles import build_article_html

def build_senior_ingested_pages():
    for art in INGESTED_SENIOR_ARTICLES:
        cat = art["category"]
        slug = art["slug"]
        art_dir = os.path.join(PORTAL_DIR, cat, slug)
        os.makedirs(art_dir, exist_ok=True)
        
        # Normalize dictionary keys
        if "vocab" not in art and "vocabulary" in art:
            art["vocab"] = art["vocabulary"]
        if "pronunciation" not in art:
            art["pronunciation"] = [
                {"phrase": art["vocabulary"][0]["word"] + " の発音・アクセント", "meaning": f"標準発音記号: {art['vocabulary'][0]['phonetic']}"},
                {"phrase": art["vocabulary"][1]["word"] + " の発音・アクセント", "meaning": f"標準発音記号: {art['vocabulary'][1]['phonetic']}"}
            ]
            
        html_content = build_article_html(art)
        # Update relative paths and nav bar if needed
        target_path = os.path.join(art_dir, "index.html")
        with open(target_path, "w", encoding="utf-8") as f:
            f.write(html_content)
        print(f"[OK] Generated Senior Article: {cat}/{slug}/index.html")

if __name__ == "__main__":
    build_senior_ingested_pages()
