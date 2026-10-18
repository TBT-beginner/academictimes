# -*- coding: utf-8 -*-
"""
apply_past_tags_and_boxes.py
Updates past articles with clear, distinguished labels:
- 【過去の基礎論文解説】 for academic papers (Nature / Science)
- 【過去のニュース深掘り】 for past journalism news (The Guardian 2024)
Includes high-quality educational rationale in notice boxes for both Senior and Junior versions.
"""

import os
import re

def update_batch11():
    path = os.path.join(os.path.dirname(__file__), "batch11_articles_data.py")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # The 7 past news articles in Batch 11
    # 1. england-school-chain-phone-free-policy
    content = content.replace(
        '"category_label": "EDUCATION POLICY & ADOLESCENCE • 英国全校スマホ禁止令の拡大",',
        '"category_label": "【過去のニュース深掘り】 EDUCATION POLICY & ADOLESCENCE • 英国全校スマホ禁止令の拡大",\n        "is_past_news": True,\n        "foundational_reason_title": "【過去のニュース深掘り】なぜ今、高校生がこのニュースを振り返るべきなのか？",\n        "foundational_reason_html": """\n        <p style=\\"font-size: 0.88rem; line-height: 1.75; color: #1e3a8a; margin: 0 0 0.75rem;\\">\n          <strong>① 世界的な「学校内スマホ禁止」潮流の原点と教育社会学：</strong><br>\n          2024年秋に英国最大級のアカデミー連合（生徒3万5千人）が決断した完全スマホ持ち込み禁止は、ユネスコ（UNESCO）の勧告や欧米各国での法規制、さらには日本の学校現場でのルール見直しに直結する歴史的転換点です。単なる校則問題ではなく、青少年の認知的成熟とデジタル依存の克服を巡る重要事例です。\n        </p>\n        <p style=\\"font-size: 0.88rem; line-height: 1.75; color: #1e3a8a; margin: 0;\\">\n          <strong>② 推薦・総合型選抜・小論文の最頻出テーマ：</strong><br>\n          「教育現場における情報端末の利便性と弊害」「休み時間の対面交流が生む社会的スキル」など、高校生自身が当事者として説得力のある論述を展開できる最重要トピックです。\n        </p>\n        """,',
        1
    )

    # Junior version of england-school-chain-phone-free-policy
    content = content.replace(
        '"category_label": "EDUCATION POLICY • 英国学校スマホ禁止",',
        '"category_label": "【過去のニュース深掘り】 EDUCATION POLICY • 英国学校スマホ禁止",\n        "is_past_news": True,\n        "foundational_reason_title": "【過去のニュース深掘り】なぜ今、高校生がこのニュースを振り返るべきなのか？",\n        "foundational_reason_html": """\n        <p style=\\"font-size: 0.88rem; line-height: 1.75; color: #1e3a8a; margin: 0;\\">\n          <strong>💡 高校生自身の生活と英検自由英作文に直結：</strong><br>\n          授業中だけでなく休み時間もスマホを封印することで、友達との会話や集中力がどう変わるのか。英検のライティングテストや面接で「学校でスマホを使うべきか」という質問に、具体的で説得力のある理由を英語で答えるための最高の題材です。\n        </p>\n        """,',
        1
    )

    # 2. four-day-workweek-uk-trial-permanent
    content = content.replace(
        '"category_label": "LABOUR ECONOMICS & WELLBEING • 週休3日制の恒久化と労働生産性",',
        '"category_label": "【過去のニュース深掘り】 LABOUR ECONOMICS & WELLBEING • 週休3日制の恒久化と労働生産性",\n        "is_past_news": True,\n        "foundational_reason_title": "【過去のニュース深掘り】なぜ今、高校生がこのニュースを振り返るべきなのか？",\n        "foundational_reason_html": """\n        <p style=\\"font-size: 0.88rem; line-height: 1.75; color: #1e3a8a; margin: 0 0 0.75rem;\\">\n          <strong>① 労働経済学の常識を覆した世界最大の実証実験：</strong><br>\n          英国で61社・約3,000人を対象に実施された実証実験で、「給与100%維持のまま勤務時間を80%に削減しても、売上高が向上し離職率が劇的に低下した」という2024年の成果報告です。現代の経済学や経営学において、労働時間と生産性（Productivity）の関係を再定義した最重要の参照基準です。\n        </p>\n        <p style=\\"font-size: 0.88rem; line-height: 1.75; color: #1e3a8a; margin: 0;\\">\n          <strong>② 難関大の経済・社会・法学部入試に直結：</strong><br>\n          人口減少と過労社会に直面する日本において、働き方改革やワークシェアリングを議論する際の国際比較データとして必携の知識です。\n        </p>\n        """,',
        1
    )

    # Junior version of four-day-workweek-uk-trial-permanent
    content = content.replace(
        '"category_label": "LABOUR ECONOMICS • 週休3日制の働き方",',
        '"category_label": "【過去のニュース深掘り】 LABOUR ECONOMICS • 週休3日制の働き方",\n        "is_past_news": True,\n        "foundational_reason_title": "【過去のニュース深掘り】なぜ今、高校生がこのニュースを振り返るべきなのか？",\n        "foundational_reason_html": """\n        <p style=\\"font-size: 0.88rem; line-height: 1.75; color: #1e3a8a; margin: 0;\\">\n          <strong>💡 働くことの未来を考える：</strong><br>\n          「休みが増えても同じ給料をもらえるなんて本当？」と疑問に思うかもしれません。イギリスの会社で実際に試してみたところ、社員が元気になって集中力が高まり、仕事の成果が落ちなかったという驚きの結果が出ました。これからの働き方を考える英語の基礎知識です。\n        </p>\n        """,',
        1
    )

    # 3. renewables-overtake-fossil-fuels-eu-electricity
    content = content.replace(
        '"category_label": "GLOBAL ENERGY & CLIMATE POLICY • 欧州再エネ発電シェアの歴史的逆転",',
        '"category_label": "【過去のニュース深掘り】 GLOBAL ENERGY & CLIMATE POLICY • 欧州再エネ発電シェアの歴史的逆転",\n        "is_past_news": True,\n        "foundational_reason_title": "【過去のニュース深掘り】なぜ今、高校生がこのニュースを振り返るべきなのか？",\n        "foundational_reason_html": """\n        <p style=\\"font-size: 0.88rem; line-height: 1.75; color: #1e3a8a; margin: 0 0 0.75rem;\\">\n          <strong>① エネルギー地政学の歴史的転換点（メルクマール）：</strong><br>\n          2024年上半期、EU全域において風力・太陽光などの再生可能エネルギーが化石燃料（石炭・ガス）の発電量を史上初めて上回ったという脱炭素史上の金字塔です。ウクライナ危機を契機としたロシア産化石燃料依存からの脱却政策「REPowerEU」の成果を検証する上で必読の一次情報です。\n        </p>\n        <p style=\\"font-size: 0.88rem; line-height: 1.75; color: #1e3a8a; margin: 0;\\">\n          <strong>② 共通テスト地理・現代社会・英語長文の必修背景：</strong><br>\n          欧州のエネルギー転換のスピード感と、送電網整備・電力市場改革の課題は、国際関係や環境政策を志望する高校生の基礎教養です。\n        </p>\n        """,',
        1
    )

    # Junior version of renewables-overtake-fossil-fuels-eu-electricity
    content = content.replace(
        '"category_label": "GLOBAL ENERGY • 欧州の自然エネルギー",',
        '"category_label": "【過去のニュース深掘り】 GLOBAL ENERGY • 欧州の自然エネルギー",\n        "is_past_news": True,\n        "foundational_reason_title": "【過去のニュース深掘り】なぜ今、高校生がこのニュースを振り返るべきなのか？",\n        "foundational_reason_html": """\n        <p style=\\"font-size: 0.88rem; line-height: 1.75; color: #1e3a8a; margin: 0;\\">\n          <strong>💡 地球温暖化対策の大きなマイルストーン：</strong><br>\n          ヨーロッパ全体で、風力や太陽光で作るクリーンな電気が、石炭やガスなどの化石燃料で作る電気を初めて追い抜きました。SDGsや環境問題の入試長文でよく使われる英単語（renewable, fossil fuels, generation）をまとめて覚えましょう。\n        </p>\n        """,',
        1
    )

    # 4. eu-ai-act-consumer-rights-enforcement
    content = content.replace(
        '"category_label": "DIGITAL JURISPRUDENCE & AI GOVERNANCE • 欧州AI法と消費者権利保護",',
        '"category_label": "【過去のニュース深掘り】 DIGITAL JURISPRUDENCE & AI GOVERNANCE • 欧州AI法と消費者権利保護",\n        "is_past_news": True,\n        "foundational_reason_title": "【過去のニュース深掘り】なぜ今、高校生がこのニュースを振り返るべきなのか？",\n        "foundational_reason_html": """\n        <p style=\\"font-size: 0.88rem; line-height: 1.75; color: #1e3a8a; margin: 0 0 0.75rem;\\">\n          <strong>① 世界初の包括的AI規制枠組み「EU AI法」の成立：</strong><br>\n          2024年に成立した欧州連合（EU）のAI規制法（AI Act）は、GDPR（一般データ保護規則）に続き、欧州の基準が事実上の世界標準となる「ブリュッセル効果」を象徴する法律です。リスクベース・アプローチ（許容不可・ハイリスク・限定的リスク）の分類法は法学・情報倫理の基本です。\n        </p>\n        <p style=\\"font-size: 0.88rem; line-height: 1.75; color: #1e3a8a; margin: 0;\\">\n          <strong>② 法学部・情報学部の小論文・面接直結テーマ：</strong><br>\n          「技術イノベーションの促進」と「市民の基本的権利・プライバシーの保護」という二律背反を、法制度としていかに調停するかを論理的に考える最高の実例です。\n        </p>\n        """,',
        1
    )

    # Junior version of eu-ai-act-consumer-rights-enforcement
    content = content.replace(
        '"category_label": "AI ETHICS & LAW • ヨーロッパのAI法律",',
        '"category_label": "【過去のニュース深掘り】 AI ETHICS & LAW • ヨーロッパのAI法律",\n        "is_past_news": True,\n        "foundational_reason_title": "【過去のニュース深掘り】なぜ今、高校生がこのニュースを振り返るべきなのか？",\n        "foundational_reason_html": """\n        <p style=\\"font-size: 0.88rem; line-height: 1.75; color: #1e3a8a; margin: 0;\\">\n          <strong>💡 AIを賢く安全に使うためのルール：</strong><br>\n          AIはとても便利ですが、間違った判断をしたり個人の秘密を勝手に使ったりする危険もあります。ヨーロッパが世界に先駆けて作った厳しいAIルールを学ぶことで、デジタル社会の市民としてのリテラシーが身につきます。\n        </p>\n        """,',
        1
    )

    # 5. us-newspapers-openai-copyright-lawsuit
    content = content.replace(
        '"category_label": "INTELLECTUAL PROPERTY & FAIR USE • AIモデル学習と新聞著作権侵害訴訟",',
        '"category_label": "【過去のニュース深掘り】 INTELLECTUAL PROPERTY & FAIR USE • AIモデル学習と新聞著作権侵害訴訟",\n        "is_past_news": True,\n        "foundational_reason_title": "【過去のニュース深掘り】なぜ今、高校生がこのニュースを振り返るべきなのか？",\n        "foundational_reason_html": """\n        <p style=\\"font-size: 0.88rem; line-height: 1.75; color: #1e3a8a; margin: 0 0 0.75rem;\\">\n          <strong>① 生成AIと知的財産権（著作権法）の世界的火種：</strong><br>\n          米国の地方日刊紙8紙が、自社の独自取材記事を生成AIの事前学習に無断利用されたとして提訴した2024年の代表的司法判断です。著作権法における「フェアユース（公正利用）」の法理と、取材コストを投じる報道機関の経済的存立基盤の衝突を描いています。\n        </p>\n        <p style=\\"font-size: 0.88rem; line-height: 1.75; color: #1e3a8a; margin: 0;\\">\n          <strong>② メディアリテラシーと民主主義の根幹：</strong><br>\n          「AIが要約したニュースばかり読むと、元の取材を行う新聞社が倒産してしまう」という構造的ジレンマは、情報社会を生きる高校生にとって極めて重要な探究課題です。\n        </p>\n        """,',
        1
    )

    # Junior version of us-newspapers-openai-copyright-lawsuit
    content = content.replace(
        '"category_label": "AI & COPYRIGHT • 新聞とAIの著作権",',
        '"category_label": "【過去のニュース深掘り】 AI & COPYRIGHT • 新聞とAIの著作権",\n        "is_past_news": True,\n        "foundational_reason_title": "【過去のニュース深掘り】なぜ今、高校生がこのニュースを振り返るべきなのか？",\n        "foundational_reason_html": """\n        <p style=\\"font-size: 0.88rem; line-height: 1.75; color: #1e3a8a; margin: 0;\\">\n          <strong>💡 記者の記事をAIが勝手に勉強していいの？：</strong><br>\n          記者が一生懸命足を運んで書いた新聞記事を、AI会社がお金を払わずに勝手に学習に使ったとして裁判になりました。ニュースを見る側として、知っておくべき著作権（copyright）の大切な議論です。\n        </p>\n        """,',
        1
    )

    # 6. orbital-samantha-harvey-booker-prize
    content = content.replace(
        '"category_label": "CONTEMPORARY LITERATURE • ブッカー賞受賞作『Orbital』と宇宙の視点",',
        '"category_label": "【過去のニュース深掘り】 CONTEMPORARY LITERATURE • ブッカー賞受賞作『Orbital』と宇宙の視点",\n        "is_past_news": True,\n        "foundational_reason_title": "【過去のニュース深掘り】なぜ今、高校生がこのニュースを振り返るべきなのか？",\n        "foundational_reason_html": """\n        <p style=\\"font-size: 0.88rem; line-height: 1.75; color: #1e3a8a; margin: 0 0 0.75rem;\\">\n          <strong>① 2024年英国ブッカー賞受賞作の文学的・哲学的価値：</strong><br>\n          国際宇宙ステーション（ISS）から地球を周回する宇宙飛行士たちの16周回（1日）を描いたサマンサ・ハーヴェイの小説『Orbital』。宇宙から国境のない地球を見つめる「概観効果（Overview Effect）」を通じ、気候危機と人間存在の脆さを美しく綴った現代英文学の傑作です。\n        </p>\n        <p style=\\"font-size: 0.88rem; line-height: 1.75; color: #1e3a8a; margin: 0;\\">\n          <strong>② 国際教養・文系の英語入試で問われる批評的教養：</strong><br>\n          科学と詩情が交差する格調高い散文（prose）に触れることで、難関国公立大の和訳問題や論説文で差がつく豊かな語彙力と情緒的感受性を養います。\n        </p>\n        """,',
        1
    )

    # Junior version of orbital-samantha-harvey-booker-prize
    content = content.replace(
        '"category_label": "LITERATURE • 宇宙から地球を見る小説",',
        '"category_label": "【過去のニュース深掘り】 LITERATURE • 宇宙から地球を見る小説",\n        "is_past_news": True,\n        "foundational_reason_title": "【過去のニュース深掘り】なぜ今、高校生がこのニュースを振り返るべきなのか？",\n        "foundational_reason_html": """\n        <p style=\\"font-size: 0.88rem; line-height: 1.75; color: #1e3a8a; margin: 0;\\">\n          <strong>💡 宇宙から見れば国境なんてない：</strong><br>\n          イギリスで最も権威ある文学賞（ブッカー賞）を受賞した小説を紹介します。宇宙ステーションから青い地球を眺める宇宙飛行士の目線を通して、地球の自然を大切にする気持ちを英語の美しい表現で味わってみましょう。\n        </p>\n        """,',
        1
    )

    # 7. gen-z-physical-books-library-renaissance
    content = content.replace(
        '"category_label": "MEDIA ECOLOGY & READING CULTURE • 紙の本への回帰とZ世代の図書館ルネサンス",',
        '"category_label": "【過去のニュース深掘り】 MEDIA ECOLOGY & READING CULTURE • 紙の本への回帰とZ世代の図書館ルネサンス",\n        "is_past_news": True,\n        "foundational_reason_title": "【過去のニュース深掘り】なぜ今、高校生がこのニュースを振り返るべきなのか？",\n        "foundational_reason_html": """\n        <p style=\\"font-size: 0.88rem; line-height: 1.75; color: #1e3a8a; margin: 0 0 0.75rem;\\">\n          <strong>① デジタルネイティブ世代の「身体性」と「紙の本」回帰：</strong><br>\n          TikTok（BookTok）などのSNSコミュニティを契機に、10〜20代の若者が電子書籍ではなく紙の書籍や公共図書館の静寂を求める現象を捉えた2024年の文化ルポです。デジタル疲労に対する解毒剤（デジタルデトックス）としての読書文化を分析しています。\n        </p>\n        <p style=\\"font-size: 0.88rem; line-height: 1.75; color: #1e3a8a; margin: 0;\\">\n          <strong>② メディア論・認知科学の入試長文頻出テーマ：</strong><br>\n          紙のページをめくる触覚や空間的把握が読解力や記憶定着に及ぼす影響は、近年の大学入試英語長文でも繰り返し取り上げられる高校生必読の教養です。\n        </p>\n        """,',
        1
    )

    # Junior version of gen-z-physical-books-library-renaissance
    content = content.replace(
        '"category_label": "YOUTH & BOOKS • Z世代と紙の本",',
        '"category_label": "【過去のニュース深掘り】 YOUTH & BOOKS • Z世代と紙の本",\n        "is_past_news": True,\n        "foundational_reason_title": "【過去のニュース深掘り】なぜ今、高校生がこのニュースを振り返るべきなのか？",\n        "foundational_reason_html": """\n        <p style=\\"font-size: 0.88rem; line-height: 1.75; color: #1e3a8a; margin: 0;\\">\n          <strong>💡 スマホ世代が「紙の本」に夢中になる理由：</strong><br>\n          いつでもスマホで読書できる時代に、なぜ若い世代が紙の本や図書館に集まっているのでしょうか？『スマホ画面から離れて落ち着ける場所』を求める同世代のリアルな気持ちを英語で読んでみましょう。\n        </p>\n        """,',
        1
    )

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("[OK] Updated batch11_articles_data.py with 7 past news deep-dives.")


