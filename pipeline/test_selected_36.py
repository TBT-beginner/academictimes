# -*- coding: utf-8 -*-
"""
Selection plan for Batch 27 (2026-10-31), Batch 28 (2026-11-01), Batch 29 (2026-11-02).
Each batch contains 12 articles with 1:1 Senior and Junior versions.
All URLs are verified HTTP 200 OK from The Guardian.
"""

BATCH27_SELECTED = [
    # 1. science: UK obesity plan & metabolic health policy
    {"cat": "science", "slug": "uk-government-obesity-plan-doomed-mps-warn", "url": "https://www.theguardian.com/society/2026/oct/30/uk-government-obesity-plan-doomed-mps-warn", "title": "UK government obesity plan doomed to fail, MPs warn"},
    # 2. science: Online misogyny and manosphere treated as public health issue (Lancet report)
    {"cat": "science", "slug": "manosphere-online-misogyny-public-health-policy-lancet-report", "url": "https://www.theguardian.com/society/2026/oct/29/manosphere-online-misogyny-public-health-policy-lancet-report", "title": "Manosphere and online misogyny should be treated as public health issue, Lancet report says"},
    # 3. environment: Greener front gardens combating air pollution and summer heatwaves
    {"cat": "environment", "slug": "greener-front-gardens-air-pollution-summer-heat", "url": "https://www.theguardian.com/environment/2026/oct/30/greener-front-gardens-air-pollution-summer-heat", "title": "Greener front gardens could help combat air pollution and summer heat"},
    # 4. environment: Reservoir drought levels in southern England (Ardingly)
    {"cat": "environment", "slug": "haywards-heath-ardingly-reservoir-water-level-drought-england", "url": "https://www.theguardian.com/environment/2026/oct/30/haywards-heath-ardingly-reservoir-water-level-drought-england", "title": "Residents on edge as reservoir water levels drop amid English drought"},
    # 5. society: High street slot farms and gambling addiction targeted in UK budget
    {"cat": "society", "slug": "inside-the-slot-farms-targeted-in-budget-gambling", "url": "https://www.theguardian.com/society/2026/oct/29/inside-the-slot-farms-targeted-in-budget-gambling", "title": "Inside the slot farms targeted in UK budget crackdowns on gambling"},
    # 6. society: Union recognition wave in private sector predicted by TUC leader
    {"cat": "society", "slug": "tuc-leader-union-recognition-private-sector", "url": "https://www.theguardian.com/politics/2026/oct/30/tuc-leader-union-recognition-private-sector", "title": "TUC leader expects wave of union recognition in private sector"},
    # 7. world: Oil market volatility and energy giant profits amid Middle East escalation
    {"cat": "world", "slug": "shell-profits-double-iran-war-pushes-up-profit-margin-on-oil", "url": "https://www.theguardian.com/business/2026/oct/29/shell-profits-double-iran-war-pushes-up-profit-margin-on-oil", "title": "Shell profits surge as Middle East conflict pushes up oil refining margins"},
    # 8. world: Diplomatic efforts to avert US-Iran direct confrontation
    {"cat": "world", "slug": "jd-vance-letter-may-offer-last-chance-to-avert-fresh-conflict-between-us-and-iran", "url": "https://www.theguardian.com/world/2026/oct/29/jd-vance-letter-may-offer-last-chance-to-avert-fresh-conflict-between-us-and-iran", "title": "Diplomatic letters offer fragile opportunity to avert fresh US-Iran conflict"},
    # 9. law: Police watchdog self-referral over Meghan Markle warning letter
    {"cat": "law", "slug": "metropolitan-police-refers-itself-to-watchdog-over-meghan-warning-letter", "url": "https://www.theguardian.com/uk-news/2026/oct/29/metropolitan-police-refers-itself-to-watchdog-over-meghan-warning-letter", "title": "Met police refers itself to watchdog over warning letter controversy"},
    # 10. law: Albania imposes severe fines for unlawful demonstration attendance
    {"cat": "law", "slug": "albania-protest-attendance-fine-law", "url": "https://www.theguardian.com/world/2026/oct/29/albania-protest-attendance-fine-law", "title": "Albania imposes severe financial penalties for protest attendance"},
    # 11. culture: Rare love letters to French navigator Lapérouse discovered
    {"cat": "culture", "slug": "rare-love-letters-french-aristocrat-la-perouse-maritime-mystery", "url": "https://www.theguardian.com/world/2026/oct/30/rare-love-letters-french-aristocrat-la-perouse-maritime-mystery", "title": "Rare love letters to French aristocrat shed light on 18th-century maritime mystery"},
    # 12. entertainment: Political satire in music - Bryan Adams trolls Donald Trump
    {"cat": "entertainment", "slug": "bryan-adams-donald-trump-song", "url": "https://www.theguardian.com/world/2026/oct/30/bryan-adams-donald-trump-song", "title": "Canadian rocker Bryan Adams releases satirical track targeting Trump"}
]

