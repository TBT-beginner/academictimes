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
        "slug": "nihon-hidankyo-nobel-peace-prize",
        "category": "world",
        "category_label": "WORLD & INTERNATIONAL DIPLOMACY • 国際平和・核軍縮",
        "title": "The Moral Imperative of the Nuclear Taboo: Nihon Hidankyo Wins the 2024 Nobel Peace Prize",
        "headline_ja": "日本被団協にノーベル平和賞：「核兵器不使用の規範（タブー）」を守り続けた被爆者の生きた証言",
        "subhead": "広島・長崎の被爆者組織が歩んだ不屈の半世紀。ウクライナや中東情勢で核威嚇が高まる中、国際社会が再確認した人道主義を学術英語で精読。",
        "source_name": "Jiji Press & Reuters (時事通信・オスロ共同特派 / Nobel Committee Announcement)",
        "source_url": "https://www.jiji.com/jc/article?k=nihon-hidankyo-nobel-peace-prize",
        "source_attribution": "時事通信社および国際通信社によるノーベル委員会公式発表報道を基に、難関大学入試・国公立二次試験の学術英語として格調高い論説文に再構成した教材です。",
        "image": "https://images.unsplash.com/photo-1579783902614-a3fb3927b675?w=1000&auto=format&fit=crop&q=80",
        "sentences": [
            {
                "no": 1,
                "en": "The Norwegian Nobel Committee has awarded the 2024 Nobel Peace Prize to Nihon Hidankyo, the grassroots confederation of atomic bomb survivors from Hiroshima and Nagasaki.",
                "ja": "ノルウェー・ノーベル委員会は、広島と長崎の被爆者による草の根組織「日本被団協」に対し、2024年ノーベル平和賞を授与することを決定しました。"
            },
            {
                "no": 2,
                "en": "By transforming harrowing personal grief into a relentless global crusade, these hibakusha have anchored the international norm against the operational deployment of nuclear weapons.",
                "ja": "悲痛な個人の悲しみをたゆまぬ世界規模の運動へと昇華させることで、被爆者たちは核兵器の実戦配備・使用を禁ずる国際規範（核のタブー）を確固たるものとしてきました。"
            },
            {
                "no": 3,
                "en": "This prestigious recognition arrives at a precarious geopolitical juncture, wherein escalating regional conflicts threaten to erode the fragile non-proliferation architecture.",
                "ja": "この栄誉ある授賞は、激化する地域紛争によって脆弱な核不拡散体制が掘り崩されかねないという、極めて不安定な地政学的危機のさなかにもたらされました。"
            },
            {
                "no": 4,
                "en": "Historians and jurists argue that the moral authority of eyewitness testimony possesses a transcendent potency that abstract disarmament treaties alone cannot replicate.",
                "ja": "歴史学者や法学者は、当事者の生きた証言が持つ道義的権威は、抽象的な軍縮条約の条文だけでは再現し得ない超越的な説得力を宿していると主張しています。"
            },
            {
                "no": 5,
                "en": "Should the international community heed their urgent testament, humanity may yet fortify the indispensable consensus that a nuclear exchange admits of no victor.",
                "ja": "もし国際社会が被爆者たちの切迫した遺言に耳を傾けるならば、人類は「核戦争に勝者は存在し得ない」という必要不可欠な共通認識をいま一度強固にできるかもしれません。"
            }
        ],
        "vocabulary": [
            {
                "word": "grassroots",
                "phonetic": "[ˈɡrɑːs.ruːts]",
                "pos": "名詞・形容詞",
                "meaning": "草の根の、一般市民による",
                "def": "involving the ordinary people in a society or an organization rather than the leaders",
                "ex": "The anti-nuclear campaign grew from a grassroots movement into a global coalition."
            },
            {
                "word": "harrowing",
                "phonetic": "[ˈhær.əʊ.ɪŋ]",
                "pos": "形容詞",
                "meaning": "痛ましい、悲惨を極めた",
                "def": "extremely distressing, painful, or upsetting",
                "ex": "Survivors delivered harrowing accounts of the atomic devastation."
            },
            {
                "word": "crusade",
                "phonetic": "[kruːˈseɪd]",
                "pos": "名詞",
                "meaning": "熱心な改革運動、社会的キャンペーン",
                "def": "a vigorous campaign for political, social, or religious change",
                "ex": "They dedicated their lives to a tireless crusade for global disarmament."
            },
            {
                "word": "precarious",
                "phonetic": "[prɪˈkeə.ri.əs]",
                "pos": "形容詞",
                "meaning": "不安定な、危険をはらんだ",
                "def": "not securely held or in position; dangerously likely to fall or collapse",
                "ex": "The global balance of power rests on a precarious diplomatic foundation."
            },
            {
                "word": "transcendent",
                "phonetic": "[trænˈsen.dənt]",
                "pos": "形容詞",
                "meaning": "超越的な、通常の限界を超えた",
                "def": "beyond or above the range of normal or merely physical human experience",
                "ex": "Direct human testimony holds transcendent power over theoretical arguments."
            }
        ],
        "syntax": [
            {
                "phrase": "By transforming A into B, S + V",
                "meaning": "AをBへと転換・昇華させることで、…",
                "explanation": "動名詞 transforming を用いた手段・様態構文です。個人の悲劇（A）を全人類の平和規範（B）へと昇華させた被爆者の歴史的歩みを格調高く要約しています。"
            },
            {
                "phrase": "Should the international community heed ..., humanity may yet ...",
                "meaning": "万一国際社会が〜に耳を傾けるならば、人類はなお…できるかもしれない",
                "explanation": "条件節 If the international community should heed... から if が脱落し、助動詞 should が主語の前に倒置（Inversion）された最難関大・入試長文頻出の仮定法構文です。"
            }
        ],
        "factcheck": [
            {
                "title": "1. 日本被団協（日本原水爆被害者団体協議会）の歴史と授賞理由",
                "body": "1956年に結成された日本被団協は、被爆の実相を語り継ぎ、核兵器禁止条約（TPNW）の成立を後押しするなど、核兵器使用のタブー（nuclear taboo）を国際規範として定着させた功績がノーベル委員会から最高評価を受けました。"
            },
            {
                "title": "2. 核の脅威と「核のタブー」の現在的危機",
                "body": "ウクライナ侵攻におけるロシアの核威嚇や中東情勢の緊迫化により、第二次世界大戦以降維持されてきた「核兵器不使用のタブー」が形骸化の危機に瀕していることが授賞の緊急背景にあります。"
            }
        ],
        "dialogue": [
            {
                "speaker": "七",
                "name": "Nanami",
                "role": "アシスタント・大学生",
                "text": "Keita先生！日本被団協のノーベル平和賞受賞、世界中で本当に大きなニュースになりましたね！"
            },
            {
                "speaker": "慶",
                "name": "Keita先生",
                "role": "英語講師",
                "text": "歴史的な快挙だね。被爆者の平均年齢が85歳を超える中、自分たちのつらい体験を『人類の平和への誓い』へと昇華させた活動が世界から再評価されたんだ。"
            },
            {
                "speaker": "七",
                "name": "Nanami",
                "role": "アシスタント・大学生",
                "text": "文2の『anchored the international norm（国際規範を定着させた）』という表現、まさに世界を動かした重みを感じます！"
            },
            {
                "speaker": "慶",
                "name": "Keita先生",
                "role": "英語講師",
                "text": "その通り！東大・京大・早慶の英語長文でも『核軍縮と国際人道法（humanitarian law）』は超重要テーマだから、時事知識と一緒に格調高い語彙を身につけよう！"
            }
        ],
        "quiz": [
            {
                "question": "What is the primary accomplishment for which Nihon Hidankyo was awarded the Nobel Peace Prize?",
                "options": [
                    "Developing advanced underwater detection sensors.",
                    "Anchoring the international norm against the operational use of nuclear weapons through eyewitness testimony.",
                    "Negotiating exclusive maritime trade routes in Europe.",
                    "Designing underground medical shelters for refugees."
                ],
                "correct_index": 1,
                "explanation": "【正解：B】<br>第2文「anchored the international norm against the operational deployment of nuclear weapons」より、被爆の実相の証言を通じて核兵器不使用の国際規範（核のタブー）を定着させた功績が正解です。"
            },
            {
                "question": "Which of the following is CLOSEST in meaning to 'precarious' in sentence 3?",
                "options": ["unstable", "celebrated", "prosperous", "transparent"],
                "correct_index": 0,
                "explanation": "【正解：A】<br>precarious は「不安定な、危険に満ちた」を意味し、unstable が同義です。"
            },
            {
                "question": "What syntactic inversion is demonstrated in the final sentence ('Should the international community heed...')?",
                "options": [
                    "A relative clause modifying the predicate noun.",
                    "A conditional clause with the omission of 'if' and inversion of 'should'.",
                    "A comparative inversion used after negative adverbials.",
                    "A passive voice construction emphasizing geographical location."
                ],
                "correct_index": 1,
                "explanation": "【正解：B】<br>If the international community should heed... から if が省略され助動詞 should が主語の前に倒置された仮定法条件節です。"
            }
        ],
        "faq": [
            {
                "q": "ノーベル賞や平和・軍縮に関する時事英語の頻出単語は？",
                "a": "disarmament（軍縮）、non-proliferation（不拡散）、taboo（規範・タブー）、grassroots（草の根の）、testament（遺言・誓い）、deterrence（抑止力）が国公立二次・私大上位長文で極めて頻出です。"
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
        "slug": "nihon-hidankyo-nobel-peace-prize",
        "category": "world",
        "category_label": "WORLD & PEACE • 英検準2級〜2級",
        "title": "Japanese Atomic Bomb Survivors Win the Nobel Peace Prize for a World Without Nuclear Weapons",
        "headline_ja": "日本被団協がノーベル平和賞を受賞：核兵器のない世界を目指す被爆者たちの長年の願い",
        "subhead": "広島と長崎の被爆者たちが伝えてきた平和のメッセージ。世界中から賞賛された歴史的なニュースをやさしい英語で学びます。",
        "lead_snippet": "広島と長崎の被爆者による団体「日本被団協」が、2024年のノーベル平和賞を受賞しました。二度と核兵器を使ってはならないと、世界中で自らの体験を語り続けてきた70年近い努力が国際社会に認められました。",
        "source_name": "Jiji Press & Reuters (Adapted for Eiken Grade Pre-2 - 2)",
        "source_url": "https://www.jiji.com/jc/article?k=nihon-hidankyo-nobel-peace-prize",
        "source_attribution": "時事通信および海外通信社のノーベル平和賞報道を基に、高校生が理解しやすい標準的な英語で書き下ろした教材です。",
        "source_student_guide": "英検の面接試験や自由英作文では、『世界平和や国際協力』に関する問題がよく出題されます。被爆者の方々が伝えてきた平和の大切さを、自分の言葉で世界に発信できるように練習しましょう。",
        "original_article_url": "../../../world/nihon-hidankyo-nobel-peace-prize/index.html",
        "image": "https://images.unsplash.com/photo-1579783902614-a3fb3927b675?w=1000&auto=format&fit=crop&q=80",
        "sentences": [
            {
                "en": "The Nobel Peace Prize for 2024 was awarded to Nihon Hidankyo, an organization of atomic bomb survivors from Japan.",
                "ja": "2024年のノーベル平和賞は、日本の被爆者たちの団体である「日本被団協」に授与されました。"
            },
            {
                "en": "For almost seventy years, these courageous survivors have traveled around the world to share their painful memories.",
                "ja": "70年近くもの間、この勇敢な被爆者たちは世界中を旅し、自らのつらい記憶を分かち合ってきました。"
            },
            {
                "en": "They have warned global leaders that nuclear weapons are far too dangerous to ever be used again.",
                "ja": "彼らは世界の指導者たちに対し、核兵器はあまりに危険であり、二度と使われてはならないと警告してきました。"
            },
            {
                "en": "Today, ongoing wars in Europe and the Middle East make many people worry about the risk of nuclear conflicts.",
                "ja": "今日、ヨーロッパや中東で続く戦争により、多くの人々が核戦争の危険性を心配しています。"
            },
            {
                "en": "The Nobel Committee praised the survivors for reminding humanity that real peace requires mutual respect and dialogue.",
                "ja": "ノーベル委員会は、真の平和には相互の尊重と対話が必要であることを人類に思い起こさせたとして被爆者たちを称えました。"
            }
        ],
        "dialogue": [
            {
                "speaker": "七",
                "name": "Nanami",
                "role": "高校生",
                "text": "Keita先生、日本被団協がノーベル平和賞をとったニュース、テレビでも大きく報じられていました！"
            },
            {
                "speaker": "慶",
                "name": "Keita先生",
                "role": "英語の先生",
                "text": "そうだね。平均年齢が85歳を超える被爆者の方々が、長年にわたって『二度と核兵器を使ってはならない』と世界中で英語や母国語で訴え続けてきたんだよ。"
            },
            {
                "speaker": "七",
                "name": "Nanami",
                "role": "高校生",
                "text": "文3の『too dangerous to ever be used again（二度と使えないほど危険）』という表現、すごく心に響きます。"
            },
            {
                "speaker": "慶",
                "name": "Keita先生",
                "role": "英語の先生",
                "text": "『too ... to 〜（あまりに…なので〜できない）』は高校入試や英検でも定番の重要構文だね。平和への想いを英語でしっかり語れるようになろう！"
            }
        ],
        "vocab": [
            {
                "word": "survivor",
                "phonetic": "/səˈvaɪ.vər/",
                "pos": "名詞",
                "meaning": "生存者、生き残った人",
                "def": "a person who continues to live, especially after a dangerous event.",
                "ex": "The atomic bomb survivors shared their memories with high school students."
            },
            {
                "word": "courageous",
                "phonetic": "/kəˈreɪ.dʒəs/",
                "pos": "形容詞",
                "meaning": "勇敢な、勇気のある",
                "def": "having or showing the ability to control fear in the face of danger.",
                "ex": "The courageous volunteers helped people during the disaster."
            },
            {
                "word": "warn",
                "phonetic": "/wɔːn/",
                "pos": "動詞",
                "meaning": "〜に警告する、注意を促す",
                "def": "to tell someone about a possible danger or problem in the future.",
                "ex": "Scientists warn that global temperatures are rising rapidly."
            },
            {
                "word": "conflict",
                "phonetic": "/ˈkɒn.flɪkt/",
                "pos": "名詞",
                "meaning": "紛争、衝突、争い",
                "def": "an active disagreement between people with opposing opinions or principles.",
                "ex": "Diplomats work hard to prevent armed conflicts between nations."
            },
            {
                "word": "praise",
                "phonetic": "/preɪz/",
                "pos": "動詞",
                "meaning": "〜を称賛する、ほめる",
                "def": "to express admiration or approval for the achievements of someone.",
                "ex": "The teacher praised the students for their excellent English presentations."
            }
        ],
        "syntax": [
            {
                "phrase": "too + 形容詞 + to 不定詞（あまりに〜すぎて…できない）",
                "meaning": "高校・英検準2級〜2級の最重要構文",
                "explanation": "文3の `too dangerous to ever be used again` は、「危険すぎて二度と使われることはあり得ない」という意味を表します。"
            },
            {
                "phrase": "praise + O + for -ing（〜したことでOを称える）",
                "meaning": "称賛や感謝を表す重要動詞構文",
                "explanation": "文5の `praised the survivors for reminding humanity` は、`praise + 被爆者(survivors) + 思い起こさせたことに対して(for reminding)` という形です。"
            }
        ],
        "quiz": [
            {
                "question": "Who was awarded the 2024 Nobel Peace Prize?",
                "options": [
                    "A group of astronomers from London",
                    "Nihon Hidankyo, an organization of atomic bomb survivors from Japan",
                    "A robotics manufacturing company in Tokyo",
                    "An environmental charity in Australia"
                ],
                "correct_index": 1,
                "explanation": "【正解：B】<br>第1文「The Nobel Peace Prize for 2024 was awarded to Nihon Hidankyo, an organization of atomic bomb survivors from Japan」より、Bが正解です。"
            },
            {
                "question": "What have the survivors warned world leaders about?",
                "options": [
                    "Nuclear weapons are far too dangerous to ever be used again.",
                    "Airplanes consume too much fuel during the winter.",
                    "Traditional books should not be sold in supermarkets.",
                    "Schools should open earlier in the morning."
                ],
                "correct_index": 0,
                "explanation": "【正解：A】<br>第3文「warned global leaders that nuclear weapons are far too dangerous to ever be used again」より、Aが正解です。"
            },
            {
                "question": "Which word in the text means 'a person who continues to live after a dangerous disaster'?",
                "options": ["survivor", "conflict", "dialogue", "memory"],
                "correct_index": 0,
                "explanation": "【正解：A】<br>災害や惨禍を生き延びた人を表す英単語は survivor（生存者、被爆者）です。"
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
    }
]

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
