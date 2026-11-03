# -*- coding: utf-8 -*-
"""Update index.html and junior/index.html for 2026-11-04."""

# 1. news_portal/index.html
with open("news_portal/index.html", "r", encoding="utf-8") as f:
    text = f.read()

text_norm = text.replace('\r\n', '\n')

old_top = '''      <span id="top-date-bar-text">Tuesday November 3 2026 &nbsp;|&nbsp; Tokyo & London Editions &nbsp;•&nbsp; Daily University Exam Academic Digest</span>
      <div class="edition-selector-wrap">
        <span style="font-weight: 700; color: #111;">📅 紙面切替:</span>
        <select id="select-edition-date" class="edition-select" aria-label="Select edition date">
          <option value="2026-11-03" selected>2026年11月3日 (火) 号 【本日付・最新・全12記事】</option>'''

new_top = '''      <span id="top-date-bar-text">Wednesday November 4 2026 &nbsp;|&nbsp; Tokyo & London Editions &nbsp;•&nbsp; Daily University Exam Academic Digest</span>
      <div class="edition-selector-wrap">
        <span style="font-weight: 700; color: #111;">📅 紙面切替:</span>
        <select id="select-edition-date" class="edition-select" aria-label="Select edition date">
          <option value="2026-11-04" selected>2026年11月4日 (水) 号 【本日付・最新・全12記事】</option>
          <option value="2026-11-03">2026年11月3日 (火) 号 【全12記事・アーカイブ】</option>'''

old_pills = '''        <!-- Recent Editions (Prominently displayed) -->
        <div class="edition-quick-pills">
          <a href="index.html#date-2026-11-03" style="padding: 0.35rem 0.75rem; border: 1px solid var(--times-black); background: #111; color: #fff; text-decoration: none; font-size: 0.78rem; font-weight: 700;" onclick="window.switchEdition('2026-11-03'); window.scrollTo({top:0, behavior:'smooth'}); return false;">11/03 (火) 本日最新号</a>
          <a href="index.html#date-2026-11-02" style="padding: 0.35rem 0.75rem; border: 1px solid var(--times-light-border); background: #fff; color: var(--times-black); text-decoration: none; font-size: 0.78rem; font-weight: 600;" onclick="window.switchEdition('2026-11-02'); window.scrollTo({top:0, behavior:'smooth'}); return false;">11/02 (月) 号</a>
          <a href="index.html#date-2026-11-01" style="padding: 0.35rem 0.75rem; border: 1px solid var(--times-light-border); background: #fff; color: var(--times-black); text-decoration: none; font-size: 0.78rem; font-weight: 600;" onclick="window.switchEdition('2026-11-01'); window.scrollTo({top:0, behavior:'smooth'}); return false;">11/01 (日) 号</a>
          <a href="index.html#date-2026-10-31" style="padding: 0.35rem 0.75rem; border: 1px solid var(--times-light-border); background: #fff; color: var(--times-black); text-decoration: none; font-size: 0.78rem; font-weight: 600;" onclick="window.switchEdition('2026-10-31'); window.scrollTo({top:0, behavior:'smooth'}); return false;">10/31 (土) 号</a>
          <a href="index.html#date-2026-10-30" style="padding: 0.35rem 0.75rem; border: 1px solid var(--times-light-border); background: #fff; color: var(--times-black); text-decoration: none; font-size: 0.78rem; font-weight: 600;" onclick="window.switchEdition('2026-10-30'); window.scrollTo({top:0, behavior:'smooth'}); return false;">10/30 (金) 号</a>
          <a href="index.html#date-2026-10-29" style="padding: 0.35rem 0.75rem; border: 1px solid var(--times-light-border); background: #fff; color: var(--times-black); text-decoration: none; font-size: 0.78rem; font-weight: 600;" onclick="window.switchEdition('2026-10-29'); window.scrollTo({top:0, behavior:'smooth'}); return false;">10/29 (木) 号</a>
        </div>

        <!-- Collapsible Older Editions (Preserves all past paper editions cleanly) -->
        <div class="edition-collapsible-content" id="edition-collapsible-content">
          <div class="edition-period-heading">📅 10月下旬〜創刊号の紙面アーカイブ（10/28〜10/1 創刊号）</div>
          <div class="edition-quick-pills" style="margin-top: 0.4rem;">
            <a href="index.html#date-2026-10-28"'''

