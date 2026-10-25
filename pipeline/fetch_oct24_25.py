import urllib.request
import re
import json

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

archive_urls = [
    'https://www.theguardian.com/theguardian/2026/oct/24/all',
    'https://www.theguardian.com/theguardian/2026/oct/25/all'
]

rss_urls = [
    'https://www.theguardian.com/world/rss',
    'https://www.theguardian.com/science/rss',
    'https://www.theguardian.com/environment/rss',
    'https://www.theguardian.com/technology/rss',
    'https://www.theguardian.com/culture/rss',
    'https://www.theguardian.com/business/rss',
    'https://www.theguardian.com/uk-news/rss',
    'https://www.theguardian.com/society/rss',
    'https://www.theguardian.com/law/rss'
]

found = {}

# From Archives
for a_url in archive_urls:
    try:
        req = urllib.request.Request(a_url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8')
            # Extract links and titles
            matches = re.findall(r'<a[^>]+href="(https://www.theguardian.com/[^"]+/(?:2026/oct/24|2026/oct/25)/[^"]+)"[^>]*>(.*?)</a>', html, re.DOTALL)
            for link, title in matches:
                clean_title = re.sub(r'<[^>]+>', '', title).strip()
                if clean_title and link not in found and not any(skip in link for skip in ['/live/', '/audio/', '/video/', '/gallery/']):
                    found[link] = clean_title
    except Exception as e:
        print(f"Error fetching archive {a_url}: {e}")

# From RSS
for r_url in rss_urls:
    try:
        req = urllib.request.Request(r_url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            xml_data = resp.read().decode('utf-8')
            items = re.findall(r'<item>(.*?)</item>', xml_data, re.DOTALL)
            for item in items:
                title_match = re.search(r'<title><!\[CDATA\[(.*?)\]\]></title>', item) or re.search(r'<title>(.*?)</title>', item)
                link_match = re.search(r'<link>(.*?)</link>', item)
                if title_match and link_match:
                    link = link_match.group(1).strip()
                    title = title_match.group(1).strip()
                    if ('2026/oct/24' in link or '2026/oct/25' in link) and link not in found:
                        if not any(skip in link for skip in ['/live/', '/audio/', '/video/', '/gallery/']):
                            found[link] = title
    except Exception as e:
        print(f"Error fetching RSS {r_url}: {e}")

print(f"Total articles found: {len(found)}")
res = [{"url": k, "title": v} for k, v in found.items()]
with open('c:/Users/teacher/Documents/lessonfactory/news_portal/pipeline/oct24_25_articles.json', 'w', encoding='utf-8') as f:
    json.dump(res, f, ensure_ascii=False, indent=2)

for item in res[:30]:
    print(f"- {item['title']} -> {item['url']}")
