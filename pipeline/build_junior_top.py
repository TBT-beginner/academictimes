# -*- coding: utf-8 -*-
"""
Generates news_portal/junior/index.html
The broadsheet top page for THE JUNIOR (Eiken Pre-2 ~ 2 Edition).
Fully matching The Academic Times layout:
- Interactive Edition Switcher (10/6, 10/5, 10/4, 10/3, 10/2, 10/1)
- 3-Column Broadsheet Hero (Left 3 stories + Center Lead & 2 Sub-leads + Right 4 stories with thumbnails)
- Category Blocks (5 Academic & Exam Genres)
- Most Read Ranking (Top 5)
- Back Numbers & Instant Article Search (Live keyword search, Category buttons, Source filter, 15 cards)
- Essential Media & Eiken Study Guide
- 4-Column Broadsheet Footer
"""

import os
from junior_articles_data import JUNIOR_ARTICLES
from build_junior_data_js import JUNIOR_STUDY_RESOURCES

PORTAL_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
JUNIOR_INDEX_PATH = os.path.join(PORTAL_DIR, "junior", "index.html")

def generate_junior_index():
    # Map articles by slug
    art_map = {a["slug"]: a for a in JUNIOR_ARTICLES}
    
    # 10/9 Default Edition Stories
    lead = art_map.get("stoic-philosophy-digital-age", JUNIOR_ARTICLES[6])
    sub1 = art_map.get("headphones-in-public", JUNIOR_ARTICLES[0])
    sub2 = art_map.get("psychology-casual-encounters", JUNIOR_ARTICLES[2])
    
    left1 = art_map.get("critical-minerals-geopolitics", JUNIOR_ARTICLES[4])
    left2 = art_map.get("colorectal-cancer-under-50s", JUNIOR_ARTICLES[1])
    left3 = art_map.get("air-defence-shield", JUNIOR_ARTICLES[3])
    
    right1 = art_map.get("mediterranean-marine-heatwaves", JUNIOR_ARTICLES[8])
    right2 = art_map.get("ai-pediatric-diagnosis-consent", JUNIOR_ARTICLES[11])
    right3 = art_map.get("clarkson-business-red-tape", JUNIOR_ARTICLES[9])
    right4 = art_map.get("generative-ai-paleontology", JUNIOR_ARTICLES[7])

    # Pre-render all 15 catalog cards for initial display & SEO
    cards_html = []
    for art in JUNIOR_ARTICLES:
        card = f"""
        <div class="junior-catalog-card" style="border: 1px solid var(--times-light-border); padding: 1.25rem; background: #fff; margin-bottom: 1.25rem; display: flex; flex-direction: column; justify-content: space-between;">
          <div>
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
              <span class="category-tag green-fill" style="padding: 0.15rem 0.45rem;">{art['category'].upper()}</span>
              <span style="font-size: 0.75rem; color: #235937; font-weight: 700;">英検準2級〜2級 • 🎧 音声＆クイズ</span>
            </div>
            <h3 style="font-family: var(--font-headline); font-size: 1.15rem; margin-bottom: 0.35rem; line-height: 1.35;">
              <a href="{art['category']}/{art['slug']}/index.html" style="color: var(--times-black); text-decoration: none;">
                {art['title']}
              </a>
            </h3>
            <p style="font-size: 0.85rem; font-weight: 700; color: #222; margin-bottom: 0.4rem;">
              {art['headline_ja']}
            </p>
            <p style="font-size: 0.8rem; color: var(--times-muted); line-height: 1.6;">
              {art['subhead']}
            </p>
          </div>
          <div style="margin-top: 1rem; padding-top: 0.75rem; border-top: 1px dashed #e0e0e0; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 0.5rem;">
            <a href="{art['category']}/{art['slug']}/index.html" style="color: #235937; font-weight: 700; font-size: 0.82rem; text-decoration: underline;">
              🌱 Junior版を読む（音声付） →
            </a>
            <a href="../{art['category']}/{art['slug']}/index.html" style="color: #111; font-size: 0.78rem; text-decoration: none;">
              🏛️ 発展版（難関大） ↗
            </a>
          </div>
        </div>
        """
        cards_html.append(card)
    cards_str = "\n".join(cards_html)

    media_cards_html = []
    for media in JUNIOR_STUDY_RESOURCES:
        title_en = media.get("title_en", media["name"])
        title_ja = media.get("title_ja", "")
        tip_text = media.get("tip", "")
        tip_html = f"""
        <div class="junior-media-footer">
          <span>💡 <strong>学習のコツ：</strong>{tip_text}</span>
        </div>
        """ if tip_text else ""
        
        m_card = f"""
        <div class="junior-media-card">
          <div class="junior-media-badge-wrap">
            <span class="junior-media-badge">{media['badge']}</span>
          </div>
          <div class="junior-media-header">
            <h3 class="junior-media-title-en">{title_en}</h3>
            {f'<div class="junior-media-title-ja">{title_ja}</div>' if title_ja else ''}
          </div>
          <div class="junior-media-body">
            {media['point']}
          </div>
          {tip_html}
        </div>
        """
        media_cards_html.append(m_card)
    media_cards_str = "\n".join(media_cards_html)

    html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>THE JUNIOR | 高校生・英検準2級〜2級のための本格英語ニュースポータル</title>
  <meta name="description" content="THE ACADEMIC TIMESの公式兄弟サイト。世界の本格ニュースを英検準2級〜2級（CEFR A2〜B1）の標準英語、135wpmのゆっくり音声、Keita先生とNanamiさんの掛け合い対話で学ぶ日刊ポータル。">
  <link rel="stylesheet" href="../styles/times.css">
  <link rel="stylesheet" href="styles/times-junior.css">
  <style>
    .junior-hero-lead-box {{
      border-bottom: 1px solid var(--times-light-border);
      padding-bottom: 1.5rem;
      margin-bottom: 1.5rem;
    }}
    .cat-card-genre.junior-genre {{
      color: #235937 !important;
    }}
  </style>
