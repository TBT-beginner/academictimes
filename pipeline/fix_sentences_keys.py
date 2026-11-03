# -*- coding: utf-8 -*-
import re

files = [
    'news_portal/pipeline/data_batch31_part1.py',
    'news_portal/pipeline/data_batch31_part2.py',
    'news_portal/pipeline/data_batch31_junior_part1.py',
    'news_portal/pipeline/data_batch31_junior_part2.py'
]

for fpath in files:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace "s": with "en": ... wait, let's keep both or replace:
    # Actually in dict:
    # {"s": "...", "t": "..."} -> {"en": "...", "ja": "...", "s": "...", "t": "..."}
    # Or just "en": ..., "ja": ..., "s": ..., "t": ...
    def repl(m):
        s_val = m.group(1)
        t_val = m.group(2)
        return f'"en": {s_val},\n                "ja": {t_val},\n                "s": {s_val},\n                "t": {t_val}'

    pattern = r'"s":\s*(".*?"|[\'\'].*?[\'\']),\s*\n\s*"t":\s*(".*?"|[\'\'].*?[\'\'])'
    new_content = re.sub(pattern, repl, content, flags=re.DOTALL)
    
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Updated {fpath}")
