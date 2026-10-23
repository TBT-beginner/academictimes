import urllib.request

urls = [
    "https://www.theguardian.com/global-development/2026/oct/22/have-scientists-finally-found-a-way-to-save-the-banana-from-disaster",
    "https://www.theguardian.com/world/2026/oct/22/shamonda-virus-detected-in-human-first-time-france",
    "https://www.theguardian.com/news/2026/oct/23/the-great-moth-revival-how-bogongs-have-bounced-back",
    "https://www.theguardian.com/environment/2026/oct/22/cop17-cali-conservation-fund-pharmaceutical-freeriding-nature-aoe",
    "https://www.theguardian.com/environment/ng-interactive/2026/oct/22/finland-google-felling-trees-datacentre",
    "https://www.theguardian.com/environment/2026/oct/22/thousands-of-butterflies-surprise-experts-on-restored-west-sussex-farmland",
    "https://www.theguardian.com/culture/2026/oct/22/canadian-publisher-boreal-ends-relationship-author-thelyson-orelien-over-ai",
    "https://www.theguardian.com/technology/2026/oct/22/websites-across-world-hit-by-millions-of-attempts-to-exploit-php-code-flaw",
    "https://www.theguardian.com/australia-news/2026/oct/23/australian-astronaut-katherine-bennell-pegg-2028-space-mission",
    "https://www.theguardian.com/world/2026/oct/22/canada-alberta-migrant-workers",
    "https://www.theguardian.com/society/2026/oct/23/child-health-england-at-risk-sharp-rise-nhs-waiting-times",
    "https://www.theguardian.com/australia-news/2026/oct/22/airbnb-guests-freed-from-chores-involving-significant-effort-under-new-global-rules"
]

headers = {'User-Agent': 'Mozilla/5.0'}

all_ok = True
for u in urls:
    try:
        req = urllib.request.Request(u, headers=headers)
        res = urllib.request.urlopen(req, timeout=8)
        print(f"[STATUS {res.status}] {u}")
    except Exception as e:
        print(f"[FAIL] {u} -> {e}")
        all_ok = False

if all_ok:
    print("\nALL 12 URLS ARE 100% LIVE (HTTP 200 OK)!")
else:
    print("\nSOME URLS FAILED!")
