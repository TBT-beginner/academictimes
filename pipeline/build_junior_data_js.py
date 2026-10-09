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
    "smart-glasses-ai-privacy": "2026-10-09",
    "japan-semiconductor-revival-rapidus": "2026-10-09",
    "digital-school-backpack-reform": "2026-10-09",
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
    "smart-glasses-ai-privacy": "getnews",
    "japan-semiconductor-revival-rapidus": "jiji",
    "digital-school-backpack-reform": "yahoo",
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
        "tagline": "特集：最新スマートグラスのプライバシー・北海道半導体再興戦略・教育現場のランドセル改革",
        "topLeadSlug": "smart-glasses-ai-privacy",
        "subLeadSlugs": ["japan-semiconductor-revival-rapidus", "digital-school-backpack-reform"],
        "leftDispatches": ["stoic-philosophy-digital-age", "headphones-in-public", "psychology-casual-encounters"],
        "rightDigestSlugs": ["critical-minerals-geopolitics", "colorectal-cancer-under-50s", "air-defence-shield", "generative-ai-paleontology"]
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