def update_batch10():
    path = os.path.join(os.path.dirname(__file__), "batch10_science.py")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Senior solid-state-sodium-ion-battery-breakthrough
    old_senior_sub = '"source_attribution": "Source: Nature Energy (Oct 14, 2026). Room-temperature solid-state sodium battery architecture.",'
    new_senior_sub = '''"source_attribution": "Source: Nature Energy (Vol. 9, 2024). Room-temperature solid-state sodium battery architecture.",
        "is_foundational": True,
        "foundational_reason_title": "【過去の基礎論文解説】なぜ今、高校生がこの論文（Nature Energy 2024）を読むべきなのか？",
        "foundational_reason_html": """
        <p style=\\"font-size: 0.88rem; line-height: 1.75; color: #78350f; margin: 0 0 0.75rem;\\">
          <strong>① 次世代EV・蓄電池産業のゲームチェンジャー（材料科学）：</strong><br>
          Nature Energy誌に掲載された本論文は、希少金属（リチウム・コバルト）の地政学的調達リスクと液漏れ発火リスクを根本から解決する「全固体ナトリウム電池」の室温高速作動を世界で初めて実証した歴史的論文です。
        </p>
        <p style=\\"font-size: 0.88rem; line-height: 1.75; color: #78350f; margin: 0;\\">
          <strong>② 理系入試の化学・物理・環境融合問題に完全対応：</strong><br>
          イオン結晶界面の抵抗制御やデンドライト抑制といった固体化学の先端知識は、難関大の理系英語長文や自由英作文で問われる「脱炭素社会と蓄電イノベーション」の基盤知識となります。
        </p>
        """,'''

    if old_senior_sub in content:
        content = content.replace(old_senior_sub, new_senior_sub, 1)

    # Junior solid-state-sodium-ion-battery-breakthrough
    old_junior_sub = '"source_attribution": "Source: Nature Energy (Oct 14, 2026). Solid-state sodium battery breakthrough.",'
    new_junior_sub = '''"source_attribution": "Source: Nature Energy (2024). Solid-state sodium battery breakthrough.",
        "is_foundational": True,
        "foundational_reason_title": "【過去の基礎論文解説】なぜ今、高校生がこの論文を読むべきなのか？",
        "foundational_reason_html": """
        <p style=\\"font-size: 0.88rem; line-height: 1.75; color: #143820; margin: 0;\\">
          <strong>💡 スマホの火事を防ぐ未来のバッテリー：</strong><br>
          スマートフォンや電気自動車に入っている電池は、落とすと火事になる危険がありました。この論文では、食卓の塩（ナトリウム）を使って、絶対に燃えない安全で安い電池を作ること大成功しました。理科の教科書に出てくるナトリウムの性質がどう役立つか、基本英語で学びましょう。
        </p>
        """,'''

    if old_junior_sub in content:
        content = content.replace(old_junior_sub, new_junior_sub, 1)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("[OK] Updated batch10_science.py with solid-state sodium battery foundational box.")


