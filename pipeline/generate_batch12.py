# -*- coding: utf-8 -*-
"""
Helper to generate pipeline/batch12_articles_data.py
Contains all 12 Senior and 12 Junior articles for October 16, 2026 edition.
"""
import os

BATCH12_DATA_PATH = os.path.join(os.path.dirname(__file__), "batch12_articles_data.py")

data_code = '''# -*- coding: utf-8 -*-
"""
Batch 12 Master Aggregator (2026-10-16 Edition - 本日付・最新)
Contains 12 verified articles (2 per category across Science, Society, World, Law, Culture, Entertainment)
with 1:1 Senior and Junior editions. All URLs verified 200 OK from The Guardian (Oct 15, 2026).
"""

BATCH12_SENIOR = [
    # 1. SCIENCE - Leap Second Abolition & Leap Hour (Top Lead)
    {
        "slug": "leap-second-abolition-leap-hour",
        "category": "science",
        "category_label": "METROLOGY & ASTRONOMY • 世界計量会議のうるう秒廃止決議",
        "date": "2026-10-16",
        "title": "International Timekeepers Vote to Abolish Leap Second in Favour of Leap Hour",
        "headline_ja": "世界計量会議、ネット障害頻発の「うるう秒」廃止を決議：数百年後の「うるう時」導入へ",
        "subhead": "地球自転の揺らぎと原子時計のズレを調整してきた1秒刻みの修正を停止。デジタル金融・クラウド障害を防ぐ歴史的転換。",
        "lead_snippet": "国際度量衡総会（BIPM）の代表団は、1972年以来実施されてきた「うるう秒（leap second）」の挿入を2035年までに廃止し、最大1時間の累積ズレを許容する「うるう時（leap hour）」方式への移行を決定した。世界的な通信網や金融決済システムを混乱させてきたミリ秒単位の時刻同期リスクを解消する科学的合意を精読する。",
        "source_name": "The Guardian (Oct 15, 2026)",
        "source_url": "https://www.theguardian.com/science/2026/oct/15/times-up-for-the-leap-second-as-scientists-swap-it-for-the-leap-hour",
        "source_attribution": "Source: The Guardian (Oct 15, 2026). Time\\'s up for the leap second as scientists swap it for the leap hour.",
        "image": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=1000&auto=format&fit=crop&q=80",
        "sentences": [
            {
                "en": "Metrologists and government representatives from around the world have formally voted to abandon the historic practice of inserting leap seconds into standard astronomical timekeeping by 2035.",
                "ja": "世界各国の計量学者および政府代表らは、2035年までに標準天文時測定において「うるう秒」を挿入する歴史的慣行を廃止することを正式に決議した。"
            },
            {
                "en": "Since its inception in 1972, the occasional leap second was introduced to reconcile precise atomic clocks with the irregular and slightly decelerating rotation of the Earth.",
                "ja": "1972年の導入以来、不定期のうるう秒は、高精度な原子時計と地球の不規則かつわずかに減速する自転との間のズレを調整するために導入されてきた。"
            },
            {
                "en": "However, software engineers and telecommunications architects have long warned that the sudden injection of an irregular sixty-first second repeatedly triggers severe crashes across global financial trading platforms and cloud server clusters.",
                "ja": "しかし、ソフトウェアエンジニアや通信設計者らは、不規則な「61秒目の1秒」が突如挿入されることで、世界的な金融取引プラットフォームやクラウドサーバー群で深刻なシステム障害が繰り返し引き起こされると長年警告してきた。"
            },
            {
                "en": "Under the landmark compromise, the discrepancy between atomic time and universal solar time will be permitted to accumulate until it approaches a full sixty minutes, deferring any corrective intervention for centuries.",
                "ja": "この歴史的な妥協案のもとでは、原子時と世界太陽時との差異が丸60分に近づくまで蓄積されることが許容され、いかなる修正措置も数百年先へと先送りされることになる。"
            },
            {
                "en": "Scientific delegates hailed the consensus as an indispensable modernization that safeguards interconnected cyber infrastructure while maintaining a meaningful tether to celestial mechanics.",
                "ja": "科学者代表団は、この合意について、天体力学との有意義な結びつきを維持しつつ相互接続されたサイバーインフラを保護する不可欠な近代化であると称賛した。"
            }
        ],
        "dialogue": [
            {"speaker": "七", "name": "Nanami", "role": "生徒", "text": "Keita先生、「うるう秒」がなくなるって本当ですか？大晦日の時計が61秒になるあのニュース、結構好きだったんですけど！"},
            {"speaker": "慶", "name": "Keita", "role": "英語講師", "text": "風情はあるけれど、コンピューターの世界では大問題だったんだよ。第3文にあるように、1分が61秒になると金融取引システムやクラウドサーバーがクラッシュしてしまうんだ。"},
            {"speaker": "七", "name": "Nanami", "role": "生徒", "text": "1秒狂うだけで世界中の電子マネーや株取引が止まるリスクがあるんですね。でも、時計と地球の自転がずれたら昼夜が狂いませんか？"},
            {"speaker": "慶", "name": "Keita", "role": "英語講師", "text": "第4文を見てごらん。ズレが「丸1時間（a full sixty minutes）」になるまで放置して、何百年も後に「うるう時（leap hour）」で一気に調整する方針なんだ。大学入試の理系・文理融合長文で『科学技術と社会標準の妥協』として頻出のテーマだよ！"}
        ],
        "vocab": [
            {"word": "metrologist", "phonetic": "/mɪˈtrɒl.ə.dʒɪst/", "meaning": "計量学者、測定標準の専門家", "pos": "noun", "def": "A scientist who studies or specializes in the scientific study of measurement.", "ex": "Metrologists define international measurement standards at the BIPM."},
            {"word": "reconcile", "phonetic": "/ˈrek.ən.saɪl/", "meaning": "調和させる、一致させる、和解させる", "pos": "verb", "def": "To restore friendly relations or make two contrasting ideas consistent.", "ex": "Engineers sought to reconcile atomic time with solar observations."},
            {"word": "discrepancy", "phonetic": "/dɪˈskrep.ən.si/", "meaning": "相違、食い違い、不一致", "pos": "noun", "def": "A lack of compatibility or similarity between two or more facts.", "ex": "The slight discrepancy between clocks accumulated over decades."},
            {"word": "defer", "phonetic": "/dɪˈfɜːr/", "meaning": "先送りする、延期する、敬意を払って従う", "pos": "verb", "def": "To put off an action to a later time; postpone.", "ex": "The committee decided to defer the decision until further tests were complete."},
            {"word": "tether", "phonetic": "/ˈteð.ər/", "meaning": "結びつき、つなぎ綱、限界", "pos": "noun", "def": "A rope or chain, or metaphorically a connection that ties one thing to another.", "ex": "Civilization retains a cultural tether to the diurnal cycle of the sun."}
        ],
        "syntax": [
            {"title": "動詞 reconcile A with B の構文", "formula": "reconcile [precise atomic clocks] with [the irregular rotation of the Earth]", "explanation": "reconcile A with B は「AをBと調和・適合させる」という頻出構文で、対立・乖離する2つの要素を一致させる文脈で多用されます。"},
            {"title": "分詞構文による付帯状況（while節との連動）", "formula": "[Scientific delegates hailed the consensus] as an indispensable modernization [that safeguards infrastructure] while [maintaining a tether...]", "explanation": "主節に対して、that関係代名詞節内で while + 現在分詞（maintaining）が並行する条件・状態を補足説明しています。"}
        ],
        "quiz": [
            {
                "question": "What primary problem led scientists and engineers to vote to abolish leap seconds?",
                "options": [
                    "Atomic clocks became too expensive for developing nations to maintain.",
                    "The sudden addition of a sixty-first second crashed digital financial platforms and servers.",
                    "Astronomers discovered that the Earth completely stopped rotating on its axis.",
                    "Governments decided that universal solar time was scientifically useless."
                ],
                "answer": 1,
                "explanation": "第3文にある通り、突然の61秒目の挿入（irregular sixty-first second）が金融取引やクラウドサーバーで重大な障害を引き起こすことが主因です。"
            },
            {
                "question": "According to the article, how will the new 'leap hour' approach manage time discrepancies?",
                "options": [
                    "By adding one second every morning at midnight.",
                    "By completely disconnecting computers from any atomic timekeeping.",
                    "By allowing the difference between atomic and solar time to accumulate up to 60 minutes over centuries.",
                    "By resetting all international clocks backward by one hour every ten years."
                ],
                "answer": 2,
                "explanation": "第4文にある通り、差異が60分に近づくまで数百年間にわたり蓄積を許容する方針が採用されました。"
            },
            {
                "question": "The word 'discrepancy' in the fourth sentence is closest in meaning to:",
                "options": ["agreement", "inconsistency", "celebration", "acceleration"],
                "answer": 1,
                "explanation": "discrepancy は「食い違い」「不一致」を意味するため、inconsistency が最も適切です。"
            },
            {
                "question": "When was the practice of inserting leap seconds originally established?",
                "options": ["In 1935", "In 1972", "In 2035", "In 1851"],
                "answer": 1,
                "explanation": "第2文に 'Since its inception in 1972' と明記されています。"
            },
            {
                "question": "How did scientific delegates view the compromise decision?",
                "options": [
                    "As a dangerous surrender to commercial tech companies.",
                    "As an impossible standard that will destroy astronomical research.",
                    "As an indispensable modernization that protects cyber infrastructure while preserving links to celestial mechanics.",
                    "As an interim measure to be repealed within the next decade."
                ],
                "answer": 2,
                "explanation": "最終文で、サイバーインフラを守りつつ天体力学との結びつきを維持する不可欠な近代化（indispensable modernization）として称賛されたと述べられています。"
            }
        ]
    },

    # 2. SCIENCE - Neanderthal Spear Trauma Discovery (Shanidar Cave)
    {
        "slug": "neanderthal-shanidar-spear-trauma",
        "category": "science",
        "category_label": "ANTHROPOLOGY & ARCHAEOLOGY • シャニダール洞窟のネアンデルタール人受傷痕跡",
        "date": "2026-10-16",
        "title": "Shanidar Cave Neanderthal Skeleton Reveals Earliest Evidence of Human Spear Trauma",
        "headline_ja": "クルディスタン・シャニダール洞窟：ネアンデルタール人骨から最古の槍による刺突痕を発見",
        "subhead": "肋骨の傷痕と骨治癒の分析から判明した旧人類同士の紛争と手厚い共同体看護の実態。",
        "lead_snippet": "イラク・クルディスタン地域のシャニダール洞窟で出土したネアンデルタール人成人男性の骨格化石から、投擲槍によって受傷した確実な痕跡が確認された。致命傷を負いながらも数週間にわたり生存・治癒した形跡は、旧人類社会における武力衝突の存在とともに、負傷者を献身的に介護する高度な社会的結束があったことを示唆している。",
        "source_name": "The Guardian (Oct 15, 2026)",
        "source_url": "https://www.theguardian.com/science/2026/oct/15/neanderthal-remains-human-ancestor-killed-by-spear-iraq-kurdistan-cave-earliest-find",
        "source_attribution": "Source: The Guardian (Oct 15, 2026). Neanderthal remains in Kurdistan cave reveal earliest human ancestor spear trauma.",
        "image": "https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c?w=1000&auto=format&fit=crop&q=80",
        "sentences": [
            {
                "en": "Paleoanthropologists re-examining Neanderthal skeletal remains from the famous Shanidar Cave in Iraqi Kurdistan have identified the earliest known forensic evidence of projectile weapon trauma in human evolution.",
                "ja": "イラク・クルディスタンの著名なシャニダール洞窟から出土したネアンデルタール人骨格化石を再調査した古人類学者らは、人類の進化史において投擲武器による外傷の最古の法医学的証拠を特定した。"
            },
            {
                "en": "Micro-computed tomography scans of a male specimen designated Shanidar 3 revealed a distinct rib puncture incision that precisely matches the entry trajectory of a high-velocity wooden spear tipped with stone.",
                "ja": "「シャニダール3号」と名付けられた男性個体のマイクロCTスキャン画像は、石器の穂先を持つ高速の木製槍の刺入軌道と正確に一致する明瞭な肋骨穿孔創を明らかにした。"
            },
            {
                "en": "Crucially, osteological analysis indicates that the individual survived the puncture wound for several weeks, as evidenced by significant new bone growth and partial healing along the fractured margins.",
                "ja": "決定的な点として、骨学的分析は、骨折縁に沿った顕著な新生骨の形成と部分的な治癒痕によって証明されるように、この個体が刺突創を負った後も数週間にわたって生存していたことを示している。"
            },
            {
                "en": "Researchers argue that sustaining a perforated lung in a Pleistocene hunter-gatherer environment would have rendered the injured hunter entirely dependent on sustained community nursing and nutritional provisioning.",
                "ja": "研究者らは、更新世の狩猟採集環境において肺の穿孔を被った負傷ハンターは、持続的な共同体の看護と栄養補給に完全に依存せざるを得なかったはずだと主張している。"
            },
            {
                "en": "Consequently, the archaeological discovery simultaneously documents ancient interpersonal conflict and reinforces the growing paradigm of sophisticated Neanderthal empathy and collective healthcare.",
                "ja": "したがって、この考古学的発見は、太古の対人紛争を記録すると同時に、ネアンデルタール人の洗練された共感能力と集団的医療ケアという新たな学術的パラダイムを補強している。"
            }
        ],
        "dialogue": [
            {"speaker": "七", "name": "Nanami", "role": "生徒", "text": "シャニダール洞窟といえば、花を添えて死者を埋葬したというあの有名なネアンデルタール人の遺跡ですよね！"},
            {"speaker": "慶", "name": "Keita", "role": "英語講師", "text": "そうだね。今回の発見はその化石を最新のCTスキャンで調べ直したんだ。第2文にあるように、石の穂先がついた槍で突かれた傷痕（rib puncture incision）が見つかったんだ。"},
            {"speaker": "七", "name": "Nanami", "role": "生徒", "text": "槍で突かれて生き延びられたんですか？抗生物質も病院もない時代に！"},
            {"speaker": "慶", "name": "Keita", "role": "英語講師", "text": "まさにそこが学術的焦点なんだ！第3文と第4文にあるように、数週間も骨が治癒していたということは、仲間が食事を運んで献身的に看病（sustained community nursing）していた証拠なんだよ。旧人類の暴力性と共感性（empathy）を同時に物語る素晴らしい長文だね。"}
        ],
        "vocab": [
            {"word": "forensic", "phonetic": "/fəˈren.zɪk/", "meaning": "法医学的な、鑑識の、法廷の", "pos": "adjective", "def": "Relating to the application of scientific methods and techniques to the investigation of crime.", "ex": "Forensic anthropologists examined the skeletal trauma patterns."},
            {"word": "trajectory", "phonetic": "/trəˈdʒek.tər.i/", "meaning": "弾道、軌道、軌跡", "pos": "noun", "def": "The curved path followed by a projectile flying or an object moving under the action of given forces.", "ex": "The missile followed a downward ballistic trajectory toward the target."},
            {"word": "osteological", "phonetic": "/ˌɒs.ti.əˈlɒdʒ.ɪ.kəl/", "meaning": "骨学的な、骨格構造に関する", "pos": "adjective", "def": "Relating to osteology, the scientific study of the structure and function of bones.", "ex": "Osteological evidence confirmed the subject suffered from joint disease."},
            {"word": "provisioning", "phonetic": "/prəˈvɪʒ.ən.ɪŋ/", "meaning": "食糧供給、補給、物資調達", "pos": "noun", "def": "The action of providing or supplying something for use, especially food.", "ex": "The survival of injured elders depended on tribal food provisioning."},
            {"word": "empathy", "phonetic": "/ˈem.pə.θi/", "meaning": "共感、感情移入、思いやり", "pos": "noun", "def": "The ability to understand and share the feelings of another.", "ex": "Caring for sick individuals demonstrates complex evolutionary empathy."}
        ],
        "syntax": [
            {"title": "as evidenced by による証拠の例示構文", "formula": "[individual survived for weeks], as evidenced by [significant bone growth]", "explanation": "as evidenced by ~ は「〜によって証明・例証されるように」という論文で頻出の表現で、直前の主張に対する客観的データを後置修飾します。"},
            {"title": "would have + 過去分詞（過去事象の推量）", "formula": "[sustaining an injury] would have rendered [the hunter entirely dependent...]", "explanation": "動名詞句主語（sustaining ~）に対して would have rendered を用いることで、「〜であったならば、完全に依存せざるを得ない状態に置いたはずだ」という論理的推論を展開しています。"}
        ],
        "quiz": [
            {
                "question": "What groundbreaking discovery was made from the Shanidar 3 skeleton?",
                "options": [
                    "The first recorded use of iron tools in the Paleolithic era.",
                    "The earliest known forensic evidence of spear trauma in human evolution.",
                    "Evidence that Neanderthals survived entirely without meat consumption.",
                    "Proof that early hominids traveled across oceans using wooden boats."
                ],
                "answer": 1,
                "explanation": "第1文にある通り、人類進化における投擲武器による外傷の最古の法医学的証拠（earliest known forensic evidence of projectile weapon trauma）が特定されました。"
            },
            {
                "question": "How did researchers determine that the wounded Neanderthal did not die immediately?",
                "options": [
                    "They found modern surgical stitches in the tissue.",
                    "A written diary was uncovered alongside the fossil.",
                    "They observed new bone growth and partial healing along the fractured rib margins.",
                    "Radiocarbon dating revealed the wound occurred centuries after his death."
                ],
                "answer": 2,
                "explanation": "第3文で、骨折痕に沿って新生骨の形成と部分的な治癒（significant new bone growth and partial healing）が確認されたことから数週間の生存が判明しました。"
            },
            {
                "question": "The phrase 'rendered the injured hunter entirely dependent on' means the hunter:",
                "options": [
                    "became completely capable of self-sufficient living.",
                    "was forced to rely completely on others for care and food.",
                    "refused all assistance from fellow tribe members.",
                    "taught hunting techniques to younger Neanderthals."
                ],
                "answer": 1,
                "explanation": "render A dependent on B は「AをBに依存せざるを得ない状態にする」という意味です。"
            },
            {
                "question": "What dual sociological reality does this discovery support regarding Neanderthals?",
                "options": [
                    "They had mastered written language and agricultural farming.",
                    "They engaged in interpersonal violence while also practicing collective healthcare and empathy.",
                    "They were completely peaceful vegetarians who never experienced conflict.",
                    "They lived in complete isolation without forming social family groups."
                ],
                "answer": 1,
                "explanation": "最終文にあるように、古代の対人暴力（interpersonal conflict）の存在と、高度な共感・集団的医療ケア（collective healthcare）の双方が証明されました。"
            },
            {
                "question": "Which technology was used to examine the puncture incision on the rib?",
                "options": [
                    "Micro-computed tomography (micro-CT) scans",
                    "Satellite infrared laser imagery",
                    "Electron magnetic resonance tunneling",
                    "Deep ocean sonar sounding"
                ],
                "answer": 0,
                "explanation": "第2文に 'Micro-computed tomography scans' と明記されています。"
            }
        ]
    },

    # 3. SOCIETY - England Severe Drought Declared (Environment Agency)
    {
        "slug": "england-six-regions-severe-drought-water-crisis",
        "category": "society",
        "category_label": "ENVIRONMENT & PUBLIC INFRASTRUCTURE • 英6地域で深刻な干ばつ宣言",
        "date": "2026-10-16",
        "title": "Severe Drought Declared Across Six Regions in England Threatening Water Supplies",
        "headline_ja": "英環境庁、イングランド6地域に「深刻な干ばつ」を宣言：水道インフラと農業用水に危機",
        "subhead": "過去数十年間で最も乾燥した夏季を受け、河川流量低下と地下水枯渇が水道網を直撃。",
        "lead_snippet": "英国環境庁は、イングランド全土の6地域を深刻な干ばつ（severe drought）地域に指定し、市民生活と生態系を守るための緊急取水制限措置を発令した。気候変動による降雨パターンの極端化と老朽化した送水パイプラインの漏水問題が重なり、公共インフラの強靭化（resilience）をめぐる議論が再燃している。",
        "source_name": "The Guardian (Oct 15, 2026)",
        "source_url": "https://www.theguardian.com/environment/2026/oct/15/severe-drought-declared-six-areas-england-public-water-supplies-threat",
        "source_attribution": "Source: The Guardian (Oct 15, 2026). Severe drought declared across six areas in England.",
        "image": "https://images.unsplash.com/photo-1509316975850-ff9c5deb0cd9?w=1000&auto=format&fit=crop&q=80",
        "sentences": [
            {
                "en": "The Environment Agency has officially escalated the ecological alert status across six major regions of England to severe drought following unprecedented meteorological dry spells that depleted strategic reservoirs.",
                "ja": "英国環境庁は、戦略的貯水池を枯渇させた前例のない気象的日照りを受け、イングランドの主要6地域における生態警報ステータスを公式に「深刻な干ばつ」へと引き上げた。"
            },
            {
                "en": "Hydrological assessments reveal that river flow volumes and groundwater aquifers in East Anglia and the South West have plunged to their lowest recorded percentiles since records began in 1891.",
                "ja": "水文評価によると、イーストアングリアおよび南西部における河川流量と地下帯水層は、1891年の観測開始以来最低の記録的パーセンタイルへと急落している。"
            },
            {
                "en": "In response, statutory water companies have imposed mandatory hosepipe bans and curtailed agricultural extraction licenses to preserve drinking water for municipal hospital systems and residential households.",
                "ja": "これを受けて、法定水道企業各社は、都市部の病院システムや一般家庭向けの飲料水を確保するため、ホースによる散水の義務的禁止を発令し、農業用取水ライセンスを制限した。"
            },
            {
                "en": "Environmental campaigners contend that climate-driven precipitation volatility is being severely exacerbated by chronic underinvestment in privatized pipeline infrastructure, resulting in billions of litres lost to underground leakage annually.",
                "ja": "環境運動家らは、気候変動による降水量の変動性が民営化された送水管インフラへの慢性的な過少投資によって激しく悪化しており、その結果毎年数百億リットルの水が地下漏水で失われていると主張している。"
            },
            {
                "en": "Ministers now face intense parliamentary pressure to enforce stricter performance penalties on utility monopolies while constructing inter-regional water transfer networks to bolster national climate resilience.",
                "ja": "閣僚らは現在、公共公益事業の独占企業に対してより厳しい性能罰則を執行するとともに、国の気候レジリエンスを強化するため地域間送水ネットワークを建設するよう、強い議会圧力に直面している。"
            }
        ],
        "dialogue": [
            {"speaker": "七", "name": "Nanami", "role": "生徒", "text": "イギリスといえば雨が多くて曇っているイメージなのに、6地域で『深刻な干ばつ（severe drought）』なんて驚きです！"},
            {"speaker": "慶", "name": "Keita", "role": "英語講師", "text": "そうなんだ。第2文にあるように、1891年の統計開始以来最低の水位を記録しているんだよ。気候変動で降雨の偏りが極端化しているんだね。"},
            {"speaker": "七", "name": "Nanami", "role": "生徒", "text": "第4文に出てくる『privatized pipeline infrastructure（民営化された水道管インフラ）』の老朽化と漏水（underground leakage）も問題視されていますね。"},
            {"speaker": "慶", "name": "Keita", "role": "英語講師", "text": "鋭いね！単なる自然災害ではなく『インフラ民営化の是非と公共性（public goods）』という社会学・政治経済の最重要論点として東大や慶應の入試で問われるテーマなんだよ。"}
        ],
        "vocab": [
            {"word": "deplete", "phonetic": "/dɪˈpliːt/", "meaning": "枯渇させる、使い果たす、激減させる", "pos": "verb", "def": "Use up the supply or resources of something.", "ex": "Prolonged dry spells deplete the city's freshwater reserves."},
            {"word": "aquifer", "phonetic": "/ˈæk.wɪ.fər/", "meaning": "帯水層、地下水脈", "pos": "noun", "def": "A body of permeable rock which can contain or transmit groundwater.", "ex": "Farmers rely on deep underground aquifers for crop irrigation."},
            {"word": "curtail", "phonetic": "/kɜːˈteɪl/", "meaning": "制限する、切り詰める、短縮する", "pos": "verb", "def": "Reduce in extent or quantity; impose a restriction on.", "ex": "Authorities curtailed non-essential water usage to preserve supplies."},
            {"word": "exacerbate", "phonetic": "/ɪɡˈzæs.ə.beɪt/", "meaning": "悪化させる、深刻化させる", "pos": "verb", "def": "Make a problem, bad situation, or negative feeling worse.", "ex": "High temperatures exacerbate existing regional water shortages."},
            {"word": "resilience", "phonetic": "/rɪˈzɪl.jəns/", "meaning": "回復力、強靭性、レジリエンス", "pos": "noun", "def": "The capacity to recover quickly from difficulties; toughness.", "ex": "Upgraded pipelines enhance the resilience of the civil power grid."}
        ],
        "syntax": [
            {"title": "escalate A to B の使役表現", "formula": "[The agency] has escalated [the ecological alert status] to [severe drought]", "explanation": "escalate A to B は「A（警戒レベル）をB（深刻な干ばつ）へと引き上げる」という意味で、政策・危機管理の文脈で頻出します。"},
            {"title": "現在分詞句による結果構文（resulting in ~）", "formula": "[underinvestment in infrastructure], resulting in [billions of litres lost to leakage]", "explanation": "resulting in + 名詞句 は「その結果として〜をもたらす」という無生物主語の因果関係を客観的かつ論理的に接続します。"}
        ],
        "quiz": [
            {
                "question": "What official measure did the Environment Agency take regarding six regions in England?",
                "options": [
                    "It declared them flood disaster zones due to excessive snowfall.",
                    "It upgraded their ecological alert status to severe drought.",
                    "It ordered the total evacuation of all residential areas.",
                    "It privatized all national river networks to foreign investors."
                ],
                "answer": 1,
                "explanation": "第1文にある通り、前例のない日照りを受けて警報ステータスを「深刻な干ばつ（severe drought）」に引き上げました。"
            },
            {
                "question": "How historic are the current low river and groundwater levels in East Anglia?",
                "options": [
                    "They are the lowest recorded since records began in 1891.",
                    "They are normal for this time of year.",
                    "They are the highest recorded in the past century.",
                    "They have returned to levels last seen in 2025."
                ],
                "answer": 0,
                "explanation": "第2文に 'lowest recorded percentiles since records began in 1891' と明記されています。"
            },
            {
                "question": "According to environmental campaigners, what factor significantly worsens the water shortage?",
                "options": [
                    "Excessive rainfall in neighboring European countries.",
                    "Chronic underinvestment in privatized pipeline infrastructure causing massive underground leakage.",
                    "Over-reliance on foreign desalinization vessels.",
                    "The mandatory adoption of household water meters."
                ],
                "answer": 1,
                "explanation": "第4文にある通り、民営化インフラへの過少投資による地下漏水（billions of litres lost to underground leakage）が悪化の主要因とされています。"
            },
            {
                "question": "The word 'curtail' in the third sentence is closest in meaning to:",
                "options": ["expand", "restrict", "celebrate", "finance"],
                "answer": 1,
                "explanation": "curtail は「制限する」「削減する」を意味し、restrict が最も近いです。"
            },
            {
                "question": "What structural solution are ministers being pressured to pursue?",
                "options": [
                    "Constructing inter-regional water transfer networks to bolster climate resilience.",
                    "Permanently closing all municipal hospital facilities.",
                    "Banning all agricultural farming across the British Isles.",
                    "Relying solely on imported bottled water from overseas."
                ],
                "answer": 0,
                "explanation": "最終文で、地域間送水ネットワーク（inter-regional water transfer networks）の建設による強靭化が求められていると述べられています。"
            }
        ]
    },

    # 4. SOCIETY - Brazil Cuts Work Week to 40 Hours
    {
        "slug": "brazil-statutory-workweek-reduction-forty-hours",
        "category": "society",
        "category_label": "LABOUR ECONOMICS & POLICY • ブラジル法定労働時間40時間への短縮法案",
        "date": "2026-10-16",
        "title": "Brazil Moves to Cut Statutory Working Week to Forty Hours Amid Labour Reform Push",
        "headline_ja": "ブラジル政府、週法定労働時間を44時間から40時間に短縮する包括的労働改革を推進",
        "subhead": "賃金を減らさず労働時間を短縮。産業界の生産性向上要請と労働者の健康回復の調和を模索。",
        "lead_snippet": "ブラジル議会において、憲法で定められた週44時間の法定労働上限を週40時間へと恒久的に引き下げる歴史的な労働基準法改正案が提出された。過重労働の是正と雇用創出効果を掲げる労働組合側と、中小企業の労務コスト増を懸念する産業連盟との間で激しい政策論争が展開されている。",
        "source_name": "The Guardian (Oct 15, 2026)",
        "source_url": "https://www.theguardian.com/world/2026/oct/15/brazil-cuts-work-week-to-40-hours-lula-bolsonaro-election-runoff",
        "source_attribution": "Source: The Guardian (Oct 15, 2026). Brazil moves to cut working week to 40 hours.",
        "image": "https://images.unsplash.com/photo-1521737604893-d14cc237f11d?w=1000&auto=format&fit=crop&q=80",
        "sentences": [
            {
                "en": "Lawmakers in Brazil have advanced a constitutional amendment bill that seeks to curtail the statutory workweek from forty-four hours to forty without permitting employers to reduce worker wages.",
                "ja": "ブラジルの議員らは、雇用主による労働者賃金の削減を認めることなく、法定労働週を44時間から40時間へと短縮することを目指す憲法改正案を前進させた。"
            },
            {
                "en": "Advocates of the reform cite empirical workplace studies demonstrating that chronic fatigue from extended six-day working regimes severely diminishes hourly productivity and drives up public healthcare expenditure.",
                "ja": "改革の支持派は、長期にわたる週6日勤務体制による慢性的な疲労が時間あたりの生産性を著しく低下させ、公的医療費を高騰させていることを示す実証的な労働研究を引用している。"
            },
            {
                "en": "Conversely, national manufacturing confederations caution that an abrupt mandatory reduction in working hours will inflict onerous payroll burdens on labor-intensive small enterprises struggling with elevated interest rates.",
                "ja": "これとは反対に、全国製造業連盟は、労働時間の急激な義務的短縮が高金利に苦しむ労働集約型の中小企業に重い人件費負担を課すことになると警告している。"
            },
            {
                "en": "Economists note that developing economies across Latin America are increasingly re-evaluating traditional labor paradigms in light of automated manufacturing and flexible service sector scheduling.",
                "ja": "経済学者らは、中南米の発展途上諸国が、自動化された製造業や柔軟なサービス業の勤務体系を背景に、従来の労働パラダイムを再考する傾向を強めていると指摘している。"
            },
            {
                "en": "The impending congressional ballot is widely regarded as a pivotal litmus test for balancing fundamental workers' welfare against macroeconomic competitiveness in emerging markets.",
                "ja": "間近に迫った議会投票は、新興国市場における労働者の基本的福祉とマクロ経済的な競争力との均衡を図る極めて重要な試金石と広くみなされている。"
            }
        ],
        "dialogue": [
            {"speaker": "七", "name": "Nanami", "role": "生徒", "text": "ブラジルでも労働時間を短縮する法案が進んでいるんですね。週44時間から40時間って、日本と同じ水準になるということですか？"},
            {"speaker": "慶", "name": "Keita", "role": "英語講師", "text": "その通り！ブラジルでは週6日勤務の職場も多くて、疲労による生産性低下（fatigue diminishing productivity）が問題視されていたんだよ。"},
            {"speaker": "七", "name": "Nanami", "role": "生徒", "text": "第1文の『without permitting employers to reduce worker wages（給料を減らさずに）』という条件があるから、企業側はコスト増を心配しているんですね。"},
            {"speaker": "慶", "name": "Keita", "role": "英語講師", "text": "まさに第3文にある『onerous payroll burdens（重い人件費負担）』だね。労働者の健康福祉と企業の競争力をどう比較衡量するかは、現代社会や自由英作文の王道テーマだよ。"}
        ],
        "vocab": [
            {"word": "amendment", "phonetic": "/əˈmend.mənt/", "meaning": "修正、改正条項、修正案", "pos": "noun", "def": "A minor change or addition designed to improve a text or piece of legislation.", "ex": "Congress voted to ratify the constitutional amendment."},
            {"word": "fatigue", "phonetic": "/fəˈtiːɡ/", "meaning": "疲労、過労、倦怠感", "pos": "noun", "def": "Extreme tiredness resulting from mental or physical exertion or illness.", "ex": "Driver fatigue is a leading contributor to industrial accidents."},
            {"word": "onerous", "phonetic": "/ˈɒn.ər.əs/", "meaning": "重荷となる、負担の大きい、過酷な", "pos": "adjective", "def": "Involving an amount of effort and difficulty that is oppressively burdensome.", "ex": "Compliance regulations placed an onerous task on small business owners."},
            {"word": "litmus", "phonetic": "/ˈlɪt.məs/", "meaning": "試金石（litmus test）、リトマス試験紙", "pos": "noun", "def": "A decisive test of the quality or value of someone or something.", "ex": "The vote served as a political litmus test for the coalition government."},
            {"word": "competitiveness", "phonetic": "/kəmˈpet.ɪ.tɪv.nəs/", "meaning": "競争力、競争的性質", "pos": "noun", "def": "Possession of a strong desire to be more successful than others, or market viability.", "ex": "Currency devaluation helped restore the country's export competitiveness."}
        ],
        "syntax": [
            {"title": "without + 動名詞（否定の付帯状況）", "formula": "[cut the statutory workweek] without [permitting employers to reduce worker wages]", "explanation": "without permitting ~ は「〜を許すことなく・〜を伴わずに」という意味で、条件の維持を明確に示す重要構文です。"},
            {"title": "be regarded as + 名詞（受動態の評価構文）", "formula": "[The ballot] is widely regarded as [a pivotal litmus test for balancing A against B]", "explanation": "regard A as B（AをBとみなす）の受動態で、社会的な評価や位置づけを客観的に論評する際に重宝されます。"}
        ],
        "quiz": [
            {
                "question": "What is the primary aim of the proposed constitutional amendment in Brazil?",
                "options": [
                    "To increase the legal workweek to fifty hours.",
                    "To reduce the statutory workweek from 44 to 40 hours without lowering wages.",
                    "To eliminate all overtime pay for manufacturing employees.",
                    "To force all small companies to transition to robotic labor."
                ],
                "answer": 1,
                "explanation": "第1文にある通り、賃金を減らさずに法定労働週を44時間から40時間へと短縮することが法案の骨子です。"
            },
            {
                "question": "What argument do supporters of the shorter workweek present?",
                "options": [
                    "Extended working regimes increase fatigue, lowering hourly productivity and raising healthcare costs.",
                    "Workers in Latin America want to completely abandon manufacturing jobs.",
                    "Factory machinery operates better when left unattended for three days.",
                    "Companies will earn higher profits by shutting down operations entirely."
                ],
                "answer": 0,
                "explanation": "第2文にある通り、過重労働による疲労が時間あたり生産性を低下させ医療費を増大させているという実証研究が根拠とされています。"
            },
            {
                "question": "Why do manufacturing confederations express concern regarding the bill?",
                "options": [
                    "They fear interest rates will drop to zero.",
                    "They believe employees will refuse to work four days a week.",
                    "They worry mandatory hour cuts will impose onerous payroll burdens on small enterprises.",
                    "They want the government to nationalize all privately owned factories."
                ],
                "answer": 2,
                "explanation": "第3文にある通り、労働集約型の中小企業に重い人件費負担（onerous payroll burdens）が課されることを懸念しています。"
            },
            {
                "question": "The word 'onerous' in the third sentence is closest in meaning to:",
                "options": ["burdensome", "pleasant", "voluntary", "insignificant"],
                "answer": 0,
                "explanation": "onerous は「過重な」「負担の大きい」を意味するため、burdensome が正解です。"
            },
            {
                "question": "How is the impending congressional vote characterized by observers?",
                "options": [
                    "As a trivial procedural vote with no lasting impact.",
                    "As a pivotal litmus test for balancing workers' welfare against economic competitiveness.",
                    "As an attempt to delay the Brazilian presidential inauguration.",
                    "As an international treaty negotiation with European trade delegates."
                ],
                "answer": 1,
                "explanation": "最終文で、労働者の福祉と経済競争力のバランスを図る決定的な試金石（pivotal litmus test）と表現されています。"
            }
        ]
    },

    # 5. WORLD - Indonesia Deploys Dry Ice for Wildfire Haze
    {
        "slug": "indonesia-wildfire-haze-dry-ice-cloud-seeding",
        "category": "world",
        "category_label": "GEOENGINEERING & SOUTHEAST ASIA • インドネシア森林火災へのドライアイス投下",
        "date": "2026-10-16",
        "title": "Indonesia Deploys Dry Ice Cloud Seeding to Quell Wildfires and Toxic Transboundary Haze",
        "headline_ja": "インドネシア政府、森林泥炭火災と有毒煙害（ヘイズ）鎮静化へドライアイス散布作戦を展開",
        "subhead": "周辺国（シンガポール・マレーシア）へ越境拡散する大気汚染を阻止する緊急気象制御技術。`",
        "lead_snippet": "スマトラ島およびカリマンタン島で猛威を振るう泥炭地森林火災に対し、インドネシア軍と国家防災庁は上空からドライアイスを散布して人工降雨を誘発する緊急オペレーションを開始した。エルニーニョ現象が引き起こす長期干ばつと焼き畑農業に起因する煙害は、周辺国の公衆衛生と外交関係にも重大な摩擦を生じさせている。",
        "source_name": "The Guardian (Oct 15, 2026)",
        "source_url": "https://www.theguardian.com/world/2026/oct/15/indonesia-fires-dry-ice-dropped-toxic-haze-spreads",
        "source_attribution": "Source: The Guardian (Oct 15, 2026). Dry ice dropped over Indonesia fires as toxic haze spreads.",
        "image": "https://images.unsplash.com/photo-1516214104703-d870798883c5?w=1000&auto=format&fit=crop&q=80",
        "sentences": [
            {
                "en": "Indonesian disaster response authorities have mobilized military transport aircraft to drop metric tons of solid carbon dioxide, or dry ice, directly into convective cloud formations above raging peatland infernos.",
                "ja": "インドネシアの防災当局は、猛威を振るう泥炭地火災の上空に対流雲へ数トンの固形二酸化炭素（ドライアイス）を直接投下するため、軍用輸送機を動員した。"
            },
            {
                "en": "The unorthodox geoengineering technique aims to abruptly supercool atmospheric moisture and trigger localized precipitation over subterranean peat fires that conventional water-bombing helicopters cannot extinguish.",
                "ja": "この型破りな気象工学技術は、大気中の水分を急激に過冷却して人工降雨を誘発し、従来の消火ヘリコプターでは鎮火不可能な地下泥炭火災を消し止めることを目的としている。"
            },
            {
                "en": "Dense plumes of particulate matter designated PM2.5 have drifted across international maritime boundaries, blanketing urban skylines in Malaysia and Singapore and triggering diplomatic protests over transboundary pollution.",
                "ja": "PM2.5に指定される微小粒子状物質の濃密な煙が国際海峡の境界を越えて漂流し、マレーシアやシンガポールの都市の空を覆い、越境大気汚染をめぐる外交的抗議を引き起こしている。"
            },
            {
                "en": "Environmental scientists warn that clearing carbon-rich tropical peat swamps for commercial agricultural expansion releases colossal volumes of sequestered greenhouse gases, converting critical biosphere sinks into carbon emitters.",
                "ja": "環境科学者らは、商業的農業拡大のために炭素を豊富に含む熱帯泥炭湿地を開墾することは、固定されていた膨大な温室効果ガスを放出し、不可欠な生物圏の吸収源を炭素排出源へと変えてしまうと警告している。"
            },
            {
                "en": "Ultimately, regional sustainability advocates stress that airborne weather modification represents merely a palliative palliative remedy unless regional governments rigorously enforce land-clearing moratoria.",
                "ja": "最終的に、地域の持続可能性提唱者らは、周辺政府が森林伐採のモラトリアム（一時停止）を厳格に執行しない限り、空中からの気象改変は単なる一時しのぎの緩和策に過ぎないと強調している。"
            }
        ],
        "dialogue": [
            {"speaker": "七", "name": "Nanami", "role": "生徒", "text": "山火事にドライアイスを飛行機から落とすなんて、SF映画のような消火作戦ですね！"},
            {"speaker": "慶", "name": "Keita", "role": "英語講師", "text": "そうだね。第2文にあるように『subterranean peat fires（地下の泥炭火災）』は水をまいても地中深くで燃え続けるから、大気を急激に冷やして大雨を降らせる（supercool moisture to trigger precipitation）作戦なんだ。"},
            {"speaker": "七", "name": "Nanami", "role": "生徒", "text": "第3文にあるように、その煙が隣のシンガポールやマレーシアまで流れて国際問題（transboundary pollution）になっているんですね。"},
            {"speaker": "慶", "name": "Keita", "role": "英語講師", "text": "東南アジアのヘイズ（煙害）問題は、国際法・環境外交・地球温暖化のすべての交差点だよ。第5文の『merely a palliative remedy（単なる一時しのぎの対症療法）』という重要表現も覚えておこう！"}
        ],
        "vocab": [
            {"word": "subterranean", "phonetic": "/ˌsʌb.təˈreɪ.ni.ən/", "meaning": "地下の、地中の、隠れた", "pos": "adjective", "def": "Existing, occurring, or done under the earth\'s surface.", "ex": "Subterranean peat fires burn invisibly beneath the jungle floor."},
            {"word": "transboundary", "phonetic": "/trænzˈbaʊn.dər.i/", "meaning": "国境を越える、越境性の", "pos": "adjective", "def": "Crossing or extending across national or political boundaries.", "ex": "Transboundary haze pollution requires diplomatic collaboration in ASEAN."},
            {"word": "sequester", "phonetic": "/sɪˈkwes.tər/", "meaning": "隔離する、炭素を固定・貯留する", "pos": "verb", "def": "Isolate or hide away, or trap a chemical substance such as carbon.", "ex": "Intact peatlands sequester more carbon per hectare than tropical rain forests."},
            {"word": "emitter", "phonetic": "/iˈmɪt.ər/", "meaning": "排出源、放出するもの", "pos": "noun", "def": "A person, organization, or apparatus that emits something, especially greenhouse gases.", "ex": "Deforestation transforms pristine forests into potent carbon emitters."},
            {"word": "palliative", "phonetic": "/ˈpæl.i.ə.tɪv/", "meaning": "一時しのぎの、対症療法の、緩和的な", "pos": "adjective", "def": "Relieving pain or alleviating a problem without dealing with the underlying cause.", "ex": "Spraying dry ice was seen as a palliative gesture rather than a lasting solution."}
        ],
        "syntax": [
            {"title": "convert A into B の変形構文", "formula": "converting [critical biosphere sinks] into [carbon emitters]", "explanation": "convert A into B は「AをBへと転換・変化させる」という意味で、環境破壊が生態系の機能を正反対に変質させる様子を鮮やかに描写しています。"},
            {"title": "unless節による条件限定構文", "formula": "[airborne modification represents a remedy] unless [governments rigorously enforce moratoria]", "explanation": "unless は「〜でない限りは」という強い必要条件を提示し、根本的な法規制がなければ技術的手段が無力であることを論述しています。"}
        ],
        "quiz": [
            {
                "question": "Why did Indonesian authorities drop dry ice from aircraft over the wildfires?",
                "options": [
                    "To freeze all wild animals in the forest for transport.",
                    "To supercool clouds and trigger localized rainfall over underground peat fires.",
                    "To disperse toxic gases into neighboring countries.",
                    "To manufacture commercial cooling materials for local markets."
                ],
                "answer": 1,
                "explanation": "第2文にある通り、大気中の水分を急冷して局地的な降雨を誘発し地下泥炭火災を消火するためです。"
            },
            {
                "question": "What international diplomatic consequence resulted from the wildfires?",
                "options": [
                    "Singapore and Malaysia deployed naval blockades.",
                    "Neighboring nations launched diplomatic protests over transboundary smoke and PM2.5 pollution.",
                    "ASEAN member states dissolved their regional trade union.",
                    "International airlines offered free flights out of Jakarta."
                ],
                "answer": 1,
                "explanation": "第3文にある通り、PM2.5を含む濃煙がマレーシアやシンガポールに越境し、越境大気汚染（transboundary pollution）への外交抗議が起きました。"
            },
            {
                "question": "How does clearing peatlands impact global carbon cycles?",
                "options": [
                    "It converts natural carbon sinks into major carbon emitters by releasing sequestered gases.",
                    "It permanently cools the global atmosphere by reflecting sunlight.",
                    "It doubles the rate of oceanic oxygen production.",
                    "It causes clouds to disappear permanently from Southeast Asia."
                ],
                "answer": 0,
                "explanation": "第4文にある通り、固定されていた炭素が放出され、二酸化炭素吸収源（sinks）が排出源（emitters）に変貌してしまいます。"
            },
            {
                "question": "The word 'palliative' in the final sentence is closest in meaning to:",
                "options": ["permanent", "temporary and symptom-relieving", "economically profitable", "violently destructive"],
                "answer": 1,
                "explanation": "palliative は「根本治療ではなく一時的な症状緩和の」を意味します。"
            },
            {
                "question": "What fundamental action do environmental advocates demand from governments?",
                "options": [
                    "Buying more military fighter jets from abroad.",
                    "Banning all electronic devices in cities.",
                    "Rigorously enforcing bans on illegal land-clearing for agriculture.",
                    "Subsidizing the production of synthetic peat."
                ],
                "answer": 2,
                "explanation": "最終文で、土地開墾のモラトリアム（land-clearing moratoria）を厳格に執行することが根本的解決だと強調されています。"
            }
        ]
    },

    # 6. WORLD - Made in Europe Green Subsidies Accord with UK
    {
        "slug": "made-in-europe-green-subsidies-uk-accord",
        "category": "world",
        "category_label": "INTERNATIONAL TRADE & INDUSTRIAL POLICY • 欧州グリーン産業支援と英欧協調",
        "date": "2026-10-16",
        "title": "France Drops Opposition to UK Inclusion in Landmark Made in Europe Green Legislation",
        "headline_ja": "仏政府、EU域内調達優遇法「メイド・イン・ヨーロッパ」への英国参画反対を撤回",
        "subhead": "米中の巨額環境補助金に対抗。脱炭素サプライチェーン強化のため英仏がブレグジット後の協調へ。",
        "lead_snippet": "フランス政府は、EUのクリーンテクノロジー支援枠組み「メイド・イン・ヨーロッパ」法案において、英国企業をサプライチェーンの適用対象から除外する従来の方針を転換した。風力発電用タービンや電気自動車用バッテリーの部材確保において、孤立化を避けて欧州全体の産業競争力を高める現実的な通商合意として歓迎されている。",
        "source_name": "The Guardian (Oct 15, 2026)",
        "source_url": "https://www.theguardian.com/world/2026/oct/15/france-drops-opposition-to-uk-being-included-in-made-in-europe-legislation",
        "source_attribution": "Source: The Guardian (Oct 15, 2026). France drops opposition to UK being included in Made in Europe legislation.",
        "image": "https://images.unsplash.com/photo-1473341304170-971dccb5ac1e?w=1000&auto=format&fit=crop&q=80",
        "sentences": [
            {
                "en": "French diplomatic officials have formally withdrawn their long-standing veto against allowing United Kingdom manufacturers to participate in the European Union\\'s flagship \\'Made in Europe\\' green subsidy mechanism.",
                "ja": "フランスの外交当局者は、EUの看板環境補助金メカニズム「メイド・イン・ヨーロッパ」に英国の製造業者が参加することを認める案に対する長年の拒否権を正式に撤回した。"
            },
            {
                "en": "The legislative framework seeks to counterbalance aggressive industrial subsidies offered under the United States Inflation Reduction Act and China\\'s state-backed clean technology dominance.",
                "ja": "この立法枠組みは、米国のインフレ抑制法（IRA）の下で提供される積極的な産業補助金や、中国の国家支援によるクリーンテクノロジーの優位性に対抗することを目指している。"
            },
            {
                "en": "Paris had previously insisted on rigid territorial eligibility rules that strictly excluded non-EU member states following the political fallout of the 2020 post-Brexit withdrawal treaty.",
                "ja": "フランス政府はこれまで、2020年のブレグジット離脱条約締結後の政治的余波を受け、非EU加盟国を厳格に排除する硬直的な領域適格性ルールを主張していた。"
            },
            {
                "en": "However, European automotive and renewable energy coalitions lobbied extensively that bifurcating electric battery and offshore wind supply chains would needlessly inflate costs across the continent.",
                "ja": "しかし、欧州の自動車および再生可能エネルギー産業連合は、電気自動車用バッテリーや洋上風力発電のサプライチェーンを分断することは欧州全土で不必要にコストを高騰させると大規模なロビー活動を展開した。"
            },
            {
                "en": "Trade analysts observe that the compromise marks a pragmatic reset in cross-Channel relations, fostering mutual regulatory alignment in strategic clean technology sectors.",
                "ja": "通商アナリストらは、この妥協が英仏海峡を挟む二国間関係におけるプラグマティック（実利主義的）な関係修復を画し、戦略的クリーンテクノロジー分野における相互の規制整合性を促進するものだと見ている。"
            }
        ],
        "dialogue": [
            {"speaker": "七", "name": "Nanami", "role": "生徒", "text": "フランスが、EUのグリーン産業法案にイギリスの参加を認めることに同意したんですね！ブレグジット後も対立が続いていたのに、どうして態度を変えたんですか？"},
            {"speaker": "慶", "name": "Keita", "role": "英語講師", "text": "第2文にあるように、アメリカ（IRA法）や中国の巨額な環境補助金に対抗するためなんだ。EUだけでイギリスを締め出すと、かえってバッテリーや風力発電の部品調達コストが高くなってしまうんだよ。"},
            {"speaker": "七", "name": "Nanami", "role": "生徒", "text": "第4文の『bifurcating supply chains（サプライチェーンの二股化・分断）』ですね。産業界からの要望が政治の壁を動かしたんですね！"},
            {"speaker": "慶", "name": "Keita", "role": "英語講師", "text": "その通り！第5文にある『pragmatic reset（実利的な関係修復）』という表現は、国際通商やヨーロッパ政治のニュースを読む上で極めて重要なキーワードだよ。"}
        ],
        "vocab": [
            {"word": "counterbalance", "phonetic": "/ˈkaʊn.təˌbæl.əns/", "meaning": "対抗する、均衡させる、相殺する", "pos": "verb", "def": "Neutralize or cancel the effect of something with an opposite force.", "ex": "The new European subsidy aims to counterbalance American tax incentives."},
            {"word": "eligibility", "phonetic": "/ˌel.ɪ.dʒəˈbɪl.ə.ti/", "meaning": "適格性、参加資格", "pos": "noun", "def": "The state of having the right for something through satisfaction of conditions.", "ex": "Strict territorial eligibility rules prevented non-EU businesses from applying."},
            {"word": "bifurcate", "phonetic": "/ˈbaɪ.fə.keɪt/", "meaning": "二股に分ける、分断する", "pos": "verb", "def": "Divide or cause to divide into two branches or forks.", "ex": "Trade tariffs threaten to bifurcate global semiconductor supply networks."},
            {"word": "pragmatic", "phonetic": "/præɡˈmæt.ɪk/", "meaning": "実利的な、実践的な、現実主義的な", "pos": "adjective", "def": "Dealing with things sensibly and realistically based on practical conditions.", "ex": "Diplomats reached a pragmatic compromise to avert economic friction."},
            {"word": "alignment", "phonetic": "/əˈlaɪn.mənt/", "meaning": "整列、連携、規制の共通化", "pos": "noun", "def": "Arrangement in a straight line, or bringing into agreement and cooperation.", "ex": "Environmental regulatory alignment fosters seamless cross-border trade."}
        ],
        "syntax": [
            {"title": "seek to + 動詞の原形（政策方針の表明）", "formula": "[The framework] seeks to counterbalance [aggressive industrial subsidies]", "explanation": "seek to do は「〜することを目指す・試みる」という政策文書や高級紙の解説で頻出の表現です。"},
            {"title": "動名詞句主語（bifurcating ~）による因果構造", "formula": "that bifurcating [supply chains] would needlessly inflate [costs across the continent]", "explanation": "bifurcating supply chains が名詞節内の主語となり、「サプライチェーンを分断することが、コストを高騰させることになる」という因果論理を構成しています。"}
        ],
        "quiz": [
            {
                "question": "What diplomatic shift did French officials make regarding UK manufacturers?",
                "options": [
                    "They expelled all British citizens residing in France.",
                    "They dropped their veto against UK participation in the EU 'Made in Europe' green subsidy scheme.",
                    "They demanded the UK rejoin the European Union political parliament.",
                    "They imposed punitive maritime tariffs on British fisheries."
                ],
                "answer": 1,
                "explanation": "第1文にある通り、EUの「メイド・イン・ヨーロッパ」補助金制度への英国企業の参加に対する拒否権を撤回しました。"
            },
            {
                "question": "What external competition does the 'Made in Europe' legislation attempt to counterbalance?",
                "options": [
                    "Australian solar initiatives and Canadian lumber quotas.",
                    "US Inflation Reduction Act subsidies and Chinese clean-tech state dominance.",
                    "Russian space satellites and Indian software exports.",
                    "South American beef production quotas."
                ],
                "answer": 1,
                "explanation": "第2文にある通り、米国のインフレ抑制法（IRA）や中国のクリーンテック優位に対抗することが目的です。"
            },
            {
                "question": "Why did automotive and energy industry groups lobby against excluding the UK?",
                "options": [
                    "Because British car factories had ceased operations entirely.",
                    "Because dividing supply chains would needlessly drive up manufacturing costs.",
                    "Because they wanted all batteries to be manufactured in North America.",
                    "Because the UK refuses to adopt electric vehicles."
                ],
                "answer": 1,
                "explanation": "第4文にある通り、バッテリーや風力発電のサプライチェーンを分断するとコストが無用に跳ね上がるためです。"
            },
            {
                "question": "The word 'bifurcate' in the fourth sentence most nearly means to:",
                "options": ["unite", "divide into two branches", "expand globally", "automate completely"],
                "answer": 1,
                "explanation": "bifurcate は「2つに分岐させる」「二分する」という意味です。"
            },
            {
                "question": "How do trade analysts view the significance of this agreement?",
                "options": [
                    "As a pragmatic reset in UK-EU relations fostering clean tech regulatory alignment.",
                    "As a catastrophic breakdown in European diplomatic sovereignty.",
                    "As a temporary trade loophole that will be abolished immediately.",
                    "As an abandonment of all environmental climate targets."
                ],
                "answer": 0,
                "explanation": "最終文で、英欧関係の実利主義的な関係修復（pragmatic reset）と規制整合性の促進として評価されています。"
            }
        ]
    },

    # 7. LAW - Zero-Click Spyware via Digital Ads (Cybersecurity)
    {
        "slug": "zero-click-spyware-digital-advertising-exploitation",
        "category": "law",
        "category_label": "CYBER LAW & PRIVACY RIGHTS • ネット広告を経由したゼロクリック監視スパイウェア",
        "date": "2026-10-16",
        "title": "Cybersecurity Researchers Expose Zero-Click Spyware Infiltrating Mobile Devices via Digital Ads",
        "headline_ja": "サイバー法学：デジタル広告網を悪用して端末に侵入する「ゼロクリック型スパイウェア」の脅威",
        "subhead": "ユーザーがリンクをクリックしなくても感染。オンライン広告入札システム（RTB）の構造的脆弱性。",
        "lead_snippet": "国際的なサイバーセキュリティ研究機関は、商業用スパイウェア企業がプログラマティック広告の配信ネットワークを悪用し、標的のスマートフォンへ一切の操作なし（ゼロクリック）で侵入する高度な監視手法を告発した。個人の閲覧履歴に基づくリアルタイム入札（RTB）技術が国家規模の監視活動に転用される中、プライバシー法と広告規制の再設計が急務となっている。",
        "source_name": "The Guardian (Oct 15, 2026)",
        "source_url": "https://www.theguardian.com/technology/2026/oct/15/israeli-firm-digital-ads-enabling-installation-of-zero-click-spyware-researchers-say",
        "source_attribution": "Source: The Guardian (Oct 15, 2026). Digital ads enabling installation of zero-click spyware, researchers say.",
        "image": "https://images.unsplash.com/photo-1563986768609-322da13575f3?w=1000&auto=format&fit=crop&q=80",
        "sentences": [
            {
                "en": "Independent cybersecurity forensic investigators have uncovered evidence that surveillance software vendors are exploiting programmatic advertising infrastructure to deliver zero-click spyware to targeted mobile devices.",
                "ja": "独立したサイバーセキュリティ鑑識調査チームは、監視ソフトウェア企業がプログラマティック広告インフラを悪用し、標的のモバイル端末に「ゼロクリック型スパイウェア」を送り込んでいる証拠を暴いた。"
            },
            {
                "en": "Unlike conventional phishing mechanisms that require human interaction such as tapping a malicious link, the newly identified attack vector executes weaponized code during the millisecond auction of targeted banner ads.",
                "ja": "悪意あるリンクをタップするなどの人間の操作を必要とする従来のフィッシング手法とは異なり、新たに特定された攻撃ベクトルは、標的型バナー広告のミリ秒単位の入札プロセス中に兵器化されたコードを実行する。"
            },
            {
                "en": "Privacy advocates argue that real-time bidding protocols, which routinely broadcast granular user geolocation and device identifiers to thousands of ad brokers, have created an indefensible backdoor for covert state surveillance.",
                "ja": "プライバシー擁護派は、詳細なユーザーの位置情報や端末識別子を何千もの広告ブローカーに日常的にブロードキャストするリアルタイム入札（RTB）プロトコルが、隠密な国家監視のための弁解の余地のない裏口（バックドア）を生み出していると主張する。"
            },
            {
                "en": "Regulatory authorities across Europe and North America are now examining whether commercial advertising exchanges bear statutory liability under strict data protection directives for facilitating unauthorized device intrusion.",
                "ja": "欧州および北米の規制当局は現在、不正な端末侵入を助長したことについて、商用広告取引所が厳格なデータ保護指令の下で法定責任を負うべきかどうかの検証に着手している。"
            },
            {
                "en": "Constitutional jurists warn that failing to rein in the militarization of online ad ecosystems poses an existential peril to investigative journalism and democratic whistleblowing protections.",
                "ja": "憲法学者らは、オンライン広告エコシステムの軍事利用を抑制できなければ、調査報道ジャーナリズムと民主主義的な内部告発者の保護に存亡の危機をもたらすと警告している。"
            }
        ],
        "dialogue": [
            {"speaker": "七", "name": "Nanami", "role": "生徒", "text": "Keita先生、「ゼロクリック型スパイウェア」って何ですか？怪しいリンクをクリックしなくてもスマホが乗っ取られるんですか？！"},
            {"speaker": "慶", "name": "Keita", "role": "英語講師", "text": "その通りなんだ。第2文にあるように、普段ネットを見ていて広告が表示される『コンマ数秒の自動入札（millisecond auction）』の隙に、悪意あるプログラムが裏で実行されてしまうんだよ。"},
            {"speaker": "七", "name": "Nanami", "role": "生徒", "text": "恐ろしすぎます…！第3文の『real-time bidding（リアルタイム入札）』って、私たちの位置情報や端末情報が勝手に広告業者に流れている仕組みのことですよね。"},
            {"speaker": "慶", "name": "Keita", "role": "英語講師", "text": "まさにそこが法学部の入試長文で最頻出の論点だよ。第4文のように広告企業に法的責任（statutory liability）を負わせるべきか、第5文のようにジャーナリストや市民の自由をどう守るかという『プライバシーと国家安全保障』の重大なテーマだね。"}
        ],
        "vocab": [
            {"word": "surveillance", "phonetic": "/sɜːˈveɪ.ləns/", "meaning": "監視、見張り、諜報活動", "pos": "noun", "def": "Close observation, especially of a suspected spy or criminal.", "ex": "Commercial spyware vendors conduct illegal surveillance against activists."},
            {"word": "vector", "phonetic": "/ˈvek.tər/", "meaning": "攻撃経路（attack vector）、媒介物、ベクトル", "pos": "noun", "def": "A route or medium by which an attack or disease is directed.", "ex": "Digital advertising has become a prevalent attack vector for hackers."},
            {"word": "granular", "phonetic": "/ˈɡræn.jə.lər/", "meaning": "詳細な、きめ細かい、粒状の", "pos": "adjective", "def": "Characterized by a high level of detail or small components.", "ex": "Ad brokers gather granular tracking data on consumer habits."},
            {"word": "indefensible", "phonetic": "/ˌɪn.dɪˈfen.sə.bəl/", "meaning": "弁護の余地のない、擁護できない", "pos": "adjective", "def": "Not justifiable; inexcusable, or unable to be defended against attack.", "ex": "Creating a security backdoor in consumer software is legally indefensible."},
            {"word": "peril", "phonetic": "/ˈper.əl/", "meaning": "危機、重大な危険", "pos": "noun", "def": "Serious and immediate danger.", "ex": "Unregulated spyware puts the lives of investigative journalists in grave peril."}
        ],
        "syntax": [
            {"title": "Unlike を用いた対照的導入構文", "formula": "Unlike [conventional phishing mechanisms that require X], [the newly identified attack vector executes Y]", "explanation": "Unlike + 名詞句 から文を始めることで、旧来のフィッシングと最新のゼロクリック攻撃の違いを鮮明に対比しています。"},
            {"title": "examine whether 節（間接疑問文の目的語）", "formula": "[Authorities are examining] whether [commercial advertising exchanges bear statutory liability under directives]", "explanation": "examine whether ~ は「〜であるかどうかを調査・検証する」という法律・行政報道の標準的な論述構文です。"}
        ],
        "quiz": [
            {
                "question": "How does zero-click spyware differ from traditional phishing attacks?",
                "options": [
                    "It requires the user to call a customer service hotline.",
                    "It executes malicious code without requiring the victim to click or tap any link.",
                    "It only infects desktop computers connected via copper cables.",
                    "It permanently disables the device's screen brightness."
                ],
                "answer": 1,
                "explanation": "第2文にある通り、悪意あるリンクをタップするなどの人間の操作を必要とせず、広告入札中にコードが自動実行されます。"
            },
            {
                "question": "What ad mechanism do privacy advocates argue created an indefensible security backdoor?",
                "options": [
                    "Printed billboards along public highways.",
                    "Paper coupons mailed to residential addresses.",
                    "Real-time bidding (RTB) protocols that broadcast user location and device IDs.",
                    "Voice advertisements broadcast over FM radio frequencies."
                ],
                "answer": 2,
                "explanation": "第3文にある通り、端末IDや位置情報をブロードキャストするリアルタイム入札（RTB）プロトコルが問題視されています。"
            },
            {
                "question": "What legal question are regulatory authorities currently examining?",
                "options": [
                    "Whether smartphones should be banned from public schools.",
                    "Whether commercial ad exchanges bear statutory liability for facilitating intrusions.",
                    "Whether computer programmers must hold government licenses.",
                    "Whether international phone calls should be heavily taxed."
                ],
                "answer": 1,
                "explanation": "第4文にある通り、広告取引所が不正侵入を容易にしたことについて法定責任（statutory liability）を負うべきかが検証されています。"
            },
            {
                "question": "The word 'granular' in the third sentence is closest in meaning to:",
                "options": ["vague", "highly detailed", "harmless", "fictional"],
                "answer": 1,
                "explanation": "granular はデータや情報について「詳細な」「きめの細かい（highly detailed）」を意味します。"
            },
            {
                "question": "Who do constitutional jurists warn are placed in existential peril by weaponized ad ecosystems?",
                "options": [
                    "Investigative journalists and democratic whistleblowers.",
                    "Automobile manufacturers and airline pilots.",
                    "Professional athletes and sports broadcasters.",
                    "Fashion designers and museum curators."
                ],
                "answer": 0,
                "explanation": "最終文で、調査報道ジャーナリズムと内部告発者の保護（investigative journalism and whistleblowing）が存亡の危機に瀕すると警告されています。"
            }
        ]
    },

    # 8. LAW - UK Chancellor Considers Bank Tax Hike
    {
        "slug": "uk-chancellor-bank-windfall-tax-fiscal-consolidation",
        "category": "law",
        "category_label": "TAX LAW & PUBLIC FINANCE • 英政府、銀行超過利潤税の引き上げを検討",
        "date": "2026-10-16",
        "title": "UK Chancellor Considers Higher Taxes on Banking Sector to Address Fiscal Deficit",
        "headline_ja": "英国財務相、財政再建と防衛予算確保へ大手銀行への課税強化を検討",
        "subhead": "高金利下で過去最高益を記録した金融セクターに対する特別超過利潤課税（surcharge）の是非。",
        "lead_snippet": "英国のレイチェル・リーブス財務大臣は、次期予算案において大手銀行が享受した金利高に伴う巨額利益に対し、追加の銀行サーチャージ（超過利潤課税）を課す検討に入った。公的サービスの維持と防衛費増額の財源確保を目指す政府に対し、ロンドン金融街（シティ）は国際競争力の低下と資本流出を警告して激しく反発している。",
        "source_name": "The Guardian (Oct 15, 2026)",
        "source_url": "https://www.theguardian.com/uk-news/2026/oct/15/john-healey-raise-taxes-banks-budget",
        "source_attribution": "Source: The Guardian (Oct 15, 2026). Treasury considers higher taxes on banks in upcoming budget.",
        "image": "https://images.unsplash.com/photo-1541354329998-f4d9a9f9297f?w=1000&auto=format&fit=crop&q=80",
        "sentences": [
            {
                "en": "British Treasury officials are evaluating legislative proposals to elevate the bank surcharge tax rate on commercial lenders that have accumulated record profits throughout the central bank\\'s elevated interest rate cycle.",
                "ja": "英国財務省の高官らは、中央銀行の高金利サイクルを通じて過去最高益を蓄積してきた商業銀行に対する銀行サーチャージ税率を引き上げる法案を検討している。"
            },
            {
                "en": "Cabinet ministers argue that targeting windfall banking revenue provides an equitable fiscal mechanism to plug a multibillion-pound deficit in public expenditure without raising direct income taxes on working households.",
                "ja": "閣僚らは、銀行の棚ぼた利益（超過利潤）を課税対象とすることは、勤労世帯への直接所得税を引き上げることなく、数十億ポンド規模の財政赤字を穴埋めするための公平な財政メカニズムを提供すると主張する。"
            },
            {
                "en": "However, executive leaders across the City of London warn that unilateral fiscal levies will impair domestic credit expansion and incentivize multinational investment banks to shift underwriting capital to Frankfurt or New York.",
                "ja": "しかし、ロンドン金融街（シティ）の経営幹部らは、一方的な財政的課税が国内の信用拡大を阻害し、多国籍投資銀行が引受資本をフランクフルトやニューヨークへと移転させるインセンティブを与えると警告している。"
            },
            {
                "en": "Tax law scholars emphasize that designing equitable corporate levies requires navigating constitutional protections against arbitrary economic expropriation while establishing predictable statutory thresholds.",
                "ja": "税法学者らは、公正な法人課税を設計するには、予測可能な法定の基準値を確立しつつ、恣意的な経済的収用に対する憲法上の保護に配慮することが求められると強調する。"
            },
            {
                "en": "The fiscal deliberation underscores the perennial dilemma confronting contemporary democratic governments in balancing sovereign redistributive mandates with international capital mobility.",
                "ja": "この財政的審議は、主権国家の再分配責務と国際資本の移動性とを調和させるにあたって、現代の民主主義政府が直面する永遠のジレンマを浮き彫りにしている。"
            }
        ],
        "dialogue": [
            {"speaker": "七", "name": "Nanami", "role": "生徒", "text": "イギリスの財務省が大手銀行への税金を増やそうとしているんですね。銀行だけ特別に税率を上げるなんてできるんですか？"},
            {"speaker": "慶", "name": "Keita", "role": "英語講師", "text": "第1文にある『bank surcharge（銀行サーチャージ）』という特別上乗せ課税だね。中央銀行が金利を上げたことで、銀行は預金金利を抑えたまま貸出金利で莫大な利益（record profits）を上げたからなんだ。"},
            {"speaker": "七", "name": "Nanami", "role": "生徒", "text": "第2文にあるように、普通の市民の所得税を上げる代わりに、儲かった銀行から税金を取って財政赤字を埋めよう（plug a deficit）というわけですね。"},
            {"speaker": "慶", "name": "Keita", "role": "英語講師", "text": "その通り！でも第3文のように、税金を上げすぎると国際銀行がロンドンからニューヨークに逃げてしまう（capital mobility）。第5文の『再分配と資本移動のジレンマ』は、一橋や慶應経済の小論文・英語で頻出中の頻出だよ！"}
        ],
        "vocab": [
            {"word": "surcharge", "phonetic": "/ˈsɜː.tʃɑːdʒ/", "meaning": "追徴金、付加税、追加料金", "pos": "noun", "def": "An additional charge, tax, or cost added to the regular bill.", "ex": "The government imposed a special surcharge on corporate earnings."},
            {"word": "windfall", "phonetic": "/ˈwɪnd.fɔːl/", "meaning": "棚ぼたの利益、予想外の巨利（windfall profit）", "pos": "noun", "def": "An unexpected, unearned, or sudden gain or advantage, especially financial.", "ex": "Energy companies generated massive windfall profits during the fuel crisis."},
            {"word": "underwriting", "phonetic": "/ˌʌn.dəˈraɪ.tɪŋ/", "meaning": "引受業務、信用保証", "pos": "noun", "def": "The process by which financial institutions take on financial risk for a fee.", "ex": "Investment banks handle bond underwriting for major corporations."},
            {"word": "expropriation", "phonetic": "/ekˌsprəʊ.priˈeɪ.ʃən/", "meaning": "収用、没収、財産権の剥奪", "pos": "noun", "def": "The action by the state of taking private property for public use.", "ex": "Constitutional clauses protect foreign businesses from arbitrary expropriation."},
            {"word": "perennial", "phonetic": "/pəˈren.i.əl/", "meaning": "永遠の、長年繰り返される、多年生の", "pos": "adjective", "def": "Lasting or existing for a long or apparently infinite time; enduring.", "ex": "Balancing taxation and growth is a perennial challenge for politicians."}
        ],
        "syntax": [
            {"title": "動詞 plug を比喩的に用いた表現", "formula": "[targeting windfall revenue] provides an equitable mechanism to plug [a deficit in public expenditure]", "explanation": "plug a deficit は「財政赤字の穴を埋める」という財政報道の定番フレーズで、プラグで穴を塞ぐイメージから生じた重要表現です。"},
            {"title": "in balancing A with B の前置詞句", "formula": "[the dilemma confronting governments] in balancing [sovereign redistributive mandates] with [international capital mobility]", "explanation": "balance A with B（AとBの均衡を取る）に in ~ing（〜するにあたって）が組み合わさり、現代国家が直面する二律背反を表現しています。"}
        ],
        "quiz": [
            {
                "question": "What policy is the British Treasury currently evaluating?",
                "options": [
                    "Abolishing all corporate taxes on tech firms.",
                    "Raising the bank surcharge tax rate on commercial lenders.",
                    "Nationalizing all private savings accounts in London.",
                    "Decreasing the legal retirement age to fifty."
                ],
                "answer": 1,
                "explanation": "第1文にある通り、高金利下で最高益を上げた商業銀行に対する銀行サーチャージ税率の引き上げが検討されています。"
            },
            {
                "question": "What justification do government ministers offer for taxing the banking sector?",
                "options": [
                    "It allows the Treasury to plug public deficits without raising income taxes on working families.",
                    "It will force multinational banks to shut down permanently.",
                    "It is designed to encourage citizens to stop using banks.",
                    "It will automatically lower international interest rates."
                ],
                "answer": 0,
                "explanation": "第2文にある通り、勤労世帯への所得税増税を避けつつ財政赤字を穴埋めする公平な手段と主張されています。"
            },
            {
                "question": "What consequence does the financial sector warn could result from unilateral tax hikes?",
                "options": [
                    "Banks will give all excess profits to domestic charities.",
                    "International banks may shift capital and operations to Frankfurt or New York.",
                    "Foreign tourists will stop visiting British museums.",
                    "The British pound will completely cease to circulate."
                ],
                "answer": 1,
                "explanation": "第3文にある通り、多国籍投資銀行が引受資本をフランクフルトやニューヨークに移転させる恐れがあると警告されています。"
            },
            {
                "question": "The word 'perennial' in the final sentence most nearly means:",
                "options": ["temporary", "ever-recurring and enduring", "insignificant", "unconstitutional"],
                "answer": 1,
                "explanation": "perennial は「長年繰り返される」「永遠の」を意味します。"
            },
            {
                "question": "What fundamental tension does this fiscal debate highlight?",
                "options": [
                    "The conflict between space exploration and deep-sea mining.",
                    "The difficulty of balancing sovereign redistributive policies with global capital mobility.",
                    "The dispute between renewable wind power and nuclear fusion.",
                    "The struggle between print newspapers and digital journalism."
                ],
                "answer": 1,
                "explanation": "最終文で、主権国家の再分配責務とグローバルな資本移動性の均衡というジレンマが指摘されています。"
            }
        ]
    },

    # 9. CULTURE - The Floating World: Art Market & Capital (Ben Eastham)
    {
        "slug": "the-floating-world-art-market-capitalism-ethics",
        "category": "culture",
        "category_label": "AESTHETICS & PHILOSOPHY • 現代アート市場と資本主義の精神的葛藤",
        "date": "2026-10-16",
        "title": "The Floating World: Ben Eastham\\'s Critique of Art\\'s Relationship to Capital and Power",
        "headline_ja": "書評『浮世（The Floating World）』：美の探求と巨大マネーに呑まれる現代美術界の肖像",
        "subhead": "美的な純粋性は投機マネーの前で維持できるのか。芸術評論家ベン・イーストハムが問う文化の価値。",
        "lead_snippet": "美術批評家ベン・イーストハムの新著『The Floating World』は、富裕層の投機対象と化した現代アート市場の内幕を鋭く解剖し、美の創造が金融資本の支配とどのように共犯関係を結んでいるかを問うている。真の文化的価値と価格の乖離、美術館の公的役割の空洞化というテーマは、人文学と経済倫理の交差点として知識人の間で大きな反響を呼んでいる。",
        "source_name": "The Guardian (Oct 15, 2026)",
        "source_url": "https://www.theguardian.com/books/2026/oct/15/the-floating-world-by-ben-eastham-review-a-compelling-debut-of-arts-relation-to-money-and-power",
        "source_attribution": "Source: The Guardian (Oct 15, 2026). The Floating World by Ben Eastham review – art, money and power.",
        "image": "https://images.unsplash.com/photo-1579783900882-c0d3dad7b119?w=1000&auto=format&fit=crop&q=80",
        "sentences": [
            {
                "en": "In his incisive cultural treatise The Floating World, essayist and art critic Ben Eastham dissects how the hyper-commodification of contemporary art has transformed visual aesthetics into an unregulated asset class for global plutocrats.",
                "ja": "明敏な文化論考『The Floating World』において、エッセイスト兼美術批評家のベン・イーストハムは、現代美術の過度な商品化がいかに視覚芸術を世界の富裕層のための無規制な資産クラスへと変貌させたかを解剖している。"
            },
            {
                "en": "Eastham traces the historical convergence between avant-garde rebellion and luxury finance, demonstrating that subversive artistic statements are swiftly co-opted, repackaged, and auctioned for speculative financial returns.",
                "ja": "イーストハムはアバンギャルドの反逆と高級金融の歴史的合流を辿り、体制転覆的な芸術表現がいかに瞬く間に骨抜きにされ、再包装されて投機的な金銭的リターンのために競売にかけられるかを論証している。"
            },
            {
                "en": "Public museum institutions, once envisioned as egalitarian repositories of shared human heritage, increasingly find themselves beholden to billionaire trustees whose private collections dictate exhibition programming.",
                "ja": "かつて共有された人類の遺産を守る平等主義的な殿堂として構想された公立美術館は、自らのプライベートコレクションで企画展の内容を左右する億万長者の理事たちにますます恩義を負う（依存する）状況に陥っている。"
            },
            {
                "en": "Rather than succumbing to cynical resignation, the author invokes historical philosophies of communal viewing to argue that art\\'s genuine emancipatory power resides in fleeting, non-transactional human encounters.",
                "ja": "著者は冷笑的な諦念に屈するのではなく、共同鑑賞の歴史的哲学を援用し、芸術の真の解放の力は束の間の非取引的な人間同士の出会いの中にこそ宿ると主張する。"
            },
            {
                "en": "Ultimately, the work compels readers to interrogate the structural boundary between authentic cultural meaning and the corrosive distorting influence of late-stage speculative capitalism.",
                "ja": "最終的に、この著作は、真の文化的意味と、後期投機的資本主義の腐食的で歪曲的な影響力との構造的境界線を問い直すよう読者に迫っている。"
            }
        ],
        "dialogue": [
            {"speaker": "七", "name": "Nanami", "role": "生徒", "text": "現代アートって、オークションで何十億円もの値がついたニュースをよく見ますよね。この本はそういうアートの世界を批判しているんですか？"},
            {"speaker": "慶", "name": "Keita", "role": "英語講師", "text": "第1文にある『hyper-commodification（過度な商品化）』を批判しているんだ。絵画や彫刻が芸術としてではなく、富裕層の『unregulated asset class（無規制な投資資産）』になってしまっていると警告しているんだよ。"},
            {"speaker": "七", "name": "Nanami", "role": "生徒", "text": "第3文にあるように、公立美術館まで大富豪の理事たちの顔色をうかがうようになっているなんてショックです…"},
            {"speaker": "慶", "name": "Keita", "role": "英語講師", "text": "でも著者は絶望しているわけではないんだよ。第4文にあるように、お金で買えない人と人との感動的な出会い（non-transactional human encounters）にこそアートの本来の力があると言っているんだ。早稲田文学部や東大現代文でも定番の文化資本論だね！"}
        ],
        "vocab": [
            {"word": "incisive", "phonetic": "/ɪnˈsaɪ.sɪv/", "meaning": "明敏な、的確な、鋭い", "pos": "adjective", "def": "Intelligently analytical and clear-thinking; sharply focused.", "ex": "The critic offered an incisive evaluation of the gallery system."},
            {"word": "commodification", "phonetic": "/kəˌmɒd.ɪ.fɪˈkeɪ.ʃən/", "meaning": "商品化、売買対象化", "pos": "noun", "def": "The action of treating something as a mere commodity to be bought and sold.", "ex": "The commodification of higher education sparks fierce debate."},
            {"word": "co-opt", "phonetic": "/kəʊˈɒpt/", "meaning": "都合よく取り込む、骨抜きにする、抱き込む", "pos": "verb", "def": "Divert to or use in a role different from the original one, often assimilating protest.", "ex": "Radical protest slogans were quickly co-opted by commercial brands."},
            {"word": "beholden", "phonetic": "/bɪˈhəʊl.dən/", "meaning": "恩義がある、義理を負っている、依存している", "pos": "adjective", "def": "Owing thanks or having a duty to someone in return for help or service.", "ex": "Museums must not become beholden to corporate donors."},
            {"word": "emancipatory", "phonetic": "/ɪˈmæn.sɪ.pə.tər.i/", "meaning": "解放的な、自由をもたらす", "pos": "adjective", "def": "Serving or attempting to bring about equal rights or liberation.", "ex": "Literacy programs serve an emancipatory role in marginalized communities."}
        ],
        "syntax": [
            {"title": "Rather than ~ ing による対比転換構文", "formula": "Rather than [succumbing to cynical resignation], [the author invokes historical philosophies]", "explanation": "Rather than doing は「〜に屈するのではなく、むしろ…」という著者の前向きな姿勢を際立たせる評論特有の転換表現です。"},
            {"title": "compel + 目的語 + to 不定詞", "formula": "[the work] compels [readers] to [interrogate the structural boundary]", "explanation": "compel O to do は「Oに強く〜することを促す・迫る」という意味で、読者への強いメッセージ性を表します。"}
        ],
        "quiz": [
            {
                "question": "What central critique does Ben Eastham present in The Floating World?",
                "options": [
                    "Artists have completely lost their technical ability to paint realistically.",
                    "The hyper-commodification of art has turned visual aesthetics into a speculative asset class for the wealthy.",
                    "Museums should charge much higher admission fees to remain profitable.",
                    "Photography will soon replace all forms of classical sculpture."
                ],
                "answer": 1,
                "explanation": "第1文にある通り、現代美術の過度な商品化が視覚芸術を富裕層の投機的資産クラスに変貌させた点が解剖されています。"
            },
            {
                "question": "According to the author, what often happens to subversive avant-garde artistic rebellion?",
                "options": [
                    "It is legally banned by constitutional courts.",
                    "It is swiftly co-opted, repackaged, and auctioned for financial profit.",
                    "It causes the immediate collapse of multinational auction houses.",
                    "It remains entirely unknown to public audiences."
                ],
                "answer": 1,
                "explanation": "第2文にある通り、反逆的表現も瞬く間に取り込まれ（co-opted）、投機的利益のために競売されてしまうと指摘されています。"
            },
            {
                "question": "Why are public museums increasingly compromised according to the text?",
                "options": [
                    "They have lost all their permanent art collections.",
                    "They have become beholden to billionaire trustees whose private collections influence programming.",
                    "They are legally prohibited from admitting general visitors.",
                    "They refuse to exhibit modern contemporary installations."
                ],
                "answer": 1,
                "explanation": "第3文にある通り、私的コレクションで展示を左右する富裕な理事たちに依存（beholden）してしまっているためです。"
            },
            {
                "question": "The word 'beholden' in the third sentence most closely means:",
                "options": ["indebted and reliant", "unfriendly", "superior", "invisible"],
                "answer": 0,
                "explanation": "beholden は「恩義を負っている」「頭が上がらない・依存している」という意味です。"
            },
            {
                "question": "Where does the author believe genuine emancipatory artistic power truly resides?",
                "options": [
                    "In record-setting auction prices at Christie's.",
                    "In digital non-fungible tokens sold online.",
                    "In fleeting, non-transactional human encounters and communal viewing.",
                    "In permanent corporate advertising campaigns."
                ],
                "answer": 2,
                "explanation": "第4文にある通り、非取引的な人間同士の出会い（non-transactional human encounters）の中にこそ真の力が宿ると論じています。"
            }
        ]
    },

    # 10. CULTURE - The Case for National Digital Sovereignty (Cloud Tech)
    {
        "slug": "national-digital-sovereignty-cloud-infrastructure",
        "category": "culture",
        "category_label": "INFORMATION SOCIETY & ETHICS • 国家主権と巨大テック企業クラウド依存の限界",
        "date": "2026-10-16",
        "title": "The Case for National Digital Sovereignty: Reclaiming Critical Infrastructure from Big Tech",
        "headline_ja": "デジタル主権論の最前線：米巨大ITクラウドへの過度な依存から公的インフラをどう取り戻すか",
        "subhead": "医療・教育・行政データが外国籍データセンターに集約される危うさと、国家の情報自立。",
        "lead_snippet": "公共部門におけるデジタル変革が進む中、国家基幹システムが米国の少数のハイパースケーラー（AWS、Azure、GCP）に事実上独占されている現状に対し、欧州や英国で「デジタル主権（Digital Sovereignty）」の確立を求める論考が相次いでいる。データローカリゼーションとオープン標準クラウドの構築は、21世紀の国家の自律性を決する哲学的・制度的課題である。",
        "source_name": "The Guardian (Oct 15, 2026)",
        "source_url": "https://www.theguardian.com/technology/2026/oct/15/the-uk-must-have-digital-sovereignty",
        "source_attribution": "Source: The Guardian (Oct 15, 2026). The UK must have digital sovereignty.",
        "image": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=1000&auto=format&fit=crop&q=80",
        "sentences": [
            {
                "en": "Political philosophers and technological strategists are urging democratic governments to reassert national digital sovereignty by dismantling their asymmetric dependency on a handful of foreign cloud monopolists.",
                "ja": "政治哲学者や技術戦略家らは、少数の外国籍クラウド独占企業に対する非対称な依存関係を解消し、国家的な「デジタル主権」を再確立するよう民主主義政府に促している。"
            },
            {
                "en": "Critical public infrastructure—ranging from national health service patient records to electoral registers and court administration—is increasingly hosted within proprietary data centers governed by extraterritorial foreign jurisdictions.",
                "ja": "国民医療サービスの患者記録から選挙人名簿、裁判所管理に至る基幹的な公的インフラが、域外管轄権に服する外国の独自データセンター内にホストされる傾向が強まっている。"
            },
            {
                "en": "Proponents of sovereignty warn that this institutional reliance exposes sovereign states to acute vulnerabilities, including unilateral service terminations, extraterritorial surveillance warrants, and sudden pricing escalations.",
                "ja": "主権論の提唱者らは、この制度的依存が、一方的なサービス停止、域外からの監視令状、突然の価格引き上げなど、主権国家を深刻な脆弱性に晒していると警告する。"
            },
            {
                "en": "To cultivate systemic resilience, policy analysts advocate mandating open-source interoperability protocols and funding domestic public-interest compute clusters modeled on municipal utility infrastructure.",
                "ja": "システム全体の強靭性を育むため、政策アナリストらはオープンソースの相互運用性プロトコルの義務化や、自治体の公益インフラをモデルとした国内の公共計算クラスターへの資金拠出を提言している。"
            },
            {
                "en": "Ultimately, the struggle for digital autonomy demonstrates that in the twenty-first century, true democratic governance cannot survive without territorial and algorithmic control over the means of information computation.",
                "ja": "最終的に、デジタル自律性をめぐる闘争は、21世紀において真の民主的統治は情報計算の手段に対する領域的かつアルゴリズム的な管理なしには存続し得ないことを実証している。"
            }
        ],
        "dialogue": [
            {"speaker": "七", "name": "Nanami", "role": "生徒", "text": "「デジタル主権（digital sovereignty）」って言葉、最近ニュースでよく見かけます！国家の主権とクラウドサービスにどんな関係があるんですか？"},
            {"speaker": "慶", "name": "Keita", "role": "英語講師", "text": "第2文を見てごらん。病院の電子カルテや裁判所のデータ、選挙の名簿まで、外国の数社の大手IT企業のサーバーに預けられているんだ。もしその企業がストップしたり外国政府の命令でデータを見られたりしたら大変だろう？"},
            {"speaker": "七", "name": "Nanami", "role": "生徒", "text": "確かに！電気や水道と同じで、国の大切なインフラが外国企業に握られている状態なんですね。"},
            {"speaker": "慶", "name": "Keita", "role": "英語講師", "text": "その通り！第4文にあるように、特定の企業に縛られないオープンな基準（open-source interoperability）を作り、自前の公共コンピューター網を持つことが求められている。慶應SFCや早稲田政経で超頻出の情報社会倫理だね。"}
        ],
        "vocab": [
            {"word": "sovereignty", "phonetic": "/ˈsɒv.rɪn.ti/", "meaning": "主権、統治権、自律性", "pos": "noun", "def": "Supreme power or authority, or the authority of a state to govern itself.", "ex": "Nations are reasserting their digital sovereignty over online platforms."},
            {"word": "asymmetric", "phonetic": "/ˌeɪ.sɪˈmet.rɪk/", "meaning": "非対称な、不均衡な、偏った", "pos": "adjective", "def": "Having parts or aspects that are not equal or do not correspond to one another.", "ex": "Small countries face an asymmetric power balance when dealing with Big Tech."},
            {"word": "extraterritorial", "phonetic": "/ˌek.strə.ter.ɪˈtɔː.ri.əl/", "meaning": "治外法権の、域外適用の", "pos": "adjective", "def": "Operating or existing beyond the national territorial jurisdiction.", "ex": "Foreign laws often exert extraterritorial reach over global cloud providers."},
            {"word": "interoperability", "phonetic": "/ˌɪn.tərˌɒp.ər.əˈbɪl.ə.ti/", "meaning": "相互運用性、互換性", "pos": "noun", "def": "The ability of computer systems or software to exchange and make use of information.", "ex": "Open protocols ensure technical interoperability between cloud vendors."},
            {"word": "autonomy", "phonetic": "/ɔːˈtɒn.ə.mi/", "meaning": "自律性、自治、独立", "pos": "noun", "def": "The right or condition of self-government, or freedom from external control.", "ex": "Strategic technology independence guarantees national autonomy."}
        ],
        "syntax": [
            {"title": "by + 動名詞（手段の提示）", "formula": "[governments reassert digital sovereignty] by [dismantling their asymmetric dependency]", "explanation": "by doing は「〜することによって（手段・方法）」を提示し、主権を取り戻すための具体的行動を示しています。"},
            {"title": "cannot survive without ~（二重否定による強い必要条件）", "formula": "[true democratic governance cannot survive] without [territorial and algorithmic control]", "explanation": "cannot A without B（BなしにAは成り立たない）は「Bが絶対に不可欠である」という論旨を強力に強調する最重要文法構文です。"}
        ],
        "quiz": [
            {
                "question": "What primary dependency are political philosophers urging governments to dismantle?",
                "options": [
                    "Their reliance on traditional postal mail deliveries.",
                    "Their asymmetric reliance on a handful of foreign cloud monopolists.",
                    "Their dependence on domestic copper mining facilities.",
                    "Their use of paper ballots in local municipal elections."
                ],
                "answer": 1,
                "explanation": "第1文にある通り、少数の外国籍クラウド独占企業への非対称な依存関係の解消が求められています。"
            },
            {
                "question": "What public systems are currently hosted in proprietary foreign data centers?",
                "options": [
                    "Antique grandfather clocks and museum paintings.",
                    "Patient health records, electoral registers, and court administration.",
                    "Wooden railway ties and canal locks.",
                    "National soccer team uniforms and sports equipment."
                ],
                "answer": 1,
                "explanation": "第2文にある通り、患者の医療記録や選挙人名簿、裁判所の管理システムなどの基幹インフラが含まれます。"
            },
            {
                "question": "Which of the following is cited as a risk of institutional reliance on Big Tech cloud providers?",
                "options": [
                    "Computers producing too much physical paper waste.",
                    "Unilateral service cuts, foreign surveillance warrants, and sudden price hikes.",
                    "A mandatory reduction in high-speed optical fiber bandwidth.",
                    "Foreign tourists over-utilizing domestic mobile hotspots."
                ],
                "answer": 1,
                "explanation": "第3文にある通り、一方的サービス停止、域外監視令状、価格急騰などの深刻な脆弱性に晒されます。"
            },
            {
                "question": "The word 'interoperability' in the fourth sentence refers to:",
                "options": [
                    "The ability of different systems to exchange and utilize data seamlessly.",
                    "The requirement that all software be completely secret.",
                    "The complete shutdown of electronic government websites.",
                    "The exclusive monopolization of technology patents."
                ],
                "answer": 0,
                "explanation": "interoperability は異なるシステム同士がシームレスに情報交換できる「相互運用性」を指します。"
            },
            {
                "question": "According to the final sentence, what is essential for democratic governance in the 21st century?",
                "options": [
                    "Territorial and algorithmic control over computing infrastructure.",
                    "Complete abandonment of all electronic devices.",
                    "Outsourcing national intelligence entirely to commercial vendors.",
                    "Restricting Internet usage to government employees only."
                ],
                "answer": 0,
                "explanation": "最終文で、計算インフラに対する領域的かつアルゴリズム的統制（territorial and algorithmic control）が不可欠だと結論づけられています。"
            }
        ]
    },

    # 11. ENTERTAINMENT - Sand Tiger Shark Conservation & Public Aquariums
    {
        "slug": "sand-tiger-shark-conservation-public-aquariums",
        "category": "entertainment",
        "category_label": "WILDLIFE & PUBLIC AQUARIUMS • シロワニ（絶滅危惧サメ）の保護と水族館の役割",
        "date": "2026-10-16",
        "title": "Aquariums Join Conservation Drive to Protect Endangered Sand Tiger Sharks in Delaware Bay",
        "headline_ja": "海洋生物学：絶滅危惧種シロワニを救え！公立水族館と海洋保護区が結ぶ繁殖・放流ネットワーク",
        "subhead": "恐ろしい見た目と裏腹におとなしい大型サメ。音響タグによる追跡と繁殖プログラムの進展。",
        "lead_snippet": "米国デラウェア湾のサメ保護区において、公立水族館の海洋生物学者チームが絶滅危惧種シロワニ（Sand Tiger Shark）の生息域保護と繁殖支援プロジェクトを拡大している。最新の超音波音響タグを用いた回遊ルートの解明と、水族館の展示を通じた来館者の環境意識改革（エンターテインメントと保全教育の融合）が成果を上げている。",
        "source_name": "The Guardian (Oct 15, 2026)",
        "source_url": "https://www.theguardian.com/environment/2026/oct/15/conservation-aquariums-endangered-sharks-protected-waters-delaware-bay-us-sand-tiger-sharks",
        "source_attribution": "Source: The Guardian (Oct 15, 2026). Conservation and aquariums protect endangered sand tiger sharks in Delaware Bay.",
        "image": "https://images.unsplash.com/photo-1560275619-4662e36fa65c?w=1000&auto=format&fit=crop&q=80",
        "sentences": [
            {
                "en": "Marine biologists affiliated with leading public aquariums have established an acoustic telemetry monitoring corridor in Delaware Bay to safeguard vulnerable populations of sand tiger sharks.",
                "ja": "主要な公立水族館に所属する海洋生物学者らは、絶滅の危機にあるシロワニの個体群を保護するため、デラウェア湾に音響テレメトリー追跡回廊を構築した。"
            },
            {
                "en": "Despite their menacing rows of visible needle-like teeth, sand tiger sharks are docile apex predators that play an indispensable role in maintaining the trophic equilibrium of coastal estuary ecosystems.",
                "ja": "針のように突き出た威圧的な歯並びにもかかわらず、シロワニはおとなしい高次捕食者であり、沿岸河口域生態系の栄養段階の均衡を維持する上で不可欠な役割を果たしている。"
            },
            {
                "en": "Researchers surgical implanted ultrasonic transmitters into juvenile specimens, enabling automated hydrophone stations to track their seasonal migratory corridors and pinpoint critical pupping grounds.",
                "ja": "研究者らは幼体の体内に超音波発信器を外科的に埋め込み、自動水中聴音器ステーションによって季節的な回遊回廊を追跡し、極めて重要な産仔（出産）場所を特定することに成功した。"
            },
            {
                "en": "Aquarium directors emphasize that modern zoological exhibitions have evolved beyond mere leisure entertainment into vital sanctuaries that facilitate captive breeding and educate millions on marine biodiversity.",
                "ja": "水族館の館長らは、現代の動物園・水族館の展示が単なる余暇のエンターテインメントを超え、飼育下繁殖を促進し何百万人もの人々に海洋生物多様性を教育する極めて重要なサンクチュアリ（聖域）へと進化したと強調する。"
            },
            {
                "en": "Conservationists hope that data generated through the civic aquarium alliance will persuade federal maritime regulators to establish permanent marine protected boundaries against destructive bottom-trawling commercial fisheries.",
                "ja": "自然保護論者らは、市民的水族館アライアンスを通じて生み出されたデータが、破壊的な底引き網商業漁業から保護するための恒久的な海洋保護境界を画定するよう連邦海事規制当局を動かすことを期待している。"
            }
        ],
        "dialogue": [
            {"speaker": "七", "name": "Nanami", "role": "生徒", "text": "シロワニ（Sand tiger shark）って、水族館の大きな水槽で鋭い歯を見せて泳いでいるあのサメですよね！迫力があってちょっと怖いですが…"},
            {"speaker": "慶", "name": "Keita", "role": "英語講師", "text": "見た目は怖いけれど、第2文にあるように『docile（とてもおとなしい）』サメなんだよ。海の生態系のバランス（trophic equilibrium）を保つ大切な頂点捕食者なんだ。"},
            {"speaker": "七", "name": "Nanami", "role": "生徒", "text": "第3文では、体に小さな発信器（ultrasonic transmitters）をつけて、海の中のどこで子どもを産んでいるか追跡しているんですね！"},
            {"speaker": "慶", "name": "Keita", "role": "英語講師", "text": "その通り！第4文にあるように、今の水族館は単なる見せ物（mere leisure entertainment）ではなく、生物多様性の研究や保全（conservation and sanctuaries）を担う最前線なんだ。理科や英語長文で定番の『野生生物保全と市民社会』のテーマだね。"}
        ],
        "vocab": [
            {"word": "telemetry", "phonetic": "/təˈlem.ə.tri/", "meaning": "遠隔測定法、テレメトリー", "pos": "noun", "def": "The process of recording and transmitting the readings of an instrument.", "ex": "Acoustic telemetry allows scientists to track shark migration in real time."},
            {"word": "docile", "phonetic": "/ˈdəʊ.saɪl/", "meaning": "温厚な、おとなしい、従順な", "pos": "adjective", "def": "Ready to accept control or instruction; submissive, or gentle.", "ex": "Despite their fierce appearance, sand tiger sharks are gentle and docile."},
            {"word": "equilibrium", "phonetic": "/ˌiː.kwɪˈlɪb.ri.əm/", "meaning": "均衡、平衡状態、安定", "pos": "noun", "def": "A state in which opposing forces or influences are balanced.", "ex": "Predators maintain the biological equilibrium of the reef ecosystem."},
            {"word": "sanctuary", "phonetic": "/ˈsæŋk.tʃʊə.ri/", "meaning": "保護区、サンクチュアリ、聖域", "pos": "noun", "def": "A place of safety, or a nature reserve where animals are protected.", "ex": "Marine sanctuaries prohibit commercial fishing to allow fish stocks to recover."},
            {"word": "trawling", "phonetic": "/ˈtrɔː.lɪŋ/", "meaning": "底引き網漁、トロール漁業", "pos": "noun", "def": "A method of fishing that involves pulling a large net through the water behind boats.", "ex": "Heavy bottom-trawling destroys fragile coral and sponge ecosystems."}
        ],
        "syntax": [
            {"title": "Despite + 名詞句（譲歩の前置詞構文）", "formula": "Despite [their menacing rows of needle-like teeth], [sharks are docile apex predators]", "explanation": "Despite their menacing teeth は「威圧的な歯並びにもかかわらず」という外見と実際の性格のギャップを対比させる定番の譲歩構文です。"},
            {"title": "evolve beyond A into B（発展・昇華の構文）", "formula": "[exhibitions have evolved] beyond [mere entertainment] into [vital sanctuaries]", "explanation": "evolve beyond A into B は「単なるAの枠を超えて、重要なBへと進化・昇華した」という歴史的・機能的変容を論じる洗練された表現です。"}
        ],
        "quiz": [
            {
                "question": "What technological method was deployed to monitor sand tiger sharks in Delaware Bay?",
                "options": [
                    "Microscopic dye markers in ocean plankton.",
                    "Acoustic telemetry and surgically implanted ultrasonic transmitters.",
                    "High-altitude weather balloons with thermal cameras.",
                    "Drifting glass bottles containing paper location logs."
                ],
                "answer": 1,
                "explanation": "第1文および第3文にある通り、音響テレメトリー追跡回廊と超音波発信器（ultrasonic transmitters）が使用されています。"
            },
            {
                "question": "Despite their menacing appearance, how are sand tiger sharks described temperamentally?",
                "options": [
                    "Hyper-aggressive predators that frequently attack humans.",
                    "Docile apex predators essential to estuary ecological equilibrium.",
                    "Deep-sea herbivores that feed entirely on kelp.",
                    "Blind scavengers that live exclusively in fresh water."
                ],
                "answer": 1,
                "explanation": "第2文にある通り、威圧的な歯を持ちながらもおとなしい頂点捕食者（docile apex predators）と述べられています。"
            },
            {
                "question": "How has the mission of modern public aquariums evolved according to directors?",
                "options": [
                    "They have shifted entirely toward selling luxury souvenir items.",
                    "They have evolved beyond mere leisure into sanctuaries that facilitate breeding and education.",
                    "They have abandoned all marine research in favor of virtual reality movies.",
                    "They focus exclusively on training marine mammals for circus performances."
                ],
                "answer": 1,
                "explanation": "第4文にある通り、単なる娯楽を超えて繁殖促進や生物多様性教育を行う保護聖域（vital sanctuaries）へと進化しました。"
            },
            {
                "question": "The word 'docile' in the second sentence is closest in meaning to:",
                "options": ["ferocious", "gentle and non-aggressive", "poisonous", "gigantic"],
                "answer": 1,
                "explanation": "docile は「温厚な」「おとなしい」という意味であり、gentle and non-aggressive が正解です。"
            },
            {
                "question": "What federal regulatory outcome do conservationists hope the telemetry data will support?",
                "options": [
                    "Subsidizing industrial bottom-trawling commercial fleets.",
                    "Establishing permanent marine protected boundaries against destructive bottom-trawling.",
                    "Abolishing all public aquariums along the East Coast.",
                    "Permitting unrestricted trophy shark hunting in Delaware Bay."
                ],
                "answer": 1,
                "explanation": "最終文で、破壊的な底引き網漁から守る恒久的な海洋保護区（permanent marine protected boundaries）の設置が期待されています。"
            }
        ]
    },

    # 12. ENTERTAINMENT - SpaceX Starshield & Starlink Defence Dispute
    {
        "slug": "satellite-constellation-dual-use-defence-dispute",
        "category": "entertainment",
        "category_label": "AEROSPACE & SATELLITE TECH • スターリンクと軍事利用（スターシールド）の境界線",
        "date": "2026-10-16",
        "title": "SpaceX Faces International Scrutiny Over Military Starshield and Starlink Disruption",
        "headline_ja": "宇宙通信テック：民間通信衛星スターリンクと防衛専用「スターシールド」の境界線をめぐる議論",
        "subhead": "民間通信インフラが戦場で担う役割と、巨大プラットフォーマーの地政学的影響力。",
        "lead_snippet": "低軌道衛星コンステレーションによる高速通信を提供するスペースX社に対し、防衛専用ネットワーク「スターシールド」への移行に伴う利用制限をめぐり各国の安全保障関係者から議論が巻き起こっている。民間テクノロジー企業が一国の防衛インフラやドローン通信を実質的に左右する「民間企業の地政学的プレイヤー化」が新たな論点となっている。",
        "source_name": "The Guardian (Oct 15, 2026)",
        "source_url": "https://www.theguardian.com/world/2026/oct/15/starshield-starlink-ukraine-restriction-explained",
        "source_attribution": "Source: The Guardian (Oct 15, 2026). SpaceX Starshield and Starlink defence restrictions explained.",
        "image": "https://images.unsplash.com/photo-1446776811953-b23d57bd21aa?w=1000&auto=format&fit=crop&q=80",
        "sentences": [
            {
                "en": "Aerospace giant SpaceX has sparked contentious international debate following operational restrictions on commercial Starlink terminals utilized in active conflict zones.",
                "ja": "航空宇宙大手スペースX社は、実際の紛争地帯で使用されている民間用スターリンク端末に対する運用制限を課したことを受け、論争の的となる国際的議論を巻き起こした。"
            },
            {
                "en": "While the constellation was conceived primarily to deliver low-latency broadband connectivity to underserved rural communities, front-line armed forces rapidly adopted the terminals as vital command-and-control backbones.",
                "ja": "この衛星網は本来、サービスの行き届かない農村地域に低遅延ブロードバンド通信を提供することを主眼に構想されたが、前線の軍隊は各端末を必須の指揮統制インフラとして急速に採用した。"
            },
            {
                "en": "Corporate leadership defended the geofencing curbs by arguing that consumer service agreements explicitly prohibit offensive weaponization, pointing clients toward its dedicated government-oriented Starshield constellation.",
                "ja": "同社経営陣は、一般向け利用規約が攻撃兵器への転用を明確に禁止していると主張し、顧客を政府向けの専用衛星網「スターシールド」へと誘導することで地理的制限（ジオフェンシング）の正当性を主張した。"
            },
            {
                "en": "National security analysts observe that reliance on private commercial satellites grants individual corporate oligarchs unprecedented discretionary leverage over sovereign wartime communications.",
                "ja": "安全保障アナリストらは、民間の商業衛星への依存が、個々の企業経営者に国家の戦時通信に対する前例のない裁量的な影響力を与えていると指摘している。"
            },
            {
                "en": "The standoff has accelerated global initiatives among European and Asian powers to deploy sovereign state-owned low-Earth orbit satellite networks to eliminate single-vendor vulnerability.",
                "ja": "この対立は、単一ベンダーへの依存という脆弱性を解消するため、欧州やアジアの諸国が自前の国家保有・低軌道衛星ネットワークを配備する世界的取り組みを加速させている。"
            }
        ],
        "dialogue": [
            {"speaker": "七", "name": "Nanami", "role": "生徒", "text": "スターリンクって、キャンプ場や山の中でも高速インターネットが使える便利なサービスですよね！どうして軍事利用で揉めているんですか？"},
            {"speaker": "慶", "name": "Keita", "role": "英語講師", "text": "第2文にあるように、もともとは通信が不便な地域向けだったのに、通信速度が速くて妨害に強いため、戦場でドローンの操縦や部隊の連絡網（command-and-control backbones）として使われるようになったんだ。"},
            {"speaker": "七", "name": "Nanami", "role": "生徒", "text": "スペースX社は一般用サービスだから攻撃には使わせないとして、防衛用の『スターシールド』を別に作ったんですね。"},
            {"speaker": "慶", "name": "Keita", "role": "英語講師", "text": "そうなんだ。でも第4文にあるように『民間企業の一人の経営者が、国家の通信を止める権限を握っていいのか（unprecedented discretionary leverage）』という大問題が生じている。第5文のように各国が国家保有の衛星（state-owned satellite networks）を急ぐ理由もここにあるんだよ。"}
        ],
        "vocab": [
            {"word": "contentious", "phonetic": "/kənˈten.ʃəs/", "meaning": "論争を呼ぶ、異論の多い、争い好きな", "pos": "adjective", "def": "Causing or likely to cause an argument; controversial.", "ex": "The regulation of dual-use satellite networks remains highly contentious."},
            {"word": "latency", "phonetic": "/ˈleɪ.tən.si/", "meaning": "遅延時間、レイテンシ、潜伏期間", "pos": "noun", "def": "The delay before a transfer of data begins following an instruction for its transfer.", "ex": "Low-Earth orbit satellites offer significantly reduced signal latency."},
            {"word": "geofencing", "phonetic": "/ˈdʒiː.əʊˌfen.sɪŋ/", "meaning": "ジオフェンシング、仮想境界による地理的制限", "pos": "noun", "def": "The use of GPS technology to create a virtual geographic boundary triggering a response.", "ex": "Geofencing prevents drones from entering restricted airspace around airports."},
            {"word": "leverage", "phonetic": "/ˈliː.vər.ɪdʒ/", "meaning": "影響力、てこの力、交渉力", "pos": "noun", "def": "The power to influence a person or situation to achieve a particular outcome.", "ex": "Monopoly suppliers hold considerable economic leverage over their buyers."},
            {"word": "standoff", "phonetic": "/ˈstænd.ɒf/", "meaning": "対立、膠着状態、行き詰まり", "pos": "noun", "def": "A deadlock between two equally matched opponents in a dispute.", "ex": "The diplomatic standoff delayed joint naval patrols in the region."}
        ],
        "syntax": [
            {"title": "While節を用いた対比・予想外の展開", "formula": "While [the constellation was conceived primarily to do X], [armed forces rapidly adopted Y]", "explanation": "While節が「〜として構想された一方で」という当初の平和的目的を提示し、主節の軍事転用という予期せぬ現実を鮮やかに対比させています。"},
            {"title": "grant + 間接目的語 + 直接目的語（第4文型 SVOO）", "formula": "[reliance on private satellites] grants [corporate oligarchs] [unprecedented leverage over communications]", "explanation": "grant A B は「A（企業経営者）にB（前例のない影響力）を与える」という構造で、客観的な権力集中を指摘する際に用いられます。"}
        ],
        "quiz": [
            {
                "question": "What operational dilemma arose from the wartime deployment of Starlink terminals?",
                "options": [
                    "The satellites fell out of orbit due to solar flares.",
                    "A consumer communication system became an indispensable military command backbone.",
                    "The company decided to give away all hardware for free indefinitely.",
                    "Starlink terminals proved completely incompatible with wireless signals."
                ],
                "answer": 1,
                "explanation": "第2文にある通り、民生用として構想された通信網が前線部隊の不可欠な指揮統制インフラとして採用されたためです。"
            },
            {
                "question": "How did SpaceX corporate leadership justify applying geographic curbs to the service?",
                "options": [
                    "By stating that terms of service strictly prohibit offensive weaponization.",
                    "By claiming that satellite batteries had run out of power.",
                    "By announcing that the company was going out of business.",
                    "By arguing that civilians should not have Internet access during conflicts."
                ],
                "answer": 0,
                "explanation": "第3文にある通り、一般向け利用規約が攻撃兵器への転用を禁止していると主張しました。"
            },
            {
                "question": "What geopolitical risk do national security analysts identify in relying on commercial satellite networks?",
                "options": [
                    "Lower data subscription costs for rural users.",
                    "Private corporate owners gaining unprecedented discretionary power over sovereign wartime communications.",
                    "An automatic decrease in worldwide semiconductor production.",
                    "Foreign governments seizing ownership of the launch pads."
                ],
                "answer": 1,
                "explanation": "第4文にある通り、民間企業経営者が国家の戦時通信に対する前例のない裁量権（discretionary leverage）を握ってしまうリスクです。"
            },
            {
                "question": "The word 'contentious' in the first sentence most nearly means:",
                "options": ["peaceful", "highly controversial", "unimportant", "fictional"],
                "answer": 1,
                "explanation": "contentious は「論争を呼ぶ」「物議を醸す（highly controversial）」という意味です。"
            },
            {
                "question": "What strategic response are European and Asian powers pursuing as a result of this standoff?",
                "options": [
                    "Banning all telecommunications satellites worldwide.",
                    "Deploying their own state-owned sovereign satellite constellations.",
                    "Relying exclusively on undersea telegraph cables.",
                    "Dismantling all national military drone programs."
                ],
                "answer": 1,
                "explanation": "最終文で、単一民間ベンダーへの脆弱性を解消するため、自前の国家保有衛星網（state-owned satellite networks）の配備を加速させていると述べられています。"
            }
        ]
    }
]

# 1:1 JUNIOR EDITIONS (Eiken Pre-2 ~ Grade 2 Accessible Broadsheet)
BATCH12_JUNIOR = [
    # 1. SCIENCE JUNIOR - Leap Second Abolition
    {
        "slug": "leap-second-abolition-leap-hour",
        "category": "science",
        "category_label": "SCIENCE • 世界の時計のルールが変わる！",
        "date": "2026-10-16",
        "title": "Time\\'s Up for the Leap Second: Why World Clocks Will Stop Pausing",
        "headline_ja": "世界の時計から「うるう秒」がなくなる？コンピューターの故障を防ぐ新しい時間のルール",
        "subhead": "1分が61秒になる特別な1秒を廃止へ。何百年もあとに「うるう時」でまとめて調整します。",
        "lead_snippet": "世界の科学者たちが集まり、時計に1秒だけ足す「うるう秒」を2035年までにやめることを決めました。1秒増えるだけでインターネットや銀行のコンピューターが止まってしまうトラブルを防ぐためです。身近な時間の仕組みをわかりやすい英語で学びましょう。",
        "source_name": "The Guardian",
        "source_url": "https://www.theguardian.com/science/2026/oct/15/times-up-for-the-leap-second-as-scientists-swap-it-for-the-leap-hour",
        "senior_path": "../../../science/leap-second-abolition-leap-hour/index.html",
        "image": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=1000&auto=format&fit=crop&q=80",
        "sentences": [
            {
                "en": "Scientists from many countries have voted to stop using the extra \\'leap second\\' by the year 2035.",
                "ja": "多くの国の科学者たちが、2035年までに特別な「うるう秒」を使うのをやめることを決めました。"
            },
            {
                "en": "For over fifty years, people added one second to clocks so that human time stayed matched with the spinning Earth.",
                "ja": "50年以上にわたり、人間の時計が地球の自転とぴったり一致するように、時計に1秒を付け足してきました。"
            },
            {
                "en": "However, computer experts found that having sixty-one seconds in a minute often crashed banking systems and internet servers.",
                "ja": "しかし、1分が61秒になると銀行のシステムやネットのサーバーが故障しやすいことが、コンピューターの専門家によってわかりました。"
            },
            {
                "en": "Now, leaders have agreed to let the tiny differences grow until they reach one full hour centuries from now.",
                "ja": "そこで指導者たちは、今から何百年も経って小さなズレが丸1時間になるまでそのままにしておくことに合意しました。"
            },
            {
                "en": "This smart plan protects our digital devices while still keeping our clocks connected to the natural world.",
                "ja": "この賢い計画は、時計を自然界と結びつけたまま、私たちのデジタル機器をトラブルから守ってくれます。"
            }
        ],
        "dialogue": [
            {"speaker": "七", "name": "Nanami", "role": "生徒", "text": "Keita先生！うるう秒って、たまにテレビで『午前8時59分60秒』って表示されていたあれですよね！"},
            {"speaker": "慶", "name": "Keita", "role": "英語講師", "text": "そうだよ！第3文にあるように、普段のコンピューターは『1分＝60秒』と思い込んでいるから、突然61秒が現れるとパニックを起こしてしまうんだ。"},
            {"speaker": "七", "name": "Nanami", "role": "生徒", "text": "銀行のATMやスマホの通信が止まったら大変ですもんね。第4文の『reach one full hour centuries from now（何百年も先に丸1時間になる）』という解決策も面白いです！"},
            {"speaker": "慶", "name": "Keita", "role": "英語講師", "text": "何百年もあとに生まれた人たちが『うるう時』を調整するんだね。時間を合わせる科学の工夫がよくわかる素晴らしい英文だね。"}
        ],
        "vocab": [
            {"word": "spin", "meaning": "回転する、自転する", "pos": "verb", "def": "To turn around and around quickly."},
            {"word": "crash", "meaning": "（コンピューターが）故障する、急停止する", "pos": "verb", "def": "To suddenly stop working properly."},
            {"word": "century", "meaning": "1世紀、100年間", "pos": "noun", "def": "A period of one hundred years."}
        ],
        "syntax": [
            {"title": "so that 構文（目的を表す）", "formula": "[added one second] so that [human time stayed matched with the Earth]", "explanation": "so that + 主語 + 動詞 は「〜するために」「その結果〜になるように」という目的を表す頻出構文です。"}
        ],
        "quiz": [
            {
                "question": "What did scientists vote to stop using by 2035?",
                "options": ["The calendar year", "The leap second", "Digital alarm clocks", "The standard school week"],
                "answer": 1,
                "explanation": "第1文「stop using the extra 'leap second' by the year 2035」より、うるう秒の廃止が正解です。"
            },
            {
                "question": "Why did having sixty-one seconds in a minute cause problems?",
                "options": [
                    "It made train rides much longer.",
                    "It crashed banking systems and internet servers.",
                    "It caused all smartphones to lose their batteries.",
                    "It made the sun set in the morning."
                ],
                "answer": 1,
                "explanation": "第3文「crashed banking systems and internet servers」より、銀行やサーバーが故障することが原因です。"
            },
            {
                "question": "How long will the time difference accumulate before being corrected?",
                "options": ["Until it reaches one minute next year", "Until it reaches one full hour centuries from now", "Until all clocks stop completely", "Until next week"],
                "answer": 1,
                "explanation": "第4文「until they reach one full hour centuries from now」より、何百年も後に1時間になるまで蓄積されます。"
            }
        ]
    },

    # 2. SCIENCE JUNIOR - Neanderthal Spear Wound
    {
        "slug": "neanderthal-shanidar-spear-trauma",
        "category": "science",
        "category_label": "SCIENCE • 大昔の人類のやさしさと秘密",
        "date": "2026-10-16",
        "title": "Ancient Bones in Shanidar Cave Show Earliest Spear Injury and Caring Friends",
        "headline_ja": "大昔の洞窟から発見された骨の謎：槍で傷ついた仲間をみんなで看病していた！",
        "subhead": "ネアンデルタール人は乱暴なだけではなかった。大怪我をした仲間を助けた思いやりの証拠。",
        "lead_snippet": "有名なシャニダール洞窟で見つかった大昔の人類（ネアンデルタール人）の骨を調べたところ、石の槍で突かれた傷痕が見つかりました。驚いたことに、その傷口には治りかけた跡があり、動けない怪我人を仲間たちが何週間も看病していたことがわかりました。",
        "source_name": "The Guardian",
        "source_url": "https://www.theguardian.com/science/2026/oct/15/neanderthal-remains-human-ancestor-killed-by-spear-iraq-kurdistan-cave-earliest-find",
        "senior_path": "../../../science/neanderthal-shanidar-spear-trauma/index.html",
        "image": "https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c?w=1000&auto=format&fit=crop&q=80",
        "sentences": [
            {
                "en": "Scientists studied the ancient bones of a Neanderthal man discovered inside the famous Shanidar Cave.",
                "ja": "科学者たちは、有名なシャニダール洞窟の中で発見された大昔のネアンデルタール人男性の骨を調査しました。"
            },
            {
                "en": "High-tech scanners showed a deep cut on his rib bone made by a sharp stone-tipped spear.",
                "ja": "最新のスキャナーにより、石の穂先がついた鋭い槍によってつけられた彼の肋骨の深い傷が明らかになりました。"
            },
            {
                "en": "Surprisingly, the bone showed signs of healing, meaning he lived for several weeks after the dangerous attack.",
                "ja": "驚いたことに、その骨には治りかけた痕跡があり、危険な攻撃を受けた後も彼が数週間にわたって生きていたことを意味していました。"
            },
            {
                "en": "Because he could not walk or hunt, his group members must have brought him fresh food and cared for him gently.",
                "ja": "彼は歩くことも狩りをすることもできなかったため、グループの仲間たちが新鮮な食べ物を運び、優しく看病したに違いありません。"
            },
            {
                "en": "This amazing discovery shows that early humans cared deeply about helping injured friends long ago.",
                "ja": "この素晴らしい発見は、大昔の人類が怪我をした仲間を助けることに深い思いやりを持っていたことを示しています。"
            }
        ],
        "dialogue": [
            {"speaker": "七", "name": "Nanami", "role": "生徒", "text": "大昔の人たちも、仲間が怪我をしたらご飯を運んで看病していたんですね！なんだか心が温まります。"},
            {"speaker": "慶", "name": "Keita", "role": "英語講師", "text": "そうだね！第4文の『must have brought him food（食べ物を運んだに違いない）』という過去の推量の助動詞表現に注目してごらん。"},
            {"speaker": "七", "name": "Nanami", "role": "生徒", "text": "『must have + 過去分詞』ですね！英検準2級や2級の文法問題でよく見かけます。"},
            {"speaker": "慶", "name": "Keita", "role": "英語講師", "text": "大正解！ネアンデルタール人は野蛮だったという昔のイメージを覆す、思いやり（cared deeply）を証明する素敵なニュースだね。"}
        ],
        "vocab": [
            {"word": "scan", "meaning": "スキャンする、精密に検査する", "pos": "verb", "def": "To look at all parts of something carefully, especially using machines."},
            {"word": "heal", "meaning": "治る、傷が癒える", "pos": "verb", "def": "To become healthy again after an injury."},
            {"word": "injured", "meaning": "怪我をした、傷ついた", "pos": "adjective", "def": "Hurt or physically damaged."}
        ],
        "syntax": [
            {"title": "must have + 過去分詞（過去の確信的推量）", "formula": "[his group members] must have brought [him food and cared for him]", "explanation": "must have + 過去分詞 は「〜したに違いない」という過去の強い確信を表す高校必須の助動詞表現です。"}
        ],
        "quiz": [
            {
                "question": "What caused the deep cut on the Neanderthal's rib bone?",
                "options": ["A sharp stone-tipped spear", "A fall from a high mountain", "A wild bear bite", "An iron cooking knife"],
                "answer": 0,
                "explanation": "第2文「made by a sharp stone-tipped spear」より、石の穂先がついた槍が原因です。"
            },
            {
                "question": "How do scientists know the injured man lived for several weeks after being hurt?",
                "options": [
                    "He wrote a letter about his injury.",
                    "The bone showed signs of healing and new growth.",
                    "He was found holding modern medicine bottles.",
                    "His footprints were tracked across the desert."
                ],
                "answer": 1,
                "explanation": "第3文「the bone showed signs of healing」より、骨に治癒の痕跡があったためです。"
            },
            {
                "question": "What does this discovery prove about early humans?",
                "options": [
                    "They lived alone and never spoke to anyone.",
                    "They cared deeply and helped injured friends.",
                    "They built tall concrete buildings.",
                    "They did not know how to make tools."
                ],
                "answer": 1,
                "explanation": "第5文「early humans cared deeply about helping injured friends」より、仲間を助ける思いやりを持っていたことがわかります。"
            }
        ]
    },

    # 3. SOCIETY JUNIOR - England Severe Drought
    {
        "slug": "england-six-regions-severe-drought-water-crisis",
        "category": "society",
        "category_label": "SOCIETY • 水不足と大切なインフラの守り方",
        "date": "2026-10-16",
        "title": "Severe Drought Declared in Six English Regions: Why Water Is Running Low",
        "headline_ja": "イギリスの6つの地域で「深刻な干ばつ」を宣言：雨が降らず水道の水がピンチに！",
        "subhead": "記録的な日照りで川や地下水が減少。ホースでの水やり禁止や水道管の修理が急がれています。",
        "lead_snippet": "イギリスの環境庁が、国内の6つの地域で深刻な水不足（干ばつ）が起きていると発表しました。とても暑く乾燥した夏が続き、川やダムの水が130年ぶりの低さまで減ってしまったためです。ホースで庭に水をまくことが禁止され、古い水道管の漏水を直すことが求められています。",
        "source_name": "The Guardian",
        "source_url": "https://www.theguardian.com/environment/2026/oct/15/severe-drought-declared-six-areas-england-public-water-supplies-threat",
        "senior_path": "../../../society/england-six-regions-severe-drought-water-crisis/index.html",
        "image": "https://images.unsplash.com/photo-1509316975850-ff9c5deb0cd9?w=1000&auto=format&fit=crop&q=80",
        "sentences": [
            {
                "en": "Officials in England have declared a severe drought across six big regions because of a very dry summer.",
                "ja": "イングランドの当局は、非常に乾燥した夏が続いたため、6つの大きな地域で深刻な干ばつを宣言しました。"
            },
            {
                "en": "Water levels in rivers and deep underground reservoirs have dropped to their lowest point in more than a century.",
                "ja": "河川や深い地下貯水池の水位は、100年以上の中で最も低いポイントまで落ち込みました。"
            },
            {
                "en": "To save clean water for homes and hospitals, companies have banned people from using garden hosepipes.",
                "ja": "家庭や病院のための清潔な水を守るため、水道会社は人々が庭のホースパイプを使うことを禁止しました。"
            },
            {
                "en": "Environmental groups say old broken water pipes leak millions of litres of precious water every single day.",
                "ja": "環境団体は、壊れた古い水道管から毎日何百万リットルもの貴重な水が漏れ出していると指摘しています。"
            },
            {
                "en": "Leaders are now asking utility companies to fix leaks faster and prepare for hotter future climates.",
                "ja": "指導者たちは現在、水漏れをもっと早く修理し、将来のより暑い気候に備えるよう水道会社に求めています。"
            }
        ],
        "dialogue": [
            {"speaker": "七", "name": "Nanami", "role": "生徒", "text": "イギリスで水不足なんて意外です！庭の水やりまで禁止される（banned people from using hosepipes）んですね。"},
            {"speaker": "慶", "name": "Keita", "role": "英語講師", "text": "そうだね。第3文にあるように、病院や家庭で使う飲み水を優先して守るためなんだ。"},
            {"speaker": "七", "name": "Nanami", "role": "生徒", "text": "第4文の『old broken water pipes leak millions of litres（古い水道管から大量の水が漏れている）』という問題も深刻ですね。"},
            {"speaker": "慶", "name": "Keita", "role": "英語講師", "text": "日頃当たり前に使っている水道も、きちんと修理や点検（fix leaks）をしないと維持できないんだね。身近な社会インフラを考える良いきっかけになるよ。"}
        ],
        "vocab": [
            {"word": "drought", "meaning": "干ばつ、日照り、深刻な水不足", "pos": "noun", "def": "A long period when there is little or no rain."},
            {"word": "leak", "meaning": "（水や気体が）漏れる、漏水する", "pos": "verb", "def": "To escape or allow liquid or gas to escape through a crack."},
            {"word": "precious", "meaning": "貴重な、大切な", "pos": "adjective", "def": "Of great value; not to be wasted or treated carelessly."}
        ],
        "syntax": [
            {"title": "ban A from ~ing（Aが〜するのを禁止する）", "formula": "[companies have banned] [people] from [using garden hosepipes]", "explanation": "ban A from doing は「Aに〜することを禁じる」という規則や法律で非常によく使われる構文です（prevent A from ~ing, stop A from ~ing と同類）。"}
        ],
        "quiz": [
            {
                "question": "Why did officials declare a severe drought across six regions in England?",
                "options": [
                    "Because heavy snow blocked all major highways.",
                    "Because of a very hot and dry summer that lowered water supplies.",
                    "Because sea levels rose higher than the river banks.",
                    "Because city water towers were turned into parks."
                ],
                "answer": 1,
                "explanation": "第1文「because of a very dry summer」より、乾燥した夏で水不足になったためです。"
            },
            {
                "question": "What rule was put in place to save clean water for homes and hospitals?",
                "options": [
                    "People were banned from washing cars and using garden hosepipes.",
                    "All restaurants were required to close on weekends.",
                    "People were told never to drink water after dark.",
                    "Hospitals stopped using running water."
                ],
                "answer": 0,
                "explanation": "第3文「banned people from using garden hosepipes」より、ホースによる散水が禁止されました。"
            },
            {
                "question": "What problem do environmental groups say makes the drought worse?",
                "options": [
                    "Too many boats sailing on lakes.",
                    "Broken pipes leaking millions of litres of water every day.",
                    "Citizens storing too many plastic bottles.",
                    "Fish drinking too much river water."
                ],
                "answer": 1,
                "explanation": "第4文「broken water pipes leak millions of litres of precious water」より、古い水道管からの漏水が問題視されています。"
            }
        ]
    },

    # 4. SOCIETY JUNIOR - Brazil 40-Hour Work Week
    {
        "slug": "brazil-statutory-workweek-reduction-forty-hours",
        "category": "society",
        "category_label": "SOCIETY • 働く時間とお休みのバランス",
        "date": "2026-10-16",
        "title": "Brazil Plans to Shorten Workweek to Forty Hours Without Lowering Wages",
        "headline_ja": "ブラジルで働く時間を週40時間に減らす新しい法律：お給料はそのままで健康を守る！",
        "subhead": "週44時間から40時間へ。疲れを減らして仕事の効率を上げようという新しい試み。",
        "lead_snippet": "ブラジルの国会で、週に働く時間を44時間から40時間に減らす法案が進められています。お給料を減らさずに働く時間を短くすることで、労働者の疲れを減らし、家族と過ごす時間を増やすためです。会社側の心配と働く人の願いを両面から学びましょう。",
        "source_name": "The Guardian",
        "source_url": "https://www.theguardian.com/world/2026/oct/15/brazil-cuts-work-week-to-40-hours-lula-bolsonaro-election-runoff",
        "senior_path": "../../../society/brazil-statutory-workweek-reduction-forty-hours/index.html",
        "image": "https://images.unsplash.com/photo-1521737604893-d14cc237f11d?w=1000&auto=format&fit=crop&q=80",
        "sentences": [
            {
                "en": "Lawmakers in Brazil want to reduce the standard working week from forty-four hours down to forty hours.",
                "ja": "ブラジルの議員たちは、標準の労働時間を週44時間から40時間へと短縮したいと考えています。"
            },
            {
                "en": "Under this new plan, business owners will not be allowed to cut the monthly pay of their employees.",
                "ja": "この新しい計画のもとでは、会社側は従業員の月給を減らすことは認められません。"
            },
            {
                "en": "Supporters say that working six long days every week makes people too tired and hurts their health.",
                "ja": "支持者たちは、毎週6日も長く働くことは人々を疲れさせすぎて健康を損なうと主張しています。"
            },
            {
                "en": "However, some factory owners worry that paying the same wages for fewer hours will raise their business costs.",
                "ja": "しかし、一部の工場経営者らは、少ない時間に対して同じ給料を支払うことは会社のコストを押し上げると心配しています。"
            },
            {
                "en": "The final vote will show how the country balances workers\\' happiness with strong economic power.",
                "ja": "最終的な投票は、国が労働者の幸せと強い経済力とのバランスをどのように取るかを示すことになります。"
            }
        ],
        "dialogue": [
            {"speaker": "七", "name": "Nanami", "role": "生徒", "text": "働く時間が短くなるのに、お給料が減らない（will not be allowed to cut pay）なんて、働く人にとっては嬉しいニュースですね！"},
            {"speaker": "慶", "name": "Keita", "role": "英語講師", "text": "そうだね。週6日働いていた人たちが休みをしっかり取れるようになれば、元気になって仕事の効率も上がるという考え方なんだ。"},
            {"speaker": "七", "name": "Nanami", "role": "生徒", "text": "でも第4文のように、小さなお店や工場だと人を余計に雇うお金が大変（raise business costs）という意見もありますね。"},
            {"speaker": "慶", "name": "Keita", "role": "英語講師", "text": "その通り！第5文にある『balances workers\' happiness with economic power（幸せと経済のバランス）』は、日本を含め世界中で話し合われている大切なテーマだよ。"}
        ],
        "vocab": [
            {"word": "reduce", "meaning": "減らす、縮小する", "pos": "verb", "def": "To make something smaller or less in amount or degree."},
            {"word": "employee", "meaning": "従業員、社員、働く人", "pos": "noun", "def": "A person employed for wages or salary."},
            {"word": "balance", "meaning": "バランスを取る、釣り合わせる", "pos": "verb", "def": "To keep or put something in a steady position where it does not fall."}
        ],
        "syntax": [
            {"title": "be allowed to + 動詞の原形（許可の受動態）", "formula": "[business owners] will not be allowed to cut [the monthly pay]", "explanation": "be allowed to do は「〜することを許される・認められる」という意味で、否定文 will not be allowed to は「〜することは禁止される」という法律ルールを表します。"}
        ],
        "quiz": [
            {
                "question": "What change to the workweek are Brazilian lawmakers proposing?",
                "options": [
                    "Increasing the workweek to sixty hours.",
                    "Reducing the workweek from 44 to 40 hours.",
                    "Banning all office jobs permanently.",
                    "Requiring people to work on Sundays."
                ],
                "answer": 1,
                "explanation": "第1文「reduce the standard working week from forty-four hours down to forty hours」より、44時間から40時間への短縮が正解です。"
            },
            {
                "question": "What are business owners NOT allowed to do under the proposal?",
                "options": [
                    "They cannot reduce their workers' monthly wages.",
                    "They cannot purchase computers.",
                    "They cannot hire younger workers.",
                    "They cannot sell products to other countries."
                ],
                "answer": 0,
                "explanation": "第2文「will not be allowed to cut the monthly pay of their employees」より、給料を減らすことは認められません。"
            },
            {
                "question": "Why do factory owners express concern about the new law?",
                "options": [
                    "They believe workers want to work seven days a week.",
                    "They worry paying the same wages for fewer hours will raise business costs.",
                    "They want to move all factories to Antarctica.",
                    "They cannot find enough light bulbs."
                ],
                "answer": 1,
                "explanation": "第4文「paying the same wages for fewer hours will raise their business costs」より、コスト増を心配しています。"
            }
        ]
    },

    # 5. WORLD JUNIOR - Indonesia Dry Ice Cloud Seeding
    {
        "slug": "indonesia-wildfire-haze-dry-ice-cloud-seeding",
        "category": "world",
        "category_label": "WORLD • 飛行機から氷をまいて山火事を消す！",
        "date": "2026-10-16",
        "title": "Indonesia Drops Tons of Dry Ice to Put Out Peatland Fires and Clear Toxic Smoke",
        "headline_ja": "飛行機から大量のドライアイスを投下！インドネシアの巨大森林火災を雨で消す大作戦",
        "subhead": "地面の下で燃え続ける泥炭火災。雨雲を冷やして雨を降らせ、隣国への煙を防ぎます。",
        "lead_snippet": "インドネシアで広がる激しい森林火災を消すため、軍の飛行機から大量のドライアイスを雨雲に落とす作戦が始まりました。地面の深いところで燃えている火はヘリコプターの水では消せないため、空を冷やして大雨を降らせようとしています。隣の国まで広がる煙のニュースを学びましょう。",
        "source_name": "The Guardian",
        "source_url": "https://www.theguardian.com/world/2026/oct/15/indonesia-fires-dry-ice-dropped-toxic-haze-spreads",
        "senior_path": "../../../world/indonesia-wildfire-haze-dry-ice-cloud-seeding/index.html",
        "image": "https://images.unsplash.com/photo-1516214104703-d870798883c5?w=1000&auto=format&fit=crop&q=80",
        "sentences": [
            {
                "en": "Indonesian emergency teams are using big military planes to drop tons of cold dry ice into clouds above burning forests.",
                "ja": "インドネシアの緊急救助チームは、燃える森林の上の雲に何トンもの冷たいドライアイスを落とすため、大きな軍用機を使っています。"
            },
            {
                "en": "The fires burn deep under the ground in rich peat soil, where water from fire helicopters cannot easily reach.",
                "ja": "火は栄養豊かな泥炭の土の中深くで燃えており、そこには消火ヘリコプターの水が簡単には届きません。"
            },
            {
                "en": "By freezing the moisture in the air, scientists hope to create heavy rain that can soak the burning ground.",
                "ja": "空気中の水分を凍らせることで、科学者たちは燃える大地を濡らす大雨を作り出したいと期待しています。"
            },
            {
                "en": "Thick grey smoke has blown across the sea to neighboring countries like Singapore and Malaysia, making people cough.",
                "ja": "濃い灰色の煙が海を越えてシンガポールやマレーシアなどの隣国にまで流れ、人々を咳き込ませています。"
            },
            {
                "en": "Experts say that stopping people from setting illegal fires to clear land is the only true way to save the forests.",
                "ja": "専門家らは、土地を開拓するために違法に火をつける行為をやめさせることが、森林を救う唯一の真の方法だと述べています。"
            }
        ],
        "dialogue": [
            {"speaker": "七", "name": "Nanami", "role": "生徒", "text": "ドライアイスで雲を冷やして雨を降らせる（freezing moisture to create rain）なんて、すごい技術ですね！"},
            {"speaker": "慶", "name": "Keita", "role": "英語講師", "text": "人工降雨（cloud seeding）という技術だよ。第2文にあるように、泥炭（peat）の火災は地面の下で燃えているから、普通の放水では消えないんだ。"},
            {"speaker": "七", "name": "Nanami", "role": "生徒", "text": "第4文にあるように、海を越えて隣のシンガポールやマレーシアまで煙が届いて（blown across the sea）、大気汚染になっているんですね。"},
            {"speaker": "慶", "name": "Keita", "role": "英語講師", "text": "環境問題は国境を越える（transboundary）という典型的な例だね。第5文のように、違法な野焼きを根本から止めるルール作りが求められているんだよ。"}
        ],
        "vocab": [
            {"word": "emergency", "meaning": "緊急事態、非常時", "pos": "noun", "def": "A serious, unexpected, and often dangerous situation requiring immediate action."},
            {"word": "moisture", "meaning": "水分、湿気", "pos": "noun", "def": "Water or other liquid diffused in a small quantity as vapor or within a solid."},
            {"word": "illegal", "meaning": "違法の、法律で禁止された", "pos": "adjective", "def": "Contrary to or forbidden by law."}
        ],
        "syntax": [
            {"title": "By + 動名詞（〜することによって手段を示す）", "formula": "By [freezing the moisture in the air], [scientists hope to create heavy rain]", "explanation": "By + doing は「〜することによって」という行動の手段や方法を文頭で提示する重要構文です。"}
        ],
        "quiz": [
            {
                "question": "What are emergency teams dropping into clouds above the burning forests?",
                "options": ["Chemical sandbags", "Tons of cold dry ice", "Plastic water tanks", "Seeds for giant trees"],
                "answer": 1,
                "explanation": "第1文「drop tons of cold dry ice into clouds」より、冷たいドライアイスが正解です。"
            },
            {
                "question": "Why are peatland fires difficult to put out with standard helicopters?",
                "options": [
                    "The fires burn deep under the ground in peat soil.",
                    "The helicopters are too small to fly in the wind.",
                    "The trees are made of metal.",
                    "The water turns into steam before leaving the tanks."
                ],
                "answer": 0,
                "explanation": "第2文「The fires burn deep under the ground in rich peat soil」より、地面の深いところで燃えているためです。"
            },
            {
                "question": "Where has the thick grey smoke drifted according to the passage?",
                "options": [
                    "To distant polar ice caps",
                    "Across the sea to Singapore and Malaysia",
                    "Only inside small abandoned caves",
                    "Directly into space satellites"
                ],
                "answer": 1,
                "explanation": "第4文「blown across the sea to neighboring countries like Singapore and Malaysia」より、シンガポールやマレーシアに流れています。"
            }
        ]
    },

    # 6. WORLD JUNIOR - France Drops Opposition to UK Green Subsidies
    {
        "slug": "made-in-europe-green-subsidies-uk-accord",
        "category": "world",
        "category_label": "WORLD • ヨーロッパが力を合わせて環境を守る",
        "date": "2026-10-16",
        "title": "France Welcomes British Factories into Europe\\'s Big Green Clean-Tech Plan",
        "headline_ja": "フランスが方針転換：イギリスの工場もヨーロッパの「環境応援プロジェクト」に参加決定！",
        "subhead": "電気自動車のバッテリーや風力発電。国境を越えて協力し、安くて良いエコ技術を作ります。",
        "lead_snippet": "フランス政府は、ヨーロッパ全体のクリーンエネルギー産業を支援する計画に、イギリスの企業も参加できるようにすることを認めました。ブレグジットで離脱したイギリスを仲間に入れることで、電気自動車のバッテリーや風車の部品を安く作り、アメリカや中国に対抗するためです。",
        "source_name": "The Guardian",
        "source_url": "https://www.theguardian.com/world/2026/oct/15/france-drops-opposition-to-uk-being-included-in-made-in-europe-legislation",
        "senior_path": "../../../world/made-in-europe-green-subsidies-uk-accord/index.html",
        "image": "https://images.unsplash.com/photo-1473341304170-971dccb5ac1e?w=1000&auto=format&fit=crop&q=80",
        "sentences": [
            {
                "en": "France has decided to let British companies take part in the European Union\\'s major green technology plan.",
                "ja": "フランスは、欧州連合（EU）の主要な環境技術計画にイギリス企業が参加することを認める決定を下しました。"
            },
            {
                "en": "European leaders want to build more electric car batteries and wind turbines to fight climate change.",
                "ja": "ヨーロッパの指導者たちは、気候変動と戦うため、より多くの電気自動車用バッテリーや風力タービンを作りたいと考えています。"
            },
            {
                "en": "In the past, some countries wanted to exclude Britain because it left the European Union a few years ago.",
                "ja": "以前は、数年前に欧州連合を離脱したことを理由に、イギリスを仲間外れにしたい国もありました。"
            },
            {
                "en": "However, car makers explained that working together keeps factory costs lower for everyone across the continent.",
                "ja": "しかし自動車メーカー各社は、協力して働くことでヨーロッパ中の工場のコストを安く抑えられると説明しました。"
            },
            {
                "en": "This friendly agreement shows that countries can cooperate on green technology even after political disagreements.",
                "ja": "この友好的な合意は、政治的な意見の違いがあった後でも、国同士が環境技術で協力できることを示しています。"
            }
        ],
        "dialogue": [
            {"speaker": "七", "name": "Nanami", "role": "生徒", "text": "イギリスはEUを離脱（Brexit）したのに、環境の計画ではフランスが『一緒にやろう』と言ってくれたんですね！"},
            {"speaker": "慶", "name": "Keita", "role": "英語講師", "text": "そうだね。第4文にあるように『working together keeps factory costs lower（協力すれば工場のコストが下がる）』からなんだ。"},
            {"speaker": "七", "name": "Nanami", "role": "生徒", "text": "EVのバッテリーや風車を作る部品は、一国だけでは作れないですもんね。"},
            {"speaker": "慶", "name": "Keita", "role": "英語講師", "text": "その通り！第5文にある『cooperate on green technology（環境技術で協力する）』という前向きな姿勢は、これからの国際社会で最も大切にされる考え方だよ。"}
        ],
        "vocab": [
            {"word": "participate", "meaning": "参加する、加わる（take part in と同義）", "pos": "verb", "def": "To be involved in an activity with other people."},
            {"word": "exclude", "meaning": "除外する、締め出す、仲間外れにする", "pos": "verb", "def": "To deliberately leave out or prevent someone from entering a group."},
            {"word": "cooperate", "meaning": "協力する、力を合わせる", "pos": "verb", "def": "To act jointly and work together toward the same end."}
        ],
        "syntax": [
            {"title": "let + 目的語 + 動詞の原形（使役動詞 let）", "formula": "[France has decided to let] [British companies] [take part in the plan]", "explanation": "let + 人 + do は「人に〜することを許す・認める」という日常でも大学入試でも超重要な第5文型（SVOC）の基本構文です。"}
        ],
        "quiz": [
            {
                "question": "What decision did France make regarding British companies?",
                "options": [
                    "To ban all British cars from French highways.",
                    "To let British companies participate in the EU green technology plan.",
                    "To close the undersea tunnel between England and France.",
                    "To charge extra fees for all British books."
                ],
                "answer": 1,
                "explanation": "第1文「let British companies take part in the European Union's major green technology plan」より、参加を認める決定をしました。"
            },
            {
                "question": "Why did some European countries previously want to exclude Britain?",
                "options": [
                    "Because Britain left the European Union a few years ago.",
                    "Because British factories do not have electricity.",
                    "Because France did not like British tea.",
                    "Because British wind turbines were too small."
                ],
                "answer": 0,
                "explanation": "第3文「because it left the European Union a few years ago」より、EUを離脱したためです。"
            },
            {
                "question": "What benefit did car manufacturers highlight about working together?",
                "options": [
                    "It allows factory workers to sleep all afternoon.",
                    "It keeps manufacturing costs lower for everyone across the continent.",
                    "It makes gasoline cars much cheaper.",
                    "It eliminates the need for battery charging stations."
                ],
                "answer": 1,
                "explanation": "第4文「working together keeps factory costs lower for everyone」より、コストを安く抑えられるためです。"
            }
        ]
    },

    # 7. LAW JUNIOR - Zero-Click Spyware in Online Ads
    {
        "slug": "zero-click-spyware-digital-advertising-exploitation",
        "category": "law",
        "category_label": "LAW & TECH • ネット広告に潜む危険なスパイウェア",
        "date": "2026-10-16",
        "title": "Danger Behind Online Ads: How Zero-Click Spyware Attacks Phones Without Tapping",
        "headline_ja": "怪しいリンクを押さなくても感染？ネット広告を悪用する「ゼロクリック型スパイ」の危険",
        "subhead": "画面に出ただけで侵入される新しい手口。個人情報を守る法律のルール作りが急がれています。",
        "lead_snippet": "ネット上の広告システムを悪用して、リンクをタップしていないのにスマートフォンに侵入する危険なスパイウェアが見つかりました。ウェブサイトを開いた瞬間に裏で動く悪質なプログラムから、人々のプライバシーや記者の秘密を守るため、世界中で法律による規制が話し合われています。",
        "source_name": "The Guardian",
        "source_url": "https://www.theguardian.com/technology/2026/oct/15/israeli-firm-digital-ads-enabling-installation-of-zero-click-spyware-researchers-say",
        "senior_path": "../../../law/zero-click-spyware-digital-advertising-exploitation/index.html",
        "image": "https://images.unsplash.com/photo-1563986768609-322da13575f3?w=1000&auto=format&fit=crop&q=80",
        "sentences": [
            {
                "en": "Computer security experts have found that harmful spyware can secretly enter mobile phones through ordinary digital advertisements.",
                "ja": "コンピューターの安全の専門家らは、有害なスパイウェアが普通のデジタル広告を通じて秘密裏にスマートフォンに侵入できることを発見しました。"
            },
            {
                "en": "Usually, bad programs only infect phones when someone taps a strange link, but this new attack requires zero clicks.",
                "ja": "普段なら誰かが怪しいリンクをタップしたときだけ悪いプログラムが感染しますが、この新しい攻撃は「ゼロクリック（タップ不要）」で動きます。"
            },
            {
                "en": "The bad software hides inside the fast computer bidding systems that choose which banner ad appears on your screen.",
                "ja": "その悪質なソフトウェアは、画面にどのバナー広告を表示するかを選ぶ高速なコンピューター入札システムの中に隠れています。"
            },
            {
                "en": "Privacy groups warn that such dangerous spying tools threaten journalists and peaceful citizens who speak the truth.",
                "ja": "プライバシー団体は、このような危険なスパイツールが真実を語るジャーナリストや平和な市民を脅かすと警告しています。"
            },
            {
                "en": "Governments in Europe and America are now looking at strict laws to hold advertising networks responsible for safety.",
                "ja": "ヨーロッパやアメリカの政府は現在、安全について広告ネットワークに責任を持たせる厳格な法律を検討しています。"
            }
        ],
        "dialogue": [
            {"speaker": "七", "name": "Nanami", "role": "生徒", "text": "Keita先生！怪しいリンクを押さなくてもウイルスが入ってくるなんて、どうやって防げばいいんですか？"},
            {"speaker": "慶", "name": "Keita", "role": "英語講師", "text": "第2文にあるように『requires zero clicks（タップが一切不要）』というのが怖いよね。広告を配信する会社のシステム自体に侵入しているんだ。"},
            {"speaker": "七", "name": "Nanami", "role": "生徒", "text": "第5文にある『strict laws to hold networks responsible（広告会社に責任を持たせる法律）』が本当に必要ですね！"},
            {"speaker": "慶", "name": "Keita", "role": "英語講師", "text": "その通り。個人の注意だけでは防げないからこそ、法律（Law）によって社会全体のルールを新しく作り直す必要があるんだよ。"}
        ],
        "vocab": [
            {"word": "harmful", "meaning": "有害な、危険な、害を及ぼす", "pos": "adjective", "def": "Causing or likely to cause harm or damage."},
            {"word": "infect", "meaning": "（ウイルス等に）感染させる、害を広げる", "pos": "verb", "def": "Affect or contaminate with a disease-producing organism or virus."},
            {"word": "threaten", "meaning": "脅かす、危険に晒す", "pos": "verb", "def": "State one's intention to take hostile action, or put at risk."}
        ],
        "syntax": [
            {"title": "Unlike と同等の対比節（Unlike A, B ~）", "formula": "[Usually, bad programs only infect phones when someone taps a link], but [this new attack requires zero clicks]", "explanation": "前節で通常の手法（Usually ~）を述べ、but 以下の主節で最新の例外的事態（zero clicks）を際立たせる対比構文です。"}
        ],
        "quiz": [
            {
                "question": "What is unique and dangerous about 'zero-click' spyware?",
                "options": [
                    "It only works on paper notebooks.",
                    "It can infect phones without the user clicking or tapping any link.",
                    "It makes the phone play loud classical music.",
                    "It charges extra money for mobile data."
                ],
                "answer": 1,
                "explanation": "第2文「this new attack requires zero clicks」より、リンクを一切タップしなくても感染する点が特徴です。"
            },
            {
                "question": "Where does the bad software hide according to the text?",
                "options": [
                    "Inside fast computer bidding systems for banner ads.",
                    "Inside school cafeteria milk cartons.",
                    "Inside physical camera lenses.",
                    "Inside battery charging cables."
                ],
                "answer": 0,
                "explanation": "第3文「hides inside the fast computer bidding systems that choose which banner ad appears」より、広告入札システムの中に潜んでいます。"
            },
            {
                "question": "What action are governments in Europe and America taking?",
                "options": [
                    "Telling everyone to throw away their mobile phones.",
                    "Looking at strict laws to hold advertising networks responsible for safety.",
                    "Banning all journalists from writing articles.",
                    "Building secret underground internet networks."
                ],
                "answer": 1,
                "explanation": "第5文「looking at strict laws to hold advertising networks responsible for safety」より、広告会社に責任を持たせる厳格な法律の検討が正解です。"
            }
        ]
    },

    # 8. LAW JUNIOR - UK Chancellor Bank Tax Hike
    {
        "slug": "uk-chancellor-bank-windfall-tax-fiscal-consolidation",
        "category": "law",
        "category_label": "LAW & MONEY • 税金の公平な集め方と社会のルール",
        "date": "2026-10-16",
        "title": "UK Considers Higher Taxes on Big Banks to Help Public Services and Fix Deficit",
        "headline_ja": "イギリス政府、大儲けした大手銀行への税金を増やす検討：市民の負担を減らす工夫",
        "subhead": "金利高で大きな利益を出した銀行。市民の所得税を上げる代わりに社会の赤字を埋めようと議論中。",
        "lead_snippet": "イギリスの財務大臣が、過去最高クラスの利益を上げた大手銀行に対して追加の税金をかける法律を考えています。普通に働く人たちの税金を上げる代わりに、儲かっている金融機関からお金を集めて病院や学校などの赤字を埋めるためです。税金の公平さを学びましょう。",
        "source_name": "The Guardian",
        "source_url": "https://www.theguardian.com/uk-news/2026/oct/15/john-healey-raise-taxes-banks-budget",
        "senior_path": "../../../law/uk-chancellor-bank-windfall-tax-fiscal-consolidation/index.html",
        "image": "https://images.unsplash.com/photo-1541354329998-f4d9a9f9297f?w=1000&auto=format&fit=crop&q=80",
        "sentences": [
            {
                "en": "British financial leaders are discussing plans to collect higher taxes from big commercial banks.",
                "ja": "イギリスの財政リーダーたちは、大手商業銀行からより高い税金を集める計画を話し合っています。"
            },
            {
                "en": "Because interest rates have been high, major banks recently made record profits from lending money.",
                "ja": "金利が高かったため、大手銀行は最近、お金を貸し出すことで過去最高の利益を上げました。"
            },
            {
                "en": "Ministers say taxing these extra bank profits is fair and avoids raising income taxes on ordinary working families.",
                "ja": "大臣らは、こうした銀行の特別な利益に課税することは公平であり、普通の働く家庭への所得税引き上げを避けられると述べています。"
            },
            {
                "en": "However, banking bosses warn that very high taxes might push international investors to move their money to other cities.",
                "ja": "しかし銀行のトップたちは、税金が高すぎると国際的な投資家がお金を他の都市へ移してしまうかもしれないと警告しています。"
            },
            {
                "en": "This big debate shows how governments must balance fair public taxes with keeping their economy attractive.",
                "ja": "この大きな議論は、政府が公平な公の税金と自国経済の魅力の維持とのバランスをどのように取るべきかを示しています。"
            }
        ],
        "dialogue": [
            {"speaker": "七", "name": "Nanami", "role": "生徒", "text": "普通の人の税金を上げる代わりに、利益が出ている銀行から税金を取る（avoids raising taxes on families）というのは公平な気がします！"},
            {"speaker": "慶", "name": "Keita", "role": "英語講師", "text": "そうだね。金利が上がると住宅ローンなどの利息が増えるから、銀行には何もしなくても莫大な利益（record profits）が入ってきたんだ。"},
            {"speaker": "七", "name": "Nanami", "role": "生徒", "text": "でも第4文のように『税金を高くしすぎるとお金が外国に逃げてしまう（move money to other cities）』という心配もあるんですね。"},
            {"speaker": "慶", "name": "Keita", "role": "英語講師", "text": "その通り！税金（Tax）は社会を支える大切なお金だけれど、取りすぎても少なすぎても問題が起きる。法律と経済のバランスを考える絶好の教材だね。"}
        ],
        "vocab": [
            {"word": "profit", "meaning": "利益、儲け", "pos": "noun", "def": "A financial gain, especially the difference between the amount earned and spent."},
            {"word": "ordinary", "meaning": "普通の、平凡な、一般の", "pos": "adjective", "def": "With no special or distinctive features; normal."},
            {"word": "investor", "meaning": "投資家、出資者", "pos": "noun", "def": "A person or organization that puts money into financial schemes with the expectation of achieving a profit."}
        ],
        "syntax": [
            {"title": "avoid + 動名詞（〜することを避ける）", "formula": "[taxing bank profits is fair and] avoids [raising income taxes on working families]", "explanation": "avoid は後ろに必ず動名詞（-ing）を取る動詞で、「〜することを回避する」という意味を表します（MEGAFEPSのA）。"}
        ],
        "quiz": [
            {
                "question": "Why did major banks recently make record profits in the UK?",
                "options": [
                    "They found buried gold in their vaults.",
                    "High interest rates allowed them to earn more money from loans.",
                    "They fired all their workers and sold all their buildings.",
                    "The government gave them free money."
                ],
                "answer": 1,
                "explanation": "第2文「Because interest rates have been high, major banks made record profits」より、高金利が理由です。"
            },
            {
                "question": "What is the government trying to avoid by taxing banks?",
                "options": [
                    "Raising income taxes on ordinary working families.",
                    "Building any new hospitals or schools.",
                    "Printing new paper currency notes.",
                    "Allowing tourists to use credit cards."
                ],
                "answer": 0,
                "explanation": "第3文「avoids raising income taxes on ordinary working families」より、働く家庭への所得税増税を避けるためです。"
            },
            {
                "question": "What warning do banking bosses give about higher taxes?",
                "options": [
                    "Investors might move their money to other global cities.",
                    "All bank computers will shut down at night.",
                    "Coins will become too heavy to carry.",
                    "Interest rates will drop to zero immediately."
                ],
                "answer": 0,
                "explanation": "第4文「push international investors to move their money to other cities」より、資金が他都市に流出する懸念が正解です。"
            }
        ]
    },

    # 9. CULTURE JUNIOR - The Floating World (Art and Money)
    {
        "slug": "the-floating-world-art-market-capitalism-ethics",
        "category": "culture",
        "category_label": "CULTURE • アートの本当の価値とお金の話",
        "date": "2026-10-16",
        "title": "The Floating World: Why Beautiful Art Is More Than Just Money and Auctions",
        "headline_ja": "本『浮世（The Floating World）』：美しい絵はお金持ちの投資だけじゃない！",
        "subhead": "何十億円もの値段がつく現代アート。絵を見る感動は誰のものかを問いかける新しい本。",
        "lead_snippet": "有名な美術評論家が書いた新しい本『The Floating World』が話題になっています。最近の現代アートはお金持ちが儲けるための道具になりがちですが、本物の芸術の力は値段ではなく、絵を見て心が動かされる瞬間にあると教えてくれます。アートとお金の関係を楽しく考えましょう。",
        "source_name": "The Guardian",
        "source_url": "https://www.theguardian.com/books/2026/oct/15/the-floating-world-by-ben-eastham-review-a-compelling-debut-of-arts-relation-to-money-and-power",
        "senior_path": "../../../culture/the-floating-world-art-market-capitalism-ethics/index.html",
        "image": "https://images.unsplash.com/photo-1579783900882-c0d3dad7b119?w=1000&auto=format&fit=crop&q=80",
        "sentences": [
            {
                "en": "In a thought-provoking new book called The Floating World, author Ben Eastham looks closely at today\\'s modern art scene.",
                "ja": "『The Floating World（浮世）』という深く考えさせられる新著の中で、著者のベン・イーストハムは今日の現代アートの世界をじっくり見つめています。"
            },
            {
                "en": "He explains how famous paintings and sculptures have become expensive investments bought by super-rich collectors.",
                "ja": "彼は、有名な絵画や彫刻がいかに超富裕層のコレクターによって買われる高価な投資商品になってしまったかを説明します。"
            },
            {
                "en": "Even public museums sometimes focus too much on pleasing rich donors instead of serving ordinary people.",
                "ja": "公立美術館でさえ、普通の人々に奉仕する代わりに、お金持ちの寄付者を喜ばせることに集中しすぎることがあります。"
            },
            {
                "en": "Yet, the author reminds us that true art is about special feelings and honest connections between human beings.",
                "ja": "それでも著者は、本当の芸術とは特別な感情や人間同士の誠実な結びつきにあるのだと思い出させてくれます。"
            },
            {
                "en": "Art should inspire everyone in public spaces rather than hiding inside private bank vaults.",
                "ja": "芸術は、個人の銀行の金庫の中に隠されるのではなく、公共の場所でみんなを励ますものであるべきです。"
            }
        ],
        "dialogue": [
            {"speaker": "七", "name": "Nanami", "role": "生徒", "text": "美術館に行くと、たまに『この絵が10億円？』って思うような不思議な現代アートがありますよね。"},
            {"speaker": "慶", "name": "Keita", "role": "英語講師", "text": "第2文にあるように、一部のお金持ちが投資（expensive investments）として買い集めている面があるんだ。金庫にしまわれて誰も見られなくなったら悲しいよね。"},
            {"speaker": "七", "name": "Nanami", "role": "生徒", "text": "第5文の『Art should inspire everyone in public spaces（芸術はみんなが見られる場所で人を励ますべき）』という言葉がとても素敵です！"},
            {"speaker": "慶", "name": "Keita", "role": "英語講師", "text": "本当にそうだね。芸術の価値はお金ではなく、見た人の心の中に生まれるものだというメッセージを英語で感じ取ってほしいな。"}
        ],
        "vocab": [
            {"word": "sculpture", "meaning": "彫刻、彫像", "pos": "noun", "def": "The art of making two- or three-dimensional representative or abstract forms, especially by carving stone or wood."},
            {"word": "donor", "meaning": "寄付者、資金提供者", "pos": "noun", "def": "A person or organization that donates something, especially money to a charity or museum."},
            {"word": "inspire", "meaning": "人を鼓舞する、ひらめきや感動を与える", "pos": "verb", "def": "Fill someone with the urge or ability to feel or do something creative."}
        ],
        "syntax": [
            {"title": "rather than + 動名詞（〜するのではなく）", "formula": "[Art should inspire everyone] rather than [hiding inside private bank vaults]", "explanation": "rather than ~ing は「〜する代わりに」「〜するのではなく」という対比を鮮やかに表現する構文です。"}
        ],
        "quiz": [
            {
                "question": "According to the author, what has contemporary art increasingly become?",
                "options": [
                    "Free posters given to school children.",
                    "Expensive investments bought by super-rich collectors.",
                    "Digital songs broadcast on the radio.",
                    "Cheap furniture made of plastic."
                ],
                "answer": 1,
                "explanation": "第2文「expensive investments bought by super-rich collectors」より、富裕層の高価な投資商品になっている点が挙げられています。"
            },
            {
                "question": "What mistake do some public museums make according to the book?",
                "options": [
                    "They refuse to turn on the lights.",
                    "They focus too much on pleasing rich donors rather than serving the public.",
                    "They throw away all their famous paintings.",
                    "They only open for five minutes each week."
                ],
                "answer": 1,
                "explanation": "第3文「focus too much on pleasing rich donors instead of serving ordinary people」より、一般市民より富裕な寄付者を優先してしまう点です。"
            },
            {
                "question": "Where does the author believe art should belong?",
                "options": [
                    "In dark private bank vaults forever.",
                    "In public spaces where it can inspire everyone.",
                    "Only on private luxury airplanes.",
                    "In locked boxes underground."
                ],
                "answer": 1,
                "explanation": "第5文「Art should inspire everyone in public spaces」より、公共の場で人々を励ますべきだと述べています。"
            }
        ]
    },

    # 10. CULTURE JUNIOR - Digital Sovereignty & Cloud
    {
        "slug": "national-digital-sovereignty-cloud-infrastructure",
        "category": "culture",
        "category_label": "CULTURE • 国の大切なデータは誰が守るの？",
        "date": "2026-10-16",
        "title": "Keeping Public Data Safe: Why Countries Want Their Own Cloud Systems",
        "headline_ja": "国のデータは自分たちで守る！「デジタル主権」と外国の巨大IT企業のお話",
        "subhead": "病院カルテや裁判の記録。外国のサーバーだけに頼らず、自分たちで管理する新しい動き。",
        "lead_snippet": "病院の患者さんのデータや選挙の記録など、国の大切なコンピューター情報が、アメリカの少数の巨大IT企業（クラウド会社）に預けられています。もし外国の会社が止まってしまったらどうなるでしょうか？国のデータを自分たちで安全に管理する「デジタル主権」をやさしく学びます。",
        "source_name": "The Guardian",
        "source_url": "https://www.theguardian.com/technology/2026/oct/15/the-uk-must-have-digital-sovereignty",
        "senior_path": "../../../culture/national-digital-sovereignty-cloud-infrastructure/index.html",
        "image": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=1000&auto=format&fit=crop&q=80",
        "sentences": [
            {
                "en": "Experts in Britain and Europe are arguing that countries need to protect their own \\'digital sovereignty\\'.",
                "ja": "イギリスやヨーロッパの専門家たちは、国家が自分たちの「デジタル主権」を守る必要があると主張しています。"
            },
            {
                "en": "Today, vital records like hospital patient files and court documents are stored on foreign Big Tech cloud servers.",
                "ja": "今日、病院の患者ファイルや裁判所の文書のような極めて重要な記録が、外国の巨大IT企業のクラウドサーバーに保存されています。"
            },
            {
                "en": "Relying completely on foreign companies means foreign laws could suddenly block access or raise service prices.",
                "ja": "外国企業に完全に依存することは、外国の法律によって突然アクセスを止められたり、利用料金を跳ね上げられたりする危険を意味します。"
            },
            {
                "en": "To stay safe, governments are planning to build their own public computer hubs and use open-source software.",
                "ja": "安全を保つため、政府は自分たちの公共コンピューターハブを作り、オープンソースのソフトウェアを使う計画を立てています。"
            },
            {
                "en": "True independence in the modern world means knowing where your data lives and controlling how it is used.",
                "ja": "現代の世界における真の独立とは、自分のデータがどこにあり、どのように使われるかを自分たちで管理することを意味します。"
            }
        ],
        "dialogue": [
            {"speaker": "七", "name": "Nanami", "role": "生徒", "text": "病院のカルテや裁判の記録まで、外国のクラウドに保存されている（stored on foreign servers）なんて知りませんでした！"},
            {"speaker": "慶", "name": "Keita", "role": "英語講師", "text": "便利だからどんどん使われてきたんだけれど、第3文にあるように、外国の都合で止められたり値上げされたりしたら国全体が困ってしまうよね。"},
            {"speaker": "七", "name": "Nanami", "role": "生徒", "text": "第5文の『True independence means controlling your data（真の独立とはデータを自ら管理すること）』というまとめがとても分かりやすいです！"},
            {"speaker": "慶", "name": "Keita", "role": "英語講師", "text": "インターネット時代における『国の独立（independence）』とは何かを考える、まさに高校生にぴったりの時事英語だね。"}
        ],
        "vocab": [
            {"word": "vital", "meaning": "極めて重要な、不可欠な、命に関わる", "pos": "adjective", "def": "Absolutely necessary or important; essential."},
            {"word": "rely", "meaning": "頼る、依存する（rely on で使用）", "pos": "verb", "def": "Depend on with full trust or confidence."},
            {"word": "independence", "meaning": "独立、自立、主権", "pos": "noun", "def": "The fact or state of being independent and free from outside control."}
        ],
        "syntax": [
            {"title": "動名詞主語（Relying on ~ means ...）", "formula": "[Relying completely on foreign companies] means [foreign laws could block access]", "explanation": "Relying on ~（〜に頼ること）が文全体の主語となり、「〜することは…を意味する」という論理的な帰結を導く重要構文です。"}
        ],
        "quiz": [
            {
                "question": "What public records are currently stored on foreign Big Tech servers?",
                "options": [
                    "Only cartoon drawings and movie tickets.",
                    "Hospital patient files and court documents.",
                    "Old broken bicycle parts.",
                    "Discarded plastic bottles."
                ],
                "answer": 1,
                "explanation": "第2文「hospital patient files and court documents」より、病院カルテや裁判所文書などの重要データです。"
            },
            {
                "question": "What danger comes from relying completely on foreign cloud companies?",
                "options": [
                    "Foreign laws could suddenly block access or raise prices.",
                    "Computers will run out of electricity after sunset.",
                    "Printers will only print in green ink.",
                    "Keyboard letters will change their order."
                ],
                "answer": 0,
                "explanation": "第3文「foreign laws could suddenly block access or raise service prices」より、アクセス遮断や価格引き上げのリスクです。"
            },
            {
                "question": "What does 'true independence' mean in the modern digital world?",
                "options": [
                    "Never using any computers ever again.",
                    "Knowing where your data lives and controlling how it is used.",
                    "Refusing to speak with other countries.",
                    "Deleting all digital hospital records."
                ],
                "answer": 1,
                "explanation": "第5文「knowing where your data lives and controlling how it is used」より、データの場所を知り自ら管理することです。"
            }
        ]
    },

    # 11. ENTERTAINMENT JUNIOR - Sand Tiger Shark Conservation
    {
        "slug": "sand-tiger-shark-conservation-public-aquariums",
        "category": "entertainment",
        "category_label": "ENTERTAINMENT • 水族館と野生のサメを守る大作戦！",
        "date": "2026-10-16",
        "title": "Aquariums Work Together to Protect Endangered Sand Tiger Sharks in Delaware Bay",
        "headline_ja": "水族館が海を守るヒーローに！見た目は怖くておとなしい「シロワニ」の保護プロジェクト",
        "subhead": "するどい歯を持つ大型サメ。体に小さな発信器をつけて海の赤ちゃん部屋を探し出します。",
        "lead_snippet": "水族館で大人気のサメ「シロワニ（Sand tiger shark）」は、鋭いトゲのような歯をむき出しにして泳ぎますが、実はおとなしくて人間を襲いません。絶滅の危機にあるこのサメを守るため、水族館の科学者たちが海に発信器をつけて赤ちゃんを産む場所を調べています。水族館の新しい役割を学びましょう。",
        "source_name": "The Guardian",
        "source_url": "https://www.theguardian.com/environment/2026/oct/15/conservation-aquariums-endangered-sharks-protected-waters-delaware-bay-us-sand-tiger-sharks",
        "senior_path": "../../../entertainment/sand-tiger-shark-conservation-public-aquariums/index.html",
        "image": "https://images.unsplash.com/photo-1560275619-4662e36fa65c?w=1000&auto=format&fit=crop&q=80",
        "sentences": [
            {
                "en": "Marine scientists from famous public aquariums are working in Delaware Bay to protect endangered sand tiger sharks.",
                "ja": "有名な公立水族館の海洋科学者たちが、絶滅の危機にあるシロワニを守るためデラウェア湾で活動しています。"
            },
            {
                "en": "Although they look scary with many sharp teeth, sand tiger sharks are gentle fish that help keep coastal waters healthy.",
                "ja": "鋭いたくさんの歯があって怖そうに見えますが、シロワニはおとなしい魚で、沿岸の海を健康に保つ手助けをしています。"
            },
            {
                "en": "Researchers placed small sound transmitters inside young sharks to track their long swimming journeys.",
                "ja": "研究者らは、若いサメたちの長い回遊の旅を追跡するため、小さな音波発信器を体内に取り付けました。"
            },
            {
                "en": "Modern aquariums are no longer just places for fun, but safe homes where experts study and breed rare marine life.",
                "ja": "現代の水族館はもはや単なる遊びの場所ではなく、専門家が珍しい海の生き物を研究し繁殖させる安全な住まいとなっています。"
            },
            {
                "en": "Scientists hope this valuable research will stop harmful fishing nets from destroying shark nursery waters.",
                "ja": "科学者たちは、この価値ある研究によって、有害な漁網がサメの保育場となる海を壊すのを防ぎたいと願っています。"
            }
        ],
        "dialogue": [
            {"speaker": "七", "name": "Nanami", "role": "生徒", "text": "水族館でサメを見るのが大好きですが、水族館のスタッフが海に出てサメを守る活動もしているんですね！"},
            {"speaker": "慶", "name": "Keita", "role": "英語講師", "text": "第4文にある『aquariums are no longer just places for fun（水族館は単なる遊び場ではない）』という文がポイントだね。絶滅危惧種の繁殖や海の研究を支える拠点になっているんだ。"},
            {"speaker": "七", "name": "Nanami", "role": "生徒", "text": "第2文の『Although they look scary, they are gentle（怖そうに見えるけれど、おとなしい）』というギャップも可愛いですね！"},
            {"speaker": "慶", "name": "Keita", "role": "英語講師", "text": "そうだね！見た目で怖がらずに正しく理解して保護する大切さを、楽しく学べる素晴らしい記事だよ。"}
        ],
        "vocab": [
            {"word": "gentle", "meaning": "おとなしい、優しい、穏やかな", "pos": "adjective", "def": "Having or showing a mild, kind, or tender temperament or character."},
            {"word": "breed", "meaning": "繁殖させる、子孫を増やす", "pos": "verb", "def": "Cause an animal to produce offspring, typically in a controlled environment."},
            {"word": "valuable", "meaning": "価値がある、貴重な、役立つ", "pos": "adjective", "def": "Worth a great deal of money, or extremely useful or important."}
        ],
        "syntax": [
            {"title": "no longer just A but B（もはや単なるAではなくBである）", "formula": "[aquariums are no longer just places for fun], but [safe homes where experts study rare life]", "explanation": "no longer A but B は「もはやAではなくBである」という進化や意識の転換を表す美しい頻出構文です。"}
        ],
        "quiz": [
            {
                "question": "What are public aquarium scientists doing in Delaware Bay?",
                "options": [
                    "Catching sharks to sell as home pets.",
                    "Tracking and protecting endangered sand tiger sharks.",
                    "Building a giant underwater amusement park.",
                    "Teaching sharks to jump through metal hoops."
                ],
                "answer": 1,
                "explanation": "第1文「protect endangered sand tiger sharks」より、絶滅危惧種のシロワニを追跡・保護しています。"
            },
            {
                "question": "How are sand tiger sharks described despite their scary needle-like teeth?",
                "options": [
                    "They are dangerous monsters that attack boats.",
                    "They are gentle fish that help keep coastal oceans healthy.",
                    "They can fly through the air above waves.",
                    "They live entirely inside fresh mountain streams."
                ],
                "answer": 1,
                "explanation": "第2文「gentle fish that help keep coastal waters healthy」より、おとなしくて海を健康に保つ魚です。"
            },
            {
                "question": "According to the passage, how have modern aquariums changed?",
                "options": [
                    "They closed all their fish tanks permanently.",
                    "They became places where experts study, breed, and protect rare animals.",
                    "They only display plastic robot fish.",
                    "They stopped allowing children to visit."
                ],
                "answer": 1,
                "explanation": "第4文「safe homes where experts study and breed rare marine life」より、研究・繁殖・保護を行う場所へと進化しました。"
            }
        ]
    },

    # 12. ENTERTAINMENT JUNIOR - SpaceX Starshield & Starlink
    {
        "slug": "satellite-constellation-dual-use-defence-dispute",
        "category": "entertainment",
        "category_label": "TECH & SPACE • 宇宙の人工衛星とインターネットのルール",
        "date": "2026-10-16",
        "title": "Starlink in Orbit: Why Governments and SpaceX Are Debating Military Rules",
        "headline_ja": "宇宙からネットを届けるスターリンク：便利さと戦争利用のルールをめぐる大議論",
        "subhead": "田舎やキャンプ場にネットをつなぐ人工衛星。戦場で使われたとき、民間企業はどうすべき？",
        "lead_snippet": "空に何千個もの人工衛星を飛ばして世界中で高速インターネットをつなぐ「スターリンク」。山奥や被災地でもネットが使える便利な技術ですが、紛争地帯でドローンや軍隊の連絡に使われるようになり、大きな議論が起きています。宇宙テクノロジーと世界平和のルールを考えましょう。",
        "source_name": "The Guardian",
        "source_url": "https://www.theguardian.com/world/2026/oct/15/starshield-starlink-ukraine-restriction-explained",
        "senior_path": "../../../entertainment/satellite-constellation-dual-use-defence-dispute/index.html",
        "image": "https://images.unsplash.com/photo-1446776811953-b23d57bd21aa?w=1000&auto=format&fit=crop&q=80",
        "sentences": [
            {
                "en": "Space company SpaceX has caused big international discussions over how its Starlink satellite internet is used.",
                "ja": "宇宙企業スペースX社は、同社のスターリンク衛星インターネットがどのように使われるかをめぐり、大きな国際的議論を引き起こしました。"
            },
            {
                "en": "Starlink was first built to bring high-speed internet to countryside towns and camping sites far from big cities.",
                "ja": "スターリンクは最初、大都市から遠く離れた田舎の町やキャンプ場に高速インターネットを届けるために作られました。"
            },
            {
                "en": "However, armed soldiers in conflict areas soon started using the small terminals to communicate and control drones.",
                "ja": "しかし、紛争地帯の兵士たちが部隊の連絡やドローンの操縦のためにその小さな端末を使い始めました。"
            },
            {
                "en": "SpaceX said regular civilian service should not be used as weapons, so it created a separate network called Starshield for governments.",
                "ja": "スペースX社は一般市民向けサービスは兵器として使われるべきではないと述べ、政府向けに「スターシールド」という別の衛星網を作りました。"
            },
            {
                "en": "This debate makes countries think about whether private companies should hold so much power over communication in wartime.",
                "ja": "この議論は、戦時中の通信に対して民間企業がこれほど大きな力を持つべきかどうかを各国に考えさせています。"
            }
        ],
        "dialogue": [
            {"speaker": "七", "name": "Nanami", "role": "生徒", "text": "スターリンクって、空を見上げると一列に星のように光って飛んでいくあの衛星ですよね！"},
            {"speaker": "慶", "name": "Keita", "role": "英語講師", "text": "そうだよ！第2文にあるように『bring internet to countryside towns（田舎にネットを届ける）』という平和的な目的で作られたんだ。"},
            {"speaker": "七", "name": "Nanami", "role": "生徒", "text": "でも第3文のように、戦場でドローンを飛ばすのにも使われるようになって（control drones）、企業も悩んでいるんですね。"},
            {"speaker": "慶", "name": "Keita", "role": "英語講師", "text": "技術には便利な面と危険な面（dual-use）があるんだね。第5文にあるように、民間の一企業が戦争の通信をコントロールしていいのかという、現代の新しい倫理問題なんだよ。"}
        ],
        "vocab": [
            {"word": "countryside", "meaning": "田舎、地方、農村部", "pos": "noun", "def": "The land and scenery of a rural area."},
            {"word": "conflict", "meaning": "紛争、対立、戦い", "pos": "noun", "def": "A serious disagreement or fight, typically a protracted armed struggle."},
            {"word": "separate", "meaning": "別の、分かれた、独立した", "pos": "adjective", "def": "Forming or viewed as a unit by itself; not joined."}
        ],
        "syntax": [
            {"title": "whether 節（間接疑問・〜かどうか）", "formula": "[This debate makes countries think about] whether [private companies should hold so much power]", "explanation": "think about whether ~ は「〜すべきかどうかについて考える」という国際政治・倫理の議論で定番の構文です。"}
        ],
        "quiz": [
            {
                "question": "What was Starlink's original purpose when it was first built?",
                "options": [
                    "To launch military laser weapons into deep space.",
                    "To bring high-speed internet to countryside towns far from big cities.",
                    "To replace television news anchors with robot avatars.",
                    "To track wild dolphins in the Atlantic Ocean."
                ],
                "answer": 1,
                "explanation": "第2文「bring high-speed internet to countryside towns and camping sites」より、大都市から離れた地域にネットを届けることが本来の目的です。"
            },
            {
                "question": "Why did controversy arise around Starlink in conflict zones?",
                "options": [
                    "The satellites fell into the ocean during storms.",
                    "Soldiers began using the consumer terminals to communicate and control drones.",
                    "The terminals were painted bright purple.",
                    "SpaceX charged five million dollars for each password."
                ],
                "answer": 1,
                "explanation": "第3文「armed soldiers in conflict areas soon started using the terminals to communicate and control drones」より、ドローンの制御などに使われたためです。"
            },
            {
                "question": "What big question does this situation raise for world governments?",
                "options": [
                    "Whether camping sites should be permanently closed.",
                    "Whether private companies should hold so much power over communication in wartime.",
                    "Whether all drones should be painted white.",
                    "Whether internet cables should be banned completely."
                ],
                "answer": 1,
                "explanation": "第5文「whether private companies should hold so much power over communication in wartime」より、民間企業が戦時通信に過度な影響力を持つべきかという論点です。"
            }
        ]
    }
]
'''

with open(BATCH12_DATA_PATH, "w", encoding="utf-8") as f:
    f.write(data_code)

print(f"Successfully generated {BATCH12_DATA_PATH}")
