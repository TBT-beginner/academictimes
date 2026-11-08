# -*- coding: utf-8 -*-
"""Normalize dialogue keys across Batch 34 files to include name and role."""

import re

files = [
    "news_portal/pipeline/data_batch34_part1.py",
    "news_portal/pipeline/data_batch34_part2.py",
    "news_portal/pipeline/data_batch34_junior_part1.py",
    "news_portal/pipeline/data_batch34_junior_part2.py",
]

for filepath in files:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Replace speaker 'nanami' with full dict
    # Pattern: {'speaker': 'nanami', 'text': '...'}
    # Replace with: {'speaker': 'Nanami', 'name': 'Nanami', 'role': '高校生', 'text': '...', 'en_text': '...'}
    
    # We can parse the file in python, update the dicts, and re-serialize or do regex replacement
    # Regex replacement for nanami:
    content = re.sub(
        r"\{\s*'speaker':\s*'nanami',\s*'text':\s*([^\}]+)\}",
        r"{'speaker': 'Nanami', 'name': 'Nanami', 'role': '高校生', 'text': \1, 'en_text': \1}",
        content
    )
    # Regex replacement for keita:
    content = re.sub(
        r"\{\s*'speaker':\s*'keita',\s*'text':\s*([^\}]+)\}",
        r"{'speaker': 'Keita先生', 'name': 'Keita先生', 'role': '英語講師', 'text': \1, 'en_text': \1}",
        content
    )

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Updated {filepath}")

print("All Batch 34 dialogue turns normalized successfully!")
