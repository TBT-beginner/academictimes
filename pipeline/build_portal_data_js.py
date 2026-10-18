# -*- coding: utf-8 -*-
"""
Generates news_portal/js/portal-data.js
Contains all 57 Senior Academic Times articles, dynamic daily edition configurations, and media literacy resources.
"""

import os
import sys
import json
import re

PORTAL_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
JS_DIR = os.path.join(PORTAL_DIR, "js")
os.makedirs(JS_DIR, exist_ok=True)

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from articles_data import ARTICLES

MEDIA_RESOURCES = [
  {
    "key": "time",
    "name": "TIME Magazine (米国・オピニオン週刊誌)",
    "country": "USA",
    "founded": "1923年",
    "stance": "教養・分析・中道リベラル",
    "examSignificance": "早慶・上智・東大など難関大入試長文で過去30年間最頻出。感情論を排し、認知心理学や統計データに基づいた論証型エッセイの最高峰。",
    "whyHighSchoolersMustKnow": "ニュースに興味がない高校生でも、TIME誌の『日常の当たり前を疑うエッセイ』を読むだけで、自由英作文や小論文で問われる論理構成（主張→具体例→反論の考慮）が自然と身につきます。",
    "sampleTopics": "デジタル社会の孤独、退屈と創造性、労働観の変容、宇宙探査の意義",
    "badge": "頻出度: Sランク（文理共通）"
  },
  {
    "key": "the-times",
    "name": "The Times (英国・本格高級日刊紙)",
    "country": "UK",
    "founded": "1785年",
    "stance": "伝統的保守・格調高い言論",
    "examSignificance": "世界標準フォント『Times New Roman』の発祥元。英国議会政治、法制度、司法判断の最高権威。東大・京大・一橋の要約・下線部和訳の定番出典。",
    "whyHighSchoolersMustKnow": "簡潔で引き締まった格調高い文体（The Times Style）は、文法的に厳密な複文（倒置・同格・分詞構文）の宝庫。正確な英文解釈力を鍛えるのに最適です。",
    "sampleTopics": "国家安全保障、司法審査、王室・憲法制度、大英帝国の歴史的検証",
    "badge": "頻出度: Sランク（難関国公立2次）"
  },
  {
    "key": "the-guardian",
    "name": "The Guardian (英国・国際的リベラル高級紙)",
    "country": "UK",
    "founded": "1821年",
    "stance": "中道リベラル・環境・調査報道",
    "examSignificance": "世界で最も読まれるオンライン高級紙の一つ。環境問題、人権、AI倫理、社会的不平等など『現代の重要課題』を最も深く追究するメディア。",
    "whyHighSchoolersMustKnow": "全記事が完全無料公開されているため、高校生の独習に最適。現代社会・倫理の教科書に載っているようなテーマの最前線を生きた英語で学べます。",
    "sampleTopics": "気候変動、AI診断と親の同意、貧困と教育格差、監視資本主義批判",
    "badge": "頻出度: Sランク（自由英作文・小論文直結）"
  },
  {
    "key": "nature",
    "name": "Nature & Nature Medicine (国際総合科学学術誌)",
    "country": "UK / Global",
    "founded": "1869年",
    "stance": "厳格な査読制・自然科学最高峰",
    "examSignificance": "医学部・東工大・京大理系などの超難関長文で毎年必ず出題。最新の疫学、がん研究、気候変動データを客観的に論じる専門英語。",
    "whyHighSchoolersMustKnow": "科学論文特有の論理展開（Background → Hypothesis → Method → Result → Discussion）を高校生のうちに掴むことで、共通テストの図表問題も一瞬で解けるようになります。",
    "sampleTopics": "若年性がん急増の疫学、マイクロプラスチック、腸内細菌叢、ゲノム編集",
    "badge": "頻出度: 特Aランク（医学部・難関理系）"
  },
  {
    "key": "science-mag",
    "name": "Science (全米科学振興協会・世界的学術誌)",
    "country": "USA",
    "founded": "1880年（トーマス・エジソンが創刊支援）",
    "stance": "先端科学総合・文理融合",
    "examSignificance": "Natureと双璧をなす世界最高峰の学術誌。計算生物学、生成AIを用いた進化の解明、量子力学など文理融合の学際的テーマに強い。",
    "whyHighSchoolersMustKnow": "AIを使って絶滅動物の歩き方を再現するなど、知的好奇心を刺激する最先端の研究を英語で知ることで、大学で何を学びたいかの探究学習に繋がります。",
    "sampleTopics": "AI古生物学、計算生物学、超電導、気候モデリング",
    "badge": "頻出度: 特Aランク（理系・情報系・総合型）"
  },
  {
    "key": "ft",
    "name": "Financial Times (英国・国際経済政治高級紙)",
    "country": "UK / Global",
    "founded": "1888年（サーモンピンクの紙面が象徴）",
    "stance": "自由市場・グローバル資本主義・政策精査",
    "examSignificance": "慶應経済・法、一橋大、東大文系で圧倒的信頼を誇る出典。防衛予算の使途、国際サプライチェーン、金融政策を冷静に数字で検証。",
    "whyHighSchoolersMustKnow": "感情論になりがちな政治・社会問題を『財政・コスト・費用対効果』の視点で冷徹に捉える思考法が養われ、慶應小論文の合格レベルに直結します。",
    "sampleTopics": "防衛調達の透明性、重要鉱物の囲い込み、エネルギー転換のコスト、中央銀行デジタル通貨",
    "badge": "頻出度: Sランク（難関社会科学系）"
  },
  {
    "key": "reuters",
    "name": "Reuters (世界最大級の国際総合通信社)",
    "country": "UK / Global",
    "founded": "1851年",
    "stance": "完全中立・客観報道・速報性",
    "examSignificance": "記者の主観や形容詞を極力排除し、事実（Fact）のみを正確に伝える最高峰の通信社英語。共通テストや国公立2次の事実把握問題の基礎。",
    "whyHighSchoolersMustKnow": "世界中のニュースの『大元の一次情報』がどう書かれているかを知ることで、ネット上のフェイクニュースや偏向報道に惑わされないメディアリテラシーが身につきます。",
    "sampleTopics": "米軍爆撃機再配置、地中海深海熱波、国連気候サミット、サプライチェーン速報",
    "badge": "客観性: 世界基準（ファクトチェック必須）"
  },
  {
    "key": "jiji",
    "name": "Jiji Press (時事通信社・国内総合通信社)",
    "country": "Japan",
    "founded": "1945年",
    "stance": "国政・行政・金融・経済安全保障のファクト重視",
    "examSignificance": "日本政府・経産省の政策決定、ラピダス半導体プロジェクト、最高裁判所判例など、日本の最重要国策を正確な一次情報として発信。",
    "whyHighSchoolersMustKnow": "国内で起きている重要国策や法改正を世界水準の英語でどう発信・表現するかを学ぶことで、日本の課題をグローバルな視点から客観的に論じる力が身につきます。",
    "sampleTopics": "ラピダス2nm半導体支援、楽譜ネット無断複製最高裁判決、プラ条約、日米地位協定",
    "badge": "信頼性: 国内一次報道の最高峰"
  },
  {
    "key": "yahoo",
    "name": "Yahoo! News Japan (国内最大級ニュースポータル・特集報道)",
    "country": "Japan",
    "founded": "1996年",
    "stance": "生活者目線・教育・社会課題・徹底深層取材",
    "examSignificance": "ランドセルの過重負担問題、地方路線バスの完全キャッシュレス化と高齢者移動権など、市民生活の最前線で起きているリアルな構造矛盾を掘り下げる特集記事群。",
    "whyHighSchoolersMustKnow": "自分たちの学校生活や身近な地域の困りごとが、そのまま大学入試の社会問題（公共・現代社会）の論述テーマになります。日常の違和感を英語で言語化する最高の素材です。",
    "sampleTopics": "小学生ランドセル10kg問題とデジタル教科書、地方路線バスの維持とキャッシュレス化、郊外サテライト移住",
    "badge": "身近度: Aランク（現代社会・身近な課題）"
  },
  {
    "key": "getnews",
    "name": "GetNews Japan (ガジェット通信・先端カルチャー)",
    "country": "Japan",
    "founded": "2008年",
    "stance": "デジタルカルチャー・先端ガジェット・ゲーム・ネット世論",
    "examSignificance": "AIスマートグラスによる常時録画と公衆プライバシー、高校eスポーツ部活の教育的妥当性など、デジタルネイティブ世代が直面する先端テクノロジーと倫理のフロンティアを速報。",
    "whyHighSchoolersMustKnow": "最新のスマートデバイスやゲーム、SNSカルチャーをただ消費するだけでなく、『テクノロジーの進化が社会のルールや人間の尊厳をどう変えるか』を批判的に考える視点が得られます。",
    "sampleTopics": "AIスマートグラスのプライバシー、高校eスポーツ部活動の教育的価値、生成AI音楽と著作権",
    "badge": "先端性: Sランク（情報社会・テクノロジー倫理）"
  }
]

