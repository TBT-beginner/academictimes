# -*- coding: utf-8 -*-
with open("news_portal/pipeline/data_batch22.py", "r", encoding="utf-8") as f:
    text22 = f.read()

import re
matches = re.findall(r'"source[^"]*":\s*"([^"]+)"', text22)
print("Source matches in batch 22:", matches)

matches_all = re.findall(r'http[s]?://[^\s",\']+', text22)
print("All URLs in batch 22:")
for u in set(matches_all):
    print(" -", u)