new_pills = '''        <!-- Recent Editions (Prominently displayed) -->
        <div class="edition-quick-pills">
          <a href="index.html#date-2026-11-04" style="padding: 0.35rem 0.75rem; border: 1px solid var(--times-black); background: #111; color: #fff; text-decoration: none; font-size: 0.78rem; font-weight: 700;" onclick="window.switchEdition('2026-11-04'); window.scrollTo({top:0, behavior:'smooth'}); return false;">11/04 (水) 本日最新号</a>
          <a href="index.html#date-2026-11-03" style="padding: 0.35rem 0.75rem; border: 1px solid var(--times-light-border); background: #fff; color: var(--times-black); text-decoration: none; font-size: 0.78rem; font-weight: 600;" onclick="window.switchEdition('2026-11-03'); window.scrollTo({top:0, behavior:'smooth'}); return false;">11/03 (火) 号</a>
          <a href="index.html#date-2026-11-02" style="padding: 0.35rem 0.75rem; border: 1px solid var(--times-light-border); background: #fff; color: var(--times-black); text-decoration: none; font-size: 0.78rem; font-weight: 600;" onclick="window.switchEdition('2026-11-02'); window.scrollTo({top:0, behavior:'smooth'}); return false;">11/02 (月) 号</a>
          <a href="index.html#date-2026-11-01" style="padding: 0.35rem 0.75rem; border: 1px solid var(--times-light-border); background: #fff; color: var(--times-black); text-decoration: none; font-size: 0.78rem; font-weight: 600;" onclick="window.switchEdition('2026-11-01'); window.scrollTo({top:0, behavior:'smooth'}); return false;">11/01 (日) 号</a>
          <a href="index.html#date-2026-10-31" style="padding: 0.35rem 0.75rem; border: 1px solid var(--times-light-border); background: #fff; color: var(--times-black); text-decoration: none; font-size: 0.78rem; font-weight: 600;" onclick="window.switchEdition('2026-10-31'); window.scrollTo({top:0, behavior:'smooth'}); return false;">10/31 (土) 号</a>
          <a href="index.html#date-2026-10-30" style="padding: 0.35rem 0.75rem; border: 1px solid var(--times-light-border); background: #fff; color: var(--times-black); text-decoration: none; font-size: 0.78rem; font-weight: 600;" onclick="window.switchEdition('2026-10-30'); window.scrollTo({top:0, behavior:'smooth'}); return false;">10/30 (金) 号</a>
        </div>

        <!-- Collapsible Older Editions (Preserves all past paper editions cleanly) -->
        <div class="edition-collapsible-content" id="edition-collapsible-content">
          <div class="edition-period-heading">📅 10月下旬〜創刊号の紙面アーカイブ（10/29〜10/1 創刊号）</div>
          <div class="edition-quick-pills" style="margin-top: 0.4rem;">
            <a href="index.html#date-2026-10-29" style="padding: 0.35rem 0.75rem; border: 1px solid var(--times-light-border); background: #fff; color: var(--times-black); text-decoration: none; font-size: 0.78rem; font-weight: 600;" onclick="window.switchEdition('2026-10-29'); window.scrollTo({top:0, behavior:'smooth'}); return false;">10/29 (木) 号</a>
            <a href="index.html#date-2026-10-28"'''

if old_top in text_norm:
    text_norm = text_norm.replace(old_top, new_top, 1)
    print("Updated index.html top date bar.")
else:
    print("old_top not found in index.html")

if old_pills in text_norm:
    text_norm = text_norm.replace(old_pills, new_pills, 1)
    print("Updated index.html quick pills.")
else:
    print("old_pills not found in index.html")

with open("news_portal/index.html", "w", encoding="utf-8") as f:
    f.write(text_norm)

# 2. news_portal/junior/index.html
with open("news_portal/junior/index.html", "r", encoding="utf-8") as f:
    jtext = f.read()

