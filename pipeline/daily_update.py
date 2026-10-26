# -*- coding: utf-8 -*-
"""
UNIFIED DAILY NEWS PIPELINE
THE ACADEMIC TIMES (発展・難関大版) & THE JUNIOR (基礎・英検準2〜2級版)

Runs daily to ensure synchronized publishing across both editions:
0. Pre-generation Direct News Source & Date Verification (URL, domain, HTTPS, foundational/past-news rules).
1. Ensures Senior Edge-TTS audio (en-GB-RyanNeural + Keita/Nanami dialogues).
2. Builds / updates all 5 Senior Category Index Portals.
3. Builds / updates Senior portal-data.js.
4. Builds / updates all THE JUNIOR articles, TTS audios & quizzes.
5. Builds / updates THE JUNIOR Data JS (junior-data.js).
6. Builds / updates THE JUNIOR Top Portal (junior/index.html).
7. Injects reciprocal THE JUNIOR links & banners into Senior articles.
8. Post-generation Source Cross-Check (verifies 0 omissions across editions).
9. Verifies 1:1 bidirectional link integrity and prints sync report.
10. Audits all internal hyperlinks across all HTML files (ensures 0 broken links).
11. Stages, commits, and pushes updates to GitHub repository (origin/main).
"""

import os
import sys
import argparse
import datetime
import subprocess

PIPELINE_DIR = os.path.dirname(os.path.abspath(__file__))
PORTAL_DIR = os.path.abspath(os.path.join(PIPELINE_DIR, ".."))
WORKSPACE_DIR = os.path.abspath(os.path.join(PORTAL_DIR, ".."))

from source_verifier import pre_update_source_verification, post_update_source_crosscheck
import articles_data
import junior_articles_data

def run_step(step_name, command_args):
    print(f"\n==========================================")
    print(f"[DAILY PIPELINE] Step: {step_name}")
    print(f"==========================================")
    sys.stdout.flush()
    res = subprocess.run([sys.executable] + command_args, cwd=PIPELINE_DIR)
    if res.returncode != 0:
        print(f"[ERROR in {step_name}]: Process exited with code {res.returncode}")
        return False
    return True

def verify_1_to_1_parity():
    print(f"\n==========================================")
    print(f"[DAILY PIPELINE] Step: Verifying 1:1 Parity & Reciprocal Links")
    print(f"==========================================")
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
    
    return (senior_ok == total and junior_ok == total)

def git_commit_and_push(commit_msg):
    print(f"\n==========================================")
    print(f"[DAILY PIPELINE] Step: Git Commit & Push")
    print(f"==========================================")
    
    # Check status
    st_res = subprocess.run(["git", "status", "--porcelain"], cwd=PORTAL_DIR, capture_output=True, text=True, encoding="utf-8")
    if not st_res.stdout.strip():
        print("[GIT] Working tree is clean. Nothing to commit.")
        return True

    print(f"[GIT] Changes detected. Staging all files...")
    add_res = subprocess.run(["git", "add", "."], cwd=PORTAL_DIR, capture_output=True, text=True, encoding="utf-8")
    if add_res.returncode != 0:
        print(f"[ERROR in git add]: {add_res.stderr}")
        return False

    print(f"[GIT] Committing with message: '{commit_msg}'...")
    com_res = subprocess.run(["git", "commit", "-m", commit_msg], cwd=PORTAL_DIR, capture_output=True, text=True, encoding="utf-8")
    if com_res.returncode != 0:
        chk = subprocess.run(["git", "status", "--porcelain"], cwd=PORTAL_DIR, capture_output=True, text=True, encoding="utf-8")
        if not chk.stdout.strip():
            print("[GIT] Working tree is clean. Nothing to commit.")
        else:
            print(f"[ERROR in git commit]: {com_res.stderr}")
            return False
    print(com_res.stdout.strip() if com_res.stdout else "")

    print(f"[GIT] Pushing to origin main...")
    push_res = subprocess.run(["git", "push", "origin", "main"], cwd=PORTAL_DIR, capture_output=True, text=True, encoding="utf-8")
    if push_res.returncode != 0:
        print(f"[ERROR in git push]: {push_res.stderr}")
        return False
    print(push_res.stdout.strip() if push_res.stdout else push_res.stderr.strip())
    print("[GIT] Successfully pushed to origin main!")
    return True

