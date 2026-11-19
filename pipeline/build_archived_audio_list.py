# -*- coding: utf-8 -*-
"""Generate archived_audio_slugs.json for articles older than 2026-11-14 (keep last 7 days local)."""

import json
import os
import sys

PIPELINE_DIR = os.path.dirname(os.path.abspath(__file__))
if PIPELINE_DIR not in sys.path:
    sys.path.insert(0, PIPELINE_DIR)

from articles_data import ARTICLES

KEEP_FROM_DATE = "2026-11-14"

archived = sorted({
    a["slug"]
    for a in ARTICLES
    if a.get("date", "") < KEEP_FROM_DATE
})

out_path = os.path.join(PIPELINE_DIR, "archived_audio_slugs.json")
with open(out_path, "w", encoding="utf-8") as f:
    json.dump({"keep_from_date": KEEP_FROM_DATE, "slugs": archived}, f, ensure_ascii=False, indent=2)

print(f"Saved {len(archived)} archived slugs (keeping >= {KEEP_FROM_DATE} local).")
