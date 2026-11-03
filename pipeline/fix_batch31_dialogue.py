# -*- coding: utf-8 -*-
import importlib
import re

files = [
    'news_portal/pipeline/data_batch31_part1.py',
    'news_portal/pipeline/data_batch31_part2.py',
    'news_portal/pipeline/data_batch31_junior_part1.py',
    'news_portal/pipeline/data_batch31_junior_part2.py'
]

for fpath in files:
    with open(fpath, 'r', encoding='utf-8') as f:
        code = f.read()

    # We want to replace each item in dialogue list:
    # {
    #     "speaker": "Keita",
    #     "text": "...",
    #     "translation": "..."
    # }
    # with:
    # {
    #     "speaker": "Keita先生",
    #     "name": "Keita先生",
    #     "role": "英語講師",
    #     "text": "...",  # using translation
    #     "en_text": "..." # original text
    # }
    # Or for Nanami:
    # {
    #     "speaker": "Nanami",
    #     "name": "Nanami",
    #     "role": "高校生・アシスタント",
    #     "text": "...",
    #     "en_text": "..."
    # }

    def repl_turn(m):
        spk = m.group(1).strip()
        txt = m.group(2).strip()
        trans = m.group(3).strip()
        is_keita = "keita" in spk.lower()
        speaker = "Keita先生" if is_keita else "Nanami"
        name = "Keita先生" if is_keita else "Nanami"
        role = "英語講師" if is_keita else "高校生・アシスタント"
        return f'''{{
                "speaker": "{speaker}",
                "name": "{name}",
                "role": "{role}",
                "text": {trans},
                "en_text": {txt}
            }}'''

    pattern = r'\{\s*"speaker":\s*"([^"]+)",\s*\n\s*"text":\s*(".*?"|[\'\'].*?[\'\']),\s*\n\s*"translation":\s*(".*?"|[\'\'].*?[\'\'])\s*\}'
    new_code = re.sub(pattern, repl_turn, code, flags=re.DOTALL)
    
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(new_code)
    print(f"Updated {fpath}")

print("All Batch 31 dialogue items normalized!")