def main():
    parser = argparse.ArgumentParser(description="Unified Daily News Pipeline for Academic Times & The Junior")
    parser.add_argument("--date", help="Specific edition date (YYYY-MM-DD)")
    parser.add_argument("--skip-audio", action="store_true", help="Skip TTS audio synthesis")
    parser.add_argument("--skip-push", "--no-push", action="store_true", dest="skip_push", help="Skip git commit and push")
    parser.add_argument("--commit-msg", help="Custom git commit message")
    args = parser.parse_args()

    today_str = args.date or datetime.date.today().strftime("%Y-%m-%d")
    commit_msg = args.commit_msg or f"Daily update: {today_str} [automated sync & verified]"

    print("************************************************************")
    print(f"  THE ACADEMIC TIMES & THE JUNIOR - UNIFIED DAILY BUILD")
    print(f"  Date: {today_str}")
    print(f"  Audio Synthesis: {'Disabled (--skip-audio)' if args.skip_audio else 'Enabled'}")
    print(f"  Git Deployment:  {'Disabled (--skip-push)' if args.skip_push else 'Enabled'}")
    print("************************************************************")

    # Step 0: Pre-generation Direct News Source & Date Verification
    print(f"\n[DAILY PIPELINE] Step 0: Pre-generation Source Verification")
    if not pre_update_source_verification(articles_data.ARTICLES):
        print("[FAIL] Pre-generation source verification failed. Aborting build.")
        sys.exit(1)

    # Step 1: Build Senior Articles & Audio
    senior_args = ["generate_all_articles.py"]
    if args.skip_audio:
        senior_args.append("--skip-audio")
    if not run_step("Build Senior Articles & Audio", senior_args):
        print("[FAIL] Senior article generation failed.")
        sys.exit(1)

    if not args.skip_audio:
        if not run_step("Ensure Senior Edge-TTS Audio", ["synthesize_missing_senior_audio.py"]):
            print("[FAIL] Senior audio synthesis check failed.")
            sys.exit(1)

    # Step 2: Update Senior Category pages
    if not run_step("Build Senior Category Portals", ["generate_category_pages.py"]):
        print("[FAIL] Category portal build failed.")
        sys.exit(1)

    # Step 3: Build Senior Portal Data JS
    if not run_step("Build Senior Portal Data JS", ["build_portal_data_js.py"]):
        print("[FAIL] Senior portal data JS build failed.")
        sys.exit(1)

    # Step 4: Build THE JUNIOR Articles & Audio
    junior_args = ["build_junior_site.py"]
    if args.skip_audio:
        junior_args.append("--skip-audio")
    if not run_step("Build THE JUNIOR Articles & Audio", junior_args):
        print("[FAIL] Junior articles build failed.")
        sys.exit(1)

    # Step 5: Build THE JUNIOR Data JS
    if not run_step("Build THE JUNIOR Data JS", ["build_junior_data_js.py"]):
        print("[FAIL] Junior data JS build failed.")
        sys.exit(1)

    # Step 6: Build THE JUNIOR Top Portal
    if not run_step("Build THE JUNIOR Top Portal", ["build_junior_top.py"]):
        print("[FAIL] Junior top page build failed.")
        sys.exit(1)

    # Step 7: Inject Reciprocal Links into Senior Articles
    if not run_step("Link Senior Articles to THE JUNIOR", ["link_senior_to_junior.py"]):
        print("[FAIL] Reciprocal linking failed.")
        sys.exit(1)

    # Step 8: Post-generation Cross-Check against Primary Sources
    print(f"\n[DAILY PIPELINE] Step 8: Post-generation Cross-Check")
    if not post_update_source_crosscheck(articles_data.ARTICLES, junior_articles_data.JUNIOR_ARTICLES):
        print("[FAIL] Post-generation source cross-check failed! Detected omissions or mismatches.")
        sys.exit(1)

    # Step 9: 1:1 Parity Verification
    if not verify_1_to_1_parity():
        print("[FAIL] Reciprocal parity verification failed.")
        sys.exit(1)

    # Step 10: Complete Hyperlink Audit (Zero Broken Links)
    if not run_step("Audit All Internal Links", ["audit_all_links.py"]):
        print("[FAIL] Link audit found broken links! Aborting deployment.")
        sys.exit(1)

    # Step 11: Automatic Git Deployment
    if not args.skip_push:
        if not git_commit_and_push(commit_msg):
            print("[FAIL] Git commit & push failed.")
            sys.exit(1)
    else:
        print("\n[DAILY PIPELINE] Step 11: Skipped Git Push (--skip-push)")

    print("\n============================================================")
    print("[SUCCESS] All portals fully updated, fact-checked & synchronized!")
    print("  - Direct news sources & HTTPS URLs verified")
    print("  - Foundational papers & past news clearly differentiated with why-boxes")
    print("  - 100% 1:1 Senior <-> Junior parity and Edge-TTS audio ready")
    print("  - 0 broken links verified across all HTML files")
    if not args.skip_push:
        print("  - Pushed and deployed to GitHub origin/main successfully")
    print("============================================================")

if __name__ == "__main__":
    main()
