import urllib.request
import re

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

found_articles = []
for d in ['2026/nov/09', '2026/nov/10']:
    archive_url = f"https://www.theguardian.com/theguardian/{d}/all"
    try:
        req = urllib.request.Request(archive_url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            urls = re.findall(rf'href="(https://www.theguardian.com/[a-z-]+/{d}/[^"]+)"', html)
            for u in urls:
                if u not in found_articles and not u.endswith('/all'):
                    found_articles.append(u)
    except Exception as e:
        print(f"Error {archive_url}: {e}")

# Also check section homepages
sections = [
    'world', 'science', 'environment', 'business', 'technology', 'culture', 'law', 'society', 'books', 'media', 'stage', 'sport'
]
for sec in sections:
    url = f"https://www.theguardian.com/{sec}"
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            urls = re.findall(r'href="(https://www.theguardian.com/[a-z-]+/2026/nov/(?:09|10)/[^"]+)"', html)
            for u in urls:
                if u not in found_articles and not u.endswith('/all'):
                    found_articles.append(u)
    except Exception as e:
        print(f"Error {url}: {e}")

print(f"Total candidate articles found: {len(found_articles)}")

# Verify HTTP 200 OK and get headlines
verified = []
for u in found_articles:
    try:
        req = urllib.request.Request(u, headers=headers)
        with urllib.request.urlopen(req, timeout=8) as resp:
            if resp.status == 200:
                html = resp.read().decode('utf-8', errors='ignore')
                tm = re.search(r'<title>(.*?)</title>', html)
                title = tm.group(1).replace(' | The Guardian', '').strip() if tm else ''
                # extract meta description or intro if available
                dm = re.search(r'<meta name="description" content="(.*?)"', html)
                desc = dm.group(1) if dm else ''
                verified.append({'url': u, 'title': title, 'desc': desc})
                print(f"[OK] {u} -> {title[:60]}")
    except Exception as e:
        pass

print(f"\nTotal verified 200 OK: {len(verified)}")
import json
with open('pipeline/batch35_candidates.json', 'w', encoding='utf-8') as f:
    json.dump(verified, f, ensure_ascii=False, indent=2)
