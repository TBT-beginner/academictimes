# -*- coding: utf-8 -*-
"""
Regenerates all article HTML pages from updated ARTICLES in articles_data.py
without re-synthesizing existing audio files.
"""
import os
import sys

sys.path.append(os.path.dirname(__file__))
from articles_data import ARTICLES
from generate_all_articles import build_article_html

def regenerate_all():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    
    count = 0
    for art in ARTICLES:
        slug = art["slug"]
        cat = art["category"]
        art_dir = os.path.join(base_dir, cat, slug)
        os.makedirs(art_dir, exist_ok=True)
        
        html_content = build_article_html(art)
        html_path = os.path.join(art_dir, "index.html")
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(html_content)
        
        quiz_count = len(art.get("quiz", []))
        print(f"[OK] Generated {cat}/{slug}/index.html ({quiz_count} quiz questions)")
        count += 1
        
    print(f"\nAll {count} articles successfully updated with full 3-question quizzes!")

if __name__ == "__main__":
    regenerate_all()