jtext_norm = jtext.replace('\r\n', '\n')

j_old_top = '''      <span id="top-date-bar-text">Tuesday November 3 2026 &nbsp;|&nbsp; Tokyo & London Editions &nbsp;•&nbsp; Daily Junior English Learning Digest</span>
      <div class="edition-selector-wrap">
        <span style="font-weight: 700; color: #111;">📅 紙面切替:</span>
        <select id="select-edition-date" class="edition-select" aria-label="Select edition date">
          <option value="2026-11-03" selected>2026年11月3日 (火) 号 【本日・最新・全12記事】</option>'''

j_new_top = '''      <span id="top-date-bar-text">Wednesday November 4 2026 &nbsp;|&nbsp; Tokyo & London Editions &nbsp;•&nbsp; Daily Junior English Learning Digest</span>
      <div class="edition-selector-wrap">
        <span style="font-weight: 700; color: #111;">📅 紙面切替:</span>
        <select id="select-edition-date" class="edition-select" aria-label="Select edition date">
          <option value="2026-11-04" selected>2026年11月4日 (水) 号 【本日・最新・全12記事】</option>
          <option value="2026-11-03">2026年11月3日 (火) 号 【全12記事・アーカイブ】</option>'''

j_old_pills = '''          <div style="display: flex; flex-wrap: wrap; gap: 0.4rem;">
            <a href="index.html#date-2026-11-03" style="padding: 0.35rem 0.75rem; border: 1px solid #235937; background: #235937; color: #fff; text-decoration: none; font-size: 0.78rem; font-weight: 700;" onclick="window.switchEdition('2026-11-03'); window.scrollTo({top:0, behavior:'smooth'}); return false;">11/03 (火) 本日最新号</a>
            <a href="index.html#date-2026-11-02" style="padding: 0.35rem 0.75rem; border: 1px solid var(--times-light-border); background: #fff; color: var(--times-black); text-decoration: none; font-size: 0.78rem; font-weight: 600;" onclick="window.switchEdition('2026-11-02'); window.scrollTo({top:0, behavior:'smooth'}); return false;">11/02 (月) 号</a>
            <a href="index.html#date-2026-11-01" style="padding: 0.35rem 0.75rem; border: 1px solid var(--times-light-border); background: #fff; color: var(--times-black); text-decoration: none; font-size: 0.78rem; font-weight: 600;" onclick="window.switchEdition('2026-11-01'); window.scrollTo({top:0, behavior:'smooth'}); return false;">11/01 (日) 号</a>
            <a href="index.html#date-2026-10-31" style="padding: 0.35rem 0.75rem; border: 1px solid var(--times-light-border); background: #fff; color: var(--times-black); text-decoration: none; font-size: 0.78rem; font-weight: 600;" onclick="window.switchEdition('2026-10-31'); window.scrollTo({top:0, behavior:'smooth'}); return false;">10/31 (土) 号</a>
            <a href="index.html#date-2026-10-30" style="padding: 0.35rem 0.75rem; border: 1px solid var(--times-light-border); background: #fff; color: var(--times-black); text-decoration: none; font-size: 0.78rem; font-weight: 600;" onclick="window.switchEdition('2026-10-30'); window.scrollTo({top:0, behavior:'smooth'}); return false;">10/30 (金) 号</a>
            <a href="index.html#date-2026-10-29" style="padding: 0.35rem 0.75rem; border: 1px solid var(--times-light-border); background: #fff; color: var(--times-black); text-decoration: none; font-size: 0.78rem; font-weight: 600;" onclick="window.switchEdition('2026-10-29'); window.scrollTo({top:0, behavior:'smooth'}); return false;">10/29 (木) 号</a>
          </div>
        </div>
        
        <details style="margin-top: 0.5rem; width: 100%;">
          <summary style="font-size: 0.8rem; font-weight: 700; color: #235937; cursor: pointer; padding: 0.3rem 0;">
            📂 過去の全号を展開（28日分アーカイブ） ▾
          </summary>
          <div style="display: flex; flex-wrap: wrap; gap: 0.4rem; margin-top: 0.5rem; padding: 0.5rem; background: #fff; border: 1px dashed var(--times-light-border);">
            <a href="index.html#date-2026-10-28"'''

