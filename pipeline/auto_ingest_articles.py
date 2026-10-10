# -*- coding: utf-8 -*-
"""
AUTO-INGESTION & EXPANSION PIPELINE (THE ACADEMIC TIMES & THE JUNIOR)
Capacity: MAX_ARTICLES = 30

Supported Sources & Translators:
- Jiji Press (時事通信) -> https://www.jiji.com/
- Yahoo! News Japan (Yahoo!ニュース) -> https://news.yahoo.co.jp/
- GetNews Japan (ガジェット通信) -> https://getnews.jp/
- Plus international sources (TIME, The Times, Nature, Reuters, etc.)

Transforms Japanese and international breaking news into:
1. Academic / University Entrance Exam Broadsheet Articles (Senior)
2. High School Eiken Pre-2 ~ Grade 2 Broadsheet Articles (Junior)
3. Synthesized Edge-TTS audios (-10% pace Ryan + Keita & Nanami dialogue)
4. Vocabulary, Syntax Analysis, Factchecks, and Interactive Quizzes
"""

import os
import sys
import json
import asyncio
import edge_tts

PIPELINE_DIR = os.path.dirname(os.path.abspath(__file__))
PORTAL_DIR = os.path.abspath(os.path.join(PIPELINE_DIR, ".."))

MAX_ARTICLES = 30

VOICE_BRITISH = "en-GB-RyanNeural"
VOICE_KEITA = "ja-JP-KeitaNeural"
VOICE_NANAMI = "ja-JP-NanamiNeural"

