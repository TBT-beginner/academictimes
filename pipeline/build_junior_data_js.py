# -*- coding: utf-8 -*-
"""
Generates news_portal/junior/js/junior-data.js
Contains all 15 Junior articles, daily edition mappings, and high-school study/media guides.
"""

import os
import json
import re
from junior_articles_data import JUNIOR_ARTICLES

PORTAL_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
JUNIOR_JS_DIR = os.path.join(PORTAL_DIR, "junior", "js")
os.makedirs(JUNIOR_JS_DIR, exist_ok=True)

DATE_MAP = {
    "soai-reaction-nobel-chemistry": "2026-10-10",
    "regulatory-t-cells-nobel-breakthrough": "2026-10-10",
    "smart-glasses-ai-privacy": "2026-10-09",
    "japan-semiconductor-revival-rapidus": "2026-10-09",
    "digital-school-backpack-reform": "2026-10-09",
    "esports-highschool-education": "2026-10-09",
    "global-plastics-treaty-negotiations": "2026-10-09",
    "cashless-society-local-bus-crisis": "2026-10-09",
    "perovskite-solar-cells-commercialization": "2026-10-09",
    "space-debris-corporate-liability": "2026-10-09",
    "handwriting-cognitive-benefits": "2026-10-09",
    "remote-work-suburban-revitalization": "2026-10-09",
    "ai-music-copyright-royalties": "2026-10-09",
    "ai-energy-nuclear-data-centers": "2026-10-09",
    "headphones-in-public": "2026-10-06",
    "psychology-casual-encounters": "2026-10-06",
    "critical-minerals-geopolitics": "2026-10-06",
    "air-defence-shield": "2026-10-05",
    "royal-security-judicial-review": "2026-10-05",
    "clarkson-business-red-tape": "2026-10-05",
    "colorectal-cancer-under-50s": "2026-10-04",
    "mediterranean-marine-heatwaves": "2026-10-04",
    "ai-pediatric-diagnosis-consent": "2026-10-03",
    "generative-ai-paleontology": "2026-10-03",
    "arctic-sea-route-unclos": "2026-10-03",
    "inheritance-tax-reform-debate": "2026-10-02",
    "stoic-philosophy-digital-age": "2026-10-02",
    "jeffrey-archer-obituary": "2026-10-01",
    "raf-fairford-bomber-redeployment": "2026-10-01"
}

MEDIA_KEY_MAP = {
    "soai-reaction-nobel-chemistry": "jiji",
    "regulatory-t-cells-nobel-breakthrough": "jiji",
    "smart-glasses-ai-privacy": "getnews",
    "japan-semiconductor-revival-rapidus": "jiji",
    "digital-school-backpack-reform": "yahoo",
    "esports-highschool-education": "getnews",
    "global-plastics-treaty-negotiations": "jiji",
    "cashless-society-local-bus-crisis": "yahoo",
    "perovskite-solar-cells-commercialization": "jiji",
    "space-debris-corporate-liability": "ft",
    "handwriting-cognitive-benefits": "time",
    "remote-work-suburban-revitalization": "yahoo",
    "ai-music-copyright-royalties": "getnews",
    "ai-energy-nuclear-data-centers": "reuters",
    "headphones-in-public": "time",
    "colorectal-cancer-under-50s": "nature",
    "psychology-casual-encounters": "the-conversation",
    "air-defence-shield": "the-times",
    "critical-minerals-geopolitics": "ft",
    "jeffrey-archer-obituary": "the-guardian",
    "stoic-philosophy-digital-age": "time",
    "generative-ai-paleontology": "science-mag",
    "mediterranean-marine-heatwaves": "nature",
    "clarkson-business-red-tape": "ft",
    "inheritance-tax-reform-debate": "ft",
    "ai-pediatric-diagnosis-consent": "the-guardian",
    "royal-security-judicial-review": "the-times",
    "arctic-sea-route-unclos": "the-times",
    "raf-fairford-bomber-redeployment": "reuters"
}

