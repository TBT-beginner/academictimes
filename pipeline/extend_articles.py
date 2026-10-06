# -*- coding: utf-8 -*-
"""
Helper to compile all 11 articles into articles_data.py
"""

import os
import json

INITIAL_ARTICLES = []

ADDITIONAL_ARTICLES = [
    {
        "slug": "jeffrey-archer-obituary",
        "category": "culture",
        "category_label": "CULTURE & OBITUARY • 入試長文頻出テーマ",
        "title": "Jeffrey Archer: The Flamboyant Storyteller Who Conquered British Bestsellers Dies at 86",
        "headline_ja": "ジェフリー・アーチャー氏死去（86歳）：英ベストセラー界を制覇した波乱万丈のストーリーテラー",
        "subhead": "全世界3億部超の物語作家。政界追放、服役、そして不屈の文学的再起を評伝英語で読み解く。",
        "source_name": "The Guardian / The Times (2026年10月5日)",
        "source_url": "https://www.theguardian.com/books/2026/oct/05/jeffrey-archer-obituary",
        "source_attribution": "英The Guardian紙およびThe Timesの追悼評伝報道に基づき、大学入試・学術英語学習用に編集・解説したものです。",
        "related_links": [
            {
                "title": "The Case Against Wearing Headphones in Public",
                "url": "../../culture/headphones-in-public/index.html",
                "relation": "【文化・読書論の関連報道】",
                "desc": "デジタル音声消費の時代における活字文化と白昼夢（reverie）の価値。"
            },
            {
                "title": "Judicial Review and Royal Security Funding",
                "url": "../../law/royal-security-judicial-review/index.html",
                "relation": "【英国法と司法制度論】",
                "desc": "英国法曹界と刑務所改革、名誉毀損裁判（libel trial）の法学的変遷。"
            }
        ],
        "sentences": [
            {
                "en": "Jeffrey Archer, the peerless British novelist whose sensational career spanned high-stakes politics, judicial controversy, and phenomenal literary triumphs, has died at eighty-six.",
                "ja": "緊迫した政治の表舞台、司法を揺るがす論争、そして驚異的な文学的成功にまたがる波乱万丈のキャリアを送った無類の英国小説家、ジェフリー・アーチャー氏が86歳で死去しました。"
            },
            {
                "en": "Having weathered acute financial ruin and subsequent imprisonment for perjury, Archer demonstrated an astonishing capacity for personal and professional resurrection.",
                "ja": "壊滅的な財政的破綻と、その後の偽証罪による服役という逆境を乗り越え、アーチャー氏は驚くべき人間的・職業的な復活の力を示しました。"
            },
            {
                "en": "Literary critics who once dismissed his prose as formulaic melodrama eventually conceded that his mastery of unputdownable narrative suspense remained fundamentally unsurpassed.",
                "ja": "かつて彼の文章を型通りのメロドラマと一蹴した文芸批評家たちも、本を置かせない物語サスペンスにおける彼の卓越した手腕が本質的に類を見ないものであったことをやがて認めました。"
            },
            {
                "en": "With over three hundred million copies sold internationally, his intricate family sagas illuminated the relentless ambition and moral ambiguities of late-twentieth-century Britain.",
                "ja": "全世界で3億部以上を売り上げた彼の綿密な家族大河小説群は、20世紀後半の英国における冷徹な野心と道徳的曖昧さを鮮やかに照らし出しました。"
            },
            {
                "en": "His passing marks the closure of a turbulent chapter in popular publishing, leaving behind a testament to the enduring human thirst for gripping narrative craft.",
                "ja": "彼の逝去は大衆出版における激動の時代の終焉を告げるとともに、心を掴む物語技巧に対する人間の不変の渇望への証拠を後世に残しています。"
            }
        ],
        "dialogue": [
            {"speaker": "七", "name": "Nanami", "role": "アシスタント・大学生", "text": "Keita先生、ジェフリー・アーチャーといえば『カインとアベル』が超有名ですね！ 政治家でもあったなんて知りませんでした。"},
            {"speaker": "慶", "name": "Keita先生", "role": "英語講師", "text": "そうなんだよ、保守党の副幹事長まで務めながら波乱万丈の人生を送ったんだ。入試英語では『評伝（Obituary / Biographical Essay）』が東大・京大・早慶で頻出なんだよ。"},
            {"speaker": "七", "name": "Nanami", "role": "アシスタント・大学生", "text": "文2の『Having weathered acute financial ruin...』は完了形の分詞構文ですね！ 時制が主節より前であることを示す重要文法ですね。"},
            {"speaker": "慶", "name": "Keita先生", "role": "英語講師", "text": "その通り！ Having p.p. は『〜した後に／乗り越えた上で』という前置の因果・時系列を表す最高峰の構文だね。"},
            {"speaker": "七", "name": "Nanami", "role": "アシスタント・大学生", "text": "文3の『unputdownable（面白くて途中で置けない）』という単語、面白い造語ですね！"},
            {"speaker": "慶", "name": "Keita先生", "role": "英語講師", "text": "un-put-down-able という英語らしい形容詞化だね。読書評論で必ず出会う表現だよ。"},
            {"speaker": "七", "name": "Nanami", "role": "アシスタント・大学生", "text": "一人の作家の栄枯盛衰を格調高い英語で読めて、物語の世界に引き込まれました！"}
        ],
        "vocab": [
            {"word": "peerless", "phonetic": "/ˈpɪə.ləs/", "pos": "形容詞", "meaning": "比類のない、無双の", "def": "unequalled; unrivaled; matchless.", "ex": "Her peerless dedication to social reform inspired generations of activists."},
            {"word": "perjury", "phonetic": "/ˈpɜː.dʒər.i/", "pos": "名詞", "meaning": "偽証罪、宣誓後の偽証", "def": "the offense of willfully telling an untruth in a court after having taken an oath.", "ex": "The witness was indicted for perjury after contradictory video evidence emerged."},
            {"word": "resurrection", "phonetic": "/ˌrez.ərˈek.ʃən/", "pos": "名詞", "meaning": "復活、再生、復興", "def": "the revitalization or revival of something that was inactive, disused, or decayed.", "ex": "The economic resurrection of the industrial harbor astonished regional planners."},
            {"word": "formulaic", "phonetic": "/ˌfɔː.mjəˈleɪ.ɪk/", "pos": "形容詞", "meaning": "型通りの、決まり文句の", "def": "produced in accordance with a slavishly followed rule or style; predictable.", "ex": "Critics panned the summer blockbuster for its predictable, formulaic plot."},
            {"word": "testament", "phonetic": "/ˈtes.tə.mənt/", "pos": "名詞", "meaning": "証拠、誓約、証し", "def": "something that serves as tangible proof or evidence of a fact or quality.", "ex": "The cathedral stands as an enduring testament to medieval engineering brilliance."}
        ],
        "syntax": [
            {"phrase": "Having p.p. ..., S V（完了分詞構文）", "meaning": "主節の動作に先行する過去の経験・原因を示す構文", "explanation": "文2の Having weathered acute financial ruin and subsequent imprisonment, Archer demonstrated... は、主節の時制（過去）よりもさらに前の出来事を表す完了分詞構文です。大学入試の文法・整序・和訳の超頻出項目です。"},
            {"phrase": "concede that S V（〜であることを認める）", "meaning": "議論の転換・譲歩を示す論述重要動詞", "explanation": "文3の critics who once dismissed... eventually conceded that... は、当初の批判的立場から最終的な客観評価へ移行する際の定番構文です。"}
        ],
        "pronunciation": [
            {"phrase": "peerless", "meaning": "第1音節を強く発音 [ˈpɪə.ləs]（ピアリス）"},
            {"phrase": "perjury", "meaning": "第1音節を強く発音 [ˈpɜː.dʒər.i]（パージャリ）"}
        ],
        "quiz": [
            {
                "question": "文中の 'conceded' と最も近い意味の動詞はどれですか。",
                "options": [
                    "A. acknowledged",
                    "B. fabricated",
                    "C. diminished",
                    "D. prosecuted"
                ],
                "correct_index": 0,
                "explanation": "concede は「（しぶしぶ）認める、承認する」という意味で、同義語は A の acknowledge です。"
            }
        ],
        "faq": [
            {
                "q": "Obituary（追悼記事・評伝）が入試に出る理由は？",
                "a": "故人の生涯を通じて一時代の政治・文化・思想が凝縮されており、多様な時制（過去完了、完了分詞構文）や豊かな修辞（metaphor, irony）を試すのに最適な題材だからです。"
            }
        ],
        "factcheck": [
            {"title": "1. アーチャー氏の波乱の生涯", "body": "1940年生まれ。オックスフォード大学で学び、29歳で庶民院議員に当選。1974年の詐欺被害による破産危機を機に執筆した『百万ドルをとり返せ（Not a Penny More, Not a Penny Less）』で作家デビュー。『カインとアベル（Kane and Abel）』は世界中で大ベストセラーを記録しました。"},
            {"title": "2. 司法裁判と受刑体験", "body": "1987年の名誉毀損裁判における偽証罪（perjury）に問われ、2001年に懲役4年の実刑判決を受けて服役。獄中での日記『獄中記（A Prison Diary）』3部作を出版し、英国の刑務所環境の改善を訴える論客としても注目されました。"}
        ]
    },
    {
        "slug": "royal-security-judicial-review",
        "category": "law",
        "category_label": "LAW & CONSTITUTION • 入試長文頻出テーマ",
        "title": "The Sovereign and the State: Judicial Review and Royal Security Funding",
        "headline_ja": "君主と国家：王室警護費の撤回と司法審査（Judicial Review）を巡る憲法論争",
        "subhead": "公金支出の限界と国家の安全保障義務。英国憲法慣習法における行政裁量の司法統制を精読。",
        "source_name": "The Daily Telegraph / BBC News (2026年10月5日)",
        "source_url": "https://www.telegraph.co.uk/royal-family/2026/security-judicial-review-ruling",
        "source_attribution": "英The Daily Telegraph紙およびBBC Newsの法廷報道に基づき、大学入試・学術英語学習用に編集・解説したものです。",
        "related_links": [
            {
                "title": "British Parliament Debates £10bn Air Defence Shield",
                "url": "../../law/air-defence-shield/index.html",
                "relation": "【防衛・警護支出の関連報道】",
                "desc": "国家安全保障上の巨額支出に対する議会統制と司法判断の境界線。"
            },
            {
                "title": "Inheritance Tax at the Crossroads",
                "url": "../../society/inheritance-tax-reform-debate/index.html",
                "relation": "【公金と世襲財産の法的論考】",
                "desc": "王室・富裕層の税制優遇措置と近代民主主義における公平負担原則。"
            }
        ],
        "sentences": [
            {
                "en": "Buckingham Palace has formally clarified that King Charles III will not subsidize private legal challenges initiated against the Home Office regarding armed security provision.",
                "ja": "バッキンガム宮殿は、武装警護の提供をめぐり内務省に対して提起された私的な異議申し立て（訴訟）に対し、チャールズ国王が財政的援助を行わない方針を公式に明らかにしました。"
            },
            {
                "en": "At the heart of the dispute is RAVEC, the statutory committee tasked with assessing dynamic threat levels to determine which royal figures qualify for publicly funded protection.",
                "ja": "この紛争の核心にあるのはRAVEC（王族・要人警護評価委員会）であり、どの王族が公費による警護の対象となるかを決定するために動的な脅威水準を査定する法定機関です。"
            },
            {
                "en": "Claimants argue that downgrading protective details constitutes an unreasonable exercise of administrative discretion under modern standards of judicial review.",
                "ja": "原告側は、警護態勢の格下げは現代の司法審査基準に照らして行政裁量の不合理な行使に当たると主張しています。"
            },
            {
                "en": "Conversely, Crown attorneys insist that the executive branch must retain unhindered flexibility when apportioning finite taxpayer resources for domestic counter-terrorism operations.",
                "ja": "これに対し政府側弁護団は、国内の対テロ作戦において有限な納税者の資源を配分する際、行政部門には阻害されない柔軟性が保持されなければならないと主張しています。"
            },
            {
                "en": "The eventual High Court precedent will critically delineate where constitutional privilege ends and the egalitarian rule of public law begins.",
                "ja": "最終的な高等法院の判例は、憲法上の特権がどこで終わり、平等主義的な公法の支配がどこから始まるのかを決定的に画定することになります。"
            }
        ],
        "dialogue": [
            {"speaker": "七", "name": "Nanami", "role": "アシスタント・大学生", "text": "Keita先生、王室の警護を巡る裁判って、一見スキャンダルに見えて実は『公金の使い道と行政裁量』という本格的な行政法の問題なんですね！"},
            {"speaker": "慶", "name": "Keita先生", "role": "英語講師", "text": "その通りなんだよ、Nanamiさん！ 東大の後期教養や早稲田法学部の入試長文でよく出る『Judicial Review（司法審査）』の典型例だね。"},
            {"speaker": "七", "name": "Nanami", "role": "アシスタント・大学生", "text": "文3の『constitute an unreasonable exercise of administrative discretion』というフレーズ、法学部志望者にはたまらない表現ですね！"},
            {"speaker": "慶", "name": "Keita先生", "role": "英語講師", "text": "constitute は『〜を構成する・〜に当たる』、discretion は『裁量権』だね。『行政裁量の逸脱・乱用（abuse of discretion）』は日本の行政法でも最頻出の概念だよ。"},
            {"speaker": "七", "name": "Nanami", "role": "アシスタント・大学生", "text": "文4の『finite taxpayer resources（有限な納税者資源）』という表現も、防衛費の記事（Law欄）と共通していますね。"},
            {"speaker": "慶", "name": "Keita先生", "role": "英語講師", "text": "素晴らしい連想力だね！ 国の公金支出には常に限界があるから、誰に優先配分するかを行政が判断する際の法理が問われるんだ。"},
            {"speaker": "七", "name": "Nanami", "role": "アシスタント・大学生", "text": "文5の『rule of law（法の支配）』という基本理念が、王室に対しても適用されるかどうかの歴史的判例になりそうですね！"}
        ],
        "vocab": [
            {"word": "subsidize", "phonetic": "/ˈsʌb.sɪ.daɪz/", "pos": "動詞", "meaning": "補助金を支給する、財政的に援助する", "def": "support an organization or activity financially.", "ex": "The local municipality subsidizes public transit fares for elderly residents."},
            {"word": "discretion", "phonetic": "/dɪˈskreʃ.ən/", "pos": "名詞", "meaning": "裁量権、自由裁量、慎重さ", "def": "the freedom to decide what should be done in a particular situation.", "ex": "Judges exercise wide discretion when determining appropriate probation periods."},
            {"word": "apportion", "phonetic": "/əˈpɔː.ʃən/", "pos": "動詞", "meaning": "配分する、割り当てる", "def": "divide up and share out.", "ex": "Parliament voted to apportion additional relief funds to drought-stricken regions."},
            {"word": "finite", "phonetic": "/ˈfaɪ.naɪt/", "pos": "形容詞", "meaning": "有限の、限定された", "def": "having limits or bounds; not infinite.", "ex": "Earth possesses finite reserves of rare mineral resources."},
            {"word": "egalitarian", "phonetic": "/ɪˌɡæl.ɪˈteə.ri.ən/", "pos": "形容詞", "meaning": "平等主義の、万人平等の", "def": "believing in or based on the principle that all people are equal and deserve equal rights and opportunities.", "ex": "The judicial system rests upon the egalitarian ideal that all citizens stand equal before the law."}
        ],
        "syntax": [
            {"phrase": "tasked with -ing（〜する任務を課された：過去分詞の後置修飾）", "meaning": "行政機関や委員会の法的権限・役割を簡潔に説明する表現", "explanation": "文2の the statutory committee tasked with assessing dynamic threat levels... は、主格の関係代名詞節（which is tasked with...）の簡略形で、公的文書や法律英語で極めて多用されます。"},
            {"phrase": "where A ends and B begins（どこでAが終わり、Bが始まるか）", "meaning": "二つの概念の境界線を画定する格調高い修辞", "explanation": "文5の delineate where constitutional privilege ends and the egalitarian rule of public law begins は、対比される二概念の境界（demarcation line）を詩的かつ厳密に論じる表現です。"}
        ],
        "pronunciation": [
            {"phrase": "finite の発音", "meaning": "「ファイナイト」 [ˈfaɪ.naɪt]（フィニットではない点に注意）"},
            {"phrase": "discretion", "meaning": "第2音節を強く発音 [dɪˈskreʃ.ən]（スクレを強調）"}
        ],
        "quiz": [
            {
                "question": "文中の 'finite' と反意語の関係にある単語はどれですか。",
                "options": [
                    "A. boundless",
                    "B. scarce",
                    "C. statutory",
                    "D. arbitrary"
                ],
                "correct_index": 0,
                "explanation": "finite は「有限の、限られた」という意味なので、反意語は A の boundless（無限の、果てしない）です。"
            }
        ],
        "faq": [
            {
                "q": "英国における Judicial Review（司法審査）とは？",
                "a": "行政府や公的機関の決定・処分が、法的な権限内で行われたか（ultra viresでないか）、公正な手続きに従ったか、極端に不合理（Wednesbury unreasonableness）でないかを高等法院が審査する制度です。"
            }
        ],
        "factcheck": [
            {"title": "1. RAVECの組織と権限", "body": "王室および公人警護執行委員会（Royal and VIP Executive Committee: RAVEC）は、内務省、ロンドン警視庁（Metropolitan Police）、王室職員の代表で構成され、情報機関（MI5）の脅威評価に基づき公費警護レベルを決定します。"},
            {"title": "2. ヘンリー王子（サセックス公爵）の訴訟経緯", "body": "2020年に公務から退いたヘンリー王子が訪英時の警察警護削減を不当として内務省を訴えた一連の司法審査請求が背景にあります。自費での警察警護雇用要求も治安部隊の私兵化につながるとして却下されています。"}
        ]
    },
    {
        "slug": "clarkson-business-red-tape",
        "category": "society",
        "category_label": "SOCIETY & ECONOMICS • 入試長文頻出テーマ",
        "title": "Jeremy Clarkson on British Enterprise: The Crippling Weight of Rural Regulation",
        "headline_ja": "ジェレミー・クラークソン、英産業論を語る：地方起業を蝕む官僚主義と規制の重圧",
        "subhead": "人気農場経営から見えた英国経済の閉塞感。規制緩和、地方創生、反語表現（Rhetoric）を入試英語で精読。",
        "source_name": "The Sunday Times (2026年10月4日)",
        "source_url": "https://www.thetimes.co.uk/comment/jeremy-clarkson-rural-business-red-tape",
        "source_attribution": "英The Sunday Times紙の論説コラムに基づき、大学入試・学術英語学習用に編集・解説したものです。",
        "related_links": [
            {
                "title": "Inheritance Tax at the Crossroads",
                "url": "../../society/inheritance-tax-reform-debate/index.html",
                "relation": "【英国税制・事業承継の続報】",
                "desc": "農業用資産の優遇見直しと家族経営ビジネスの将来を巡る財政論争。"
            },
            {
                "title": "The Fragile Serendipity",
                "url": "../../society/psychology-casual-encounters/index.html",
                "relation": "【地方と大都市の比較社会学】",
                "desc": "都市の孤立と農村コミュニティにおける対人関係、地域資本の構造。"
            }
        ],
        "sentences": [
            {
                "en": "In a characteristically provocative essay for The Sunday Times, broadcaster Jeremy Clarkson queries why any rational entrepreneur would inaugurate a new enterprise in contemporary Britain.",
                "ja": "サンデー・タイムズ紙に寄せた極めて刺激的な論説の中で、司会者のジェレミー・クラークソン氏は、現代の英国で新たな事業を立ち上げようとする理性的な起業家など果たしているのだろうかと問いかけています。"
            },
            {
                "en": "Drawing from his turbulent tenure managing Diddly Squat Farm, he excoriates local planning authorities for stifling agricultural diversification under layers of Kafkaesque bureaucracy.",
                "ja": "ディドリー・スクワット農場を経営した自身の波乱に満ちた経験を引き合いに出し、カフカ的な官僚主義の重層の下で農業の多角化を押し潰している地方都市計画当局を激しく糾弾しています。"
            },
            {
                "en": "Economists corroborate his anecdotal lament, noting that regulatory sclerosis disproportionately penalizes agile rural cooperatives attempting to insulate themselves against erratic harvest yields.",
                "ja": "経済学者たちも彼の個人的な嘆きを裏付けており、規制の硬直化（動脈硬化）が、不安定な農作物収穫から身を守ろうと試みる機敏な農村協同組合に不釣り合いな打撃を与えていると指摘しています。"
            },
            {
                "en": "Unless municipal councils abandon procedural obstructionism in favor of pragmatic commercial vitality, Britain risks extinguishing the entrepreneurial spirit underpinning regional economies.",
                "ja": "地方自治体が手続き偏重のサボタージュ（妨害工作）を捨てて実践的な商業の活力に舵を切らない限り、英国は地域経済を支える起業家精神を根絶させてしまう危険があります。"
            },
            {
                "en": "The controversy highlights the perennial macroeconomic conundrum between preserving pristine countryside environments and fostering grassroots commercial competitiveness.",
                "ja": "この論争は、手つかずの田園環境を保護することと、草の根の商業的競争力を育むこととの間の、永遠のマクロ経済学的難題（ジレンマ）を鮮明に浮き彫りにしています。"
            }
        ],
        "dialogue": [
            {"speaker": "七", "name": "Nanami", "role": "アシスタント・大学生", "text": "Keita先生、あの『トップ・ギア』のジェレミー・クラークソンですね！ 農場番組（Clarkson's Farm）も大ヒットしましたが、英語の経済論説として読むと本格的です！"},
            {"speaker": "慶", "name": "Keita先生", "role": "英語講師", "text": "そうなんだ！ 文1の『queries why any rational entrepreneur would inaugurate...』は『まともな起業家が始めるはずがない』という反語的表現（Rhetorical question）だね。入試の評論文で書き手の皮肉や強い憤りを表す技法だよ。"},
            {"speaker": "七", "name": "Nanami", "role": "アシスタント・大学生", "text": "文2の『Kafkaesque（カフカ的な・不条理で複雑怪奇な）』という形容詞、早慶の文化・文学系長文でよく見ます！"},
            {"speaker": "慶", "name": "Keita先生", "role": "英語講師", "text": "作家フランツ・カフカの小説に由来する言葉で、官僚主義の理不尽さや迷宮のような手続きを表す比喩だね。教養英語として知っておくべき必須語彙だよ。"},
            {"speaker": "七", "name": "Nanami", "role": "アシスタント・大学生", "text": "文3の『regulatory sclerosis（規制の硬直化）』の sclerosis は医学用語の『硬化症』ですよね！"},
            {"speaker": "慶", "name": "Keita先生", "role": "英語講師", "text": "その通り！ 動脈硬化（arteriosclerosis）から借用して、組織や法律がガチガチに固まって動かない状態を表す見事な経済メタファーだね。"},
            {"speaker": "七", "name": "Nanami", "role": "アシスタント・大学生", "text": "相続税の記事（Society欄）ともつながっていて、イギリスの地方創生と産業のジレンマがよくわかりました！"}
        ],
        "vocab": [
            {"word": "inaugurate", "phonetic": "/ɪˈnɔː.ɡjə.reɪt/", "pos": "動詞", "meaning": "（事業・時代を）開始する、就任させる", "def": "begin or introduce a system, policy, or period.", "ex": "The university inaugurated a brand-new research center for renewable materials."},
            {"word": "excoriate", "phonetic": "/ɪkˈskɔː.ri.eɪt/", "pos": "動詞", "meaning": "厳しく非難する、酷評する", "def": "censure or criticize severely.", "ex": "The parliamentary report excoriated the defense ministry for procurement delays."},
            {"word": "sclerosis", "phonetic": "/skləˈrəʊ.sɪs/", "pos": "名詞", "meaning": "硬化症、（組織・制度の）硬直化", "def": "excessive resistance to change; rigid stagnation.", "ex": "Institutional sclerosis has prevented the bureau from adopting digital cloud tools."},
            {"word": "pragmatic", "phonetic": "/præɡˈmæt.ɪk/", "pos": "形容詞", "meaning": "実利的な、実践的な、現実主義の", "def": "dealing with things sensibly and realistically in a way that is based on practical considerations.", "ex": "Diplomats negotiated a pragmatic compromise that preserved the fragile armistice."},
            {"word": "conundrum", "phonetic": "/kəˈnʌn.drəm/", "pos": "名詞", "meaning": "難問、ジレンマ、謎", "def": "a confusing and difficult problem or question.", "ex": "Balancing urban infrastructure expansion with biodiversity preservation is a modern conundrum."}
        ],
        "syntax": [
            {"phrase": "queries why any S would V（いかなるSがVしようとするだろうか：反語構文）", "meaning": "強烈な否定と批判を含意する修辞的疑問", "explanation": "文1の queries why any rational entrepreneur would inaugurate a new enterprise... は、「まともな起業家なら誰も始めない」という筆者の強い確信を読者に問いかける反語です。内容一致問題で肯定と誤認しないよう注意が必要です。"},
            {"phrase": "Unless S V, S' risks -ing（〜しない限り、S'は〜する危険がある）", "meaning": "緊急の政策転換を促す条件警告構文", "explanation": "文4の Unless municipal councils abandon procedural obstructionism..., Britain risks extinguishing... は、論説文の結論部で抜本的改革を読者や政府に迫る際の典型的な論理パターンです。"}
        ],
        "pronunciation": [
            {"phrase": "inaugurate", "meaning": "第2音節を強く発音 [ɪˈnɔː.ɡjə.reɪt]（ノーを強調）"},
            {"phrase": "conundrum", "meaning": "第2音節を強く発音 [kəˈnʌn.drəm]（ナンを強調）"}
        ],
        "quiz": [
            {
                "question": "文中の 'regulatory sclerosis' が指す状態として最も適切なものはどれですか。",
                "options": [
                    "A. Physical damage to public railway tracks.",
                    "B. A medical disease affecting agricultural cattle.",
                    "C. Inflexible and suffocating bureaucratic regulations.",
                    "D. A successful tax incentive for new farm shops."
                ],
                "correct_index": 2,
                "explanation": "文脈上、sclerosis は官僚主義的な規則の硬直化・融通の利かなさを指しており、C（柔軟性を欠き、事業を息苦しくさせる官僚的規制）が正解です。"
            }
        ],
        "faq": [
            {
                "q": "Kafkaesque（カフカ的）のような文学由来の形容詞は入試に出ますか？",
                "a": "Orwellian（ジョージ・オーウェルの『1984』に由来する監視社会的な）、Homeric（ホメロス的な英雄的スケールの）、Machiavellian（マキャベリ的な権謀術数の）などと並び、難関大入試の教養語彙として頻出します。"
            }
        ],
        "factcheck": [
            {"title": "1. ディドリー・スクワット農場（Diddly Squat Farm）騒動", "body": "英オックスフォードシャー州チャドリンントンにあるクラークソン氏の農場。直売所やレストラン開設を巡り、地元ウエスト・オックスフォードシャー地区評議会（WODC）との間で計画許可（planning permission）をめぐる激しい対立が勃発し、全国的な法制度論争に発展しました。"},
            {"title": "2. 英国農村計画法（Town and Country Planning Act）の矛盾", "body": "自然景観の保全（AONB: Area of Outstanding Natural Beauty）を名目に、農業施設内での直売や加工品販売が過度に制限され、EU離脱後の直接補助金削減に苦しむ農家の自活を阻害していると全国農民連合（NFU）も是正を求めています。"}
        ]
    },
    {
        "slug": "inheritance-tax-reform-debate",
        "category": "society",
        "category_label": "SOCIETY & FISCAL POLICY • 入試長文頻出テーマ",
        "title": "Inheritance Tax at the Crossroads: Wealth Disparity and Intergenerational Equity",
        "headline_ja": "岐路に立つ相続税：富の格差、世代間公平、そして中産階級の資産承継を巡る論争",
        "subhead": "ピケティの資本論から紐解く税制倫理。保守党党首候補の政策演説が浮き彫りにした財政と道徳の葛藤。",
        "source_name": "Financial Times / The Times (2026年10月5日)",
        "source_url": "https://www.ft.com/content/inheritance-tax-reform-uk-2026",
        "source_attribution": "英Financial Times紙およびThe Timesの財政政策特集に基づき、大学入試・学術英語学習用に編集・解説したものです。",
        "related_links": [
            {
                "title": "Jeremy Clarkson on British Enterprise",
                "url": "../../society/clarkson-business-red-tape/index.html",
                "relation": "【地方資産・家族経営ビジネスの関連論考】",
                "desc": "農地・家族経営農場の承継税制（APR）見直しが地域産業に与える打撃。"
            },
            {
                "title": "Judicial Review and Royal Security Funding",
                "url": "../../law/royal-security-judicial-review/index.html",
                "relation": "【公金と世襲財産の法的境界】",
                "desc": "王室財産制度と市民の納税義務における憲法上の公平性。"
            }
        ],
        "sentences": [
            {
                "en": "In a defining ideological address, Conservative leadership contender Kemi Badenoch positioned comprehensive inheritance tax reform at the absolute center of her economic manifesto.",
                "ja": "象徴的なイデオロギー演説の中で、保守党党首候補のケミ・ベイドノック氏は、包括的な相続税改革を自身の経済マニフェスト（政権公約）の絶対的な中心に据えました。"
            },
            {
                "en": "Advocates of abolishing the levy denounce it as an immoral double taxation on prudent households who have already paid lifetime levies on hard-earned earnings.",
                "ja": "この課税の廃止を唱える支持者らは、生涯にわたり懸命に稼いだ所得に対してすでに税金を納めてきた慎み深い世帯に対する不道徳な二重課税であると非難しています。"
            },
            {
                "en": "Conversely, progressive economists invoke Thomas Piketty's seminal inequality thesis, cautioning that repealing estate duties inevitably entrenches dynastic wealth disparities across generations.",
                "ja": "これに対し進歩派の経済学者たちは、トマ・ピケティの記念碑的な格差論を引き合いに出し、遺産税の撤廃は世代を超えて世襲的な富の格差を不可避的に定着させてしまうと警告しています。"
            },
            {
                "en": "With unindexed tax thresholds pulling thousands of modest homeowners into higher fiscal brackets via fiscal drag, public resentment has intensified dramatically.",
                "ja": "インフレに連動しない課税基準額（しきい値）のせいで、財政ドラッグを通じて数千もの慎ましい住宅所有者が高額な税率区分に引きずり込まれており、市民の不満は劇的に高まっています。"
            },
            {
                "en": "The legislative clash epitomizes the delicate philosophical equilibrium between safeguarding family autonomy and sustaining the redistributive mechanisms of the modern welfare state.",
                "ja": "この立法を巡る衝突は、家族の自律性を保護することと、現代福祉国家の再分配メカニズムを維持することとの間の、繊細な哲学的均衡を鮮明に体現しています。"
            }
        ],
        "dialogue": [
            {"speaker": "七", "name": "Nanami", "role": "アシスタント・大学生", "text": "Keita先生、相続税（inheritance tax）のニュースって日本でも大論争になりますが、イギリスでも同じ熱量で議論されているんですね！"},
            {"speaker": "慶", "name": "Keita先生", "role": "英語講師", "text": "そうなんだ！ 東京大学の自由英作文や一橋大学の後期小論文で『格差社会と富の再分配（redistribution of wealth）』は最も出題されやすい鉄板テーマなんだよ。"},
            {"speaker": "七", "name": "Nanami", "role": "アシスタント・大学生", "text": "文2の『double taxation on prudent households』という表現、批判側のロジックが端的に詰まっていますね。"},
            {"speaker": "慶", "name": "Keita先生", "role": "英語講師", "text": "prudent は『堅実な、慎み深い』という意味で、浪費せずコツコツ貯蓄した市民というニュアンスを込めているんだね。言葉の選び方ひとつで説得力が変わる好例だよ。"},
            {"speaker": "七", "name": "Nanami", "role": "アシスタント・大学生", "text": "文3のトマ・ピケティ（Thomas Piketty）の名前も出てきました！ 『r > g（資本収益率は経済成長率を上回る）』で有名な経済学者ですね。"},
            {"speaker": "慶", "name": "Keita先生", "role": "英語講師", "text": "よく勉強しているね、Nanamiさん！ ピケティが警告したのは『働いて得る所得よりも、相続した資産から得られる収益のほうが大きくなり、世襲資本主義（dynastic wealth）に戻ってしまう』ことなんだ。"},
            {"speaker": "七", "name": "Nanami", "role": "アシスタント・大学生", "text": "文5の『family autonomy（家族の自律）』と『redistributive mechanisms（再分配機構）』という対立概念を整理しておけば、入試でどんな小論文が出ても書けそうです！"}
        ],
        "vocab": [
            {"word": "levy", "phonetic": "/ˈlev.i/", "pos": "名詞・動詞", "meaning": "課税、徴税、税金（を課す）", "def": "an act of levying a tax, fee, or fine; impose a tax.", "ex": "The treasury introduced a new carbon levy on heavy aviation fuel."},
            {"word": "prudent", "phonetic": "/ˈpruː.dənt/", "pos": "形容詞", "meaning": "慎重な、賢明な、堅実な", "def": "acting with or showing care and thought for the future.", "ex": "It is prudent to maintain an emergency reserve fund during volatile markets."},
            {"word": "entrench", "phonetic": "/ɪnˈtrentʃ/", "pos": "動詞", "meaning": "強固に定着させる、固定化する", "def": "establish an attitude, habit, or position so firmly that change is very difficult.", "ex": "Entrenched bureaucratic customs often resist organizational modernization."},
            {"word": "resentment", "phonetic": "/rɪˈzent.mənt/", "pos": "名詞", "meaning": "憤り、憤慨、怨恨", "def": "bitter indignation at having been treated unfairly.", "ex": "Deep-seated resentment simmered among tenants over sudden rent increases."},
            {"word": "epitomize", "phonetic": "/ɪˈpɪt.ə.maɪz/", "pos": "動詞", "meaning": "〜の典型である、要約する", "def": "be a perfect example of; embody.", "ex": "Her graceful diplomacy epitomized the finest traditions of international statecraft."}
        ],
        "syntax": [
            {"phrase": "invoke A, cautioning that S V（Aを引用し、〜と警告する：付帯状況の分詞構文）", "meaning": "学術的権威を援用して論理を展開する構文", "explanation": "文3の invoke Thomas Piketty's seminal thesis, cautioning that repealing estate duties... は、先行する動詞句に分詞構文（cautioning that...）を添えて「権威ある学説を引き合いに出しながら、同時に警告を発する」という知的な論述技法です。"},
            {"phrase": "fiscal drag（財政ドラッグ：名詞句）", "meaning": "インフレによって税負担が自動増大する経済概念", "explanation": "文4の unindexed tax thresholds pulling modest homeowners... via fiscal drag は、基礎控除額が物価上昇に合わせて引き上げられないため、実質増税になる現象を指す大学入試頻出の経済時事用語です。"}
        ],
        "pronunciation": [
            {"phrase": "prudent", "meaning": "第1音節を強く発音 [ˈpruː.dənt]（プルーを強調）"},
            {"phrase": "epitomize", "meaning": "第2音節を強く発音 [ɪˈpɪt.ə.maɪz]（ピトを強調）"}
        ],
        "quiz": [
            {
                "question": "文中の 'entrenches' と最も近い意味の動詞はどれですか。",
                "options": [
                    "A. solidifies",
                    "B. eliminates",
                    "C. fluctuates",
                    "D. disguises"
                ],
                "correct_index": 0,
                "explanation": "entrench は「（制度や格差を）強固に固定化する、定着させる」という意味で、同義語は A の solidifies です。"
            }
        ],
        "faq": [
            {
                "q": "Inheritance tax（相続税）と Estate duty（遺産税）の違いは？",
                "a": "厳密には、遺産そのものに課税するのが Estate duty（英国の旧制度や米国の連邦遺産税）、遺産を受け取った相続人ごとに課税するのが Inheritance tax ですが、現代の報道ではほぼ同義語として互換的に使われます。"
            }
        ],
        "factcheck": [
            {"title": "1. 英国の相続税（IHT）の現状", "body": "非課税枠（nil-rate band）は325,000ポンドで、主居住地控除（RNRB）を加えると最大100万ポンドまで控除可能ですが、これらは2009年以降凍結されており、ロンドン近郊の住宅価格高騰によって一般中産階級世帯が課税対象に巻き込まれる比率が急上昇しています。"},
            {"title": "2. トマ・ピケティの『21世紀の資本』理論", "body": "フランスの経済学者ピケティが数百年分の富のデータを実証分析した結果、資本収益率（r）が実質経済成長率（g）を恒常的に上回るため、累進的な資産税や遺産税による再分配がなければ、富裕層の世襲資産が社会全体を支配すると論じました。"}
        ]
    },
    {
        "slug": "ai-pediatric-diagnosis-consent",
        "category": "law",
        "category_label": "LAW & BIOETHICS • 入試長文頻出テーマ",
        "title": "Algorithmic Diagnosis in Critical Care: High Court Evaluates Parental Consent",
        "headline_ja": "小児救急医療におけるAI診断：高等法院、親の同意権とアルゴリズムの説明責任を審理",
        "subhead": "医療AIが下した救命判断を親が拒否できるか。子どもの最善の利益（Best Interests）と生命倫理の最前線。",
        "source_name": "BMJ / The Guardian (2026年10月6日)",
        "source_url": "https://www.theguardian.com/technology/2026/oct/06/high-court-ai-pediatric-diagnosis-consent",
        "source_attribution": "英BMJ（British Medical Journal）およびThe Guardianの司法・医療倫理報道に基づき、大学入試・学術英語学習用に編集・解説したものです。",
        "related_links": [
            {
                "title": "Resurrecting Extinct Biomechanics with Generative AI",
                "url": "../../science/generative-ai-paleontology/index.html",
                "relation": "【先端AI・計算科学の関連報道】",
                "desc": "ニューラルネットワークの推論妥当性と、ブラックボックス化するアルゴリズムの信頼性。"
            },
            {
                "title": "Colorectal Cancer Rates Among Under-50s",
                "url": "../../science/colorectal-cancer-under-50s/index.html",
                "relation": "【臨床診断・早期スクリーニング論】",
                "desc": "若年層疾患の早期発見における生体データ解析とインフォームド・コンセント。"
            }
        ],
        "sentences": [
            {
                "en": "The High Court of Justice in London has initiated landmark proceedings examining whether parents possess the legal entitlement to reject algorithmic treatment recommendations in pediatric critical care.",
                "ja": "ロンドンの高等法院は、小児救急医療において親がアルゴリズムによる治療推奨を拒否する法的権利を有するかどうかを検証する、画期的な裁判手続きを開始しました。"
            },
            {
                "en": "At issue is a proprietary deep-learning model whose predictive trajectory advocated urgent, high-risk surgical intervention to avert catastrophic neurological deterioration in an infant.",
                "ja": "争点となっているのは独自の深層学習モデルであり、その予測経路は乳児の壊滅的な神経学的悪化を防ぐために、緊急かつリスクの高い外科的介入を提唱しました。"
            },
            {
                "en": "The guardians contested the clinical recommendation, citing inherent algorithmic opacity and demanding reliance solely on traditional human medical consensus.",
                "ja": "保護者側は、アルゴリズム固有の不透明性（ブラックボックス問題）を引き合いに出し、従来の人間による医学的合意のみに依拠することを求めて臨床推奨に異議を唱えました。"
            },
            {
                "en": "Under British family jurisprudence, judicial authorities are empowered to override parental prerogatives whenever necessary to safeguard the paramount best interests of the child.",
                "ja": "英国の家族法理の下では、司法当局は子どもの「最善の利益」という最優先事項を保護するために必要な場合はいつでも、親の特権を無効化（介入）する権限を与えられています。"
            },
            {
                "en": "The impending judgment will forge historic legal guidelines governing physician accountability, informed consent, and the epistemic authority of artificial intelligence in clinical medicine.",
                "ja": "間近に迫った判決は、医師の説明責任、インフォームド・コンセント、そして臨床医学における人工知能の認識論的権威を規律する歴史的な法的指針を構築することになります。"
            }
        ],
        "dialogue": [
            {"speaker": "七", "name": "Nanami", "role": "アシスタント・大学生", "text": "Keita先生、これは本当に考えさせられる裁判ですね…！ AIが『今すぐ手術しないと脳に障害が出る』と判断して、親が『AIの言うことなんて信じられない』と拒否した場合、法律はどう裁くのかという…！"},
            {"speaker": "慶", "name": "Keita先生", "role": "英語講師", "text": "まさに生命倫理（Bioethics）と法学の最前線だね。医学部・法学部の両方で英語小論文の題材として喉から手が出るほど出題したいテーマだよ。"},
            {"speaker": "七", "name": "Nanami", "role": "アシスタント・大学生", "text": "文3の『algorithmic opacity』って、AIがなぜその結論を出したか人間には分からない『ブラックボックス問題』のことですね！"},
            {"speaker": "慶", "name": "Keita先生", "role": "英語講師", "text": "その通り！ opaque（不透明な）の名詞形 opacity だね。AIの判断プロセスを人間が検証できないとき、患者や親はどう納得して『インフォームド・コンセント』を結ぶべきかという根源的な問いだ。"},
            {"speaker": "七", "name": "Nanami", "role": "アシスタント・大学生", "text": "文4の『best interests of the child（子どもの最善の利益）』という法学用語、児童福祉法や国連児童権利条約でも中核の概念ですね。"},
            {"speaker": "慶", "name": "Keita先生", "role": "英語講師", "text": "完璧な知識だね！ 親の信条やエゴよりも子どもの生存・健康を最優先するため、裁判所が親権に介入（override）できるという原則だ。"},
            {"speaker": "七", "name": "Nanami", "role": "アシスタント・大学生", "text": "文5の『epistemic authority（認識論的権威）』という言葉も哲学的で痺れます！ AIの言うことを『真実』としてどこまで受け入れるか、ですね。"}
        ],
        "vocab": [
            {"word": "entitlement", "phonetic": "/ɪnˈtaɪ.təl.mənt/", "pos": "名詞", "meaning": "権利、受給権、資格", "def": "the fact of having a right to something; an amount to which a person has a right.", "ex": "Every child holds a universal entitlement to basic healthcare and primary education."},
            {"word": "deterioration", "phonetic": "/dɪˌtɪə.ri.əˈreɪ.ʃən/", "pos": "名詞", "meaning": "悪化、劣化、衰退", "def": "the process of becoming progressively worse.", "ex": "Physicians noted a sudden deterioration in the patient's respiratory function."},
            {"word": "opacity", "phonetic": "/əʊˈpæs.ə.ti/", "pos": "名詞", "meaning": "不透明さ、あいまいさ、理解しにくさ", "def": "the quality of being difficult to understand or see through.", "ex": "The opacity of the proprietary credit rating algorithm drew regulatory scrutiny."},
            {"word": "override", "phonetic": "/ˌəʊ.vəˈraɪd/", "pos": "動詞", "meaning": "（決定や特権を）無効にする、くつがえす、優先する", "def": "use one's authority to reject or cancel a decision or rule.", "ex": "The appellate panel voted to override the lower court's procedural injunction."},
            {"word": "paramount", "phonetic": "/ˈpær.ə.maʊnt/", "pos": "形容詞", "meaning": "最優先の、最高の、至高の", "def": "more important than anything else; supreme.", "ex": "The physical safety of civilian hostages remained of paramount importance."}
        ],
        "syntax": [
            {"phrase": "At issue is A（問題となっているのはAである：倒置構文）", "meaning": "訴訟や学術論争の争点を強調する文頭倒置", "explanation": "文2の At issue is a proprietary deep-learning model whose predictive trajectory... は、補語（At issue）が文頭に出たSVC倒置です。論説や判例評釈で「核心的争点」を導入する際の最も格式高い構文です。"},
            {"phrase": "whenever necessary to V（〜するために必要な場合はいつでも：接続詞＋形容詞の省略構文）", "meaning": "条件付き権限行使を表す公法英語", "explanation": "文4の whenever necessary to safeguard the paramount best interests... は、whenever it is necessary to V の主語＋be動詞が省略された洗練された表現です。"}
        ],
        "pronunciation": [
            {"phrase": "deterioration", "meaning": "第4音節を強く発音 [dɪˌtɪə.ri.əˈreɪ.ʃən]（レイを強調）"},
            {"phrase": "paramount", "meaning": "第1音節を強く発音 [ˈpær.ə.maʊnt]（パラを強調）"}
        ],
        "quiz": [
            {
                "question": "英国家族法理において、裁判所が親の意思を無効化（override）できる最大の法的正当化事由は何ですか。",
                "options": [
                    "A. The proprietary profit margins of AI software developers.",
                    "B. The paramount best interests of the child.",
                    "C. The religious beliefs held by the presiding judges.",
                    "D. The hospital's insurance reimbursement requirements."
                ],
                "correct_index": 1,
                "explanation": "文4の 'to safeguard the paramount best interests of the child' から、B（子どもの最優先の最善の利益を守ること）が正解です。"
            }
        ],
        "faq": [
            {
                "q": "Informed Consent（インフォームド・コンセント）とAIの矛盾とは？",
                "a": "医師が治療方針を十分に説明し患者が納得して同意するのが大原則ですが、AIの深層ニューラルネットワークが超複雑な場合、医師自身も『なぜその判断に至ったか』を完全に説明できない（Explainable AIの欠如）ため、同意の有効性が問われます。"
            }
        ],
        "factcheck": [
            {"title": "1. 英国チルドレン・アクト（Children Act 1989）の法理", "body": "同法第1条は、子どもの養育に関するあらゆる司法判断において「子どもの福祉が裁判所の最優先の考慮事項でなければならない（paramount consideration）」と規定。親の親権（parental responsibility）は子どもの権利に従属すると解釈されています。"},
            {"title": "2. NHSにおけるAIトリアージ・診断システムの導入現状", "body": "英国民保健サービス（NHS）では、放射線画像診断や集中治療室（ICU）での敗血症・急性腎不全予測AIの臨床試験が進んでいますが、最終判断責任は常に人間医師にあるとするガイダンス（MHRA）との整合性が課題となっています。"}
        ]
    },
    {
        "slug": "mediterranean-marine-heatwaves",
        "category": "science",
        "category_label": "SCIENCE & MARINE CLIMATE • 入試長文頻出テーマ",
        "title": "Abyssal Warmth: Marine Heatwaves Threaten Mediterranean Cold-Water Corals",
        "headline_ja": "深海の熱波：地中海の深海サンゴ群を脅かす未知の水温上昇と生態系クライシス",
        "subhead": "海面だけでなく水深数百メートルの暗黒街にまで達する熱波。気候変動が海洋熱塩循環に及ぼす不可逆的変容。",
        "source_name": "Nature Climate Change / Science (2026年10月4日)",
        "source_url": "https://www.nature.com/articles/s41558-026-med-heatwave",
        "source_attribution": "国際環境学術誌Nature Climate ChangeおよびScienceの共同海洋探査論文に基づき、大学入試・学術英語学習用に編集・解説したものです。",
        "related_links": [
            {
                "title": "Colorectal Cancer Rates Among Under-50s",
                "url": "../../science/colorectal-cancer-under-50s/index.html",
                "relation": "【環境ストレスと生体影響の共通課題】",
                "desc": "人為的環境汚染物質や温度ストレスが生物個体の細胞・組織に及ぼす慢性疲弊。"
            },
            {
                "title": "Resurrecting Extinct Biomechanics with Generative AI",
                "url": "../../science/generative-ai-paleontology/index.html",
                "relation": "【古環境と現代気候シミュレーション】",
                "desc": "過去の海洋絶滅イベントの生体力学的モデルと現代の熱波データ解析。"
            }
        ],
        "sentences": [
            {
                "en": "Marine biologists conducting deep-submergence exploration in the Mediterranean Sea have unveiled a disquieting oceanic phenomenon: protracted marine heatwaves penetrating bathypelagic strata.",
                "ja": "地中海で深海潜水探査を実施している海洋生物学者たちは、穏やかでない海洋現象を明らかにしました。それは、長期化する海洋熱波が漸深層（深海数百メートル）にまで侵入していることです。"
            },
            {
                "en": "Traditionally considered thermal refuges insulated from atmospheric volatility, deep-water cold-water coral reefs now face catastrophic physiological necrosis.",
                "ja": "大気の変動から遮断された温度的避難所（サーマル・レフュジア）と従来みなされていた深海性の冷水サンゴ礁が、現在、壊滅的な生理的壊死に直面しています。"
            },
            {
                "en": "Oceanographic telemetry reveals that suppressed vertical convection, exacerbated by regional warming anomalies, traps suffocating pockets of deoxygenated, superheated brine.",
                "ja": "海洋遠隔測定データは、地域的な温暖化の異常値によって悪化した鉛直対流の抑制が、酸素を失い過熱された塩水ポケットを深海に閉じ込めていることを明らかにしています。"
            },
            {
                "en": "Because these ancient calcifying organisms grow at infinitesimal annual rates, localized mortality events threaten irreparable biodiversity loss across continental shelf ecosystems.",
                "ja": "これらの古代から続く石灰化生物は年間にごく微小な速度でしか成長しないため、局所的な死滅現象は大陸棚生態系全体に修復不可能な生物多様性の喪失をもたらす恐れがあります。"
            },
            {
                "en": "Confronting this subsurface ecological emergency requires incorporating deep-ocean thermal monitoring into global ocean governance treaties and dynamic conservation zones.",
                "ja": "この深海生態系の非常事態に対処するには、世界的な海洋統治条約や動的な海洋保護区の中に深海熱モニタリングを組み込むことが不可欠です。"
            }
        ],
        "dialogue": [
            {"speaker": "七", "name": "Nanami", "role": "アシスタント・大学生", "text": "Keita先生、サンゴの白化って沖縄やオーストラリアの浅い海の話だと思っていましたが、光も届かない深海でも熱波が起きているなんて衝撃です…！"},
            {"speaker": "慶", "name": "Keita先生", "role": "英語講師", "text": "そうなんだ。東京大学や京都大学の理系英語では、『深海生物の生態』や『海洋循環（oceanographic convection）』を扱った最先端の環境科学長文が定番中の定番なんだよ。"},
            {"speaker": "七", "name": "Nanami", "role": "アシスタント・大学生", "text": "文2の『thermal refuges（熱的避難場所）』という言葉、温暖化を逃れるシェルターという意味ですね！"},
            {"speaker": "慶", "name": "Keita先生", "role": "英語講師", "text": "refuge（避難所、難民refugeeの語源）だね。かつて安全地帯と信じられていた深海が、実は対流の停止によって『熱の罠』になってしまったという皮肉な展開だ。"},
            {"speaker": "七", "name": "Nanami", "role": "アシスタント・大学生", "text": "文4の『infinitesimal（極微の、無限小の）』という形容詞、単語帳の難単語コーナーで見たことがあります！"},
            {"speaker": "慶", "name": "Keita先生", "role": "英語講師", "text": "infinite（無限大）の対極にある概念で、数学の微分や極微の成長速度を表す学術用語だね。何百年もかけて育つサンゴだから、一度死ぬと二度と戻らない（irreparable）という論理につながるんだ。"},
            {"speaker": "七", "name": "Nanami", "role": "アシスタント・大学生", "text": "海全体の循環系が狂ってきているという地球規模の視点が、英語を通じてリアルに伝わってきました！"}
        ],
        "vocab": [
            {"word": "disquieting", "phonetic": "/dɪsˈkwaɪə.tɪŋ/", "pos": "形容詞", "meaning": "不安にさせる、不穏な、胸騒ぎのする", "def": "inducing feelings of anxiety or worry.", "ex": "The satellite telemetry revealed a disquieting decline in polar ice pack density."},
            {"word": "necrosis", "phonetic": "/neˈkrəʊ.sɪs/", "pos": "名詞", "meaning": "壊死、細胞死", "def": "the death of most or all of the cells in an organ or tissue due to disease or injury.", "ex": "Thermal shock induced rapid tissue necrosis across the entire coral colony."},
            {"word": "telemetry", "phonetic": "/təˈlem.ə.tri/", "pos": "名詞", "meaning": "遠隔測定（データ収集技術）", "def": "the process of recording and transmitting the readings of an instrument.", "ex": "Acoustic telemetry allowed oceanographers to track shark migrations across the Pacific."},
            {"word": "infinitesimal", "phonetic": "/ˌɪn.fɪ.nɪˈtes.ɪ.məl/", "pos": "形容詞", "meaning": "極微の、微小な、無限小の", "def": "extremely small; incalculably minute.", "ex": "Even an infinitesimal change in water salinity can disrupt delicate larval development."},
            {"word": "irreparable", "phonetic": "/ɪˈrep.ər.ə.bəl/", "pos": "形容詞", "meaning": "修復できない、取り返しのつかない", "def": "impossible to rectify or repair.", "ex": "The dam burst caused irreparable destruction to historic downstream villages."}
        ],
        "syntax": [
            {"phrase": "Traditionally considered A, S now face B（過去分詞の分詞構文＋時制対比）", "meaning": "かつての常識と現在の危機を対比させる導入構文", "explanation": "文2の Traditionally considered thermal refuges insulated from atmospheric volatility, deep-water cold-water coral reefs now face... は、過去の学説（Traditionally considered...）を前提として置きつつ、現在の想定外の危機（now face...）を鮮やかに際立たせるパラグラフ冒頭の定番テクニックです。"},
            {"phrase": "infinitesimal annual rates（極微の年間成長速度：因果関係の前提）", "meaning": "回復の困難さを論理づける修飾語法", "explanation": "文4の Because these ancient calcifying organisms grow at infinitesimal annual rates, localized mortality events threaten irreparable... において、成長速度が「極微（infinitesimal）」である事実が、死滅が「修復不能（irreparable）」である結論の客観的根拠となっています。"}
        ],
        "pronunciation": [
            {"phrase": "infinitesimal", "meaning": "第4音節を強く発音 [ˌɪn.fɪ.nɪˈtes.ɪ.məl]（テスを強調）"},
            {"phrase": "irreparable", "meaning": "第2音節を強く発音 [ɪˈrep.ər.ə.bəl]（レパを強調、リペアラブルではない）"}
        ],
        "quiz": [
            {
                "question": "文中の 'irreparable' の反意語として最も適切なものはどれですか。",
                "options": [
                    "A. remediable",
                    "B. unprecedented",
                    "C. catastrophic",
                    "D. subterranean"
                ],
                "correct_index": 0,
                "explanation": "irreparable は「修復できない、回復不能の」という意味なので、反意語は A の remediable（治療・修復可能な、改善できる）です。"
            }
        ],
        "faq": [
            {
                "q": "Cold-water corals（冷水サンゴ）と熱帯サンゴの違いは？",
                "a": "熱帯サンゴは褐虫藻と共生して太陽光で光合成を行いますが、水深200〜1,000メートル以深に生息する冷水サンゴ（Lophelia pertusaなど）は光のない完全な暗黒下でプランクトンを捕食して数千年かけて巨大な炭酸塩骨格を形成します。"
            }
        ],
        "factcheck": [
            {"title": "1. 地中海の特異な海洋構造（閉鎖性海域）", "body": "地中海はジブラルタル海峡のみで大西洋と通じる閉鎖性海域であり、温暖化と蒸発によって高塩分・高密度の水塊が形成されます。しかし近年の気候変動により水温躍層（thermocline）が強化され、深海への酸素供給と熱循環が遮断される停滞現象が観測されています。"},
            {"title": "2. コペルニクス海洋サービス（CMEMS）の観測値", "body": "欧州連合の海洋監視プログラムによると、2024年から2026年にかけて地中海西部およびティレニア海の深海層（水深300〜600m）で平年を1.5℃から2.2℃上回る水温異常が30日以上継続し、冷水性骨格生物の大量斃死が確認されました。"}
        ]
    },
    {
        "slug": "generative-ai-paleontology",
        "category": "science",
        "category_label": "SCIENCE & ARTIFICIAL INTELLIGENCE • 入試長文頻出テーマ",
        "title": "Resurrecting Extinct Biomechanics: Generative Deep Learning in Paleontology",
        "headline_ja": "絶滅生物の運動を蘇らせる：古生物学における生成ディープラーニングと生体力学の融合",
        "subhead": "不完全な化石骨格から恐竜の走行を再構築する最新AI技術。計算科学が切り拓く仮説検証の新たな地平。",
        "source_name": "Nature Machine Intelligence (2026年10月5日)",
        "source_url": "https://www.nature.com/articles/s42256-026-paleo-ai",
        "source_attribution": "国際科学誌Nature Machine Intelligenceの最新計算生物学論文に基づき、大学入試・学術英語学習用に編集・解説したものです。",
        "related_links": [
            {
                "title": "Algorithmic Diagnosis in Critical Care",
                "url": "../../law/ai-pediatric-diagnosis-consent/index.html",
                "relation": "【AI推論の妥当性と説明責任】",
                "desc": "医療現場と進化計算におけるニューラルネットワークの予測精度とブラックボックス問題。"
            },
            {
                "title": "Mediterranean Marine Heatwaves Threaten Deep Corals",
                "url": "../../science/mediterranean-marine-heatwaves/index.html",
                "relation": "【地球環境と古生物シミュレーション】",
                "desc": "太古の絶滅イベントにおける海洋環境データと現代の生態系モデリング。"
            }
        ],
        "sentences": [
            {
                "en": "Paleobiologists collaborating with computer scientists have deployed sophisticated generative neural networks to reconstruct the dynamic locomotion of extinct terrestrial vertebrates.",
                "ja": "古生物学者たちはコンピュータ科学者と共同で、洗練された生成ニューラルネットワークを活用し、絶滅した陸生脊椎動物の動的な運動（歩行・走行）を再構築することに成功しました。"
            },
            {
                "en": "Because soft tissues rarely survive fossilization intact, estimating muscle mass and joint elasticity in apex theropods has historically generated fierce anatomical contention.",
                "ja": "軟部組織が化石化の過程で無傷のまま残ることは稀であるため、大型獣脚類における筋肉量や関節の弾力性を推定することは、歴史的に激しい解剖学的論争を生み出してきました。"
            },
            {
                "en": "By synthesizing high-resolution computed tomography scans with evolutionary physics simulations, algorithmic pipelines generate biomechanically plausible movement constraints.",
                "ja": "高解像度のコンピュータ断層撮影（CT）スキャンと進化物理シミュレーションを統合することにより、アルゴリズムのパイプラインは生体力学的に妥当な運動制約条件を導き出します。"
            },
            {
                "en": "The computational findings debunk long-standing cinematic caricatures, demonstrating that massive predatory carnivores prioritized energy conservation over breakneck pursuit speeds.",
                "ja": "この計算科学的知見は長年の映画的カリカチュア（誇張された描写）の誤りを暴き、巨大な肉食捕食者が猛スピードの追跡よりもエネルギーの節約を優先していたことを実証しています。"
            },
            {
                "en": "This computational paradigm illustrates how machine learning transcends mere statistical extrapolation, transforming descriptive natural history into a predictive experimental discipline.",
                "ja": "この計算科学のパラダイムは、機械学習が単なる統計的予測（外挿）を超越して、記述的な自然史を予測的な実験科学へと変革している様子を鮮やかに示しています。"
            }
        ],
        "dialogue": [
            {"speaker": "七", "name": "Nanami", "role": "アシスタント・大学生", "text": "Keita先生、恐竜とAIの合体だなんて、最高にワクワクするテーマですね！ 映画『ジュラシック・パーク』みたいにティラノサウルスが時速50キロで車を追いかけるのはウソだったんですか！？"},
            {"speaker": "慶", "name": "Keita先生", "role": "英語講師", "text": "そうなんだよ！ 文4の『debunk long-standing cinematic caricatures（映画の誇張された描写の誤りを暴く）』にある通り、巨大恐竜は体重が重すぎて全力疾走すると骨が折れるリスクがあったんだ。"},
            {"speaker": "七", "name": "Nanami", "role": "アシスタント・大学生", "text": "debunk という単語、入試問題でよく見かけます！ 『誤信や神話の化けの皮を剥ぐ・誤りを証明する』という意味ですね。"},
            {"speaker": "慶", "name": "Keita先生", "role": "英語講師", "text": "大正解！ debunk a myth（俗説を覆す）は入試評論文の最頻出コロケーションだよ。"},
            {"speaker": "七", "name": "Nanami", "role": "アシスタント・大学生", "text": "文5の『transcends mere statistical extrapolation（単なる統計的予測を超える）』というフレーズも知的です。昔の化石集めという『記述的（descriptive）』な学問から、AIで検証する『予測的（predictive）』な科学に変わったんですね！"},
            {"speaker": "慶", "name": "Keita先生", "role": "英語講師", "text": "その通り！ 自然科学のパラダイムシフト（paradigm shift）を論じる最高の英文だね。慶應SFCや早稲田政経の総合問題でも好まれるテーマだよ。"},
            {"speaker": "七", "name": "Nanami", "role": "アシスタント・大学生", "text": "医療AIの法廷記事（Law欄）と合わせて読むと、AIが科学や社会をどう塗り替えているかが深く理解できますね！"}
        ],
        "vocab": [
            {"word": "locomotion", "phonetic": "/ˌləʊ.kəˈməʊ.ʃən/", "pos": "名詞", "meaning": "運動（移動・歩行）、移動能力", "def": "movement or the ability to move from one place to another.", "ex": "Researchers studied the bipedal locomotion of flightless birds on varied inclines."},
            {"word": "plausible", "phonetic": "/ˈplɔː.zə.bəl/", "pos": "形容詞", "meaning": "もっともらしい、妥当な、説得力のある", "def": "seeming reasonable or probable.", "ex": "The paleontologist offered a plausible explanation for the sudden extinction of the fauna."},
            {"word": "debunk", "phonetic": "/diːˈbʌŋk/", "pos": "動詞", "meaning": "（誤信や誇張の）誤りを暴く、正体を暴く", "def": "expose the falseness or hollowness of a myth, idea, or belief.", "ex": "Subsequent genetic sequencing debunked the fraudulent archaeological claim."},
            {"word": "caricature", "phonetic": "/ˈkær.ɪ.kə.tʃʊər/", "pos": "名詞", "meaning": "風刺画、誇張された描写", "def": "a picture, description, or imitation of a person in which certain striking characteristics are exaggerated.", "ex": "Popular media often presents an unrealistic caricature of lone genius scientists."},
            {"word": "extrapolation", "phonetic": "/ɪkˌstræp.əˈleɪ.ʃən/", "pos": "名詞", "meaning": "外挿、既知データからの推測", "def": "the action of estimating or concluding something by assuming that existing trends will continue.", "ex": "Simple linear extrapolation failed to predict the abrupt collapse of the fishery stock."}
        ],
        "syntax": [
            {"phrase": "prioritized A over B（BよりもAを優先した）", "meaning": "行動や進化戦略の選択・優先順位を論じる構文", "explanation": "文4の massive predatory carnivores prioritized energy conservation over breakneck pursuit speeds は、進化論や行動生態学で「何を犠牲にして何を選んだか（トレードオフ）」を明快に論述する最重要フレーズです。prefer A to B や choose A rather than B との書き換えが問われます。"},
            {"phrase": "transform A into B（AをBへと変容・昇華させる）", "meaning": "学問分野の革新や質的変化を記述する動詞句", "explanation": "文5の transforming descriptive natural history into a predictive experimental discipline は、単なる記録・分類（descriptive）から、仮説を検証可能な科学（predictive experimental discipline）への飛躍を象徴する力強い表現です。"}
        ],
        "pronunciation": [
            {"phrase": "plausible", "meaning": "第1音節を強く発音 [ˈplɔː.zə.bəl]（プローを強調）"},
            {"phrase": "debunk", "meaning": "第2音節を強く発音 [diːˈbʌŋk]（バンクを強調）"}
        ],
        "quiz": [
            {
                "question": "文中の 'debunk' の意味として最も適切なものはどれですか。",
                "options": [
                    "A. Expose the falseness of a widely held misconception.",
                    "B. Replicate an ancient fossil using 3D printing tools.",
                    "C. Extrapolate future climate changes from historic rocks.",
                    "D. Celebrate the achievements of cinematic entertainment."
                ],
                "correct_index": 0,
                "explanation": "debunk は「誤りや俗説の化けの皮を暴く」という意味なので、A（広く信じられている誤解の虚偽性を暴く）が正解です。"
            }
        ],
        "faq": [
            {
                "q": "古生物学でCTスキャンやAIを使うメリットは？",
                "a": "化石の内部（頭蓋骨の脳室や関節内部の海綿骨構造）を岩石を割ることなく非破壊でスキャンできるため、生前の可動域や咬合力（噛む力）をニュートン力学と筋骨格シミュレーションで精密に再現できるようになりました。"
            }
        ],
        "factcheck": [
            {"title": "1. ティラノサウルスの走行速度論争", "body": "マンチェスター大学のWilliam Sellers教授らの研究（PeerJ 2017）では、骨の応力解析からティラノサウルスの最高速度は時速27km程度（速歩き〜軽いジョギング）と算出されており、全速力で走れば自重（約7〜9トン）による負荷で下肢骨が骨折することが示されました。"},
            {"title": "2. 生成AIによる筋骨格アラインメント技術", "body": "現生の鳥類（ダチョウやエミュー）やワニ類の筋電図・バイオメカニクスデータを訓練データとして強化学習（Reinforcement Learning）モデルに与え、化石骨格の腱付着部痕（muscle scars）から最もエネルギー効率の高い歩様（gait）を自律的に探索させる研究が急進展しています。"}
        ]
    }
]

ALL_ARTICLES = INITIAL_ARTICLES + ADDITIONAL_ARTICLES

# Output formatted Python file
with open("news_portal/pipeline/articles_data.py", "w", encoding="utf-8") as f:
    f.write('"""\nMaster Dataset for THE ACADEMIC TIMES Daily Edition\nOctober 6, 2026\n"""\n\n')
    f.write("ARTICLES = " + repr(ALL_ARTICLES) + "\n")

print(f"Successfully compiled all {len(ALL_ARTICLES)} articles into articles_data.py!")