</head>
<body class="times-theme" id="junior-top">

  <!-- Top Switcher Bar with Interactive Edition Switcher -->
  <div class="top-date-bar">
    <div style="display: flex; justify-content: space-between; align-items: center; max-width: 1200px; margin: 0 auto; padding: 0 1rem; flex-wrap: wrap; gap: 0.5rem;">
      <span id="top-date-bar-text">Friday October 9 2026 &nbsp;|&nbsp; Tokyo & London Editions &nbsp;•&nbsp; High School Eiken Pre-2 ~ 2 Broadsheet</span>
      <div class="edition-selector-wrap">
        <span style="font-weight: 700; color: #111;">📅 紙面切替:</span>
        <select id="select-edition-date" class="edition-select" aria-label="Select edition date">
          <option value="2026-10-09" selected>2026年10月9日 (金) 号 【本日付・最新】</option>
          <option value="2026-10-08">2026年10月8日 (木) 号 【重要鉱物の争奪戦・ストア哲学】</option>
          <option value="2026-10-07">2026年10月7日 (水) 号 【挨拶の魔法・北極海航路】</option>
          <option value="2026-10-06">2026年10月6日 (火) 号 【イヤホン論争・静かな時間】</option>
          <option value="2026-10-05">2026年10月5日 (月) 号 【防空計画・王室警護】</option>
          <option value="2026-10-04">2026年10月4日 (日) 号 【若年健康・海洋温暖化】</option>
          <option value="2026-10-03">2026年10月3日 (土) 号 【AI診断・恐竜の歩行】</option>
          <option value="2026-10-02">2026年10月2日 (金) 号 【相続税議論・ストア哲学】</option>
          <option value="2026-10-01">2026年10月1日 (木) 号 【創刊号・航空機分散・アーチャー追悼】</option>
        </select>
        <button type="button" class="edition-btn" id="btn-edition-prev" title="前日の紙面へ">◀ 前日</button>
        <button type="button" class="edition-btn" id="btn-edition-next" title="翌日の紙面へ" disabled>翌日 ▶</button>
        <a href="../index.html" class="edition-btn" style="background: #111; color: #fff; border-color: #111; text-decoration: none; font-weight: 700; margin-left: 0.5rem;" title="難関国公立・早慶・英検準1〜1級レベルへ">🏛️ 発展・難関大版へ ↗</a>
      </div>
    </div>
  </div>

  <!-- The Times Junior Masthead -->
  <header class="masthead-junior">
    <a href="index.html" class="masthead-link" style="text-decoration: none;">
      <h1 class="masthead-junior-title">THE JUNIOR</h1>
    </a>
    <div class="masthead-junior-tagline">The Stepping Stone to World News • English for High School Students</div>
    <div class="masthead-junior-sub">英検準2級〜2級の基礎・標準英語で読む世界の一流ニュース</div>
  </header>

  <!-- Navigation Bar -->
  <nav class="nav-bar">
    <div class="nav-container">
      <ul class="nav-list">
        <li class="nav-item active"><a href="index.html">Junior Home</a></li>
        <li class="nav-item"><a href="#cat-culture">Culture & Thought</a></li>
        <li class="nav-item"><a href="#cat-science">Science & Tech</a></li>
        <li class="nav-item"><a href="#cat-society">Society & Mind</a></li>
        <li class="nav-item"><a href="#cat-law">Law & Justice</a></li>
        <li class="nav-item"><a href="#cat-world">World & Security</a></li>
        <li class="nav-item"><a href="../nobel-prize/index.html" style="color: #b8860b; font-weight: 700;">🏆 2026ノーベル賞特設解説</a></li>
        <li class="nav-item"><a href="#section-archive" style="color: #235937; font-weight: 700;">🔍 記事一覧・検索</a></li>
        <li class="nav-item"><a href="#section-guide">高校生向け学習ガイド</a></li>
        <li class="nav-item" style="margin-left: auto;">
          <a href="../index.html" style="color: var(--times-black); font-weight: 700;">発展・難関大版へ ↗</a>
        </li>
      </ul>
    </div>
  </nav>

  <!-- Past Edition Notice Banner (Displayed when browsing older editions) -->
  <div class="page-wrapper" style="padding-top: 0; padding-bottom: 0;">
    <div id="edition-notice-banner" class="edition-notice-banner" style="display: none;"></div>
  </div>

  <!-- Sub-Banner (Empower Your English) -->
  <div class="sub-banner" style="background: var(--junior-light-green); border-bottom: 2px solid var(--junior-green);">
    <div class="sub-banner-content" style="max-width: 1200px; margin: 0 auto; padding: 0.85rem 1rem; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 0.75rem;">
      <div>
        <div class="sub-banner-title" style="font-family: var(--font-headline); font-size: 1.05rem; font-weight: 700; color: var(--junior-dark-green);">
          Empower Your English with Authentic Junior Broadsheets.
        </div>
        <div class="sub-banner-desc" style="font-size: 0.82rem; color: #1e452a; margin-top: 0.2rem;">
          世界の本格ニュースを、英検準2級〜2級（CEFR A2〜B1）の標準英語と135wpmのゆっくり音声で毎日配信。
        </div>
      </div>
      <div class="sub-banner-actions" style="display: flex; gap: 0.5rem; align-items: center;">
        <a href="#ranking" class="btn-trial" style="background: #235937; border-color: #235937; color: #ffffff !important; text-decoration: none; font-size: 0.78rem; padding: 0.35rem 0.75rem;">人気ランキングを見る ↓</a>
        <a href="{lead['category']}/{lead['slug']}/index.html" class="login-link" style="color: var(--junior-dark-green); font-size: 0.82rem; font-weight: 700; text-decoration: underline;">最新トップ記事を読む →</a>
      </div>
    </div>
  </div>

  <main class="page-wrapper" style="margin-top: 2rem;">

    <!-- ==========================================================================
         HERO SECTION: 3-COLUMN BROADSHEET LAYOUT (10 TOP STORIES)
         ========================================================================== -->
    <div class="home-grid">
      
      <!-- LEFT COLUMN: 3 Stories -->
      <aside class="home-col-left">
        <div style="font-family: var(--font-headline); font-weight: 700; font-size: 0.9rem; border-bottom: 2px solid var(--times-black); padding-bottom: 0.3rem; margin-bottom: 1rem; color: #235937;">
          LATEST DISPATCHES • 注目の話題
        </div>

        <article class="left-story">
          <span class="badge-new green-fill">NEW • {left1['category'].upper()}</span>
          <h2 class="left-story-title">
            <a href="{left1['category']}/{left1['slug']}/index.html">{left1['title']}</a>
          </h2>
          <p class="left-story-snippet">
            <strong>{left1['headline_ja']}</strong><br>{left1['subhead']}
          </p>
          <div class="article-source-meta" style="margin-top: 0.4rem;">
            <a href="{left1['category']}/{left1['slug']}/index.html" style="font-weight: 700; color: #235937; text-decoration: underline; font-size: 0.82rem;">🌱 Junior版を読む →</a>
          </div>
        </article>

        <article class="left-story">
          <span class="badge-new green-fill">DISPATCH • {left2['category'].upper()}</span>
          <h2 class="left-story-title">
            <a href="{left2['category']}/{left2['slug']}/index.html">{left2['title']}</a>
          </h2>
          <p class="left-story-snippet">
            <strong>{left2['headline_ja']}</strong><br>{left2['subhead']}
          </p>
          <div class="article-source-meta" style="margin-top: 0.4rem;">
            <a href="{left2['category']}/{left2['slug']}/index.html" style="font-weight: 700; color: #235937; text-decoration: underline; font-size: 0.82rem;">🌱 Junior版を読む →</a>
          </div>
        </article>

        <article class="left-story">
          <span class="badge-new green-fill">DISPATCH • {left3['category'].upper()}</span>
          <h2 class="left-story-title">
            <a href="{left3['category']}/{left3['slug']}/index.html">{left3['title']}</a>
          </h2>
          <p class="left-story-snippet">
            <strong>{left3['headline_ja']}</strong><br>{left3['subhead']}
          </p>
          <div class="article-source-meta" style="margin-top: 0.4rem;">
            <a href="{left3['category']}/{left3['slug']}/index.html" style="font-weight: 700; color: #235937; text-decoration: underline; font-size: 0.82rem;">🌱 Junior版を読む →</a>
          </div>
        </article>
      </aside>

      <!-- CENTER COLUMN: TOP LEAD + 2 SUB-LEADS -->
      <section class="home-col-center">
        <article class="junior-hero-lead-box">
          <div class="lead-image-wrap">
            <img src="{lead['image']}" alt="{lead['title']}" class="lead-image" onerror="this.src='https://images.unsplash.com/photo-1508700115892-45ecd05ae2ad?w=1000&auto=format&fit=crop&q=80'">
          </div>

          <span class="category-tag green-fill" style="padding: 0.2rem 0.5rem;">
            TODAY'S FEATURED LEAD • {lead['category'].upper()}
          </span>
          <h1 class="lead-story-title" style="font-size: 2.1rem; margin-top: 0.5rem; line-height: 1.25;">
            <a href="{lead['category']}/{lead['slug']}/index.html" style="color: var(--times-black); text-decoration: none;">
              {lead['title']}
            </a>
          </h1>
          <p style="font-size: 1.05rem; font-weight: 700; color: #222; margin: 0.5rem 0;">
            {lead['headline_ja']}
          </p>
          <p class="lead-story-lead">
            {lead['lead_snippet']}
          </p>
          <div style="margin-top: 1rem; display: flex; gap: 1rem; align-items: center; flex-wrap: wrap;">
            <a href="{lead['category']}/{lead['slug']}/index.html" class="btn-trial" style="background: #235937; border-color: #235937; color: #ffffff !important; text-decoration: none; padding: 0.45rem 1.1rem; font-weight: 700; border-radius: 3px;">
              🌱 この記事をJunior版で読む（音声・クイズ付） →
            </a>
            <a href="../{lead['category']}/{lead['slug']}/index.html" style="font-size: 0.82rem; color: #555; text-decoration: underline;">
              🏛️ 発展・難関大版で比較する ↗
            </a>
          </div>
        </article>

        <!-- Sub-leads Grid (2 stories) -->
        <div class="sub-lead-grid">
          <div class="sub-lead-item">
            <div style="height: 120px; overflow: hidden; margin-bottom: 0.5rem; background: #e9ecef;">
              <img src="{sub1['image']}" alt="{sub1['title']}" style="width: 100%; height: 100%; object-fit: cover;" onerror="this.style.display='none'">
            </div>
            <span class="category-tag green-fill" style="padding: 0.15rem 0.4rem;">{sub1['category'].upper()}</span>
            <h3 class="sub-lead-title" style="margin-top: 0.35rem;">
              <a href="{sub1['category']}/{sub1['slug']}/index.html" style="color: var(--times-black); text-decoration: none;">{sub1['title']}</a>
            </h3>
            <p style="font-size: 0.85rem; font-weight: 700; color: #222; margin-top: 0.25rem;">{sub1['headline_ja']}</p>
            <p style="font-size: 0.8rem; color: var(--times-muted); margin-top: 0.25rem; line-height: 1.5;">
              {sub1['subhead']}
            </p>
          </div>

          <div class="sub-lead-item">
            <div style="height: 120px; overflow: hidden; margin-bottom: 0.5rem; background: #e9ecef;">
              <img src="{sub2['image']}" alt="{sub2['title']}" style="width: 100%; height: 100%; object-fit: cover;" onerror="this.style.display='none'">
            </div>
            <span class="category-tag green-fill" style="padding: 0.15rem 0.4rem;">{sub2['category'].upper()}</span>
            <h3 class="sub-lead-title" style="margin-top: 0.35rem;">
              <a href="{sub2['category']}/{sub2['slug']}/index.html" style="color: var(--times-black); text-decoration: none;">{sub2['title']}</a>
            </h3>
            <p style="font-size: 0.85rem; font-weight: 700; color: #222; margin-top: 0.25rem;">{sub2['headline_ja']}</p>
            <p style="font-size: 0.8rem; color: var(--times-muted); margin-top: 0.25rem; line-height: 1.5;">
              {sub2['subhead']}
            </p>
          </div>
        </div>
      </section>

      <!-- RIGHT COLUMN: 4 Curated Digest Stories with Thumbnails -->
      <aside class="home-col-right">
        <div style="background: #eef5f0; border-left: 3px solid #235937; padding: 0.75rem 1rem; margin-bottom: 1rem;">
          <div style="font-weight: 700; font-size: 0.82rem; color: #143820;">🌱 高校生ステップアップ学習</div>
          <div style="font-size: 0.75rem; color: #235937; margin-top: 0.2rem;">英検準2級〜2級の標準英文とゆっくり音声で読む厳選ダイジェスト</div>
        </div>

        <article class="right-story" style="display: flex; gap: 0.75rem; justify-content: space-between; border-bottom: 1px dotted #ccc; padding-bottom: 0.85rem; margin-bottom: 0.85rem;">
          <div class="right-story-body" style="flex: 1;">
            <span class="category-tag green-fill" style="padding: 0.1rem 0.35rem; font-size: 0.7rem;">{right1['category'].upper()}</span>
            <h3 class="right-story-title" style="font-size: 0.92rem; margin: 0.25rem 0;">
              <a href="{right1['category']}/{right1['slug']}/index.html" style="color: var(--times-black); text-decoration: none;">{right1['title']}</a>
            </h3>
            <p style="font-size: 0.76rem; color: var(--times-muted); line-height: 1.4; margin: 0;">
              {right1['headline_ja']}
            </p>
          </div>
          <div class="right-story-img" style="width: 70px; height: 70px; flex-shrink: 0; background: #e2e4e8; overflow: hidden; border-radius: 2px;">
            <img src="{right1['image']}" alt="{right1['title']}" style="width: 100%; height: 100%; object-fit: cover;" onerror="this.style.display='none'">
          </div>
        </article>

        <article class="right-story" style="display: flex; gap: 0.75rem; justify-content: space-between; border-bottom: 1px dotted #ccc; padding-bottom: 0.85rem; margin-bottom: 0.85rem;">
          <div class="right-story-body" style="flex: 1;">
            <span class="category-tag green-fill" style="padding: 0.1rem 0.35rem; font-size: 0.7rem;">{right2['category'].upper()}</span>
            <h3 class="right-story-title" style="font-size: 0.92rem; margin: 0.25rem 0;">
              <a href="{right2['category']}/{right2['slug']}/index.html" style="color: var(--times-black); text-decoration: none;">{right2['title']}</a>
            </h3>
            <p style="font-size: 0.76rem; color: var(--times-muted); line-height: 1.4; margin: 0;">
              {right2['headline_ja']}
            </p>
          </div>
          <div class="right-story-img" style="width: 70px; height: 70px; flex-shrink: 0; background: #e2e4e8; overflow: hidden; border-radius: 2px;">
            <img src="{right2['image']}" alt="{right2['title']}" style="width: 100%; height: 100%; object-fit: cover;" onerror="this.style.display='none'">
          </div>
        </article>

        <article class="right-story" style="display: flex; gap: 0.75rem; justify-content: space-between; border-bottom: 1px dotted #ccc; padding-bottom: 0.85rem; margin-bottom: 0.85rem;">
          <div class="right-story-body" style="flex: 1;">
            <span class="category-tag green-fill" style="padding: 0.1rem 0.35rem; font-size: 0.7rem;">{right3['category'].upper()}</span>
            <h3 class="right-story-title" style="font-size: 0.92rem; margin: 0.25rem 0;">
              <a href="{right3['category']}/{right3['slug']}/index.html" style="color: var(--times-black); text-decoration: none;">{right3['title']}</a>
            </h3>
            <p style="font-size: 0.76rem; color: var(--times-muted); line-height: 1.4; margin: 0;">
              {right3['headline_ja']}
            </p>
          </div>
          <div class="right-story-img" style="width: 70px; height: 70px; flex-shrink: 0; background: #e2e4e8; overflow: hidden; border-radius: 2px;">
            <img src="{right3['image']}" alt="{right3['title']}" style="width: 100%; height: 100%; object-fit: cover;" onerror="this.style.display='none'">
          </div>
        </article>

        <article class="right-story" style="display: flex; gap: 0.75rem; justify-content: space-between; border-bottom: 1px dotted #ccc; padding-bottom: 0.85rem; margin-bottom: 0.85rem;">
          <div class="right-story-body" style="flex: 1;">
            <span class="category-tag green-fill" style="padding: 0.1rem 0.35rem; font-size: 0.7rem;">{right4['category'].upper()}</span>
            <h3 class="right-story-title" style="font-size: 0.92rem; margin: 0.25rem 0;">
              <a href="{right4['category']}/{right4['slug']}/index.html" style="color: var(--times-black); text-decoration: none;">{right4['title']}</a>
            </h3>
            <p style="font-size: 0.76rem; color: var(--times-muted); line-height: 1.4; margin: 0;">
              {right4['headline_ja']}
            </p>
          </div>
          <div class="right-story-img" style="width: 70px; height: 70px; flex-shrink: 0; background: #e2e4e8; overflow: hidden; border-radius: 2px;">
            <img src="{right4['image']}" alt="{right4['title']}" style="width: 100%; height: 100%; object-fit: cover;" onerror="this.style.display='none'">
          </div>
        </article>

        <div style="background: #111; color: #fff; padding: 1rem; margin-top: 1rem; border-radius: 2px;">
          <div style="font-weight: 700; font-size: 0.85rem; color: #fff; margin-bottom: 0.35rem;">🏛️ 難関大・発展版へステップアップ</div>
          <p style="font-size: 0.75rem; color: #ccc; line-height: 1.5; margin-bottom: 0.75rem;">
            東大・京大・早慶レベルの英文解釈に挑戦するなら、本家THE ACADEMIC TIMESへ移動してください。
          </p>
          <a href="../index.html" style="display: inline-block; background: #fff; color: #111; padding: 0.3rem 0.7rem; font-weight: 700; font-size: 0.75rem; text-decoration: none; border-radius: 2px;">
            発展版トップページへ ↗
          </a>
        </div>
      </aside>

    </div>

    <!-- ==========================================================================
         SECTION 2: ACADEMIC CATEGORIES & EXAM GENRES (全5大学術・入試頻出分野)
         ========================================================================== -->
    <section class="study-section" style="margin-top: 3.5rem;">
      <div class="section-heading-bar">
        <h2 class="section-heading">ACADEMIC CATEGORIES & EXAM GENRES</h2>
        <span style="font-size: 0.8rem; color: var(--times-muted);">高校英語・英検準2級〜2級 5大出題分野</span>
      </div>

      <div class="category-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 1.25rem;">
        
        <!-- Category 1: Culture & Thought -->
        <div class="cat-card" id="cat-culture" style="border-top: 3px solid #235937;">
          <div class="cat-card-genre junior-genre">CULTURE & THOUGHT (文化・思想)</div>
          <h3 class="cat-card-title">
            <a href="culture/headphones-in-public/index.html">The Power of Quiet Moments: Why We Should Take Off Headphones</a>
          </h3>
          <p class="cat-card-lead">
            イヤホンを外すことの良さ。何気ない日常の習慣を見直し、創造性を育む思考法をやさしく読み解きます。
          </p>
        </div>

        <!-- Category 2: Science & Tech -->
        <div class="cat-card" id="cat-science" style="border-top: 3px solid #235937;">
          <div class="cat-card-genre junior-genre">SCIENCE & TECH (科学・医学)</div>
          <h3 class="cat-card-title">
            <a href="science/colorectal-cancer-under-50s/index.html">A Medical Mystery: Why Young People Are Getting Sick</a>
          </h3>
          <p class="cat-card-lead">
            若年層の病気の謎と超加工食品。最新の科学実験やデータから健康習慣を考える頻出テーマ。
          </p>
        </div>

        <!-- Category 3: Society & Mind -->
        <div class="cat-card" id="cat-society" style="border-top: 3px solid #235937;">
          <div class="cat-card-genre junior-genre">SOCIETY & MIND (社会・心理)</div>
          <h3 class="cat-card-title">
            <a href="society/psychology-casual-encounters/index.html">The Magic of a Simple Hello: Why Small Talks Bring Big Smiles</a>
          </h3>
          <p class="cat-card-lead">
            ちょっとした挨拶の魔法。知らない人との短い会話が私たちを幸せにする心理学の実験を学びます。
          </p>
        </div>

        <!-- Category 4: Law & Justice -->
        <div class="cat-card" id="cat-law" style="border-top: 3px solid #235937;">
          <div class="cat-card-genre junior-genre">LAW & JUSTICE (法・制度論)</div>
          <h3 class="cat-card-title">
            <a href="law/air-defence-shield/index.html">Protecting the Skies: UK Parliament Discusses Defence Plans</a>
          </h3>
          <p class="cat-card-lead">
            国の空を守る防衛計画と国民の税金。国会で予算を決める民主主義のルールを高校生向けに解説。
          </p>
        </div>

        <!-- Category 5: World & Security -->
        <div class="cat-card" id="cat-world" style="border-top: 3px solid #235937;">
          <div class="cat-card-genre junior-genre">WORLD & SECURITY (世界・安保)</div>
          <h3 class="cat-card-title">
            <a href="world/critical-minerals-geopolitics/index.html">The Race for Green Energy Minerals: How Countries Work Together</a>
          </h3>
          <p class="cat-card-lead">
            クリーンエネルギーに必要な鉱物の争奪戦。スマホやEVに欠かせない資源をめぐる国際協力を学びます。
          </p>
        </div>

      </div>
    </section>

    <!-- ==========================================================================
         SECTION 3: MOST READ RANKING (Top 5 Junior Articles)
         ========================================================================== -->
    <section class="study-section" id="ranking" style="margin-top: 3.5rem;">
      <div class="section-heading-bar">
        <h2 class="section-heading">MOST READ RANKING (デイリー人気記事 TOP 5)</h2>
        <span style="font-size: 0.8rem; color: var(--times-muted);">高校生・英語学習者が今一番読んでいる記事</span>
      </div>

      <div class="ranking-grid">
        
        <div class="ranking-card">
          <div class="ranking-num" style="color: #a3cdb2;">1</div>
          <div class="ranking-body">
            <span class="category-tag green-fill" style="padding: 0.1rem 0.35rem; font-size: 0.7rem;">CULTURE</span>
            <div class="ranking-title" style="margin-top: 0.25rem;">
              <a href="culture/headphones-in-public/index.html">The Power of Quiet Moments: Why We Should Sometimes Take Off Headphones</a>
            </div>
            <div style="font-size: 0.72rem; color: var(--times-muted); margin-top: 0.2rem;">閲覧数: 14,820 views • 英検準2級〜2級</div>
          </div>
        </div>

        <div class="ranking-card">
          <div class="ranking-num" style="color: #a3cdb2;">2</div>
          <div class="ranking-body">
            <span class="category-tag green-fill" style="padding: 0.1rem 0.35rem; font-size: 0.7rem;">SCIENCE</span>
            <div class="ranking-title" style="margin-top: 0.25rem;">
              <a href="science/colorectal-cancer-under-50s/index.html">A Medical Mystery: Why Young People Are Getting Sick</a>
            </div>
            <div style="font-size: 0.72rem; color: var(--times-muted); margin-top: 0.2rem;">閲覧数: 11,250 views • 英検準2級〜2級</div>
          </div>
        </div>

        <div class="ranking-card">
          <div class="ranking-num" style="color: #a3cdb2;">3</div>
          <div class="ranking-body">
            <span class="category-tag green-fill" style="padding: 0.1rem 0.35rem; font-size: 0.7rem;">LAW</span>
            <div class="ranking-title" style="margin-top: 0.25rem;">
              <a href="law/air-defence-shield/index.html">Protecting the Skies: UK Parliament Discusses New Defence Plans</a>
            </div>
            <div style="font-size: 0.72rem; color: var(--times-muted); margin-top: 0.2rem;">閲覧数: 9,840 views • 英検準2級〜2級</div>
          </div>
        </div>

        <div class="ranking-card">
          <div class="ranking-num" style="color: #a3cdb2;">4</div>
          <div class="ranking-body">
            <span class="category-tag green-fill" style="padding: 0.1rem 0.35rem; font-size: 0.7rem;">SOCIETY</span>
            <div class="ranking-title" style="margin-top: 0.25rem;">
              <a href="society/clarkson-business-red-tape/index.html">Farms and Rules: Why Starting a Business Is Hard in Britain</a>
            </div>
            <div style="font-size: 0.72rem; color: var(--times-muted); margin-top: 0.2rem;">閲覧数: 8,320 views • 英検準2級〜2級</div>
          </div>
        </div>

        <div class="ranking-card">
          <div class="ranking-num" style="color: #a3cdb2;">5</div>
          <div class="ranking-body">
            <span class="category-tag green-fill" style="padding: 0.1rem 0.35rem; font-size: 0.7rem;">WORLD</span>
            <div class="ranking-title" style="margin-top: 0.25rem;">
              <a href="world/raf-fairford-bomber-redeployment/index.html">Keeping the Skies Safe: Moving Military Aircraft in Europe</a>
            </div>
            <div style="font-size: 0.72rem; color: var(--times-muted); margin-top: 0.2rem;">閲覧数: 7,190 views • 英検準2級〜2級</div>
          </div>
        </div>

      </div>
    </section>

    <!-- ==========================================================================
         SECTION 4: BACK NUMBERS & INSTANT ARTICLE SEARCH (トップ記事一覧・バックナンバー一括検索)
         ========================================================================== -->
    <section class="study-section" id="section-archive" style="margin-top: 4rem;">
      <div class="section-heading-bar">
        <h2 class="section-heading">BACK NUMBERS & INSTANT SEARCH (トップ記事一覧・バックナンバー一括検索)</h2>
        <span style="font-size: 0.8rem; color: var(--times-muted);">全15記事のリアルタイム検索・分野別絞り込み</span>
      </div>
      <p style="font-size: 0.85rem; color: var(--times-muted); margin-bottom: 1.25rem; line-height: 1.6;">
        THE JUNIORに掲載されたすべての記事を、英単語・日本語キーワード・出題分野・ニュース元で瞬時に絞り込み検索できます。英検準2級〜2級の長文対策や高校の定期試験対策にご活用ください。
      </p>

      <!-- Daily Editions Quick Navigator -->
      <div style="background: #f8f9fa; border: 1px solid var(--times-light-border); padding: 1rem 1.25rem; margin-bottom: 1.5rem; display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 0.75rem;">
        <div style="font-weight: 700; font-size: 0.85rem; color: var(--times-black);">
          <span>📰 日別トップページ一覧（バックナンバー紙面）:</span>
        </div>
        <div style="display: flex; flex-wrap: wrap; gap: 0.4rem;">
          <a href="index.html#date-2026-10-09" style="padding: 0.35rem 0.75rem; border: 1px solid #235937; background: #235937; color: #fff; text-decoration: none; font-size: 0.78rem; font-weight: 700;" onclick="window.switchEdition('2026-10-09'); window.scrollTo({{top:0, behavior:'smooth'}}); return false;">10/9 (金) 本日最新号</a>
          <a href="index.html#date-2026-10-08" style="padding: 0.35rem 0.75rem; border: 1px solid var(--times-light-border); background: #fff; color: var(--times-black); text-decoration: none; font-size: 0.78rem; font-weight: 600;" onclick="window.switchEdition('2026-10-08'); window.scrollTo({{top:0, behavior:'smooth'}}); return false;">10/8 (木) 号</a>
          <a href="index.html#date-2026-10-07" style="padding: 0.35rem 0.75rem; border: 1px solid var(--times-light-border); background: #fff; color: var(--times-black); text-decoration: none; font-size: 0.78rem; font-weight: 600;" onclick="window.switchEdition('2026-10-07'); window.scrollTo({{top:0, behavior:'smooth'}}); return false;">10/7 (水) 号</a>
          <a href="index.html#date-2026-10-06" style="padding: 0.35rem 0.75rem; border: 1px solid var(--times-light-border); background: #fff; color: var(--times-black); text-decoration: none; font-size: 0.78rem; font-weight: 600;" onclick="window.switchEdition('2026-10-06'); window.scrollTo({{top:0, behavior:'smooth'}}); return false;">10/6 (火) 号</a>
          <a href="index.html#date-2026-10-05" style="padding: 0.35rem 0.75rem; border: 1px solid var(--times-light-border); background: #fff; color: var(--times-black); text-decoration: none; font-size: 0.78rem; font-weight: 600;" onclick="window.switchEdition('2026-10-05'); window.scrollTo({{top:0, behavior:'smooth'}}); return false;">10/5 (月) 号</a>
          <a href="index.html#date-2026-10-04" style="padding: 0.35rem 0.75rem; border: 1px solid var(--times-light-border); background: #fff; color: var(--times-black); text-decoration: none; font-size: 0.78rem; font-weight: 600;" onclick="window.switchEdition('2026-10-04'); window.scrollTo({{top:0, behavior:'smooth'}}); return false;">10/4 (日) 号</a>
          <a href="index.html#date-2026-10-03" style="padding: 0.35rem 0.75rem; border: 1px solid var(--times-light-border); background: #fff; color: var(--times-black); text-decoration: none; font-size: 0.78rem; font-weight: 600;" onclick="window.switchEdition('2026-10-03'); window.scrollTo({{top:0, behavior:'smooth'}}); return false;">10/3 (土) 号</a>
          <a href="index.html#date-2026-10-02" style="padding: 0.35rem 0.75rem; border: 1px solid var(--times-light-border); background: #fff; color: var(--times-black); text-decoration: none; font-size: 0.78rem; font-weight: 600;" onclick="window.switchEdition('2026-10-02'); window.scrollTo({{top:0, behavior:'smooth'}}); return false;">10/2 (金) 号</a>
          <a href="index.html#date-2026-10-01" style="padding: 0.35rem 0.75rem; border: 1px solid var(--times-light-border); background: #fff; color: var(--times-black); text-decoration: none; font-size: 0.78rem; font-weight: 600;" onclick="window.switchEdition('2026-10-01'); window.scrollTo({{top:0, behavior:'smooth'}}); return false;">10/1 (木) 創刊号</a>
        </div>
      </div>

      <div class="archive-search-box">
        <div class="archive-search-input-wrap">
          <span class="archive-search-icon">🔍</span>
          <input type="text" id="archive-search-input" class="archive-search-input" placeholder="タイトル、英単語（headphones, cancer, rules等）、日本語キーワードで検索...">
        </div>
        
        <div class="archive-filter-row">
          <div class="filter-category-group">
            <button type="button" class="filter-category-btn active" data-cat="all">全分野 (All)</button>
            <button type="button" class="filter-category-btn" data-cat="culture">Culture (文化・思想)</button>
            <button type="button" class="filter-category-btn" data-cat="law">Law (法律・制度)</button>
            <button type="button" class="filter-category-btn" data-cat="science">Science (科学・医学)</button>
            <button type="button" class="filter-category-btn" data-cat="society">Society (社会・経済)</button>
            <button type="button" class="filter-category-btn" data-cat="world">World (世界・安保)</button>
          </div>

          <div style="display: flex; align-items: center; gap: 0.75rem;">
            <select id="archive-source-select" class="archive-source-select" aria-label="Filter by Source Media">
              <option value="all">すべてのニュースソース (All Media)</option>
              <option value="time">TIME Magazine</option>
              <option value="the-times">The Times / Sunday Times</option>
              <option value="the-guardian">The Guardian</option>
              <option value="nature">Nature / Nature Medicine</option>
              <option value="reuters">Reuters / AP News</option>
              <option value="ft">Financial Times</option>
              <option value="science-mag">Science / MIT Tech Review</option>
              <option value="the-conversation">The Conversation / Atlantic</option>
            </select>
            <span id="archive-count-badge" class="archive-count-badge" style="color: #235937;">該当件数: {len(JUNIOR_ARTICLES)} 件</span>
          </div>
        </div>
      </div>

      <!-- Live Search Results Grid (Pre-rendered for immediate display & filtered live by JS) -->
      <div id="archive-results-grid" class="archive-results-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 1.25rem;">
        {cards_str}
      </div>
    </section>

    <!-- ==========================================================================
         SECTION 5: ESSENTIAL MEDIA & EIKEN STUDY GUIDE (高校生向け学習ガイド)
         ========================================================================== -->
    <section class="study-section" id="section-guide" style="margin-top: 4rem;">
      <div class="section-heading-bar">
        <h2 class="section-heading">ESSENTIAL MEDIA & EIKEN STUDY GUIDE (高校生のための英検・ニュース英語学習法)</h2>
        <span style="font-size: 0.8rem; color: var(--times-muted);">「やさしい英語」から「一生モノのアカデミック英語」へ</span>
      </div>
      <div style="background: #eef5f0; border-left: 3px solid #235937; padding: 1.25rem; margin-bottom: 1.5rem; font-size: 0.88rem; line-height: 1.7; color: var(--times-body);">
        <strong style="color: #143820;">🌱 THE JUNIORで伸ばす3大英語力：</strong><br>
        1. <strong>リスニング力：</strong> イギリス公共放送アナウンサー基準の品格ある英語音声（標準135wpm）で、共通テスト・英検の聴き取りを強化。<br>
        2. <strong>読解の骨組み（パラグラフ・リーディング）：</strong> 身近な疑問から社会の課題へ広がる英文の展開パターンを体得。<br>
        3. <strong>発展版への跳躍力：</strong> 同じニュースを扱った本家『THE ACADEMIC TIMES』と見比べることで、難関大入試の最難関構文へ無理なくステップアップ。
      </div>

      <!-- Media Resources Grid -->
      <div id="media-resources-grid" class="media-resources-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 1.25rem;">
        {media_cards_str}
      </div>
    </section>

  </main>

  <!-- The Times UK Style Footer (Junior Edition) -->
  <footer class="times-footer" style="margin-top: 4rem;">
    <div class="footer-container">
      <div class="footer-top">
        <a href="index.html" class="footer-logo">THE JUNIOR</a>
        <div style="font-size: 0.8125rem; color: #888;">
          The Stepping Stone to World News • Eiken Grade Pre-2 & Grade 2 Broadsheet
        </div>
      </div>
      <div class="footer-grid">
        <div class="footer-col">
          <h4>About The Junior</h4>
          <p style="font-size: 0.8125rem; line-height: 1.7; color: #999;">
            高校1〜2年生・英検準2級〜2級の標準的な語彙と文法で、世界の最新ニュースを深く読み解くニュースポータルです。
          </p>
        </div>
        <div class="footer-col">
          <h4>Junior Categories</h4>
          <ul class="footer-links">
            <li><a href="#cat-society">/society/ — 社会・教育・心理</a></li>
            <li><a href="#cat-science">/science/ — 科学・医学・環境</a></li>
            <li><a href="#cat-culture">/culture/ — 文化・思想・習慣</a></li>
            <li><a href="#cat-law">/law/ — 法律・制度・ルール</a></li>
            <li><a href="#cat-world">/world/ — 国際情勢・安全保障</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Learning Architecture</h4>
          <ul class="footer-links">
            <li><a href="#section-guide">Edge-TTS Slow Voice (-10%)</a></li>
            <li><a href="#section-guide">Keita & Nanami Dialogue</a></li>
            <li><a href="#section-archive">Eiken Pre-2 ~ 2 Quizzes</a></li>
            <li><a href="../index.html">Step-Up to Academic Times</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Sibling Portal</h4>
          <ul class="footer-links">
            <li><a href="../index.html">THE ACADEMIC TIMES (発展版) ↗</a></li>
            <li><a href="../society/index.html">Senior Society Portal ↗</a></li>
            <li><a href="../science/index.html">Senior Science Portal ↗</a></li>
            <li><a href="../culture/index.html">Senior Culture Portal ↗</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <div>© 2026 THE JUNIOR ACADEMIC TIMES. All rights reserved. Sibling Portal to The Academic Times.</div>
        <div>
          <a href="../index.html" style="color: #bbb; margin-right: 1rem; text-decoration: underline;">発展・難関大版へ ↗</a>
          <a href="#junior-top" style="color: #888; text-decoration: underline;">Top of Page ↑</a>
        </div>
      </div>
    </div>
  </footer>

  <!-- Scripts -->
  <script src="js/junior-data.js"></script>
  <script src="js/junior-home.js"></script>
  <script src="../js/app.js"></script>
</body>
</html>
"""
    with open(JUNIOR_INDEX_PATH, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"[OK] Generated {JUNIOR_INDEX_PATH}")

if __name__ == "__main__":
    generate_junior_index()
