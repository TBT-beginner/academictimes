# -*- coding: utf-8 -*-
"""
Builds THE JUNIOR website:
1. Synthesizes Edge-TTS audio (British Ryan at -10% rate for clear listening + Keita/Nanami dialogues).
2. Generates article HTMLs in junior/{category}/{slug}/index.html.
3. Generates junior/index.html (Broadsheet landing page) and junior/js/junior-data.js.
"""

import os
import sys
import asyncio
import edge_tts
from junior_articles_data import JUNIOR_ARTICLES

VOICE_BRITISH = "en-GB-RyanNeural"
VOICE_KEITA = "ja-JP-KeitaNeural"
VOICE_NANAMI = "ja-JP-NanamiNeural"

PORTAL_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
JUNIOR_DIR = os.path.join(PORTAL_DIR, "junior")

async def synth_audio(text, voice, out_path, sem, rate="+0%"):
    async with sem:
        for attempt in range(3):
            try:
                comm = edge_tts.Communicate(text, voice, rate=rate)
                await comm.save(out_path)
                return
            except Exception as e:
                if attempt == 2:
                    print(f"[ERR] Failed {out_path}: {e}")
                else:
                    await asyncio.sleep(1)

def build_junior_article_html(art):
    cat = art["category"]
    slug = art["slug"]
    title = art["title"]
    headline_ja = art["headline_ja"]
    subhead = art["subhead"]
    lead = art["lead_snippet"]
    source_name = art["source_name"]
    source_url = art["source_url"]
    source_attr = art["source_attribution"]
    guide = art["source_student_guide"]
    orig_url = art["original_article_url"]
    image = art["image"]
    
    # Sentences
    s1_en, s1_ja = art["sentences"][0]["en"], art["sentences"][0]["ja"]
    s2_en, s2_ja = art["sentences"][1]["en"], art["sentences"][1]["ja"]
    s3_en, s3_ja = art["sentences"][2]["en"], art["sentences"][2]["ja"]
    s4_en, s4_ja = art["sentences"][3]["en"], art["sentences"][3]["ja"]
    s5_en, s5_ja = art["sentences"][4]["en"], art["sentences"][4]["ja"]

    # Dialogue HTML
    dlg_blocks = []
    for i, d in enumerate(art["dialogue"]):
        is_teacher = ("Keita" in d["name"] or d.get("role", "") == "英語講師" or d.get("speaker", "") == "慶")
        turn_cls = "turn-teacher" if is_teacher else "turn-assistant"
        avatar_cls = "avatar-teacher" if is_teacher else "avatar-assistant"
        avatar_char = "慶" if is_teacher else "七"
        turn_id = f"dlg-{i+1}"
        audio_file = f"audio/dlg_{i+1:02d}.mp3"
        d_html = f"""
        <div class="dlg-turn {turn_cls}" id="{turn_id}">
          <div class="dlg-avatar {avatar_cls}">{avatar_char}</div>
          <div class="dlg-content">
            <div class="dlg-meta">
              <span class="dlg-name">{d['name']}</span>
              <span class="dlg-role">{d['role']}</span>
            </div>
            <div class="dlg-bubble">
              <p>{d['text']}</p>
              <button type="button" class="dlg-play-btn" data-dlg-audio="{audio_file}" aria-label="Play dialogue turn {i+1}">
                <span class="audio-state-icon">▶</span>
              </button>
            </div>
          </div>
        </div>
        """
        dlg_blocks.append(d_html)
    dlg_html = "\n".join(dlg_blocks)

    # Vocab Rows HTML
    vocab_rows = []
    for v in art["vocab"]:
        row = f"""
        <tr>
          <td>
            <div class="vocab-word">{v['word']}</div>
            <div class="vocab-phonetic">{v['phonetic']}</div>
          </td>
          <td>
            <span class="vocab-pos">{v['pos']}</span>
            <div class="vocab-meaning">{v['meaning']}</div>
          </td>
          <td>
            <div class="vocab-def-en">{v['def']}</div>
            <div class="vocab-example">{v['ex']}</div>
          </td>
        </tr>
        """
        vocab_rows.append(row)
    vocab_html = "\n".join(vocab_rows)

    # Syntax Cards HTML
    syntax_cards = []
    for s in art["syntax"]:
        card = f"""
        <div class="grammar-card">
          <div class="grammar-card-head">
            <span class="grammar-target-phrase">{s['phrase']}</span>
            <span class="grammar-meaning">【{s['meaning']}】</span>
          </div>
          <div class="grammar-card-body">
            <p>{s['explanation']}</p>
          </div>
        </div>
        """
        syntax_cards.append(card)
    syntax_html = "\n".join(syntax_cards)

    # Quiz Cards HTML
    quiz_cards = []
    for i, q in enumerate(art["quiz"]):
        opt_letters = ["A", "B", "C", "D"]
        opt_btns = []
        for j, opt in enumerate(q["options"]):
            is_correct = "true" if j == q["correct_index"] else "false"
            btn = f"""
            <button type="button" class="quiz-btn" data-correct="{is_correct}">
              <span class="quiz-opt-letter">{opt_letters[j]}</span>
              <span>{opt}</span>
            </button>
            """
            opt_btns.append(btn)
        opts_html = "\n".join(opt_btns)
        
        q_card = f"""
        <div class="quiz-card" style="margin-bottom: 2rem; border: 1px solid var(--times-light-border); padding: 1.25rem;">
          <div class="quiz-card-header">
            <span class="quiz-num-badge">QUESTION {i+1}</span>
            <span style="font-size: 0.8rem; color: var(--times-muted);">英検準2級〜2級形式</span>
          </div>
          <p class="quiz-question-text" style="font-weight: 700; margin: 0.75rem 0 1rem; font-size: 1rem;">
            {q['question']}
          </p>
          <div class="quiz-choices">
            {opts_html}
          </div>
          <div class="quiz-explanation" style="margin-top: 1rem; padding: 0.75rem 1rem; background: #f8f9fa; border-left: 3px solid var(--junior-green); display: none;">
            {q['explanation']}
          </div>
        </div>
        """
        quiz_cards.append(q_card)
    quiz_html = "\n".join(quiz_cards)

    html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | THE JUNIOR</title>
  <link rel="stylesheet" href="../../styles/times-junior.css">
  <style>
    .junior-level-banner {{
      background: #eaf3ed;
      border: 1px solid #c8e0d1;
      padding: 0.75rem 1.25rem;
      margin-bottom: 1.5rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 0.75rem;
    }}
    .junior-level-badge {{
      background: #235937;
      color: #fff;
      font-size: 0.75rem;
      font-weight: 700;
      padding: 0.25rem 0.6rem;
      border-radius: 2px;
      letter-spacing: 0.05em;
    }}
  </style>