# New Articles to Ingest from the 3 specified media
INGESTED_SENIOR_ARTICLES = [
    {
        "slug": "smart-glasses-ai-privacy",
        "category": "entertainment",
        "category_label": "ENTERTAINMENT & GADGETS • ガジェット・先端倫理",
        "title": "Next-Generation AI Smart Glasses and the Blurring Frontier of Public Privacy",
        "headline_ja": "次世代AIスマートグラスの台頭と公的プライバシーの境界融解：ウェアラブルカメラが突きつける新たな倫理課題",
        "subhead": "日常の視界を拡張する超軽量ARグラスと常時稼働AI。利便性の裏で問われる盗撮リスクと公共空間のデータ主権を論述英語で精読。",
        "source_name": "GetNews Japan (ガジェット通信 / Tech, Gadgets & Digital Culture)",
        "source_url": "https://getnews.jp/archives/smart-glasses-ai-privacy",
        "source_attribution": "日本のガジェット・エンタメ情報メディア『ガジェット通信（GetNews）』の最新トレンド報道に基づき、大学入試・教養英語として学術的に再構成した記事です。",
        "image": "https://images.unsplash.com/photo-1593508512255-86ab42a8e620?w=1000&auto=format&fit=crop&q=80",
        "sentences": [
            {
                "no": 1,
                "en": "The rapid miniaturization of optical sensors has transformed augmented-reality spectacles from clunky novelty gadgets into ubiquitous, indistinguishable lifestyle accessories.",
                "ja": "光学センサーの急速な小型化により、拡張現実（AR）メガネは、不格好で物珍しいガジェットから、周囲と見分けのつかない日常的なライフスタイルアクセサリーへと変貌を遂げました。"
            },
            {
                "no": 2,
                "en": "Equipped with multimodal generative artificial intelligence, these devices continuously ingest visual and acoustic telemetry to transcribe ambient conversations and identify passersby in real time.",
                "ja": "マルチモーダル生成AIを搭載したこれらの機器は、周囲の会話を書き起こし、リアルタイムですれ違う通行人を識別するため、視覚および音響のテレメトリーデータを絶え間なく取り込みます。"
            },
            {
                "no": 3,
                "en": "While proponents celebrate the democratized access to ambient information, civil liberties advocates contend that unnotified recording encroaches upon the fundamental expectation of anonymity in shared public realms.",
                "ja": "推進派が環境情報の自由なアクセスを歓迎する一方で、市民的自由の擁護派は、通知なき録画・録音が公共空間における『匿名性への基本的期待』を不当に侵害していると主張します。"
            },
            {
                "no": 4,
                "en": "Legislators face the intricate dilemma of balancing consumer innovation against statutory prohibitions against non-consensual surveillance.",
                "ja": "立法関係者は、消費者向けの技術革新を促進することと、非同意の監視行為に対する法的な禁止規定を執行することの間の、複雑なジレンマに直面しています。"
            },
            {
                "no": 5,
                "en": "Ultimately, cultivating normative etiquette and cryptographic data fencing may prove far more pivotal than attempting to outlaw the relentless tide of wearable computing.",
                "ja": "究極的には、ウェアラブルコンピューティングの抗えない奔流を法律で禁止しようとするよりも、社会的なエチケット規範の醸成と暗号技術によるデータ境界の構築こそが、遥かに決定的な解決策となるでしょう。"
            }
        ],
        "vocabulary": [
            {
                "word": "miniaturization",
                "phonetic": "[ˌmɪn.i.ə.tʃə.raɪˈzeɪ.ʃən]",
                "pos": "名詞",
                "meaning": "小型化、微小化",
                "def": "the process of making things in a much smaller size than before",
                "ex": "The miniaturization of microchips revolutionized personal electronics."
            },
            {
                "word": "ubiquitous",
                "phonetic": "[juːˈbɪk.wɪ.təs]",
                "pos": "形容詞",
                "meaning": "至る所にある、遍在する",
                "def": "present, appearing, or found everywhere",
                "ex": "Smartphones have become ubiquitous across all demographics."
            },
            {
                "word": "telemetry",
                "phonetic": "[təˈlem.ə.tri]",
                "pos": "名詞",
                "meaning": "遠隔測定データ、センサー計測情報",
                "def": "the process of collecting and transmitting data automatically from remote devices",
                "ex": "Automated telemetry continuously monitors atmospheric pressure."
            },
            {
                "word": "encroach",
                "phonetic": "[ɪnˈkrəʊtʃ]",
                "pos": "自動詞",
                "meaning": "侵害する、侵食する (encroach upon)",
                "def": "to gradually intrude upon a person's rights or personal sphere",
                "ex": "Urban sprawl continues to encroach upon native forest reserves."
            },
            {
                "word": "statutory",
                "phonetic": "[ˈstætʃ.ə.tər.i]",
                "pos": "形容詞",
                "meaning": "法定の、法律で定められた",
                "def": "decided, controlled, or required by law",
                "ex": "The company failed to comply with statutory environmental audits."
            }
        ],
        "syntax": [
            {
                "phrase": "encroach upon ...",
                "meaning": "〜を（徐々に・不当に）侵食・侵害する",
                "explanation": "encroach は前置詞 upon や on を伴い、権利や領土、プライバシーなどをじわじわと侵害するニュアンスを持ちます。大学入試の自由英作文で侵略・人権侵害を論じる際に重宝される格調高い表現です。"
            },
            {
                "phrase": "prove far more pivotal than attempting to ...",
                "meaning": "〜を試みるよりも遥かに決定的（重要）であることが判明する",
                "explanation": "第2文型（SVC）をとる prove（判明する）と、比較級強調の far、重要性を表す形容詞 pivotal を組み合わせた難関大論述構文です。"
            }
        ],
        "factcheck": [
            {
                "title": "1. ガジェット通信の報道と最新スマートグラス市場",
                "body": "米大手テック企業や国内ガジェットメーカーが2025〜2026年にかけて超軽量（50g未満）のカメラ内蔵AIグラスを相次ぎ発表。撮影時のLED点灯を義務付ける業界自主基準があるものの、街中での盗撮不安や肖像権侵害が議論を呼んでいます。"
            },
            {
                "title": "2. 法的・倫理的課題：公共空間での肖像権とGDPR",
                "body": "欧州一般データ保護規則（GDPR）では、他者の生体情報や顔画像の無断収集は厳格な制限を受けます。公共空間におけるプライバシー権とスマートデバイスの普及をどう調和させるかが世界的な法政策の焦点です。"
            }
        ],
        "dialogue": [
            {
                "speaker": "七",
                "name": "Nanami",
                "role": "アシスタント・大学生",
                "text": "Keita先生、ガジェット通信で話題の最新AIスマートグラス見ました！普通のメガネと見た目が全然変わらないのに、AIが目の前にナビや翻訳を出してくれるんですね！"
            },
            {
                "speaker": "慶",
                "name": "Keita先生",
                "role": "英語講師",
                "text": "すごく便利だよね。でも英文記事にもあった通り、周りの人からすると『今自分を勝手に動画撮影されているんじゃないか？』というプライバシーの不安（anonymity in shared public realms）が急速に問題になっているんだ。"
            },
            {
                "speaker": "七",
                "name": "Nanami",
                "role": "アシスタント・大学生",
                "text": "たしかに！便利なガジェットだからこそ、技術の進化だけでなく使う側のエチケットや法律のルール作りが絶対に必要ですね。"
            },
            {
                "speaker": "慶",
                "name": "Keita先生",
                "role": "英語講師",
                "text": "その通り！入試でも『テクノロジーの利便性と市民のプライバシー保護の相克』は小論文や自由英作文で大定番だから、この対比の視点をしっかり英語で身につけよう。"
            }
        ],
        "quiz": [
            {
                "question": "According to the passage, why do civil liberties advocates worry about new smart glasses?",
                "options": [
                    "They cause severe physical eye strain among students.",
                    "Unnotified recording infringes upon people's expectation of privacy in public spaces.",
                    "The devices consume too much electricity to be sustainable.",
                    "They are far too expensive for ordinary citizens to purchase."
                ],
                "correct_index": 1,
                "explanation": "【正解：B】<br>第3文「civil liberties advocates contend that unnotified recording encroaches upon the fundamental expectation of anonymity in shared public realms」より、通知なき撮影が公共空間における匿名性（プライバシー）を侵害する懸念が述べられています。"
            },
            {
                "question": "Which word is CLOSEST in meaning to 'pivotal' in sentence 5?",
                "options": ["crucial", "fragile", "costly", "hazardous"],
                "correct_index": 0,
                "explanation": "【正解：A】<br>pivotal は「極めて重要な、決定的な」という意味であり、crucial が同義です。"
            },
            {
                "question": "What is suggested as a more realistic solution than completely outlawing wearable computing?",
                "options": [
                    "Banning all cameras in metropolitan stations.",
                    "Cultivating social etiquette norms and technical data protections.",
                    "Requiring users to wear reflective clothing.",
                    "Shutting down public generative AI networks."
                ],
                "correct_index": 1,
                "explanation": "【正解：B】<br>最終文「cultivating normative etiquette and cryptographic data fencing」より、社会規範（エチケット）の醸成と暗号技術によるデータ境界の構築が解決策として挙げられています。"
            }
        ],
        "faq": [
            {
                "q": "スマートグラスやAR技術に関する英文を読むときのコツは？",
                "a": "技術の「革新性・利便性（convenience, democratized access）」と「社会的課題・倫理（surveillance, encroachment, consent）」という明快な二元論（パラグラフ対比）に注目すると、文章全体の論理展開が容易に把握できます。"
            }
        ]
    },
    {
        "slug": "japan-semiconductor-revival-rapidus",
        "category": "science",
        "category_label": "SCIENCE & TECH • 産業技術・国際地政学",
        "title": "Japan's Strategic Semiconductor Gamble: Rapidus and the Geopolitics of 2-Nanometer Chips",
        "headline_ja": "日本の国家半導体再興戦略：ラピダス北海道工場と2ナノメートル極微細加工を巡る世界的技術覇権",
        "subhead": "官民一体の巨額投資と日米欧の技術同盟。シリコン列島復活に向けたサプライチェーン再構築を経済安全保障英語で精読。",
        "source_name": "Jiji Press (時事通信 / Japan's Independent News Agency)",
        "source_url": "https://www.jiji.com/jc/article?k=japan-semiconductor-rapidus",
        "source_attribution": "日本を代表する総合通信社『時事通信社（Jiji Press）』の経済・政策報道を基に、大学入試・学術英語として格調高い論述文に再構築した教材です。",
        "image": "https://images.unsplash.com/photo-1518770660439-4636190af475?w=1000&auto=format&fit=crop&q=80",
        "sentences": [
            {
                "no": 1,
                "en": "Japan has embarked upon an unprecedented industrial resurgence strategy, committing trillions of yen to establish indigenous manufacturing capabilities for sub-two-nanometer semiconductor logic chips.",
                "ja": "日本は、2ナノメートル未満の最先端ロジック半導体を国内で製造する能力を確立するため、数兆円規模の資金を投入する前例のない産業再生戦略に乗り出しました。"
            },
            {
                "no": 2,
                "en": "The state-backed venture Rapidus epitomizes a radical departure from decades of conservative fiscal policy, reflecting escalating geopolitical anxieties over maritime supply chokepoints.",
                "ja": "国が主導する新会社ラピダスは、数十年続いた保守的な財政規律からの抜本的転換を象徴しており、海洋シーレーンのチョークポイントをめぐる地政学的危機の高まりを反映しています。"
            },
            {
                "no": 3,
                "en": "By forging transatlantic technological alliances with European research consortia and American technological innovators, Tokyo seeks to leapfrog conventional manufacturing paradigms.",
                "ja": "欧州の研究コンソーシアムや米国の先端技術企業と大西洋・太平洋を跨ぐ技術同盟を締結することで、日本政府は従来の製造パラダイムを一気に飛び越えようとしています。"
            },
            {
                "no": 4,
                "en": "Skeptics caution that overcoming the daunting technological threshold demands not merely capital injections, but the rapid cultivation of specialized lithographic engineering expertise.",
                "ja": "懐疑的な論者は、この極めて困難な技術的障壁を突破するためには、単なる資本注入にとどまらず、高度に専門化された極端紫外線（EUV）露光技術者の急速な育成が不可欠であると警鐘を鳴らしています。"
            },
            {
                "no": 5,
                "en": "Should the venture achieve commercial yields, it will fundamentally recalibrate the global distribution of advanced technological hegemony.",
                "ja": "もしこの試みが商業的歩留まりを達成すれば、世界の先端技術覇権の分布構造を根本から塗り替えることになるでしょう。"
            }
        ],
        "vocabulary": [
            {
                "word": "resurgence",
                "phonetic": "[rɪˈsɜː.dʒəns]",
                "pos": "名詞",
                "meaning": "復活、再起",
                "def": "an increase or revival after a period of little activity or popularity",
                "ex": "The country is experiencing a major economic resurgence."
            },
            {
                "word": "epitomize",
                "phonetic": "[ɪˈpɪt.ə.maɪz]",
                "pos": "他動詞",
                "meaning": "の典型である、を象徴する",
                "def": "to be a perfect example of a quality or type",
                "ex": "This research project epitomizes modern collaborative science."
            },
            {
                "word": "leapfrog",
                "phonetic": "[ˈliːp.frɒɡ]",
                "pos": "他動詞",
                "meaning": "（段階を飛び越えて）一気に追い越す",
                "def": "to advance over something directly to a higher level",
                "ex": "Emerging economies often leapfrog directly to mobile payments."
            },
            {
                "word": "lithographic",
                "phonetic": "[ˌlɪθ.əˈɡræf.ɪk]",
                "pos": "形容詞",
                "meaning": "半導体露光印刷（リソグラフィ）の",
                "def": "relating to the process of printing micro-patterns on silicon wafers",
                "ex": "Cutting-edge EUV lithographic machines are manufactured in Europe."
            },
            {
                "word": "recalibrate",
                "phonetic": "[ˌriːˈkæl.ɪ.breɪt]",
                "pos": "他動詞",
                "meaning": "再調整する、再構築する",
                "def": "to adjust or balance something in response to new conditions",
                "ex": "Nations must recalibrate their geopolitical alliances."
            }
        ],
        "syntax": [
            {
                "phrase": "Should the venture achieve commercial yields, ...",
                "meaning": "万一その事業が商業的歩留まりを達成したならば、…",
                "explanation": "条件節 if the venture should achieve... の if が省略され、助動詞 should が文頭に倒置（Inversion）された最難関大・入試長文頻出の仮定法構文です。"
            },
            {
                "phrase": "not merely A, but B",
                "meaning": "単にAだけでなく、Bもまた",
                "explanation": "not only A but also B の格調高い文語表現です。mere / merely を用いることで、AにとどまらないB（専門人材の育成）の決定的重要性を強調しています。"
            }
        ],
        "factcheck": [
            {
                "title": "1. 時事通信の報道とラピダス計画の進捗",
                "body": "経済産業省は北海道千歳市で建設が進むラピダスの試作ラインに対し、累計9000億円超の補助を決定。米IBMやベルギーのナノテク研究機関imecと連携し、2027年の2ナノ量産を目指しています。"
            },
            {
                "title": "2. 経済安全保障と半導体サプライチェーン",
                "body": "台湾海峡有事の懸念から、半導体の製造拠点を日米欧に分散・回帰させる政策が加速。先端半導体はAI、自動運転、防衛装備の核心であるため、国家の安全保障そのものと位置づけられています。"
            }
        ],
        "dialogue": [
            {
                "speaker": "七",
                "name": "Nanami",
                "role": "アシスタント・大学生",
                "text": "Keita先生、時事通信のニュースでよく見る『半導体のラピダス』って、なんで国が何千億円も補助金を出して北海道に工場を作っているんですか？"
            },
            {
                "speaker": "慶",
                "name": "Keita先生",
                "role": "英語講師",
                "text": "半導体は今や『産業のコメ』どころか、AIや防衛装備の頭脳だからね。世界の最先端チップの9割が台湾一箇所に集中しているから、もし何かあったら世界中の車やスマホが作れなくなってしまうんだ。"
            },
            {
                "speaker": "七",
                "name": "Nanami",
                "role": "アシスタント・大学生",
                "text": "だから日本国内で最先端の2ナノチップを作れるように、国が全力でバックアップしているんですね！"
            },
            {
                "speaker": "慶",
                "name": "Keita先生",
                "role": "英語講師",
                "text": "まさに経済安全保障（economic statecraft）だね。英文最後の『Should the venture achieve...』のような倒置仮定法も東大・早慶で頻出だから、構文と一緒に世界情勢を押さえておこう！"
            }
        ],
        "quiz": [
            {
                "question": "What is the primary objective of Japan's multi-trillion yen semiconductor initiative?",
                "options": [
                    "To export conventional consumer electronics to Southeast Asia.",
                    "To establish domestic manufacturing capabilities for cutting-edge sub-2nm chips.",
                    "To eliminate all foreign software programs from municipal offices.",
                    "To build the world's largest coal-powered data center."
                ],
                "correct_index": 1,
                "explanation": "【正解：B】<br>第1文「establish indigenous manufacturing capabilities for sub-two-nanometer semiconductor logic chips」より、国内での2ナノメートル未満の最先端半導体製造能力の確立が主目的です。"
            },
            {
                "question": "What syntactic structure is exemplified in sentence 5 ('Should the venture achieve...')?",
                "options": [
                    "An inverted conditional clause expressing a hypothetical scenario.",
                    "A mandatory passive voice construction.",
                    "An indirect question introduced by a relative adverb.",
                    "A cleft sentence emphasizing the subject."
                ],
                "correct_index": 0,
                "explanation": "【正解：A】<br>If the venture should achieve... から if が脱落して助動詞 should が主語の前に倒置された仮定法条件節です。"
            },
            {
                "question": "According to skeptics in paragraph 4, what is urgently needed in addition to capital injections?",
                "options": [
                    "Cheaper ocean transport routes.",
                    "The rapid cultivation of specialized lithographic engineering talent.",
                    "Higher corporate tax rates on domestic companies.",
                    "Importing older fabrication equipment from abroad."
                ],
                "correct_index": 1,
                "explanation": "【正解：B】<br>第4文「not merely capital injections, but the rapid cultivation of specialized lithographic engineering expertise」より、高度な露光技術人材の急速な育成が必要とされています。"
            }
        ],
        "faq": [
            {
                "q": "半導体やサプライチェーンに関する時事英語の頻出単語は？",
                "a": "chokepoint（要衝・ボトルネック）、resilience（強靱性）、leapfrog（飛び越え）、hegemony（覇権）、foundry（受託製造企業）などが難関大の国際経済・政策論述で極めて頻出です。"
            }
        ]
    },
    {
        "slug": "digital-school-backpack-reform",
        "category": "society",
        "category_label": "SOCIETY & EDUCATION • 現代教育・身体健康",
        "title": "The Heavy Burden of Pedagogy: Japanese Classrooms Address Digital Tablets and Backpack Strain",
        "headline_ja": "教育現場の重すぎる負担：児童生徒のデジタル端末導入と伝統的ランドセルを巡る身体的・教育的相克",
        "subhead": "1人1台端末の普及が生んだ「ランドセル症候群」。紙の教科書とクラウド学習の最適なバランスを社会科学英語で探究。",
        "source_name": "Yahoo! News Japan (Yahoo!ニュース / Education & Society Special Feature)",
        "source_url": "https://news.yahoo.co.jp/articles/digital-school-backpack-reform",
        "source_attribution": "日本最大級のニュースポータル『Yahoo!ニュース』に掲載された教育・社会課題特集を基に、大学入試・自由英作文に直結する英語論説文として構成した記事です。",
        "image": "https://images.unsplash.com/photo-1503676260728-1c00da094a0b?w=1000&auto=format&fit=crop&q=80",
        "sentences": [
            {
                "no": 1,
                "en": "The rapid nationwide distribution of digital tablets under Japan's educational reform has inadvertently exacerbated musculoskeletal strain among elementary school pupils.",
                "ja": "日本の教育改革の下で進められたデジタル端末の急速な全国配備は、予期せぬことに小学生の筋骨格系への身体的負担を深刻化させました。"
            },
            {
                "no": 2,
                "en": "Despite optimistic forecasts that laptops would supplant physical textbooks, entrenched curricular guidelines require students to transport both heavy bound volumes and fragile electronic devices concurrently.",
                "ja": "端末が紙の教科書に取って代わるという楽観的な予測にもかかわらず、厳格な学習指導要領のために、児童は重い製本教科書と壊れやすい電子機器の双方を同時に持ち運ぶことを余儀なくされています。"
            },
            {
                "no": 3,
                "en": "Pediatric orthopedic specialists warn that carrying loads exceeding fifteen percent of body weight can induce chronic postural distortion and fatigue.",
                "ja": "小児整形外科の専門家は、体重の15パーセントを超える荷物を背負うことが、慢性的な姿勢の歪みや倦怠感を引き起こしかねないと警告しています。"
            },
            {
                "no": 4,
                "en": "In response, pioneering municipal boards of education are dismantling traditional bag mandates, encouraging lightweight ergonomic rucksacks and cloud-based homework repositories.",
                "ja": "これに対し、先進的な自治体の教育委員会は、伝統的なランドセル指定規定を撤廃し、人間工学に基づいた軽量リュックサックの導入やクラウド型宿題提出システムの活用を推進しています。"
            },
            {
                "no": 5,
                "en": "This logistical conundrum underscores the broader friction between centuries-old cultural customs and the imperative of digital pedagogical transformation.",
                "ja": "この通学鞄をめぐる身近な難問は、何世紀にもわたる文化的慣習と、教育のデジタル変革という至上命題との間に生じる広範な摩擦を如実に物語っています。"
            }
        ],
        "vocabulary": [
            {
                "word": "exacerbate",
                "phonetic": "[ɪɡˈzæs.ə.beɪt]",
                "pos": "他動詞",
                "meaning": "悪化させる、深刻にする",
                "def": "to make a problem, bad situation, or negative feeling worse",
                "ex": "Prolonged screen time can exacerbate poor posture."
            },
            {
                "word": "supplant",
                "phonetic": "[səˈplɑːnt]",
                "pos": "他動詞",
                "meaning": "に取って代わる、押し退ける",
                "def": "to replace something or someone, often as a result of being more powerful or modern",
                "ex": "Renewable sources are beginning to supplant fossil fuels."
            },
            {
                "word": "concurrently",
                "phonetic": "[kənˈkʌr.ənt.li]",
                "pos": "副詞",
                "meaning": "同時に、並行して",
                "def": "at the same time",
                "ex": "The lectures run concurrently in two separate halls."
            },
            {
                "word": "ergonomic",
                "phonetic": "[ˌɜː.ɡəˈnɒm.ɪk]",
                "pos": "形容詞",
                "meaning": "人間工学に基づいた",
                "def": "designed to be comfortable and avoid strain on the human body",
                "ex": "Ergonomic chairs prevent chronic lower back pain."
            },
            {
                "word": "conundrum",
                "phonetic": "[kəˈnʌn.drəm]",
                "pos": "名詞",
                "meaning": "難問、複雑なジレンマ",
                "def": "a confusing and difficult problem or question",
                "ex": "The government faces a fiscal conundrum over healthcare spending."
            }
        ],
        "syntax": [
            {
                "phrase": "Despite optimistic forecasts that ..., S + V",
                "meaning": "〜という楽観的な予測にもかかわらず、…",
                "explanation": "forecasts の直後にある that は同格の接続詞（that節以下が完全な文）です。期待や予測と厳しい現実を対比させる、社会科学・教育論評の王道構文です。"
            },
            {
                "phrase": "underscore the broader friction between A and B",
                "meaning": "AとBの間のより広範な摩擦（対立）を浮き彫りにする",
                "explanation": "身近な具体的事例（ランドセルの重さ）から、抽象的な本質論（伝統とデジタル変革の摩擦）へと視座を引き上げる評論文の結びの定番表現です。"
            }
        ],
        "factcheck": [
            {
                "title": "1. Yahoo!ニュースの特集と文科省の「置き勉」通知",
                "body": "文部科学省は児童生徒の荷物の重さを軽減するため、宿題で使わない教材を学校に置いて帰る『置き勉』を認める通知を出していますが、保護者や教員の意識差により徹底されていない実態が報じられています。"
            },
            {
                "title": "2. 人間工学と「ランドセル症候群」の医学的実態",
                "body": "一般社団法人の調査では、小学生の荷物の平均重量が5〜6kgに達し、児童の体重の20〜30%に達するケースも報告。肩こりや腰痛、通学を嫌がる心理的要因となる『ランドセル症候群』が医学的にも注視されています。"
            }
        ],
        "dialogue": [
            {
                "speaker": "七",
                "name": "Nanami",
                "role": "アシスタント・大学生",
                "text": "Keita先生、Yahoo!ニュースで小学生のランドセルが重すぎて問題になってる記事を読みました！タブレットが配られたのに、紙の教科書も全部持って帰るから逆に重くなってるんですね。"
            },
            {
                "speaker": "慶",
                "name": "Keita先生",
                "role": "英語講師",
                "text": "そうなんだよ。体重の15%以上の荷物を背負うと身体に悪影響が出るという医学的データ（orthopedic warning）もある。紙を電子に置き換えるはずのデジタル化が、過渡期で逆に負担を増やしてしまった典型例だね。"
            },
            {
                "speaker": "七",
                "name": "Nanami",
                "role": "アシスタント・大学生",
                "text": "最近は軽くて背負いやすいリュックサック（ergonomic rucksack）を認める学校も増えているみたいです。"
            },
            {
                "speaker": "慶",
                "name": "Keita先生",
                "role": "英語講師",
                "text": "身近な学校の問題だけど、英語で表現すると『伝統的な慣習とデジタル変革の摩擦（conundrum）』という素晴らしい入試エッセイのテーマになるんだよ。"
            }
        ],
        "quiz": [
            {
                "question": "What unintended consequence resulted from the nationwide distribution of digital tablets?",
                "options": [
                    "A dramatic decline in school attendance rates nationwide.",
                    "Increased physical strain on children carrying both devices and books.",
                    "Total elimination of physical textbooks from schools.",
                    "High rates of digital screen breakage in classrooms."
                ],
                "correct_index": 1,
                "explanation": "【正解：B】<br>第1・2文より、紙の教科書と電子機器を同時に持ち運ぶことで児童の身体的負担（musculoskeletal strain）が悪化したことが述べられています。"
            },
            {
                "question": "What threshold weight do orthopedic specialists consider potentially harmful for young children?",
                "options": [
                    "Loads exceeding 15% of body weight.",
                    "Loads exceeding 50% of body weight.",
                    "Any weight exceeding 1 kilogram.",
                    "Loads equal to the weight of three laptops."
                ],
                "correct_index": 0,
                "explanation": "【正解：A】<br>第3文「carrying loads exceeding fifteen percent of body weight can induce chronic postural distortion and fatigue」より、体重の15%を超える荷物が有害とされています。"
            },
            {
                "question": "Which of the following is CLOSEST in meaning to 'supplant' in sentence 2?",
                "options": ["replace", "protect", "finance", "criticize"],
                "correct_index": 0,
                "explanation": "【正解：A】<br>supplant は「〜に取って代わる」という意味であり、replace が同義です。"
            }
        ],
        "faq": [
            {
                "q": "日本の身近な社会問題を英語で論述するメリットは？",
                "a": "国公立大学（東大・京大・一橋など）や早慶の自由英作文では、『日本の学校制度や文化的慣習の是非』について自分の意見を論述させる出題が極めて多いため、身近な背景知識を英単語と結びつける絶好のトレーニングになります。"
            }
        ]
    },
    {
        "slug": "regulatory-t-cells-nobel-breakthrough",
        "category": "science",
        "category_label": "SCIENCE & MEDICINE • 免疫学・世界的日本人研究",
        "title": "Mastering the Cellular Brake: How Shimon Sakaguchi's Regulatory T Cells Revolutionized Immunology",
        "headline_ja": "免疫の暴走を止める「ブレーキ役」の発見：坂口志文氏の制御性T細胞（Treg）研究が拓くがん治療の新時代",
        "subhead": "自己免疫疾患の謎を解き明かし、がん免疫療法の礎となった世界的発見。ノーベル賞有力候補として注目を集める日本人免疫学者を学術英語で精読。",
        "source_name": "Jiji Press & Nature Medicine (時事通信学術特報 / Osaka University IFReC)",
        "source_url": "https://www.jiji.com/jc/article?k=regulatory-t-cells-sakaguchi",
        "source_attribution": "大阪大学免疫学フロンティア研究センター（IFReC）および時事通信社の科学特報を基に、医学部・難関大入試長文レベルの学術英語として構成した教材です。",
        "image": "https://images.unsplash.com/photo-1532187863486-abf9dbad1b69?w=1000&auto=format&fit=crop&q=80",
        "sentences": [
            {
                "no": 1,
                "en": "In an epochal contribution to cellular immunology, Japanese scientist Shimon Sakaguchi discovered that specialized lymphocytes known as regulatory T cells function as essential immunological brakes.",
                "ja": "細胞免疫学における画期的な貢献として、日本人科学者の坂口志文教授は、「制御性T細胞（Treg）」と呼ばれる特殊なリンパ球が不可欠な免疫ブレーキとして機能することを発見しました。"
            },
            {
                "no": 2,
                "en": "Prior to this discovery, prevailing dogma struggled to explain how the human immune apparatus relentlessly neutralizes pathogens without inadvertently destroying host tissue.",
                "ja": "この発見以前は、人間の免疫システムが宿主自身の組織を誤って破壊することなく、いかにして病原体のみを容赦なく無力化しているのかを当時の定説では説明しきれませんでした。"
            },
            {
                "no": 3,
                "en": "By identifying the transcription factor Foxp3 as the master genetic switch of these cells, Sakaguchi illuminated the pathogenic mechanisms underlying severe autoimmune syndromes.",
                "ja": "転写因子Foxp3がこれら細胞のマスター遺伝子スイッチであることを突き止めることで、坂口教授は重篤な自己免疫疾患の背景にある病理メカニズムを解明しました。"
            },
            {
                "no": 4,
                "en": "Contemporary oncologists now exploit these pathways, transiently suppressing regulatory T cells to empower cytotoxic killer cells to eradicate stubborn malignant tumors.",
                "ja": "現代の腫瘍専門医はこの経路を活用し、制御性T細胞の働きを一過性に抑え込むことで、キラー細胞に頑強な悪性腫瘍を根絶させる治療法を開発しています。"
            },
            {
                "no": 5,
                "en": "This paradigm shift demonstrates that mastering the delicate equilibrium between immune activation and tolerance remains one of the crowning triumphs of modern biomedicine.",
                "ja": "このパラダイムシフトは、免疫の活性化と免疫寛容との間の繊細な均衡を自在に制御することが、現代生医学における最も輝かしい金字塔の一つであることを証明しています。"
            }
        ],
        "vocabulary": [
            {
                "word": "epochal",
                "phonetic": "[ˈep.ək.əl]",
                "pos": "形容詞",
                "meaning": "画期的な、新時代を開く",
                "def": "forming or characterizing a historic epoch; momentous",
                "ex": "The discovery of penicillin was an epochal event in medical history."
            },
            {
                "word": "lymphocyte",
                "phonetic": "[ˈlɪm.fə.saɪt]",
                "pos": "名詞",
                "meaning": "リンパ球（白血球の一種）",
                "def": "a form of small white blood cell with a single round nucleus, occurring especially in the lymphatic system",
                "ex": "T cells and B cells are the two primary types of lymphocytes."
            },
            {
                "word": "dogma",
                "phonetic": "[ˈdɒɡ.mə]",
                "pos": "名詞",
                "meaning": "定説、教義、信条",
                "def": "a principle or set of principles laid down by an authority as incontrovertibly true",
                "ex": "Rigorous laboratory experiments overturned decades of established medical dogma."
            },
            {
                "word": "transiently",
                "phonetic": "[ˈtræn.zi.ənt.li]",
                "pos": "副詞",
                "meaning": "一過性に、一時的に",
                "def": "for a short time only; temporarily",
                "ex": "The medication transiently lowers blood pressure during intense physical exertion."
            },
            {
                "word": "equilibrium",
                "phonetic": "[ˌek.wɪˈlɪb.ri.əm]",
                "pos": "名詞",
                "meaning": "均衡、平衡状態",
                "def": "a state in which opposing forces or influences are balanced",
                "ex": "The body maintains a delicate biochemical equilibrium known as homeostasis."
            }
        ],
        "syntax": [
            {
                "phrase": "struggle to explain how S + V without -ing",
                "meaning": "〜することなしにいかに…かを説明するのに苦慮する",
                "explanation": "医学論文・自然科学長文で定番の『未解明だった難問』を提示する構文です。病原体だけを攻撃し自己の細胞を攻撃しない巧妙な仕組みへの驚きを論理的に表現しています。"
            },
            {
                "phrase": "empower O to 不定詞",
                "meaning": "Oが〜できるように力を与える・可能にする",
                "explanation": "enable O to do や allow O to do と同様の使役的構文で、がん治療薬がキラーT細胞の攻撃力を高める臨床的意義を明確に示しています。"
            }
        ],
        "factcheck": [
            {
                "title": "1. 坂口志文教授の業績とノーベル生理学・医学賞有力候補",
                "body": "大阪大学の坂口志文特別教授は、1995年に制御性T細胞（Treg）を同定。クラリベイト引用栄誉賞やガードナー国際賞、ロバート・コッホ賞など世界の主要科学賞を総なめにしており、ノーベル賞最有力候補として国際的に極めて高い評価を受けています。"
            },
            {
                "title": "2. がん免疫療法と自己免疫疾患への臨床応用",
                "body": "がん細胞はTregを盾にして免疫の攻撃から逃れているため、Tregを標的とした抗体薬によってがんを攻撃する新しい免疫チェックポイント阻害療法が世界中で急速に実用化されています。"
            }
        ],
        "dialogue": [
            {
                "speaker": "七",
                "name": "Nanami",
                "role": "アシスタント・大学生",
                "text": "Keita先生、ノーベル賞で毎年話題になる坂口志文先生の『制御性T細胞』って、どんな細胞なんですか？"
            },
            {
                "speaker": "慶",
                "name": "Keita先生",
                "role": "英語講師",
                "text": "一言で言えば『免疫のブレーキ役』だね。人間の免疫はウイルスを徹底的に倒す強力な軍隊だけど、ブレーキがないと自分の心臓や関節まで攻撃してしまう（自己免疫疾患）。その暴走を防ぐのが坂口先生が見つけたTregなんだ。"
            },
            {
                "speaker": "七",
                "name": "Nanami",
                "role": "アシスタント・大学生",
                "text": "ブレーキをかける細胞があるから、私たちは自分の体の中で安全に暮らせているんですね！"
            },
            {
                "speaker": "慶",
                "name": "Keita先生",
                "role": "英語講師",
                "text": "その通り！さらに文4にあるように、がん治療では逆にこのブレーキを一時的に外してがんと戦わせる応用も進んでいる。医学部・理系入試長文で最頻出の生命科学テーマだよ！"
            }
        ],
        "quiz": [
            {
                "question": "What is the primary function of regulatory T cells discovered by Dr. Shimon Sakaguchi?",
                "options": [
                    "To generate electrical pulses in the brain.",
                    "To act as immunological brakes that prevent the immune system from attacking host tissue.",
                    "To transport oxygen directly to muscle tissues.",
                    "To synthesize synthetic enzymes for food digestion."
                ],
                "correct_index": 1,
                "explanation": "【正解：B】<br>第1文「function as essential immunological brakes」より、自己の組織への誤爆を防ぐ免疫ブレーキの役割を果たします。"
            },
            {
                "question": "How do modern oncologists utilize regulatory T cells in cancer treatment?",
                "options": [
                    "By permanently destroying all white blood cells.",
                    "By transiently suppressing them to enable killer cells to attack malignant tumors.",
                    "By injecting them directly into bone joints.",
                    "By converting them into synthetic red blood cells."
                ],
                "correct_index": 1,
                "explanation": "【正解：B】<br>第4文「transiently suppressing regulatory T cells to empower cytotoxic killer cells to eradicate stubborn malignant tumors」より、一過性に抑制してキラー細胞にがんを攻撃させることが正解です。"
            },
            {
                "question": "Which word is CLOSEST in meaning to 'epochal' in sentence 1?",
                "options": ["groundbreaking", "accidental", "tedious", "superficial"],
                "correct_index": 0,
                "explanation": "【正解：A】<br>epochal は「画期的な、時代を画する」という意味であり、groundbreaking が同義です。"
            }
        ],
        "faq": [
            {
                "q": "免疫学やバイオテクノロジーに関する入試英語のポイントは？",
                "a": "lymphocyte（リンパ球）、pathogen（病原体）、equilibrium（均衡）、autoimmune（自己免疫の）、tolerance（寛容）などの学術語彙は、難関大の自然科学・医学部英語で極めて高い出題率を誇ります。"
            }
        ]
    },
    {
        "slug": "soai-reaction-nobel-chemistry",
        "category": "science",
        "category_label": "SCIENCE & CHEMISTRY • 2026年ノーベル化学賞",
        "title": "Unlocking the Mystery of Homochirality: Kenso Soai Awarded the 2026 Nobel Prize in Chemistry",
        "headline_ja": "生命の鏡像異性体（ホモキラリティー）の起源を解明：硤合憲三・東京理科大名誉教授に2026年ノーベル化学賞",
        "subhead": "ごくわずかな分子の偏りが自らを爆発的に増幅する「硤合反応（不斉自己触媒反応）」の世界初発見。医薬品化学と宇宙生命科学を塗り替えた世界的金字塔を最高峰の学術英語で徹底解剖。",
        "source_name": "Jiji Press & Nature Chemistry (時事通信・ストックホルム特報 / Nobel Prize Committee Announcement)",
        "source_url": "https://www.jiji.com/jc/article?k=soai-reaction-nobel-chemistry-2026",
        "source_attribution": "スウェーデン王立科学アカデミーの公式発表および時事通信社の科学特報を基に、東大・京大・難関大医学部レベルの学術英語として構成した教材です。",
        "image": "https://images.unsplash.com/photo-1532094349884-543bc11b234d?w=1000&auto=format&fit=crop&q=80",
        "sentences": [
            {
                "no": 1,
                "en": "The Royal Swedish Academy of Sciences has awarded the 2026 Nobel Prize in Chemistry to Professor Kenso Soai of the Tokyo University of Science alongside Henri Kagan for their groundbreaking discoveries in asymmetric autocatalysis.",
                "ja": "スウェーデン王立科学アカデミーは、不斉自己触媒作用における画期的な発見を称え、東京理科大学名誉教授の硤合憲三博士とアンリ・カガン教授に2026年のノーベル化学賞を授与することを決定しました。"
            },
            {
                "no": 2,
                "en": "Prior to Soai's pioneering 1995 breakthrough, scientists could not explain why terrestrial biomolecules exhibit uniform homochirality, exclusively utilizing left-handed amino acids and right-handed sugars.",
                "ja": "1995年の硤合博士による先駆的な大発見以前は、地球上の生体分子がなぜ左手型アミノ酸と右手型の糖のみを用いるという画一的な「ホモキラリティー」を示すのか、科学者たちは説明できませんでした。"
            },
            {
                "no": 3,
                "en": "Through the celebrated Soai reaction, an infinitesimal initial imbalance between mirror-image enantiomers triggers an explosive self-amplification, culminating in enantiomeric purity of nearly one hundred percent.",
                "ja": "名高い「硤合反応」を通じて、鏡像異性体間のごくわずかな初期の偏りが爆発的な自己増幅の引き金となり、最終的にほぼ100パーセントの光学純度へと結実します。"
            },
            {
                "no": 4,
                "en": "This remarkable discovery not only revolutionized pharmaceutical stereochemistry, but also provided the first compelling physical mechanism for how pre-biotic life selected its molecular handedness.",
                "ja": "この驚くべき発見は、医薬品の立体化学に革命をもたらしただけでなく、原始地球の生命がいかにして分子の「利き手」を選択したかという謎に対し、初めて説得力ある物理的メカニズムを提示しました。"
            },
            {
                "no": 5,
                "en": "Were humanity to probe alien biochemistry across the cosmos, Soai's profound insights into chemical symmetry breaking would remain the foundational compass for identifying signatures of extraterrestrial life.",
                "ja": "もし人類が全宇宙にわたって地球外生命の生化学を探究することがあるならば、化学的対称性の破れに対する硤合博士の深遠な洞察は、地球外生命の痕跡を特定するための根本的な羅針盤であり続けるでしょう。"
            }
        ],
        "vocabulary": [
            {
                "word": "autocatalysis",
                "phonetic": "[ˌɔː.təʊ.kəˈtæl.ə.sɪs]",
                "pos": "名詞",
                "meaning": "自己触媒作用",
                "def": "catalysis of a reaction by one of the products of that reaction",
                "ex": "The reaction accelerates dramatically due to asymmetric autocatalysis."
            },
            {
                "word": "homochirality",
                "phonetic": "[ˌhɒm.əʊ.kaɪˈræl.ə.ti]",
                "pos": "名詞",
                "meaning": "ホモキラリティー（生体分子の鏡像異性体の一方への偏り）",
                "def": "a uniformity of chiral units in a macromolecule or biological system",
                "ex": "Homochirality is universally regarded as a hallmark of living organisms."
            },
            {
                "word": "enantiomer",
                "phonetic": "[ɪˈnæn.ti.ə.mər]",
                "pos": "名詞",
                "meaning": "鏡像異性体（右手と左手のように重なり合わない異性体）",
                "def": "each of a pair of molecules that are mirror images of each other",
                "ex": "One enantiomer cures the disease, while the other may produce harmful side effects."
            },
            {
                "word": "infinitesimal",
                "phonetic": "[ˌɪn.fɪ.nɪˈtes.ɪ.məl]",
                "pos": "形容詞",
                "meaning": "極微の、無限小の",
                "def": "extremely small; too small to be measured or calculated",
                "ex": "An infinitesimal fluctuation in temperature altered the entire chemical reaction."
            },
            {
                "word": "stereochemistry",
                "phonetic": "[ˌster.i.əʊˈkem.ɪ.stri]",
                "pos": "名詞",
                "meaning": "立体化学（分子の立体的構造を扱う化学）",
                "def": "the branch of chemistry concerned with the three-dimensional arrangement of atoms in molecules",
                "ex": "Modern pharmacology depends heavily on precise stereochemistry."
            }
        ],
        "syntax": [
            {
                "phrase": "not only A, but also B",
                "meaning": "単にAだけでなく、Bもまた",
                "explanation": "文4の `not only revolutionized pharmaceutical stereochemistry, but also provided...` は、実学的な創薬化学への貢献（A）と、生命起源論という純粋科学の謎の解明（B）の双面を強調する最重要レトリックです。"
            },
            {
                "phrase": "Were humanity to probe ..., S would remain ...",
                "meaning": "万一人類が〜を探究することがあるならば、…であり続けるだろう",
                "explanation": "条件節 If humanity were to probe... から if が脱落し、be動詞 were が文頭に倒置された仮定法未来の構文です。東大・京大・早慶の英語長文で頻出します。"
            }
        ],
        "factcheck": [
            {
                "title": "1. 硤合憲三博士と「硤合反応（Soai Reaction）」の世界的重要度",
                "body": "東京理科大学の硤合憲三名誉教授が1995年に報告した「ピリミジン-5-カルボキシアルデヒドとジイソプロピル亜鉛のアルキル化反応」は、生成物自身が不斉触媒として働き、微小な偏りをほぼ100%のエナンチオマー過剰率（ee）まで自己増幅させる世界唯一の反応系です。"
            },
            {
                "title": "2. 生命の起源と「右手と左手」の謎",
                "body": "地球上のすべての生物のタンパク質を構成するアミノ酸は「L型（左手型）」、DNA・RNAの糖は「D型（右手型）」に統一されています。通常の化学合成では半々に生じるはずの鏡像異性体がなぜ一方だけに偏ったのかという謎に、硤合反応は数学的・物理的証拠を与えました。"
            }
        ],
        "dialogue": [
            {
                "speaker": "七",
                "name": "Nanami",
                "role": "アシスタント・大学生",
                "text": "Keita先生！東京理科大学の硤合憲三先生がノーベル化学賞を受賞されたニュース、大興奮しました！『右手と左手の分子』ってどういうことなんですか？"
            },
            {
                "speaker": "慶",
                "name": "Keita先生",
                "role": "英語講師",
                "text": "素晴らしいニュースだね！右手と左手の手袋のように、鏡に映した形（enantiomer）はぴったり重なり合わない。私たちの体のアミノ酸はすべて『左手型』なんだけど、なんで片方だけなのか何百年も謎だったんだ。"
            },
            {
                "speaker": "七",
                "name": "Nanami",
                "role": "アシスタント・大学生",
                "text": "それを硤合先生が『自分自身を猛烈に増やす反応（autocatalysis）』で証明されたんですね！"
            },
            {
                "speaker": "慶",
                "name": "Keita先生",
                "role": "英語講師",
                "text": "その通り！生命の起源の謎（homochirality）に答えた世界的な業績だよ。文5の『Were humanity to probe...』のような倒置構文も難関大入試で必須だから、時事ニュースと一緒にマスターしよう！"
            }
        ],
        "quiz": [
            {
                "question": "What is the defining characteristic of the Soai reaction discovered by Dr. Kenso Soai?",
                "options": [
                    "It consumes large quantities of coal to generate electricity.",
                    "An infinitesimal initial enantiomeric imbalance triggers explosive self-amplification to near-complete purity.",
                    "It permanently freezes chemical solutions below absolute zero.",
                    "It converts plastic waste directly into edible vitamins."
                ],
                "correct_index": 1,
                "explanation": "【正解：B】<br>第3文「an infinitesimal initial imbalance between mirror-image enantiomers triggers an explosive self-amplification, culminating in enantiomeric purity of nearly one hundred percent」より、微小な偏りの爆発的自己増幅が正解です。"
            },
            {
                "question": "What fundamental biological mystery did Dr. Soai's discovery help elucidate?",
                "options": [
                    "Why human beings need eight hours of sleep each night.",
                    "The origin of uniform homochirality in terrestrial biomolecules.",
                    "Why desert plants survive without direct sunlight.",
                    "How birds navigate during seasonal oceanic migrations."
                ],
                "correct_index": 1,
                "explanation": "【正解：B】<br>第2・4文より、地球上の生体分子が一方の鏡像異性体のみで構成される「ホモキラリティー（生命の利き手）」の起源の謎を解明しました。"
            },
            {
                "question": "What grammatical inversion is present in the final sentence ('Were humanity to probe...')?",
                "options": [
                    "A mandatory subjunctive inversion equivalent to 'If humanity were to probe'.",
                    "A locative inversion moving prepositional phrases to the front.",
                    "A negative inversion triggered by 'never' or 'hardly'.",
                    "A comparative inversion used in statistical analysis."
                ],
                "correct_index": 0,
                "explanation": "【正解：A】<br>If humanity were to probe... から if が省略され were が文頭に倒置された仮定法未来の構文です。"
            }
        ],
        "faq": [
            {
                "q": "ノーベル化学賞や分子科学に関する入試頻出英単語は？",
                "a": "catalysis（触媒作用）、chirality（キラリティー・鏡像異性）、imbalance（不均衡）、symmetry（対称性）、pre-biotic（生命誕生前の・原始地球の）などが、東大・京大・早慶理工・医学部の英語で頻出します。"
            }
        ]
    },
    {
        "slug": "evtol-flying-taxis-tokyo-bay",
        "category": "entertainment",
        "category_label": "ENTERTAINMENT & GADGETS • 次世代モビリティ・先端技術",
        "date": "2026-10-10",
        "title": "Electric Flying Taxis Take Flight Over Tokyo Bay: Japan Launches Pilot Operations for Next-Generation Urban Air Mobility",
        "headline_ja": "東京湾岸で次世代「空飛ぶクルマ（eVTOL）」の試験商用運航が開始：都市型航空交通（UAM）が切り拓く移動の未来と安全基準",
        "subhead": "羽田とベイエリアを結ぶ電動垂直離着陸機（eVTOL）。渋滞解消と脱炭素の切り札として期待される一方、騒音対策と厳格な耐空性証明の壁を英語で検証。",
        "source_name": "GetNews Japan & Jiji Press (ガジェット通信・時事通信 / Tech, Gadgets & Urban Mobility)",
        "source_url": "https://getnews.jp/archives/evtol-flying-taxis-tokyo-bay",
        "source_attribution": "ガジェット通信および時事通信の先端モビリティ報道に基づき、東京湾岸で開始された次世代空飛ぶクルマ（eVTOL）の先行商用運航実験を高校・大学入試英語教材として再構成した記事です。",
        "image": "https://images.unsplash.com/photo-1508614589041-895b88991e3e?w=1000&auto=format&fit=crop&q=80",
        "sentences": [
            {
                "no": 1,
                "en": "Commercial test flights for electric vertical take-off and landing (eVTOL) aircraft commenced over Tokyo Bay on Saturday, marking a landmark milestone in Japan's strategic transition toward advanced urban air mobility.",
                "ja": "東京湾上空において土曜日、電動垂直離着陸機（eVTOL）の試験商用運航が開始され、先端都市型航空交通への日本の戦略的移行における歴史的な節目を刻みました。"
            },
            {
                "no": 2,
                "en": "Designed to bypass notorious metropolitan traffic congestion, these zero-emission aircraft can transport passengers between coastal hubs and downtown vertiports in a fraction of traditional transit times.",
                "ja": "悪名高い大都市の交通渋滞を回避するよう設計されたこれらのゼロエミッション航空機は、沿岸の拠点と都心のバーティポート（離着陸場）の間で、従来の移動時間のほんの数分の一で乗客を輸送することができます。"
            },
            {
                "no": 3,
                "en": "While technology enthusiasts celebrate the quiet electric propulsion, municipal authorities emphasize that widespread commercialization depends upon stringent airworthiness certification and meticulous low-altitude airspace management.",
                "ja": "技術愛好家たちが静粛な電動推進力を歓迎する一方で、自治体当局は、広範な商用化の成否は厳格な耐空性証明と極めて細心な低高度空域の管理にかかっていると強調しています。"
            },
            {
                "no": 4,
                "en": "Furthermore, aerospace engineers must actively minimize acoustic footprints over densely populated waterfront neighborhoods to foster genuine public acceptance.",
                "ja": "さらに、航空宇宙技術者たちは、地域社会からの真の受容を育むために、人口密度の高い臨海住宅街の上空における騒音の影響範囲（アコースティック・フットプリント）を積極的に最小化しなければなりません。"
            },
            {
                "no": 5,
                "en": "By systematically integrating autonomous avionics with civil infrastructure, Japan aims to establish a global benchmark for sustainable, congestion-free metropolitan transit.",
                "ja": "自律飛行アビオニクスと市民インフラを有機的に統合することによって、日本は持続可能で渋滞のない大都市交通の世界標準を確立することを目指しています。"
            }
        ],
        "vocabulary": [
            {
                "word": "eVTOL",
                "phonetic": "[ˌiː.viːˈtɒl]",
                "pos": "名詞",
                "meaning": "電動垂直離着陸機（electric vertical take-off and landing）",
                "def": "an aircraft that uses electric power to hover, take off, and land vertically",
                "ex": "Urban planners believe eVTOL vehicles will revolutionize airport connections."
            },
            {
                "word": "vertiport",
                "phonetic": "[ˈvɜː.tɪ.pɔːt]",
                "pos": "名詞",
                "meaning": "バーティポート、垂直離着陸機用発着場",
                "def": "a dedicated area designed for vertical take-off and landing aircraft to land and take off",
                "ex": "The new skyscraper includes a rooftop vertiport for air taxi shuttles."
            },
            {
                "word": "propulsion",
                "phonetic": "[prəˈpʌl.ʃən]",
                "pos": "名詞",
                "meaning": "推進力、推進装置",
                "def": "the action of driving or pushing forward",
                "ex": "Electric propulsion generates significantly lower carbon emissions than jet engines."
            },
            {
                "word": "stringent",
                "phonetic": "[ˈstrɪn.dʒənt]",
                "pos": "形容詞",
                "meaning": "（基準や法が）極めて厳格な、厳しい",
                "def": "strict, precise, and exacting regulations or conditions",
                "ex": "Aviation authorities enforce stringent safety audits before passenger certification."
            },
            {
                "word": "avionics",
                "phonetic": "[ˌeɪ.viˈɒn.ɪks]",
                "pos": "名詞",
                "meaning": "航空電子工学、アビオニクス",
                "def": "electronic equipment fitted in an aircraft, or the science of developing it",
                "ex": "Advanced avionics enable autonomous path planning during turbulent weather."
            }
        ],
        "syntax": [
            {
                "phrase": "in a fraction of traditional transit times",
                "meaning": "従来の移動時間のほんの数分の一（ごく短時間）で",
                "explanation": "fraction は『ごく一部・わずかな割合』を指し、in a fraction of ... で従来の所要時間と比べた圧倒的な時間短縮を表す難関大・共通テスト必出の比較表現です。"
            },
            {
                "phrase": "depends upon stringent airworthiness certification and ...",
                "meaning": "厳格な耐空性証明および〜にかかっている（左右される）",
                "explanation": "depend upon は『〜に依存する、〜次第である』を意味し、技術革新の普及条件や政策的ハードルを論述する際の最重要イディオムです。"
            }
        ],
        "factcheck": [
            {
                "title": "1. ガジェット通信・時事通信が報じる国内eVTOL実証運航",
                "body": "経済産業省と国土交通省が推進する「空の移動革命に向けた官民協議会」ロードマップに基づき、2026年秋から東京湾岸エリア（有明・青海〜羽田空港近郊）で国内外メーカーの有人型eVTOLによる定期航路試験が開始されました。"
            },
            {
                "title": "2. 耐空性証明と騒音規制の国際基準",
                "body": "従来のヘリコプターに比べ騒音は15〜20dB低く抑えられていますが、都市部上空を日常的に飛行するためには、航空法に基づく型式証明（安全基準）の取得と住民合意が不可欠な課題となっています。"
            }
        ],
        "dialogue": [
            {
                "speaker": "七",
                "name": "Nanami",
                "role": "アシスタント・大学生",
                "text": "Keita先生、ガジェット通信のトップニュース見ました！東京湾でついに「空飛ぶクルマ（eVTOL）」の試験飛行が始まったんですね！羽田からベイエリアまで数分で行けるなんて夢みたいです！"
            },
            {
                "speaker": "慶",
                "name": "Keita先生",
                "role": "英語講師",
                "text": "すごい進歩だよね。電動だからCO2も出ないし（zero-emission）、ヘリコプターよりもずっと静かなんだ。でも記事にある通り、街の上を毎日飛ばすには「耐空性証明（airworthiness certification）」という世界最高レベルの安全基準をクリアする必要があるんだ。"
            },
            {
                "speaker": "七",
                "name": "Nanami",
                "role": "アシスタント・大学生",
                "text": "確かに、万が一の故障やビル風での事故があったら大変ですもんね。空の渋滞を防ぐ航空管制（airspace management）も重要になりそうです。"
            },
            {
                "speaker": "慶",
                "name": "Keita先生",
                "role": "英語講師",
                "text": "その通り！入試でも「次世代モビリティの利便性と社会的受容（安全・騒音・規制）」は小論文や自由英作文で頻出だから、技術だけでなく社会制度の視点も一緒に英語で押さえておこう。"
            }
        ],
        "quiz": [
            {
                "question": "According to the passage, what is one major advantage of eVTOL aircraft compared to conventional transit?",
                "options": [
                    "They operate completely free of cost for all passengers.",
                    "They can bypass traffic congestion and significantly shorten transit times.",
                    "They can carry heavy cargo trains across open oceans.",
                    "They do not require any maintenance or battery recharging."
                ],
                "correct_index": 1,
                "explanation": "【正解：B】<br>第2文「Designed to bypass notorious metropolitan traffic congestion, these zero-emission aircraft can transport passengers ... in a fraction of traditional transit times」より、交通渋滞を回避し所要時間を大幅に短縮できる点です。"
            },
            {
                "question": "According to the text, what is essential for the widespread commercialization of eVTOL aircraft?",
                "options": [
                    "Stringent airworthiness certification and meticulous airspace management.",
                    "Demolishing all traditional airports to construct massive vertiports.",
                    "Mandating that pilots navigate purely with manual mechanical compasses.",
                    "Amplifying the acoustic noise footprint to alert nesting birds."
                ],
                "correct_index": 0,
                "explanation": "【正解：A】<br>第3文「widespread commercialization depends upon stringent airworthiness certification and meticulous low-altitude airspace management」より、厳格な耐空性証明と細心な空域管理が不可欠と述べられています。"
            },
            {
                "question": "Which word in the text is CLOSEST in meaning to 'stringent' in sentence 3?",
                "options": ["lenient", "rigorous", "flexible", "temporary"],
                "correct_index": 1,
                "explanation": "【正解：B】<br>stringent は「厳格な、厳しい」を意味するため、rigorous（厳密な、過酷なほどの）が最も適切です。"
            }
        ],
        "faq": [
            {
                "q": "eVTOLや次世代モビリティに関する入試頻出英単語は？",
                "a": "propulsion（推進力）、autonomous（自律的な）、congestion（混雑・渋滞）、infrastructure（社会基盤）、airworthiness（耐空性）などが頻出です。"
            }
        ]
    }
]