def detect_media_key(art):
    src_url = art.get("source_url", "").lower()
    slug = art.get("slug", "")
    if "jiji" in src_url:
        return "jiji"
    elif "yahoo" in src_url:
        return "yahoo"
    elif "getnews" in src_url:
        return "getnews"
    elif "nature" in src_url or "science" in src_url:
        return "nature"
    elif "guardian" in src_url:
        return "the-guardian"
    elif "ft.com" in src_url:
        return "ft"
    elif "reuters" in src_url:
        return "reuters"
    elif "time" in src_url:
        return "time"
    elif "thetimes" in src_url or "telegraph" in src_url:
        return "the-times"
    return "all"

def build_portal_data():
    articles_list = []
    
    # Stock photo images by category for visual richness
    cat_images = {
        "science": "https://images.unsplash.com/photo-1507668077129-56e32842fceb?w=1000&auto=format&fit=crop&q=80",
        "society": "https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=1000&auto=format&fit=crop&q=80",
        "world": "https://images.unsplash.com/photo-1526304640581-d334cdbbf45e?w=1000&auto=format&fit=crop&q=80",
        "law": "https://images.unsplash.com/photo-1589829545856-d10d557cf95f?w=1000&auto=format&fit=crop&q=80",
        "culture": "https://images.unsplash.com/photo-1457369804613-52c61a468e7d?w=1000&auto=format&fit=crop&q=80",
        "entertainment": "https://images.unsplash.com/photo-1511512578047-dfb367046420?w=1000&auto=format&fit=crop&q=80"
    }
    
    for art in ARTICLES:
        slug = art["slug"]
        cat = art["category"]
        date_str = art.get("date", "2026-10-10")
        media_key = detect_media_key(art)
        img = art.get("image") or cat_images.get(cat, "https://images.unsplash.com/photo-1504711434969-e33886168f5c?w=1000&auto=format&fit=crop&q=80")
        
        # Lead snippet
        lead_snippet = art.get("lead_snippet", "")
        if not lead_snippet:
            lead_snippet = art.get("subhead", "")
            
        articles_list.append({
            "slug": slug,
            "category": cat,
            "category_label": art.get("category_label", cat.upper()),
            "date": date_str,
            "title": art["title"],
            "headline_ja": art["headline_ja"],
            "subhead": art["subhead"],
            "lead_snippet": lead_snippet,
            "source_name": art["source_name"],
            "source_media_key": media_key,
            "source_url": art["source_url"],
            "path": f"{cat}/{slug}/index.html",
            "image": img
        })

    # Group by date
    oct10_slugs = [a["slug"] for a in ARTICLES if a.get("date") == "2026-10-10"]
    editions_dict = {
        "2026-10-19": {
            "dateStr": "Monday October 19 2026",
            "editionLabel": "2026年10月19日 (月) 号 【本日付・最新・全12記事】",
            "tagline": "特集：ガボン聖なる植物イボガと先住権・住宅断熱とヒートポンプ光熱費削減・刑務所過密と更生危機・欧州主要都市住宅デモ",
            "topLeadSlug": "gabon-iboga-sacred-plant-addiction-treatment-biopiracy",
            "subLeadSlugs": [
                "heat-pumps-building-insulation-energy-transition-study",
                "penal-reform-prison-overcrowding-rehabilitation-barriers",
                "european-housing-crisis-short-term-rentals-unrest"
            ],
            "leftDispatches": [
                "public-transit-acoustic-etiquette-civic-campaign",
                "world-bank-ai-governance-developing-economies",
                "industrial-energy-tariffs-green-steelmaking-subsidies",
                "iot-botnet-cyber-threats-financial-clearing-houses"
            ],
            "rightDigestSlugs": [
                "climate-communication-fatalism-constructive-agency",
                "sarah-forbes-bonetta-biography-victorian-empire",
                "afrobeats-performance-culture-lagos-hype-phenomenon",
                "australian-literature-tim-winton-national-canon"
            ]
        },
        "2026-10-18": {
            "dateStr": "Sunday October 18 2026",
            "editionLabel": "2026年10月18日 (日) 号 【全12記事・アーカイブ】",
            "tagline": "特集：JAXA火星衛星フォボス探査MMX・腸内難病血液バイオマーカー早期予測・職場猛暑保護・サルデーニャ長寿の秘密",
            "topLeadSlug": "japan-jaxa-mmx-phobos-sample-return-mission",
            "subLeadSlugs": [
                "inflammatory-bowel-disease-blood-biomarkers-early-prediction",
                "occupational-heat-stress-statutory-workplace-protections",
                "sardinian-blue-zone-female-centenarians-longevity"
            ],
            "leftDispatches": [
                "youth-unemployment-neet-welfare-reform-review",
                "epa-pfas-forever-chemicals-regulatory-backtrack",
                "non-consensual-deepfakes-criminalization-european-parliament",
                "uk-eu-cross-border-law-enforcement-pact"
            ],
            "rightDigestSlugs": [
                "shakespeare-authorship-edward-iii-computational-stylistics",
                "medieval-romance-origins-modern-fantasy-literature",
                "wikipedia-human-curation-ai-content-pollution",
                "autonomous-ai-worms-cybersecurity-vulnerabilities"
            ]
        },
        "2026-10-17": {
            "dateStr": "Saturday October 17 2026",
            "editionLabel": "2026年10月17日 (土) 号 【全12記事・アーカイブ】",
            "tagline": "特集：ニシツノメドリ海洋温暖化適応・養蜂ミツバチと野生ハナバチ競合・若者雇用見習い税改革・メキシコ巨大ハリケーン",
            "topLeadSlug": "puffin-seabird-climate-resilience-hope",
            "subLeadSlugs": [
                "honeybees-competition-wild-pollinators-biodiversity",
                "workforce-retraining-youth-apprenticeships-levy",
                "hurricane-trudy-pacific-coastal-resilience"
            ],
            "leftDispatches": [
                "nhs-medical-records-privacy-breach-dismissals",
                "us-corporate-lobbying-eu-deforestation-regulation",
                "nhs-hospital-trusts-reject-palantir-data-platform",
                "oecd-warns-populist-economic-policies-cost-of-living"
            ],
            "rightDigestSlugs": [
                "isabel-allende-premio-planeta-pseudonym",
                "as-byatt-literary-archive-british-library",
                "bespoke-coachbuilding-luxury-automotive-craftsmanship",
                "uk-ai-safety-institute-counter-extremism-testing"
            ]
        },
        "2026-10-16": {
            "dateStr": "Friday October 16 2026",
            "editionLabel": "2026年10月16日 (金) 号 【全12記事・アーカイブ】",
            "tagline": "特集：世界計量会議「うるう秒」廃止とうるう時導入・シャニダール洞窟旧人類投槍・イングランド6地域深刻干ばつ宣言",
            "topLeadSlug": "leap-second-abolition-leap-hour",
            "subLeadSlugs": [
                "neanderthal-shanidar-spear-trauma",
                "england-six-regions-severe-drought-water-crisis",
                "indonesia-wildfire-haze-dry-ice-cloud-seeding"
            ],
            "leftDispatches": [
                "made-in-europe-green-subsidies-uk-accord",
                "brazil-statutory-workweek-reduction-forty-hours",
                "zero-click-spyware-digital-advertising-exploitation",
                "sand-tiger-shark-conservation-public-aquariums"
            ],
            "rightDigestSlugs": [
                "uk-chancellor-bank-windfall-tax-fiscal-consolidation",
                "the-floating-world-art-market-capitalism-ethics",
                "national-digital-sovereignty-cloud-infrastructure",
                "satellite-constellation-dual-use-defence-dispute"
            ]
        },
        "2026-10-15": {
            "dateStr": "Thursday October 15 2026",
            "editionLabel": "2026年10月15日 (木) 号 【全12記事・アーカイブ】",
            "tagline": "特集：【過去の基礎論文解説】AlphaFold 3生体分子予測・【過去のニュース深掘り】英学校スマホ禁止＆欧州再エネ逆転・音声重視の言語習得法",
            "topLeadSlug": "alphafold-3-biomolecular-structure-prediction",
            "subLeadSlugs": [
                "phonetic-focus-foreign-language-acquisition",
                "england-school-chain-phone-free-policy",
                "renewables-overtake-fossil-fuels-eu-electricity"
            ],
            "leftDispatches": [
                "four-day-workweek-uk-trial-permanent",
                "eu-ai-act-consumer-rights-enforcement",
                "mont-blanc-glacier-melt-elevation-loss",
                "smart-glasses-parliament-privacy-controversy"
            ],
            "rightDigestSlugs": [
                "us-newspapers-openai-copyright-lawsuit",
                "orbital-samantha-harvey-booker-prize",
                "gen-z-physical-books-library-renaissance",
                "england-organic-farming-expansion-target"
            ]
        },
        "2026-10-14": {
            "dateStr": "Wednesday October 14 2026",
            "editionLabel": "2026年10月14日 (水) 号 【全30記事・アーカイブ】",
            "tagline": "特集：全固体ナトリウムイオン電池革新・WTO電子商取引恒久化・デジタル遺産パスワード開示最高裁・地方交通地域通貨連携",
            "topLeadSlug": "solid-state-sodium-ion-battery-breakthrough",
            "subLeadSlugs": [
                "wto-electronic-commerce-moratorium-negotiations",
                "supreme-court-probate-digital-asset-passwords",
                "local-train-revitalization-community-tourism-passes"
            ],
            "leftDispatches": [
                "crispr-epigenetic-silencing-chronic-pain",
                "school-attendance-counseling-vr-classrooms",
                "iaea-small-modular-reactor-safety-standards",
                "digital-nostalgia-analog-media-generation-z"
            ],
            "rightDigestSlugs": [
                "exoplanet-atmospheric-carbon-biosignature-jwst",
                "ocean-acidification-deepwater-coral-calcification",
                "neuromorphic-spiking-chips-edge-ai-robotics",
                "elderly-volunteer-childcare-intergenerational-community",
                "un-global-water-security-transboundary-aquifers",
                "personal-information-protection-generative-model-training",
                "flexible-graphene-audio-transducers-smart-jackets"
            ]
        },
        "2026-10-13": {
            "dateStr": "Tuesday October 13 2026",
            "editionLabel": "2026年10月13日 (火) 号 【全30記事・アーカイブ】",
            "tagline": "特集：CO2固定化人工合成細菌・国連生物多様性枠組・テレワーク労働者性最高裁審理・超高齢社会歩行者空間設計",
            "topLeadSlug": "synthetic-biology-co2-eating-bacteria-enzymes",
            "subLeadSlugs": [
                "un-cop16-biodiversity-fund-cali-framework",
                "supreme-court-worker-classification-remote-telecommuters",
                "elderly-pedestrian-traffic-safety-urban-redesign"
            ],
            "leftDispatches": [
                "alzheimers-blood-biomarker-early-detection",
                "youth-mental-health-smartphone-ban-boarding-schools",
                "eu-ai-act-high-risk-algorithm-enforcement",
                "philosophical-ethics-deepfake-historical-figures"
            ],
            "rightDigestSlugs": [
                "perovskite-silicon-tandem-solar-efficiency-record",
                "antarctic-ice-shelf-subglacial-meltwater-dynamics",
                "quantum-dot-infrared-imaging-cancer-margins",
                "regional-revitalization-telework-subsidies-families",
                "indo-pacific-subsea-telecom-cable-redundancy",
                "consumer-protection-digital-will-asset-inheritance",
                "neural-interface-earbuds-brainwave-music-curation"
            ]
        },
        "2026-10-11": {
            "dateStr": "Sunday October 11 2026",
            "editionLabel": "2026年10月11日 (日) 号 【全30記事・アーカイブ】",
            "tagline": "特集：JWST初期宇宙ブラックホール解明・国連気候安全保障決議・G20最低法人税率・SNS迅速開示最高裁判決",
            "topLeadSlug": "james-webb-early-universe-supermassive-black-holes",
            "subLeadSlugs": [
                "unsc-climate-security-conflict-refugee-nexus",
                "g20-pillar-two-global-minimum-corporate-tax",
                "supreme-court-sns-slander-speedy-disclosure-ruling"
            ],
            "leftDispatches": [
                "autonomous-bus-pilot-aging-rural-towns",
                "personalized-mrna-cancer-vaccine-phase3",
                "rural-kabuki-digital-archive-vr-preservation",
                "micro-fluidic-haptic-controllers-handheld-gaming"
            ],
            "rightDigestSlugs": [
                "fusion-high-temperature-superconducting-magnets",
                "deep-sea-microplastics-thermohaline-plankton-flux",
                "inquiry-based-learning-university-admissions",
                "arctic-council-sea-ice-shipping-environmental-accord",
                "ai-voice-likeness-right-of-publicity-precedent",
                "attention-economy-philosophical-critique-ethics",
                "museum-spatial-ar-smartglasses-exhibits"
            ]
        },
        "2026-10-10": {
            "dateStr": "Saturday October 10 2026",
            "editionLabel": "2026年10月10日 (土) 号 【全30記事・フルアーカイブ】",
            "tagline": "特集：ノーベル化学賞硤合教授・坂口特任教授免疫革新・AIデータセンター・食料品消費税減税",
            "topLeadSlug": "soai-reaction-nobel-chemistry",
            "subLeadSlugs": [
                "regulatory-t-cells-nobel-breakthrough",
                "food-sales-tax-cut-income-benefits",
                "ukraine-drone-strike-yandex-ai-datacenter"
            ],
            "leftDispatches": [
                "supreme-court-sheet-music-piracy-ruling",
                "japan-icc-sanctions-rule-of-law",
                "pnas-ai-biodiversity-monitoring",
                "kyocera-ceramic-coating-vacuum-tumblers"
            ],
            "rightDigestSlugs": [
                "wwf-living-planet-biodiversity-collapse",
                "commercial-fusion-reactor-engineering",
                "dementia-smart-home-minder-system",
                "white-house-press-secretary-zacharias",
                "cop31-antalya-climate-finance-negotiations",
                "okinawa-assembly-sofa-revision-resolution",
                "tateyama-shugendo-faith-cinema"
            ]
        },
        "2026-10-09": {
            "dateStr": "Friday October 9 2026",
            "editionLabel": "2026年10月9日 (金) 号 【全30記事・フルアーカイブ】",
            "tagline": "特集：ノーベル物理学賞AI基盤・ラピダス半導体・全固体電池・同性婚最高裁審理",
            "topLeadSlug": "nobel-physics-hopfield-hinton-machine-learning",
            "subLeadSlugs": [
                "japan-semiconductor-revival-rapidus",
                "solid-state-battery-ev-commercial-trial",
                "supreme-court-same-sex-marriage-constitution"
            ],
            "leftDispatches": [
                "asean-summit-vientiane-south-china-sea-code",
                "traditional-sake-unesco-intangible-cultural-heritage",
                "cloud-gaming-latency-low-earth-orbit-satellite",
                "dual-earner-childcare-leave-wage-replacement"
            ],
            "rightDigestSlugs": [
                "generative-ai-fair-use-copyright-lawsuit",
                "eu-carbon-border-adjustment-mechanism-cbam",
                "algorithmic-pricing-antitrust-collusion",
                "solitude-vs-loneliness-philosophy-existentialism",
                "virtual-production-led-volume-filmmaking",
                "digital-detox-camps-youth-neuroplasticity",
                "archaeological-lidar-maya-civilization-discovery"
            ]
        },
        "2026-10-08": {
            "dateStr": "Thursday October 8 2026",
            "editionLabel": "2026年10月8日 (木) 号 【全30記事・アーカイブ】",
            "tagline": "特集：重要鉱物地政学と脱炭素サプライチェーン・デジタル時代のストア派哲学",
            "topLeadSlug": "critical-minerals-geopolitics",
            "subLeadSlugs": ["stoic-philosophy-digital-age", "mediterranean-marine-heatwaves"],
            "leftDispatches": ["psychology-casual-encounters", "air-defence-shield", "colorectal-cancer-under-50s"],
            "rightDigestSlugs": ["headphones-in-public", "clarkson-business-red-tape", "inheritance-tax-reform-debate", "ai-pediatric-diagnosis-consent"]
        },
        "2026-10-07": {
            "dateStr": "Wednesday October 7 2026",
            "editionLabel": "2026年10月7日 (水) 号 【全30記事・アーカイブ】",
            "tagline": "特集：偶発的日常交流の心理学と社会的幸福・北極海航路と国連海洋法条約",
            "topLeadSlug": "psychology-casual-encounters",
            "subLeadSlugs": ["arctic-sea-route-unclos", "generative-ai-paleontology"],
            "leftDispatches": ["critical-minerals-geopolitics", "royal-security-judicial-review", "raf-fairford-bomber-redeployment"],
            "rightDigestSlugs": ["headphones-in-public", "stoic-philosophy-digital-age", "colorectal-cancer-under-50s", "air-defence-shield"]
        },
        "2026-10-06": {
            "dateStr": "Tuesday October 6 2026",
            "editionLabel": "2026年10月6日 (火) 号 【バックナンバー】",
            "tagline": "特集：公共空間のイヤホン論争と都市の孤独・偶発的出会いの心理学",
            "topLeadSlug": "headphones-in-public",
            "subLeadSlugs": ["jeffrey-archer-obituary", "royal-security-judicial-review"],
            "leftDispatches": ["air-defence-shield", "colorectal-cancer-under-50s", "raf-fairford-bomber-redeployment"],
            "rightDigestSlugs": ["clarkson-business-red-tape", "inheritance-tax-reform-debate", "ai-pediatric-diagnosis-consent", "mediterranean-marine-heatwaves"]
        },
        "2026-10-05": {
            "dateStr": "Monday October 5 2026",
            "editionLabel": "2026年10月5日 (月) 号 【バックナンバー】",
            "tagline": "特集：英国100億ポンド防衛シールド審議と司法審査・王室警護裁量",
            "topLeadSlug": "air-defence-shield",
            "subLeadSlugs": ["royal-security-judicial-review", "clarkson-business-red-tape"],
            "leftDispatches": ["headphones-in-public", "inheritance-tax-reform-debate", "mediterranean-marine-heatwaves"],
            "rightDigestSlugs": ["jeffrey-archer-obituary", "ai-pediatric-diagnosis-consent", "colorectal-cancer-under-50s", "raf-fairford-bomber-redeployment"]
        },
        "2026-10-04": {
            "dateStr": "Sunday October 4 2026",
            "editionLabel": "2026年10月4日 (日) 号 【バックナンバー】",
            "tagline": "特集：50歳未満の大腸がん世界的急増と地中海深海熱波の生体ストレス",
            "topLeadSlug": "colorectal-cancer-under-50s",
            "subLeadSlugs": ["mediterranean-marine-heatwaves", "generative-ai-paleontology"],
            "leftDispatches": ["ai-pediatric-diagnosis-consent", "psychology-casual-encounters", "inheritance-tax-reform-debate"],
            "rightDigestSlugs": ["headphones-in-public", "air-defence-shield", "clarkson-business-red-tape", "jeffrey-archer-obituary"]
        },
        "2026-10-03": {
            "dateStr": "Saturday October 3 2026",
            "editionLabel": "2026年10月3日 (土) 号 【バックナンバー】",
            "tagline": "特集：小児AI診断の親同意権と古生物学における生成ニューラルネットワーク",
            "topLeadSlug": "ai-pediatric-diagnosis-consent",
            "subLeadSlugs": ["generative-ai-paleontology", "royal-security-judicial-review"],
            "leftDispatches": ["clarkson-business-red-tape", "colorectal-cancer-under-50s", "jeffrey-archer-obituary"],
            "rightDigestSlugs": ["headphones-in-public", "mediterranean-marine-heatwaves", "psychology-casual-encounters", "inheritance-tax-reform-debate"]
        },
        "2026-10-02": {
            "dateStr": "Friday October 2 2026",
            "editionLabel": "2026年10月2日 (金) 号 【バックナンバー】",
            "tagline": "特集：相続税改革と世代間格差の政治哲学・クラークソン英起業規制論",
            "topLeadSlug": "inheritance-tax-reform-debate",
            "subLeadSlugs": ["clarkson-business-red-tape", "psychology-casual-encounters"],
            "leftDispatches": ["raf-fairford-bomber-redeployment", "royal-security-judicial-review", "generative-ai-paleontology"],
            "rightDigestSlugs": ["air-defence-shield", "colorectal-cancer-under-50s", "headphones-in-public", "ai-pediatric-diagnosis-consent"]
        },
        "2026-10-01": {
            "dateStr": "Thursday October 1 2026",
            "editionLabel": "2026年10月1日 (木) 号 【創刊バックナンバー】",
            "tagline": "特集：フェアフォード米戦略爆撃機再配置とジェフリー・アーチャー氏追悼",
            "topLeadSlug": "raf-fairford-bomber-redeployment",
            "subLeadSlugs": ["jeffrey-archer-obituary", "generative-ai-paleontology"],
            "leftDispatches": ["air-defence-shield", "inheritance-tax-reform-debate", "mediterranean-marine-heatwaves"],
            "rightDigestSlugs": ["clarkson-business-red-tape", "psychology-casual-encounters", "royal-security-judicial-review", "headphones-in-public"]
        }
    }

    js_content = f"""// THE ACADEMIC TIMES - Master Portal Data & Media Literacy Knowledge Base
// Contains all {len(articles_list)} articles, daily editions, and high-school media literacy references.

const MEDIA_RESOURCES = {json.dumps(MEDIA_RESOURCES, ensure_ascii=False, indent=2)};

const ARTICLES = {json.dumps(articles_list, ensure_ascii=False, indent=2)};

const ALL_ARTICLES = ARTICLES;

const EDITIONS = {json.dumps(editions_dict, ensure_ascii=False, indent=2)};
"""

    out_file = os.path.join(JS_DIR, "portal-data.js")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(js_content)
    print(f"[OK] Generated {out_file} with {len(articles_list)} articles across {len(editions_dict)} editions.")

if __name__ == "__main__":
    build_portal_data()
