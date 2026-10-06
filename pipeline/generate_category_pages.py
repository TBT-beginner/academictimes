# -*- coding: utf-8 -*-
"""
Generates rich, high-aesthetic Category Portal pages for all 5 academic genres:
- Society & Mind (/society/index.html)
- Science & Tech (/science/index.html)
- Culture & Thought (/culture/index.html)
- Law & Justice (/law/index.html)
- World & Security (/world/index.html)
"""

import os
import sys

CATEGORY_METADATA = {
    "world": {
        "title_en": "WORLD & SECURITY",
        "title_ja": "国際情勢・外交・安全保障",
        "subtitle": "Global Governance, Geopolitics, Maritime Law & Alliances",
        "description": "東大・京大・早慶・一橋などの最難関大学入試長文で最頻出の国際関係論。国家主権、条約解釈、抑止力、資源安全保障、海洋法をめぐる客観的事実報道と論述英語を学びます。",
        "exam_strategy": "国際情勢の英文を読む鍵は『党派的主観（プロパガンダ）と客観的事実の区別』です。条約条文の適用（UNCLOS、地位協定など）や、因果関係・対比レトリック（not A but rather B、irrespective of等）を正確に押さえることで、内容一致問題や要約問題で圧倒的な得点源になります。",
        "key_phrases": [
            ("customary international law", "国際慣習法（条約化されていなくても国家間で法と信じられている慣習）"),
            ("deterrence doctrine", "抑止力ドクトリン（先制攻撃の利益を否定し平和を保つ防衛戦略）"),
            ("asymmetric warfare", "非対称戦争（通常兵力差をドローンやサイバー等で埋める現代戦）"),
            ("littoral jurisdiction", "沿岸国の管轄権（領海および排他的経済水域における法的権限）"),
            ("preferential trade subsidy", "特恵貿易補助金（特定同盟国の戦略産業を優遇する通商政策）")
        ]
    },
    "culture": {
        "title_en": "CULTURE & THOUGHT",
        "title_ja": "文化・思想・現代哲学",
        "subtitle": "Cognitive Psychology, Classical Philosophy, Literary Criticism & Solitude",
        "description": "TIME誌や文芸評論紙に代表される格調高いオピニオン・エッセイ。デジタル常時接続時代の孤独、古代ストア派哲学の復権、大衆文学の叙事詩的手法など、人間存在の本質を問う深層論説。",
        "exam_strategy": "文化・思想系の英文では、抽象度の高い概念（reverie, equanimity, dichotomy等）が具体的な日常体験を通じて言い換え（パラフレーズ）されます。比喩表現や対比構文の真意を見抜き、筆者の価値観の転換点を捉える読解力を養います。",
        "key_phrases": [
            ("dichotomy of control", "制御の二分法（自分の意志で変えられる内的思考と、変えられない外界の峻別）"),
            ("power of reverie", "物思い（白昼夢）の力（目的のないぼんやりした時間こそが創造性を育む）"),
            ("cognitive equanimity", "精神の平静・沈着（外的変動に動揺せず理性的自律を保つ徳目）"),
            ("formulaic prose", "型通りの文章・定型句（独創性を欠くありふれたプロットに対する批評）"),
            ("external validation loop", "外部承認欲求のループ（SNSの通知や他者評価に依存する心理的罠）")
        ]
    },
    "society": {
        "title_en": "SOCIETY & MIND",
        "title_ja": "社会・行動科学・経済倫理",
        "subtitle": "Urban Sociology, Wealth Distribution, Behavioral Economics & Bureaucracy",
        "description": "都市の孤立を防ぐ微小な対話の心理学、世代間公平と相続税改革、地方起業を蝕む官僚主義規制など、市民生活とマクロ経済・社会政策が交差する重要テーマを凝縮。",
        "exam_strategy": "社会科学系長文では、統計データや心理実験（Epley教授の通勤実験、ピケティの格差論など）の『仮説・実験手法・結果・社会的示唆』の流れを論理的に追うことが不可欠です。因果関係構文（attribute A to B、epitomize等）を確実にマスターしましょう。",
        "key_phrases": [
            ("pluralistic ignorance", "多元的無知（全員がつながりを望んでいるのに、皆が無関心だと誤認する逆説）"),
            ("intergenerational equity", "世代間公平（現役世代と将来世代、親世代との間の富と負担の公正な配分）"),
            ("regulatory sclerosis", "規制の硬直化（柔軟性を失った官僚的ルールが経済の活力を殺す現象）"),
            ("strength of weak ties", "弱い紐帯の強み（グラノヴェッター理論：束の間の知人関係がもたらす情報と回復力）"),
            ("fiscal drag", "財政ドラッグ（インフレで名目所得が増えただけで実質増税枠に引き込まれる現象）")
        ]
    },
    "law": {
        "title_en": "LAW & JUSTICE",
        "title_ja": "法律・憲法・生命倫理",
        "subtitle": "Judicial Review, AI Accountability, Royal Prerogatives & Statutory Oversight",
        "description": "英高等法院におけるAI小児医療診断の親同意権、国家安全保障予算の議会監視、王室警護費の行政裁量と司法審査など、法治国家の根幹を揺るがす現代の最前線判例・法哲学的対立。",
        "exam_strategy": "法学・制度論述では、二つの対立する正当な利益（例：子どもの最善の利益 vs 親の意思決定権、安全保障の機密性 vs 財政の公的説明責任）をどのように比較衡量（balancing）するかが焦点となります。倒置構文（At issue is...）や後置修飾を正確に解釈する力が問われます。",
        "key_phrases": [
            ("judicial review", "司法審査（行政機関の裁量行使が合理的・適法であるかを裁判所が審査する手続）"),
            ("paramount best interests", "最優先される最善の利益（英米児童法における絶対原則）"),
            ("statutory scrutiny", "法定の議会精査（法律に基づいて行われる厳格な公的予算・政策の監視）"),
            ("epistemic authority", "認識論的権威（AIの出力が専門医と同等の医学的正当性を持ちうるかという倫理概念）"),
            ("administrative discretion", "行政裁量（法令の枠組み内で行政庁が自らの判断で選択できる裁量の範囲）")
        ]
    },
    "science": {
        "title_en": "SCIENCE & TECH",
        "title_ja": "科学・医学・先端技術",
        "subtitle": "Global Oncology, Deep Marine Ecology, Generative Deep Learning & Biomechanics",
        "description": "NatureやScience誌の先端学術論文から、50歳未満の大腸がん急増とマイクロプラスチックの因果関係、地中海深海熱波の生体ストレス、生成ニューラルネットワークによる古生物生体力学復元などを精読。",
        "exam_strategy": "医学・自然科学長文は、難解な専門用語に見えても『従来の通説（senescence, thermal refuges）』と『最新の実験データ（oncological surge, suppressed convection）』が明確に対比されます。対比のWhileや分詞構文による因果の連鎖を正確に辿ることが得点直結の急所です。",
        "key_phrases": [
            ("microbiome equilibrium", "腸内細菌叢の平衡（宿主の免疫機能や代謝を支える細菌バランス）"),
            ("bathypelagic strata", "漸深層（太陽光の届かない水深数百〜数千メートルの深海環境）"),
            ("locomotion biomechanics", "運動生体力学（筋肉の配置や骨格強度から生物の歩行・疾走能力を計算する物理学）"),
            ("subclinical inflammation", "潜在性（慢性）炎症（自覚症状がないまま細胞を侵食する微小な炎症反応）"),
            ("predictive extrapolation", "予測的外挿（既知の骨格データから未知の生体機能をAIで導き出す計算科学）")
        ]
    }
}

