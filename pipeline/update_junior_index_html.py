# -*- coding: utf-8 -*-
"""Update news_portal/junior/index.html with top date bar, dropdown options, and quick pills."""

with open("news_portal/junior/index.html", "r", encoding="utf-8") as f:
    text = f.read()

text_norm = text.replace('\r\n', '\n')

old_top = '''      <span id="top-date-bar-text">Friday October 30 2026 &nbsp;|&nbsp; Tokyo & London Editions &nbsp;•&nbsp; High School Eiken Pre-2 ~ 2 Broadsheet</span>
      <div class="edition-selector-wrap">
        <span style="font-weight: 700; color: #111;">📅 紙面切替:</span>
        <select id="select-edition-date" class="edition-select" aria-label="Select edition date">
          <option value="2026-10-30" selected>2026年10月30日 (金) 号 【本日・最新・全12記事】</option>'''

new_top = '''      <span id="top-date-bar-text">Monday November 2 2026 &nbsp;|&nbsp; Tokyo & London Editions &nbsp;•&nbsp; High School Eiken Pre-2 ~ 2 Broadsheet</span>
      <div class="edition-selector-wrap">
        <span style="font-weight: 700; color: #111;">📅 紙面切替:</span>
        <select id="select-edition-date" class="edition-select" aria-label="Select edition date">
          <option value="2026-11-02" selected>2026年11月2日 (月) 号 【本日・最新・全12記事】</option>
          <option value="2026-11-01">2026年11月1日 (日) 号 【全12記事・アーカイブ】</option>
          <option value="2026-10-31">2026年10月31日 (土) 号 【全12記事・アーカイブ】</option>
          <option value="2026-10-30">2026年10月30日 (金) 号 【全12記事・アーカイブ】</option>'''

old_pills = '''          <div style="display: flex; flex-wrap: wrap; gap: 0.4rem;">
            <a href="index.html#date-2026-10-30" style="padding: 0.35rem 0.75rem; border: 1px solid #235937; background: #235937; color: #fff; text-decoration: none; font-size: 0.78rem; font-weight: 700;" onclick="window.switchEdition('2026-10-30'); window.scrollTo({top:0, behavior:'smooth'}); return false;">10/30 (金) 本日最新号</a>
            <a href="index.html#date-2026-10-29" style="padding: 0.35rem 0.75rem; border: 1px solid var(--times-light-border); background: #fff; color: var(--times-black); text-decoration: none; font-size: 0.78rem; font-weight: 600;" onclick="window.switchEdition('2026-10-29'); window.scrollTo({top:0, behavior:'smooth'}); return false;">10/29 (木) 号</a>
            <a href="index.html#date-2026-10-28" style="padding: 0.35rem 0.75rem; border: 1px solid var(--times-light-border); background: #fff; color: var(--times-black); text-decoration: none; font-size: 0.78rem; font-weight: 600;" onclick="window.switchEdition('2026-10-28'); window.scrollTo({top:0, behavior:'smooth'}); return false;">10/28 (水) 号</a>
            <a href="index.html#date-2026-10-27" style="padding: 0.35rem 0.75rem; border: 1px solid var(--times-light-border); background: #fff; color: var(--times-black); text-decoration: none; font-size: 0.78rem; font-weight: 600;" onclick="window.switchEdition('2026-10-27'); window.scrollTo({top:0, behavior:'smooth'}); return false;">10/27 (火) 号</a>
            <a href="index.html#date-2026-10-26" style="padding: 0.35rem 0.75rem; border: 1px solid var(--times-light-border); background: #fff; color: var(--times-black); text-decoration: none; font-size: 0.78rem; font-weight: 600;" onclick="window.switchEdition('2026-10-26'); window.scrollTo({top:0, behavior:'smooth'}); return false;">10/26 (月) 号</a>
          </div>
        </div>
        
        <details style="margin-top: 0.5rem; width: 100%;">
          <summary style="font-size: 0.8rem; font-weight: 700; color: #235937; cursor: pointer; padding: 0.3rem 0;">
            📂 過去の全号を展開（24日分アーカイブ） ▾
          </summary>
          <div style="display: flex; flex-wrap: wrap; gap: 0.4rem; margin-top: 0.5rem; padding: 0.5rem; background: #fff; border: 1px dashed var(--times-light-border);">
            <a href="index.html#date-2026-10-25"'''

