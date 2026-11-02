# -*- coding: utf-8 -*-
"""Update news_portal/index.html with top date bar, dropdown options, and quick pills."""

with open("news_portal/index.html", "r", encoding="utf-8") as f:
    text = f.read()

# 1. Update date bar & dropdown
old_top = '''      <span id="top-date-bar-text">Friday October 30 2026 &nbsp;|&nbsp; Tokyo & London Editions &nbsp;•&nbsp; Daily University Exam Academic Digest</span>
      <div class="edition-selector-wrap">
        <span style="font-weight: 700; color: #111;">📅 紙面切替:</span>
        <select id="select-edition-date" class="edition-select" aria-label="Select edition date">
          <option value="2026-10-30" selected>2026年10月30日 (金) 号 【本日付・最新・全12記事】</option>'''

new_top = '''      <span id="top-date-bar-text">Monday November 2 2026 &nbsp;|&nbsp; Tokyo & London Editions &nbsp;•&nbsp; Daily University Exam Academic Digest</span>
      <div class="edition-selector-wrap">
        <span style="font-weight: 700; color: #111;">📅 紙面切替:</span>
        <select id="select-edition-date" class="edition-select" aria-label="Select edition date">
          <option value="2026-11-02" selected>2026年11月2日 (月) 号 【本日付・最新・全12記事】</option>
          <option value="2026-11-01">2026年11月1日 (日) 号 【全12記事・アーカイブ】</option>
          <option value="2026-10-31">2026年10月31日 (土) 号 【全12記事・アーカイブ】</option>
          <option value="2026-10-30">2026年10月30日 (金) 号 【全12記事・アーカイブ】</option>'''

# 2. Update quick pills & accordion
old_pills = '''        <!-- Recent Editions (Prominently displayed) -->
        <div class="edition-quick-pills">
          <a href="index.html#date-2026-10-30" style="padding: 0.35rem 0.75rem; border: 1px solid var(--times-black); background: #111; color: #fff; text-decoration: none; font-size: 0.78rem; font-weight: 700;" onclick="window.switchEdition('2026-10-30'); window.scrollTo({top:0, behavior:'smooth'}); return false;">10/30 (金) 本日最新号</a>
          <a href="index.html#date-2026-10-29" style="padding: 0.35rem 0.75rem; border: 1px solid var(--times-light-border); background: #fff; color: var(--times-black); text-decoration: none; font-size: 0.78rem; font-weight: 600;" onclick="window.switchEdition('2026-10-29'); window.scrollTo({top:0, behavior:'smooth'}); return false;">10/29 (木) 号</a>
          <a href="index.html#date-2026-10-28" style="padding: 0.35rem 0.75rem; border: 1px solid var(--times-light-border); background: #fff; color: var(--times-black); text-decoration: none; font-size: 0.78rem; font-weight: 600;" onclick="window.switchEdition('2026-10-28'); window.scrollTo({top:0, behavior:'smooth'}); return false;">10/28 (水) 号</a>
          <a href="index.html#date-2026-10-27" style="padding: 0.35rem 0.75rem; border: 1px solid var(--times-light-border); background: #fff; color: var(--times-black); text-decoration: none; font-size: 0.78rem; font-weight: 600;" onclick="window.switchEdition('2026-10-27'); window.scrollTo({top:0, behavior:'smooth'}); return false;">10/27 (火) 号</a>
          <a href="index.html#date-2026-10-26" style="padding: 0.35rem 0.75rem; border: 1px solid var(--times-light-border); background: #fff; color: var(--times-black); text-decoration: none; font-size: 0.78rem; font-weight: 600;" onclick="window.switchEdition('2026-10-26'); window.scrollTo({top:0, behavior:'smooth'}); return false;">10/26 (月) 号</a>
          <a href="index.html#date-2026-10-25" style="padding: 0.35rem 0.75rem; border: 1px solid var(--times-light-border); background: #fff; color: var(--times-black); text-decoration: none; font-size: 0.78rem; font-weight: 600;" onclick="window.switchEdition('2026-10-25'); window.scrollTo({top:0, behavior:'smooth'}); return false;">10/25 (日) 号</a>
        </div>

        <!-- Collapsible Older Editions (Preserves all past paper editions cleanly) -->
        <div class="edition-collapsible-content" id="edition-collapsible-content">
          <div class="edition-period-heading">📅 10月上旬〜中旬の紙面アーカイブ（10/24〜10/1 創刊号）</div>
          <div class="edition-quick-pills" style="margin-top: 0.4rem;">
            <a href="index.html#date-2026-10-24"'''

