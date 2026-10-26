import urllib.request
import re

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

for url in [
    'https://www.theguardian.com/theguardian/2026/oct/24/all',
    'https://www.theguardian.com/theguardian/2026/oct/25/all',
    'https://www.theguardian.com/observer/2026/oct/25/all'
]:
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            links = sorted(list(set(re.findall(r'href="(https://www.theguardian.com/[a-z-]+/2026/oct/2[45]/[^"#\?]+)"', html))))
            print(f"=== {url}: {len(links)} links found ===")
            for l in links[:15]:
                print("  ", l)
    except Exception as e:
        print(f"Error {url}: {e}")
