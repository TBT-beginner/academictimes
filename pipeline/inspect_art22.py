# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, "news_portal/pipeline")
import data_batch22
art = data_batch22.BATCH22_SENIOR[0]
print("Keys in article:", art.keys())
for k in art:
    if k in ["title", "slug", "category", "date", "source_url", "source", "source_meta", "origin_url"]:
        print(f"{k}: {art[k]}")
    elif "source" in k or "url" in k:
        print(f"{k}: {art[k]}")