EDITIONS_DATA = {
    "2026-10-26": {
        "dateStr": "Monday October 26 2026",
        "editionLabel": "2026年10月26日 (月) 号 【本日付・最新・全12記事】",
        "tagline": "特集：セルビアの歴史的選挙と学生の力・ブラジル大統領選・古代ローマの変色ガラス・中世ごっこの大流行",
        "topLeadSlug": "serbian-election-vucic-concedes-defeat-student-movement",
        "subLeadSlugs": ["brazil-presidential-runoff-lula-flavio-bolsonaro-polarization", "ancient-roman-colour-changing-glass-nanotechnology-rediscovered", "ai-copyright-training-data-smart-fund-creators-compensation"],
        "leftDispatches": ["un-secretary-general-race-emirati-diplomat-lana-nusseibeh", "venezuela-opposition-leader-machado-returns-democratic-transition", "uk-datacentre-power-water-strain-public-protest-risk", "australian-climate-data-scrutiny-bom-temperature-records"],
        "rightDigestSlugs": ["ten-days-shake-democratic-norms-four-continents-elections", "uk-government-be-ready-emergency-stockpile-campaign", "medievalcore-youth-culture-lime-bike-jousts-subversion", "kimi-antonelli-f1-us-grand-prix-mercedes-youngest-champion"]
    },
    "2026-10-24": {
        "dateStr": "Saturday October 24 2026",
        "editionLabel": "2026年10月24日 (土) 号 【全12記事・アーカイブ】",
        "tagline": "特集：子犬の生中継と健康な暮らし・スマホ写真で守る美しい砂浜",
        "topLeadSlug": "finnish-24-hour-puppy-livestream-tv-hit",
        "subLeadSlugs": ["weight-loss-drugs-beer-sales-heineken-pubs", "citizen-science-tracking-global-coastal-erosion", "uk-children-social-media-harm-ofcom-online-safety-act"],
        "leftDispatches": ["telegraph-job-cuts-ai-powered-newsroom-transformation", "historic-england-oldest-surviving-inns-archaeology", "james-bond-casting-emotional-audition-rigor", "glacier-retreat-western-mountains-hydrological-crisis"],
        "rightDigestSlugs": ["ukraine-starlink-satellite-network-battlefield-vulnerabilities", "deepfake-election-video-spain-digital-disinformation", "winter-energy-price-disparity-britain-household-strain", "storm-austen-south-west-england-power-grid-disruption"]
    },
    "2026-10-23": {
        "dateStr": "Friday October 23 2026",
        "editionLabel": "2026年10月23日 (金) 号 【全12記事・アーカイブ】",
        "tagline": "特集：バナナの危機を救う科学・ボゴン蛾の復活と宇宙飛行士の挑戦",
        "topLeadSlug": "scientists-race-save-bananas-panama-disease-extinction",
        "subLeadSlugs": ["shamonda-virus-detected-human-first-time-france-zoonosis", "bogong-moth-population-recovery-alpine-ecosystem", "cop17-conservation-fund-pharmaceutical-free-riding-nature"],
        "leftDispatches": ["finland-google-fells-trees-ai-datacentre-environmental-backlash", "thousands-butterflies-flourish-restored-sussex-farmland-rewilding", "canadian-publisher-ends-ties-author-alleged-ai-novel-use", "millions-exploit-attempts-target-php-flaw-global-cyber-defense"],
        "rightDigestSlugs": ["australia-nominates-astronaut-katherine-bennell-pegg-space-station", "canada-alberta-migrant-workers-rights-restrictions-controversy", "child-health-england-nhs-waiting-times-surge-pediatric-crisis", "airbnb-bans-excessive-guest-chores-global-hospitality-standards"]
    },
    "2026-10-22": {
        "dateStr": "Thursday October 22 2026",
        "editionLabel": "2026年10月22日 (木) 号 【全12記事・アーカイブ】",
        "tagline": "特集：オランウータンの笑い声と大人のひらめき・ネットの安全とサメの救出",
        "topLeadSlug": "orangutans-prefer-food-laughter-sounds-study",
        "subLeadSlugs": ["creativity-aging-cognitive-flexibility-knowledge-synthesis", "critical-php-vulnerability-triggers-global-website-shutdowns", "un-warns-emissions-must-fall-eighteen-percent-in-four-years"],
        "leftDispatches": ["bad-apple-effect-social-contagion-rule-breaking-study", "svalbard-village-confronts-rapid-arctic-heating-permafrost", "taiwan-indicts-cross-border-plot-targeting-political-satirist", "trapped-shark-in-busan-canal-freed-after-citizen-vigil"],
        "rightDigestSlugs": ["literary-prize-books-co-written-with-ai-launched", "music-fans-reject-synthetic-ai-tracks-human-authenticity", "penicillin-allergy-misdiagnosis-strains-antibiotic-stewardship", "nsw-legalizes-human-composting-green-burial-bioethics"]
    },
    "2026-10-21": {
        "dateStr": "Wednesday October 21 2026",
        "editionLabel": "2026年10月21日 (水) 号 【全12記事・アーカイブ】",
        "tagline": "特集：国連IPCC第7次報告書延期・北極永久凍土融解と水道水・北海ガス田再承認・NATO黒海監視ドローン",
        "topLeadSlug": "ipcc-seventh-assessment-report-delay-climate-diplomacy",
        "subLeadSlugs": ["arctic-permafrost-thaw-toxic-metals-drinking-water", "jackdaw-north-sea-gas-field-approval-climate-litigation", "nato-black-sea-maritime-surveillance-grain-corridor"],
        "leftDispatches": ["ai-workplace-limitations-human-judgment-ethics", "ai-synthetic-bioweapons-threat-global-security", "australia-eu-free-trade-agreement-agricultural-tariffs", "guinea-bissau-vaccine-trial-raid-global-health-ethics"],
        "rightDigestSlugs": ["theranos-corporate-fraud-streaming-viewership-surge", "myanmar-aung-san-suu-kyi-diplomatic-royal-gift", "us-midterm-elections-voter-sentiment-economic-anxiety", "southern-europe-youth-protests-housing-affordability"]
    },
    "2026-10-20": {
        "dateStr": "Tuesday October 20 2026",
        "editionLabel": "2026年10月20日 (火) 号 【全12記事・アーカイブ】",
        "tagline": "特集：迷惑インフルエンサー撮影禁止・図書館に迷い込んだ黒クマ・オリオン座流星群・海鳥のV字回復",
        "topLeadSlug": "social-media-influencer-photography-bans-hospitality-tourism",
        "subLeadSlugs": ["black-bear-wanders-california-public-library", "orionid-meteor-shower-peaks-halley-comet-debris", "seabird-population-recovery-solent-avian-flu"],
        "leftDispatches": ["urban-air-pollution-health-inequality-inquiry", "britain-eu-security-pact-geopolitical-realignment", "french-civil-unrest-policing-tactics-scrutiny", "aviation-accessibility-statutory-safeguards-disabled-passengers"],
        "rightDigestSlugs": ["corporate-profit-warnings-energy-shocks-supply-chains", "rural-maternity-units-staffing-crisis-nhs", "austrian-heirloom-apple-orchards-biodiversity-revival", "documentary-cinema-modern-corporate-fraud-spectacle"]
    },
    "2026-10-19": {
        "dateStr": "Monday October 19 2026",
        "editionLabel": "2026年10月19日 (月) 号 【全12記事・アーカイブ】",
        "tagline": "特集：森の秘薬イボガを守れ・住宅断熱と光熱費・やり直すチャンスを支える刑務所教育・リスボンとミラノの住宅デモ",
        "topLeadSlug": "gabon-iboga-sacred-plant-addiction-treatment-biopiracy",
        "subLeadSlugs": ["heat-pumps-building-insulation-energy-transition-study", "penal-reform-prison-overcrowding-rehabilitation-barriers", "european-housing-crisis-short-term-rentals-unrest"],
        "leftDispatches": ["public-transit-acoustic-etiquette-civic-campaign", "world-bank-ai-governance-developing-economies", "industrial-energy-tariffs-green-steelmaking-subsidies", "iot-botnet-cyber-threats-financial-clearing-houses"],
        "rightDigestSlugs": ["climate-communication-fatalism-constructive-agency", "sarah-forbes-bonetta-biography-victorian-empire", "afrobeats-performance-culture-lagos-hype-phenomenon", "australian-literature-tim-winton-national-canon"]
    },
    "2026-10-18": {
        "dateStr": "Sunday October 18 2026",
        "editionLabel": "2026年10月18日 (日) 号 【全12記事・アーカイブ】",
        "tagline": "特集：火星の月フォボス探査MMX・8年前の血液検査で腸の難病発見・職場の熱中症対策・サルデーニャ島の長寿の秘密",
        "topLeadSlug": "japan-jaxa-mmx-phobos-sample-return-mission",
        "subLeadSlugs": ["inflammatory-bowel-disease-blood-biomarkers-early-prediction", "occupational-heat-stress-statutory-workplace-protections", "sardinian-blue-zone-female-centenarians-longevity"],
        "leftDispatches": ["youth-unemployment-neet-welfare-reform-review", "epa-pfas-forever-chemicals-regulatory-backtrack", "non-consensual-deepfakes-criminalization-european-parliament", "uk-eu-cross-border-law-enforcement-pact"],
        "rightDigestSlugs": ["shakespeare-authorship-edward-iii-computational-stylistics", "medieval-romance-origins-modern-fantasy-literature", "wikipedia-human-curation-ai-content-pollution", "autonomous-ai-worms-cybersecurity-vulnerabilities"]
    },
    "2026-10-17": {
        "dateStr": "Saturday October 17 2026",
        "editionLabel": "2026年10月17日 (土) 号 【全12記事・アーカイブ】",
        "tagline": "特集：パフィン鳥の生き抜く力・ミツバチと野生ハナバチ・若者応援の職業訓練・ハリケーンから身を守る防災",
        "topLeadSlug": "puffin-seabird-climate-resilience-hope",
        "subLeadSlugs": ["honeybees-competition-wild-pollinators-biodiversity", "workforce-retraining-youth-apprenticeships-levy", "hurricane-trudy-pacific-coastal-resilience"],
        "leftDispatches": ["nhs-medical-records-privacy-breach-dismissals", "us-corporate-lobbying-eu-deforestation-regulation", "nhs-hospital-trusts-reject-palantir-data-platform", "oecd-warns-populist-economic-policies-cost-of-living"],
        "rightDigestSlugs": ["isabel-allende-premio-planeta-pseudonym", "as-byatt-literary-archive-british-library", "bespoke-coachbuilding-luxury-automotive-craftsmanship", "uk-ai-safety-institute-counter-extremism-testing"]
    },
    "2026-10-16": {
        "dateStr": "Friday October 16 2026",
        "editionLabel": "2026年10月16日 (金) 号 【全12記事・アーカイブ】",
        "tagline": "特集：世界計量会議「うるう秒」廃止とうるう時導入・シャニダール洞窟旧人類投槍・イングランド6地域深刻干ばつ宣言",
        "topLeadSlug": "leap-second-abolition-leap-hour",
        "subLeadSlugs": ["neanderthal-shanidar-spear-trauma", "england-six-regions-severe-drought-water-crisis", "indonesia-wildfire-haze-dry-ice-cloud-seeding"],
        "leftDispatches": ["made-in-europe-green-subsidies-uk-accord", "brazil-statutory-workweek-reduction-forty-hours", "zero-click-spyware-digital-advertising-exploitation", "sand-tiger-shark-conservation-public-aquariums"],
        "rightDigestSlugs": ["uk-chancellor-bank-windfall-tax-fiscal-consolidation", "the-floating-world-art-market-capitalism-ethics", "national-digital-sovereignty-cloud-infrastructure", "satellite-constellation-dual-use-defence-dispute"]
    },
    "2026-10-15": {
        "dateStr": "Thursday October 15 2026",
        "editionLabel": "2026年10月15日 (木) 号 【全12記事・アーカイブ】",
        "tagline": "特集：【過去の基礎論文解説】ノーベル賞AI「AlphaFold 3」・【過去のニュース深掘り】学校のスマホ禁止・英語の音を聞く力・ヨーロッパの自然エネルギー",
        "topLeadSlug": "alphafold-3-biomolecular-structure-prediction",
        "subLeadSlugs": ["phonetic-focus-foreign-language-acquisition", "england-school-chain-phone-free-policy", "renewables-overtake-fossil-fuels-eu-electricity"],
        "leftDispatches": ["four-day-workweek-uk-trial-permanent", "eu-ai-act-consumer-rights-enforcement", "mont-blanc-glacier-melt-elevation-loss", "smart-glasses-parliament-privacy-controversy"],
        "rightDigestSlugs": ["us-newspapers-openai-copyright-lawsuit", "orbital-samantha-harvey-booker-prize", "gen-z-physical-books-library-renaissance", "england-organic-farming-expansion-target"]
    },
    "2026-10-14": {
        "dateStr": "Wednesday October 14 2026",
        "editionLabel": "2026年10月14日 (水) 号 【全30記事・アーカイブ】",
        "tagline": "特集：全固体ナトリウムイオン電池・ネット貿易の世界的ルール・デジタル遺産の行方・観光と地域交通",
        "topLeadSlug": "solid-state-sodium-ion-battery-breakthrough",
        "subLeadSlugs": ["wto-electronic-commerce-moratorium-negotiations", "supreme-court-probate-digital-asset-passwords", "local-train-revitalization-community-tourism-passes"],
        "leftDispatches": ["crispr-epigenetic-silencing-chronic-pain", "school-attendance-counseling-vr-classrooms", "iaea-small-modular-reactor-safety-standards"],
        "rightDigestSlugs": ["digital-nostalgia-analog-media-generation-z", "exoplanet-atmospheric-carbon-biosignature-jwst", "ocean-acidification-deepwater-coral-calcification", "neuromorphic-spiking-chips-edge-ai-robotics"]
    },
    "2026-10-13": {
        "dateStr": "Tuesday October 13 2026",
        "editionLabel": "2026年10月13日 (火) 号 【全30記事・アーカイブ】",
        "tagline": "特集：二酸化炭素を食べる細菌・世界の自然を守る約束・テレワークと働くルール・高齢者にやさしい街づくり",
        "topLeadSlug": "synthetic-biology-co2-eating-bacteria-enzymes",
        "subLeadSlugs": ["un-cop16-biodiversity-fund-cali-framework", "supreme-court-worker-classification-remote-telecommuters", "elderly-pedestrian-traffic-safety-urban-redesign"],
        "leftDispatches": ["alzheimers-blood-biomarker-early-detection", "youth-mental-health-smartphone-ban-boarding-schools", "eu-ai-act-high-risk-algorithm-enforcement"],
        "rightDigestSlugs": ["philosophical-ethics-deepfake-historical-figures", "perovskite-silicon-tandem-solar-efficiency-record", "antarctic-ice-shelf-subglacial-meltwater-dynamics", "quantum-dot-infrared-imaging-cancer-margins"]
    },
    "2026-10-11": {
        "dateStr": "Sunday October 11 2026",
        "editionLabel": "2026年10月11日 (日) 号 【全30記事・アーカイブ】",
        "tagline": "特集：宇宙のブラックホールの謎・気候変動と難民問題・自動運転バス・SNSトラブルの解決ルール",
        "topLeadSlug": "james-webb-early-universe-supermassive-black-holes",
        "subLeadSlugs": ["unsc-climate-security-conflict-refugee-nexus", "g20-pillar-two-global-minimum-corporate-tax", "supreme-court-sns-slander-speedy-disclosure-ruling"],
        "leftDispatches": ["autonomous-bus-pilot-aging-rural-towns", "personalized-mrna-cancer-vaccine-phase3", "rural-kabuki-digital-archive-vr-preservation"],
        "rightDigestSlugs": ["fusion-high-temperature-superconducting-magnets", "deep-sea-microplastics-thermohaline-plankton-flux", "inquiry-based-learning-university-admissions", "micro-fluidic-haptic-controllers-handheld-gaming"]
    },
    "2026-10-10": {
        "dateStr": "Saturday October 10 2026",
        "editionLabel": "2026年10月10日 (土) 号 【全30記事・フルアーカイブ】",
        "tagline": "特集：ノーベル化学賞硤合教授・坂口特任教授免疫革新・AIデータセンター・食料品消費税減税",
        "topLeadSlug": "soai-reaction-nobel-chemistry",
        "subLeadSlugs": ["regulatory-t-cells-nobel-breakthrough", "food-sales-tax-cut-income-benefits", "ukraine-drone-strike-yandex-ai-datacenter"],
        "leftDispatches": ["supreme-court-sheet-music-piracy-ruling", "japan-icc-sanctions-rule-of-law", "pnas-ai-biodiversity-monitoring"],
        "rightDigestSlugs": ["wwf-living-planet-biodiversity-collapse", "commercial-fusion-reactor-engineering", "kyocera-ceramic-coating-vacuum-tumblers", "dementia-smart-home-minder-system"]
    },
    "2026-10-09": {
        "dateStr": "Friday October 9 2026",
        "editionLabel": "2026年10月9日 (金) 号 【全30記事・フルアーカイブ】",
        "tagline": "特集：ノーベル物理学賞AI基盤・ラピダス半導体・全固体電池・同性婚最高裁審理",
        "topLeadSlug": "nobel-physics-hopfield-hinton-machine-learning",
        "subLeadSlugs": ["japan-semiconductor-revival-rapidus", "solid-state-battery-ev-commercial-trial"],
        "leftDispatches": ["asean-summit-vientiane-south-china-sea-code", "traditional-sake-unesco-intangible-cultural-heritage", "cloud-gaming-latency-low-earth-orbit-satellite"],
        "rightDigestSlugs": ["supreme-court-same-sex-marriage-constitution", "dual-earner-childcare-leave-wage-replacement", "generative-ai-fair-use-copyright-lawsuit", "digital-detox-camps-youth-neuroplasticity"]
    },
    "2026-10-08": {
        "dateStr": "Thursday October 8 2026",
        "editionLabel": "2026年10月8日 (木) 号 【バックナンバー】",
        "tagline": "特集：クリーンエネルギーに必要な鉱物の争奪戦とスマホ時代の心の整理",
        "topLeadSlug": "critical-minerals-geopolitics",
        "subLeadSlugs": ["stoic-philosophy-digital-age", "mediterranean-marine-heatwaves"],
        "leftDispatches": ["psychology-casual-encounters", "air-defence-shield", "colorectal-cancer-under-50s"],
        "rightDigestSlugs": ["headphones-in-public", "clarkson-business-red-tape", "inheritance-tax-reform-debate", "ai-pediatric-diagnosis-consent"]
    },
    "2026-10-07": {
        "dateStr": "Wednesday October 7 2026",
        "editionLabel": "2026年10月7日 (水) 号 【バックナンバー】",
        "tagline": "特集：ちょっとした挨拶の魔法と氷が解ける北極海航路のルール",
        "topLeadSlug": "psychology-casual-encounters",
        "subLeadSlugs": ["arctic-sea-route-unclos", "generative-ai-paleontology"],
        "leftDispatches": ["critical-minerals-geopolitics", "royal-security-judicial-review", "raf-fairford-bomber-redeployment"],
        "rightDigestSlugs": ["headphones-in-public", "stoic-philosophy-digital-age", "colorectal-cancer-under-50s", "air-defence-shield"]
    },
    "2026-10-06": {
        "dateStr": "Tuesday October 6 2026",
        "editionLabel": "2026年10月6日 (火) 号 【バックナンバー】",
        "tagline": "特集：静かな時間の力（イヤホン論争）と見知らぬ人への挨拶の魔法",
        "topLeadSlug": "headphones-in-public",
        "subLeadSlugs": ["colorectal-cancer-under-50s", "psychology-casual-encounters"],
        "leftDispatches": ["air-defence-shield", "critical-minerals-geopolitics", "raf-fairford-bomber-redeployment"],
        "rightDigestSlugs": ["clarkson-business-red-tape", "inheritance-tax-reform-debate", "ai-pediatric-diagnosis-consent", "mediterranean-marine-heatwaves"]
    },
    "2026-10-05": {
        "dateStr": "Monday October 5 2026",
        "editionLabel": "2026年10月5日 (月) 号 【バックナンバー】",
        "tagline": "特集：国の空を守る防衛計画と王室警護・お役所ルール論争",
        "topLeadSlug": "air-defence-shield",
        "subLeadSlugs": ["royal-security-judicial-review", "clarkson-business-red-tape"],
        "leftDispatches": ["headphones-in-public", "inheritance-tax-reform-debate", "mediterranean-marine-heatwaves"],
        "rightDigestSlugs": ["jeffrey-archer-obituary", "ai-pediatric-diagnosis-consent", "colorectal-cancer-under-50s", "raf-fairford-bomber-redeployment"]
    },
    "2026-10-04": {
        "dateStr": "Sunday October 4 2026",
        "editionLabel": "2026年10月4日 (日) 号 【バックナンバー】",
        "tagline": "特集：若い世代の病気の謎と地中海の海の温暖化・魚たちの危機",
        "topLeadSlug": "colorectal-cancer-under-50s",
        "subLeadSlugs": ["mediterranean-marine-heatwaves", "generative-ai-paleontology"],
        "leftDispatches": ["ai-pediatric-diagnosis-consent", "psychology-casual-encounters", "inheritance-tax-reform-debate"],
        "rightDigestSlugs": ["headphones-in-public", "air-defence-shield", "clarkson-business-red-tape", "jeffrey-archer-obituary"]
    },
    "2026-10-03": {
        "dateStr": "Saturday October 3 2026",
        "editionLabel": "2026年10月3日 (土) 号 【バックナンバー】",
        "tagline": "特集：子どものAI診断と恐竜の歩き方・氷が解ける北極海航路",
        "topLeadSlug": "ai-pediatric-diagnosis-consent",
        "subLeadSlugs": ["generative-ai-paleontology", "arctic-sea-route-unclos"],
        "leftDispatches": ["clarkson-business-red-tape", "colorectal-cancer-under-50s", "jeffrey-archer-obituary"],
        "rightDigestSlugs": ["headphones-in-public", "mediterranean-marine-heatwaves", "psychology-casual-encounters", "critical-minerals-geopolitics"]
    },
    "2026-10-02": {
        "dateStr": "Friday October 2 2026",
        "editionLabel": "2026年10月2日 (金) 号 【バックナンバー】",
        "tagline": "特集：相続税をめぐる議論と古代ストア哲学・スマホ時代の心の整理",
        "topLeadSlug": "inheritance-tax-reform-debate",
        "subLeadSlugs": ["stoic-philosophy-digital-age", "psychology-casual-encounters"],
        "leftDispatches": ["raf-fairford-bomber-redeployment", "royal-security-judicial-review", "generative-ai-paleontology"],
        "rightDigestSlugs": ["air-defence-shield", "colorectal-cancer-under-50s", "headphones-in-public", "critical-minerals-geopolitics"]
    },
    "2026-10-01": {
        "dateStr": "Thursday October 1 2026",
        "editionLabel": "2026年10月1日 (木) 号 【創刊バックナンバー】",
        "tagline": "特集：ヨーロッパの空の安全とベストセラー作家J・アーチャーの生涯",
        "topLeadSlug": "raf-fairford-bomber-redeployment",
        "subLeadSlugs": ["jeffrey-archer-obituary", "generative-ai-paleontology"],
        "leftDispatches": ["air-defence-shield", "inheritance-tax-reform-debate", "mediterranean-marine-heatwaves"],
        "rightDigestSlugs": ["clarkson-business-red-tape", "psychology-casual-encounters", "royal-security-judicial-review", "critical-minerals-geopolitics"]
    }
}

