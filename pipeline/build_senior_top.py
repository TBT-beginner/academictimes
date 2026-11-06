# -*- coding: utf-8 -*-
"""
Generates and updates news_portal/index.html (Senior Top Page).
Bakes the latest edition statically into the HTML for instant First Paint,
zero-JS fallback, SEO, and social previews, while ensuring seamless dynamic
interactive switching via js/home.js.
"""

import os
import sys
import json
import re

PORTAL_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
INDEX_PATH = os.path.join(PORTAL_DIR, "index.html")
PORTAL_DATA_PATH = os.path.join(PORTAL_DIR, "js", "portal-data.js")

def build_senior_top():
    if not os.path.exists(INDEX_PATH):
        print(f"[ERROR] {INDEX_PATH} not found.")
        return False

    if not os.path.exists(PORTAL_DATA_PATH):
        print(f"[ERROR] {PORTAL_DATA_PATH} not found.")
        return False

    with open(PORTAL_DATA_PATH, "r", encoding="utf-8") as f:
        js_text = f.read()

    m_art = re.search(r"const ARTICLES = (\[.*?\]);\s*\n", js_text, re.DOTALL)
    if not m_art:
        print("[ERROR] Could not parse ARTICLES from portal-data.js")
        return False
    articles = json.loads(m_art.group(1))
    art_map = {a["slug"]: a for a in articles}

    m_ed = re.search(r"const EDITIONS = ({.*?});\s*$", js_text, re.DOTALL)
    if not m_ed:
        print("[ERROR] Could not parse EDITIONS from portal-data.js")
        return False
    editions = json.loads(m_ed.group(1))

    date_keys = sorted(editions.keys(), reverse=True)
    latest_date = date_keys[0]
    ed = editions[latest_date]

    lead = art_map.get(ed["topLeadSlug"])
    if not lead:
        print(f"[ERROR] Top lead slug '{ed['topLeadSlug']}' not found in articles.")
        return False

    sub_leads = [art_map[s] for s in ed["subLeadSlugs"] if s in art_map]
    left_articles = [art_map[s] for s in ed["leftDispatches"] if s in art_map]
    right_articles = [art_map[s] for s in ed["rightDigestSlugs"] if s in art_map]

    with open(INDEX_PATH, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. Update Top Date Bar Text
    date_bar_text = f"{ed['dateStr']} &nbsp;|&nbsp; Tokyo & London Editions &nbsp;•&nbsp; Daily University Exam Academic Digest"
    html = re.sub(
        r'<span id="top-date-bar-text">.*?</span>',
        f'<span id="top-date-bar-text">{date_bar_text}</span>',
        html,
        flags=re.DOTALL
    )

    # 2. Update Select Dropdown Options
    select_options = []
    for dKey in date_keys:
        curr_ed = editions[dKey]
        sel_attr = " selected" if dKey == latest_date else ""
        label = curr_ed.get("editionLabel", f"{dKey} 号")
        select_options.append(f'          <option value="{dKey}"{sel_attr}>{label}</option>')
    select_options_str = "\n".join(select_options)

    html = re.sub(
        r'<select id="select-edition-date" class="edition-select" aria-label="Select edition date">.*?</select>',
        f'<select id="select-edition-date" class="edition-select" aria-label="Select edition date">\n{select_options_str}\n        </select>',
        html,
        flags=re.DOTALL
    )

    # 3. Update Sub Banner "Read Latest Top Story" link
    html = re.sub(
        r'<a href="[^"]*?" class="login-link">最新トップ記事を読む →</a>',
        f'<a href="{lead["path"]}" class="login-link">最新トップ記事を読む →</a>',
        html
    )

    # 4. Generate Hero Section (Left Column, Center Column, Right Column)
    # Left Column
    left_col_html_parts = []
    for idx, art in enumerate(left_articles):
        badge_cls = "badge-new" if idx == 0 else "badge-updated"
        badge_txt = "NEW" if idx == 0 else "DISPATCH"
        left_col_html_parts.append(f"""        <article class="left-story">
          <span class="{badge_cls}">{badge_txt} • {art['category_label']}</span>
          <h2 class="left-story-title">
            <a href="{art['path']}">{art['title']}</a>
          </h2>
          <p class="left-story-snippet">
            {art['headline_ja']}。{art['subhead']}
          </p>
          <div class="article-source-meta">
            <span>According to {art['source_name']}</span>
          </div>
        </article>""")
    left_col_str = "\n\n".join(left_col_html_parts)

    # Center Column (Lead + Sub-leads)
    sub_leads_html_parts = []
    for sub in sub_leads:
        sub_leads_html_parts.append(f"""          <div class="sub-lead-item">
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
          </div>""")
    sub_leads_str = "\n\n".join(sub_leads_html_parts)

    center_col_str = f"""        <article>
          <div class="lead-image-wrap">
            <img src="{lead['image']}" 
                 alt="{lead['title']}" 
                 class="lead-image"
                 onerror="this.src='https://images.unsplash.com/photo-1508700115892-45ecd05ae2ad?w=1000&auto=format&fit=crop&q=80'">
          </div>

          <span class="category-tag">TOP LEAD STORY • {lead['category_label']}</span>
          <h1 class="lead-story-title">
            <a href="{lead['path']}">
              {lead['title']}
            </a>
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
{sub_leads_str}
        </div>"""

    # Right Column
    right_col_html_parts = []
    for art in right_articles:
        right_col_html_parts.append(f"""        <article class="right-story">
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
        </article>""")
    right_col_str = "\n\n".join(right_col_html_parts)

    new_home_grid = f"""    <div class="home-grid">
      
      <!-- LEFT COLUMN: Latest Breaking Academic Dispatches -->
      <aside class="home-col-left">
{left_col_str}
      </aside>

      <!-- CENTER COLUMN: Top Lead Story (Featured Article) -->
      <section class="home-col-center">
{center_col_str}
      </section>

      <!-- RIGHT COLUMN: Academic & Opinion Digest -->
      <aside class="home-col-right">
{right_col_str}
      </aside>

    </div>"""

    html = re.sub(
        r'<div class="home-grid">.*?</div>\s*<!--\s*={5,}\s*SECTION 2:',
        f'{new_home_grid}\n\n    <!-- ==========================================================================\n         SECTION 2:',
        html,
        flags=re.DOTALL
    )

    # 5. Update Quick Pills (Top 5 Recent Editions)
    weekday_ja = ["月", "火", "水", "木", "金", "土", "日"]
    quick_pills = []
    for idx, dKey in enumerate(date_keys[:5]):
        # Parse month/day
        parts = dKey.split("-")
        m, d = parts[1], parts[2]
        import datetime
        dt = datetime.date(int(parts[0]), int(parts[1]), int(parts[2]))
        w = weekday_ja[dt.weekday()]
        if idx == 0:
            pill = f'<a href="index.html#date-{dKey}" style="padding: 0.35rem 0.75rem; border: 1px solid var(--times-black); background: #111; color: #fff; text-decoration: none; font-size: 0.78rem; font-weight: 700;" onclick="window.switchEdition(\'{dKey}\'); window.scrollTo({{top:0, behavior:\'smooth\'}}); return false;">{m}/{d} ({w}) 本日最新号</a>'
        else:
            pill = f'<a href="index.html#date-{dKey}" style="padding: 0.35rem 0.75rem; border: 1px solid var(--times-light-border); background: #fff; color: var(--times-black); text-decoration: none; font-size: 0.78rem; font-weight: 600;" onclick="window.switchEdition(\'{dKey}\'); window.scrollTo({{top:0, behavior:\'smooth\'}}); return false;">{m}/{d} ({w}) 号</a>'
        quick_pills.append(f"          {pill}")
    quick_pills_str = "\n".join(quick_pills)

    html = re.sub(
        r'<div class="edition-quick-pills">.*?</div>',
        f'<div class="edition-quick-pills">\n{quick_pills_str}\n        </div>',
        html,
        flags=re.DOTALL
    )

    with open(INDEX_PATH, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"[OK] Successfully built Senior Top Portal ({INDEX_PATH}) for edition {latest_date}.")
    return True

if __name__ == "__main__":
    build_senior_top()
