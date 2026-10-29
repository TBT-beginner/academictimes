# -*- coding: utf-8 -*-
"""Update news_portal/index.html for 2026-10-30."""
import os

INDEX_PATH = os.path.join(os.path.dirname(__file__), "..", "index.html")

with open(INDEX_PATH, "r", encoding="utf-8") as f:
    text = f.read()

# 1. Date bar text
old_date_bar = '<span id="top-date-bar-text">Thursday October 29 2026 &nbsp;|&nbsp; Tokyo & London Editions &nbsp;•&nbsp; Daily University Exam Academic Digest</span>'
new_date_bar = '<span id="top-date-bar-text">Friday October 30 2026 &nbsp;|&nbsp; Tokyo & London Editions &nbsp;•&nbsp; Daily University Exam Academic Digest</span>'
assert old_date_bar in text, "old_date_bar not found"
text = text.replace(old_date_bar, new_date_bar, 1)

# 2. Select option
old_select = '<select id="select-edition-date" class="edition-select" aria-label="Select edition date">\n          <option value="2026-10-29" selected>2026年10月29日 (木) 号 【本日付・最新・全12記事】</option>'
new_select = '<select id="select-edition-date" class="edition-select" aria-label="Select edition date">\n          <option value="2026-10-30" selected>2026年10月30日 (金) 号 【本日付・最新・全12記事】</option>\n          <option value="2026-10-29">2026年10月29日 (木) 号 【全12記事・アーカイブ】</option>'
assert old_select in text, "old_select not found"
text = text.replace(old_select, new_select, 1)

# 3. Quick pills & collapsible
old_pills = """        <div class="edition-quick-pills">
          <a href="index.html#date-2026-10-29" style="padding: 0.35rem 0.75rem; border: 1px solid var(--times-black); background: #111; color: #fff; text-decoration: none; font-size: 0.78rem; font-weight: 700;" onclick="window.switchEdition('2026-10-29'); window.scrollTo({top:0, behavior:'smooth'}); return false;">10/29 (木) 本日最新号</a>
          <a href="index.html#date-2026-10-28" style="padding: 0.35rem 0.75rem; border: 1px solid var(--times-light-border); background: #fff; color: var(--times-black); text-decoration: none; font-size: 0.78rem; font-weight: 600;" onclick="window.switchEdition('2026-10-28'); window.scrollTo({top:0, behavior:'smooth'}); return false;">10/28 (水) 号</a>
          <a href="index.html#date-2026-10-27" style="padding: 0.35rem 0.75rem; border: 1px solid var(--times-light-border); background: #fff; color: var(--times-black); text-decoration: none; font-size: 0.78rem; font-weight: 600;" onclick="window.switchEdition('2026-10-27'); window.scrollTo({top:0, behavior:'smooth'}); return false;">10/27 (火) 号</a>
          <a href="index.html#date-2026-10-26" style="padding: 0.35rem 0.75rem; border: 1px solid var(--times-light-border); background: #fff; color: var(--times-black); text-decoration: none; font-size: 0.78rem; font-weight: 600;" onclick="window.switchEdition('2026-10-26'); window.scrollTo({top:0, behavior:'smooth'}); return false;">10/26 (月) 号</a>
          <a href="index.html#date-2026-10-25" style="padding: 0.35rem 0.75rem; border: 1px solid var(--times-light-border); background: #fff; color: var(--times-black); text-decoration: none; font-size: 0.78rem; font-weight: 600;" onclick="window.switchEdition('2026-10-25'); window.scrollTo({top:0, behavior:'smooth'}); return false;">10/25 (日) 号</a>
          <a href="index.html#date-2026-10-24" style="padding: 0.35rem 0.75rem; border: 1px solid var(--times-light-border); background: #fff; color: var(--times-black); text-decoration: none; font-size: 0.78rem; font-weight: 600;" onclick="window.switchEdition('2026-10-24'); window.scrollTo({top:0, behavior:'smooth'}); return false;">10/24 (土) 号</a>
        </div>

        <!-- Collapsible Older Editions (Preserves all past paper editions cleanly) -->
        <div class="edition-collapsible-content" id="edition-collapsible-content">
          <div class="edition-period-heading">📅 10月上旬〜中旬の紙面アーカイブ（10/23〜10/1 創刊号）</div>
          <div class="edition-quick-pills" style="margin-top: 0.4rem;">"""

new_pills = """        <div class="edition-quick-pills">
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
            <a href="index.html#date-2026-10-24" style="padding: 0.35rem 0.75rem; border: 1px solid var(--times-light-border); background: #fff; color: var(--times-black); text-decoration: none; font-size: 0.78rem; font-weight: 600;" onclick="window.switchEdition('2026-10-24'); window.scrollTo({top:0, behavior:'smooth'}); return false;">10/24 (土) 号</a>"""

assert old_pills in text, "old_pills not found"
text = text.replace(old_pills, new_pills, 1)

with open(INDEX_PATH, "w", encoding="utf-8") as f:
    f.write(text)

print("[OK] Successfully updated news_portal/index.html")