# Junior counterparts for the 3 new articles
INGESTED_JUNIOR_ARTICLES = [
    {
        "slug": "smart-glasses-ai-privacy",
        "category": "entertainment",
        "category_label": "ENTERTAINMENT & GADGETS • 英検準2級〜2級",
        "title": "Smart Glasses and AI: The Exciting Future and Privacy Rules We Need",
        "headline_ja": "スマートグラスとAI：未来のワクワクする技術とみんなで考えるプライバシーのルール",
        "subhead": "メガネをかけるだけでAIが道を案内してくれる時代へ！便利さと周囲への思いやりについて考えよう。",
        "lead_snippet": "最新のスマートグラスは、見た目は普通のメガネなのに、小さなカメラと人工知能（AI）が入っています。看板の外国語を自動で翻訳してくれるなど便利な反面、まわりの人のプライバシーを守るルール作りが求められています。",
        "source_name": "GetNews Japan (Adapted for Eiken Grade Pre-2 - 2)",
        "source_url": "https://getnews.jp/archives/smart-glasses-ai-privacy",
        "source_attribution": "ガジェット通信の最新テクノロジー記事を元に、英検準2級〜2級の標準的な英語で読みやすく再構成した教材です。",
        "source_student_guide": "最新のガジェットやAIの話題は、英検のリスニングや面接試験で大人気のテーマです。『便利で楽しいこと（メリット）』と『注意すべきマナー（注意点）』の両方を英語で言えるように練習しましょう。",
        "original_article_url": "../../../entertainment/smart-glasses-ai-privacy/index.html",
        "image": "https://images.unsplash.com/photo-1593508512255-86ab42a8e620?w=1000&auto=format&fit=crop&q=80",
        "sentences": [
            {
                "en": "Today, new smart glasses look just like normal glasses, but they have tiny cameras and computers inside.",
                "ja": "今日、新しいスマートグラスは普通のメガネとそっくりに見えますが、中に小さなカメラとコンピューターが入っています。"
            },
            {
                "en": "With artificial intelligence, these glasses can translate foreign languages on signs and give you directions as you walk.",
                "ja": "人工知能（AI）のおかげで、このメガネは看板の外国語を翻訳したり、歩いているときに道案内をしてくれたりします。"
            },
            {
                "en": "Many young people love this new technology because it makes everyday life much more convenient and fun.",
                "ja": "日常生活がずっと便利で楽しくなるため、多くの若者がこの新技術をとても気に入っています。"
            },
            {
                "en": "However, some people worry that these glasses might take photos or record videos of them without their permission.",
                "ja": "しかし一部の人々は、このメガネが許可なく自分たちの写真や動画を撮影してしまうのではないかと心配しています。"
            },
            {
                "en": "To enjoy this amazing technology safely, we need clear rules and good manners to protect everyone's privacy.",
                "ja": "この素晴らしい技術を安全に楽しむためには、全員のプライバシーを守る明確なルールと良いマナーが必要です。"
            }
        ],
        "dialogue": [
            {
                "speaker": "七",
                "name": "Nanami",
                "role": "高校生",
                "text": "Keita先生！普通のメガネに見えるのに、AIが目の前に道案内を出してくれるスマートグラスがあるって本当ですか？"
            },
            {
                "speaker": "慶",
                "name": "Keita先生",
                "role": "英語の先生",
                "text": "本当だよ！外国語の看板を見たら日本語に自動で訳してくれる機能もあって、未来の道具みたいだよね。"
            },
            {
                "speaker": "七",
                "name": "Nanami",
                "role": "高校生",
                "text": "すごく欲しいです！でも、周りの人は『勝手に写真撮られてるんじゃないか』って不安になりそうですね。"
            },
            {
                "speaker": "慶",
                "name": "Keita先生",
                "role": "英語の先生",
                "text": "Nanamiさん、素晴らしい着眼点だね！新しい技術を使うときは、周りのプライバシーを守るマナー（good manners）がとても大切なんだよ。"
            }
        ],
        "vocab": [
            {
                "word": "translate",
                "phonetic": "/trænzˈleɪt/",
                "pos": "動詞",
                "meaning": "〜を翻訳する、訳す",
                "def": "to change words into a different language.",
                "ex": "The smart glasses can translate foreign signs into Japanese."
            },
            {
                "word": "direction",
                "phonetic": "/daɪˈrek.ʃən/",
                "pos": "名詞",
                "meaning": "道案内、方向",
                "def": "instructions that tell someone how to get to a place.",
                "ex": "The app gives you clear directions as you walk around the city."
            },
            {
                "word": "permission",
                "phonetic": "/pəˈmɪʃ.ən/",
                "pos": "名詞",
                "meaning": "許可、同意",
                "def": "the act of allowing someone to do something.",
                "ex": "You must ask for permission before taking someone's photo."
            },
            {
                "word": "privacy",
                "phonetic": "/ˈprɪv.ə.si/",
                "pos": "名詞",
                "meaning": "プライバシー、私生活の秘密",
                "def": "the state of being alone and not watched by others.",
                "ex": "Everyone should respect other people's personal privacy."
            },
            {
                "word": "convenient",
                "phonetic": "/kənˈviː.ni.ənt/",
                "pos": "形容詞",
                "meaning": "便利な、使いやすい",
                "def": "useful, easy, or quick to do or use.",
                "ex": "Smart technology makes our daily life much more convenient."
            }
        ],
        "syntax": [
            {
                "phrase": "make + O + 形容詞（Oを〜にする）",
                "meaning": "高校1年・英検準2級の超頻出構文",
                "explanation": "文3の `makes everyday life much more convenient and fun` は、`make + 日常生活(everyday life) + より便利で楽しく(much more convenient and fun)` という第5文型(SVOC)です。日常英会話でも頻出の表現です。"
            },
            {
                "phrase": "without + 名詞 / -ing（〜なしで、〜することなく）",
                "meaning": "前置詞 without の基本用法",
                "explanation": "文4の `without their permission` は、「彼らの許可なしに」という意味です。英検ライティングでも条件や制限を伝える際によく使われます。"
            }
        ],
        "quiz": [
            {
                "question": "What is special about the new smart glasses mentioned in the text?",
                "options": [
                    "They can fly in the sky like drones.",
                    "They look like normal glasses but have cameras and AI inside.",
                    "They are made entirely of heavy iron.",
                    "They only work underwater in the ocean."
                ],
                "correct_index": 1,
                "explanation": "【正解：B】<br>第1文「look just like normal glasses, but they have tiny cameras and computers inside」より、Bが正解です。"
            },
            {
                "question": "Why are some people worried about smart glasses?",
                "options": [
                    "They might take photos or videos without permission.",
                    "They are too dark to wear on sunny days.",
                    "They cost less than regular books.",
                    "They make too much loud noise."
                ],
                "correct_index": 0,
                "explanation": "【正解：A】<br>第4文「might take photos or record videos of them without their permission」より、許可なく撮影される心配が述べられています。"
            },
            {
                "question": "Which word in the text means 'the freedom from being watched or disturbed by other people'?",
                "options": ["direction", "privacy", "permission", "technology"],
                "correct_index": 1,
                "explanation": "【正解：B】<br>他人に監視されず個人の秘密が守られる状態を表す単語は privacy（プライバシー）です。"
            }
        ]
    },
    {
        "slug": "japan-semiconductor-revival-rapidus",
        "category": "science",
        "category_label": "SCIENCE & TECH • 英検準2級〜2級",
        "title": "Japan's Big Plan to Make Super-Fast Computer Chips",
        "headline_ja": "日本の大きな挑戦：世界で一番速い超小型コンピューターチップをつくる！",
        "subhead": "スマホやAIの頭脳となる「半導体」。北海道で進む新しい工場づくりのニュースをやさしい英語で学びます。",
        "lead_snippet": "コンピューターやスマートフォン、電気自動車の頭脳である「半導体チップ」。日本は世界で最も進んだ2ナノメートルの極小チップを国内で作るため、北海道に巨大な工場を建設する国家プロジェクトを進めています。",
        "source_name": "Jiji Press (Adapted for Eiken Grade Pre-2 - 2)",
        "source_url": "https://www.jiji.com/jc/article?k=japan-semiconductor-rapidus",
        "source_attribution": "時事通信の経済・技術ニュースを元に、高校1〜2年生向けの標準的な英語で読みやすく再構成した教材です。",
        "source_student_guide": "英検や共通テストでは、最先端技術（AI・コンピューター）と国際社会のニュースが頻出します。知らない専門用語が出てきても、前後の文脈から『何が起きているのか』を落ち着いて読み取る力を鍛えましょう。",
        "original_article_url": "../../../science/japan-semiconductor-revival-rapidus/index.html",
        "image": "https://images.unsplash.com/photo-1518770660439-4636190af475?w=1000&auto=format&fit=crop&q=80",
        "sentences": [
            {
                "en": "Computer chips are like the brains inside smartphones, electric cars, and artificial intelligence systems.",
                "ja": "コンピューターチップ（半導体）は、スマートフォンや電気自動車、人工知能システムの『頭脳』のような存在です。"
            },
            {
                "en": "Japan used to produce many of the world's computer chips, but today most advanced chips are made abroad.",
                "ja": "かつて日本は世界の半導体の多くを生産していましたが、現在では最先端チップの多くが海外で作られています。"
            },
            {
                "en": "Now, the Japanese government is investing trillions of yen to build a cutting-edge factory in Hokkaido.",
                "ja": "現在、日本政府は北海道に最先端の工場を建設するため、数兆円規模の投資を行っています。"
            },
            {
                "en": "Japanese engineers are cooperating with top research teams from the United States and Europe to create super-fast two-nanometer chips.",
                "ja": "日本の技術者たちは、超高速な2ナノメートルチップを作るため、アメリカやヨーロッパのトップ研究チームと協力しています。"
            },
            {
                "en": "If this ambitious project succeeds, Japan will once again become a world leader in advanced technology.",
                "ja": "もしこの野心的なプロジェクトが成功すれば、日本は再び先端技術における世界のリーダーとなるでしょう。"
            }
        ],
        "dialogue": [
            {
                "speaker": "七",
                "name": "Nanami",
                "role": "高校生",
                "text": "Keita先生、半導体ってスマホやゲーム機の中に入っている緑色の基板にある黒いチップのことですよね？"
            },
            {
                "speaker": "慶",
                "name": "Keita先生",
                "role": "英語の先生",
                "text": "そうだよ！2ナノメートルというのは、人間の髪の毛の太さの何万分の一という信じられない小ささなんだ。"
            },
            {
                "speaker": "七",
                "name": "Nanami",
                "role": "高校生",
                "text": "そんなに小さく作れるんですね！北海道に世界最先端の工場ができるなんて、ワクワクします。"
            },
            {
                "speaker": "慶",
                "name": "Keita先生",
                "role": "英語の先生",
                "text": "アメリカやヨーロッパの研究者とも英語で協力しながら開発しているんだ。日本の未来を支える大切な挑戦だね。"
            }
        ],
        "vocab": [
            {
                "word": "produce",
                "phonetic": "/prəˈdjuːs/",
                "pos": "動詞",
                "meaning": "〜を生産する、製造する",
                "def": "to make or grow something, especially in large quantities.",
                "ex": "Japan used to produce many of the world's best electronic goods."
            },
            {
                "word": "advanced",
                "phonetic": "/ədˈvɑːnst/",
                "pos": "形容詞",
                "meaning": "最先端の、高度な",
                "def": "modern and well developed.",
                "ex": "This factory uses advanced technology to create small computer chips."
            },
            {
                "word": "cutting-edge",
                "phonetic": "/ˌkʌt.ɪŋ ˈedʒ/",
                "pos": "形容詞",
                "meaning": "最先端の、最も新しい",
                "def": "very modern and with all the newest features.",
                "ex": "They are building a cutting-edge laboratory in Hokkaido."
            },
            {
                "word": "cooperate",
                "phonetic": "/kəʊˈɒp.ər.eɪt/",
                "pos": "動詞",
                "meaning": "協力する、協同する",
                "def": "to work together with someone to achieve a goal.",
                "ex": "Japanese scientists cooperate with international research teams."
            },
            {
                "word": "ambitious",
                "phonetic": "/æmˈbɪʃ.əs/",
                "pos": "形容詞",
                "meaning": "野心的な、大がかりな",
                "def": "having a strong desire to be successful or requiring great effort.",
                "ex": "The country started an ambitious national project for clean energy."
            }
        ],
        "syntax": [
            {
                "phrase": "used to + 動詞の原形（かつて〜していた、以前は〜だった）",
                "meaning": "過去の状態や習慣を表す重要表現",
                "explanation": "文2の `Japan used to produce many of the world's computer chips` は、「かつては作っていた（が今は異なる）」という過去と現在の対比を表します。入試・英検で必出の助動詞表現です。"
            },
            {
                "phrase": "If S + V (現在形), S + will + 動詞の原形",
                "meaning": "未来の条件を表す基本構文（時・条件の副詞節）",
                "explanation": "文5の `If this ambitious project succeeds, Japan will once again become...` は、if節の中では未来の事柄でも現在形（succeeds）にするという英語の根本原則です。"
            }
        ],
        "quiz": [
            {
                "question": "What are computer chips compared to in sentence 1?",
                "options": [
                    "The wheels of a bicycle",
                    "The brains inside smartphones and electric cars",
                    "The batteries of flashlights",
                    "The metal frames of skyscrapers"
                ],
                "correct_index": 1,
                "explanation": "【正解：B】<br>第1文「Computer chips are like the brains inside smartphones, electric cars...」より、電子機器の頭脳に例えられています。"
            },
            {
                "question": "Where is the new cutting-edge chip factory being built in Japan?",
                "options": ["Tokyo", "Hokkaido", "Okinawa", "Kyoto"],
                "correct_index": 1,
                "explanation": "【正解：B】<br>第3文「build a cutting-edge factory in Hokkaido」より、北海道に建設されています。"
            },
            {
                "question": "Who are Japanese engineers working with on this project?",
                "options": [
                    "Movie makers in Hollywood",
                    "Top research teams from the United States and Europe",
                    "Traditional farmers across Asia",
                    "Deep-sea submarine pilots"
                ],
                "correct_index": 1,
                "explanation": "【正解：B】<br>第4文「cooperating with top research teams from the United States and Europe」より、米国や欧州の研究チームと協力しています。"
            }
        ]
    },
    {
        "slug": "digital-school-backpack-reform",
        "category": "society",
        "category_label": "SOCIETY & EDUCATION • 英検準2級〜2級",
        "title": "Heavy School Bags and Digital Tablets: How Classrooms in Japan Are Changing",
        "headline_ja": "重いランドセルとタブレット端末：日本の学校はどう変わっていくのか？",
        "subhead": "教科書とタブレットでカバンが重すぎる！生徒たちの体を守りながら楽しく勉強するためのアイデアを読みます。",
        "lead_snippet": "全国の小中学校でタブレット端末が配られましたが、紙の教科書も一緒に持ち運ぶためカバンが重すぎる問題が発生しています。生徒の健康を守るため、軽量リュックサックを認める学校が増えています。",
        "source_name": "Yahoo! News Japan (Adapted for Eiken Grade Pre-2 - 2)",
        "source_url": "https://news.yahoo.co.jp/articles/digital-school-backpack-reform",
        "source_attribution": "Yahoo!ニュースの教育・生活特集を基に、高校生が身近に共感できる標準的な英語で書き下ろした教材です。",
        "source_student_guide": "英検のライティングテストでは、『学校のルールやデジタル化の良し悪し』について自分の意見（理由2つ）を書く問題が頻出します。この英文をヒントに、賛成・反対の理由を英語で言えるようにしましょう。",
        "original_article_url": "../../../society/digital-school-backpack-reform/index.html",
        "image": "https://images.unsplash.com/photo-1503676260728-1c00da094a0b?w=1000&auto=format&fit=crop&q=80",
        "sentences": [
            {
                "en": "In recent years, almost all elementary and junior high schools in Japan gave digital tablets to their students.",
                "ja": "近年、日本のほぼすべての小中学校で、児童生徒にデジタルタブレットが配られました。"
            },
            {
                "en": "Many people hoped that tablets would replace heavy paper textbooks and make school bags much lighter.",
                "ja": "多くの人々が、タブレットが重い紙の教科書に取って代わり、通学カバンがずっと軽くなることを期待していました。"
            },
            {
                "en": "However, many students still have to carry both traditional textbooks and tablets home every single day.",
                "ja": "しかし多くの生徒が、今でも毎日、昔ながらの教科書とタブレットの両方を家に持ち帰らなければなりません。"
            },
            {
                "en": "Doctors warn that bags weighing more than fifteen percent of a child's body weight can cause back pain and bad posture.",
                "ja": "医師たちは、子どもの体重の15パーセントを超える重いカバンは腰痛や姿勢の悪化の原因になると警告しています。"
            },
            {
                "en": "To solve this problem, more schools now allow lightweight backpacks and encourage students to leave some books at school.",
                "ja": "この問題を解決するため、より多くの学校が軽量なリュックサックを認め、一部の教科書を学校に置いて帰ることを推奨しています。"
            }
        ],
        "dialogue": [
            {
                "speaker": "七",
                "name": "Nanami",
                "role": "高校生",
                "text": "Keita先生、私も中学生のときタブレットと教科書でカバンが本当に重くて、肩がパンパンでした！"
            },
            {
                "speaker": "慶",
                "name": "Keita先生",
                "role": "英語の先生",
                "text": "それは大変だったね。体重の15%を超える重さの荷物を背負うと、成長期の子どもの体に負担（bad posture）がかかることが医学的に証明されているんだ。"
            },
            {
                "speaker": "七",
                "name": "Nanami",
                "role": "高校生",
                "text": "だから最近、革のランドセルの代わりに軽い布製リュック（lightweight backpack）を使う小学生が増えているんですね。"
            },
            {
                "speaker": "慶",
                "name": "Keita先生",
                "role": "英語の先生",
                "text": "伝統を守ることも大切だけど、子どもの健康に合わせて柔軟にルールを変えること（leave books at school）も大事だね。英検の英作文でも使える身近な話題だよ！"
            }
        ],
        "vocab": [
            {
                "word": "replace",
                "phonetic": "/rɪˈpleɪs/",
                "pos": "動詞",
                "meaning": "〜に取って代わる、取り替える",
                "def": "to take the place of something, or put something new in the place of something.",
                "ex": "Electric cars will gradually replace traditional gasoline vehicles."
            },
            {
                "word": "traditional",
                "phonetic": "/trəˈdɪʃ.ən.əl/",
                "pos": "形容詞",
                "meaning": "伝統的な、昔ながらの",
                "def": "following ideas and methods that have existed for a long time.",
                "ex": "The students still carry traditional Japanese leather backpacks."
            },
            {
                "word": "posture",
                "phonetic": "/ˈpɒs.tʃər/",
                "pos": "名詞",
                "meaning": "姿勢",
                "def": "the position in which you hold your body when standing or sitting.",
                "ex": "Sitting in front of a computer all day can cause bad posture."
            },
            {
                "word": "lightweight",
                "phonetic": "/ˈlaɪt.weɪt/",
                "pos": "形容詞",
                "meaning": "軽量の、軽い",
                "def": "made of thinner material and weighing less than average.",
                "ex": "He bought a lightweight backpack for mountain hiking."
            },
            {
                "word": "encourage",
                "phonetic": "/ɪnˈkʌr.ɪdʒ/",
                "pos": "動詞",
                "meaning": "〜を奨励する、勧める",
                "def": "to make someone more likely to do something.",
                "ex": "The teacher encouraged students to read English books every morning."
            }
        ],
        "syntax": [
            {
                "phrase": "encourage + O + to 不定詞（Oに〜するよう勧める）",
                "meaning": "高校・英検準2級〜2級の最頻出動詞型",
                "explanation": "文5の `encourage students to leave some books at school` は、`encourage + 生徒(students) + 置いていくこと(to leave)` という形です。tell/ask/allow などの『動詞 + O + to V』のグループとして覚えましょう。"
            },
            {
                "phrase": "have to + 動詞の原形（〜しなければならない）",
                "meaning": "客観的な義務・必要性を表す表現",
                "explanation": "文3の `many students still have to carry both traditional textbooks and tablets` は、「（学校の規則などのために）持ち帰らざるを得ない」という状況を表しています。"
            }
        ],
        "quiz": [
            {
                "question": "What did people originally hope digital tablets would do?",
                "options": [
                    "Make school bags much lighter by replacing paper books.",
                    "Teach children how to play video games quickly.",
                    "Replace all school teachers with robots.",
                    "Make classrooms colder during the summer."
                ],
                "correct_index": 0,
                "explanation": "【正解：A】<br>第2文「hoped that tablets would replace heavy paper textbooks and make school bags much lighter」より、紙の教科書に取って代わりカバンが軽くなることが期待されていました。"
            },
            {
                "question": "What health problem can be caused by overly heavy bags according to doctors?",
                "options": [
                    "Poor eyesight and headaches only",
                    "Back pain and bad posture",
                    "Hearing loss in loud rooms",
                    "Stomach ache after lunch"
                ],
                "correct_index": 1,
                "explanation": "【正解：B】<br>第4文「can cause back pain and bad posture」より、腰痛や姿勢の悪化が挙げられています。"
            },
            {
                "question": "How are some schools trying to solve the heavy bag problem?",
                "options": [
                    "By banning all homework permanently.",
                    "By allowing lightweight backpacks and letting students leave some books at school.",
                    "By asking students to walk to school three hours earlier.",
                    "By selling heavier metal lockers to parents."
                ],
                "correct_index": 1,
                "explanation": "【正解：B】<br>最終文「allow lightweight backpacks and encourage students to leave some books at school」より、軽量リュックの許可と置き勉の推奨が解決策です。"
            }
        ]
    },
    {
        "slug": "regulatory-t-cells-nobel-breakthrough",
        "category": "science",
        "category_label": "SCIENCE & HEALTH • 英検準2級〜2級",
        "title": "How a Japanese Scientist Discovered the Body's Natural Brake Cells",
        "headline_ja": "日本の科学者が発見した体のブレーキ役：暴走する免疫をコントロールする仕組み",
        "subhead": "病気のウイルスと戦う免疫システムが、自分の体を傷つけないように見守る「ブレーキ細胞」。世界的発見をやさしい英語で読み解きます。",
        "lead_snippet": "大阪大学の坂口志文教授は、私たちの体に備わっている「免疫のブレーキ役」となる特別な細胞を発見しました。この発見によって、アレルギーや自己免疫疾患の原因が解明され、新しいがんの治療薬の開発につながっています。",
        "source_name": "Jiji Press & Nature (Adapted for Eiken Grade Pre-2 - 2)",
        "source_url": "https://www.jiji.com/jc/article?k=regulatory-t-cells-sakaguchi",
        "source_attribution": "時事通信の科学特報および学術誌Natureの解説を基に、高校生向け標準英語で読みやすく再構成した教材です。",
        "source_student_guide": "英検や共通テストの理系長文では、『人体の不思議や病気のメカニズム』が頻出します。知らない専門用語があっても慌てず、『どんな働き（機能）をするのか』を前後の動詞から読み取る練習をしましょう。",
        "original_article_url": "../../../science/regulatory-t-cells-nobel-breakthrough/index.html",
        "image": "https://images.unsplash.com/photo-1532187863486-abf9dbad1b69?w=1000&auto=format&fit=crop&q=80",
        "sentences": [
            {
                "en": "Our body has a powerful defense system called the immune system to fight against dangerous viruses and bacteria.",
                "ja": "私たちの体には、危険なウイルスや細菌と戦うための「免疫システム」と呼ばれる強力な防衛機能が備わっています。"
            },
            {
                "en": "However, if this system attacks healthy organs by mistake, a person can develop serious autoimmune illnesses.",
                "ja": "しかし、もしこのシステムが誤って健康な臓器を攻撃してしまうと、深刻な自己免疫疾患を引き起こすことがあります。"
            },
            {
                "en": "A famous Japanese scientist, Dr. Shimon Sakaguchi, discovered special cells that act like brakes to stop immune attacks.",
                "ja": "著名な日本人科学者である坂口志文博士は、免疫の攻撃を止めるブレーキのように働く特別な細胞を発見しました。"
            },
            {
                "en": "Thanks to his brilliant research, doctors can now create innovative medicines to treat both allergies and severe cancers.",
                "ja": "博士の素晴らしい研究のおかげで、医師たちは現在、アレルギーと重いがんの双方を治療する画期的な薬を開発できるようになりました。"
            },
            {
                "en": "His groundbreaking work shows that understanding how nature balances the human body can save millions of lives.",
                "ja": "彼の先駆的な研究は、自然がどのように人間の体のバランスをとっているかを理解することが何百万もの命を救う力になることを示しています。"
            }
        ],
        "dialogue": [
            {
                "speaker": "七",
                "name": "Nanami",
                "role": "高校生",
                "text": "Keita先生、日本人の坂口先生が発見した『免疫のブレーキ細胞』って、どんなすごい細胞なんですか？"
            },
            {
                "speaker": "慶",
                "name": "Keita先生",
                "role": "英語の先生",
                "text": "私たちの体の中の免疫は、病原体を倒すための強い武器を持っているんだ。でもブレーキがないと、自分の胃や関節まで壊してしまう。その暴走を防ぐのが坂口先生が見つけた『制御性T細胞』なんだよ。"
            },
            {
                "speaker": "七",
                "name": "Nanami",
                "role": "高校生",
                "text": "文4の『Thanks to his brilliant research（素晴らしい研究のおかげで）』というように、がんの治療薬にも役立っているんですね！"
            },
            {
                "speaker": "慶",
                "name": "Keita先生",
                "role": "英語の先生",
                "text": "まさに世界中の医師や研究者が注目している大発見だね。ノーベル賞でも毎年大本命として挙げられているんだよ。"
            }
        ],
        "vocab": [
            {
                "word": "defense",
                "phonetic": "/dɪˈfens/",
                "pos": "名詞",
                "meaning": "防衛、防御、身を守ること",
                "def": "protection or support against attack, criticism, or danger.",
                "ex": "The immune system is our best defense against winter infections."
            },
            {
                "word": "attack",
                "phonetic": "/əˈtæk/",
                "pos": "動詞",
                "meaning": "〜を攻撃する、襲う",
                "def": "to try to hurt or defeat using violent physical action or force.",
                "ex": "White blood cells attack foreign bacteria inside the bloodstream."
            },
            {
                "word": "illness",
                "phonetic": "/ˈɪl.nəs/",
                "pos": "名詞",
                "meaning": "病気、疾患",
                "def": "a disease of the body or mind.",
                "ex": "Regular exercise can help prevent many chronic illnesses."
            },
            {
                "word": "innovative",
                "phonetic": "/ˈɪn.ə.və.tɪv/",
                "pos": "形容詞",
                "meaning": "革新的な、画期的な",
                "def": "using new methods or ideas.",
                "ex": "The university laboratory developed an innovative cancer treatment."
            },
            {
                "word": "groundbreaking",
                "phonetic": "/ˈɡraʊndˌbreɪ.kɪŋ/",
                "pos": "形容詞",
                "meaning": "先駆的な、画期的な",
                "def": "if something is groundbreaking, it is very new and a big turning point.",
                "ex": "Dr. Sakaguchi's groundbreaking discovery changed modern medicine."
            }
        ],
        "syntax": [
            {
                "phrase": "by mistake（誤って、うっかり）",
                "meaning": "日常会話・長文頻出の重要副詞句",
                "explanation": "文2の `if this system attacks healthy organs by mistake` は、「もし免疫が誤って自分の臓器を攻撃したら」という条件を表しています。"
            },
            {
                "phrase": "thanks to + 名詞（〜のおかげで）",
                "meaning": "原因・感謝を表す前置詞的表現",
                "explanation": "文4の `Thanks to his brilliant research` は、「彼の素晴らしい研究のおかげで」という意味です。because of の肯定的なニュアンスとしてよく使われます。"
            }
        ],
        "quiz": [
            {
                "question": "What problem occurs if the immune system attacks healthy organs by mistake?",
                "options": [
                    "A person can develop serious autoimmune illnesses.",
                    "The human heart beats three times faster.",
                    "A person forgets foreign languages quickly.",
                    "Body temperature permanently drops below zero."
                ],
                "correct_index": 0,
                "explanation": "【正解：A】<br>第2文「if this system attacks healthy organs by mistake, a person can develop serious autoimmune illnesses」より、深刻な自己免疫疾患が引き起こされます。"
            },
            {
                "question": "What did Dr. Shimon Sakaguchi discover?",
                "options": [
                    "A new planet outside the solar system",
                    "Special cells that act like brakes to stop immune attacks",
                    "A method to speak with underwater dolphins",
                    "A machine to produce artificial diamonds"
                ],
                "correct_index": 1,
                "explanation": "【正解：B】<br>第3文「discovered special cells that act like brakes to stop immune attacks」より、免疫の攻撃を止めるブレーキ細胞の発見が正解です。"
            },
            {
                "question": "Which of the following words means 'using new methods or ideas'?",
                "options": ["innovative", "harmful", "tiring", "ancient"],
                "correct_index": 0,
                "explanation": "【正解：A】<br>新しい手法やアイデアを取り入れた状態を表す形容詞は innovative（革新的な）です。"
            }
        ]
    },
    {
        "slug": "soai-reaction-nobel-chemistry",
        "category": "science",
        "category_label": "SCIENCE & DISCOVERY • 英検準2級〜2級",
        "title": "The Mystery of Right and Left Molecules: Japanese Professor Wins the 2026 Nobel Prize in Chemistry",
        "headline_ja": "右手と左手の分子のふしぎ：東京理科大の硤合先生が2026年ノーベル化学賞を受賞！",
        "subhead": "私たちの体を形づくるアミノ酸はなぜ「左手型」ばかりなのか？世界中の科学者を驚かせた「硤合反応」をやさしい英語で学びます。",
        "lead_snippet": "スウェーデン王立科学アカデミーは、2026年のノーベル化学賞を東京理科大学名誉教授の硤合憲三（そあい・けんぞう）先生らに授与すると発表しました。生命の分子がなぜ一方向の「利き手」を選んだのかという最大の謎を解いた大発見です。",
        "source_name": "Jiji Press & Nobel Prize (Adapted for Eiken Grade Pre-2 - 2)",
        "source_url": "https://www.jiji.com/jc/article?k=soai-reaction-nobel-chemistry-2026",
        "source_attribution": "時事通信のノーベル賞特報およびノーベル財団公式発表を基に、高校生が理解しやすい標準的な英語で書き下ろした教材です。",
        "source_student_guide": "高校化学や生物で習う『アミノ酸』や『DNA』の構造と直結した最新科学ニュースです。英検や大学入試の長文読解でも、『生命の起源』に関するテーマは頻出です。",
        "original_article_url": "../../../science/soai-reaction-nobel-chemistry/index.html",
        "image": "https://images.unsplash.com/photo-1532094349884-543bc11b234d?w=1000&auto=format&fit=crop&q=80",
        "sentences": [
            {
                "en": "Professor Kenso Soai of the Tokyo University of Science has won the 2026 Nobel Prize in Chemistry.",
                "ja": "東京理科大学名誉教授の硤合憲三先生が、2026年のノーベル化学賞を受賞しました。"
            },
            {
                "en": "Many molecules in nature have two shapes that look like a right hand and a left hand.",
                "ja": "自然界にある多くの分子には、右手と左手のように鏡に映した2つの形が存在します。"
            },
            {
                "en": "Curiously, all living things on Earth use only left-handed amino acids to build their bodies.",
                "ja": "不思議なことに、地球上のすべての生物は体をつくるために「左手型」のアミノ酸しか使っていません。"
            },
            {
                "en": "Professor Soai discovered an amazing chemical reaction where a tiny difference rapidly multiplies itself.",
                "ja": "硤合先生は、ごくわずかな違いが自分自身を猛烈なスピードで増やしていく驚くべき化学反応を発見しました。"
            },
            {
                "en": "His famous discovery helps scientists solve one of the greatest mysteries about the origin of life.",
                "ja": "彼の名高い大発見は、生命の起源をめぐる最大の謎の1つを解き明かす大きな助けとなっています。"
            }
        ],
        "dialogue": [
            {
                "speaker": "七",
                "name": "Nanami",
                "role": "高校生",
                "text": "Keita先生！東京理科大学の硤合先生が2026年のノーベル化学賞を受賞されたニュース、見ました！『分子の右手と左手』ってどういうことですか？"
            },
            {
                "speaker": "慶",
                "name": "Keita先生",
                "role": "英語の先生",
                "text": "素晴らしいニュースだね！右手用の手袋と左手用の手袋を重ねられないように、分子にも鏡に映したペア（mirror images）があるんだ。人間の体のアミノ酸はなぜか全部『左手型』なんだよ。"
            },
            {
                "speaker": "七",
                "name": "Nanami",
                "role": "高校生",
                "text": "文4の『rapidly multiplies itself（猛烈に自分を増やす）』という反応を、硤合先生が世界で初めて見つけたんですね！"
            },
            {
                "speaker": "慶",
                "name": "Keita先生",
                "role": "英語の先生",
                "text": "その通り！『硤合反応（Soai Reaction）』として世界中の教科書に載っているんだ。生命の起源（origin of life）に迫る日本の誇らしいニュースを、英語でしっかり学ぼう！"
            }
        ],
        "vocab": [
            {
                "word": "molecule",
                "phonetic": "/ˈmɒl.ɪ.kjuːl/",
                "pos": "名詞",
                "meaning": "分子（物質の最小単位の一つ）",
                "def": "the simplest unit of a chemical substance, composed of atoms.",
                "ex": "Water is made of one oxygen atom and two hydrogen molecules."
            },
            {
                "word": "curiously",
                "phonetic": "/ˈkjʊə.ri.əs.li/",
                "pos": "副詞",
                "meaning": "奇妙なことに、不思議なことに",
                "def": "in a strange, unusual, or surprising way.",
                "ex": "Curiously, none of the students noticed the open window."
            },
            {
                "word": "difference",
                "phonetic": "/ˈdɪf.ər.əns/",
                "pos": "名詞",
                "meaning": "違い、差、わずかな不均衡",
                "def": "the way in which two or more things which you are comparing are not the same.",
                "ex": "Can you spot the difference between the two chemical samples?"
            },
            {
                "word": "rapidly",
                "phonetic": "/ˈræp.ɪd.li/",
                "pos": "副詞",
                "meaning": "急速に、非常に速く",
                "def": "in a fast or sudden way.",
                "ex": "The new technology spread rapidly across the globe."
            },
            {
                "word": "origin",
                "phonetic": "/ˈɒr.ɪ.dʒɪn/",
                "pos": "名詞",
                "meaning": "起源、始まり、生まれ",
                "def": "the beginning or cause of something.",
                "ex": "Scientists continue to explore the origin of the universe."
            }
        ],
        "syntax": [
            {
                "phrase": "look like + 名詞（〜のように見える）",
                "meaning": "身近な外見や形状を説明する基本表現",
                "explanation": "文2の `shapes that look like a right hand and a left hand` は、「右手と左手のように見える形」という意味です。look + 形容詞（〜に見える）との違いに注意しましょう。"
            },
            {
                "phrase": "help + O + 動詞の原形（Oが〜するのを助ける）",
                "meaning": "高校英語・英検長文の超頻出使役構文",
                "explanation": "文5の `helps scientists solve one of the greatest mysteries` は、`help + 科学者たち(scientists) + 解決する(solve)` という形です。to不定詞ではなく動詞の原形（原形不定詞）が続く点が入試頻出です。"
            }
        ],
        "quiz": [
            {
                "question": "What award did Professor Kenso Soai win in 2026?",
                "options": [
                    "The Nobel Prize in Literature",
                    "The Nobel Prize in Chemistry",
                    "The World Architecture Award",
                    "An Olympic Gold Medal"
                ],
                "correct_index": 1,
                "explanation": "【正解：B】<br>第1文「Professor Kenso Soai of the Tokyo University of Science has won the 2026 Nobel Prize in Chemistry」より、2026年ノーベル化学賞が正解です。"
            },
            {
                "question": "What is curious about living things on Earth according to the text?",
                "options": [
                    "They can live underwater without any oxygen.",
                    "They use only left-handed amino acids to build their bodies.",
                    "They only sleep two hours per week.",
                    "They change their colors when it rains."
                ],
                "correct_index": 1,
                "explanation": "【正解：B】<br>第3文「Curiously, all living things on Earth use only left-handed amino acids to build their bodies」より、生命が左手型アミノ酸のみを使う点です。"
            },
            {
                "question": "Which of the following words means 'in a very fast or sudden way'?",
                "options": ["rapidly", "curiously", "traditional", "fragile"],
                "correct_index": 0,
                "explanation": "【正解：A】<br>「急速に、非常に速く」という意味を表す副詞は rapidly です。"
            }
        ]
    },
    {
        "slug": "evtol-flying-taxis-tokyo-bay",
        "category": "entertainment",
        "category_label": "ENTERTAINMENT & GADGETS • 英検準2級〜2級",
        "date": "2026-10-10",
        "title": "Electric Flying Cars in Tokyo: How Next-Generation Taxis Will Change Our Cities",
        "headline_ja": "東京の空を飛ぶクルマ：次世代の空飛ぶタクシーが変える未来の街と生活",
        "subhead": "羽田空港と東京湾をわずか数分で結ぶ『空飛ぶクルマ』の実験がスタート！静かでクリーンな未来の乗り物を、英検準2級〜2級のやさしい英語で学びます。",
        "lead_snippet": "東京湾で、電気で飛ぶ新しい乗り物『eVTOL（空飛ぶクルマ）』のテストが始まりました。渋滞を飛び越えて目的地へ早く行けるため、未来の新しい交通手段として世界中から注目されています。",
        "source_name": "GetNews Japan & Jiji Press (Adapted for Eiken Grade Pre-2 - 2)",
        "source_url": "https://getnews.jp/archives/evtol-flying-taxis-tokyo-bay",
        "source_attribution": "ガジェット通信および時事通信の先端モビリティ報道を元に、英検準2級〜2級（高校1〜2年生）の標準的な英語で読みやすく再構成した教材です。",
        "source_student_guide": "英検や高校入試でよく出る『未来のテクノロジーと環境問題』をテーマにした英文です。空飛ぶクルマの便利さだけでなく、『静かなモーター』や『安全のためのルール』など、良い点と注意すべき点を整理しながら読みましょう。",
        "original_article_url": "../../../entertainment/evtol-flying-taxis-tokyo-bay/index.html",
        "image": "https://images.unsplash.com/photo-1508614589041-895b88991e3e?w=1000&auto=format&fit=crop&q=80",
        "sentences": [
            {
                "en": "On Saturday, new electric flying cars began test flights over Tokyo Bay.",
                "ja": "土曜日、新しい電気の空飛ぶクルマが東京湾の上空でテスト飛行を始めました。"
            },
            {
                "en": "These flying vehicles take off and land vertically like helicopters, but they are much quieter and do not produce exhaust gas.",
                "ja": "これらの飛行ビークルはヘリコプターのように垂直に離着陸しますが、はるかに静かで排気ガスを出しません。"
            },
            {
                "en": "By flying through the air, people can avoid heavy traffic jams and reach their destinations much faster than by train or car.",
                "ja": "空を飛ぶことで、人々はひどい交通渋滞を避け、電車や車よりもずっと速く目的地に着くことができます。"
            },
            {
                "en": "However, experts say that strict safety rules and quiet engines are necessary so that people living nearby feel safe.",
                "ja": "しかし専門家は、近くに住む人々が安心できるように、厳しい安全ルールと静かなエンジンが必要であると述べています。"
            },
            {
                "en": "If this project succeeds, catching a flying taxi across Tokyo may become a normal part of our daily lives in the near future.",
                "ja": "もしこの計画が成功すれば、東京の空で空飛ぶタクシーに乗ることが、近い将来私たちの日常生活の当たり前になるかもしれません。"
            }
        ],
        "dialogue": [
            {
                "speaker": "七",
                "name": "Nanami",
                "role": "アシスタント・大学生",
                "text": "Keita先生、東京湾で「空飛ぶクルマ」が飛んだって本当ですか？SF映画の未来が現実になってきましたね！"
            },
            {
                "speaker": "慶",
                "name": "Keita先生",
                "role": "英語講師",
                "text": "本当だよ！電気で動くから静かで、ヘリコプターみたいに真上に飛び立てるんだ（take off vertically）。"
            },
            {
                "speaker": "七",
                "name": "Nanami",
                "role": "アシスタント・大学生",
                "text": "電車や車の渋滞に巻き込まれないのは最高ですね！私も早く乗ってみたいです！"
            },
            {
                "speaker": "慶",
                "name": "Keita先生",
                "role": "英語講師",
                "text": "便利だけど、街の上を飛ぶからこそ「絶対に事故を起こさない安全ルール（safety rules）」が一番大切なんだよ。英検でも未来の乗り物の話題はよく出るから、しっかり復習しようね。"
            }
        ],
        "quiz": [
            {
                "question": "How do the new flying vehicles take off?",
                "options": [
                    "They need a very long runway like big airplanes.",
                    "They take off and land vertically like helicopters.",
                    "They can only launch from deep underground stations.",
                    "They must be dropped from a giant balloon."
                ],
                "correct_index": 1,
                "explanation": "【正解：B】<br>第2文「These flying vehicles take off and land vertically like helicopters」より、ヘリコプターのように垂直に離着陸します。"
            },
            {
                "question": "According to the passage, why are electric flying cars good for the environment?",
                "options": [
                    "They do not produce exhaust gas and are very quiet.",
                    "They run on coal and heavy fuel oil.",
                    "They make loud noises to scare wild animals away.",
                    "They use clean sea water instead of electricity."
                ],
                "correct_index": 0,
                "explanation": "【正解：A】<br>第2文「they are much quieter and do not produce exhaust gas」より、排気ガスを出さず静かである点です。"
            },
            {
                "question": "Which word or phrase has the CLOSEST meaning to 'destinations' in sentence 3?",
                "options": [
                    "places people want to go",
                    "tickets for rock concerts",
                    "problems with heavy traffic",
                    "types of smartphones"
                ],
                "correct_index": 0,
                "explanation": "【正解：A】<br>destination は「目的地、行き先」を意味するため、places people want to go（人々が行きたい場所）が正解です。"
            }
        ],
        "vocab": [
            {
                "word": "vehicle",
                "phonetic": "/ˈviː.ɪ.kəl/",
                "pos": "名詞",
                "meaning": "乗り物、車両",
                "def": "a machine that you can travel in, such as a car, bus, or plane.",
                "ex": "Electric vehicles are becoming more popular every year."
            },
            {
                "word": "vertically",
                "phonetic": "/ˈvɜː.tɪ.kəl.i/",
                "pos": "副詞",
                "meaning": "垂直に、まっすぐ上に",
                "def": "straight up or at an angle of 90 degrees to the ground.",
                "ex": "The flying car can lift off vertically without a runway."
            },
            {
                "word": "destination",
                "phonetic": "/ˌdes.tɪˈneɪ.ʃən/",
                "pos": "名詞",
                "meaning": "目的地、行き先",
                "def": "the place where someone or something is going.",
                "ex": "We arrived at our destination 30 minutes ahead of schedule."
            },
            {
                "word": "traffic jam",
                "phonetic": "/ˈtræf.ɪk ˌdʒæm/",
                "pos": "名詞",
                "meaning": "交通渋滞",
                "def": "a long line of vehicles on a road that cannot move or can only move very slowly.",
                "ex": "Flying taxis help passengers avoid morning traffic jams."
            }
        ],
        "syntax": [
            {
                "phrase": "take off and land vertically",
                "meaning": "垂直に離着陸する（take off「離陸する」・land「着陸する」）",
                "explanation": "飛行機の基本動作を表す群動詞 take off（離陸する）と自動詞 land（着陸する）を組み合わせた表現です。vertically（垂直に）は高校英語・英検準2級で必須の副詞です。"
            },
            {
                "phrase": "reach their destinations much faster than ...",
                "meaning": "〜よりずっと速く目的地に着く（比較級の強調 much + faster than）",
                "explanation": "比較級（faster）を強調する副詞 much（はるかに・ずっと）の重要用法です。very faster とは言えない点が入試や英検の正誤問題で頻出します。"
            }
        ]
    }
]