JUNIOR_STUDY_RESOURCES = [
    {
        "key": "time",
        "title_en": "TIME Magazine",
        "title_ja": "米・オピニオン週刊誌",
        "name": "TIME Magazine (米・オピニオン週刊誌)",
        "badge": "🎯 英検2級・準1級・共通テスト最頻出",
        "point": "日常の習慣（イヤホン、スマホ、睡眠）を題材にしながら、社会の大きな変化を分かりやすく問いかけるエッセイの宝庫です。段落ごとの主張の流れがとてもクリアで、自由英作文のお手本になります。",
        "tip": "各段落の第1文（トピックセンテンス）を拾い読みするだけで、全体の論理展開が掴めるようになります。"
    },
    {
        "key": "the-times",
        "title_en": "The Times",
        "title_ja": "英・本格高級日刊紙",
        "name": "The Times (英・本格高級日刊紙)",
        "badge": "🏛️ 英語の標準スタイル・英検準1級〜",
        "point": "英語圏で最も伝統ある新聞。ルールや法律、社会制度の議論を正確な言葉で伝えます。受動態や関係詞のきれいな構文が多く、高校の文法知識がどう使われているかを実感できます。",
        "tip": "関係代名詞や分詞構文が多用されるため、主語と述語を正確に捉える英文解釈力の強化に最適です。"
    },
    {
        "key": "the-guardian",
        "title_en": "The Guardian",
        "title_ja": "英・国際的リベラル日刊紙",
        "name": "The Guardian (英・国際的リベラル紙)",
        "badge": "🌍 医療倫理・環境問題・人権テーマ",
        "point": "AIと医療、気候変動など、教科書で習うSDGsや現代社会のテーマを深く掘り下げます。登場人物の生の声（インタビュー）が豊富で、会話表現の読解にも役立ちます。",
        "tip": "小論文や自由英作文で問われる『現代社会の論点・背景知識』を英語と日本語の両面から学べます。"
    },
    {
        "key": "nature",
        "title_en": "Nature & Science News",
        "title_ja": "英米・国際総合科学学術誌",
        "name": "Nature & Science News (国際科学誌)",
        "badge": "🔬 理科・生物・環境の入試頻出",
        "point": "「なぜ病気が増えているのか」「海で何が起きているのか」という謎解きの面白さを学べます。図表問題や共通テストの科学パッセージで求められる論理的思考力が身につきます。",
        "tip": "『仮説→実験手法→結果→考察』という理系論文の王道展開パターンを英語で掴むことができます。"
    },
    {
        "key": "jiji",
        "title_en": "Jiji Press",
        "title_ja": "時事通信（国内総合通信社）",
        "name": "Jiji Press (時事通信社)",
        "badge": "🇯🇵 日本の重要ニュース・国際経済・政策",
        "point": "日本の国策や半導体産業（ラピダス）、安全保障の最前線を客観的に伝える通信社です。日本語の重要ニュースを高校生レベルの標準英語に翻訳した記事を読むことで、日本の課題を世界に発信する表現力が身につきます。",
        "tip": "ニュースでよく聞くカタカナ語や政策用語（サプライチェーン、半導体など）が英語でどう表現されるかに注目しましょう。"
    },
    {
        "key": "yahoo",
        "title_en": "Yahoo! News Japan",
        "title_ja": "Yahoo!ニュース（教育・社会特集）",
        "name": "Yahoo! News Japan (Yahoo!ニュース)",
        "badge": "🎒 教育・健康・身近な生活課題",
        "point": "ランドセルの重さやタブレット端末の活用など、中高生自身の生活に密着したホットな話題を扱います。身近な問題だからこそ英語でも共感しやすく、英検の意見論述で自分の考えを述べる材料になります。",
        "tip": "『賛成の理由・反対の理由』を整理しながら読むと、自由英作文のライティング力が劇的にアップします。"
    },
    {
        "key": "getnews",
        "title_en": "GetNews Japan",
        "title_ja": "ガジェット通信（エンタメ・新技術）",
        "name": "GetNews Japan (ガジェット通信)",
        "badge": "🕶️ 最新ガジェット・AI・エンタメ",
        "point": "スマートグラスや最新AIツール、ポップカルチャーのワクワクする進化をいち早くレポートします。『テクノロジーの便利さ』と『使う側のマナー・ルール』の両面を楽しく学べます。",
        "tip": "新しいデジタル機器の説明に出てくる最新のIT英語やカタカナ言葉を、高校基本英語と結びつけて覚えられます。"
    }
]

