# -*- coding: utf-8 -*-
with open("news_portal/pipeline/articles_data.py", "r", encoding="utf-8") as f:
    text = f.read()

target = """try:
    from batch22_articles_data import BATCH22_SENIOR
    for _art in BATCH22_SENIOR:
        if _art.get("slug") not in _existing_slugs:
            ARTICLES.append(_art)
            _existing_slugs.add(_art.get("slug"))
except ImportError:
    pass"""

addition = """try:
    from batch22_articles_data import BATCH22_SENIOR
    for _art in BATCH22_SENIOR:
        if _art.get("slug") not in _existing_slugs:
            ARTICLES.append(_art)
            _existing_slugs.add(_art.get("slug"))
except ImportError:
    pass

try:
    from batch23_articles_data import BATCH23_SENIOR
    for _art in BATCH23_SENIOR:
        if _art.get("slug") not in _existing_slugs:
            ARTICLES.append(_art)
            _existing_slugs.add(_art.get("slug"))
except ImportError:
    pass"""

norm_text = text.replace("\r\n", "\n")
norm_target = target.replace("\r\n", "\n")
norm_addition = addition.replace("\r\n", "\n")

assert norm_target in norm_text, "target not found"
new_text = norm_text.replace(norm_target, norm_addition, 1)

with open("news_portal/pipeline/articles_data.py", "w", encoding="utf-8", newline="\n") as f:
    f.write(new_text)

print("Successfully updated articles_data.py with Batch 23")
