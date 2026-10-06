# -*- coding: utf-8 -*-
"""
Generates standalone, pre-rendered Daily Edition top pages for:
- 2026-10-04 (Sun)
- 2026-10-03 (Sat)
- 2026-10-02 (Fri)
- 2026-10-01 (Thu)
- (and 2026-10-05)
Matching the broadsheet layout of THE ACADEMIC TIMES index.html.
"""

import os
import sys

# Master article data dictionary
ARTICLES_DATA = {
    "headphones-in-public": {
        "title": "The Case Against Wearing Headphones in Public: Reclaiming the Power of Reverie",
        "category_label": "COGNITIVE PSYCHOLOGY & CULTURE",
        "path": "culture/headphones-in-public/index.html",
        "lead_snippet": "英国通信庁（Ofcom）の最新調査では成人の93%が毎週音声メディアに浸り、1日の中の「すべての静寂の合間」が埋め尽くされている。公共空間でイヤホンを外したジャーナリストの気づきから、認知心理学が解き明かす「意図せぬ白昼夢」と「見知らぬ他者との偶発的交流」がもたらす計り知れない効用を精読する。",
        "subhead": "米週刊誌TIME掲載のエッセイ。常時接続と孤独、創造性を育む退屈の価値を認知心理学で徹底解説。",
        "headline_ja": "公共空間でイヤホンを外す効用：失われた「物思い（白昼夢）」を取り戻す",
        "source_name": "TIME Magazine (Oct 5, 2026 / Meehika Barua)",
        "image": "https://static.time.com/v3/assets/bltea6093859af6183b/blt96d6f358ea9d50b0/6abfba6215869b08e9e95a32/headphones.jpg?branch=production&width=1200&quality=80&auto=webp"
    },
    "jeffrey-archer-obituary": {
        "title": "Jeffrey Archer, Bestselling Novelist and Political Figure, Dies Aged 86",
        "category_label": "CULTURE & OBITUARY",
        "path": "culture/jeffrey-archer-obituary/index.html",
        "lead_snippet": "世界的ベストセラー『ケインとアベル』で知られる英国の小説家・政治家ジェフリー・アーチャー氏の生涯。栄光と服役、そして不屈の復活劇を英国高級紙の格調高い評伝英語で読み解く。",
        "subhead": "3億部を売り上げた英国大衆文学の巨匠の軌跡。伝記・文学論述における時制と修辞を学ぶ。",
        "headline_ja": "ベストセラー作家で元政治家のジェフリー・アーチャー氏が86歳で死去",
        "source_name": "The Times UK / The Guardian (Oct 1, 2026)",
        "image": "https://images.unsplash.com/photo-1457369804613-52c61a468e7d?w=1000&auto=format&fit=crop&q=80"
    },
    "air-defence-shield": {
        "title": "British Parliament Debates £10bn Integrated Air Defence Shield",
        "category_label": "LAW & NATIONAL SECURITY",
        "path": "law/air-defence-shield/index.html",
        "lead_snippet": "防空レーダー網と迎撃システムの刷新を巡る英国議会の白熱した討論。国家安全保障上の機密保持と公的資金の使途説明責任（accountability）という法哲学的ジレンマを検証する。",
        "subhead": "防衛装備調達の透明性と国家安全保障法制。財政民主主義の観点から法学英語を精読。",
        "headline_ja": "英国議会、100億ポンド規模の統合防空シールド配備をめぐり審議入り",
        "source_name": "Financial Times / The Times UK (Oct 5, 2026)",
        "image": "https://images.unsplash.com/photo-1541872703-74c5e44368f9?w=1000&auto=format&fit=crop&q=80"
    },
    "royal-security-judicial-review": {
        "title": "King Will Not Fund Legal Challenge Against Security Withdrawal",
        "category_label": "LAW & CONSTITUTION",
        "path": "law/royal-security-judicial-review/index.html",
        "lead_snippet": "王室離脱後の公的警護費用をめぐる法廷闘争。税金による警護の妥当性と行政裁量権の限界を、英米法の最高裁判例のロジックから読み解く。",
        "subhead": "王室経費と公的警護権をめぐる司法審査（judicial review）の基本概念と行政法論述。",
        "headline_ja": "国王、公的警護打ち切りに対する法的異議申し立てへの資金拠出を拒否",
        "source_name": "The Telegraph / The Times UK (Oct 5, 2026)",
        "image": "https://images.unsplash.com/photo-1589829545856-d10d557cf95f?w=1000&auto=format&fit=crop&q=80"
    },
    "ai-pediatric-diagnosis-consent": {
        "title": "High Court Weighs Parental Consent in AI-Driven Pediatric Diagnoses",
        "category_label": "LAW & BIOETHICS",
        "path": "law/ai-pediatric-diagnosis-consent/index.html",
        "lead_snippet": "小児疾患の早期発見においてAI診断アルゴリズムが医師の所見と食い違った場合、親の治療選択権はどう保護されるのか。英米法におけるギリック能力（Gillick competence）の現代的解釈。",
        "subhead": "AI医療判断と親の同意権。アルゴリズムの説明責任とインフォームド・コンセントの再定義。",
        "headline_ja": "英高等法院、AIによる小児診療判断における親の同意権の範囲を審理",
        "source_name": "The Guardian / BMJ Health Tech (Oct 3, 2026)",
        "image": "https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?w=1000&auto=format&fit=crop&q=80"
    },
    "colorectal-cancer-under-50s": {
        "title": "Mystery Rise in Colorectal Cancer Rates Among Under-50s",
        "category_label": "SCIENCE & MEDICINE",
        "path": "science/colorectal-cancer-under-50s/index.html",
        "lead_snippet": "従来は高齢者特有とされていた大腸がんが若年層で急増している背景とは。超加工食品に含まれる乳化剤やマイクロプラスチックが生体組織に与える長期的影響を科学論文の論理展開で精読。",
        "subhead": "マイクロプラスチック、超加工食品、腸内細菌叢の変容。最新の医学疫学論文を平易に解説。",
        "headline_ja": "50歳未満における大腸がん罹患率の世界的急増：科学が追う環境要因の謎",
        "source_name": "Nature Medicine / BBC Health (Oct 4, 2026)",
        "image": "https://images.unsplash.com/photo-1532938911079-1b06ac7ceec7?w=1000&auto=format&fit=crop&q=80"
    },
    "generative-ai-paleontology": {
        "title": "Generative Neural Networks Reconstruct Locomotion in Extinct Vertebrates",
        "category_label": "SCIENCE & COMPUTATIONAL BIOLOGY",
        "path": "science/generative-ai-paleontology/index.html",
        "lead_snippet": "数千万年前に絶滅した生物の歩行速度や筋肉配置を、生成AIの物理シミュレーションによって再現。生物進化の謎を解き明かす先端テクノロジーの英語構文。",
        "subhead": "化石の断片から生体運動を再現する最新ディープラーニング技術。仮説検証の英文法。",
        "headline_ja": "生成ニューラルネットワーク、絶滅脊椎動物の運動メカニズムを生体復元",
        "source_name": "Science / MIT Technology Review (Oct 3, 2026)",
        "image": "https://images.unsplash.com/photo-1507668077129-56e32842fceb?w=1000&auto=format&fit=crop&q=80"
    },
    "mediterranean-marine-heatwaves": {
        "title": "Mediterranean Marine Heatwaves Threaten Deep-Water Coral Colonies",
        "category_label": "SCIENCE & MARINE ECOLOGY",
        "path": "science/mediterranean-marine-heatwaves/index.html",
        "lead_snippet": "水面下数十メートルから百メートル以上の深海域にまで及ぶ未知の海洋熱波。光の届かない冷水域で数百年かけて成長する深海サンゴの大量死滅が警告する海洋生態系の危機。",
        "subhead": "海水温躍層の崩壊と生物多様性の損失。環境変動の因果関係構文と科学的ファクトチェック。",
        "headline_ja": "地中海の海洋熱波、深海性サンゴ群集を直撃：深海生態系に迫る不可逆的危機",
        "source_name": "Reuters Science / Copernicus Climate Service (Oct 4, 2026)",
        "image": "https://images.unsplash.com/photo-1544551763-46a013bb70d5?w=1000&auto=format&fit=crop&q=80"
    },
    "psychology-casual-encounters": {
        "title": "The Psychology of Casual Encounters: Why Micro-Connections Boost Urban Well-Being",
        "category_label": "SOCIETY & BEHAVIORAL SCIENCE",
        "path": "society/psychology-casual-encounters/index.html",
        "lead_snippet": "「話しかけたら嫌がられるだろう」という人々の思い込み（多元的無知）を打ち破る社会心理学実験。カフェの店員やすれ違う人との挨拶が、都市生活者の主観的幸福度を劇的に高めるメカニズム。",
        "subhead": "シカゴ大学Epley教授の通勤実験とGranovetterの『弱い紐帯の強み』。都市社会学の最前線。",
        "headline_ja": "偶然の出会いの心理学：見知らぬ人とのささやかな会話が都市の幸福感を高める理由",
        "source_name": "Journal of Personality and Social Psychology / The Atlantic (Oct 6, 2026)",
        "image": "https://images.unsplash.com/photo-1477959858617-67f30bc75b82?w=1000&auto=format&fit=crop&q=80"
    },
    "clarkson-business-red-tape": {
        "title": "Jeremy Clarkson: Why Would Anyone Open a New Venture in Britain?",
        "category_label": "SOCIETY & RURAL ECONOMY",
        "path": "society/clarkson-business-red-tape/index.html",
        "lead_snippet": "人気テレビ司会者が地方農場レストラン経営で直面した過剰な規制と自治体官僚主義。起業意欲を削ぐ地方自治体のレッドテープ（お役所仕事）を痛烈に批判する論説文。",
        "subhead": "規制緩和と地方経済の疲弊。反語表現（Rhetorical Question）の読解演習と経済英語。",
        "headline_ja": "ジェレミー・クラークソン氏寄稿：『いま英国で誰が新規事業など始めるのか？』",
        "source_name": "The Sunday Times (Oct 5, 2026)",
        "image": "https://images.unsplash.com/photo-1500382017468-9049fed747ef?w=1000&auto=format&fit=crop&q=80"
    },
    "inheritance-tax-reform-debate": {
        "title": "Badenoch Puts Inheritance Tax Reform at the Heart of Policy Agenda",
        "category_label": "SOCIETY & POLITICAL ECONOMY",
        "path": "society/inheritance-tax-reform-debate/index.html",
        "lead_snippet": "富の世代間移転と機会の平等（equality of opportunity）をめぐる英国保守党の税制改革論争。親が築いた資産を子が受け継ぐ正当性と、再分配を重視する累進課税の思想的対立。",
        "subhead": "相続税と世代間格差。税制倫理を論じる大学入試論述頻出のキーワード群と政治哲学。",
        "headline_ja": "英国保守党党首候補ベイデノック氏、相続税改革を政策綱領の核心に提示",
        "source_name": "The Times UK / Financial Times (Oct 2, 2026)",
        "image": "https://images.unsplash.com/photo-1554224155-8d04cb21cd6c?w=1000&auto=format&fit=crop&q=80"
    },
    "raf-fairford-bomber-redeployment": {
        "title": "US Strategic Bombers Relocated From RAF Fairford Amid Regional Drone Alerts",
        "category_label": "WORLD & DIPLOMACY",
        "path": "world/raf-fairford-bomber-redeployment/index.html",
        "lead_snippet": "党派的プロパガンダを排し、NATO集団防衛条約第5条および地位協定（SOFA）に基づく戦力再配備を客観的事実として報道。抑止力維持とエスカレーション防止の国際関係論。",
        "subhead": "国際法・安保条約上の兵力再配置（redeployment）と抑止力（deterrence）の軍事・外交英語構文。",
        "headline_ja": "米空軍戦略爆撃機、中東ドローン警戒の高まりを受けフェアフォード英空軍基地から再配置",
        "source_name": "Reuters / AP News (Oct 1, 2026)",
        "image": "https://images.unsplash.com/photo-1508614589041-895b88991e3e?w=1000&auto=format&fit=crop&q=80"
    }
}

