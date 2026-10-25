import urllib.request
import re
import json

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

dates_to_check = [
    'https://www.theguardian.com/theguardian/2026/oct/25/all',
    'https://www.theguardian.com/theguardian/2026/oct/24/all',
    'https://www.theguardian.com/international'
]

found_links = set()
for url in dates_to_check:
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            # Extract links matching 2026/oct/24 or 2026/oct/25
            links = re.findall(r'href="(https://www\.theguardian\.com/[a-z0-9\-]+(?:/[a-z0-9\-]+)*/2026/oct/(?:24|25)/[a-z0-9\-]+)"', html)
            for l in links:
                if not any(x in l for x in ['/live/', '/picture/', '/gallery/', '/audio/', '/video/']):
                    found_links.add(l)
    except Exception as e:
        print(f"Error fetching {url}: {e}")

print(f"Total unique links found: {len(found_links)}")
valid_articles = []
for l in list(found_links)[:40]:
    try:
        req = urllib.request.Request(l, headers=headers)
        with urllib.request.urlopen(req, timeout=5) as resp:
            if resp.status == 200:
                # get title
                page_html = resp.read(50000).decode('utf-8', errors='ignore')
                title_match = re.search(r'<title>(.*?)</title>', page_html)
                title = title_match.group(1) if title_match else ""
                valid_articles.append({"url": l, "title": title})
                if len(valid_articles) >= 20:
                    break
    except Exception as e:
        pass

print(f"Valid verified 200 articles: {len(valid_articles)}")
for a in valid_articles:
    print(f"- {a['url']}\n  {a['title']}")
with open('c:/Users/teacher/Documents/lessonfactory/news_portal/pipeline/found_20261026_urls.json', 'w', encoding='utf-8') as f:
    json.dump(valid_articles, f, indent=2, ensure_ascii=False)
