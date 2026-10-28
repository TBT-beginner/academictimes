import urllib.request

candidates = [
    # 1. Environment / Energy: Sizewell C Nuclear Plant deal
    ("science", "uk-sizewell-nuclear-plant-deal-taxpayer-mps-warning", "https://www.theguardian.com/business/2026/oct/28/plan-for-multibillion-pound-sizewell-nuclear-plant-a-terrible-deal-for-uk-taxpayers-mps-say"),
    # 2. Science / Environment: Venice Lagoon sea rise transformation
    ("science", "venice-lagoon-rising-seas-dry-land-submergence", "https://www.theguardian.com/science/2026/oct/28/rising-seas-transformed-dry-land-venice-lagoon"),
    # 3. Environment: Low-interest loans for home solar panels and heat pumps
    ("environment", "uk-homes-low-interest-loans-solar-heat-pumps", "https://www.theguardian.com/environment/2026/oct/27/homes-across-uk-to-get-low--or-no-interest-loans-to-fund-solar-panels-and-heat-pumps"),
    # 4. Science / Health: Ferritin face social media iron deficiency claims
    ("science", "ferritin-face-social-media-claims-iron-deficiency-risks", "https://www.theguardian.com/science/2026/oct/28/ferritin-face-social-media-claims-iron-deficiency"),
    # 5. Society: Emergency stockpile bottled water and tinned food sales surge
    ("society", "uk-emergency-stockpile-advice-bottled-water-food-surge", "https://www.theguardian.com/society/2026/oct/27/bottled-water-and-tinned-food-sales-surge-after-uk-government-issues-emergency-stockpile-advice"),
    # 6. Society / Tech: Gen Z digital detox apps and dumbphones
    ("society", "gen-z-digital-detox-apps-dumbphones-screen-time", "https://www.theguardian.com/technology/2026/oct/27/gen-z-digital-detox-apps"),
    # 7. World: Spain high-speed train collision investigation
    ("world", "spain-high-speed-train-crash-investigation-toledo", "https://www.theguardian.com/world/2026/oct/28/spain-train-crash-high-speed-toledo"),
    # 8. World / Politics: Israel election exit polls tie Netanyahu and Eisenkot
    ("world", "israel-election-results-netanyahu-eisenkot-deadlock", "https://www.theguardian.com/world/2026/oct/28/israel-election-exit-polls-suggest-netanyahu-eisenkot-blocs-tied-ntwnfb"),
    # 9. World: King Charles to address legacy of slavery at Commonwealth summit
    ("world", "king-charles-commonwealth-summit-slavery-legacy-reparations", "https://www.theguardian.com/world/2026/oct/28/king-charles-confirms-he-will-discuss-legacy-of-slavery-at-commonwealth-summit"),
    # 10. Law / Culture: Bafta trustees charity law scrutiny over guest tickets
    ("law", "bafta-trustees-charity-law-free-guest-tickets-scrutiny", "https://www.theguardian.com/culture/2026/oct/28/bafta-trustees-charity-law-accepting-free-guest-tickets"),
    # 11. Culture: Rolling Stones historical Charlie Watts letter on Brian Jones auction
    ("culture", "rolling-stones-charlie-watts-letter-brian-jones-auction", "https://www.theguardian.com/music/2026/oct/28/charlie-watts-brian-jones-letter-rolling-stones-auction"),
    # 12. Entertainment / Tech: ABC Australia legal action over political cartoon using Bluey
    ("entertainment", "bluey-copyright-dispute-abc-australia-one-nation-cartoon", "https://www.theguardian.com/tv-and-radio/2026/oct/27/abc-to-take-legal-action-after-right-wing-one-nation-party-used-bluey-in-shocking-and-disrespectful-cartoon-ntwnfb"),
]

print("Checking HTTP status for candidate URLs...")
for cat, slug, url in candidates:
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as resp:
            print(f"[{resp.status}] {slug} -> OK")
    except Exception as e:
        print(f"[FAIL] {slug} -> {e}")
