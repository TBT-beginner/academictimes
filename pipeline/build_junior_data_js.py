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
    "2026-10-09": {
        "dateStr": "Friday October 9 2026",
        "editionLabel": "2026年10月9日 (金) 号 【本日最新版】",
        "tagline": "特集：スマホ時代の不安を和らげる哲学とイヤホンを外す小さな勇気",
        "topLeadSlug": "stoic-philosophy-digital-age",
        "subLeadSlugs": ["headphones-in-public", "psychology-casual-encounters"],
        "leftDispatches": ["critical-minerals-geopolitics", "colorectal-cancer-under-50s", "air-defence-shield"],
        "rightDigestSlugs": ["mediterranean-marine-heatwaves", "ai-pediatric-diagnosis-consent", "clarkson-business-red-tape", "generative-ai-paleontology"]
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
        "name": "TIME Magazine (米・オピニオン週刊誌)",
        "badge": "英検2級・準1級・共通テスト最頻出",
        "point": "日常の習慣（イヤホン、スマホ、睡眠）を題材にしながら、社会の大きな変化を分かりやすく問いかけるエッセイの宝庫です。段落ごとの主張の流れがとてもクリアで、自由英作文のお手本になります。"
    },
    {
        "key": "the-times",
        "name": "The Times (英・本格高級日刊紙)",
        "badge": "英語の標準スタイル・英検準1級〜",
        "point": "英語圏で最も伝統ある新聞。ルールや法律、社会制度の議論を正確な言葉で伝えます。受動態や関係詞のきれいな構文が多く、高校の文法知識がどう使われているかを実感できます。"
    },
    {
        "key": "the-guardian",
        "name": "The Guardian (英・国際的リベラル紙)",
        "badge": "医療倫理・環境問題・人権テーマ",
        "point": "AIと医療、気候変動など、教科書で習うSDGsや現代社会のテーマを深く掘り下げます。登場人物の生の声（インタビュー）が豊富で、会話表現の読解にも役立ちます。"
    },
    {
        "key": "nature",
        "name": "Nature & Science News (国際科学誌)",
        "badge": "理科・生物・環境の入試頻出",
        "point": "「なぜ病気が増えているのか」「海で何が起きているのか」という謎解きの面白さを学べます。図表問題や共通テストの科学パッセージで求められる論理的思考力が身につきます。"
    }
]

def build_data_js():
    articles_list = []
    for art in JUNIOR_ARTICLES:
        slug = art["slug"]
        cat = art["category"]
        articles_list.append({
            "slug": slug,
            "category": cat,
            "category_label": art.get("category_label", cat.upper()),
            "date": DATE_MAP.get(slug, "2026-10-06"),
            "title": art["title"],
            "headline_ja": art["headline_ja"],
            "subhead": art["subhead"],
            "lead_snippet": art["lead_snippet"],
            "source_name": art["source_name"],
            "source_media_key": MEDIA_KEY_MAP.get(slug, "all"),
            "image": art["image"],
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