EDITIONS_CONFIG = {
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
    },
    "2026-10-05": {
        "dateStr": "Monday October 5 2026",
        "editionLabel": "2026年10月5日 (月) 号 【バックナンバー】",
        "tagline": "特集：英国100億ポンド防衛シールド審議と司法審査・王室警護裁量",
        "topLeadSlug": "air-defence-shield",
        "subLeadSlugs": ["royal-security-judicial-review", "clarkson-business-red-tape"],
        "leftDispatches": ["headphones-in-public", "inheritance-tax-reform-debate", "mediterranean-marine-heatwaves"],
        "rightDigestSlugs": ["jeffrey-archer-obituary", "ai-pediatric-diagnosis-consent", "colorectal-cancer-under-50s", "raf-fairford-bomber-redeployment"]
    }
}

def generate_edition_page(date_key):
    ed = EDITIONS_CONFIG[date_key]
    lead = ARTICLES_DATA[ed["topLeadSlug"]]
    sub_leads = [ARTICLES_DATA[s] for s in ed["subLeadSlugs"]]
    left_articles = [ARTICLES_DATA[s] for s in ed["leftDispatches"]]
    right_articles = [ARTICLES_DATA[s] for s in ed["rightDigestSlugs"]]
    
    # Left Column HTML
    left_html = ""
    for idx, art in enumerate(left_articles):
        badge = "badge-new" if idx == 0 else "badge-updated"
        badge_txt = "NEW" if idx == 0 else "DISPATCH"
        left_html += f"""
        <article class="left-story">
          <span class="{badge}">{badge_txt} • {art['category_label']}</span>
          <h2 class="left-story-title">
            <a href="{art['path']}">{art['title']}</a>
          </h2>
          <p class="left-story-snippet">
            {art['headline_ja']}。{art['subhead']}
          </p>
          <div class="article-source-meta">
            <span>According to {art['source_name']}</span>
          </div>
        </article>
        """
        
    # Sub-leads HTML
    sub_leads_html = ""
    for sub in sub_leads:
        sub_leads_html += f"""
        <div class="sub-lead-item">
          <div style="height: 120px; overflow: hidden; margin-bottom: 0.5rem; background: #e9ecef;">
            <img src="{sub['image']}" alt="{sub['title']}" style="width: 100%; height: 100%; object-fit: cover;" onerror="this.style.display='none'">
          </div>
          <span class="category-tag">{sub['category_label']}</span>
          <h3 class="sub-lead-title">
            <a href="{sub['path']}">{sub['title']}</a>
          </h3>
          <p style="font-size: 0.8rem; color: var(--times-muted); margin-top: 0.25rem;">
            {sub['subhead']}
          </p>
        </div>
        """
        
    # Right Column HTML
    right_html = ""
    for art in right_articles:
        right_html += f"""
        <article class="right-story">
          <div class="right-story-body">
            <span class="category-tag">{art['category_label']}</span>
            <h3 class="right-story-title">
              <a href="{art['path']}">{art['title']}</a>
            </h3>
            <p style="font-size: 0.8rem; color: var(--times-muted);">
              {art['headline_ja']}
            </p>
          </div>
          <div class="right-story-img" style="background: #e2e4e8; overflow: hidden;">
            <img src="{art['image']}" alt="{art['title']}" style="width: 100%; height: 100%; object-fit: cover;" onerror="this.style.display='none'">
          </div>
        </article>
        """

    # Build options
    all_dates = [
        ("2026-10-06", "2026年10月6日 (火) 号 【本日付・最新】"),
        ("2026-10-05", "2026年10月5日 (月) 号 【防衛シールド・王室警護】"),
        ("2026-10-04", "2026年10月4日 (日) 号 【若年大腸がん・海洋熱波】"),
        ("2026-10-03", "2026年10月3日 (土) 号 【小児AI診断・古生物学】"),
        ("2026-10-02", "2026年10月2日 (金) 号 【相続税改革・農村起業規制】"),
        ("2026-10-01", "2026年10月1日 (木) 号 【創刊号・米軍再配置・アーチャー追悼】"),
    ]
    options_html = ""
    for d_val, d_label in all_dates:
        sel = "selected" if d_val == date_key else ""
        options_html += f'          <option value="{d_val}" {sel}>{d_label}</option>\n'

    # Read base index.html to reuse sections 4, 5, 6, footer, head
    base_index_path = os.path.join(os.path.dirname(__file__), "..", "index.html")
    with open(base_index_path, "r", encoding="utf-8") as f:
        base_html = f.read()
        
    # We replace top-date-bar, notice-banner, hero section, and select options
    html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{ed['editionLabel']} | THE ACADEMIC TIMES</title>
  <meta name="description" content="THE ACADEMIC TIMES {ed['editionLabel']}。{ed['tagline']}">
  
  <!-- CSS -->
  <link rel="stylesheet" href="styles/times.css">
