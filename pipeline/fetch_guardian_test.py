import urllib.request
import re

headers = {'User-Agent': 'Mozilla/5.0'}
for d in ['2026/nov/09', '2026/nov/08', '2026/nov/07']:
    url = f"https://www.theguardian.com/theguardian/{d}/all"
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            links = re.findall(r'href="(https://www.theguardian.com/[^"]+?/' + d + r'/[^"]+?)"', html)
            unique_links = list(dict.fromkeys(links))
            print(f"{url} -> HTTP {resp.status}, found {len(unique_links)} articles")
            for l in unique_links[:8]:
                print("   ", l)
    except Exception as e:
        print(f"{url} -> Error: {e}")