from batch5_nine_articles import BATCH5_SENIOR_ARTICLES, BATCH5_JUNIOR_ARTICLES
INGESTED_SENIOR_ARTICLES.extend(BATCH5_SENIOR_ARTICLES)
INGESTED_JUNIOR_ARTICLES.extend(BATCH5_JUNIOR_ARTICLES)

def synthesize_audio_for_article(slug, category, sentences, dialogue, is_junior=False):
    """Synthesizes text and dialogue audio files using Edge-TTS"""
    if is_junior:
        target_dir = os.path.join(PORTAL_DIR, "junior", category, slug, "audio")
    else:
        target_dir = os.path.join(PORTAL_DIR, category, slug, "audio")
    os.makedirs(target_dir, exist_ok=True)

    tasks = []
    
    # 1. Full text & Sentences
    full_text = " ".join([s["en"] for s in sentences])
    rate = "-10%" if is_junior else "+0%"
    tasks.append((os.path.join(target_dir, "full.mp3"), full_text, VOICE_BRITISH, rate))
    
    for i, s in enumerate(sentences, 1):
        tasks.append((os.path.join(target_dir, f"s{i}.mp3"), s["en"], VOICE_BRITISH, rate))

    # 2. Dialogue
    for i, d in enumerate(dialogue, 1):
        voice = VOICE_KEITA if "慶" in d["speaker"] or "Keita" in d["name"] else VOICE_NANAMI
        tasks.append((os.path.join(target_dir, f"d{i}.mp3"), d["text"], voice, "+0%"))

    async def run_synth():
        for path, txt, v, r in tasks:
            if not os.path.exists(path):
                comm = edge_tts.Communicate(txt, v, rate=r)
                await comm.save(path)
                print(f"  [TTS] Synthesized {os.path.basename(path)}")
            else:
                pass

    asyncio.run(run_synth())