def generate_category_pages():
    import articles_data
    all_arts = articles_data.ARTICLES
    
    # Also add prototype headphones-in-public if not in articles_data
    slugs = [a["slug"] for a in all_arts]
    if "headphones-in-public" not in slugs:
        all_arts.insert(0, {
            "slug": "headphones-in-public",
            "category": "culture",
            "category_label": "COGNITIVE PSYCHOLOGY & CULTURE",
            "title": "The Case Against Wearing Headphones in Public: Reclaiming the Power of Reverie",
            "headline_ja": "公共空間でイヤホンを外す効用：失われた「物思い（白昼夢）」を取り戻す",
            "subhead": "米週刊誌TIME掲載のエッセイ。常時接続と孤独、創造性を育む退屈の価値を認知心理学で徹底解説。",
            "source_name": "TIME Magazine (Oct 6, 2026 / Meehika Barua)",
            "sentences": [{"en": "The modern human mind is constantly bombarded with noise.", "ja": ""}],
            "quiz": [1, 2, 3]
        })
        
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    
    for cat_key, meta in CATEGORY_METADATA.items():
        cat_dir = os.path.join(base_dir, cat_key)
        os.makedirs(cat_dir, exist_ok=True)
        
        # Filter articles belonging to this category
        cat_articles = [a for a in all_arts if a["category"] == cat_key]
        lead_art = cat_articles[0] if cat_articles else None
        other_arts = cat_articles[1:] if len(cat_articles) > 1 else []
        
        # Navigation active states
        soc_act = "active" if cat_key == "society" else ""
        sci_act = "active" if cat_key == "science" else ""
        cul_act = "active" if cat_key == "culture" else ""
        law_act = "active" if cat_key == "law" else ""
        wor_act = "active" if cat_key == "world" else ""
        
        # Lead article HTML
        lead_html = ""
        if lead_art:
            lead_html = f"""
            <article class="cat-lead-card" style="border: 1px solid var(--times-black); padding: 1.5rem; background: #fff; margin-bottom: 2rem;">
              <div style="display: flex; flex-direction: column; gap: 0.75rem;">
                <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 0.5rem;">
                  <span class="badge-new">FEATURED LEAD STORY • {lead_art.get('category_label', meta['title_en'])}</span>
                  <span style="font-size: 0.8rem; color: var(--times-muted);">一次出典: {lead_art.get('source_name', '')}</span>
                </div>
                <h2 style="font-family: var(--font-headline); font-size: 1.85rem; line-height: 1.25; margin: 0.25rem 0;">
                  <a href="{lead_art['slug']}/index.html" style="color: var(--times-black); text-decoration: none;">{lead_art['title']}</a>
                </h2>
                <p style="font-size: 1.05rem; font-weight: 700; color: var(--times-black); margin-bottom: 0.25rem;">
                  {lead_art.get('headline_ja', '')}
                </p>
                <p style="font-size: 0.92rem; color: var(--times-body); line-height: 1.7; margin-bottom: 0.75rem;">
                  {lead_art.get('subhead', '')}
                </p>
                <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 1rem; border-top: 1px solid var(--times-light-border); padding-top: 0.75rem;">
                  <div style="display: flex; align-items: center; gap: 0.75rem; font-size: 0.8rem; color: var(--times-muted);">
                    <span>🎧 英国高品位朗読 ＆ 対話解説完備</span>
                    <span>•</span>
                    <span>📝 入試実戦4択クイズ3問完備</span>
                  </div>
                  <a href="{lead_art['slug']}/index.html" style="display: inline-block; padding: 0.4rem 1rem; background: var(--times-black); color: #fff; text-decoration: none; font-size: 0.85rem; font-weight: 700;">
                    記事本文・解説を読む →
                  </a>
                </div>
              </div>
            </article>
            """
            
        # Other articles cards grid
        cards_html = ""
        for art in other_arts:
            q_count = len(art.get("quiz", []))
            cards_html += f"""
            <div class="archive-card" style="display: flex; flex-direction: column; justify-content: space-between;">
              <div>
                <div class="archive-card-meta">
                  <span class="category-tag">{art.get('category_label', meta['title_en'])}</span>
                  <span class="archive-date-tag">🎧 音声完備</span>
                </div>
                <h3 class="archive-card-title">
                  <a href="{art['slug']}/index.html">{art['title']}</a>
                </h3>
                <p class="archive-card-ja">{art.get('headline_ja', '')}</p>
                <p class="archive-card-snippet">{art.get('subhead', '')}</p>
              </div>
              <div class="archive-card-footer" style="margin-top: 1rem; padding-top: 0.75rem; border-top: 1px solid var(--times-light-border); display: flex; align-items: center; justify-content: space-between;">
                <span class="archive-source-tag">出典: {art.get('source_name', '')}</span>
                <a href="{art['slug']}/index.html" style="font-size: 0.8rem; font-weight: 700; color: var(--times-blue); text-decoration: underline;">
                  演習を開く ({q_count}問) →
                </a>
              </div>
            </div>
            """
            
        # Key phrases HTML
        phrases_html = ""
        for phr, exp in meta["key_phrases"]:
            phrases_html += f"""
            <div style="padding: 0.6rem 0; border-bottom: 1px solid var(--times-light-border);">
              <div style="font-family: var(--font-headline); font-size: 1rem; font-weight: bold; color: var(--times-black);">
                {phr}
              </div>
              <div style="font-size: 0.85rem; color: var(--times-muted); margin-top: 0.2rem;">
                {exp}
              </div>
            </div>
            """

        cat_page_html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{meta['title_en']} ({meta['title_ja']}) | THE ACADEMIC TIMES</title>
  <meta name="description" content="THE ACADEMIC TIMES {meta['title_en']} カテゴリ専用ポータル。{meta['subtitle']}">
  
  <!-- CSS -->
  <link rel="stylesheet" href="../styles/times.css">