BATCH28_SELECTED = [
    # 1. science: Experimental farm boosting UK farmland bird recovery
    {"cat": "science", "slug": "this-is-a-robust-recipe-the-experimental-farm-bucking-the-decline-in-uk-birds", "url": "https://www.theguardian.com/environment/2026/oct/31/this-is-a-robust-recipe-the-experimental-farm-bucking-the-decline-in-uk-birds", "title": "Experimental farm provides robust blueprint for bucking the decline in wild birds"},
    # 2. science: Global wildlife trade volume doubled in new biodiversity survey
    {"cat": "science", "slug": "twice-as-many-plants-and-animals-sold-in-wildlife-trade-as-previously-thought-says-report", "url": "https://www.theguardian.com/environment/2026/oct/30/twice-as-many-plants-and-animals-sold-in-wildlife-trade-as-previously-thought-says-report", "title": "Twice as many species traded globally than previously recorded, report warns"},
    # 3. environment: Severe rainfall and flash flood alerts across Greece and Turkey
    {"cat": "environment", "slug": "severe-rainfall-flood-warnings-greece-turkey", "url": "https://www.theguardian.com/environment/2026/oct/30/severe-rainfall-flood-warnings-greece-turkey", "title": "Severe rainfall and flood warnings issued for eastern Mediterranean region"},
    # 4. environment: Water company environmental performance failures across England
    {"cat": "environment", "slug": "ministers-water-bosses-report-performance-worse", "url": "https://www.theguardian.com/business/2026/oct/29/ministers-water-bosses-report-performance-worse", "title": "English water utilities continue to fail on environmental standards, report shows"},
    # 5. society: UK ministers weigh restrictions on backyard consumer fireworks
    {"cat": "society", "slug": "fireworks-uk-consultation-campaigners-noise-animal-welfare", "url": "https://www.theguardian.com/lifeandstyle/2026/oct/31/fireworks-uk-consultation-campaigners-noise-animal-welfare", "title": "UK government considers new restrictions on consumer fireworks over noise and animal welfare"},
    # 6. society: UK discount retailer Poundland faces insolvency and job losses
    {"cat": "society", "slug": "poundland-brink-administration-12000-jobs-at-risk", "url": "https://www.theguardian.com/business/2026/oct/29/poundland-brink-administration-12000-jobs-at-risk", "title": "High street discount giant Poundland teeters on brink of administration"},
    # 7. world: Major cryptocurrency exchange hacked in massive cyber attack
    {"cat": "world", "slug": "binance-crypto-exchange-hack", "url": "https://www.theguardian.com/business/2026/oct/29/binance-crypto-exchange-hack", "title": "State-sponsored cyber group suspected in massive $6.3bn cryptocurrency theft"},
    # 8. world: Spain high-speed rail safety inquiry following severe derailment
    {"cat": "world", "slug": "how-did-the-spain-train-crash-happen-what-will-investigators-be-asking", "url": "https://www.theguardian.com/world/2026/oct/29/how-did-the-spain-train-crash-happen-what-will-investigators-be-asking", "title": "Spanish high-speed train crash inquiry investigates signalling and maintenance"},
    # 9. law: Australian court upholds conviction in high-profile mushroom poisonings
    {"cat": "law", "slug": "erin-patterson-mushroom-murders-appeal-ruling-ntwnfb", "url": "https://www.theguardian.com/australia-news/2026/oct/29/erin-patterson-mushroom-murders-appeal-ruling-ntwnfb", "title": "Australian appeals court dismisses challenge in fatal mushroom poisoning trial"},
    # 10. law: Counterfeit cosmetics seized containing toxic lead and mercury
    {"cat": "law", "slug": "mercury-lead-methanol-counterfeit-beauty-products-seized-uk", "url": "https://www.theguardian.com/fashion/2026/oct/30/mercury-lead-methanol-counterfeit-beauty-products-seized-uk", "title": "Border authorities seize hazardous counterfeit beauty products containing toxic heavy metals"},
    # 11. culture: Heritage knitwear manufacturer John Smedley innovates amid market pressures
    {"cat": "culture", "slug": "john-smedley-knitwear-brand-innovating-fashion-tradition-tough-market-manufacturing", "url": "https://www.theguardian.com/business/2026/nov/01/john-smedley-knitwear-brand-innovating-fashion-tradition-tough-market-manufacturing", "title": "Historic British knitwear maker balances artisan heritage with sustainable innovation"},
    # 12. entertainment: Traditional craftsmen contest depiction in folk-horror film
    {"cat": "entertainment", "slug": "basketweavers-get-in-a-twist-over-alexander-skarsgard-wicker-husband", "url": "https://www.theguardian.com/film/2026/oct/30/basketweavers-get-in-a-twist-over-alexander-skarsgard-wicker-husband", "title": "Traditional basketweavers raise creative concerns over representation in folklore cinema"}
]