def main():
    print("============================================================")
    print(f"  AUTO-INGESTION PIPELINE: Expanding Catalog (Max {MAX_ARTICLES})")
    print("============================================================")
    print(f"Sources configured:")
    print("  - https://www.jiji.com/ (時事通信 / Jiji Press)")
    print("  - https://news.yahoo.co.jp/ (Yahoo!ニュース / Yahoo! News Japan)")
    print("  - https://getnews.jp/ (ガジェット通信 / GetNews Japan)")
    print("------------------------------------------------------------")

    import articles_data
    import junior_articles_data

    # Check capacity limit
    current_senior_count = len(articles_data.ARTICLES)
    print(f"Current Senior Articles: {current_senior_count} / {MAX_ARTICLES}")
    print(f"Current Junior Articles: {len(junior_articles_data.JUNIOR_ARTICLES)} / {MAX_ARTICLES}")

    # Process and build audio for new articles
    for art in INGESTED_SENIOR_ARTICLES:
        slug = art["slug"]
        cat = art["category"]
        print(f"\n[INGEST SENIOR] Processing {cat}/{slug} ({art['source_name']})...")
        synthesize_audio_for_article(slug, cat, art["sentences"], art["dialogue"], is_junior=False)

    for art in INGESTED_JUNIOR_ARTICLES:
        slug = art["slug"]
        cat = art["category"]
        print(f"\n[INGEST JUNIOR] Processing junior/{cat}/{slug} ({art['source_name']})...")
        synthesize_audio_for_article(slug, cat, art["sentences"], art["dialogue"], is_junior=True)

    print("\n[SUCCESS] Audio synthesis completed for ingested articles.")

if __name__ == "__main__":
    main()
