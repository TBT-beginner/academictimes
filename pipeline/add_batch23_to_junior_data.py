# -*- coding: utf-8 -*-
with open("news_portal/pipeline/junior_articles_data.py", "r", encoding="utf-8") as f:
    text = f.read()

import_target = "from batch22_articles_data import BATCH22_JUNIOR"
import_addition = """from batch22_articles_data import BATCH22_JUNIOR
from batch23_articles_data import BATCH23_JUNIOR"""

extend_target = "JUNIOR_ARTICLES.extend(BATCH22_JUNIOR)"
extend_addition = """JUNIOR_ARTICLES.extend(BATCH22_JUNIOR)
JUNIOR_ARTICLES.extend(BATCH23_JUNIOR)"""

assert import_target in text, "import target not found"
text = text.replace(import_target, import_addition, 1)

assert extend_target in text, "extend target not found"
text = text.replace(extend_target, extend_addition, 1)

with open("news_portal/pipeline/junior_articles_data.py", "w", encoding="utf-8", newline="\n") as f:
    f.write(text)

print("Successfully linked Batch 23 into junior_articles_data.py")