</head>
<body class="times-theme" id="article-top">

  <!-- Top Switcher Bar -->
  <div class="edition-switcher-bar-junior">
    <div>
      <span class="level-badge-pre2">THE JUNIOR</span>
      <span style="font-weight: 600; color: #111;">英検準2級〜2級（高校1〜2年・基礎〜標準）</span>
    </div>
    <div>
      <a href="{orig_url}" class="btn-switch-to-senior" title="同じテーマの発展・難関大版へジャンプ">
        🏛️ THE ACADEMIC TIMES（発展・難関大版）で読む ↗
      </a>
    </div>
  </div>

  <!-- The Times Masthead -->
  <header class="masthead-junior">
    <a href="../../index.html" class="masthead-link" style="text-decoration: none;">
      <h1 class="masthead-junior-title">THE JUNIOR</h1>
    </a>
    <div class="masthead-junior-tagline">The Stepping Stone to World News • English for High School Students</div>
    <div class="masthead-junior-sub">英検準2級〜2級レベルで世界の一流ニュースの核心を読む</div>
  </header>

  <!-- Navigation Bar -->
  <nav class="nav-bar">
    <div class="nav-container">
      <ul class="nav-list">
        <li class="nav-item active"><a href="../../index.html">Junior Home</a></li>
        <li class="nav-item"><a href="#section-article">Article & Audio</a></li>
        <li class="nav-item"><a href="#section-discussion">Discussion (解説)</a></li>
        <li class="nav-item"><a href="#section-vocabulary">Vocabulary</a></li>
        <li class="nav-item"><a href="#section-syntax">Syntax</a></li>
        <li class="nav-item"><a href="#section-quiz">Quiz (全3問)</a></li>
        <li class="nav-item" style="margin-left: auto;">
          <a href="{orig_url}" style="color: var(--times-red); font-weight: 700;">発展版へ移動 ↗</a>
        </li>
      </ul>
    </div>
  </nav>

  <main class="page-wrapper">
    <article class="article-container">

      <!-- Level & Step-Up Banner -->
      <div class="junior-level-banner">
        <div>
          <span class="junior-level-badge">LEVEL: 英検準2級〜2級</span>
          <span style="font-size: 0.85rem; color: #235937; font-weight: 600; margin-left: 0.5rem;">
            🌱 わかりやすい構文と落ち着いた朗読音声（聞き取りやすい標準スピード）
          </span>
        </div>
        <div>
          <a href="{orig_url}" style="font-size: 0.82rem; color: #111; text-decoration: underline; font-weight: 700;">
            難関大・英検準1級〜1級の表現で読む →
          </a>
        </div>
      </div>

      <!-- HERO HEADLINE -->
      <header class="hero-header" style="min-height: auto; padding: 1.5rem 0;">
        <span class="category-tag" style="background: #235937; color: #fff; padding: 0.2rem 0.5rem;">
          {art['category_label']}
        </span>
        <h1 class="hero-title" style="font-size: 2.2rem; margin: 0.75rem 0;">{title}</h1>
        <p class="hero-headline-ja" style="font-size: 1.15rem; font-weight: 700; color: #222;">{headline_ja}</p>
        <p class="hero-subhead" style="font-size: 0.95rem; color: var(--times-muted); margin-top: 0.5rem; line-height: 1.6;">
          {subhead}
        </p>

        <!-- Source Accordion -->
        <details class="source-accordion" style="margin-top: 1rem;">
          <summary class="source-accordion-summary">
            📰 ニュースソースについて（出典: {source_name}）
          </summary>
          <div class="source-accordion-body">
            {source_attr}<br>
            <div style="font-size: 0.82rem; line-height: 1.6; margin-top: 0.5rem; color: #444;">
              <strong>🎓 高校生向け学習のヒント：</strong> {guide}
            </div>
          </div>
        </details>
      </header>

      <!-- ARTICLE BODY -->
      <section id="section-article">
        <div class="article-headline-block" id="article-headline-block">
          <span class="category-tag">ENGLISH READING • ゆっくり朗読 (約135 wpm)</span>
          <div style="font-family: var(--font-headline); font-size: 1.4rem; font-weight: 700; margin-top: 0.4rem;">
            {title}
          </div>

          <!-- Audio Menu -->
          <div class="audio-inline-bar" id="full-body-banner">
            <div class="speed-control-group">
              <span class="speed-control-label">SPEED</span>
              <button type="button" class="btn-speed-opt" data-speed="0.8">0.8x</button>
              <button type="button" class="btn-speed-opt active-speed" data-speed="1.0">1.0x</button>
              <button type="button" class="btn-speed-opt" data-speed="1.2">1.2x</button>
            </div>

            <button type="button" class="btn-audio-circle" id="btn-play-continuous" title="朗読＋解説を再生">
              <span class="audio-state-icon">▶</span>
            </button>

            <button type="button" class="btn-flag-toggle" id="btn-toggle-ja" title="日本語全訳の表示/非表示">
              <span>🇯🇵</span>
            </button>
            <span class="inline-reading-hint">※文クリックで個別再生・🇯🇵で日本語訳表示</span>
          </div>
        </div>

        <!-- Broadsheet Body -->
        <div class="article-real-body" style="font-size: 1.15rem; line-height: 1.85;">
          <p class="real-para lead-para">
            <span class="article-sentence" data-sentence-audio="audio/s1.mp3">{s1_en}</span>
            <span class="article-sentence" data-sentence-audio="audio/s2.mp3">{s2_en}</span>
          </p>
          <p class="real-para">
            <span class="article-sentence" data-sentence-audio="audio/s3.mp3">{s3_en}</span>
            <span class="article-sentence" data-sentence-audio="audio/s4.mp3">{s4_en}</span>
            <span class="article-sentence" data-sentence-audio="audio/s5.mp3">{s5_en}</span>
          </p>
        </div>

        <!-- Hidden Translation -->
        <div class="ja-translation article-real-translation" id="ja-article-translation">
          <div style="font-size: 0.75rem; font-weight: 700; color: var(--times-muted); margin-bottom: 0.5rem;">【日本語全訳】</div>
          <p class="real-para">{s1_ja} {s2_ja}</p>
          <p class="real-para">{s3_ja} {s4_ja} {s5_ja}</p>
        </div>
      </section>

      <!-- DISCUSSION -->
      <section class="dialogue-wrapper" id="section-discussion" style="margin-top: 3rem;">
        <div class="dialogue-head">
          <div class="dialogue-title-area">
            <span class="dialogue-badge" style="background: #235937;">TALK & DISCUSS</span>
            <h2 class="dialogue-main-heading">Keita先生とNanamiさんのニュース深掘りトーク（Junior版）</h2>
          </div>
          <div>
            <button type="button" class="btn-audio-play" id="btn-play-dialogue-all" style="font-size: 0.75rem; padding: 0.35rem 0.8rem; background: transparent; border: 1px solid #111; color: #111;">
              <span class="audio-state-icon">▶</span>
              <span>解説トークを通しで聴く</span>
            </button>
          </div>
        </div>
        <p class="dialogue-lead">
          「ニュースの面白さを知りたい！」「英検準2級〜2級で狙われるポイントを学びたい！」という高校生のために、Keita先生とNanamiさんがわかりやすく解説します。
        </p>

        {dlg_html}
      </section>

      <!-- VOCABULARY -->
      <section class="study-section" id="section-vocabulary" style="margin-top: 3rem;">
        <h2 class="study-section-title">
          <span class="marker">■</span> 英検準2級〜2級 重要語彙（Vocabulary Drill）
        </h2>
        <table class="vocab-table">
          <thead>
            <tr>
              <th style="width: 25%;">語句・発音</th>
              <th style="width: 30%;">意味・品詞</th>
              <th style="width: 45%;">定義 & 例文</th>
            </tr>
          </thead>
          <tbody>
            {vocab_html}
          </tbody>
        </table>
      </section>

      <!-- SYNTAX -->
      <section class="study-section" id="section-syntax" style="margin-top: 3rem;">
        <h2 class="study-section-title">
          <span class="marker">■</span> 必須基本構文（Syntax & Grammar）
        </h2>
        {syntax_html}
      </section>

      <!-- QUIZ -->
      <section class="study-section" id="section-quiz" style="margin-top: 3rem;">
        <h2 class="study-section-title">
          <span class="marker">■</span> 確認クイズ（Interactive Quiz • 全3問）
        </h2>
        <p style="font-size: 0.875rem; color: var(--times-muted); margin-bottom: 1.5rem;">
          英検準2級・2級の長文読解形式に準拠した3問です。選択肢をクリックすると即座に正誤判定と解説が表示されます。
        </p>
        {quiz_html}
      </section>

      <!-- STEP UP BANNER -->
      <div style="background: #f8f9fa; border: 2px solid var(--times-black); padding: 1.5rem; margin-top: 3rem; text-align: center;">
        <h3 style="font-family: var(--font-headline); font-size: 1.3rem; margin-bottom: 0.5rem;">
          🌟 もっとハイレベルな英語に挑戦してみよう！
        </h3>
        <p style="font-size: 0.88rem; color: var(--times-muted); margin-bottom: 1rem; line-height: 1.6;">
          この記事の内容が理解できたら、英検準1級〜1級・難関大レベルの『発展版』元記事を読んでみましょう。<br>
          同じテーマがより格調高い英国高級紙の文体で書かれており、英語長文の読解力が飛躍的に向上します。
        </p>
        <a href="{orig_url}" class="btn-trial" style="background: #111; color: #fff; text-decoration: none; padding: 0.5rem 1.25rem; font-weight: 700; font-size: 0.85rem;">
          🏛️ THE ACADEMIC TIMES（発展・難関大版）を開く →
        </a>
      </div>

    </article>
  </main>

  <footer class="times-footer" style="margin-top: 4rem;">
    <div class="footer-container">
      <div class="footer-top">
        <a href="../../index.html" class="footer-logo">THE JUNIOR</a>
        <div style="font-size: 0.8125rem; color: #888;">
          The Stepping Stone to World News • Eiken Grade Pre-2 & Grade 2 Broadsheet
        </div>
      </div>
      <div class="footer-bottom">
        <div>© 2026 THE JUNIOR ACADEMIC TIMES. All rights reserved.</div>
        <div><a href="#article-top" style="color: #888; text-decoration: underline;">Back to Top ↑</a></div>
      </div>
    </div>
  </footer>

  <script src="../../../../js/app.js"></script>
