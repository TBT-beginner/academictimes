# -*- coding: utf-8 -*-
"""
Automated Page Generator & Edge-TTS Audio Synthesizer
Builds complete, production-ready article pages matching The Times broadsheet layout.
"""

import os
import asyncio
import edge_tts
import sys
sys.path.append(os.path.dirname(__file__))
from articles_data import ARTICLES
from build_junior_data_js import DATE_MAP
import datetime

VOICE_BRITISH = "en-GB-RyanNeural"
VOICE_KEITA = "ja-JP-KeitaNeural"
VOICE_NANAMI = "ja-JP-NanamiNeural"

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title} | THE ACADEMIC TIMES</title>
  <meta name="description" content="{subhead}">
  
  <!-- CSS -->
  <link rel="stylesheet" href="../../styles/times.css">
</head>
<body id="article-top">

  <!-- ==========================================================================
       1. STICKY ARTICLE TITLE BAR (スクロール追従・最大1行・小さめ表示)
       ========================================================================== -->
  <div class="sticky-article-bar" id="sticky-article-bar">
    <div class="sticky-bar-inner">
      <div style="display: flex; align-items: baseline; min-width: 0; flex: 1;">
        <span class="sticky-bar-category">{category_short}</span>
        <span class="sticky-title-text">{title}</span>
      </div>
      <a href="#article-top" style="font-size: 0.75rem; color: var(--times-blue); font-weight: 700; text-decoration: none; flex-shrink: 0; padding-left: 0.5rem;">Top ↑</a>
    </div>
    <div class="reading-progress-track" id="reading-progress"></div>
  </div>

  <!-- Top Date Bar -->
  <div class="top-date-bar">
    {date_en_bar} &nbsp;|&nbsp; Tokyo & London Editions &nbsp;•&nbsp; Daily University Exam Academic Digest
  </div>

  <!-- The Times Masthead -->
  <header class="masthead">
    <a href="../../index.html" class="masthead-link">
      <span class="masthead-title">THE ACADEMIC TIMES</span>
    </a>
    <div class="masthead-subtitle">The Daily Broadsheet for Scholarly English, Global News & Critical Analysis</div>
  </header>

  <!-- Navigation Bar -->
  <nav class="nav-bar">
    <div class="nav-container">
      <ul class="nav-list">
        <li class="nav-item"><a href="../../index.html">Home</a></li>
        <li class="nav-item {society_active}"><a href="../../society/index.html">Society & Mind</a></li>
        <li class="nav-item {science_active}"><a href="../../science/index.html">Science & Tech</a></li>
        <li class="nav-item {culture_active}"><a href="../../culture/index.html">Culture & Thought</a></li>
        <li class="nav-item {law_active}"><a href="../../law/index.html">Law & Justice</a></li>
        <li class="nav-item {world_active}"><a href="../../world/index.html">World & Security</a></li>
        <li class="nav-item {entertainment_active}"><a href="../../entertainment/index.html">Entertainment & Gadgets</a></li>
        <li class="nav-item"><a href="../../index.html#ranking">Most Read</a></li>
      </ul>
    </div>
  </nav>

  <!-- Main Article Content -->
  <main class="page-wrapper">
    <article class="article-container">
      
      <!-- Hero Header (Full Screen Viewport with generous vertical space) -->
      <header class="article-header hero-header" id="hero-header">
        <div class="hero-content-inner">
          <div class="article-kicker" style="margin-bottom: 1.25rem;">{category_label}</div>
          <h1 class="article-h1" style="margin: 1.5rem 0 1.25rem;">{title}</h1>
          <p class="article-subhead" style="margin: 0 auto 1.75rem;">
            {headline_ja}<br>
            {subhead}
          </p>
          <div class="article-meta-row">
            <span class="article-author">解説：Keita先生 ＆ Nanamiさん（THE ACADEMIC TIMES）</span>
            <span>•</span>
            <time datetime="{date_iso}">📅 ニュースソース発行日: {date_ja}（{date_en_full}）</time>
            <span>•</span>
            <span class="badge-new">NEW EDITION</span>
          </div>

          <!-- NEWS SOURCE ATTRIBUTION (初期画面内に地味に表示・装飾なし) -->
          <details class="source-accordion">
            <summary>
              <span>ニュースソース（出典: {source_name}）</span>
              <span class="source-toggle-icon">▾</span>
            </summary>
            <div class="source-accordion-body">
              <div style="margin-bottom: 0.4rem; font-size: 0.85rem; color: var(--times-dark);">
                <strong>📰 ニュースソース：</strong><span>{source_name}</span>
              </div>
              <div style="margin-bottom: 0.6rem; padding-bottom: 0.5rem; border-bottom: 1px dashed #ccc; font-size: 0.85rem; color: var(--times-dark);">
                <strong>📅 ニュースソース発行日：</strong><time datetime="{date_iso}">{date_ja}（{date_en_full}）</time>
              </div>
              {source_attribution}<br>
              <span style="font-size: 0.8rem; color: var(--times-muted); margin-top: 0.4rem; display: inline-block;">
                元記事URL: <a href="{source_url}" target="_blank" rel="noopener noreferrer" style="color: var(--times-dark); text-decoration: underline;">{source_url} ↗</a>
              </span>
              <div class="student-source-guide" style="margin-top: 0.85rem; padding-top: 0.85rem; border-top: 1px dashed #bbb;">
                <div style="font-weight: 700; font-size: 0.82rem; color: var(--times-black); margin-bottom: 0.35rem;">
                  🎓 高校生が知っておくべきメディアの視点 & 入試での価値
                </div>
                <div style="font-size: 0.82rem; line-height: 1.65; color: var(--times-body);">
                  {source_student_guide}
                </div>
              </div>
            </div>
          </details>

          <!-- Scroll to Article Cue -->
          <div style="display: flex; justify-content: center; align-items: center; width: 100%; margin-top: 2.25rem;">
            <div class="hero-scroll-cue" id="hero-scroll-cue" title="記事本文へスクロール" style="margin: 0 auto; text-align: center;">
              <span class="cue-label">SCROLL TO ARTICLE</span>
              <span class="cue-arrow">↓</span>
            </div>
          </div>
        </div>
      </header>

      <!-- ==========================================================================
           ARTICLE BODY & INLINE AUDIO
           ========================================================================== -->
      <section id="section-article">
        <div class="article-headline-block" id="article-headline-block" style="margin: 0.5rem 0 1.25rem; padding-bottom: 0.75rem; border-bottom: 1px solid var(--times-light-border);">
          <span class="category-tag">ORIGINAL ESSAY HEADLINE</span>
          <div style="font-family: var(--font-headline); font-size: 1.55rem; font-weight: 700; color: var(--times-black); margin-top: 0.35rem; line-height: 1.3;">
            {title}
          </div>

          <!-- 音声メニュー：SPEED + 再生ボタン(アイコンのみ) + 日本語訳(国旗アイコンのみ) -->
          <div class="audio-inline-bar" id="full-body-banner">
            <!-- Speed Controller -->
            <div class="speed-control-group" title="再生速度の調節">
              <span class="speed-control-label">SPEED</span>
              <button type="button" class="btn-speed-opt" data-speed="0.8">0.8x</button>
              <button type="button" class="btn-speed-opt active-speed" data-speed="1.0">1.0x</button>
              <button type="button" class="btn-speed-opt" data-speed="1.2">1.2x</button>
              <button type="button" class="btn-speed-opt" data-speed="1.5">1.5x</button>
            </div>

            <!-- Single Play Button: 英語朗読＋解説（ラベルなし・アイコンのみ） -->
            <button type="button" class="btn-audio-circle" id="btn-play-continuous" title="英語朗読＋解説を再生 / 一時停止" aria-label="Play continuous audio and dialogue">
              <span class="audio-state-icon">▶</span>
            </button>

            <!-- Single Flag Toggle: 日本語全訳トグル（国旗アイコンのみ） -->
            <button type="button" class="btn-flag-toggle" id="btn-toggle-ja" title="日本語全訳の表示 / 非表示" aria-label="Toggle Japanese translation">
              <span>🇯🇵</span>
            </button>

            <span class="inline-reading-hint">※文クリックで音声再生</span>
          </div>
        </div>

        <!-- Authentic Broadsheet Body -->
        <div class="article-real-body">
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

        <!-- Hidden Japanese Translation (Toggled by Flag Button) -->
        <div class="ja-translation article-real-translation" id="ja-article-translation">
          <div style="font-size: 0.75rem; font-weight: 700; color: var(--times-muted); text-transform: uppercase; margin-bottom: 0.5rem; letter-spacing: 0.05em;">【日本語全訳】</div>
          <p class="real-para">
            {s1_ja} {s2_ja}
          </p>
          <p class="real-para">
            {s3_ja} {s4_ja} {s5_ja}
          </p>
        </div>
      </section>

      <!-- ==========================================================================
           RELATED & ANTECEDENT COVERAGE (関連報道・先行研究・続報)
           ========================================================================== -->
      <section class="study-section" id="section-related" style="margin-top: 2rem; border-top: 1px solid var(--times-black); padding-top: 2rem;">
        <h2 class="study-section-title">
          <span class="marker">■</span> 関連ニュース・先行報道（Related & Antecedent Coverage）
        </h2>
        <p style="font-size: 0.875rem; color: var(--times-muted); margin-bottom: 1.25rem;">
          本記事の理解を深める関連報道・先行研究および制度的背景を合わせて精読できます。
        </p>
        <div style="display: grid; gap: 1rem;">
          {related_html}
        </div>
      </section>

      <!-- ==========================================================================
           DISCUSSION: Keita先生 & Nanamiさん (中高生向け対話解説)
           ========================================================================== -->
      <section class="dialogue-wrapper" id="section-discussion">
        <div class="dialogue-head">
          <div class="dialogue-title-area">
            <span class="dialogue-badge">TALK & DISCUSS</span>
            <h2 class="dialogue-main-heading">5分でわかる！Keita先生とNanamiさんのニュース深掘りトーク</h2>
          </div>
          <div>
            <button type="button" class="btn-audio-play" id="btn-play-dialogue-all" style="font-size: 0.75rem; padding: 0.35rem 0.8rem; background: transparent; border: 1px solid #111; color: #111;">
              <span class="audio-state-icon">▶</span>
              <span>解説トークを通しで聴く (約2分)</span>
            </button>
          </div>
        </div>
        
        <p class="dialogue-lead">
          「英文は読んだけれど、背景知識や入試での問われ方が知りたい！」という受験生のために、予備校講師のKeita先生と現役大学生アシスタントのNanamiさんが、今回のニュースの狙われどころを分かりやすくナビゲートします！
        </p>

        {dialogue_turns_html}
      </section>

      <!-- ==========================================================================
           VOCABULARY DRILL (厳選重要語彙演習)
           ========================================================================== -->
      <section class="study-section" id="section-vocabulary">
        <h2 class="study-section-title">
          <span class="marker">■</span> 厳選重要語彙（Vocabulary Drill）
        </h2>
        <p style="font-size: 0.875rem; color: var(--times-muted); margin-bottom: 1rem;">
          大学入試長文・英検準1級〜1級で問われる「多義語」「学術的語彙」「文脈語」を厳選。英英定義でコアイメージを掴みます。
        </p>

        <table class="vocab-table">
          <thead>
            <tr>
              <th style="width: 25%;">語句・発音</th>
              <th style="width: 30%;">意味・品詞</th>
              <th style="width: 45%;">英英定義 & 入試頻出例文</th>
            </tr>
          </thead>
          <tbody>
            {vocab_rows_html}
          </tbody>
        </table>
      </section>

      <!-- ==========================================================================
           SYNTAX & RHETORIC (構文・文法徹底解説)
           ========================================================================== -->
      <section class="study-section" id="section-syntax">
        <h2 class="study-section-title">
          <span class="marker">■</span> 構文・文法徹底解説（Syntax & Rhetoric）
        </h2>
        {syntax_cards_html}
      </section>

      <!-- ==========================================================================
           PRONUNCIATION & LINKING GUIDE (発音・リズムの急所)
           ========================================================================== -->
      <section class="study-section" id="section-pronunciation">
        <h2 class="study-section-title">
          <span class="marker">🗣</span> 発音・リズムの急所（日本人が戸惑いやすいポイント）
        </h2>
        <p style="font-size: 0.875rem; color: var(--times-muted); margin-bottom: 1.25rem;">
          単語単体の発音では聞き取れない「音の脱落（リダクション）」「音の連結（リンキング）」「アクセントの罠」を確認しましょう。
        </p>
        {pronunciation_cards_html}
      </section>

      <!-- ==========================================================================
           INTERACTIVE QUIZ (入試実戦 確認クイズ)
           ========================================================================== -->
      <section class="study-section" id="section-quiz">
        <h2 class="study-section-title">
          <span class="marker">■</span> 入試実戦 確認クイズ（Interactive Quiz）
        </h2>
        <p style="font-size: 0.875rem; color: var(--times-muted); margin-bottom: 1.25rem;">
          本文で学んだ構文・語彙・文脈理解を4択問題でテストします。
        </p>
        {quiz_items_html}
      </section>

      <!-- ==========================================================================
           FAQ & STUDY ADVICE (読者からのFAQ・学習相談)
           ========================================================================== -->
      <section class="study-section" id="section-faq">
        <h2 class="study-section-title">
          <span class="marker">■</span> 読者からのFAQ・学習相談（Frequently Asked Questions）
        </h2>
        <div class="faq-box">
          {faq_items_html}
        </div>
      </section>

      <!-- ==========================================================================
           FACT-CHECK & CRITICAL CONTEXT (最深層ファクトチェック & 学術的背景知識)
           ========================================================================== -->
      <section class="study-section" id="section-factcheck">
        <h2 class="study-section-title">
          <span class="marker">■</span> ファクトチェック & 背景知識（Fact-Check & Critical Context）
        </h2>
        <p style="font-size: 0.875rem; color: var(--times-muted); margin-bottom: 1.25rem;">
          海外メディアの元記事で提示された統計データ、社会心理学実験、および科学的背景を学術的に検証します。
        </p>
        {factcheck_blocks_html}
      </section>

    </article>
  </main>

  <!-- FLOATING TABLE OF CONTENTS -->
  <div class="floating-toc-wrapper">
    <div class="floating-toc-panel" id="floating-toc-panel">
      <div class="toc-heading">TABLE OF CONTENTS</div>
      <ul class="toc-list">
        <li><a href="#article-top" class="toc-link">Top of Page</a></li>
        <li><a href="#section-article" class="toc-link">Article & Audio</a></li>
        <li><a href="#section-related" class="toc-link">Related Coverage</a></li>
        <li><a href="#section-discussion" class="toc-link">Discussion (Keita & Nanami)</a></li>
        <li><a href="#section-vocabulary" class="toc-link">Vocabulary Drill</a></li>
        <li><a href="#section-syntax" class="toc-link">Syntax & Grammar</a></li>
        <li><a href="#section-pronunciation" class="toc-link">Pronunciation Guide</a></li>
        <li><a href="#section-quiz" class="toc-link">Interactive Quiz</a></li>
        <li><a href="#section-faq" class="toc-link">FAQ & Advice</a></li>
        <li><a href="#section-factcheck" class="toc-link">Fact-Check Context</a></li>
      </ul>
    </div>
    <button type="button" class="btn-floating-toc" id="btn-floating-toc" aria-label="Open Table of Contents">
      <span>☰</span>
      <span>Contents</span>
    </button>
  </div>

  <!-- Times UK Style Footer -->
  <footer class="times-footer">
    <div class="footer-container">
      <div class="footer-top">
        <a href="../../index.html" class="footer-logo">THE ACADEMIC TIMES</a>
        <div style="font-size: 0.8125rem; color: #888;">
          Authentic English Journalism for University Entrance & Lifelong Learning
        </div>
      </div>
      <div class="footer-bottom">
        <div>© 2026 THE ACADEMIC TIMES. All rights reserved. Fact-checked against original sources.</div>
        <div><a href="#article-top" style="color: #888; text-decoration: underline;">Back to Top ↑</a></div>
      </div>
    </div>
  </footer>

  <!-- Scripts -->
  <script src="../../js/app.js"></script>
