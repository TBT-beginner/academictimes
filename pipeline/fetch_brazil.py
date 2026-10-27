# -*- coding: utf-8 -*-
import urllib.request
import re

url = "https://www.theguardian.com/world/2026/oct/26/flavio-bolsonaro-brazil-lula-election"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
try:
    with urllib.request.urlopen(req, timeout=10) as resp:
        html = resp.read().decode("utf-8", errors="ignore")
        title_m = re.search(r'<title>([^<]+)</title>', html)
        title = title_m.group(1).replace(" | The Guardian", "").strip() if title_m else ""
        paras = re.findall(r'<p>([^<]+)</p>', html)
        print("Brazil Title:", title.encode("ascii", errors="replace").decode("ascii"))
        print("Brazil Lead:", paras[0].encode("ascii", errors="replace").decode("ascii") if paras else "No lead")
except Exception as e:
    print("Error:", e)