</head>
<body data-default-edition="{date_key}">

  <!-- Top Date Bar & Paper Edition Selector -->
  <div class="top-date-bar">
    <div class="top-date-bar-inner">
      <span id="top-date-bar-text">{ed['dateStr']} &nbsp;|&nbsp; Tokyo & London Editions &nbsp;•&nbsp; Daily University Exam Academic Digest</span>
      <div class="edition-selector-wrap">
        <span style="font-weight: 700; color: #111;">📅 紙面切替:</span>
        <select id="select-edition-date" class="edition-select" aria-label="Select edition date">
{options_html}        </select>
        <button type="button" class="edition-btn" id="btn-edition-prev" title="前日の紙面へ">◀ 前日</button>
        <button type="button" class="edition-btn" id="btn-edition-next" title="翌日の紙面へ">翌日 ▶</button>
      </div>
    </div>
  </div>

  <!-- The Times Style Masthead -->
  <header class="masthead">
    <a href="index.html" class="masthead-link">
      <span class="masthead-title">THE ACADEMIC TIMES</span>
    </a>
    <div class="masthead-subtitle">The Daily Broadsheet for Scholarly English, Global News & Critical Analysis</div>
  </header>

  <!-- Navigation Bar -->
  <nav class="nav-bar">
    <div class="nav-container">
      <ul class="nav-list">
        <li class="nav-item active"><a href="index.html">Home</a></li>
        <li class="nav-item"><a href="society/index.html">Society & Mind</a></li>
        <li class="nav-item"><a href="science/index.html">Science & Tech</a></li>
        <li class="nav-item"><a href="culture/index.html">Culture & Thought</a></li>
        <li class="nav-item"><a href="law/index.html">Law & Justice</a></li>
        <li class="nav-item"><a href="world/index.html">World & Security</a></li>
        <li class="nav-item"><a href="#section-archive" style="color: var(--times-red); font-weight: 700;">🔍 過去記事検索</a></li>
        <li class="nav-item"><a href="#section-media-literacy">高校生向けメディア解説</a></li>
      </ul>
    </div>
  </nav>

  <!-- Past Edition Notice Banner -->
  <div class="page-wrapper" style="padding-top: 0; padding-bottom: 0;">
    <div id="edition-notice-banner" class="edition-notice-banner" style="display: block;">
      <span>📅 表示中：<strong>{ed['editionLabel']}</strong> — {ed['tagline']}</span>
      <a href="index.html" class="btn-return-today" style="text-decoration: none;">本日最新号に戻る ↺</a>
    </div>
  </div>

  <!-- Sub Banner -->
  <div class="sub-banner">
    <div class="sub-banner-content">
      <div>
        <div class="sub-banner-title">Empower Your Academic English with Authentic Daily Broadsheets.</div>
        <div class="sub-banner-desc">入試出題頻出の科学・社会・法制度・国際情勢を、ファクトチェック済み英文と英国高品位音声（Edge-TTS）で毎日更新。</div>
      </div>
      <div class="sub-banner-actions">
        <a href="#section-archive" class="btn-trial">過去記事検索</a>
        <a href="{lead['path']}" class="login-link">この号のトップ記事を読む →</a>
      </div>
    </div>
  </div>

  <!-- Main Container -->
  <main class="page-wrapper">

    <!-- HERO SECTION: 3-COLUMN THE TIMES LAYOUT -->
    <div class="home-grid">
      
      <!-- LEFT COLUMN -->
      <aside class="home-col-left">
{left_html}
      </aside>

      <!-- CENTER COLUMN -->
      <section class="home-col-center">
        <article>
          <div class="lead-image-wrap">
            <img src="{lead['image']}" alt="{lead['title']}" class="lead-image" onerror="this.src='https://images.unsplash.com/photo-1508700115892-45ecd05ae2ad?w=1000&auto=format&fit=crop&q=80'">
          </div>
          <span class="category-tag">TOP LEAD STORY • {lead['category_label']}</span>
          <h1 class="lead-story-title">
            <a href="{lead['path']}">{lead['title']}</a>
          </h1>
          <p class="lead-story-lead">
            {lead['lead_snippet']}
          </p>
          <div class="article-source-meta" style="margin-top: 0.75rem;">
            <strong>Source:</strong> <span>{lead['source_name']}</span>
          </div>
        </article>

        <!-- Sub-leads inside Center Column -->
        <div class="sub-lead-grid">
{sub_leads_html}
        </div>
      </section>

      <!-- RIGHT COLUMN -->
      <aside class="home-col-right">
{right_html}
      </aside>

    </div>
"""

    # Extract the bottom sections from index.html (from Section 2 to footer and scripts)
    sec2_mark = "<!-- ==========================================================================\n         SECTION 2: CATEGORY BLOCKS"
    sec2_idx = base_html.find(sec2_mark)
    if sec2_idx == -1:
        sec2_idx = base_html.find("SECTION 2: CATEGORY BLOCKS")
        sec2_idx = base_html.rfind("<!--", 0, sec2_idx)

    bottom_part = base_html[sec2_idx:]
    full_page = html + "\n" + bottom_part
    return full_page

def main():
    target_dates = ["2026-10-04", "2026-10-03", "2026-10-02", "2026-10-01", "2026-10-05"]
    out_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    
    for d in target_dates:
        filename = f"edition-{d}.html"
        filepath = os.path.join(out_dir, filename)
        content = generate_edition_page(d)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"[OK] Generated {filename} for {d}")

if __name__ == "__main__":
    main()
