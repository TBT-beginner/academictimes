# -*- coding: utf-8 -*-
with open("news_portal/pipeline/data_batch22.py", "r", encoding="utf-8") as f:
    text = f.read()

import re
matches = re.findall(r'"source_url":\s*"([^"]+)"', text)
print(f"Total source_url in batch22: {len(matches)}")
for m in matches:
    print(" -", m)
