import urllib.request
import ssl
import json

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

urls = [
    ("serbia", "https://www.theguardian.com/world/2026/oct/25/serbian-leader-aleksandar-vucic-concedes-defeat-in-fiercely-contested-parliamentary-election"),
    ("brazil", "https://www.theguardian.com/world/2026/oct/25/brazilians-vote-in-presidential-election-runoff-pitting-leftist-lula-against-far-right-bolsonaro"),
    ("un-race", "https://www.theguardian.com/world/2026/oct/25/emirati-diplomat-who-helped-deliver-aid-to-gaza-enters-un-secretary-general-race"),
    ("venezuela", "https://www.theguardian.com/world/2026/oct/25/exiled-opposition-leader-maria-corina-machado-returns-to-venezuela"),
    ("roman-glass", "https://www.theguardian.com/science/2026/oct/25/scientists-rediscover-ancient-roman-colour-changing-glass"),
    ("creator-fund", "https://www.theguardian.com/technology/2026/oct/25/tech-firms-should-pay-the-creators-whose-work-they-use"),
    ("datacentre-protests", "https://www.theguardian.com/uk-news/2026/oct/22/ai-firms-say-uk-has-a-year-to-head-off-datacentre-protests-before-construction-is-threatened"),
    ("bom-climate", "https://www.theguardian.com/environment/2026/oct/24/the-australian-reports-widespread-errors-in-bom-temperature-data-where-is-the-evidence-for-those-big-claims"),
    ("elections-10-days", "https://www.theguardian.com/world/ng-interactive/2026/oct/25/ten-days-shake-world-democratic-norms-pivotal-elections-brazil-israel-serbia-us"),
    ("be-ready-stockpile", "https://www.theguardian.com/world/2026/oct/22/every-briton-should-stockpile-water-and-food-supplies-government-advises"),
    ("medieval-lime-bike", "https://www.theguardian.com/culture/2026/oct/24/lime-bike-jousts-why-youth-culture-is-embracing-the-medieval-era"),
    ("f1-antonelli", "https://www.theguardian.com/sport/2026/oct/25/kimi-antonelli-storms-to-us-f1-gp-victory-but-is-made-to-wait-for-title-glory")
]

results = []
for name, u in urls:
    try:
        req = urllib.request.Request(u, headers=headers)
        with urllib.request.urlopen(req, timeout=10, context=ctx) as resp:
            print(f"[OK 200] {name}: {u}")
            results.append({"name": name, "url": u, "status": resp.status})
    except Exception as e:
        print(f"[FAIL] {name}: {e}")
        results.append({"name": name, "url": u, "error": str(e)})

with open("c:/Users/teacher/Documents/lessonfactory/news_portal/pipeline/batch21_url_check.json", "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2)
print("Finished testing URLs.")
