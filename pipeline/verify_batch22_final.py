import urllib.request
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

urls = [
    ("world", "https://www.theguardian.com/world/2026/oct/24/kim-jong-un-crosses-newly-opened-bridge-into-china"),
    ("society", "https://www.theguardian.com/world/2026/oct/24/hundreds-of-thousands-march-across-france-in-protests-over-schools-and-policing"),
    ("law", "https://www.theguardian.com/us-news/2026/oct/24/california-noncitizen-voting-trump-administration"),
    ("law", "https://www.theguardian.com/law/2026/oct/24/icc-deputy-prosecutor-nazhat-shameem-khan-marco-rubio-us-sanctions"),
    ("culture", "https://www.theguardian.com/books/2026/oct/25/ireland-wales-children-laureates-chris-haughton-nicola-davies-sally-rooney-royalties-ban-on-uk-sales"),
    ("culture", "https://www.theguardian.com/books/2026/oct/25/stephen-fry-sherlock-holmes-altered-the-course-of-my-whole-life"),
    ("environment", "https://www.theguardian.com/environment/2026/oct/25/cabinet-split-emerges-over-controversial-rosebank-oilfield-decision"),
    ("environment", "https://www.theguardian.com/environment/2026/oct/25/corvo-azores-corys-shearwaters-switch-off-saving-seabirds-aoe"),
    ("tech", "https://www.theguardian.com/technology/2026/oct/25/synthetic-twin-why-socceroo-cristian-volpato-is-the-latest-footballer-to-license-his-ai-clone"),
    ("tech", "https://www.theguardian.com/technology/2026/oct/25/traintok-trend-train-spotters-rail-staff-videos"),
    ("science", "https://www.theguardian.com/science/2026/oct/25/plague-risks-in-russia-and-a-dangerous-delay-on-who-pandemic-agreement"),
    ("society", "https://www.theguardian.com/uk-news/2026/oct/24/can-john-healey-make-a-dent-in-the-cost-of-living-crisis-in-his-first-budget")
]

all_ok = True
for cat, u in urls:
    try:
        req = urllib.request.Request(u, headers=headers)
        with urllib.request.urlopen(req, timeout=10, context=ctx) as r:
            if r.status == 200:
                print(f"[200 OK] ({cat}) {u}")
            else:
                print(f"[{r.status}] {u}")
                all_ok = False
    except Exception as e:
        print(f"[FAIL] {u}: {e}")
        all_ok = False

if all_ok:
    print("\nALL 12 URLS VERIFIED 100% HTTP 200 OK!")