new_pills = '''          <div style="display: flex; flex-wrap: wrap; gap: 0.4rem;">
            <a href="index.html#date-2026-11-02" style="padding: 0.35rem 0.75rem; border: 1px solid #235937; background: #235937; color: #fff; text-decoration: none; font-size: 0.78rem; font-weight: 700;" onclick="window.switchEdition('2026-11-02'); window.scrollTo({top:0, behavior:'smooth'}); return false;">11/02 (月) 本日最新号</a>
            <a href="index.html#date-2026-11-01" style="padding: 0.35rem 0.75rem; border: 1px solid var(--times-light-border); background: #fff; color: var(--times-black); text-decoration: none; font-size: 0.78rem; font-weight: 600;" onclick="window.switchEdition('2026-11-01'); window.scrollTo({top:0, behavior:'smooth'}); return false;">11/01 (日) 号</a>
            <a href="index.html#date-2026-10-31" style="padding: 0.35rem 0.75rem; border: 1px solid var(--times-light-border); background: #fff; color: var(--times-black); text-decoration: none; font-size: 0.78rem; font-weight: 600;" onclick="window.switchEdition('2026-10-31'); window.scrollTo({top:0, behavior:'smooth'}); return false;">10/31 (土) 号</a>
            <a href="index.html#date-2026-10-30" style="padding: 0.35rem 0.75rem; border: 1px solid var(--times-light-border); background: #fff; color: var(--times-black); text-decoration: none; font-size: 0.78rem; font-weight: 600;" onclick="window.switchEdition('2026-10-30'); window.scrollTo({top:0, behavior:'smooth'}); return false;">10/30 (金) 号</a>
            <a href="index.html#date-2026-10-29" style="padding: 0.35rem 0.75rem; border: 1px solid var(--times-light-border); background: #fff; color: var(--times-black); text-decoration: none; font-size: 0.78rem; font-weight: 600;" onclick="window.switchEdition('2026-10-29'); window.scrollTo({top:0, behavior:'smooth'}); return false;">10/29 (木) 号</a>
            <a href="index.html#date-2026-10-28" style="padding: 0.35rem 0.75rem; border: 1px solid var(--times-light-border); background: #fff; color: var(--times-black); text-decoration: none; font-size: 0.78rem; font-weight: 600;" onclick="window.switchEdition('2026-10-28'); window.scrollTo({top:0, behavior:'smooth'}); return false;">10/28 (水) 号</a>
          </div>
        </div>
        
        <details style="margin-top: 0.5rem; width: 100%;">
          <summary style="font-size: 0.8rem; font-weight: 700; color: #235937; cursor: pointer; padding: 0.3rem 0;">
            📂 過去の全号を展開（27日分アーカイブ） ▾
          </summary>
          <div style="display: flex; flex-wrap: wrap; gap: 0.4rem; margin-top: 0.5rem; padding: 0.5rem; background: #fff; border: 1px dashed var(--times-light-border);">
            <a href="index.html#date-2026-10-27" style="padding: 0.35rem 0.75rem; border: 1px solid var(--times-light-border); background: #fff; color: var(--times-black); text-decoration: none; font-size: 0.78rem; font-weight: 600;" onclick="window.switchEdition('2026-10-27'); window.scrollTo({top:0, behavior:'smooth'}); return false;">10/27 (火) 号</a>
            <a href="index.html#date-2026-10-26" style="padding: 0.35rem 0.75rem; border: 1px solid var(--times-light-border); background: #fff; color: var(--times-black); text-decoration: none; font-size: 0.78rem; font-weight: 600;" onclick="window.switchEdition('2026-10-26'); window.scrollTo({top:0, behavior:'smooth'}); return false;">10/26 (月) 号</a>
            <a href="index.html#date-2026-10-25"'''

if old_top in text_norm:
    text_norm = text_norm.replace(old_top, new_top, 1)
    print("Updated junior top date bar and dropdown.")
else:
    print("old_top not found in junior index")

if old_pills in text_norm:
    text_norm = text_norm.replace(old_pills, new_pills, 1)
    print("Updated junior quick pills and details accordion.")
else:
    print("old_pills not found in junior index")

with open("news_portal/junior/index.html", "w", encoding="utf-8") as f:
    f.write(text_norm)
