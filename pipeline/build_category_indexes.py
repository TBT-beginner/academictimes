import os

sections = {
    'society': ('Society & Mind', '社会・教育・心理学分野', 'Sociological & Educational Analyses'),
    'science': ('Science & Tech', '科学・医学・環境分野', 'Scientific Dispatches & Biomedical Reviews'),
    'law': ('Law & Justice', '法律・制度・法哲学分野', 'Legal Opinions & Constitutional Benchmarks'),
    'world': ('World & Security', '国際情勢・安全保障分野', 'Global Affairs, Treaties & Diplomacy')
}

template = """<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title} | THE ACADEMIC TIMES</title>
  <link rel="stylesheet" href="../styles/times.css">
</head>
<body>
  <div class="top-date-bar">Tuesday October 6 2026 &nbsp;|&nbsp; {title} Section</div>
  <header class="masthead">
    <a href="../index.html" class="masthead-link">
      <span class="masthead-title">THE ACADEMIC TIMES</span>
    </a>
    <div class="masthead-subtitle">{subtitle}</div>
  </header>
  <nav class="nav-bar">
    <div class="nav-container">
      <ul class="nav-list">
        <li class="nav-item"><a href="../index.html">Home</a></li>
        <li class="nav-item {act_soc}"><a href="../society/index.html">Society & Mind</a></li>
        <li class="nav-item {act_sci}"><a href="../science/index.html">Science & Tech</a></li>
        <li class="nav-item"><a href="../culture/index.html">Culture & Thought</a></li>
        <li class="nav-item {act_law}"><a href="../law/index.html">Law & Justice</a></li>
        <li class="nav-item {act_wor}"><a href="../world/index.html">World & Security</a></li>
      </ul>
    </div>
  </nav>

  <main class="page-wrapper">
    <div class="section-heading-bar">
      <h1 class="section-heading">{title} ARCHIVE</h1>
      <span style="font-size: 0.8125rem; color: var(--times-muted);">{desc}</span>
    </div>

    <div style="padding: 3rem 1rem; text-align: center; color: var(--times-muted); background: var(--times-bg-soft); border: 1px solid var(--times-light-border); margin-top: 1.5rem;">
      <h2 style="font-family: var(--font-headline); font-size: 1.4rem; color: var(--times-black); margin-bottom: 0.5rem;">{title} カテゴリ記事一覧</h2>
      <p style="font-size: 0.9rem; max-width: 600px; margin: 0 auto 1.5rem; line-height: 1.7;">
        本カテゴリの記事は日次パイプライン（1日10本配信）により配信されます。ファクトチェックおよびEdge-TTS音声を準備中です。
      </p>
      <a href="../culture/headphones-in-public/index.html" class="btn-trial">本日のトップ特集（Culture）を見る →</a>
    </div>
  </main>

  <footer class="times-footer">
    <div class="footer-container">
      <div class="footer-bottom">
        <div>© 2026 THE ACADEMIC TIMES.</div>
        <div><a href="../index.html" style="color: #aaa;">Homeに戻る</a></div>
      </div>
    </div>
  </footer>
</body>
</html>"""

base = r'c:\Users\teacher\Documents\lessonfactory\news_portal'
for slug, (title, desc, sub) in sections.items():
    content = template.format(
        title=title, desc=desc, subtitle=sub,
        act_soc='active' if slug == 'society' else '',
        act_sci='active' if slug == 'science' else '',
        act_law='active' if slug == 'law' else '',
        act_wor='active' if slug == 'world' else ''
    )
    path = os.path.join(base, slug, 'index.html')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print('Created:', path)
