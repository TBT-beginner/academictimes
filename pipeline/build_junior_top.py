# -*- coding: utf-8 -*-
"""
Generates news_portal/junior/index.html
The broadsheet top page for THE JUNIOR (Eiken Pre-2 ~ 2 Edition).
"""

import os
from junior_articles_data import JUNIOR_ARTICLES

PORTAL_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
JUNIOR_INDEX_PATH = os.path.join(PORTAL_DIR, "junior", "index.html")

def generate_junior_index():
    lead = JUNIOR_ARTICLES[0]   # headphones-in-public
    sub1 = JUNIOR_ARTICLES[1]   # colorectal cancer
    sub2 = JUNIOR_ARTICLES[2]   # casual encounters
    left1 = JUNIOR_ARTICLES[3]  # air defence
    left2 = JUNIOR_ARTICLES[4]  # critical minerals

    # Generate article cards for directory
    cards_html = []
    for art in JUNIOR_ARTICLES:
        card = f"""
        <div class="junior-catalog-card" style="border: 1px solid var(--times-light-border); padding: 1.25rem; background: #fff; margin-bottom: 1.25rem; display: flex; flex-direction: column; justify-content: space-between;">
          <div>
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
              <span class="category-tag" style="background: #235937; color: #fff; padding: 0.15rem 0.45rem;">{art['category'].upper()}</span>
              <span style="font-size: 0.75rem; color: var(--times-muted); font-weight: 700;">英検準2級〜2級</span>
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
          <div style="margin-top: 1rem; padding-top: 0.75rem; border-top: 1px dashed #e0e0e0; display: flex; justify-content: space-between; align-items: center;">
            <a href="{art['category']}/{art['slug']}/index.html" style="color: #235937; font-weight: 700; font-size: 0.82rem; text-decoration: underline;">
              🌱 Junior版を読む（音声付） →
            </a>
            <a href="{art['original_article_url']}" style="color: #111; font-size: 0.78rem; text-decoration: none;">
              🏛️ 発展版（難関大） ↗
            </a>
          </div>
        </div>
        """
        cards_html.append(card)
    cards_str = "\n".join(cards_html)

    html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>THE JUNIOR | The Stepping Stone to World News</title>
  <link rel="stylesheet" href="../styles/times.css">
  <link rel="stylesheet" href="styles/times-junior.css">
  <style>
    .junior-hero-lead-box {{
      border-bottom: 1px solid var(--times-light-border);
      padding-bottom: 1.5rem;
      margin-bottom: 1.5rem;
    }}
  </style>
