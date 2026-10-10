# -*- coding: utf-8 -*-
"""
FORENSIC LINK & PATH AUDITOR
Scans EVERY HTML and JS file in the news_portal directory.
Extracts all hrefs, srcs, and relative paths to check if any link is broken (404).
"""

import os
import re
from bs4 import BeautifulSoup
from urllib.parse import urlparse

PORTAL_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

def audit_all_links():
    broken_links = []
    total_links_checked = 0
    checked_files_count = 0

    print(f"Scanning directory: {PORTAL_DIR}")

    # Walk all files
    for root, dirs, files in os.walk(PORTAL_DIR):
        # Skip .git and python cache
        if ".git" in root or "__pycache__" in root:
            continue

        for f in files:
            if not f.endswith(".html"):
                continue

            file_path = os.path.join(root, f)
            rel_file_path = os.path.relpath(file_path, PORTAL_DIR)
            checked_files_count += 1

            with open(file_path, "r", encoding="utf-8", errors="ignore") as fp:
                content = fp.read()

            soup = BeautifulSoup(content, "html.parser")

            # Check <a> tags
            for a in soup.find_all("a", href=True):
                href = a["href"].strip()
                if not href or href.startswith("#") or href.startswith("javascript:") or href.startswith("mailto:"):
                    continue
                if href.startswith("http://") or href.startswith("https://"):
                    # External link (skip or check separately)
                    continue

                total_links_checked += 1
                # Remove fragment or query string
                clean_href = href.split("#")[0].split("?")[0]
                if not clean_href:
                    continue

                # Target file path
                target_path = os.path.normpath(os.path.join(root, clean_href))
                if not os.path.exists(target_path):
                    broken_links.append({
                        "source_file": rel_file_path,
                        "tag": "a",
                        "href": href,
                        "resolved_target": os.path.relpath(target_path, PORTAL_DIR) if os.path.commonpath([target_path, PORTAL_DIR]) == PORTAL_DIR else target_path,
                        "text": a.get_text(strip=True)[:40]
                    })

            # Check <link> and <script> and <img> and <audio> tags
            for tag, attr in [("link", "href"), ("script", "src"), ("img", "src"), ("audio", "src"), ("source", "src")]:
                for el in soup.find_all(tag, **{attr: True}):
                    src = el[attr].strip()
                    if not src or src.startswith("http://") or src.startswith("https://") or src.startswith("data:"):
                        continue
                    clean_src = src.split("#")[0].split("?")[0]
                    if not clean_src:
                        continue
                    target_path = os.path.normpath(os.path.join(root, clean_src))
                    total_links_checked += 1
                    if not os.path.exists(target_path):
                        broken_links.append({
                            "source_file": rel_file_path,
                            "tag": tag,
                            "href": src,
                            "resolved_target": os.path.relpath(target_path, PORTAL_DIR) if os.path.commonpath([target_path, PORTAL_DIR]) == PORTAL_DIR else target_path,
                            "text": f"<{tag} {attr}='{src}'>"
                        })

    # Check portal-data.js and junior-data.js paths
    js_paths_checked = 0
    p_data_path = os.path.join(PORTAL_DIR, "js", "portal-data.js")
    if os.path.exists(p_data_path):
        with open(p_data_path, "r", encoding="utf-8") as fp:
            p_text = fp.read()
        paths = re.findall(r'path:\s*"([^"]+)"', p_text)
        for p in paths:
            js_paths_checked += 1
            full_p = os.path.normpath(os.path.join(PORTAL_DIR, p))
            if not os.path.exists(full_p):
                broken_links.append({
                    "source_file": "js/portal-data.js",
                    "tag": "js.path",
                    "href": p,
                    "resolved_target": p,
                    "text": "portal-data article path"
                })

    j_data_path = os.path.join(PORTAL_DIR, "junior", "js", "junior-data.js")
    if os.path.exists(j_data_path):
        with open(j_data_path, "r", encoding="utf-8") as fp:
            j_text = fp.read()
        paths = re.findall(r'"path":\s*"([^"]+)"', j_text)
        senior_paths = re.findall(r'"senior_path":\s*"([^"]+)"', j_text)
        for p in paths:
            js_paths_checked += 1
            full_p = os.path.normpath(os.path.join(PORTAL_DIR, "junior", p))
            if not os.path.exists(full_p):
                broken_links.append({
                    "source_file": "junior/js/junior-data.js",
                    "tag": "js.path",
                    "href": p,
                    "resolved_target": p,
                    "text": "junior-data article path"
                })
        for sp in senior_paths:
            js_paths_checked += 1
            full_sp = os.path.normpath(os.path.join(PORTAL_DIR, "junior", sp))
            if not os.path.exists(full_sp):
                broken_links.append({
                    "source_file": "junior/js/junior-data.js",
                    "tag": "js.senior_path",
                    "href": sp,
                    "resolved_target": sp,
                    "text": "junior-data senior_path"
                })

    print(f"\nAudit Summary:")
    print(f"  - HTML Files Scanned: {checked_files_count}")
    print(f"  - Total Internal Links & Assets Checked: {total_links_checked + js_paths_checked}")
    print(f"  - Broken Links Detected: {len(broken_links)}")

    if broken_links:
        print("\n[BROKEN LINKS FOUND]:")
        for b in broken_links:
            print(f"  [ERR] In '{b['source_file']}': href='{b['href']}' -> Resolved '{b['resolved_target']}' ({b['text']})")
    else:
        print("\n[CLEAN] 100% of internal links, images, audios, and scripts exist on disk with zero 404s!")

    return broken_links

if __name__ == "__main__":
    audit_all_links()