</body>
</html>
"""

async def synth_audio(text, voice, outpath, sem):
    async with sem:
        if os.path.exists(outpath) and os.path.getsize(outpath) > 1000:
            return
        try:
            comm = edge_tts.Communicate(text, voice)
            await comm.save(outpath)
        except Exception as e:
            print(f"Error generating {outpath}: {e}")

async def generate_article_audio_files(art, art_dir, sem):
    audio_dir = os.path.join(art_dir, "audio")
    os.makedirs(audio_dir, exist_ok=True)
    
    tasks = []
    
    # 1. Headline
    headline_text = art["title"]
    tasks.append(synth_audio(headline_text, VOICE_BRITISH, os.path.join(audio_dir, "headline.mp3"), sem))
    
    # 2. Sentences (s1 to s5) & full body
    body_text = " ".join([s["en"] for s in art["sentences"]])
    tasks.append(synth_audio(body_text, VOICE_BRITISH, os.path.join(audio_dir, "full_body.mp3"), sem))
    
    for i, s in enumerate(art["sentences"]):
        tasks.append(synth_audio(s["en"], VOICE_BRITISH, os.path.join(audio_dir, f"s{i+1}.mp3"), sem))
        
    # 3. Dialogue (dlg_01 to dlg_07)
    for i, dlg in enumerate(art["dialogue"]):
        voice = VOICE_KEITA if dlg["speaker"] == "慶" else VOICE_NANAMI
        tasks.append(synth_audio(dlg["text"], voice, os.path.join(audio_dir, f"dlg_{i+1:02d}.mp3"), sem))
        
    await asyncio.gather(*tasks)
    print(f"Audio ready for {art['slug']}")

def build_article_html(art):
    cat = art["category"]
    
    # Active navigation class
    soc_act = "active" if cat == "society" else ""
    sci_act = "active" if cat == "science" else ""
    cul_act = "active" if cat == "culture" else ""
    law_act = "active" if cat == "law" else ""
    wor_act = "active" if cat == "world" else ""
    ent_act = "active" if cat == "entertainment" else ""
    
    # Related links HTML
    related_blocks = []
    for rel in art.get("related_links", []):
        r_html = f"""
        <div style="padding: 0.75rem 0; border-bottom: 1px solid var(--times-light-border);">
          <div style="font-size: 0.75rem; font-weight: 700; color: var(--times-blue); margin-bottom: 0.25rem;">
            {rel.get('relation', '【関連報道】')}
          </div>
          <div style="font-family: var(--font-headline); font-size: 1.05rem; font-weight: 700;">
            <a href="{rel['url']}" style="color: var(--times-black); text-decoration: underline;">{rel['title']} →</a>
          </div>
          <div style="font-size: 0.85rem; color: var(--times-muted); margin-top: 0.25rem;">
            {rel['desc']}
          </div>
        </div>
        """
        related_blocks.append(r_html)
    related_html = "\n".join(related_blocks)
    
    # Dialogue HTML
    dlg_blocks = []
    for i, d in enumerate(art["dialogue"]):
        turn_id = f"dlg-{i+1}"
        audio_file = f"audio/dlg_{i+1:02d}.mp3"
        is_teacher = ("Keita" in d["name"] or d.get("role", "") == "英語講師" or d.get("speaker", "") == "慶")
        turn_cls = "turn-teacher" if is_teacher else "turn-assistant"
        avatar_cls = "avatar-teacher" if is_teacher else "avatar-assistant"
        avatar_char = "慶" if is_teacher else "七"
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
    dialogue_turns_html = "\n".join(dlg_blocks)
    
    # Vocab rows
    vocab_list = art.get("vocab") or art.get("vocabulary") or []
    vocab_rows = []
    for v in vocab_list:
        row = f"""
        <tr>
          <td>
            <div class="vocab-word-en">{v['word']}</div>
            <div style="font-size: 0.78rem; color: var(--times-muted);">{v['phonetic']}</div>
          </td>
          <td>
            <strong>{v['meaning']}</strong>
            <div style="font-size: 0.75rem; color: #888;">{v['pos']}</div>
          </td>
          <td>
            <div class="vocab-def-en">{v['def']}</div>
            <div class="vocab-example">{v['ex']}</div>
          </td>
        </tr>
        """
        vocab_rows.append(row)
    vocab_rows_html = "\n".join(vocab_rows)
    
    # Syntax cards
    syntax_cards = []
    for syn in art["syntax"]:
        card = f"""
        <div class="grammar-card">
          <div class="grammar-card-head">
            <span class="grammar-target-phrase">{syn['phrase']}</span>
            <span class="grammar-meaning">「{syn['meaning']}」</span>
          </div>
          <div class="grammar-card-body">
            <p>{syn['explanation']}</p>
          </div>
        </div>
        """
        syntax_cards.append(card)
    syntax_cards_html = "\n".join(syntax_cards)
    
    # Pronunciation cards
    pron_list = art.get("pronunciation")
    if not pron_list and vocab_list:
        v0 = vocab_list[0]
        v1 = vocab_list[1] if len(vocab_list) > 1 else v0
        pron_list = [
            {"phrase": v0["word"] + " の発音・アクセント", "meaning": f"標準発音記号: {v0.get('phonetic', '')}"},
            {"phrase": v1["word"] + " の発音・アクセント", "meaning": f"標準発音記号: {v1.get('phonetic', '')}"}
        ]
    pron_cards = []
    for p in (pron_list or []):
        p_html = f"""
        <div class="grammar-card">
          <div class="grammar-card-head">
            <span class="grammar-target-phrase">{p['phrase']}</span>
            <span class="grammar-meaning">{p['meaning']}</span>
          </div>
        </div>
        """
        pron_cards.append(p_html)
    pronunciation_cards_html = "\n".join(pron_cards)
    
    # Quiz items
    quiz_items = []
    for q_idx, q in enumerate(art["quiz"]):
        btns = []
        letters = ["A", "B", "C", "D"]
        for opt_idx, opt in enumerate(q["options"]):
            is_cor = "true" if opt_idx == q["correct_index"] else "false"
            btns.append(f"""
            <button type="button" class="quiz-btn" data-correct="{is_cor}">
              <span class="quiz-opt-letter">{letters[opt_idx]}</span>
              <span>{opt}</span>
            </button>
            """)
        quiz_html = f"""
        <div class="quiz-item" data-answered="false">
          <div class="quiz-question-text">
            <span class="quiz-q-num">Q{q_idx+1}.</span>
            {q['question']}
          </div>
          <div class="quiz-choices">
            {''.join(btns)}
          </div>
          <div class="quiz-explanation">
            <strong>【正解解説】</strong><br>
            {q['explanation']}
          </div>
        </div>
        """
        quiz_items.append(quiz_html)
    quiz_items_html = "\n".join(quiz_items)
    
    # FAQ
    faq_items = []
    for f in art.get("faq", []):
        f_html = f"""
        <details class="faq-item">
          <summary class="faq-summary">Q. {f['q']}</summary>
          <div class="faq-answer">
            {f['a']}
          </div>
        </details>
        """
        faq_items.append(f_html)
    faq_items_html = "\n".join(faq_items)
    
    # Factcheck
    fc_blocks = []
    for fc in art.get("factcheck", []):
        fc_html = f"""
        <div class="grammar-card">
          <div class="grammar-card-head">
            <span class="grammar-target-phrase">{fc['title']}</span>
          </div>
          <div class="grammar-card-body">
            <p>{fc['body']}</p>
          </div>
        </div>
        """
        fc_blocks.append(fc_html)
    factcheck_blocks_html = "\n".join(fc_blocks)
    
    student_guides = {
        "air-defence-shield": (
            "<strong>【掲載紙：Financial Times / The Times】</strong><br>"
            "・<strong>メディアの視点：</strong>英国議会および防衛調達の透明性を検証する最高峰の経済・政治高級紙。国家安全保障の機密性と国民の税金使途（100億ポンド）のバランスを鋭く追究しています。<br>"
            "・<strong>高校生が知るべき理由：</strong>大学入試の社会科学系長文（東大・一橋・慶應法など）では、『防衛と予算』『国家主権と説明責任』が頻出。感情論ではなく制度論として安全保障を英語で論じる力が養われます。"
        ),
        "colorectal-cancer-under-50s": (
            "<strong>【掲載誌：Nature Medicine / BBC Health】</strong><br>"
            "・<strong>メディアの視点：</strong>世界最高峰の学術誌Natureの医学部門。従来の常識（高齢者の病気）を覆す若年性大腸がんの急増について、世界各国の疫学データから原因を科学的に追究しています。<br>"
            "・<strong>高校生が知るべき理由：</strong>国公立・私立医学部や難関理系の長文出題で圧倒的1位の出典分野。超加工食品やマイクロプラスチックといった日常の環境因子が生体に与える影響を、因果関係の英語構文（cause, trigger, correlate with）で読み解く絶好の教材です。"
        ),
        "raf-fairford-bomber-redeployment": (
            "<strong>【配信元：Reuters / AP News】</strong><br>"
            "・<strong>メディアの視点：</strong>世界中の新聞社・テレビ局が一次情報として頼る二大国際通信社。記者の主観や政治的バイアスを徹底排除し、客観的事実（5W1H）と国際条約上の枠組みに忠実に報道しています。<br>"
            "・<strong>高校生が知るべき理由：</strong>共通テストの速読や国公立2次試験の事実把握問題で最も重要な『事実と意見の峻別』を学べます。NATO第5条や集団的自衛権といった現代社会・政治経済の基礎知識も英語で同時に習得できます。"
        ),
        "psychology-casual-encounters": (
            "<strong>【掲載誌：Journal of Personality and Social Psychology / The Atlantic】</strong><br>"
            "・<strong>メディアの視点：</strong>社会心理学の世界的査読論文誌と、米国を代表する深層言論誌The Atlantic。都市生活者の孤独と微小なコミュニケーションの効能を実証実験から論じています。<br>"
            "・<strong>高校生が知るべき理由：</strong>早稲田・慶應・上智・国公立大の自由英作文で『現代の人間関係と孤独』は超頻出。マーク・グラノヴェッターの『弱い紐帯の強み』などの学術概念は、小論文でも強力な武器になります。"
        ),
        "jeffrey-archer-obituary": (
            "<strong>【掲載紙：The Times UK / The Guardian】</strong><br>"
            "・<strong>メディアの視点：</strong>1785年創刊のThe Timesが誇る名物コーナー『Obituaries（評伝・追悼記事）』。一人の波乱万丈な生涯を通して、20世紀後半の英国政治と大衆文学の興亡を格調高い筆致で記録しています。<br>"
            "・<strong>高校生が知るべき理由：</strong>過去完了形や分詞構文、修辞的表現（paradox, irony）など、高校英語の最難関構文が凝縮。物語や伝記調の長文読解（外語大・早稲田文系等）の突破口になります。"
        ),
        "royal-security-judicial-review": (
            "<strong>【掲載紙：The Telegraph / The Times UK】</strong><br>"
            "・<strong>メディアの視点：</strong>英国の保守本流高級紙による憲法・司法報道。元王室メンバーの公的警護費用をめぐる内務省委員会（RAVEC）の決定と、それに対する司法審査の正当性を冷静に分析しています。<br>"
            "・<strong>高校生が知るべき理由：</strong>『司法審査（Judicial Review）』や『行政裁量（executive discretion）』は、法学部志望者のみならず現代文・小論文の法と正義論の根幹。英米法の法廷ロジックに触れる最高の入門編です。"
        ),
        "clarkson-business-red-tape": (
            "<strong>【掲載紙：The Sunday Times】</strong><br>"
            "・<strong>メディアの視点：</strong>英国で最も部数の多い高級日曜紙The Sunday Timesの看板コラム。地方で農場・パブを経営する人気司会者が、過剰な官僚主義（red tape）に直面した体験を痛烈なユーモアと反語で告発しています。<br>"
            "・<strong>高校生が知るべき理由：</strong>反語表現（Rhetorical Questions）や皮肉（Sarcasm）を見抜く読解演習。地方創生と規制改革という経済政策のリアルな現場を英語で実感できます。"
        ),
        "inheritance-tax-reform-debate": (
            "<strong>【掲載紙：The Times UK / Financial Times】</strong><br>"
            "・<strong>メディアの視点：</strong>英国保守党の党首選における税制政策スピーチの論評。相続税が『努力の結晶の搾取』なのか『機会の不平等の是正』なのかという、富の再分配をめぐる根源的な哲学的対立を報じています。<br>"
            "・<strong>高校生が知るべき理由：</strong>慶應経済や東大文科・法学部で問われる『公正（Justice）と格差』のテーマ。親の財産を子が受け継ぐ権利と社会全体の公平性という、自由英作文で賛否を論じる格好の題材です。"
        ),
        "ai-pediatric-diagnosis-consent": (
            "<strong>【掲載紙：The Guardian / BMJ Health】</strong><br>"
            "・<strong>メディアの視点：</strong>先端科学と人権・生命倫理を鋭く追究するThe Guardian。小児医療へのAI診断導入にあたり、親の同意権とAIのブラックボックス化（説明責任の欠如）を法廷闘争から深掘りしています。<br>"
            "・<strong>高校生が知るべき理由：</strong>『AIと医療倫理』は、東大・京大・医学部・慶應SFCなどで近年激増している超重要出題テーマ。インフォームド・コンセントの現代的変容を英語で整理できます。"
        ),
        "mediterranean-marine-heatwaves": (
            "<strong>【配信元：Reuters Science / Copernicus Climate Service】</strong><br>"
            "・<strong>メディアの視点：</strong>EUの地球観測プログラムCopernicusの科学データに基づくロイターの環境科学スクープ。表層だけでなく水深数十メートルの冷水域にまで達する未知の海洋熱波の脅威を報じています。<br>"
            "・<strong>高校生が知るべき理由：</strong>大学入試長文で毎年必ず出題される『地球温暖化と海洋生態系』の最先端。水温躍層（thermocline）や生物濃縮など、理科・地学・環境論述の専門語彙を英語で学べます。"
        ),
        "generative-ai-paleontology": (
            "<strong>【掲載誌：Science / MIT Technology Review】</strong><br>"
            "・<strong>メディアの視点：</strong>世界的科学誌ScienceとMITの発行する先端テクノロジー誌。化石という過去の不完全なデータから、生成AIの物理演算によって生体運動を再現する文理融合の研究成果です。<br>"
            "・<strong>高校生が知るべき理由：</strong>『過去の化石記録×現代の深層学習』という知の越境（Interdisciplinary Research）。理系・情報系・文理融合学部を目指す受験生にとって、最新の学問の地平を見せてくれる内容です。"
        )
    }
    guide_text = student_guides.get(art["slug"], "海外一流紙の論理的な英文から、大学入試に直結する背景知識とクリティカル・シンキングを養います。")
    
    slug = art["slug"]
    date_iso = art.get("date") or DATE_MAP.get(slug, "2026-10-09")
    dt = datetime.datetime.strptime(date_iso, "%Y-%m-%d")
    date_ja = f"{dt.year}年{dt.month}月{dt.day}日"
    date_en_bar = dt.strftime("%A %B %d %Y").replace(" 0", " ")
    date_en_full = dt.strftime("%B %d, %Y").replace(" 0", " ")
    
    s = art["sentences"]
    return HTML_TEMPLATE.format(
        title=art["title"],
        category_short=art["category"].upper(),
        category_label=art["category_label"],
        headline_ja=art["headline_ja"],
        subhead=art["subhead"],
        source_name=art["source_name"],
        source_url=art["source_url"],
        source_attribution=art["source_attribution"],
        source_student_guide=guide_text,
        society_active=soc_act,
        science_active=sci_act,
        culture_active=cul_act,
        law_active=law_act,
        world_active=wor_act,
        entertainment_active=ent_act,
        date_iso=date_iso,
        date_ja=date_ja,
        date_en_bar=date_en_bar,
        date_en_full=date_en_full,
        s1_en=s[0]["en"], s1_ja=s[0]["ja"],
        s2_en=s[1]["en"], s2_ja=s[1]["ja"],
        s3_en=s[2]["en"], s3_ja=s[2]["ja"],
        s4_en=s[3]["en"], s4_ja=s[3]["ja"],
        s5_en=s[4]["en"], s5_ja=s[4]["ja"],
        related_html=related_html,
        dialogue_turns_html=dialogue_turns_html,
        vocab_rows_html=vocab_rows_html,
        syntax_cards_html=syntax_cards_html,
        pronunciation_cards_html=pronunciation_cards_html,
        quiz_items_html=quiz_items_html,
        faq_items_html=faq_items_html,
        factcheck_blocks_html=factcheck_blocks_html
    )

async def main():
    sem = asyncio.Semaphore(6)
    portal_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    for art in ARTICLES:
        slug = art["slug"]
        cat = art["category"]
        art_dir = os.path.join(portal_dir, cat, slug)
        os.makedirs(art_dir, exist_ok=True)
        
        # 1. Write HTML
        html_content = build_article_html(art)
        html_path = os.path.join(art_dir, "index.html")
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(html_content)
        print(f"Generated HTML for {cat}/{slug}/index.html")
        
        # 2. Synthesize Audio
        await generate_article_audio_files(art, art_dir, sem)

if __name__ == "__main__":
    asyncio.run(main())