</head>
<body class="times-theme">

  <!-- Top Switcher Bar -->
  <div class="edition-switcher-bar-junior">
    <div>
      <span class="level-badge-pre2">THE JUNIOR</span>
      <span style="font-weight: 600; color: #111;">高校1〜2年・英検準2級〜2級向けステップアップ紙面</span>
    </div>
    <div>
      <a href="../index.html" class="btn-switch-to-senior" title="難関国公立・早慶・英検準1〜1級レベルへ">
        🏛️ THE ACADEMIC TIMES（発展・難関大版）へ移動 ↗
      </a>
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
        <li class="nav-item"><a href="#articles-catalog">All Articles (全5分野)</a></li>
        <li class="nav-item"><a href="#how-to-study">学習の進め方</a></li>
        <li class="nav-item" style="margin-left: auto;">
          <a href="../index.html" style="color: var(--times-red); font-weight: 700;">発展・難関大版へ戻る ↗</a>
        </li>
      </ul>
    </div>
  </nav>

  <!-- Level Concept Sub-Banner -->
  <div style="background: #eaf3ed; border-bottom: 2px solid #235937; padding: 1.25rem 1rem;">
    <div class="page-wrapper" style="padding-top: 0; padding-bottom: 0; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem;">
      <div>
        <div style="font-family: var(--font-headline); font-size: 1.25rem; font-weight: 700; color: #1b4d2e;">
          🌱 世界の本格ニュースを、無理なく読める高校生標準英語で。
        </div>
        <div style="font-size: 0.85rem; color: #2e593d; margin-top: 0.35rem; line-height: 1.6;">
          『THE JUNIOR』は、本家THE ACADEMIC TIMESと同じ本格的なテーマ（認知心理学、先端医療、安保、国際通商など）を、<strong>英検準2級〜2級（CEFR A2〜B1）</strong>の標準的な語彙と構文、ゆっくり聴き取りやすい朗読音声（約135 wpm）で楽しむための特別エディションです。
        </div>
      </div>
      <div>
        <a href="#articles-catalog" class="btn-trial" style="background: #235937; border-color: #235937; text-decoration: none;">
          記事一覧を見る ↓
        </a>
      </div>
    </div>
  </div>

  <main class="page-wrapper" style="margin-top: 2rem;">

    <!-- 3-COLUMN BROADSHEET LAYOUT -->
    <div class="home-grid">
      
      <!-- LEFT COLUMN -->
      <aside class="home-col-left">
        <div style="font-family: var(--font-headline); font-weight: 700; font-size: 0.9rem; border-bottom: 2px solid var(--times-black); padding-bottom: 0.3rem; margin-bottom: 1rem; color: #235937;">
          LATEST DISPATCHES • 注目の話題
        </div>

        <article class="left-story">
          <span class="badge-new" style="background: #235937;">LAW & SOCIETY</span>
          <h2 class="left-story-title">
            <a href="{left1['category']}/{left1['slug']}/index.html">{left1['title']}</a>
          </h2>
          <p class="left-story-snippet">{left1['headline_ja']}。{left1['subhead']}</p>
          <div class="article-source-meta">
            <a href="{left1['category']}/{left1['slug']}/index.html" style="font-weight: 700; color: #235937;">Junior版を読む →</a>
          </div>
        </article>

        <article class="left-story">
          <span class="badge-new" style="background: #235937;">WORLD & FUTURE</span>
          <h2 class="left-story-title">
            <a href="{left2['category']}/{left2['slug']}/index.html">{left2['title']}</a>
          </h2>
          <p class="left-story-snippet">{left2['headline_ja']}。{left2['subhead']}</p>
          <div class="article-source-meta">
            <a href="{left2['category']}/{left2['slug']}/index.html" style="font-weight: 700; color: #235937;">Junior版を読む →</a>
          </div>
        </article>
      </aside>

      <!-- CENTER COLUMN: TOP LEAD STORY -->
      <section class="home-col-center">
        <article class="junior-hero-lead-box">
          <div class="lead-image-wrap">
            <img src="{lead['image']}" alt="{lead['title']}" class="lead-image">
          </div>

          <span class="category-tag" style="background: #235937; color: #fff; padding: 0.2rem 0.5rem;">
            TODAY'S FEATURED LEAD • {lead['category'].upper()}
          </span>
          <h1 class="lead-story-title" style="font-size: 2.1rem; margin-top: 0.5rem;">
            <a href="{lead['category']}/{lead['slug']}/index.html">
              {lead['title']}
            </a>
          </h1>
          <p style="font-size: 1.1rem; font-weight: 700; color: #222; margin: 0.5rem 0;">
            {lead['headline_ja']}
          </p>
          <p class="lead-story-lead">
            {lead['lead_snippet']}
          </p>
          <div style="margin-top: 1rem; display: flex; gap: 1rem; align-items: center;">
            <a href="{lead['category']}/{lead['slug']}/index.html" class="btn-trial" style="background: #235937; border-color: #235937; text-decoration: none; padding: 0.4rem 1rem;">
              この記事をJunior版で読む（音声・クイズ付） →
            </a>
            <a href="{lead['original_article_url']}" style="font-size: 0.8rem; color: #555; text-decoration: underline;">
              発展・難関大版で比較する ↗
            </a>
          </div>
        </article>

        <!-- Sub-leads Grid -->
        <div class="sub-lead-grid">
          <div class="sub-lead-item">
            <span class="category-tag" style="background: #235937; color: #fff; padding: 0.15rem 0.4rem;">{sub1['category'].upper()}</span>
            <h3 class="sub-lead-title">
              <a href="{sub1['category']}/{sub1['slug']}/index.html">{sub1['title']}</a>
            </h3>
            <p style="font-size: 0.85rem; font-weight: 700; color: #222; margin-top: 0.25rem;">{sub1['headline_ja']}</p>
            <p style="font-size: 0.8rem; color: var(--times-muted); margin-top: 0.25rem;">
              {sub1['subhead']}
            </p>
          </div>

          <div class="sub-lead-item">
            <span class="category-tag" style="background: #235937; color: #fff; padding: 0.15rem 0.4rem;">{sub2['category'].upper()}</span>
            <h3 class="sub-lead-title">
              <a href="{sub2['category']}/{sub2['slug']}/index.html">{sub2['title']}</a>
            </h3>
            <p style="font-size: 0.85rem; font-weight: 700; color: #222; margin-top: 0.25rem;">{sub2['headline_ja']}</p>
            <p style="font-size: 0.8rem; color: var(--times-muted); margin-top: 0.25rem;">
              {sub2['subhead']}
            </p>
          </div>
        </div>
      </section>

      <!-- RIGHT COLUMN: STEP-UP GUIDE -->
      <aside class="home-col-right">
        <div style="background: #fdfdfd; border: 1px solid var(--times-light-border); padding: 1.25rem; margin-bottom: 1.5rem;">
          <h3 style="font-family: var(--font-headline); font-size: 1rem; color: #235937; margin-bottom: 0.5rem;">
            🎯 Junior版の3大ステップ学習
          </h3>
          <ol style="font-size: 0.82rem; line-height: 1.7; padding-left: 1.25rem; color: var(--times-body);">
            <li><strong>まずは音読：</strong> 落ち着いた標準速度（-10%）のイギリス英語音声に合わせて声に出して読んでみる。</li>
            <li><strong>Keita & Nanami解説：</strong> 日常会話風の掛け合いで記事の面白さと文法のツボを理解する。</li>
            <li><strong>クイズ＆発展版へ挑戦：</strong> 3問のクイズで腕試しをして、自信がついたら『発展・難関大版』にステップアップ！</li>
          </ol>
        </div>

        <div style="background: #111; color: #fff; padding: 1.25rem;">
          <h4 style="font-family: var(--font-headline); font-size: 1rem; margin-bottom: 0.5rem; color: #fff;">
            🏛️ THE ACADEMIC TIMES（発展版）
          </h4>
          <p style="font-size: 0.78rem; color: #bbb; line-height: 1.6; margin-bottom: 1rem;">
            東大・京大・早慶などの二次試験や英検準1級〜1級を目指すなら、本家サイトの格調高い文体に挑戦してください。
          </p>
          <a href="../index.html" style="display: inline-block; background: #fff; color: #111; padding: 0.35rem 0.8rem; font-weight: 700; font-size: 0.78rem; text-decoration: none;">
            発展版トップページへ ↗
          </a>
        </div>
      </aside>

    </div>

    <!-- ALL ARTICLES CATALOGUE -->
    <section class="study-section" id="articles-catalog" style="margin-top: 4rem;">
      <div class="section-heading-bar">
        <h2 class="section-heading">ALL JUNIOR ARTICLES (全5分野の掲載記事)</h2>
        <span style="font-size: 0.8rem; color: var(--times-muted);">英検準2級〜2級で読める厳選アカデミック・ニュース</span>
      </div>
      <p style="font-size: 0.85rem; color: var(--times-muted); margin-bottom: 1.5rem;">
        文化、科学、社会、法制度、国際関係の全5分野から、高校生が今知るべき最先端ニュースを厳選しています。各記事から発展・難関大版へのワンクリック比較も可能です。
      </p>

      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 1.25rem;">
        {cards_str}
      </div>
    </section>

  </main>

  <!-- The Times UK Style Footer -->
  <footer class="times-footer" style="margin-top: 4rem;">
    <div class="footer-container">
      <div class="footer-top">
        <a href="index.html" class="footer-logo">THE JUNIOR</a>
        <div style="font-size: 0.8125rem; color: #888;">
          The Stepping Stone to World News • Eiken Grade Pre-2 & Grade 2 Broadsheet
        </div>
      </div>
      <div class="footer-bottom">
        <div>© 2026 THE JUNIOR ACADEMIC TIMES. Sibling Site to The Academic Times.</div>
        <div>
          <a href="../index.html" style="color: #bbb; margin-right: 1rem; text-decoration: underline;">発展・難関大版へ ↗</a>
          <a href="#" style="color: #888; text-decoration: underline;">Top of Page ↑</a>
        </div>
      </div>
    </div>
  </footer>

</body>
</html>
"""
    with open(JUNIOR_INDEX_PATH, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"[OK] Generated {JUNIOR_INDEX_PATH}")

if __name__ == "__main__":
    generate_junior_index()
