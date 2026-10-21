import urllib.request
import xml.etree.ElementTree as ET
import json
import re

feeds = [
    "https://www.theguardian.com/world/rss",
    "https://www.theguardian.com/science/rss",
    "https://www.theguardian.com/environment/rss",
    "https://www.theguardian.com/technology/rss",
    "https://www.theguardian.com/culture/rss",
    "https://www.theguardian.com/business/rss",
    "https://www.theguardian.com/uk-news/rss",
    "https://www.theguardian.com/australia-news/rss",
    "https://www.theguardian.com/us-news/rss",
    "https://www.theguardian.com/society/rss",
]

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

seen_links = set()
articles = []

for feed_url in feeds:
    try:
        req = urllib.request.Request(feed_url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            content = resp.read()
            root = ET.fromstring(content)
            for item in root.findall('.//item'):
                title = item.find('title').text if item.find('title') is not None else ""
                link = item.find('link').text if item.find('link') is not None else ""
                pubDate = item.find('pubDate').text if item.find('pubDate') is not None else ""
                desc = item.find('description').text if item.find('description') is not None else ""
                
                # Clean html tags from desc
                clean_desc = re.sub(r'<[^>]+>', '', desc).strip()
                
                if link and link not in seen_links:
                    if any(k in link for k in ['2026/oct/21', '2026/oct/22']):
                        seen_links.add(link)
                        articles.append({
                            'title': title,
                            'link': link,
                            'pubDate': pubDate,
                            'desc': clean_desc
                        })
    except Exception as e:
        print(f"Error fetching {feed_url}: {e}")

with open('pipeline/oct21_22_articles.json', 'w', encoding='utf-8') as f:
    json.dump(articles, f, ensure_ascii=False, indent=2)

print(f"Successfully saved {len(articles)} unique articles from Oct 21-22, 2026.")
