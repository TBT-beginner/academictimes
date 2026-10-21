import re
import urllib.request

content_path = r'C:/Users/teacher/.gemini/antigravity/brain/999b3ae4-c547-491d-99b4-3b2f4b355c5c/.system_generated/steps/7533/content.md'
with open(content_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Look for href="/..."
hrefs = set(re.findall(r'href=["\'](/[^"\']+)["\']', text))
print(f"Total hrefs: {len(hrefs)}")

candidates = []
for h in hrefs:
    if '2026/oct/21' in h or '2026/oct/20' in h or '2026/oct/22' in h:
        url = 'https://www.theguardian.com' + h
        candidates.append(url)

print(f"Candidates with oct date: {len(candidates)}")
for c in sorted(candidates)[:25]:
    print(c)
