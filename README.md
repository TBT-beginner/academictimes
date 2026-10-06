# THE ACADEMIC TIMES

> **The Daily Broadsheet for Scholarly English, Global News & Critical Analysis**  
> 大学入試英語長文・自由英作文・小論文対策のためのアカデミック英語ニュースポータル

---

## 📰 プロジェクト概要 (Overview)

**THE ACADEMIC TIMES** は、英米の一流高級紙（*TIME*, *The Times*, *The Guardian*, *Financial Times*, *Nature*, *Reuters* など）の本格時事記事をベースに、難関大学入試（東大・京大・早慶等）で頻出するアカデミックな5大分野を網羅した日刊ブロードシート型ウェブポータルです。

### 主な機能・特徴
- **The Times 風ブロードシート・デザイン**: 伝統的英国高級紙のタイポグラフィと3カラム紙面レイアウト。
- **マルチ音声（Edge-TTS）完全完備**:
  - 本格イギリス英語朗読（Ryan Neural）
  - Keita先生 & Nanamiさんによる日本語対話解説（文法・背景・論理展開）
- **難関大レベル インタラクティブ4択クイズ**: 全記事に東大・早慶レベルの読解問題3問と詳細解説を収録。
- **日別トップページ（バックナンバー）切り替え**: 2026年10月1日号〜10月6日号への動的・静的切り替え。
- **リアルタイム過去記事検索**: タイトル、英単語、出題分野、一次メディア名で瞬時に絞り込み可能。
- **高校生向けメディア・リテラシー解説**: ニュースに興味がない高校生でも長文の論理構成を見抜ける背景知識集。

---

## 📂 フォルダ構造 (Directory Structure)

```text
academictimes/
├── index.html                   # メインポータル最新号（動的紙面スイッチャー・リアルタイム検索）
├── edition-2026-10-01.html      # 10月1日（木）創刊号 単独トップページ
├── edition-2026-10-02.html      # 10月2日（金）号 単独トップページ
├── edition-2026-10-03.html      # 10月3日（土）号 単独トップページ
├── edition-2026-10-04.html      # 10月4日（日）号 単独トップページ
├── edition-2026-10-05.html      # 10月5日（月）号 単独トップページ
│
├── styles/                      # スタイルシート
│   └── times.css                # The Times Broadsheet デザインシステム
│
├── js/                          # フロントエンド・スクリプト
│   ├── portal-data.js           # 15記事・6日分紙面・メディアリソースのマスターデータ
│   └── home.js                  # 日付切り替え、インデックス検索、クイズ制御
│
├── culture/                     # 【Culture & Thought】文化・思想・認知心理学
│   ├── index.html               # Culture専用ハブ・学習戦略
│   ├── headphones-in-public/    # 公共空間のイヤホンと白昼夢
│   ├── jeffrey-archer-obituary/ # アーチャー氏訃報と英国大衆文学
│   └── stoic-philosophy-digital-age/ # デジタル時代のストア哲学
│
├── law/                         # 【Law & Justice】法制度・国家安全保障・生命倫理
│   ├── index.html               # Law専用ハブ・学習戦略
│   ├── air-defence-shield/      # 英国防空シールドと議会統制
│   ├── royal-security-judicial-review/ # 王室警護と公金司法審査
│   └── ai-pediatric-diagnosis-consent/ # 小児AI診断と親の同意権
│
├── science/                     # 【Science & Tech】先端科学・医学・気候変動
│   ├── index.html               # Science専用ハブ・学習戦略
│   ├── colorectal-cancer-under-50s/ # 若年大腸がん急増の謎
│   ├── generative-ai-paleontology/  # 生成ニューラルネットワークと古生物復元
│   └── mediterranean-marine-heatwaves/ # 地中海深海海洋熱波
│
├── society/                     # 【Society & Mind】社会・経済・都市心理学
│   ├── index.html               # Society専用ハブ・学習戦略
│   ├── clarkson-business-red-tape/  # 地方起業と規制緩和
│   ├── inheritance-tax-reform-debate/ # 相続税制改革と農場承継
│   └── psychology-casual-encounters/  # 偶発的対人交流と幸福感
│
├── world/                       # 【World & Security】国際情勢・外交・資源地政学
│   ├── index.html               # World専用ハブ・学習戦略
│   ├── raf-fairford-bomber-redeployment/ # フェアフォード米軍爆撃機再配置
│   ├── critical-minerals-geopolitics/    # 重要鉱物サプライチェーン同盟
│   └── arctic-sea-route-unclos/          # 北極海航路と海洋法条約
│
├── junior/                      # 🌿【THE JUNIOR】高校基礎〜標準・英検準2級〜2級エディション
│   ├── index.html               # THE JUNIOR トップ紙面（全5分野カタログ・学習ステップ）
│   ├── styles/times-junior.css  # Junior専用スタイルシート
│   ├── culture/headphones-in-public/
│   ├── science/colorectal-cancer-under-50s/
│   ├── society/psychology-casual-encounters/
│   ├── law/air-defence-shield/
│   └── world/critical-minerals-geopolitics/
│
└── pipeline/                    # 記事生成・TTS合成・管理スクリプト群
    ├── ARTICLE_REGISTRY.md      # 重複防止・一次ソース管理台帳（内部用）
    ├── articles_data.py         # 記事マスターデータセット
    ├── junior_articles_data.py  # THE JUNIOR 記事マスターデータセット
    ├── build_junior_site.py     # THE JUNIOR 記事 & 音声生成スクリプト
    ├── build_junior_top.py      # THE JUNIOR トップ紙面生成スクリプト
    ├── generate_all_articles.py # 記事HTML & Edge-TTS生成スクリプト
    ├── generate_category_pages.py # カテゴリ別トップページ生成スクリプト
    └── generate_editions_pages.py # 日別トップページ生成スクリプト
```

---

## 🚀 デプロイと利用方法 (Usage)

本リポジトリは GitHub Pages にそのまま対応しています。
リポジトリの **Settings > Pages** から `Branch: main` (または `master`) / `Folder: / (root)` を設定するだけで、Webサイトとして即時公開可能です。