def build_data_js():
    articles_list = []
    for art in JUNIOR_ARTICLES:
        slug = art["slug"]
        cat = art["category"]
        src_url = art.get("source_url", "").lower()
        media_key = MEDIA_KEY_MAP.get(slug)
        if not media_key:
            if "jiji" in src_url:
                media_key = "jiji"
            elif "yahoo" in src_url:
                media_key = "yahoo"
            elif "getnews" in src_url:
                media_key = "getnews"
            elif "nature" in src_url or "science" in src_url:
                media_key = "nature"
            elif "guardian" in src_url:
                media_key = "the-guardian"
            elif "ft.com" in src_url:
                media_key = "ft"
            elif "reuters" in src_url:
                media_key = "reuters"
            elif "time" in src_url:
                media_key = "time"
            else:
                media_key = "all"
        articles_list.append({
            "slug": slug,
            "category": cat,
            "category_label": art.get("category_label", cat.upper()),
            "date": art.get("date") or DATE_MAP.get(slug, "2026-10-10"),
            "title": art["title"],
            "headline_ja": art["headline_ja"],
            "subhead": art.get("subhead") or art.get("lead_ja", ""),
            "lead_snippet": art.get("lead_snippet") or art.get("lead_ja", "") or art.get("subhead", ""),
            "source_name": art["source_name"],
            "source_media_key": media_key,
            "image": art.get("image") or "https://images.unsplash.com/photo-1504711434969-e33886168f5c?w=1000&auto=format&fit=crop&q=80",
            "path": f"{cat}/{slug}/index.html",
            "senior_path": f"../{cat}/{slug}/index.html"
        })

    js_content = f"""// THE JUNIOR - Master Portal Data & High School Study Knowledge Base
// Contains all 15 Junior articles, daily editions, and Eiken study resources.

const JUNIOR_ARTICLES = {json.dumps(articles_list, ensure_ascii=False, indent=2)};

const JUNIOR_EDITIONS = {json.dumps(EDITIONS_DATA, ensure_ascii=False, indent=2)};

const JUNIOR_STUDY_RESOURCES = {json.dumps(JUNIOR_STUDY_RESOURCES, ensure_ascii=False, indent=2)};
"""

    out_file = os.path.join(JUNIOR_JS_DIR, "junior-data.js")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(js_content)
    print(f"[OK] Generated {out_file} ({len(articles_list)} articles, {len(EDITIONS_DATA)} editions)")

if __name__ == "__main__":
    build_data_js()