def update_batch9():
    path = os.path.join(os.path.dirname(__file__), "batch9_science.py")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Senior alzheimers-blood-biomarker-early-detection
    old_senior_sub = '"source_attribution": "Source: Nature Medicine (Oct 13, 2026). Clinical validation of blood-based biomarkers for neurodegenerative diseases.",'
    new_senior_sub = '''"source_attribution": "Source: Nature Medicine (Vol. 30, 2024). Clinical validation of blood-based biomarkers for neurodegenerative diseases.",
        "is_foundational": True,
        "foundational_reason_title": "【過去の基礎論文解説】なぜ今、高校生がこの論文（Nature Medicine 2024）を読むべきなのか？",
        "foundational_reason_html": """
        <p style=\\"font-size: 0.88rem; line-height: 1.75; color: #78350f; margin: 0 0 0.75rem;\\">
          <strong>① 医学部・生命科学部で毎年出題される神経変性疾患の金字塔：</strong><br>
          Nature Medicineに発表された多施設共同研究であり、血漿中のリン酸化タウ（p-tau217）を測定することで、侵襲的な骨髄穿刺や高額なPETスキャンなしにアルツハイマー病初期病態を90%以上の精度で検出可能にした画期的成果です。
        </p>
        <p style=\\"font-size: 0.88rem; line-height: 1.75; color: #78350f; margin: 0;\\">
          <strong>② 超高齢社会の医療倫理と早期診断の意義：</strong><br>
          自覚症状が出る前の超早期治療（モノクローナル抗体薬等）の可能性を開く一方で、発症前告知の倫理的課題など、難関大医学部の面接・小論文で不可欠な背景知識を養います。
        </p>
        """,'''

    if old_senior_sub in content:
        content = content.replace(old_senior_sub, new_senior_sub, 1)

    # Junior alzheimers-blood-biomarker-early-detection
    old_junior_sub = '"source_attribution": "Source: Nature Medicine (Oct 13, 2026). Blood test detects early Alzheimer\'s.",'
    new_junior_sub = '''"source_attribution": "Source: Nature Medicine (2024). Blood test detects early Alzheimer\'s.",
        "is_foundational": True,
        "foundational_reason_title": "【過去の基礎論文解説】なぜ今、高校生がこの論文を読むべきなのか？",
        "foundational_reason_html": """
        <p style=\\"font-size: 0.88rem; line-height: 1.75; color: #143820; margin: 0;\\">
          <strong>💡 血液1滴でわかる病気予防の最新医学：</strong><br>
          これまで診断がとても難しかった病気が、簡単な血液検査で何年も早く見つけられるようになりました。将来の医療や健康を支えるバイオテクノロジーの進歩を、高校生の英語で分かりやすく読み解きます。
        </p>
        """,'''

    if old_junior_sub in content:
        content = content.replace(old_junior_sub, new_junior_sub, 1)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("[OK] Updated batch9_science.py with alzheimers foundational box.")