</body>
</html>
"""
    return html

async def generate_all():
    sem = asyncio.Semaphore(5)
    audio_tasks = []

    print("Building THE JUNIOR website...")
    
    for art in JUNIOR_ARTICLES:
        cat = art["category"]
        slug = art["slug"]
        art_dir = os.path.join(JUNIOR_DIR, cat, slug)
        audio_dir = os.path.join(art_dir, "audio")
        os.makedirs(audio_dir, exist_ok=True)
        
        # 1. Synthesize audio
        # Full body (rate: -10% for comfortable listening pace)
        full_text = " ".join([s["en"] for s in art["sentences"]])
        audio_tasks.append(synth_audio(full_text, VOICE_BRITISH, os.path.join(audio_dir, "full_body.mp3"), sem, rate="-10%"))
        
        for i, s in enumerate(art["sentences"]):
            audio_tasks.append(synth_audio(s["en"], VOICE_BRITISH, os.path.join(audio_dir, f"s{i+1}.mp3"), sem, rate="-10%"))
            
        for i, d in enumerate(art["dialogue"]):
            voice = VOICE_KEITA if (d["speaker"] == "慶" or "Keita" in d["name"]) else VOICE_NANAMI
            audio_tasks.append(synth_audio(d["text"], voice, os.path.join(audio_dir, f"dlg_{i+1:02d}.mp3"), sem))
            
        # 2. Write Article HTML
        html_content = build_junior_article_html(art)
        html_path = os.path.join(art_dir, "index.html")
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(html_content)
        print(f"[OK] Generated junior/{cat}/{slug}/index.html")

    print(f"Synthesizing {len(audio_tasks)} audio files for THE JUNIOR...")
    await asyncio.gather(*audio_tasks)
    print("All Junior audio files generated successfully!")

if __name__ == "__main__":
    asyncio.run(generate_all())
