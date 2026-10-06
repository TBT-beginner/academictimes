# -*- coding: utf-8 -*-
"""
Injects reciprocal bidirectional links to THE JUNIOR into all 15 Senior Academic Times articles:
1. Top date bar link
2. Hero header switcher banner (prominent, accessible green)
3. Navigation bar item
4. Bottom study recommendation banner
"""

import os
import re
from junior_articles_data import JUNIOR_ARTICLES

PORTAL_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

def link_senior_articles():
    success_count = 0
    
    for art in JUNIOR_ARTICLES:
        cat = art["category"]
        slug = art["slug"]
        senior_path = os.path.join(PORTAL_DIR, cat, slug, "index.html")
        
        if not os.path.exists(senior_path):
            print(f"[WARN] Senior file not found: {senior_path}")
            continue
            
        with open(senior_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        junior_url = f"../../junior/{cat}/{slug}/index.html"
        
        # 1. Check if already has junior banner
        if "junior-edition-banner" in content:
            print(f"[SKIP] Already linked: {cat}/{slug}")
            continue
            
        # Banner HTML
        hero_banner = f"""
          <!-- JUNIOR EDITION SWITCHER BANNER -->
          <div class="junior-edition-banner" style="margin: 1.25rem 0 0.75rem; padding: 0.85rem 1.15rem; background: #eef5f0; border-left: 4px solid #235937; border-radius: 4px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 0.75rem;">
            <div>
              <span style="background: #235937; color: #fff; font-size: 0.72rem; font-weight: 700; padding: 0.2rem 0.5rem; letter-spacing: 0.05em; border-radius: 2px;">THE JUNIOR</span>
              <strong style="color: #143820; font-size: 0.88rem; margin-left: 0.5rem;">高校1〜2年・英検準2級〜2級レベルで読む</strong>
              <div style="font-size: 0.78rem; color: #2d5a3c; margin-top: 0.25rem;">
                この記事をやさしい英文（CEFR A2〜B1）と標準速度の朗読音声（-10%速度）で読める『THE JUNIOR版』が開けます。
              </div>
            </div>
            <div>
              <a href="{junior_url}" style="display: inline-block; background: #235937; color: #ffffff !important; font-size: 0.82rem; font-weight: 700; padding: 0.45rem 0.95rem; text-decoration: none; border-radius: 3px; box-shadow: 0 1px 3px rgba(0,0,0,0.12); white-space: nowrap;">
                🌱 Junior版でこの記事を読む ↗
              </a>
            </div>
          </div>
"""

        bottom_banner = f"""
      <!-- JUNIOR STEP-DOWN RECOMMENDATION BANNER -->
      <div style="margin: 2.5rem 0 1.5rem; padding: 1.25rem; background: #f4f8f5; border: 1px solid #d0e4d6; border-radius: 4px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem;">
        <div>
          <div style="font-family: var(--font-headline); font-size: 1rem; font-weight: 700; color: #143820; margin-bottom: 0.25rem;">
            🌱 『THE JUNIOR』でもう一度基礎を固める
          </div>
          <p style="font-size: 0.8rem; color: #2d5a3c; margin: 0; line-height: 1.5;">
            難関大レベルの構文や語彙が難しく感じられた場合は、同じトピックを英検準2級〜2級レベルの基礎英語で再構成したJunior版をお試しください。
          </p>
        </div>
        <div>
          <a href="{junior_url}" style="display: inline-block; background: #235937; color: #ffffff !important; font-size: 0.82rem; font-weight: 700; padding: 0.5rem 1rem; text-decoration: none; border-radius: 3px; white-space: nowrap;">
            Junior版で読む ↗
          </a>
        </div>
      </div>
"""

        # Insert hero banner after article-meta-row
        meta_pattern = r'(<div class="article-meta-row">[\s\S]*?</div>)'
        if re.search(meta_pattern, content):
            content = re.sub(meta_pattern, r'\1' + hero_banner, content, count=1)
        else:
            print(f"[WARN] article-meta-row not found in {senior_path}")

        # Insert bottom banner before </article>
        article_end_pattern = r'(\s*</article>)'
        if re.search(article_end_pattern, content):
            content = re.sub(article_end_pattern, bottom_banner + r'\1', content, count=1)
        else:
            print(f"[WARN] </article> not found in {senior_path}")

        # Add top-date-bar link if not present
        if "THE JUNIOR" not in content[:content.find("<header class=")]:
            content = re.sub(
                r'(<div class="top-date-bar"[^>]*>)([\s\S]*?)(</div>)',
                r'\1<div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 0.5rem; max-width: 1200px; margin: 0 auto; padding: 0 1rem;"><span>\2</span><a href="' + junior_url + '" style="color: #235937; font-weight: 700; text-decoration: underline; font-size: 0.78rem;">🌱 THE JUNIOR (英検準2〜2級版) ↗</a></div>\3',
                content,
                count=1
            )

        with open(senior_path, "w", encoding="utf-8") as f:
            f.write(content)
            
        print(f"[OK] Injected Junior links into {cat}/{slug}")
        success_count += 1
        
    print(f"\nDone! Injected links into {success_count} Senior articles.")

if __name__ == "__main__":
    link_senior_articles()
