import urllib.request

candidates = [
    ("science", "seabird-jet-lag-navigation-nature-study", "https://www.theguardian.com/science/2026/oct/29/jet-lag-throws-seabirds-off-course-nature"),
    ("science", "africa-ebola-outbreak-global-surveillance-uk-health", "https://www.theguardian.com/global-development/2026/oct/28/africa-ebola-outbreak-could-reach-uk-says-top-health-official"),
    ("environment", "queen-of-spain-butterfly-climate-migration-britain", "https://www.theguardian.com/environment/2026/oct/29/queen-of-spain-butterfly-invades-britain-but-will-it-become-native"),
    ("environment", "us-electric-ferries-maritime-decarbonization-transit", "https://www.theguardian.com/environment/2026/oct/29/us-electric-ferries"),
    ("society", "uk-workers-right-to-know-pay-gender-disparities-ehrc", "https://www.theguardian.com/money/2026/oct/28/uk-workers-right-know-colleagues-pay-disparities-gender-pay-gap-discrimination-watchdog-ehrc"),
    ("society", "music-streaming-fatigue-cd-sales-revival-gen-z", "https://www.theguardian.com/music/2026/oct/29/algorithms-make-everything-predictable-music-fans-opting-buy-cds"),
    ("world", "gulf-states-multipart-peace-deal-us-iran-tensions", "https://www.theguardian.com/world/2026/oct/28/gulf-states-multipart-peace-deal-avert-renewal-us-iran-war"),
    ("world", "thames-water-emergency-debt-financing-insolvency-crisis", "https://www.theguardian.com/business/2026/oct/29/thames-water-creditors-vote-emergency-loan-cash-runs-low"),
    ("law", "toblerone-trademark-shape-lawsuit-vegan-chocolate", "https://www.theguardian.com/business/2026/oct/29/toblerone-owner-sues-british-vegan-chocolate-brand-over-chunky-shape"),
    ("law", "datacenter-acoustic-pollution-lawsuit-mississippi", "https://www.theguardian.com/us-news/2026/oct/28/datacenter-noise-lawsuit-elon-musk-mississippi"),
    ("culture", "gullivers-travels-tercentenary-satire-modern-relevance", "https://www.theguardian.com/books/2026/oct/28/gullivers-travels-fans-celebrate-books-jonathan-swift-ireland-dublin"),
    ("entertainment", "doordash-instacart-grocery-delivery-merger-antitrust", "https://www.theguardian.com/business/2026/oct/29/doordash-buys-instacart-grocery-delivery")
]

print("Verifying HTTP status for Batch 26 URLs...")
for cat, slug, url in candidates:
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        with urllib.request.urlopen(req, timeout=8) as resp:
            print(f"[{resp.status}] {slug} -> OK")
    except Exception as e:
        print(f"[FAIL] {slug} -> {e}")
