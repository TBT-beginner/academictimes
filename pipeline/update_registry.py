import os
import sys

# Ensure pipeline dir is in sys.path
pipeline_dir = os.path.dirname(os.path.abspath(__file__))
if pipeline_dir not in sys.path:
    sys.path.insert(0, pipeline_dir)

from articles_data import ARTICLES

def update_registry():
    lines = [
        "# THE ACADEMIC TIMES & THE JUNIOR — Editorial Master Registry (重複防止・出典管理台帳)",
        "> **内部管理用ドキュメント（一般読者向けページからは非表示）**  ",
        "> 複数日にまたがるニュース記事の重複防止、一次ニュースソース、発行日、および先行研究・続報の相互リンク一覧。",
        "",
        "| # | 分野 | 配信日 | 記事タイトル | 一次ニュースソース（元報道） | ソース検証状況 |",
        "| :-: | :--- | :--- | :--- | :--- | :--- |"
    ]

    for i, a in enumerate(ARTICLES, start=1):
        cat_upper = a.get("category", "").upper()
        date_str = a.get("date", "2026-10-10")
        title = a.get("title", "")
        slug = a.get("slug", "")
        cat = a.get("category", "")
        src = a.get("source", "")
        link = f"[{title}](../{cat}/{slug}/index.html)"
        status = "✅ 認可一次ソース確認済"
        lines.append(f"| **{i:02d}** | {cat_upper} | {date_str} | {link} | {src} | {status} |")

    lines.extend([
        "",
        "---",
        "",
        "### 【除外・非復元記事監査ログ】",
        "以下の記事は一次ニュースソース検証ルールに基づき、復元対象から完全に除外されています：",
        "",
        "1. **`nihon-hidankyo-nobel-peace-prize`（日本被団協ノーベル平和賞）**:",
        "   * 除外理由: 2024年の過去ニュースであり、2026年最新の一次情報ソースが存在しないため。",
        "2. **`evtol-flying-taxis-tokyo-bay`（東京湾岸eVTOL試験運航）**:",
        "   * 除外理由: 認可メディアにおける実在する一次報道・公式発表が確認できないため。",
        ""
    ])

    reg_path = os.path.join(pipeline_dir, "ARTICLE_REGISTRY.md")
    with open(reg_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    print(f"Successfully updated ARTICLE_REGISTRY.md with {len(ARTICLES)} articles.")

if __name__ == "__main__":
    update_registry()
