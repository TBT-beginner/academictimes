# -*- coding: utf-8 -*-
"""
Regenerates all article HTML pages (both Senior and Junior)
from updated ARTICLES and JUNIOR_ARTICLES datasets without re-synthesizing audio.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from articles_data import ARTICLES
from junior_articles_data import JUNIOR_ARTICLES
from generate_all_articles import build_article_html
from build_junior_site import build_junior_article_html

def regenerate_all():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    junior_base = os.path.join(base_dir, "junior")
    
    # 1. Senior Articles
    senior_count = 0
    for art in ARTICLES:
        slug = art["slug"]
        cat = art["category"]
        art_dir = os.path.join(base_dir, cat, slug)
        os.makedirs(art_dir, exist_ok=True)
        
        html_content = build_article_html(art)
        html_path = os.path.join(art_dir, "index.html")
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(html_content)
        senior_count += 1
    print(f"[OK] Regenerated {senior_count} Senior HTML articles.")

    # 2. Junior Articles
    junior_count = 0
    for art in JUNIOR_ARTICLES:
        slug = art["slug"]
        cat = art["category"]
        art_dir = os.path.join(junior_base, cat, slug)
        os.makedirs(art_dir, exist_ok=True)
        
        html_content = build_junior_article_html(art)
        html_path = os.path.join(art_dir, "index.html")
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(html_content)
        junior_count += 1
    print(f"[OK] Regenerated {junior_count} Junior HTML articles.")
    print(f"\nAll {senior_count} Senior and {junior_count} Junior HTML articles successfully regenerated!")

if __name__ == "__main__":
    regenerate_all()
