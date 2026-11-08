import urllib.request
import re

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

sections = [
    'https://www.theguardian.com/world',
    'https://www.theguardian.com/uk-news',
    'https://www.theguardian.com/us-news',
    'https://www.theguardian.com/business',
    'https://www.theguardian.com/technology',
    'https://www.theguardian.com/environment',
    'https://www.theguardian.com/science',
    'https://www.theguardian.com/society',
    'https://www.theguardian.com/culture',
    'https://www.theguardian.com/music',
    'https://www.theguardian.com/books',
    'https://www.theguardian.com/media',
    'https://www.theguardian.com/stage',
    'https://www.theguardian.com/education',
    'https://www.theguardian.com/global-development'
]

found_articles = []
for sec in sections:
    try:
        req = urllib.request.Request(sec, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            urls = re.findall(r'href="(https://www.theguardian.com/[a-z-]+/2026/nov/(?:07|08|09)/[^"]+)"', html)
            for u in urls:
                if u not in found_articles and not u.endswith('/all'):
                    found_articles.append(u)
    except Exception as e:
        print(f"Error {sec}: {e}")

print(f"Total found {len(found_articles)} articles:")
# Verify HTTP 200 OK for each
verified = []
for u in found_articles:
    try:
        req = urllib.request.Request(u, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            if resp.status == 200:
                # get title
                h = resp.read().decode('utf-8', errors='ignore')
                tm = re.search(r'<title>(.*?)</title>', h)
                title = tm.group(1).replace(' | The Guardian', '').strip() if tm else ''
                verified.append((u, title))
                print(f"[200 OK] {u}")
                print(f"         {title}")
    except Exception as e:
        print(f"[FAIL] {u}: {e}")

print(f"\nTotal verified 200 OK: {len(verified)}")
