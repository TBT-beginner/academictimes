import urllib.request
import xml.etree.ElementTree as ET
import re

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

req = urllib.request.Request('https://www.theguardian.com/science/rss', headers=headers)
with urllib.request.urlopen(req, timeout=10) as resp:
    root = ET.fromstring(resp.read())
    for item in root.findall('.//item')[:15]:
        title = item.find('title').text
        link = item.find('link').text
        pubDate = item.find('pubDate').text
        print(f"TITLE: {title}")
        print(f"LINK: {link}")
        print(f"PUB: {pubDate}\n")
