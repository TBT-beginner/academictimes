import urllib.request
import re

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

# Let's search sections on The Guardian for recent articles
sections = [
    'world', 'science', 'environment', 'business', 'technology', 'culture', 'law', 'society'
]

found_articles = []
for sec in sections:
    url = f"https://www.theguardian.com/{sec}"
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            # Look for 2026 or recent article urls
            urls = re.findall(r'href="(https://www.theguardian.com/[a-z-]+/2026/[a-z]+/\d{2}/[^"]+)"', html)
            for u in urls:
                if u not in found_articles and not u.endswith('/all'):
                    found_articles.append(u)
    except Exception as e:
        print(f"Error fetching {url}: {e}")

print(f"Found {len(found_articles)} recent articles on section homepages:")
for u in found_articles[:20]:
    print("  ", u)