new_pills = '''        <!-- Recent Editions (Prominently displayed) -->
        <div class="edition-quick-pills">
          <a href="index.html#date-2026-11-02" style="padding: 0.35rem 0.75rem; border: 1px solid var(--times-black); background: #111; color: #fff; text-decoration: none; font-size: 0.78rem; font-weight: 700;" onclick="window.switchEdition('2026-11-02'); window.scrollTo({top:0, behavior:'smooth'}); return false;">11/02 (月) 本日最新号</a>
          <a href="index.html#date-2026-11-01" style="padding: 0.35rem 0.75rem; border: 1px solid var(--times-light-border); background: #fff; color: var(--times-black); text-decoration: none; font-size: 0.78rem; font-weight: 600;" onclick="window.switchEdition('2026-11-01'); window.scrollTo({top:0, behavior:'smooth'}); return false;">11/01 (日) 号</a>
          <a href="index.html#date-2026-10-31" style="padding: 0.35rem 0.75rem; border: 1px solid var(--times-light-border); background: #fff; color: var(--times-black); text-decoration: none; font-size: 0.78rem; font-weight: 600;" onclick="window.switchEdition('2026-10-31'); window.scrollTo({top:0, behavior:'smooth'}); return false;">10/31 (土) 号</a>
          <a href="index.html#date-2026-10-30" style="padding: 0.35rem 0.75rem; border: 1px solid var(--times-light-border); background: #fff; color: var(--times-black); text-decoration: none; font-size: 0.78rem; font-weight: 600;" onclick="window.switchEdition('2026-10-30'); window.scrollTo({top:0, behavior:'smooth'}); return false;">10/30 (金) 号</a>
          <a href="index.html#date-2026-10-29" style="padding: 0.35rem 0.75rem; border: 1px solid var(--times-light-border); background: #fff; color: var(--times-black); text-decoration: none; font-size: 0.78rem; font-weight: 600;" onclick="window.switchEdition('2026-10-29'); window.scrollTo({top:0, behavior:'smooth'}); return false;">10/29 (木) 号</a>
          <a href="index.html#date-2026-10-28" style="padding: 0.35rem 0.75rem; border: 1px solid var(--times-light-border); background: #fff; color: var(--times-black); text-decoration: none; font-size: 0.78rem; font-weight: 600;" onclick="window.switchEdition('2026-10-28'); window.scrollTo({top:0, behavior:'smooth'}); return false;">10/28 (水) 号</a>
        </div>

        <!-- Collapsible Older Editions (Preserves all past paper editions cleanly) -->
        <div class="edition-collapsible-content" id="edition-collapsible-content">
          <div class="edition-period-heading">📅 10月下旬〜創刊号の紙面アーカイブ（10/27〜10/1 創刊号）</div>
          <div class="edition-quick-pills" style="margin-top: 0.4rem;">
            <a href="index.html#date-2026-10-27" style="padding: 0.35rem 0.75rem; border: 1px solid var(--times-light-border); background: #fff; color: var(--times-black); text-decoration: none; font-size: 0.78rem; font-weight: 600;" onclick="window.switchEdition('2026-10-27'); window.scrollTo({top:0, behavior:'smooth'}); return false;">10/27 (火) 号</a>
            <a href="index.html#date-2026-10-26" style="padding: 0.35rem 0.75rem; border: 1px solid var(--times-light-border); background: #fff; color: var(--times-black); text-decoration: none; font-size: 0.78rem; font-weight: 600;" onclick="window.switchEdition('2026-10-26'); window.scrollTo({top:0, behavior:'smooth'}); return false;">10/26 (月) 号</a>
            <a href="index.html#date-2026-10-25" style="padding: 0.35rem 0.75rem; border: 1px solid var(--times-light-border); background: #fff; color: var(--times-black); text-decoration: none; font-size: 0.78rem; font-weight: 600;" onclick="window.switchEdition('2026-10-25'); window.scrollTo({top:0, behavior:'smooth'}); return false;">10/25 (日) 号</a>
            <a href="index.html#date-2026-10-24"'''

# Normalize newlines
text_norm = text.replace('\r\n', '\n')
old_top_norm = old_top.replace('\r\n', '\n')
new_top_norm = new_top.replace('\r\n', '\n')
old_pills_norm = old_pills.replace('\r\n', '\n')
new_pills_norm = new_pills.replace('\r\n', '\n')

if old_top_norm in text_norm:
    text_norm = text_norm.replace(old_top_norm, new_top_norm, 1)
    print("Updated top date bar and dropdown.")
else:
    print("old_top_norm not found")

if old_pills_norm in text_norm:
    text_norm = text_norm.replace(old_pills_norm, new_pills_norm, 1)
    print("Updated quick pills and accordion.")
else:
    print("old_pills_norm not found")

with open("news_portal/index.html", "w", encoding="utf-8") as f:
    f.write(text_norm)
