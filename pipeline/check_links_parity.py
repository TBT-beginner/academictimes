import os
import re

PORTAL_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# 1. Check portal-data.js
p_path = os.path.join(PORTAL_DIR, "js", "portal-data.js")
with open(p_path, "r", encoding="utf-8") as f:
    p_text = f.read()
portal_slugs = re.findall(r'["\']?slug["\']?:\s*"([^"]+)"', p_text)
print(f"portal-data.js: {len(portal_slugs)} articles ({len(set(portal_slugs))} unique)")

# 2. Check junior-data.js
j_path = os.path.join(PORTAL_DIR, "junior", "js", "junior-data.js")
with open(j_path, "r", encoding="utf-8") as f:
    j_text = f.read()
junior_slugs = re.findall(r'["\']?slug["\']?:\s*"([^"]+)"', j_text)
print(f"junior-data.js: {len(junior_slugs)} articles ({len(set(junior_slugs))} unique)")

# 3. Check articles on disk
all_articles = []
for cat in ["culture", "entertainment", "law", "science", "society", "world"]:
    cat_dir = os.path.join(PORTAL_DIR, cat)
    if os.path.isdir(cat_dir):
        for item in os.listdir(cat_dir):
            item_path = os.path.join(cat_dir, item)
            if os.path.isdir(item_path) and os.path.exists(os.path.join(item_path, "index.html")):
                all_articles.append((cat, item))

print(f"Disk Senior Articles: {len(all_articles)}")
senior_set = set(slug for _, slug in all_articles)

# Check parity
missing_in_portal = senior_set - set(portal_slugs)
missing_in_junior = senior_set - set(junior_slugs)
print(f"Senior articles missing in portal-data.js: {missing_in_portal}")
print(f"Senior articles missing in junior-data.js: {missing_in_junior}")