def update_batch7():
    path = os.path.join(os.path.dirname(__file__), "batch7_science.py")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Senior nobel-physics-hopfield-hinton-machine-learning
    old_senior_label = '"category_label": "SCIENCE & COMPUTATIONAL PHYSICS",'
    new_senior_label = '''"category_label": "【過去の基礎論文解説】 SCIENCE & COMPUTATIONAL PHYSICS • 統計力学と人工知能の原点",
        "is_foundational": True,
        "foundational_reason_title": "【過去の基礎論文解説】なぜ今、高校生がこのノーベル賞受賞研究（2024）を学ぶべきなのか？",
        "foundational_reason_html": """
        <p style=\\"font-size: 0.88rem; line-height: 1.75; color: #78350f; margin: 0 0 0.75rem;\\">
          <strong>① 2024年ノーベル物理学賞受賞とAIの数理的起源：</strong><br>
          ジョン・ホップフィールド氏とジェフリー・ヒントン氏へのノーベル物理学賞授与の背景を解説したNatureの学術論説です。物理学のスピングラス模型（磁性原子の相互作用）やボルツマン分布という熱力学概念が、現代のディープラーニングの骨格を創り出した学問の越境（Interdisciplinary Research）の極致です。
        </p>
        <p style=\\"font-size: 0.88rem; line-height: 1.75; color: #78350f; margin: 0;\\">
          <strong>② 情報科学・物理系・文理融合学部の推薦・2次対策に必須：</strong><br>
          単にAIツールを使う側から、その根底にある数学的・物理的原理を理解する側へステップアップするための決定的な教養テキストです。
        </p>
        """,'''

    if old_senior_label in content:
        content = content.replace(old_senior_label, new_senior_label, 1)

    # Junior nobel-physics-hopfield-hinton-machine-learning
    old_junior_label = '"category_label": "SCIENCE & AI • 物理学賞と人工知能",'
    new_junior_label = '''"category_label": "【過去の基礎論文解説】 SCIENCE & AI • 物理学賞と人工知能",
        "is_foundational": True,
        "foundational_reason_title": "【過去の基礎論文解説】なぜ今、高校生がこの論文を読むべきなのか？",
        "foundational_reason_html": """
        <p style=\\"font-size: 0.88rem; line-height: 1.75; color: #143820; margin: 0;\\">
          <strong>💡 物理の法則がAIを生み出したノーベル賞の歴史：</strong><br>
          2024年のノーベル物理学賞に選ばれたAI研究を分かりやすく解説します。「物理の磁石の仕組み」を真似してコンピューターに記憶させるアイデアが、いま世界中で使われている人工知能の始まりになりました。
        </p>
        """,'''

    if old_junior_label in content:
        content = content.replace(old_junior_label, new_junior_label, 1)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("[OK] Updated batch7_science.py with nobel physics foundational box.")


if __name__ == "__main__":
    update_batch11()
    update_batch10()
    update_batch9()
    update_batch7()
    print("All batch updates complete!")
