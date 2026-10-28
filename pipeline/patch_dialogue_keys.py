import re

files = [
    "news_portal/pipeline/data_batch25_part1.py",
    "news_portal/pipeline/data_batch25_part2.py",
    "news_portal/pipeline/data_batch25_junior_part1.py",
    "news_portal/pipeline/data_batch25_junior_part2.py"
]

for fpath in files:
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Replace Nanami turns
    content = content.replace(
        '"speaker": "七",\n                "text":',
        '"speaker": "七",\n                "name": "Nanami",\n                "role": "生徒・アシスタント",\n                "text":'
    )
    # Replace Keita turns
    content = content.replace(
        '"speaker": "慶",\n                "text":',
        '"speaker": "慶",\n                "name": "Keita先生",\n                "role": "英語講師",\n                "text":'
    )
    
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Patched {fpath}")
