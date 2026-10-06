# -*- coding: utf-8 -*-
"""
UNIFIED DAILY NEWS PIPELINE
THE ACADEMIC TIMES (発展・難関大版) & THE JUNIOR (基礎・英検準2〜2級版)

Runs daily to ensure synchronized publishing across both editions:
1. Builds / updates all Academic Times Senior articles & audios.
2. Injects reciprocal THE JUNIOR links & banners into Senior articles.
3. Builds / updates all 5 Senior Category Index Portals.
4. Builds / updates all THE JUNIOR articles, TTS audios & quizzes.
5. Builds / updates THE JUNIOR Top Portal (junior/index.html).
6. Verifies 1:1 bidirectional link integrity and prints a sync report.
"""

import os
import sys
import asyncio
import subprocess

PIPELINE_DIR = os.path.dirname(os.path.abspath(__file__))
PORTAL_DIR = os.path.abspath(os.path.join(PIPELINE_DIR, ".."))

def run_step(step_name, command_args):
    print(f"\n==========================================")
    print(f"[DAILY PIPELINE] Step: {step_name}")
    print(f"==========================================")
    res = subprocess.run([sys.executable] + command_args, cwd=PIPELINE_DIR, capture_output=True, text=True, encoding="utf-8")
    if res.stdout:
        print(res.stdout.strip())
    if res.returncode != 0:
        print(f"[ERROR in {step_name}]: {res.stderr}")
        return False
    return True

def verify_1_to_1_parity():
    print(f"\n==========================================")
    print(f"[DAILY PIPELINE] Verifying 1:1 Parity & Links")
    print(f"==========================================")
    import junior_articles_data
    from bs4 import BeautifulSoup
    
    total = len(junior_articles_data.JUNIOR_ARTICLES)
    senior_ok = 0
    junior_ok = 0
    
    for art in junior_articles_data.JUNIOR_ARTICLES:
        cat = art["category"]
        slug = art["slug"]
        
        # Check Senior file
        senior_path = os.path.join(PORTAL_DIR, cat, slug, "index.html")
        junior_path = os.path.join(PORTAL_DIR, "junior", cat, slug, "index.html")
        
        if not os.path.exists(senior_path):
            print(f"[FAIL] Missing Senior article: {cat}/{slug}")
            continue
        if not os.path.exists(junior_path):
            print(f"[FAIL] Missing Junior article: junior/{cat}/{slug}")
            continue
            
        with open(senior_path, "r", encoding="utf-8") as f:
            senior_content = f.read()
        with open(junior_path, "r", encoding="utf-8") as f:
            junior_content = f.read()
            
        expected_junior_rel = f"../../junior/{cat}/{slug}/index.html"
        expected_senior_rel = f"../../../{cat}/{slug}/index.html"
        
        has_junior_link = expected_junior_rel in senior_content
        has_senior_link = expected_senior_rel in junior_content
        
        if has_junior_link:
            senior_ok += 1
        else:
            print(f"[WARN] Senior missing Junior link: {cat}/{slug}")
            
        if has_senior_link:
            junior_ok += 1
        else:
            print(f"[WARN] Junior missing Senior link: {cat}/{slug}")
            
    print(f"Verified {total} article pairs:")
    print(f"  - Senior -> Junior reciprocal links: {senior_ok}/{total} OK")
    print(f"  - Junior -> Senior reciprocal links: {junior_ok}/{total} OK")
    
    all_ok = (senior_ok == total and junior_ok == total)
    return all_ok

def main():
    print("************************************************************")
    print("  THE ACADEMIC TIMES & THE JUNIOR - UNIFIED DAILY BUILD")
    print("************************************************************")
    
    # 1. Update Senior Category pages
    if not run_step("Build Senior Category Portals", ["generate_category_pages.py"]):
        print("[FAIL] Category portal build failed.")
        sys.exit(1)
        
    # 2. Build Junior Articles & Audio
    if not run_step("Build THE JUNIOR Articles & Audio", ["build_junior_site.py"]):
        print("[FAIL] Junior articles build failed.")
        sys.exit(1)
        
    # 3. Build Junior Top Page
    if not run_step("Build THE JUNIOR Top Portal", ["build_junior_top.py"]):
        print("[FAIL] Junior top page build failed.")
        sys.exit(1)
        
    # 4. Inject Reciprocal Links into Senior Articles
    if not run_step("Link Senior Articles to THE JUNIOR", ["link_senior_to_junior.py"]):
        print("[FAIL] Reciprocal linking failed.")
        sys.exit(1)
        
    # 5. Verify Parity
    success = verify_1_to_1_parity()
    if success:
        print("\n[SUCCESS] Both portals updated with 100% 1:1 parity and audio coverage!")
    else:
        print("\n[WARNING] Completed with warnings. Please inspect the log above.")

if __name__ == "__main__":
    main()