</head>
<body>

  <!-- Top Date Bar -->
  <div class="top-date-bar">
    Tuesday October 6 2026 &nbsp;|&nbsp; Tokyo & London Editions &nbsp;•&nbsp; {meta['title_en']} Academic Portal
  </div>

  <!-- The Times Masthead -->
  <header class="masthead">
    <a href="../index.html" class="masthead-link">
      <span class="masthead-title">THE ACADEMIC TIMES</span>
    </a>
    <div class="masthead-subtitle">{meta['title_en']} • {meta['subtitle']}</div>
  </header>

  <!-- Navigation Bar -->
  <nav class="nav-bar">
    <div class="nav-container">
      <ul class="nav-list">
        <li class="nav-item"><a href="../index.html">Home</a></li>
        <li class="nav-item {soc_act}"><a href="../society/index.html">Society & Mind</a></li>
        <li class="nav-item {sci_act}"><a href="../science/index.html">Science & Tech</a></li>
        <li class="nav-item {cul_act}"><a href="../culture/index.html">Culture & Thought</a></li>
        <li class="nav-item {law_act}"><a href="../law/index.html">Law & Justice</a></li>
        <li class="nav-item {wor_act}"><a href="../world/index.html">World & Security</a></li>
        <li class="nav-item"><a href="../index.html#section-archive" style="color: var(--times-red); font-weight: 700;">🔍 過去記事検索</a></li>
        <li class="nav-item"><a href="../index.html#section-media-literacy">高校生向けメディア解説</a></li>
      </ul>
    </div>
  </nav>

  <!-- Section Hero Header -->
  <header style="background: #fafafa; border-bottom: 2px solid var(--times-black); padding: 2.5rem 1rem 2rem;">
    <div class="page-wrapper" style="padding-top: 0; padding-bottom: 0;">
      <div style="font-size: 0.8125rem; font-weight: 700; letter-spacing: 0.15em; color: var(--times-blue); margin-bottom: 0.5rem; text-transform: uppercase;">
        ACADEMIC FIELD SPECIAL EDITION
      </div>
      <h1 style="font-family: var(--font-headline); font-size: 2.4rem; font-weight: 700; color: var(--times-black); line-height: 1.15; margin-bottom: 0.5rem;">
        {meta['title_en']} <span style="font-size: 1.4rem; font-weight: 400; color: #555;">({meta['title_ja']})</span>
      </h1>
      <p style="font-size: 0.95rem; color: var(--times-body); line-height: 1.7; max-width: 820px; margin-bottom: 1rem;">
        {meta['description']}
      </p>
      
      <!-- Exam Strategy Box -->
      <div style="background: #fff; border-left: 3px solid var(--times-black); padding: 0.85rem 1.25rem; font-size: 0.85rem; line-height: 1.65; color: #333;">
        <strong>🎓 難関大入試における出題傾向と攻略ポイント：</strong><br>
        {meta['exam_strategy']}
      </div>
    </div>
  </header>

  <!-- Main Content -->
  <main class="page-wrapper">
    
    <!-- Section 1: Featured Lead Article -->
    <section style="margin-bottom: 3rem;">
      <div class="section-heading-bar">
        <h2 class="section-heading">FEATURED ARTICLES IN THIS GENRE (本分野の配信記事一覧)</h2>
        <span style="font-size: 0.8rem; color: var(--times-muted);">全{len(cat_articles)}本 配信中（すべて音声・クイズ完備）</span>
      </div>

      {lead_html}

      <!-- Grid of other articles in category -->
      <div class="archive-results-grid" style="grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); margin-top: 1.5rem;">
        {cards_html}
      </div>
    </section>

    <!-- Section 2: Key Academic Vocabulary & Discourse Highlights -->
    <section class="study-section" style="margin-top: 3.5rem;">
      <div class="section-heading-bar">
        <h2 class="section-heading">ESSENTIAL DISCOURSE VOCABULARY ({meta['title_ja']} 頻出学術語彙・構文)</h2>
        <span style="font-size: 0.8rem; color: var(--times-muted);">東大・京大・早慶・難関大入試で差がつくキーワード5選</span>
      </div>
      <div style="background: #fff; border: 1px solid var(--times-light-border); padding: 1.25rem 1.5rem;">
        {phrases_html}
      </div>
    </section>

    <!-- Section 3: Cross-Category Navigation -->
    <section class="study-section" style="margin-top: 3rem; background: #fdfdfd; border: 1px solid var(--times-light-border); padding: 1.5rem;">
      <h3 style="font-family: var(--font-headline); font-size: 1.15rem; margin-bottom: 0.75rem;">
        🌐 他の学術カテゴリを見る
      </h3>
      <div style="display: flex; flex-wrap: wrap; gap: 0.5rem;">
        <a href="../society/index.html" style="padding: 0.4rem 0.85rem; border: 1px solid var(--times-light-border); background: #fff; color: var(--times-black); text-decoration: none; font-size: 0.82rem; font-weight: 600;">Society & Mind (社会・心理)</a>
        <a href="../science/index.html" style="padding: 0.4rem 0.85rem; border: 1px solid var(--times-light-border); background: #fff; color: var(--times-black); text-decoration: none; font-size: 0.82rem; font-weight: 600;">Science & Tech (科学・医学)</a>
        <a href="../culture/index.html" style="padding: 0.4rem 0.85rem; border: 1px solid var(--times-light-border); background: #fff; color: var(--times-black); text-decoration: none; font-size: 0.82rem; font-weight: 600;">Culture & Thought (文化・思想)</a>
        <a href="../law/index.html" style="padding: 0.4rem 0.85rem; border: 1px solid var(--times-light-border); background: #fff; color: var(--times-black); text-decoration: none; font-size: 0.82rem; font-weight: 600;">Law & Justice (法律・制度)</a>
        <a href="../world/index.html" style="padding: 0.4rem 0.85rem; border: 1px solid var(--times-light-border); background: #fff; color: var(--times-black); text-decoration: none; font-size: 0.82rem; font-weight: 600;">World & Security (世界・安保)</a>
      </div>
    </section>

  </main>

  <!-- The Times UK Style Footer -->
  <footer class="times-footer">
    <div class="footer-container">
      <div class="footer-top">
        <a href="../index.html" class="footer-logo">THE ACADEMIC TIMES</a>
        <div style="font-size: 0.8125rem; color: #888;">
          The Independent Broadsheet for University Entrance Examination & Liberal Arts English
        </div>
      </div>
      <div class="footer-grid">
        <div class="footer-col">
          <h4>About The Academic Times</h4>
          <p style="font-size: 0.8125rem; line-height: 1.7; color: #999;">
            海外高級紙から大学入試長文・難関大英作文・学術研究に資する記事を毎日厳選。ファクトチェックと音声（Edge-TTS）を備えたアカデミック英語ニュースサイトです。
          </p>
        </div>
        <div class="footer-col">
          <h4>Academic Categories</h4>
          <ul class="footer-links">
            <li><a href="../society/index.html">Society & Mind</a></li>
            <li><a href="../science/index.html">Science & Tech</a></li>
            <li><a href="../culture/index.html">Culture & Thought</a></li>
            <li><a href="../law/index.html">Law & Justice</a></li>
            <li><a href="../world/index.html">World & Security</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Daily Broadsheet Editions</h4>
          <ul class="footer-links">
            <li><a href="../index.html">本日付 最新号</a></li>
            <li><a href="../edition-2026-10-05.html">10月5日号 (防衛シールド・司法審査)</a></li>
            <li><a href="../edition-2026-10-04.html">10月4日号 (若年大腸がん・海洋熱波)</a></li>
            <li><a href="../edition-2026-10-03.html">10月3日号 (小児AI診断・古生物学)</a></li>
            <li><a href="../edition-2026-10-02.html">10月2日号 (相続税改革・農村起業)</a></li>
            <li><a href="../edition-2026-10-01.html">10月1日号 (創刊号・米軍再配置)</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <div>© 2026 THE ACADEMIC TIMES. All Rights Reserved.</div>
        <div><a href="../index.html" style="color: #aaa;">Homeに戻る ↑</a></div>
      </div>
    </div>
  </footer>

</body>
</html>
"""
        target_path = os.path.join(cat_dir, "index.html")
        with open(target_path, "w", encoding="utf-8") as f:
            f.write(cat_page_html)
        print(f"[OK] Generated Category Portal: {cat_key}/index.html ({len(cat_articles)} articles)")

if __name__ == "__main__":
    generate_category_pages()