j_new_pills = '''          <div style="display: flex; flex-wrap: wrap; gap: 0.4rem;">
            <a href="index.html#date-2026-11-04" style="padding: 0.35rem 0.75rem; border: 1px solid #235937; background: #235937; color: #fff; text-decoration: none; font-size: 0.78rem; font-weight: 700;" onclick="window.switchEdition('2026-11-04'); window.scrollTo({top:0, behavior:'smooth'}); return false;">11/04 (水) 本日最新号</a>
            <a href="index.html#date-2026-11-03" style="padding: 0.35rem 0.75rem; border: 1px solid var(--times-light-border); background: #fff; color: var(--times-black); text-decoration: none; font-size: 0.78rem; font-weight: 600;" onclick="window.switchEdition('2026-11-03'); window.scrollTo({top:0, behavior:'smooth'}); return false;">11/03 (火) 号</a>
            <a href="index.html#date-2026-11-02" style="padding: 0.35rem 0.75rem; border: 1px solid var(--times-light-border); background: #fff; color: var(--times-black); text-decoration: none; font-size: 0.78rem; font-weight: 600;" onclick="window.switchEdition('2026-11-02'); window.scrollTo({top:0, behavior:'smooth'}); return false;">11/02 (月) 号</a>
            <a href="index.html#date-2026-11-01" style="padding: 0.35rem 0.75rem; border: 1px solid var(--times-light-border); background: #fff; color: var(--times-black); text-decoration: none; font-size: 0.78rem; font-weight: 600;" onclick="window.switchEdition('2026-11-01'); window.scrollTo({top:0, behavior:'smooth'}); return false;">11/01 (日) 号</a>
            <a href="index.html#date-2026-10-31" style="padding: 0.35rem 0.75rem; border: 1px solid var(--times-light-border); background: #fff; color: var(--times-black); text-decoration: none; font-size: 0.78rem; font-weight: 600;" onclick="window.switchEdition('2026-10-31'); window.scrollTo({top:0, behavior:'smooth'}); return false;">10/31 (土) 号</a>
            <a href="index.html#date-2026-10-30" style="padding: 0.35rem 0.75rem; border: 1px solid var(--times-light-border); background: #fff; color: var(--times-black); text-decoration: none; font-size: 0.78rem; font-weight: 600;" onclick="window.switchEdition('2026-10-30'); window.scrollTo({top:0, behavior:'smooth'}); return false;">10/30 (金) 号</a>
          </div>
        </div>
        
        <details style="margin-top: 0.5rem; width: 100%;">
          <summary style="font-size: 0.8rem; font-weight: 700; color: #235937; cursor: pointer; padding: 0.3rem 0;">
            📂 過去の全号を展開（29日分アーカイブ） ▾
          </summary>
          <div style="display: flex; flex-wrap: wrap; gap: 0.4rem; margin-top: 0.5rem; padding: 0.5rem; background: #fff; border: 1px dashed var(--times-light-border);">
            <a href="index.html#date-2026-10-29" style="padding: 0.35rem 0.75rem; border: 1px solid var(--times-light-border); background: #fff; color: var(--times-black); text-decoration: none; font-size: 0.78rem; font-weight: 600;" onclick="window.switchEdition('2026-10-29'); window.scrollTo({top:0, behavior:'smooth'}); return false;">10/29 (木) 号</a>
            <a href="index.html#date-2026-10-28"'''

if j_old_top in jtext_norm:
    jtext_norm = jtext_norm.replace(j_old_top, j_new_top, 1)
    print("Updated junior/index.html top date bar.")
else:
    print("j_old_top not found in junior/index.html")

if j_old_pills in jtext_norm:
    jtext_norm = jtext_norm.replace(j_old_pills, j_new_pills, 1)
    print("Updated junior/index.html quick pills.")
else:
    print("j_old_pills not found in junior/index.html")

with open("news_portal/junior/index.html", "w", encoding="utf-8") as f:
    f.write(jtext_norm)
print("Finished update_html_nov04.py!")
