# -*- coding: utf-8 -*-
with open("news_portal/index.html", "r", encoding="utf-8") as f:
    text = f.read()

# Update top-date-bar-text
text = text.replace(
    'Monday October 26 2026',
    'Tuesday October 27 2026'
)

# Update dropdown option
target_opt = '<option value="2026-10-26" selected>2026年10月26日 (月) 号 【本日付・最新・全12記事】</option>'
new_opt = '<option value="2026-10-27" selected>2026年10月27日 (火) 号 【本日付・最新・全12記事】</option>\n          <option value="2026-10-26">2026年10月26日 (月) 号 【全12記事・アーカイブ】</option>'

assert target_opt in text, "target_opt not found"
text = text.replace(target_opt, new_opt, 1)

# Update quick-pills
pos = text.find('edition-quick-pills')
pos_end = text.find('10/26', pos)
pos_a_start = text.rfind('<a ', 0, pos_end)
pos_a_end = text.find('</a>', pos_end) + 4
old_first_pill = text[pos_a_start:pos_a_end]

new_first_pill = '<a href="index.html#date-2026-10-27" style="padding: 0.35rem 0.75rem; border: 1px solid var(--times-black); background: #111; color: #fff; text-decoration: none; font-size: 0.78rem; font-weight: 700;" onclick="window.switchEdition(\'2026-10-27\'); window.scrollTo({top:0, behavior:\'smooth\'}); return false;">10/27 (火) 本日最新号</a>\n          <a href="index.html#date-2026-10-26" style="padding: 0.35rem 0.75rem; border: 1px solid var(--times-light-border); background: #fff; color: var(--times-black); text-decoration: none; font-size: 0.78rem; font-weight: 600;" onclick="window.switchEdition(\'2026-10-26\'); window.scrollTo({top:0, behavior:\'smooth\'}); return false;">10/26 (月) 号</a>'

text = text[:pos_a_start] + new_first_pill + text[pos_a_end:]

with open("news_portal/index.html", "w", encoding="utf-8", newline="\n") as f:
    f.write(text)

print("Successfully updated index.html with 2026-10-27")