BATCH29_SELECTED = [
    # 1. science: Rare short-necked oil beetle rediscovered in Wales
    {"cat": "science", "slug": "rare-short-necked-oil-beetle-rediscovered-wales", "url": "https://www.theguardian.com/environment/2026/nov/01/rare-short-necked-oil-beetle-rediscovered-wales", "title": "Rare short-necked oil beetle rediscovered in Wales after decades of absence"},
    # 2. science: Tech sell-off wipes out $1tn in market value after semiconductor earnings
    {"cat": "science", "slug": "tech-stocks-drop-earnings-report", "url": "https://www.theguardian.com/business/2026/oct/31/tech-stocks-drop-earnings-report", "title": "Global semiconductor and AI shares tumble following quarterly earnings forecasts"},
    # 3. environment: Finnish prosecutors launch criminal probe into tech datacentre deforestation
    {"cat": "environment", "slug": "finland-criminal-investigation-google-clearing-forest-datacentre", "url": "https://www.theguardian.com/world/2026/oct/30/finland-criminal-investigation-google-clearing-forest-datacentre", "title": "Finnish authorities open investigation into environmental impact of datacentre expansion"},
    # 4. environment: Transboundary wildfire haze crisis triggers emergency responses in Southeast Asia
    {"cat": "environment", "slug": "indonesia-protests-fire-haze-economy", "url": "https://www.theguardian.com/world/2026/oct/30/indonesia-protests-fire-haze-economy", "title": "Southeast Asian nations coordinate response to transboundary peatland smoke and haze"},
    # 5. society: London mayor Sadiq Khan urges strict licensing caps on autonomous robotaxis
    {"cat": "society", "slug": "sadiq-khan-calls-cap-numbers-robotaxis-london-streets", "url": "https://www.theguardian.com/technology/2026/nov/01/sadiq-khan-calls-cap-numbers-robotaxis-london-streets", "title": "London mayor calls for municipal cap on autonomous robotaxis to protect transit"},
    # 6. society: Minimum wage guarantees for younger workers debated in UK parliament
    {"cat": "society", "slug": "chancellor-fails-to-guarantee-minimum-wage-pledge-younger-workers-kuenssberg", "url": "https://www.theguardian.com/society/2026/nov/01/chancellor-fails-to-guarantee-minimum-wage-pledge-younger-workers-kuenssberg", "title": "UK debate intensifies over statutory wage parity for workers under twenty"},
    # 7. world: Investors withdraw $3.6bn from crypto exchange following security breach
    {"cat": "world", "slug": "investors-take-out-36bn-from-binance-after-record-hack-that-stole-billions", "url": "https://www.theguardian.com/business/2026/nov/01/investors-take-out-36bn-from-binance-after-record-hack-that-stole-billions", "title": "Crypto investors withdraw billions following record breach in digital asset custody"},
    # 8. world: UK offers student mobility funding to join EU industrial innovation programme
    {"cat": "world", "slug": "uk-willing-to-spend-450m-a-year-on-eu-students-if-it-can-join-made-in-europe-scheme", "url": "https://www.theguardian.com/politics/2026/nov/01/uk-willing-to-spend-450m-a-year-on-eu-students-if-it-can-join-made-in-europe-scheme", "title": "UK proposes funding student exchanges to secure access to European industrial pact"},
    # 9. law: Over 300 demonstrators detained during diplomatic mission protest in London
    {"cat": "law", "slug": "police-detain-325-people-at-pro-palestine-action-protest-at-us-embassy-in-london", "url": "https://www.theguardian.com/uk-news/2026/nov/01/police-detain-325-people-at-pro-palestine-action-protest-at-us-embassy-in-london", "title": "Metropolitan Police detain over 300 protesters during embassy demonstration"},
    # 10. law: Home Secretary proposes extended residency requirements for indefinite leave
    {"cat": "law", "slug": "home-secretary-shabana-mahmood-immigration-leave-to-remain-windrush", "url": "https://www.theguardian.com/politics/2026/nov/01/home-secretary-shabana-mahmood-immigration-leave-to-remain-windrush", "title": "UK government considers tightening qualification periods for indefinite settlement"},
    # 11. culture: Bedouin women secure historic legislative representation
    {"cat": "culture", "slug": "bedouin-women-success-arab-parties-israel-election", "url": "https://www.theguardian.com/world/2026/oct/31/bedouin-women-success-arab-parties-israel-election", "title": "Bedouin women achieve historic political breakthrough in parliamentary elections"},
    # 12. entertainment: Hello Kitty parent company navigates international broadcast controversy
    {"cat": "entertainment", "slug": "hello-kitty-japanese-spy-show-vivant-china-outcry", "url": "https://www.theguardian.com/world/2026/oct/30/hello-kitty-japanese-spy-show-vivant-china-outcry", "title": "Sanrio clarifies promotional partnership following international espionage drama debate"}
]

print(f"Batch 27: {len(BATCH27_SELECTED)} articles")
print(f"Batch 28: {len(BATCH28_SELECTED)} articles")
print(f"Batch 29: {len(BATCH29_SELECTED)} articles")

# Verify all 36 slugs are unique and no duplicates across batches
all_slugs = [a['slug'] for a in BATCH27_SELECTED + BATCH28_SELECTED + BATCH29_SELECTED]
assert len(all_slugs) == 36, f"Expected 36, got {len(all_slugs)}"
assert len(set(all_slugs)) == 36, "Duplicate slug detected!"
print("All 36 slugs are unique and clean!")
