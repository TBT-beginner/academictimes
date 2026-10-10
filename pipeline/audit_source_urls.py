# -*- coding: utf-8 -*-
"""
Audits all 29 primary source URLs.
"""
import sys
import os
import urllib.request
import urllib.error

sys.path.append(os.path.dirname(__file__))
from articles_data import ARTICLES

print(f"Auditing source_url for all {len(ARTICLES)} articles...\n")

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

results = []
for idx, art in enumerate(ARTICLES):
    slug = art["slug"]
    src_url = art.get("source_url", "")
    src_name = art.get("source_name", "")

    status_str = "OK"
    status_code = None

    try:
        req = urllib.request.Request(src_url, headers=headers, method="HEAD")
        with urllib.request.urlopen(req, timeout=5) as resp:
            status_code = resp.getcode()
            status_str = f"HTTP {status_code}"
    except urllib.error.HTTPError as e:
        status_code = e.code
        # Many news sites (FT, The Times, Reuters) return 403 or 401 to automated bot headers, which confirms domain/host exists
        status_str = f"HTTP {e.code} (Server reachable)"
    except Exception as e:
        status_str = f"Net Err: {type(e).__name__}"

    results.append({
        "slug": slug,
        "src_name": src_name,
        "src_url": src_url,
        "status": status_str
    })
    print(f"[{idx+1:02d}/29] {slug[:30]:<30} | {src_url[:45]:<45} | {status_str}")

print("\nAudit Complete.")
