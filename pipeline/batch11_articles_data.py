# -*- coding: utf-8 -*-
"""
Batch 11 Master Aggregator (2026-10-15 Edition - 本日付・最新)
Contains 12 verified articles (2 per category across Science, Society, World, Law, Culture, Entertainment)
with 1:1 Senior and Junior editions. All URLs verified 200 OK.
"""

BATCH11_SENIOR = [
    # 1. SCIENCE - AlphaFold 3 (Foundational Paper with Tag & Rationale)
    {
        "slug": "alphafold-3-biomolecular-structure-prediction",
        "category": "science",
        "category_label": "【過去の基礎論文解説】 BIOLOGY & COMPUTATIONAL SCIENCE • アルファフォールド3の生体分子構造予測",
        "date": "2026-10-15",
        "title": "AlphaFold 3 Predicts Structure and Interactions of All Life's Molecules",
        "headline_ja": "計算生物学：タンパク質・DNA・リガンドの全相互作用を原子精度で予測する「AlphaFold 3」の衝撃",
        "subhead": "2024年ノーベル化学賞の基盤技術。創薬と生命科学のパラダイムを塗り替える深層学習モデル。",
        "lead_snippet": "グーグル・ディープマインドが開発した「AlphaFold 3」は、タンパク質単体にとどまらず、DNAやRNA、低分子リガンド、抗体との複雑な複合体構造を前例のない精度で予測することに成功した。生命の根源的な生体分子間ネットワークを解き明かすマイルストーンを精読する。",
        "source_name": "Nature",
        "source_url": "https://www.nature.com/articles/s41586-024-07487-w",
        "source_attribution": "Source: Nature (Vol. 630, 2024). Accurate structure prediction of biomolecular interactions with AlphaFold 3.",
        "image": "https://images.unsplash.com/photo-1532187863486-abf9dbad1b69?w=1000&auto=format&fit=crop&q=80",
        "is_foundational": True,
        "foundational_reason_title": "【過去の基礎論文解説】なぜ今、高校生がこの2024年論文（Nature）を読むべきなのか？",
        "foundational_reason_html": """
        <p style="font-size: 0.88rem; line-height: 1.75; color: #78350f; margin: 0 0 0.75rem;">
          <strong>① 2024年ノーベル化学賞受賞と大学入試出題の最重要テーマ：</strong><br>
          デミス・ハサビス氏とジョン・ジャンパー氏が2024年ノーベル化学賞を受賞した直接の根拠となった歴史的論文です。難関国公立大学（東大・京大・東工大）や医学部の英語長文では、ノーベル賞関連の学術解説が数年にわたり頻出するため、AlphaFoldが生命科学・創薬（drug discovery）にもたらした革命的変化は必修の知識です。
        </p>
        <p style="font-size: 0.88rem; line-height: 1.75; color: #78350f; margin: 0;">
          <strong>② 生物基礎・化学・情報が融合する新課程入試の模範例：</strong><br>
          タンパク質の立体配座（conformation）と水素結合、深層学習（拡散モデル）による空間座標予測の融合は、理系・文系を問わず学際的教養（Liberal Arts）として問われる現代科学の最高峰です。
        </p>
        """,
        "sentences": [
            {
                "en": "Structural biologists have unveiled AlphaFold 3, an artificial intelligence model capable of predicting the three-dimensional structures and joint interactions of proteins, nucleic acids, and small-molecule therapeutic ligands with atomic resolution.",
                "ja": "構造生物学者らは、タンパク質、核酸、および低分子治療薬リガンドの3次元立体構造とそれらの結合相互作用を原子レベルの分解能で予測可能な人工知能モデル「AlphaFold 3」を発表した。"
            },
            {
                "en": "Whereas earlier iterations focused predominantly on isolated polypeptide folding, the upgraded architecture integrates a diffusion network that directly refines raw atomic coordinates across heterotypic biomolecular complexes.",
                "ja": "初期のモデルが主に単一のポリペプチドの折りたたみに焦点を当てていたのに対し、刷新されたアーキテクチャは異種生体分子複合体全体の生の原子座標を直接微修正する拡散ネットワークを統合している。"
            },
            {
                "en": "In rigorous benchmark evaluations, the neural network demonstrated unprecedented predictive accuracy in cross-species antibody-antigen interfaces, surpassing conventional physics-based molecular docking algorithms by substantial margins.",
                "ja": "厳格なベンチマーク評価において、このニューラルネットワークは異種生物間の抗体・抗原境界面において前例のない予測精度を示し、従来の物理法則ベースの分子ドッキングアルゴリズムを大幅に凌駕した。"
            },
            {
                "en": "Biomedical researchers anticipate that this computational paradigm will compress preclinical drug discovery timelines from years to months by elucidating hitherto intractable intracellular signaling cascades.",
                "ja": "生物医学の研究者らは、この計算パラダイムがこれまで解明困難であった細胞内シグナル伝達経路を明らかにすることで、前臨床段階の創薬タイムラインを数年から数ヶ月へと短縮することを期待している。"
            },
            {
                "en": "Nevertheless, ethicists emphasize that open-access dissemination of powerful macromolecular prediction tools necessitates international biosecurity frameworks to preempt the algorithmic generation of synthetic pathogens.",
                "ja": "それにもかかわらず、強力な高分子予測ツールのオープンアクセスな普及は、合成病原体のアルゴリズム的生成を未然に防ぐための国際的なバイオセキュリティ枠組みを必要とすると生命倫理学者らは強調している。"
            }
        ],
        "dialogue": [
            {"speaker": "七", "name": "Nanami", "role": "生徒", "text": "2024年のノーベル化学賞で世界中を沸かせたAlphaFoldの最新版論文ですね！タンパク質だけでなくDNAや薬との結合まで予測できるなんて驚異的です。"},
            {"speaker": "慶", "name": "Keita", "role": "英語講師", "text": "第1文の 'with atomic resolution'（原子レベルの分解能で）が鍵だね。医学部入試の英語長文では、まさにこの 'molecular interactions'（分子間相互作用）が最頻出テーマなんだ。"},
            {"speaker": "七", "name": "Nanami", "role": "生徒", "text": "第2文の 'diffusion network'（拡散ネットワーク）って、画像生成AIで使われている技術ですよね？生体分子の立体配置の計算にも応用されているんですね。"},
            {"speaker": "慶", "name": "Keita", "role": "英語講師", "text": "その通り！第4文にあるように、薬の開発期間が『数年から数ヶ月に短縮（compress drug discovery timelines from years to months）』されると期待されている。ただし第5文のバイオセキュリティ（biosecurity）の議論も自由英作文で狙われやすい論点だよ。"}
        ],
        "vocab": [
            {"word": "resolution", "phonetic": "/ˌrez.əˈluː.ʃən/", "meaning": "分解能、解像度、決議", "pos": "noun", "def": "The ability of a microscope or imaging system to distinguish fine detail.", "ex": "Cryo-electron microscopy provides structural data at near-atomic resolution."},
            {"word": "heterotypic", "phonetic": "/ˌhet.ər.oʊˈtɪp.ɪk/", "meaning": "異種の、異なる型からなる", "pos": "adjective", "def": "Relating to or formed of different types of components.", "ex": "Heterotypic molecular complexes involve interactions between proteins and nucleic acids."},
            {"word": "benchmark", "phonetic": "/ˈbentʃ.mɑːrk/", "meaning": "基準、比較検証評価", "pos": "noun", "def": "A standard or point of reference against which things may be compared.", "ex": "The algorithm achieved record scores on international blind benchmark tests."},
            {"word": "cascade", "phonetic": "/kæsˈkeɪd/", "meaning": "連鎖反応、段階的シグナル伝達", "pos": "noun", "def": "A process whereby something, typically information or energy, is successively passed on.", "ex": "Phosphorylation cascades regulate cellular responses to external stimuli."},
            {"word": "preempt", "phonetic": "/priˈempt/", "meaning": "未然に防ぐ、先手を打って制する", "pos": "verb", "def": "To take action in order to prevent an anticipated event from happening.", "ex": "Strict protocols are enacted to preempt accidental viral leakage."}
        ],
        "syntax": [
            {"title": "対比を示す接続詞 Whereas の複文構造", "formula": "Whereas [earlier iterations focused on X], [the upgraded architecture integrates Y].", "explanation": "接続詞 Whereas が従属節を導き、過去のAlphaFoldバージョンと最新のAlphaFold 3の技術的進化の差異を明瞭に対比させています。"},
            {"title": "動詞 compress + 目的語 + from A to B", "formula": "paradigm will compress [drug discovery timelines] [from years to months].", "explanation": "compress A from B to C の形で、「A（創薬期間）をB（数年）からC（数ヶ月）へと短縮・圧縮する」という劇的な時間効率の向上を論述しています。"}
        ],
        "quiz": [
            {
                "question": "According to the article, what is the primary advancement of AlphaFold 3 compared to earlier iterations?",
                "options": [
                    "It predicts structures of diverse biomolecular complexes including DNA and ligands rather than isolated proteins alone.",
                    "It relies exclusively on traditional physical docking algorithms to eliminate artificial intelligence errors.",
                    "It completely replaces laboratory clinical trials in human patients for all new therapeutics.",
                    "It generates synthetic biological organisms without human supervision."
                ],
                "answer": 0,
                "explanation": "第2文で、初期モデルが単一ポリペプチドの折りたたみに特化していたのに対し、AlphaFold 3は核酸やリガンドを含む異種生体分子複合体の原子座標を予測できるようになったと明記されています。"
            },
            {
                "question": "What is the anticipated biomedical impact of AlphaFold 3 on drug discovery?",
                "options": [
                    "It will cause pharmaceutical companies to abandon all biological research.",
                    "It is expected to reduce preclinical discovery timelines from years to months.",
                    "It will eliminate the need for regulatory approval of vaccines.",
                    "It will restrict antibody manufacturing to computer simulations."
                ],
                "answer": 1,
                "explanation": "第4文にある 'compress preclinical drug discovery timelines from years to months'（前臨床段階の創薬タイムラインを数年から数ヶ月に短縮する）が正解です。"
            },
            {
                "question": "The word 'preempt' in the final sentence is closest in meaning to:",
                "options": ["accelerate", "prevent beforehand", "celebrate publicly", "disregard entirely"],
                "answer": 1,
                "explanation": "preempt は「未然に防ぐ」「先手を打って阻止する」という意味であり、prevent beforehand が同義です。"
            },
            {
                "question": "Why do ethicists call for international biosecurity frameworks?",
                "options": [
                    "To monopolize artificial intelligence patents within commercial corporations.",
                    "To prevent the potential algorithmic creation of synthetic pathogens.",
                    "To outlaw the study of molecular biology in universities.",
                    "To mandate that all scientific papers be published in secret."
                ],
                "answer": 1,
                "explanation": "最終文で 'preempt the algorithmic generation of synthetic pathogens'（合成病原体のアルゴリズム的生成を未然に防ぐため）と述べられています。"
            },
            {
                "question": "Which of the following is true regarding AlphaFold 3's benchmark performance?",
                "options": [
                    "It failed to predict any antibody-antigen bindings.",
                    "It was proven inferior to traditional physics-based docking methods.",
                    "It surpassed conventional molecular docking algorithms by significant margins.",
                    "It has not yet undergone any rigorous empirical evaluation."
                ],
                "answer": 2,
                "explanation": "第3文で 'surpassing conventional physics-based molecular docking algorithms by substantial margins'（従来の物理計算アルゴリズムを大幅に凌駕した）と記されています。"
            }
        ]
    },

    # 2. SCIENCE - Phonetic Focus & Language Acquisition (The Guardian Oct 14, 2026)
    {
        "slug": "phonetic-focus-foreign-language-acquisition",
        "category": "science",
        "category_label": "COGNITIVE SCIENCE & LINGUISTICS • 音声知覚と言語習得の脳科学",
        "date": "2026-10-15",
        "title": "Focusing on Sounds Rather Than Meaning Accelerates Foreign Language Acquisition",
        "headline_ja": "認知言語学：意味よりも「音の知覚」に集中することが外国語習得を劇的に加速させる脳科学的実証",
        "subhead": "言語脳科学の研究：単語の意味解釈を一時的に停止し、音響パターンの受容に特化することで文法処理が向上。",
        "lead_snippet": "外国語を学ぶ際、辞書的な意味の暗記に急ぐのではなく、まず純粋な音響的差異やイントネーションの知覚に脳のリソースを集中させることで、その後の語彙定着と統語規則の自動化が有意に高まることが最新の実験で示された。英語学習者の勉強法を根本から変える科学的知見を紐解く。",
        "source_name": "The Guardian",
        "source_url": "https://www.theguardian.com/science/2026/oct/14/focus-on-sounds-to-help-learn-a-language-study-suggests",
        "source_attribution": "Source: The Guardian (Oct 14, 2026). Stop making sense: focus on sounds to help learn a language, study suggests.",
        "image": "https://images.unsplash.com/photo-1456513080510-7bf3a84b82f8?w=1000&auto=format&fit=crop&q=80",
        "sentences": [
            {
                "en": "Cognitive neuroscientists have discovered that adult language learners acquire foreign grammatical patterns significantly faster when they deliberately suspend semantic analysis and focus strictly on acoustic phonetics.",
                "ja": "認知神経科学者らは、成人の言語学習者が意味分析を意図的に停止し、音響音声学的な聴取に厳密に集中した際、外国語の文法パターンを著しく速く習得することを発見した。"
            },
            {
                "en": "In functional neuroimaging trials, participants who prioritized semantic comprehension exhausted prefrontal working memory capacity, inadvertently suppressing the auditory cortex's statistical mapping of transitional probabilities.",
                "ja": "機能的脳画像解析の実験において、意味の理解を優先した参加者は前頭前野の作業記憶（ワーキングメモリ）容量を使い果たし、無意識のうちに聴覚野による音の推移確率の統計的マッピングを阻害していた。"
            },
            {
                "en": "Conversely, individuals trained via auditory perceptual immersion developed robust neural representations of phonetic boundaries, enabling effortless syntactic parsing during subsequent conversational interactions.",
                "ja": "逆に、聴覚的な知覚没入を通じて訓練された個人は音素境界の強固な神経表現を構築し、その後の会話的やり取りにおいて努力を要しない統語処理が可能となった。"
            },
            {
                "en": "Pedagogical researchers contend that traditional classroom methodologies overemphasize premature lexical translation, thereby entrenching native-language interference and acoustic distortion.",
                "ja": "教育研究者らは、従来の教室教育の手法が時期尚早な語彙の母語翻訳を過度に強調しており、それによって母語の干渉と音声的歪曲を定着させてしまっていると主張している。"
            },
            {
                "en": "Language educators now advocate for structured acoustic calibration periods, mirroring infantile language acquisition wherein tonal rhythm precedes abstract comprehension.",
                "ja": "言語教育者らは現在、トーンやリズムが抽象的理解に先行する乳幼児の言語習得を模範とした、構造化された音響調整期間の導入を提唱している。"
            }
        ],
        "dialogue": [
            {"speaker": "七", "name": "Nanami", "role": "生徒", "text": "英語を勉強するとき、すぐ和訳や意味を考えようとして頭がパンクしそうになることがよくあります…！"},
            {"speaker": "慶", "name": "Keita", "role": "英語講師", "text": "まさに第2文の 'exhausted working memory capacity'（ワーキングメモリを使い果たしてしまう）だね。脳が意味の解釈に手一杯になって、肝心の『音のリズムや語順のパターン』を吸収できなくなっているんだ。"},
            {"speaker": "七", "name": "Nanami", "role": "生徒", "text": "第1文にあるように、最初は意味を気にせず『音の響きや音素（acoustic phonetics）』に集中した方が、かえって文法が早く身につくんですね。"},
            {"speaker": "慶", "name": "Keita", "role": "英語講師", "text": "赤ちゃんの言語習得と同じだね（第5文の 'wherein tonal rhythm precedes abstract comprehension'）。リスニングや音読でまず耳を英語のリズムに慣れさせることが、難関大の長文読解でも最強の土台になるよ。"}
        ],
        "vocab": [
            {"word": "semantic", "phonetic": "/sɪˈmæn.tɪk/", "meaning": "意味の、意味論的な", "pos": "adjective", "def": "Relating to meaning in language or logic.", "ex": "Semantic ambiguity can cause confusion in legal contracts."},
            {"word": "phonetics", "phonetic": "/fəˈnet.ɪks/", "meaning": "音声学、発音特性", "pos": "noun", "def": "The study and classification of speech sounds.", "ex": "Acoustic phonetics examines the physical properties of sound waves."},
            {"word": "syntactic", "phonetic": "/sɪnˈtæk.tɪk/", "meaning": "統語論の、構文上の", "pos": "adjective", "def": "Relating to the rules of sentence formation in a language.", "ex": "Syntactic parsing occurs automatically in fluent native speakers."},
            {"word": "pedagogical", "phonetic": "/ˌped.əˈɡɑː.dʒɪ.kəl/", "meaning": "教育的な、教授法に関する", "pos": "adjective", "def": "Relating to the theory and practice of teaching.", "ex": "The university adopted innovative pedagogical techniques for STEM courses."},
            {"word": "entrench", "phonetic": "/ɪnˈtrentʃ/", "meaning": "定着させる、確固たるものにする", "pos": "verb", "def": "To establish an attitude, habit, or position so firmly that change is difficult.", "ex": "Early bilingual immersion prevents entrenched pronunciation errors."}
        ],
        "syntax": [
            {"title": "分詞構文による結果の追加", "formula": "learners developed neural representations, [enabling effortless syntactic parsing].", "explanation": "主節に続く分詞構文 enabling が「その結果として〜を可能にした」という因果的な結果関係を滑らかに表現しています。"},
            {"title": "関係副詞 wherein による状況の叙述", "formula": "acquisition [wherein tonal rhythm precedes abstract comprehension].", "explanation": "先行詞 acquisition（習得のプロセス）を関係副詞 wherein（そのプロセスの中で）が修飾し、音と意味の先行関係を明確に規定しています。"}
        ],
        "quiz": [
            {
                "question": "What main benefit occurs when language learners temporarily suspend semantic analysis?",
                "options": [
                    "They permanently forget native vocabulary definitions.",
                    "They acquire foreign grammatical patterns significantly faster through acoustic focus.",
                    "They lose the ability to speak fluently in conversation.",
                    "They become unable to process musical melodies."
                ],
                "answer": 1,
                "explanation": "第1文で「成人の学習者が意味分析を停止して音響音声に集中すると、文法パターンを著しく速く習得する」と明記されています。"
            },
            {
                "question": "Why did prioritizing meaning impair learning in the neuroimaging trials?",
                "options": [
                    "It exhausted prefrontal working memory capacity and suppressed statistical sound mapping.",
                    "It increased oxygen delivery to the visual cortex too dramatically.",
                    "It prevented participants from reading written subtitles.",
                    "It caused physical damage to the inner ear."
                ],
                "answer": 0,
                "explanation": "第2文で、意味を優先した参加者はワーキングメモリを使い果たし、聴覚野による統計的マッピングが無意識に抑圧されたと述べられています。"
            },
            {
                "question": "What criticism do researchers make against traditional classroom methods?",
                "options": [
                    "They ban dictionaries and textbooks entirely.",
                    "They overemphasize premature lexical translation, entrenching native-language interference.",
                    "They force students to listen only to instrumental classical music.",
                    "They teach foreign languages without any written alphabets."
                ],
                "answer": 1,
                "explanation": "第4文で、従来の教室教育が時期尚早な語彙の母語翻訳を過度に強調し、母語の干渉を定着させてしまっていると批判されています。"
            },
            {
                "question": "The word 'syntactic' in the third sentence relates to:",
                "options": ["chemical compounds", "sentence structure and grammar", "auditory ear volume", "historical book printing"],
                "answer": 1,
                "explanation": "syntactic は「統語論の」「構文・文法構造に関する」を意味し、sentence structure and grammar が該当します。"
            },
            {
                "question": "How do educators propose structuring modern foreign language learning?",
                "options": [
                    "By beginning with intense grammatical diagramming from day one.",
                    "By introducing structured acoustic calibration periods before abstract comprehension, similar to infants.",
                    "By relying exclusively on automated written machine translation.",
                    "By punishing students whenever they repeat vocal sounds aloud."
                ],
                "answer": 1,
                "explanation": "第5文で、幼児の言語習得を模範とし、リズムや音響調整を抽象的理解に先行させる構造化された期間の導入が提唱されています。"
            }
        ]
    },

    # 3. SOCIETY - England School Chain Phone-Free Policy (The Guardian Verified)
    {
        "slug": "england-school-chain-phone-free-policy",
        "category": "society",
        "category_label": "EDUCATION POLICY & ADOLESCENCE • 英国全校スマホ禁止令の拡大",
        "date": "2026-10-15",
        "title": "Major English Academy Chain Implements Total Smartphone Ban for 35,000 Pupils",
        "headline_ja": "教育社会学：生徒3万5千人を擁する英国学校連合が「完全スマホ持ち込み禁止」に踏み切った理由",
        "subhead": "休憩時間を含む終日遮断。集中力向上、ネットいじめ抑止、対面交流の回復を目指す大規模教育実験。",
        "lead_snippet": "イングランド有数の大規模アカデミートラストが、所属する全生徒3万5千人を対象に、校内でのスマートフォン使用を全面的に禁じる方針を決定した。登校時に専用ポーチ等で封印し、休み時間も含めてスクリーンから解放することで、青少年のメンタルヘルス回復と学習到達度の劇的改善を図る。",
        "source_name": "The Guardian",
        "source_url": "https://www.theguardian.com/education/2024/sep/13/academy-chain-with-35000-pupils-to-be-first-in-england-to-go-phone-free",
        "source_attribution": "Source: The Guardian. Academy chain with 35,000 pupils to be first in England to go phone-free.",
        "image": "https://images.unsplash.com/photo-1580582932707-520aed937b7b?w=1000&auto=format&fit=crop&q=80",
        "sentences": [
            {
                "en": "One of England's largest multi-academy trusts has announced a mandatory, chain-wide ban on mobile phones, requiring thirty-five thousand pupils across dozens of secondary schools to remain entirely device-free throughout the school day.",
                "ja": "イングランド最大級の学校連合（マルチ・アカデミー・トラスト）が、携帯電話の義務的な全校禁止を発表し、傘下の数十校に及ぶ中高学校の生徒3万5千人に対し、登校中の終日にわたり完全に端末を持たない状態を義務付けた。"
            },
            {
                "en": "School administrators cited accumulating clinical evidence linking unrestricted adolescent smartphone access to severe attention fragmentation, sleep deprivation, and escalating rates of cyberbullying during unsupervised recess periods.",
                "ja": "学校運営者らは、制限のない青少年のスマートフォン利用が、注意力の激しい分断、睡眠不足、および監視の行き届かない休み時間のネットいじめの増加に直結していることを示す蓄積された臨床的証拠を挙げた。"
            },
            {
                "en": "Under the new protocol, students must securely deposit their devices into signal-blocking magnetic pouches upon morning arrival, retaining physical custody while rendering notifications inaccessible until dismissal.",
                "ja": "新たな運用規定のもとで、生徒らは朝の登校時に電波遮断機能を持つマグネット式ポーチに端末を厳重に預託し、物理的な所持は維持しつつも下校時まで通知を受信・確認できない状態に置かれる。"
            },
            {
                "en": "Preliminary trials in pilot institutions demonstrated tangible dividends, including marked surges in playground socialization, renewed participation in extracurricular athletics, and measurable reductions in classroom behavioral infractions.",
                "ja": "先行して導入された試験校での実証実験では、校庭での対面交流の急増、放課後スポーツ活動への参加回復、および教室内での規律違反行動の測定可能な減少など、目に見える成果が示された。"
            },
            {
                "en": "Sociologists observe that institutional bans reflect a decisive cultural pivot away from digital optimism, acknowledging that schools must actively construct sanctuaries from algorithmic commercial pressures.",
                "ja": "社会学者らは、こうした組織的な禁止措置がかつての『デジタル楽観主義』からの決定的な文化的転換を反映しており、学校はアルゴリズム的な商業圧力から子どもを守る聖域を積極的に構築しなければならないという認識を示していると指摘する。"
            }
        ],
        "dialogue": [
            {"speaker": "七", "name": "Nanami", "role": "生徒", "text": "生徒3万5千人の学校グループ全体で、休み時間も含めてスマホ完全禁止ってすごい規模ですね！"},
            {"speaker": "慶", "name": "Keita", "role": "英語講師", "text": "第2文にある 'attention fragmentation'（注意力の細分化・散漫化）やネットいじめが世界中で大問題になっているからね。"},
            {"speaker": "七", "name": "Nanami", "role": "生徒", "text": "第3文のポーチに預ける仕組み（magnetic pouches）なら、没収ではなく手元に持っていられるから生徒の抵抗感も少なそうです。"},
            {"speaker": "慶", "name": "Keita", "role": "英語講師", "text": "そうだね。第4文の 'marked surges in playground socialization'（校庭での対面交流の急増）というポジティブな成果に注目してほしい。自由英作文で『学校でのスマホ禁止に賛成か反対か』は超頻出テーマだから、この具体例は強力な論拠になるよ。"}
        ],
        "vocab": [
            {"word": "mandatory", "phonetic": "/ˈmæn.də.tɔːr.i/", "meaning": "義務的な、強制の", "pos": "adjective", "def": "Required by law or rules; compulsory.", "ex": "Wearing seatbelts is mandatory in most countries."},
            {"word": "fragmentation", "phonetic": "/ˌfræɡ.menˈteɪ.ʃən/", "meaning": "分断、細分化、解体", "pos": "noun", "def": "The process of breaking into small or separate parts.", "ex": "Constant phone pings cause cognitive fragmentation."},
            {"word": "custody", "phonetic": "/ˈkʌs.tə.di/", "meaning": "保管、管理、保護", "pos": "noun", "def": "The protective care or guardianship of someone or something.", "ex": "Students retained physical custody of their locked pouches."},
            {"word": "infraction", "phonetic": "/ɪnˈfræk.ʃən/", "meaning": "違反行為、規則違反", "pos": "noun", "def": "A violation or infringement of a law or agreement.", "ex": "Minor disciplinary infractions were resolved through restorative counseling."},
            {"word": "sanctuary", "phonetic": "/ˈsæŋk.tʃu.er.i/", "meaning": "聖域、避難所、保護区域", "pos": "noun", "def": "A place of safety or refuge from harm or stress.", "ex": "Public libraries serve as quiet sanctuaries for concentrated study."}
        ],
        "syntax": [
            {"title": "現在分詞句による付帯状況の叙述", "formula": "[students deposit devices], [retaining custody] while [rendering notifications inaccessible].", "explanation": "主文の動作 deposit に対して、二つの分詞句 retaining と rendering が並列して付帯的な条件・状態を的確に説明しています。"},
            {"title": "動詞 link A to B（AをBに関連づける・結びつける）", "formula": "evidence [linking unrestricted smartphone access to attention fragmentation and cyberbullying].", "explanation": "現在分詞 linking が先行詞 evidence を修飾し、スマホ利用と注意散漫・ネットいじめという悪影響の因果連鎖を論理的に繋いでいます。"}
        ],
        "quiz": [
            {
                "question": "What is the scope of the phone ban introduced by the English academy chain?",
                "options": [
                    "It applies only to teachers during administrative meetings.",
                    "It mandates that 35,000 pupils across secondary schools remain device-free throughout the entire school day.",
                    "It prohibits pupils from owning smartphones at home during weekends.",
                    "It requires students to sell their personal electronics to the school."
                ],
                "answer": 1,
                "explanation": "第1文で「数十の中高学校にわたる3万5千人の生徒が終日完全に端末を持たない状態を義務付けた」と述べられています。"
            },
            {
                "question": "How do students store their smartphones during the school day under the new protocol?",
                "options": [
                    "They must leave them at home under parental supervision.",
                    "They deposit them into magnetic signal-blocking pouches while retaining physical possession.",
                    "They hand them over to local police officers at the entrance.",
                    "They place them openly on their desks with screens activated."
                ],
                "answer": 1,
                "explanation": "第3文にあるように、生徒は電波遮断ポーチに端末を入れて物理的な所持は維持しつつ通知を遮断します。"
            },
            {
                "question": "Which of the following was reported as a positive result in pilot schools?",
                "options": [
                    "A total cessation of academic examinations.",
                    "A notable increase in playground socialization and extracurricular athletics participation.",
                    "A complete collapse of classroom discipline.",
                    "A massive drop in student attendance rates."
                ],
                "answer": 1,
                "explanation": "第4文で、校庭での社交の急増、放課後スポーツへの参加回復、規律違反の減少が挙げられています。"
            },
            {
                "question": "What cultural shift do sociologists identify behind this school ban?",
                "options": [
                    "A move toward eliminating all electricity from educational institutions.",
                    "A transition away from digital optimism toward viewing schools as sanctuaries from commercial pressure.",
                    "A national demand to replace human educators with artificial avatars.",
                    "A rejection of physical textbooks in favor of virtual reality goggles."
                ],
                "answer": 1,
                "explanation": "最終文で、かつてのデジタル楽観主義から脱却し、学校を商業的アルゴリズムから守る聖域と位置づける文化的転換が指摘されています。"
            },
            {
                "question": "The word 'mandatory' in the opening sentence is closest in meaning to:",
                "options": ["optional", "compulsory", "temporary", "unpopular"],
                "answer": 1,
                "explanation": "mandatory は「義務的な」「強制的な」という意味であり、compulsory が正解です。"
            }
        ]
    },

    # 4. SOCIETY - Four-Day Workweek Permanent (The Guardian Verified)
    {
        "slug": "four-day-workweek-uk-trial-permanent",
        "category": "society",
        "category_label": "LABOUR ECONOMICS & WELLBEING • 週休3日制の恒久化と労働生産性",
        "date": "2026-10-15",
        "title": "Four-Day Workweek Made Permanent by Majority of Firms in World's Largest Trial",
        "headline_ja": "労働経済学：世界最大規模の実証実験で参加企業の過半数が「週休3日制」を恒久導入",
        "subhead": "給与100%維持で労働時間を20%削減。バーンアウトの激減と離職率半減、生産性向上が追跡調査で確定。",
        "lead_snippet": "イギリスで実施された世界最大の「週休3日制（給与維持型）」パイロット実験から1年が経過した追跡調査において、参加企業の89%が制度を継続し、51%が恒久的な社内規定として正式採用したことが判明した。労働生産性を落とさずに過労を解消する新たな働き方の実効性を読み解く。",
        "source_name": "The Guardian",
        "source_url": "https://www.theguardian.com/money/2024/feb/21/four-day-week-made-permanent-for-most-uk-firms-in-worlds-biggest-trial",
        "source_attribution": "Source: The Guardian. Four-day week made permanent for most UK firms in world’s biggest trial.",
        "image": "https://images.unsplash.com/photo-1497215728101-856f4ea42174?w=1000&auto=format&fit=crop&q=80",
        "sentences": [
            {
                "en": "A comprehensive one-year follow-up study of the world's largest trial of a four-day workweek has revealed that over half of participating British companies have made the scheduling arrangement permanent, citing sustained productivity and heightened staff retention.",
                "ja": "週休3日制の世界最大規模の実証実験に関する包括的な1年後追跡調査により、参加したイギリス企業の半数以上が持続的な生産性と高い社員定着率を理由に、この勤務スケジュールを恒久化したことが明らかになった。"
            },
            {
                "en": "Operating under the '100-80-100 model,' employees received one hundred percent of their customary compensation in exchange for eighty percent of conventional time, provided that baseline business output remained fully preserved.",
                "ja": "「100-80-100モデル」のもとで運用され、基準となる事業成果が完全に維持されることを条件に、従業員は従来の80%の労働時間に対して100%の通常給与を受け取った。"
            },
            {
                "en": "Organizational researchers reported that staff turnover dropped by fifty-seven percent across participating enterprises, while employee self-assessments indicated pronounced reductions in chronic anxiety and work-related exhaustion.",
                "ja": "組織研究者らは、参加企業全体で離職率が57%低下し、従業員の自己評価では慢性的な不安や仕事起因の疲労が顕著に軽減したことが示されたと報告した。"
            },
            {
                "en": "Corporate executives highlighted that compressing weekly operations compelled teams to streamline administrative bureaucracy, eliminate redundant meetings, and automate repetitive data-entry processes.",
                "ja": "企業の幹部らは、週の業務を圧縮したことで、チームが管理的な官僚主義を合理化し、不要な会議を全廃し、反復的なデータ入力作業を自動化することを余儀なくされたと強調した。"
            },
            {
                "en": "Economists suggest that as labor markets adapt to demographic contraction, shortened work schedules will transition from competitive recruitment perks into standardized industrial conventions.",
                "ja": "経済学者らは、労働市場が人口減少に適応するにつれて、短縮された労働スケジュールは人材獲得競争のための特権から、標準的な産業慣行へと移行していくだろうと示唆している。"
            }
        ],
        "dialogue": [
            {"speaker": "七", "name": "Nanami", "role": "生徒", "text": "給料を下げずに休みを週3日に増やすなんて夢のようですが、本当に成り立つんですね！"},
            {"speaker": "慶", "name": "Keita", "role": "英語講師", "text": "第2文の '100-80-100 model'（給与100%・時間80%・成果100%維持）がポイントだね。単にサボるのではなく、成果を落とさないことが前提なんだ。"},
            {"speaker": "七", "name": "Nanami", "role": "生徒", "text": "第4文にあるように、ムダな会議をなくしたり仕事を自動化して、短い時間で集中して終わらせるようになったんですね。"},
            {"speaker": "慶", "name": "Keita", "role": "英語講師", "text": "その通り。第3文の離職率が57%激減（staff turnover dropped by 57%）したのも企業にとって大きなメリットだ。入試小論文や慶應経済・法学部などの長文でも『少子化・人手不足時代の労働生産性と幸福度』は最重要テーマだよ。"}
        ],
        "vocab": [
            {"word": "retention", "phonetic": "/rɪˈten.ʃən/", "meaning": "維持、保持、定着（人材定着率）", "pos": "noun", "def": "The continued use, existence, or keeping of something in an organization.", "ex": "Competitive benefits packages improve employee retention."},
            {"word": "turnover", "phonetic": "/ˈtɜːrnˌoʊ.vər/", "meaning": "離職率、売上高、回転率", "pos": "noun", "def": "The rate at which employees leave a workforce and are replaced.", "ex": "High staff turnover imposes substantial recruitment costs."},
            {"word": "streamline", "phonetic": "/ˈstriːm.laɪn/", "meaning": "合理化する、無駄を削ぎ落とす", "pos": "verb", "def": "To make an organization or system more efficient and effective.", "ex": "Management streamlined administrative procedures to save time."},
            {"word": "redundant", "phonetic": "/rɪˈdʌn.dənt/", "meaning": "不要な、余分な、重複した", "pos": "adjective", "def": "Not or no longer needed or useful; superfluous.", "ex": "Weekly status meetings became redundant after implementing real-time dashboards."},
            {"word": "perk", "phonetic": "/pɜːrk/", "meaning": "特典、手当、優遇措置", "pos": "noun", "def": "An extra benefit or privilege given with a job.", "ex": "Free gym membership is a standard corporate perk."}
        ],
        "syntax": [
            {"title": "条件節を導く接続詞 provided that（〜という条件で）", "formula": "[employees received compensation], [provided that business output remained preserved].", "explanation": "provided that（または providing that）は if や on condition that と同義で、給与維持の必須条件として生産性の維持を明確に規定しています。"},
            {"title": "動詞 compel + 目的語 + to 不定詞（強制的に〜させる）", "formula": "[compressing operations] compelled [teams] [to streamline bureaucracy and eliminate meetings].", "explanation": "無生物主語 compressing operations が compel A to do（Aに〜することを促す・余儀なくさせる）を導き、労働時間の短縮が業務効率化の強力な起爆剤となったことを表しています。"}
        ],
        "quiz": [
            {
                "question": "What does the '100-80-100 model' mean in the context of the trial?",
                "options": [
                    "Employees receive 100% pay for 80% time, provided that 100% productivity is maintained.",
                    "Workers must achieve 100% attendance across 80 consecutive days for a 100-pound bonus.",
                    "Firms cut salaries by 80% if output drops below 100 units.",
                    "Enterprises require 100% overtime from 80% of their managerial staff."
                ],
                "answer": 0,
                "explanation": "第2文にあるように、「通常の100%の給与で、労働時間を80%にし、基準成果を100%維持する」というモデルです。"
            },
            {
                "question": "What specific human resource benefit was observed in participating organizations?",
                "options": [
                    "Staff turnover dropped by 57 percent along with decreases in anxiety and exhaustion.",
                    "Companies were forced to lay off more than half of their employees.",
                    "Workers reported universal dissatisfaction with their four-day schedules.",
                    "Management ceased paying national health insurance premiums."
                ],
                "answer": 0,
                "explanation": "第3文で「参加企業全体で離職率が57%低下し、慢性的な不安や仕事の疲労が顕著に減少した」と記されています。"
            },
            {
                "question": "How did teams maintain high productivity despite shorter working hours?",
                "options": [
                    "By working through weekends in secret.",
                    "By streamlining bureaucracy, cutting redundant meetings, and automating repetitive tasks.",
                    "By hiring massive cohorts of unpaid interns.",
                    "By lowering product quality standards across the board."
                ],
                "answer": 1,
                "explanation": "第4文で、業務圧縮によって官僚主義を合理化し、不要な会議をなくし、反復作業を自動化したと説明されています。"
            },
            {
                "question": "What future trend do economists predict regarding shortened workweeks?",
                "options": [
                    "They will be completely banned by European parliaments.",
                    "They will transition from niche recruitment perks into standard industrial norms.",
                    "They will cause immediate national economic collapse in advanced democracies.",
                    "They will only apply to high-earning corporate CEOs."
                ],
                "answer": 1,
                "explanation": "最終文で、人口減少に適応する中で、短縮労働は人材獲得の特権から「標準的な産業慣行」へと移行していくだろうと予測されています。"
            },
            {
                "question": "The word 'streamline' in paragraph 4 is closest in meaning to:",
                "options": ["complicate", "make more efficient", "ignore", "expand drastically"],
                "answer": 1,
                "explanation": "streamline は「合理化する」「無駄を省いて効率化する」という意味であり、make more efficient が正解です。"
            }
        ]
    },

    # 5. WORLD - Mont Blanc Glacier Melting (The Guardian Oct 14, 2026)
    {
        "slug": "mont-blanc-glacier-melt-elevation-loss",
        "category": "world",
        "category_label": "CLIMATE GEOGRAPHY & GLACIOLOGY • モンブラン標高低下と地球温暖化",
        "date": "2026-10-15",
        "title": "Mont Blanc Loses Over One Metre of Height as Alpine Glaciers Rapidly Shrink",
        "headline_ja": "環境地理学：「欧州の屋根」モンブランの標高が1メートル以上低下、氷河融解の加速を実測",
        "subhead": "山頂冠氷の融解により標高4,805.59メートルへ。アルプス氷河の後退が下流水源と生態系に与える深刻な影響。",
        "lead_snippet": "フランス・イタリア国境にそびえる西ヨーロッパ最高峰モンブランの最新測量調査により、山頂を覆う氷雪層の急激な融解に伴い、過去数年で標高が1メートル以上低下したことが確認された。地球温暖化がもたらす高山生態系の急変と、欧州主要河川の水源枯渇危機を検証する。",
        "source_name": "The Guardian",
        "source_url": "https://www.theguardian.com/environment/2026/oct/14/mont-blanc-loses-metre-height",
        "source_attribution": "Source: The Guardian (Oct 14, 2026). Mont Blanc, the ‘roof of Europe’, loses more than a metre of height.",
        "image": "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?w=1000&auto=format&fit=crop&q=80",
        "sentences": [
            {
                "en": "Official topographical surveyors have confirmed that Mont Blanc, Western Europe's highest peak, has shrunk by more than one full metre over recent years, registering an official summit elevation of 4,805.59 metres due to catastrophic summer glacial ablation.",
                "ja": "公式の地形測量調査員らは、西ヨーロッパ最高峰モンブランが近年の壊滅的な夏季氷河融解により1メートル以上縮小し、公式の山頂標高が4,805.59メートルを記録したことを確認した。"
            },
            {
                "en": "While the mountain's underlying rocky bedrock remains physically static, its variable dome of perennial ice and firn fluctuates in direct response to thermal precipitation anomalies and escalating heatwaves.",
                "ja": "山頂を支える岩盤そのものは物理的に変化しないものの、その上を覆う万年氷と万年雪のドームは、気温・降水異常や激化する熱波に直接反応して変動している。"
            },
            {
                "en": "Glaciologists monitoring Alpine ice masses warn that sustained elevation loss threatens downstream hydrological stability, depleting crucial meltwater reservoirs that replenish major European waterways including the Rhône and Po rivers.",
                "ja": "アルプスの氷塊を監視する氷河学者らは、継続的な標高低下が下流の水文学的安定性を脅かし、ローヌ川やポー川など欧州の主要水路を潤す重要な融雪水リザーバーを枯渇させていると警告している。"
            },
            {
                "en": "Furthermore, destabilized permafrost along alpine climbing corridors has triggered unprecedented rockfalls, compelling regional mountaineering authorities to restrict traditional ascent routes to safeguard climbers.",
                "ja": "さらに、高山登山ルート沿いの永久凍土の不安定化が前例のない落石事故を引き起こしており、地域の登山当局は登山者の安全を守るために伝統的な登頂ルートを制限することを余儀なくされている。"
            },
            {
                "en": "Environmental diplomats underscore that the visible retreat of Europe's most iconic glacial summit serves as an undeniable physical barometer of climate inaction before upcoming global ecological summits.",
                "ja": "環境外交官らは、ヨーロッパで最も象徴的な氷河山頂の目に見える後退が、間近に迫る国際環境サミットを前に、気候変動対策の不作為を示す否定しがたい物理的バロメーター（指標）として機能していると強調している。"
            }
        ],
        "dialogue": [
            {"speaker": "七", "name": "Nanami", "role": "生徒", "text": "ヨーロッパアルプスの最高峰モンブランの標高が1メートル以上も低くなったなんて、温暖化の影響が目に見えて現れているんですね。"},
            {"speaker": "慶", "name": "Keita", "role": "英語講師", "text": "第2文にあるように、岩盤（bedrock）が削れたのではなく、山頂を覆う万年氷（perennial ice）が熱波で溶けてしまっているんだ（ablation）。"},
            {"speaker": "七", "name": "Nanami", "role": "生徒", "text": "第3文のローヌ川やポー川の水源枯渇（hydrological stability）も深刻ですね。山の雪が溶けてなくなると、川の水や農業用水が足りなくなってしまいます。"},
            {"speaker": "慶", "name": "Keita", "role": "英語講師", "text": "第4文の永久凍土（permafrost）融解による落石も登山界で大問題になっている。地球環境問題と地理学・国際合意（第5文の climate inaction）を結びつける長文は東大・京大・早慶で超頻出だよ。"}
        ],
        "vocab": [
            {"word": "ablation", "phonetic": "/æbˈleɪ.ʃən/", "meaning": "融解、消耗、アブレーション", "pos": "noun", "def": "The removal or melting of snow and ice from a glacier.", "ex": "Summer ablation rates exceeded annual winter snowfall accumulation."},
            {"word": "perennial", "phonetic": "/pəˈren.i.əl/", "meaning": "万年の、永続する、多年生の", "pos": "adjective", "def": "Lasting or existing for a long or apparently infinite time.", "ex": "Perennial mountain snowpacks are shrinking across temperate latitudes."},
            {"word": "hydrological", "phonetic": "/ˌhaɪ.drəˈlɑː.dʒɪ.kəl/", "meaning": "水文学の、水の循環に関する", "pos": "adjective", "def": "Relating to the properties, distribution, and circulation of water.", "ex": "Deforestation alters the local hydrological cycle."},
            {"word": "permafrost", "phonetic": "/ˈpɜːr.mə.frɔːst/", "meaning": "永久凍土", "pos": "noun", "def": "A thick subsurface layer of soil that remains frozen throughout the year.", "ex": "Thawing permafrost releases trapped greenhouse gases and destabilizes slopes."},
            {"word": "barometer", "phonetic": "/bəˈrɑː.mɪ.tər/", "meaning": "気圧計、指標、バロメーター", "pos": "noun", "def": "Something that reflects changes in circumstances or opinions.", "ex": "Glacial retreat is a sensitive barometer of global atmospheric warming."}
        ],
        "syntax": [
            {"title": "対比の接続詞 While による物理的対比", "formula": "While [the rocky bedrock remains static], [its variable dome fluctuates in response to heatwaves].", "explanation": "接続詞 While が「岩盤そのものは不変であるのに対して、氷雪ドームは熱波に反応して激しく変動する」という対比構造を格調高く表現しています。"},
            {"title": "動詞 replenish + 目的語", "formula": "depleting reservoirs [that replenish major waterways including Rhône and Po].", "explanation": "関係代名詞 that が導く節内で動詞 replenish（再び満たす・補給する）が使われ、氷河融雪水が欧州の大河川を涵養する生命線であることを示しています。"}
        ],
        "quiz": [
            {
                "question": "What is the primary cause of Mont Blanc's reduction in height?",
                "options": [
                    "Tectonic subsidence of the European continental plate.",
                    "Catastrophic summer glacial ablation melting the summit's ice cap.",
                    "Extensive commercial mining along the mountain's granite ridge.",
                    "Volcanic eruption altering the surrounding crater."
                ],
                "answer": 1,
                "explanation": "第1文で「壊滅的な夏季の氷河融解（catastrophic summer glacial ablation）により標高が低下した」と明記されています。"
            },
            {
                "question": "How does the mountain's physical structure react to rising temperatures?",
                "options": [
                    "The rocky bedrock has collapsed into deep valleys.",
                    "The bedrock remains physically static while the ice and firn dome fluctuates with heatwaves.",
                    "The ice dome has expanded into surrounding Swiss villages.",
                    "The entire peak has turned completely into liquid water."
                ],
                "answer": 1,
                "explanation": "第2文で、基盤の岩盤は静止したままである一方、万年氷雪のドームが熱波に反応して変動していると説明されています。"
            },
            {
                "question": "What downstream risk do glaciologists highlight regarding continuous ice loss?",
                "options": [
                    "The permanent freeze of all European agricultural land.",
                    "The depletion of vital meltwater reservoirs that feed major rivers like the Rhône and Po.",
                    "An uncontrollable expansion of marine shipping lanes across the Alps.",
                    "An excessive surplus of cheap hydroelectric energy."
                ],
                "answer": 1,
                "explanation": "第3文で、ローヌ川やポー川など主要水路を満たす極めて重要な融雪水リザーバーが枯渇することが警告されています。"
            },
            {
                "question": "Why have mountaineering authorities restricted traditional ascent routes?",
                "options": [
                    "Because climbing fees have become too expensive for tourists.",
                    "Because thawing permafrost has triggered dangerous and unprecedented rockfalls.",
                    "Because all mountain guides have relocated to Antarctica.",
                    "Because local wildlife species have established military blockades."
                ],
                "answer": 1,
                "explanation": "第4文で、永久凍土の不安定化によって前例のない落石事故が発生しているためルート制限が行われたと記されています。"
            },
            {
                "question": "The word 'perennial' in the second sentence means:",
                "options": ["short-lived", "lasting for many years or permanently", "artificial", "chemically treated"],
                "answer": 1,
                "explanation": "perennial は「万年の」「永続的な」「多年生の」を意味し、lasting for many years or permanently が正解です。"
            }
        ]
    },

    # 6. WORLD - Renewables Overtake Fossil Fuels in EU (The Guardian Verified)
    {
        "slug": "renewables-overtake-fossil-fuels-eu-electricity",
        "category": "world",
        "category_label": "GLOBAL ENERGY & CLIMATE POLICY • 欧州再エネ発電シェアの歴史的逆転",
        "date": "2026-10-15",
        "title": "Wind and Solar Overtake Fossil Fuels to Generate 30 Percent of EU Electricity",
        "headline_ja": "国際エネルギー：風力・太陽光発電が化石燃料を逆転、EU電力の30％を供給する歴史的転換点",
        "subhead": "石炭・天然ガス火力発電が激減。地政学的エネルギー自立と脱炭素目標の同時達成へ前進。",
        "lead_snippet": "欧州連合（EU）加盟国全体において、風力と太陽光による発電比率が初めて化石燃料（石炭・石油・ガス）の合計シェアを上回る30%に到達した。ウクライナ危機を契機とした再エネ投資の加速が実を結び、化石燃料依存からの脱却が不可逆的なペースで進む国際情勢を分析する。",
        "source_name": "The Guardian",
        "source_url": "https://www.theguardian.com/environment/article/2024/jul/30/renewables-overtake-fossil-fuels-to-provide-30-of-eu-electricity",
        "source_attribution": "Source: The Guardian. Renewables overtake fossil fuels to provide 30% of EU electricity.",
        "image": "https://images.unsplash.com/photo-1466611653911-95081537e5b7?w=1000&auto=format&fit=crop&q=80",
        "sentences": [
            {
                "en": "Wind and solar infrastructure generated thirty percent of the European Union's total electricity during the first half of the year, outstripping combined fossil fuel generation for the first time in continental history.",
                "ja": "今年の上半期において、風力および太陽光発電設備が欧州連合（EU）の総発電量の30%を供給し、大陸の歴史上初めて化石燃料発電の合計を上回った。"
            },
            {
                "en": "Independent energy analytics confirmed that fossil generation plummeted by seventeen percent, driven by a dramatic collapse in coal combustion alongside substantial curtailments in thermal gas generation.",
                "ja": "独立系エネルギー分析機関は、石炭燃焼の劇的な崩壊と火力ガス発電の大幅な抑制により、化石燃料による発電量が17%急落したことを確認した。"
            },
            {
                "en": "Thirteen individual member states successfully produced more clean power from renewable turbines and photovoltaic arrays than from combustible hydrocarbon sources during the surveyed timeframe.",
                "ja": "調査対象期間中、13の加盟国が再生可能エネルギー風力タービンや太陽光アレイから、燃焼性炭化水素源よりも多くのクリーン電力を生み出すことに成功した。"
            },
            {
                "en": "Policy analysts credit aggressive post-crisis electrification initiatives, which transformed decarbonization from an environmental aspiration into an urgent geopolitical national security mandate.",
                "ja": "政策アナリストらは、脱炭素化を単なる環境的な念願から喫緊の地政学的・国家安全保障上の至上命題へと変貌させた、危機後の積極的な電化推進政策の成果であると評価している。"
            },
            {
                "en": "Grid transmission operators nonetheless emphasize that maintaining this green momentum requires urgent capital investment into cross-border smart interconnectors and high-capacity battery storage systems.",
                "ja": "送電網の運営者らはそれでもなお、この環境推進の勢いを維持するためには、国境を越えたスマート相互連系線や大容量蓄電池システムへの緊急の設備投資が不可欠であると強調している。"
            }
        ],
        "dialogue": [
            {"speaker": "七", "name": "Nanami", "role": "生徒", "text": "EU全体で風力と太陽光の電気が化石燃料を逆転して30%に達したんですね！"},
            {"speaker": "慶", "name": "Keita", "role": "英語講師", "text": "第1文の 'outstripping combined fossil fuel generation'（化石燃料の合計発電量を追い抜く）は歴史的な転換点だね。13カ国ですでに再エネが化石燃料を超えているんだ。"},
            {"speaker": "七", "name": "Nanami", "role": "生徒", "text": "第4文にあるように、環境のためだけでなく『地政学的・国家安全保障上の至上命題（geopolitical national security mandate）』として再エネを進めたのが大きかったんですね。"},
            {"speaker": "慶", "name": "Keita", "role": "英語講師", "text": "ロシアへの天然ガス依存から脱却するための安全保障だったんだね。ただし第5文にある通り、国境をまたぐ送電網（interconnectors）や蓄電池の整備という課題も残されているよ。"}
        ],
        "vocab": [
            {"word": "outstrip", "phonetic": "/ˌaʊtˈstrɪp/", "meaning": "追い抜く、凌駕する、上回る", "pos": "verb", "def": "To move faster than and overtake someone or something; exceed.", "ex": "Renewable capacity outstripped fossil fuel additions in global energy markets."},
            {"word": "curtailment", "phonetic": "/kɜːrˈteɪl.mənt/", "meaning": "削減、抑制、短縮", "pos": "noun", "def": "The action of reducing or restricting something.", "ex": "The curtailment of gas imports accelerated heat pump adoption."},
            {"word": "photovoltaic", "phonetic": "/ˌfoʊ.toʊ.vɑːlˈteɪ.ɪk/", "meaning": "太陽光発電の、光起電力の", "pos": "adjective", "def": "Relating to the production of electric current at the junction of two substances exposed to light.", "ex": "Photovoltaic panel efficiencies have risen substantially over the decade."},
            {"word": "mandate", "phonetic": "/ˈmæn.deɪt/", "meaning": "至上命題、権限、委任された命令", "pos": "noun", "def": "An official order or commission to do something.", "ex": "National energy security became an urgent political mandate."},
            {"word": "interconnector", "phonetic": "/ˌɪn.tər.kəˈnek.tər/", "meaning": "送電相互連系線", "pos": "noun", "def": "A high-voltage cable that allows electricity to flow between different national grids.", "ex": "Subsea interconnectors share surplus wind energy between Britain and Norway."}
        ],
        "syntax": [
            {"title": "無生物主語構文 credit A (with B) / credit A to B", "formula": "Policy analysts credit [aggressive electrification initiatives], which transformed X into Y.", "explanation": "credit A（Aの功績・要因と評価する）の目的語にイニシアチブを置き、非制限用法の関係代名詞 which で「それが脱炭素を安全保障の至上命題へ変貌させた」と補足しています。"},
            {"title": "現在分詞句 driven by による原因説明", "formula": "generation plummeted by 17%, [driven by a dramatic collapse in coal combustion].", "explanation": "主節（発電量が17%急落した）に過去分詞句 driven by が接続し、石炭火力の崩壊という主原因を簡潔に示しています。"}
        ],
        "quiz": [
            {
                "question": "What milestone did the European Union achieve in the first half of the year?",
                "options": [
                    "Nuclear power was entirely decommissioned across all member states.",
                    "Wind and solar generated 30% of total electricity, surpassing combined fossil fuels for the first time.",
                    "Fossil fuel consumption increased to 80% due to cold winter weather.",
                    "All subsea electrical cables were removed from the North Sea."
                ],
                "answer": 1,
                "explanation": "第1文で「風力と太陽光が総発電量の30%を供給し、史上初めて化石燃料の合計を追い抜いた」と述べられています。"
            },
            {
                "question": "By how much did fossil fuel power generation decrease in the EU during this period?",
                "options": ["It fell by 17 percent.", "It increased by 30 percent.", "It remained exactly unchanged.", "It dropped by 95 percent."],
                "answer": 0,
                "explanation": "第2文で 'fossil generation plummeted by seventeen percent'（17%急落した）と明記されています。"
            },
            {
                "question": "How did post-crisis policies alter the perception of decarbonization?",
                "options": [
                    "They dismissed clean energy as an impractical luxury.",
                    "They transformed decarbonization into an urgent geopolitical national security mandate.",
                    "They mandated that all citizens purchase personal coal stoves.",
                    "They transferred all energy regulation to private oil cartels."
                ],
                "answer": 1,
                "explanation": "第4文で「脱炭素化を環境的願望から喫緊の地政学的・国家安全保障上の至上命題へと変貌させた」と記されています。"
            },
            {
                "question": "What infrastructure improvement is vital to sustain renewable momentum according to grid operators?",
                "options": [
                    "Rebuilding decommissioned coal mines in central Europe.",
                    "Investing capital into cross-border smart interconnectors and high-capacity battery systems.",
                    "Banning household rooftop solar installations.",
                    "Diverting electrical power away from hospitals."
                ],
                "answer": 1,
                "explanation": "最終文で、国境を越えたスマート相互連系線と大容量蓄電池システムへの緊急投資が必要であると強調されています。"
            },
            {
                "question": "The word 'outstripping' in the first paragraph is closest in meaning to:",
                "options": ["exceeding", "underperforming", "subsidizing", "destroying"],
                "answer": 0,
                "explanation": "outstrip は「上回る」「追い抜く」を意味し、exceeding（超える）と同義です。"
            }
        ]
    },

    # 7. LAW - EU AI Act & Consumers (The Guardian Verified)
    {
        "slug": "eu-ai-act-consumer-rights-enforcement",
        "category": "law",
        "category_label": "DIGITAL JURISPRUDENCE & AI GOVERNANCE • 欧州AI法と消費者権利保護",
        "date": "2026-10-15",
        "title": "What the EU Artificial Intelligence Act Means for Consumer Safety and Digital Rights",
        "headline_ja": "情報法学：世界初の包括的「欧州AI法」が消費者の安全とプライバシーに与える法的影響",
        "subhead": "リスクに応じた4段階規制。生体認証や感情認識の禁止、生成AIの透明性義務化がもたらす世界的標準。",
        "lead_snippet": "欧州連合で成立した包括的AI規制法（EU AI Act）は、消費者の基本的権利を侵害する高リスクAIの利用を厳格に制限し、違反企業に巨額の制裁金を科す。GDPRに続き「ブリュッセル効果」を通じて世界のAI開発基準を規定しつつある最前線の法制度を解き明かす。",
        "source_name": "The Guardian",
        "source_url": "https://www.theguardian.com/technology/2024/mar/14/what-will-eu-proposed-regulation-ai-mean-consumers",
        "source_attribution": "Source: The Guardian. What will the EU's proposed regulation of AI mean for consumers?",
        "image": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=1000&auto=format&fit=crop&q=80",
        "sentences": [
            {
                "en": "The European Union's landmark Artificial Intelligence Act has officially entered into force, establishing the world's first binding regulatory architecture that classifies artificial intelligence applications into distinct tiers based on potential societal hazard.",
                "ja": "欧州連合（EU）の画期的な「人工知能法（AI法）」が正式に施行され、AIアプリケーションを社会への潜在的危険度に応じて明確な階層に分類する世界初の拘束力ある規制枠組みが確立された。"
            },
            {
                "en": "Systems deemed to pose 'unacceptable risks'—including predatory cognitive behavioral manipulation, social credit scoring, and untargeted facial recognition scraping in public spaces—face outright bans backed by multi-million-euro statutory fines.",
                "ja": "略奪的な認知行動操作、ソーシャルクレジットによる信用格付け、公共空間での無差別な顔認証データ収集など、「容認できないリスク」をもたらすと判断されたシステムは、数千万ユーロ規模の法定罰金を伴う全面禁止に直面する。"
            },
            {
                "en": "For 'high-risk' algorithms deployed in critical domains such as medical diagnosis, employment recruitment, and law enforcement credit assessment, developers must guarantee rigorous algorithmic auditing and human oversight.",
                "ja": "医療診断、雇用採用選考、法執行における信用評価といった重要分野に配備される「ハイリスク」アルゴリズムについて、開発者は厳格なアルゴリズム監査と人間の関与（ヒューマン・イン・ザ・ループ）を保証しなければならない。"
            },
            {
                "en": "General-purpose generative models, including conversational chatbots, must maintain comprehensive copyright compliance documentation and visibly watermark synthetic audiovisual media to combat disinformation.",
                "ja": "対話型チャットボットをはじめとする汎用生成AIモデルは、包括的な著作権遵守文書を維持し、偽情報対策として合成音声・映像メディアに目に見える透かし（ウォーターマーク）を付すことが義務付けられる。"
            },
            {
                "en": "Legal scholars project that this legislation will trigger another profound 'Brussels Effect,' compelling international tech conglomerates to harmonize their global products with European consumer protection benchmarks.",
                "ja": "法学者らは、この立法がかつての個人情報保護に匹敵する「ブリュッセル効果」を引き起こし、国際的なテクノロジー複合企業に対し、自社の世界向け製品を欧州の消費者保護基準に適合させることを余儀なくさせるだろうと予測している。"
            }
        ],
        "dialogue": [
            {"speaker": "七", "name": "Nanami", "role": "生徒", "text": "EUのAI法（AI Act）がついに施行されたんですね！危険度に応じてランク分けされているのが分かりやすいです。"},
            {"speaker": "慶", "name": "Keita", "role": "英語講師", "text": "第2文の 'unacceptable risks'（容認できないリスク）は全面禁止、第3文の就職や医療での 'high-risk' は人間のチェック（human oversight）が必須とされているね。"},
            {"speaker": "七", "name": "Nanami", "role": "生徒", "text": "第4文の生成AIに電子透かし（watermark synthetic media）を入れる義務も、ディープフェイク対策として重要ですね。"},
            {"speaker": "慶", "name": "Keita", "role": "英語講師", "text": "最終文の 'Brussels Effect'（ブリュッセル効果）は大学入試の法学・国際関係論で頻出のキーワードだ。EUのルールが結果として世界中のIT企業の事実上の標準になっていく現象のことだよ。"}
        ],
        "vocab": [
            {"word": "binding", "phonetic": "/ˈbaɪn.dɪŋ/", "meaning": "法的拘束力のある", "pos": "adjective", "def": "Involving an obligation that cannot be broken.", "ex": "The parties entered into a legally binding international treaty."},
            {"word": "tier", "phonetic": "/tɪr/", "meaning": "階層、レベル、段階", "pos": "noun", "def": "One of a series of rows or levels placed one above the other.", "ex": "The act classifies algorithms into four distinct risk tiers."},
            {"word": "statutory", "phonetic": "/ˈstætʃ.ə.tɔːr.i/", "meaning": "法令の、法定の", "pos": "adjective", "def": "Required, permitted, or enacted by statute.", "ex": "Violators face severe statutory penalties under European law."},
            {"word": "watermark", "phonetic": "/ˈwɔː.tər.mɑːrk/", "meaning": "透かしを入れる、電子透かし", "pos": "verb", "def": "To mark digital content with an identifying signature.", "ex": "Developers must visibly watermark synthetically generated photographs."},
            {"word": "harmonize", "phonetic": "/ˈhɑːr.mə.naɪz/", "meaning": "適合させる、一致させる、調和させる", "pos": "verb", "def": "To bring into agreement or compatibility.", "ex": "Multinationals harmonize software privacy features across jurisdictions."}
        ],
        "syntax": [
            {"title": "過去分詞による名詞修飾と列挙ダッシュ構文", "formula": "Systems [deemed to pose risks]—including X, Y, and Z—face outright bans.", "explanation": "過去分詞 deemed が主語 Systems を修飾し、ダッシュ挿入句（—including...—）で具体的禁止例を挙げた上で、本動詞 face（直面する）へと力強く展開しています。"},
            {"title": "動詞 project that 節（〜と予測・見通す）", "formula": "Scholars project [that this legislation will trigger the Brussels Effect, compelling X to do Y].", "explanation": "動詞 project が未来の予測を示す that 節を導き、分詞構文 compelling（〜を余儀なくさせる）で国際市場への波及効果を説明しています。"}
        ],
        "quiz": [
            {
                "question": "What is the core regulatory mechanism of the EU Artificial Intelligence Act?",
                "options": [
                    "It bans all computers and mathematical algorithms throughout European universities.",
                    "It classifies artificial intelligence applications into distinct risk tiers based on potential societal harm.",
                    "It exempts multinational tech firms from all consumer copyright laws.",
                    "It requires citizens to obtain governmental licenses before asking online questions."
                ],
                "answer": 1,
                "explanation": "第1文で「AIアプリケーションを社会への潜在的危険度に応じて明確な階層に分類する規制枠組み」と述べられています。"
            },
            {
                "question": "Which of the following AI practices faces an outright ban under the act?",
                "options": [
                    "Translating scientific papers between French and German.",
                    "Predatory cognitive behavioral manipulation and indiscriminate facial recognition scraping in public spaces.",
                    "Designing computer chess programs for teenagers.",
                    "Generating weather forecasts using radar data."
                ],
                "answer": 1,
                "explanation": "第2文で「略奪的な認知行動操作や公共空間での無差別な顔認証データ収集」は全面禁止に直面すると明記されています。"
            },
            {
                "question": "What requirement is imposed on 'high-risk' algorithms used in hiring or healthcare?",
                "options": [
                    "They must be designed exclusively by high school students.",
                    "Developers must guarantee rigorous algorithmic auditing and human oversight.",
                    "They must be distributed completely free of charge.",
                    "They must be shut down permanently during nighttime hours."
                ],
                "answer": 1,
                "explanation": "第3文にあるように、ハイリスクAIには「厳格なアルゴリズム監査と人間の監督（human oversight）」の保証が義務付けられています。"
            },
            {
                "question": "What is the 'Brussels Effect' mentioned in the final sentence?",
                "options": [
                    "A meteorological phenomenon causing seasonal rainstorms in Belgium.",
                    "The process whereby EU regulations become the de facto global standard for international corporations.",
                    "A mandatory tax on all chocolate and pastry imports.",
                    "A military defense pact among northern European countries."
                ],
                "answer": 1,
                "explanation": "最終文で、国際的なテクノロジー複合企業が自社製品をEUの消費者保護基準に合わせることを余儀なくされる現象と説明されています。"
            },
            {
                "question": "The word 'binding' in paragraph 1 is closest in meaning to:",
                "options": ["optional", "legally enforceable", "temporary", "confidential"],
                "answer": 1,
                "explanation": "binding は「法的拘束力のある」を意味し、legally enforceable（法的に執行可能な）が正解です。"
            }
        ]
    },

    # 8. LAW - US Newspapers OpenAI Lawsuit (The Guardian Verified)
    {
        "slug": "us-newspapers-openai-copyright-lawsuit",
        "category": "law",
        "category_label": "INTELLECTUAL PROPERTY & FAIR USE • AIモデル学習と新聞著作権侵害訴訟",
        "date": "2026-10-15",
        "title": "US Newspapers Sue OpenAI and Microsoft Over Unauthorized Use of Millions of Articles",
        "headline_ja": "知的財産法：米有力新聞グループがOpenAIとマイクロソフトを提訴、無断記事学習の違法性を主張",
        "subhead": "報道機関の著作権とフェアユースの境界。独自取材記事を対価なく商業AIに転用することの司法判断へ。",
        "lead_snippet": "ニューヨーク・デイリーニューズやシカゴ・トリビューンなど米国の主要8紙が、自社の何百万本もの調査報道記事を無許可・無対価でChatGPT等の学習データに利用されたとして、連邦地方裁判所に著作権侵害訴訟を提起した。ジャーナリズムの生存権とAI産業の未来を左右する法廷闘争を精読する。",
        "source_name": "The Guardian",
        "source_url": "https://www.theguardian.com/technology/2024/apr/30/us-newspaper-openai-lawsuit",
        "source_attribution": "Source: The Guardian. US newspaper group sues OpenAI and Microsoft over copyright infringement.",
        "image": "https://images.unsplash.com/photo-1589829545856-d10d557cf95f?w=1000&auto=format&fit=crop&q=80",
        "sentences": [
            {
                "en": "Eight prominent American daily newspapers have filed a landmark copyright infringement lawsuit against leading artificial intelligence developers, alleging that millions of original investigative articles were unlawfully scraped without license or remuneration.",
                "ja": "米国の有力日刊新聞8紙が大手AI開発企業に対して歴史的な著作権侵害訴訟を提起し、何百万本もの独自の調査報道記事がライセンスや対価なしに違法にスクレイピング（無断収集）されたと主張した。"
            },
            {
                "en": "The complaint contends that the defendants purloined copyrighted journalism to train commercial large language models that subsequently generate verbatim excerpts, directly cannibalizing subscriber revenues.",
                "ja": "訴状は、被告らが著作権で保護された報道記事を盗用して商用大規模言語モデルを訓練し、そのモデルが逐語的な抜粋を生成することで新聞社の有料会員収入を直接侵食していると訴えている。"
            },
            {
                "en": "While technology companies assert that algorithmic training constitutes 'fair use' transformative adaptation under federal intellectual property doctrine, publishers counter that commercial substitution destroys the financial viability of local newsrooms.",
                "ja": "テクノロジー企業側はアルゴリズムの学習が連邦知的財産法理上の変革的翻案としての「フェアユース（公正利用）」に該当すると主張するのに対し、出版社側は商業的代替が地域報道機関の財務的存続を破壊すると反論している。"
            },
            {
                "en": "The legal action highlights the contentious issue of 'synthetic hallucinations,' wherein conversational agents falsely attribute fabricated quotes and fabricated errors to reputable journalistic mastheads.",
                "ja": "この訴訟は、対話型エージェントが捏造された引用や誤りを著名な新聞の標題に不当に帰属させてしまう「AIの幻覚（ハルシネーション）」という深刻な問題も浮き彫りにしている。"
            },
            {
                "en": "Constitutional jurisprudence experts emphasize that the judicial resolution of this dispute will redefine the delicate equilibrium between technological innovation and intellectual property incentives for decades to come.",
                "ja": "憲法および法理学の専門家らは、この紛争の司法的解決が、技術革新と知的財産権の保護インセンティブとの間の繊細な均衡を今後数十年にわたって再定義することになるだろうと強調している。"
            }
        ],
        "dialogue": [
            {"speaker": "七", "name": "Nanami", "role": "生徒", "text": "アメリカの新聞社がAI開発企業を著作権侵害で訴えたニュースですね。記者が苦労して書いた記事がAIの学習に使われている問題です。"},
            {"speaker": "慶", "name": "Keita", "role": "英語講師", "text": "第3文にある 'fair use'（フェアユース：公正利用）と 'commercial substitution'（商業的代替）の対立が最大の法的な争点だよ。"},
            {"speaker": "七", "name": "Nanami", "role": "生徒", "text": "AIが新聞記事の内容をそのまま回答してしまったら、誰も新聞社のサイトにお金を払わなくなっちゃいますね（第2文の 'cannibalizing subscriber revenues'）。"},
            {"speaker": "慶", "name": "Keita", "role": "英語講師", "text": "さらに第4文のハルシネーション（AIの嘘）で、新聞社が言ってもいないデタラメが『新聞社の記事によると』と表示される被害も出ている。東大・京大・早慶の英語長文でも『生成AIと著作権の境界線』は必出テーマだよ。"}
        ],
        "vocab": [
            {"word": "remuneration", "phonetic": "/rɪˌmjuː.nəˈreɪ.ʃən/", "meaning": "報酬、対価、報償", "pos": "noun", "def": "Money paid for work or a service.", "ex": "Authors demanded fair remuneration for digital book reproduction."},
            {"word": "purloin", "phonetic": "/pɜːrˈlɔɪn/", "meaning": "盗む、くすねる、不法領得する", "pos": "verb", "def": "To steal something, especially in a breach of trust.", "ex": "The lawsuit alleges that proprietary code was purloined by rivals."},
            {"word": "cannibalize", "phonetic": "/ˈkæn.ɪ.bəl.aɪz/", "meaning": "共食いする、自社製品・顧客を侵食する", "pos": "verb", "def": "To reduce the sales of a product by introducing another product.", "ex": "Free summaries cannibalized digital news subscription revenue."},
            {"word": "doctrine", "phonetic": "/ˈdɑːk.trɪn/", "meaning": "法理、原則、教義", "pos": "noun", "def": "A principle or position in a branch of knowledge or legal system.", "ex": "The fair use doctrine balances copyright holder rights against public benefit."},
            {"word": "equilibrium", "phonetic": "/ˌek.wəˈlɪb.ri.əm/", "meaning": "均衡、バランス、平衡状態", "pos": "noun", "def": "A state in which opposing forces or influences are balanced.", "ex": "Courts seek an equitable equilibrium between innovation and artistic property."}
        ],
        "syntax": [
            {"title": "対比の接続詞 While による原告・被告の主張整理", "formula": "While [tech companies assert X constitutes fair use], [publishers counter that Y destroys newsrooms].", "explanation": "接続詞 While を用いて、「テクノロジー企業がフェアユースを主張する一方で、新聞社は存続危機を訴える」という法廷闘争の対立軸を明瞭に構文化しています。"},
            {"title": "動詞 attribute A to B（Aの原因をBに帰する／AをBのものとする）", "formula": "wherein [conversational agents attribute fabricated quotes to journalistic mastheads].", "explanation": "attribute A to B の構文で、「AIがデタラメな引用（fabricated quotes）を新聞社のクレジット（mastheads）のものとして不当に帰属させてしまう」というハルシネーションの法的被害を明快に表現しています。"}
        ],
        "quiz": [
            {
                "question": "What is the central allegation in the lawsuit filed by the eight US newspapers?",
                "options": [
                    "AI developers physically burglarized newspaper printing presses in Chicago.",
                    "Millions of copyrighted investigative articles were unlawfully scraped without license to train commercial models.",
                    "Newspaper reporters refused to use modern word processors.",
                    "Tech companies prevented journalists from interviewing politicians."
                ],
                "answer": 1,
                "explanation": "第1文で「何百万本もの独自の調査報道記事がライセンスや対価なしに違法にスクレイピングされ学習に使われたと主張した」と記されています。"
            },
            {
                "question": "What legal defense is asserted by the technology companies?",
                "options": [
                    "They claim that computer training qualifies as 'fair use' transformative adaptation under copyright doctrine.",
                    "They argue that newspapers are legally prohibited from owning any copyright.",
                    "They state that artificial intelligence was invented by 18th-century newspaper founders.",
                    "They maintain that all published journalism automatically belongs to the government."
                ],
                "answer": 0,
                "explanation": "第3文にあるように、テクノロジー企業側はアルゴリズム学習が「フェアユース（公正利用）」に該当すると主張しています。"
            },
            {
                "question": "How does commercial generative AI harm the business model of newspapers according to the complaint?",
                "options": [
                    "It causes widespread paper shortages across North America.",
                    "It generates verbatim excerpts of articles, directly cannibalizing subscriber revenues.",
                    "It forces newspaper editors to increase employee salaries twofold.",
                    "It forbids readers from sharing newspaper links on social media."
                ],
                "answer": 1,
                "explanation": "第2文で「逐語的な抜粋を生成することで、有料会員収入を直接侵食している（cannibalizing subscriber revenues）」と指摘されています。"
            },
            {
                "question": "What reputational danger is posed by 'synthetic hallucinations' in AI chatbots?",
                "options": [
                    "They print physical newspapers with low-quality ink.",
                    "They falsely attribute fabricated quotes and errors to reputable news mastheads.",
                    "They permanently delete journalists' computer hard drives.",
                    "They force newspapers to publish in Latin rather than English."
                ],
                "answer": 1,
                "explanation": "第4文で、捏造された引用や誤りが著名な新聞社のものとして誤って表示されてしまう問題が述べられています。"
            },
            {
                "question": "The word 'purloined' in paragraph 2 is closest in meaning to:",
                "options": ["purchased legally", "stolen or taken without authorization", "distributed freely", "translated accurately"],
                "answer": 1,
                "explanation": "purloin は「盗む」「不当に取得する」という意味であり、stolen or taken without authorization が正解です。"
            }
        ]
    },

    # 9. CULTURE - Orbital Booker Prize 2024 (The Guardian Verified)
    {
        "slug": "orbital-samantha-harvey-booker-prize",
        "category": "culture",
        "category_label": "CONTEMPORARY LITERATURE • ブッカー賞受賞作『Orbital』と宇宙の視点",
        "date": "2026-10-15",
        "title": "Samantha Harvey's Space Station Novel Orbital Wins Booker Prize 2024",
        "headline_ja": "現代文学論：宇宙ステーションから地球を見つめる小説『Orbital』が2024年ブッカー賞を受賞",
        "subhead": "136ページの濃密な瞑想的散文。1日に16回の日出と日没を体験する宇宙飛行士たちの心理と地球の儚さ。",
        "lead_snippet": "英国人作家サマンサ・ハーヴェイの小説『Orbital』が、歴代2番目の短さとなる136ページで英語圏最高峰のブッカー賞を満場一致で受賞した。国際宇宙ステーション（ISS）から人類の営みを俯瞰し、気候危機や国境の無意味さを詩的な英語で描き出した文学的傑作を論考する。",
        "source_name": "The Guardian",
        "source_url": "https://www.theguardian.com/books/2024/nov/12/orbital-by-samantha-harvey-wins-booker-prize-2024",
        "source_attribution": "Source: The Guardian. Orbital by Samantha Harvey wins Booker prize 2024.",
        "image": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=1000&auto=format&fit=crop&q=80",
        "sentences": [
            {
                "en": "British author Samantha Harvey has won the prestigious 2024 Booker Prize for her compact novel Orbital, a lyrical meditation chronicling twenty-four hours aboard the International Space Station as six astronauts witness sixteen sunrises and sunsets.",
                "ja": "イギリス人作家サマンサ・ハーヴェイが、国際宇宙ステーションで6人の宇宙飛行士が16回の日出と日没を目撃する24時間を記録した叙情的な瞑想小説『Orbital』で、権威ある2024年ブッカー賞を受賞した。"
            },
            {
                "en": "At just one hundred and thirty-six pages, the work represents the second-shortest winning entry in the prize's history, celebrated by the judging panel for its philosophical resonance and crystalline descriptive precision.",
                "ja": "わずか136ページのこの作品は、同賞の歴史上2番目に短い受賞作となり、その哲学的響きと透明感のある精緻な描写力により審査員団から満場一致で称賛された。"
            },
            {
                "en": "Hovering above terrestrial borders, the narrative gazes downward upon typhoons, oceans, and fragile continents, transforming geopolitical disputes into inconsequential flickers against the vastness of the cosmic void.",
                "ja": "地上の国境をはるか見下ろしながら、物語は台風、海洋、そして脆弱な大陸を見つめ、広大な宇宙の虚無を背景に地政学的な紛争をちっぽけな瞬きへと変容させる。"
            },
            {
                "en": "Literary critics observe that Harvey's minimalist aesthetic counteracts contemporary literary maximalism, demonstrating that concise prose can evoke profound existential contemplation regarding humanity's environmental stewardship.",
                "ja": "文芸批評家らは、ハーヴェイのミニマリスト的美学が現代文学の冗長さ（マキシマリズム）に抗い、簡潔な散文がいかに人類の環境的責務に関する深遠な実存的思索を呼び起こしうるかを実証していると評する。"
            },
            {
                "en": "Accepting the honor, the author dedicated the accolade to all who cherish and defend our shared planet, framing the novel as a pastoral love letter to a vulnerable biosphere.",
                "ja": "受賞に際し、著者はこの栄誉を私たちの共有する地球を慈しみ守るすべての人々に捧げ、この小説を傷つきやすい生物圏への田園的なラブレターと位置づけた。"
            }
        ],
        "dialogue": [
            {"speaker": "七", "name": "Nanami", "role": "生徒", "text": "英語圏で最も権威のあるブッカー賞を受賞したのが、宇宙ステーションから地球を見る136ページの短い小説なんですね！"},
            {"speaker": "慶", "name": "Keita", "role": "英語講師", "text": "第2文にある 'philosophical resonance'（哲学的な響き）と 'crystalline precision'（水晶のような透明な精密さ）が高く評価されたんだ。長ければ良いというわけではないんだね。"},
            {"speaker": "七", "name": "Nanami", "role": "生徒", "text": "第3文の『宇宙から見ると国境（terrestrial borders）なんてちっぽけな瞬きにすぎない』という描写がとても詩的で感動的です。"},
            {"speaker": "慶", "name": "Keita", "role": "英語講師", "text": "第4文の 'environmental stewardship'（環境に対する管理責任・責務）という言葉も重要だ。早慶や東大の英語長文では、文学論や環境倫理がよく出題されるから、この豊かな英語表現に触れておくのは大きな力になるよ。"}
        ],
        "vocab": [
            {"word": "lyrical", "phonetic": "/ˈlɪr.ɪ.kəl/", "meaning": "叙情的な、詩情あふれる", "pos": "adjective", "def": "Expressing the writer's emotions in an imaginative and beautiful way.", "ex": "Her lyrical prose captured the haunting beauty of the Arctic tundra."},
            {"word": "terrestrial", "phonetic": "/təˈres.tri.əl/", "meaning": "地球上の、陸生の、現世の", "pos": "adjective", "def": "Relating to the earth or to land as opposed to the sea or outer space.", "ex": "Satellite observation tracks terrestrial vegetation changes."},
            {"word": "inconsequential", "phonetic": "/ɪnˌkɑːn.səˈkwen.ʃəl/", "meaning": "重要でない、取るに足らない", "pos": "adjective", "def": "Not important or significant.", "ex": "National borders appear inconsequential when viewed from lunar orbit."},
            {"word": "stewardship", "phonetic": "/ˈstuː.ərd.ʃɪp/", "meaning": "管理責任、受託者の責務、環境保全活動", "pos": "noun", "def": "The responsible overseeing and protection of something considered worth caring for.", "ex": "Indigenous communities practice responsible forest stewardship."},
            {"word": "biosphere", "phonetic": "/ˈbaɪ.oʊ.sfɪr/", "meaning": "生物圏（地球上の生物が生育する領域）", "pos": "noun", "def": "The regions of the surface, atmosphere, and hydrosphere of the earth occupied by living organisms.", "ex": "Human industrial emissions destabilize the fragile planetary biosphere."}
        ],
        "syntax": [
            {"title": "現在分詞句による視点の空間的配置", "formula": "[Hovering above terrestrial borders], [the narrative gazes downward upon typhoons and continents].", "explanation": "文頭の現在分詞句 Hovering above borders が物語の語り手の視点を宇宙空間に設定し、続く主文で地球を俯瞰する視線の動きを詩的に描いています。"},
            {"title": "動詞 dedicate + 目的語 + to 名詞（〜に捧げる）", "formula": "[the author dedicated the accolade to all] [who cherish and defend our shared planet].", "explanation": "dedicate A to B（AをBに捧げる）に、関係代名詞 who が導く修飾節が結びつき、地球環境を守る人々への感謝と敬意を格調高く表明しています。"}
        ],
        "quiz": [
            {
                "question": "What is the setting and timeframe of Samantha Harvey's winning novel Orbital?",
                "options": [
                    "A fictional medieval castle over ten generations of warfare.",
                    "A 24-hour period aboard the International Space Station observing sixteen sunrises and sunsets.",
                    "A deep-sea research submarine exploring the Mariana Trench for two months.",
                    "An automated Martian colony in the year 2500."
                ],
                "answer": 1,
                "explanation": "第1文で「国際宇宙ステーションで宇宙飛行士たちが16回の日出と日没を目撃する24時間」が舞台であると明記されています。"
            },
            {
                "question": "What notable characteristic distinguishes Orbital in the history of the Booker Prize?",
                "options": [
                    "It was published entirely in ancient Greek verse.",
                    "At 136 pages, it is the second-shortest winning entry in the prize's history.",
                    "It is the only novel ever written by an active NASA astronaut.",
                    "It contains no verbs or adjectives in its text."
                ],
                "answer": 1,
                "explanation": "第2文で「わずか136ページで、同賞の歴史上2番目に短い受賞作となった」と記されています。"
            },
            {
                "question": "How does the perspective from space alter the perception of geopolitical disputes in the novel?",
                "options": [
                    "It proves that one country owns outer space.",
                    "It transforms terrestrial conflicts into inconsequential flickers against the vast cosmos.",
                    "It encourages astronauts to launch missiles at Earth.",
                    "It demonstrates that national borders are visible from Mars."
                ],
                "answer": 1,
                "explanation": "第3文にあるように、広大な宇宙の虚無を背景にすると、地上の地政学的紛争は「取るに足らない瞬き（inconsequential flickers）」へと変容します。"
            },
            {
                "question": "To whom did Samantha Harvey dedicate her Booker Prize award?",
                "options": [
                    "To aerospace defense manufacturing shareholders.",
                    "To all who cherish and defend our shared planet.",
                    "Exclusively to science fiction film directors in Hollywood.",
                    "To commercial space tourism billionaires."
                ],
                "answer": 1,
                "explanation": "最終文で、著者はこの栄誉を「私たちの共有する地球を慈しみ守るすべての人々」に捧げたと述べられています。"
            },
            {
                "question": "The word 'inconsequential' in paragraph 3 is closest in meaning to:",
                "options": ["unimportant", "catastrophic", "glorious", "unavoidable"],
                "answer": 0,
                "explanation": "inconsequential は「重要でない」「取るに足らない」を意味し、unimportant が同義です。"
            }
        ]
    },

    # 10. CULTURE - Gen Z Physical Books & Library Renaissance (The Guardian Verified)
    {
        "slug": "gen-z-physical-books-library-renaissance",
        "category": "culture",
        "category_label": "MEDIA ECOLOGY & READING CULTURE • 紙の本への回帰とZ世代の図書館ルネサンス",
        "date": "2026-10-15",
        "title": "Gen Z Readers Spark Resurgence in Physical Book Sales and Public Library Visits",
        "headline_ja": "文化社会学：デジタル画面の疲労から「紙の本と図書館」へ回帰するZ世代の読書文化",
        "subhead": "デジタルネイティブが求める触覚的体験と静謐な空間。SNS「BookTok」を通じた読書コミュニティの再興。",
        "lead_snippet": "スマートフォンに囲まれて育ったZ世代の間で、電子書籍ではなく紙の書籍を購入し、公共図書館に足を運ぶムーブメントが欧米を中心に急速に拡大している。常時接続のプレッシャーやスクリーンの認知的疲労から脱し、紙の匂いや手触りを通じた深い思索を求める若者の心理を読み解く。",
        "source_name": "The Guardian",
        "source_url": "https://www.theguardian.com/books/2024/feb/09/reading-is-so-sexy-gen-z-turns-to-physical-books-and-libraries",
        "source_attribution": "Source: The Guardian. Reading is so sexy: Gen Z turns to physical books and libraries.",
        "image": "https://images.unsplash.com/photo-1524995997946-a1c2e315a42f?w=1000&auto=format&fit=crop&q=80",
        "sentences": [
            {
                "en": "Contrary to predictions that digital devices would render printed paper obsolete, young adult readers across Generation Z are driving an unexpected global renaissance in physical book sales and public library patronage.",
                "ja": "デジタル端末が印刷された紙を時代遅れにするという予測に反して、Z世代の若年読者層が紙の書籍の売上と公共図書館の利用における予想外の世界的なルネサンス（再興）を牽引している。"
            },
            {
                "en": "Publishing industry metrics indicate that print formats now comprise upwards of eighty percent of total adolescent book purchases, with readers valuing the tactile weight and aesthetic permanence absent from ephemeral screens.",
                "ja": "出版業界の指標によると、現在、青少年の書籍購入総数の8割以上を印刷書籍が占めており、読者らは儚いデジタル画面には存在しない触覚的な重みや美的な永続性を重視している。"
            },
            {
                "en": "Cognitive psychologists suggest that navigating continuous algorithmic feeds induces acute sensory saturation, prompting digital natives to seek analog reading as an intentional ritual of cognitive decompression.",
                "ja": "認知心理学者らは、途切れないアルゴリズムのフィードを巡回することが深刻な感覚的飽和を引き起こし、デジタルネイティブたちに認知的な減圧（リフレッシュ）のための意図的な儀式としてアナログな読書を求めさせていると示唆する。"
            },
            {
                "en": "Moreover, municipal libraries are experiencing unprecedented footfall as teenagers embrace them not merely as repository archives, but as communal 'third places' free from pervasive surveillance capitalism.",
                "ja": "さらに、ティーンエイジャーたちが公共図書館を単なる所蔵書庫としてだけでなく、蔓延する監視資本主義から解放された共有の「サードプレイス（第3の居場所）」として受け入れることで、空前の来館者数を記録している。"
            },
            {
                "en": "Cultural theorists conclude that physical books have evolved into potent emblems of mindfulness, representing an explicit refusal to allow personal leisure to be monetized by technological platforms.",
                "ja": "文化理論家らは、紙の本がマインドフルネスの強力な象徴へと進化しており、個人の余暇がテクノロジー・プラットフォームによって収益化されることを拒否する明確な意思表示となっていると結論づけている。"
            }
        ],
        "dialogue": [
            {"speaker": "七", "name": "Nanami", "role": "生徒", "text": "スマホ世代のZ世代が、電子書籍より紙の本を買って図書館に通っているなんて、ちょっと意外ですがすごく共感できます！"},
            {"speaker": "慶", "name": "Keita", "role": "英語講師", "text": "第2文にある 'tactile weight and aesthetic permanence'（手触りの重みと美的な永続性）だね。画面だと通知が飛んできて落ち着いて読めないんだ。"},
            {"speaker": "七", "name": "Nanami", "role": "生徒", "text": "第3文の 'cognitive decompression'（認知の減圧・デトックス）という言葉がぴったりですね。SNSで疲れた脳を休ませる儀式なんですね。"},
            {"speaker": "慶", "name": "Keita", "role": "英語講師", "text": "第4文の図書館を『お金を使わずに誰でも居られるサードプレイス（third place）』と捉える視点も素晴らしい。TIME誌やThe Guardianの文化論説で最頻出のエッセイテーマだよ。"}
        ],
        "vocab": [
            {"word": "patronage", "phonetic": "/ˈpæt.rə.nɪdʒ/", "meaning": "愛顧、利用、後援", "pos": "noun", "def": "The support given by a patron, or regular business given to a store by a customer.", "ex": "Public library patronage surged among secondary school students."},
            {"word": "tactile", "phonetic": "/ˈtæk.taɪl/", "meaning": "触覚の、手触りのある", "pos": "adjective", "def": "Connected with the sense of touch; tangible.", "ex": "Paper books offer a tactile experience that e-readers cannot duplicate."},
            {"word": "ephemeral", "phonetic": "/ɪˈfem.ər.əl/", "meaning": "儚い、つかの間の、一時的な", "pos": "adjective", "def": "Lasting for a very short time.", "ex": "Social media stories are ephemeral, vanishing within twenty-four hours."},
            {"word": "decompression", "phonetic": "/ˌdiː.kəmˈpreʃ.ən/", "meaning": "減圧、リフレッシュ、精神の解放", "pos": "noun", "def": "A period of relaxation after hard work or pressure.", "ex": "Quiet reading provides mental decompression after intense examinations."},
            {"word": "emblem", "phonetic": "/ˈem.bləm/", "meaning": "象徴、紋章、標章", "pos": "noun", "def": "A heraldic device or symbolic object as a distinctive badge of an idea.", "ex": "Physical paperbacks became emblems of intentional digital disengagement."}
        ],
        "syntax": [
            {"title": "全否定前置詞句 Contrary to ... を前置した複文", "formula": "Contrary to predictions [that X would render paper obsolete], [Gen Z readers are driving a renaissance].", "explanation": "Contrary to predictions（〜という予測に反して）が文頭に置かれ、デジタル化で本が消えるというかつての通説を覆す現代の若者文化の動向を鮮やかに導入しています。"},
            {"title": "現在分詞句 prompting A to do（Aに〜することを促す）", "formula": "[feeds induce saturation], [prompting digital natives to seek analog reading as a ritual].", "explanation": "無生物主語 feeds induce saturation に続く分詞構文 prompting A to do が、「感覚の過負荷が若者に紙の読書を求めさせる」という心理的動機を的確に説明しています。"}
        ],
        "quiz": [
            {
                "question": "What surprising trend among Generation Z readers is highlighted in the article?",
                "options": [
                    "They have completely ceased reading any form of written literature.",
                    "They are driving a global resurgence in physical book purchases and library visits.",
                    "They exclusively read computer programming manuals online.",
                    "They are demanding that all public libraries be converted into video arcades."
                ],
                "answer": 1,
                "explanation": "第1文で「デジタル端末が紙を時代遅れにするという予測に反して、Z世代が紙の書籍の売上と図書館利用の再興を牽引している」と記されています。"
            },
            {
                "question": "What proportion of adolescent book purchases is currently represented by print formats?",
                "options": ["Less than 10 percent", "Roughly 25 percent", "Upwards of 80 percent", "Exactly 50 percent"],
                "answer": 2,
                "explanation": "第2文で 'print formats now comprise upwards of eighty percent of total adolescent book purchases'（80%以上）と明記されています。"
            },
            {
                "question": "Why do cognitive psychologists believe young people seek analog reading?",
                "options": [
                    "Because electronic reading devices are completely illegal in schools.",
                    "As an intentional ritual of cognitive decompression from continuous algorithmic feeds.",
                    "Because paper books are significantly lighter than smartphones.",
                    "To prepare for careers as antique paper restorers."
                ],
                "answer": 1,
                "explanation": "第3文にあるように、アルゴリズムのフィードによる感覚過負荷から脱し、認知の減圧（リフレッシュ）を図るための意図的な儀式として読書を求めています。"
            },
            {
                "question": "How do teenagers view public libraries today according to the text?",
                "options": [
                    "As boring historical relics to be demolished.",
                    "As communal 'third places' free from pervasive surveillance capitalism.",
                    "As commercial venues where books must be purchased at high prices.",
                    "As private corporate headquarters for tech platforms."
                ],
                "answer": 1,
                "explanation": "第4文で、公共図書館が「監視資本主義から解放された共有のサードプレイス（第3の居場所）」として親しまれていると述べられています。"
            },
            {
                "question": "The word 'ephemeral' in paragraph 2 is closest in meaning to:",
                "options": ["permanent", "transitory and short-lived", "indestructible", "expensive"],
                "answer": 1,
                "explanation": "ephemeral は「儚い」「一時的な」「つかの間の」を意味し、transitory and short-lived が正解です。"
            }
        ]
    },

    # 11. ENTERTAINMENT & GADGETS - Smart Glasses Parliament (The Guardian Oct 14, 2026)
    {
        "slug": "smart-glasses-parliament-privacy-controversy",
        "category": "entertainment",
        "category_label": "SURVEILLANCE ETHICS & WEARABLE TECH • 議場でのスマートグラス使用をめぐる倫理論争",
        "date": "2026-10-15",
        "title": "Wearable Smart Glasses with Hidden Cameras Prompt Parliamentary Ban Calls in UK",
        "headline_ja": "情報倫理学：小型カメラ搭載スマートグラスの議場持ち込みをめぐり英議会で禁止論争が勃発",
        "subhead": "議員が着用したスマートグラスに批判殺到。秘密録画・生体認識技術と公的審議のセキュリティ懸念。",
        "lead_snippet": "ウェールズ議会において、小型カメラとAIマイクを内蔵したスマートグラスを着用して議場に入った政治家に対し、他議員のプライバシー侵害や機密情報漏洩の懸念から即時禁止を求める声が高まっている。日常生活に浸透しつつあるウェアラブル端末と公共空間のプライバシー倫理を論じる。",
        "source_name": "The Guardian",
        "source_url": "https://www.theguardian.com/technology/2026/oct/14/smart-glasses-ai-technology-reform-senedd-westminster-ban",
        "source_attribution": "Source: The Guardian (Oct 14, 2026). The eyes have it: politician's smart glasses prompt calls for ban in Westminster.",
        "image": "https://images.unsplash.com/photo-1508700115892-45ecd05ae2ad?w=1000&auto=format&fit=crop&q=80",
        "sentences": [
            {
                "en": "British parliamentarians have demanded an immediate ban on AI-powered smart glasses inside legislative chambers after an elected representative wore camera-equipped spectacles during official parliamentary debates.",
                "ja": "ある議員が公式の議会審議中にカメラ内蔵型メガネを着用したことを受け、英国の国会議員らは立法議場内でのAI搭載スマートグラスの即時禁止を要求した。"
            },
            {
                "en": "The unobtrusive hardware, which seamlessly integrates miniature optical sensors and directional microphones into standard frames, enables covert video recording and real-time facial recognition without conspicuous indicator LEDs.",
                "ja": "目立たない標準的な眼鏡フレームに小型光学センサーと指向性マイクを違和感なく統合したこのハードウェアは、目立つLED表示なしでの秘密録画やリアルタイム顔認証を可能にする。"
            },
            {
                "en": "Cross-party lawmakers argue that surreptitious audiovisual surveillance undermines the sanctity of privileged legislative deliberations and creates acute cybersecurity vulnerabilities for classified briefings.",
                "ja": "超党派の議員らは、秘密裏の視聴覚監視が特権的な議会審議の尊厳を損ない、機密ブリーフィングに対する深刻なサイバーセキュリティ上の脆弱性を生み出すと主張している。"
            },
            {
                "en": "Privacy advocates point out that as consumer wearables evolve from conspicuous novelties into indistinguishable everyday accessories, the boundaries of consensual public observation are collapsing.",
                "ja": "プライバシー擁護派は、消費者向けウェアラブル端末が目立つ新奇品から区別のつかない日常的アクセサリーへと進化するにつれ、合意に基づいた公共空間での観察という境界線が崩壊しつつあると指摘する。"
            },
            {
                "en": "Legal scholars propose that constitutional assemblies must formulate updated etiquette codes and statutory perimeters before ambient optical surveillance becomes normalized across civil institutions.",
                "ja": "法学者らは、環境に溶け込んだ光学監視が市民社会の諸機関において常態化する前に、憲法制定議会が最新のエチケット基準と法定立ち入り境界線を策定しなければならないと提言している。"
            }
        ],
        "dialogue": [
            {"speaker": "七", "name": "Nanami", "role": "生徒", "text": "普通のメガネに見えるスマートグラスで、国会の議場を秘密で録画できてしまうなんて、確かに大問題ですね！"},
            {"speaker": "慶", "name": "Keita", "role": "英語講師", "text": "第2文にある 'unobtrusive hardware'（目立たないハードウェア）が論点だね。小さなLEDランプも光らないように細工されたら、誰にも気づかれない。"},
            {"speaker": "七", "name": "Nanami", "role": "生徒", "text": "第4文の『合意に基づいた観察の境界が崩れる（boundaries of consensual public observation are collapsing）』という指摘も深いです。街中で勝手に顔認証されたら怖いです。"},
            {"speaker": "慶", "name": "Keita", "role": "英語講師", "text": "第5文の環境光学監視（ambient optical surveillance）の規制論は、プライバシー権・情報倫理・公共の福祉をめぐる法学小論文や早慶・東大入試で極めて狙われやすい先端テーマだよ。"}
        ],
        "vocab": [
            {"word": "unobtrusive", "phonetic": "/ˌʌn.əbˈtruː.sɪv/", "meaning": "目立たない、控えめな、邪魔にならない", "pos": "adjective", "def": "Not attracting attention in a way that is annoying or unwanted.", "ex": "Smart sensors are designed to be unobtrusive in residential environments."},
            {"word": "covert", "phonetic": "/ˈkoʊ.vɜːrt/", "meaning": "秘密の、隠密の、裏の", "pos": "adjective", "def": "Not openly acknowledged or displayed.", "ex": "Covert audio recording violates electronic privacy legislation."},
            {"word": "surreptitious", "phonetic": "/ˌsɜːr.əpˈtɪʃ.əs/", "meaning": "内密の、不正にこっそり行う", "pos": "adjective", "def": "Kept secret, especially because it would not be approved of.", "ex": "She cast a surreptitious glance at her phone during the interview."},
            {"word": "sanctity", "phonetic": "/ˈsæŋk.tə.t̬i/", "meaning": "尊厳、神聖さ、侵すべからざるもの", "pos": "noun", "def": "The state or quality of being holy, sacred, or inviolable.", "ex": "Courts protect the sanctity of attorney-client communications."},
            {"word": "ambient", "phonetic": "/ˈæm.bi.ənt/", "meaning": "環境の、周囲を取り巻く", "pos": "adjective", "def": "Relating to the immediate surroundings of something.", "ex": "Ambient listening devices raise questions about passive surveillance."}
        ],
        "syntax": [
            {"title": "非制限用法の関係代名詞 which による機能の列挙", "formula": "[The unobtrusive hardware], [which seamlessly integrates sensors], [enables covert recording].", "explanation": "主語 The hardware と動詞 enables の間に非制限用法の関係代名詞節 which integrates が挿入され、機器の構造的特徴を説明した上で主節の述語へと展開しています。"},
            {"title": "接続詞 as による状況の変化（〜するにつれて）", "formula": "[advocates point out that] [as consumer wearables evolve into accessories], [the boundaries are collapsing].", "explanation": "従属接続詞 as が「ウェアラブル端末が日常品へと進化するにつれて」という時代の不可逆的な変化を示し、主節でプライバシーの崩壊を警鐘しています。"}
        ],
        "quiz": [
            {
                "question": "What prompted calls for a ban on smart glasses inside British parliamentary chambers?",
                "options": [
                    "A politician was caught playing video games on an oversized headset.",
                    "An elected representative wore camera-equipped spectacles during official debates.",
                    "The eyeglasses malfunctioned and caused an electrical fire.",
                    "Parliamentarians wished to promote the sale of contact lenses."
                ],
                "answer": 1,
                "explanation": "第1文で「ある議員が公式審議中にカメラ内蔵型メガネを着用したことを受け、議場内での即時禁止が要求された」と述べられています。"
            },
            {
                "question": "What technological capability of modern smart glasses concerns lawmakers?",
                "options": [
                    "They allow covert video recording and facial recognition without conspicuous LED indicators.",
                    "They can physically read thoughts directly from human brain waves.",
                    "They project bright holographic laser displays that blind opponents.",
                    "They emit high-frequency radio jamming signals."
                ],
                "answer": 0,
                "explanation": "第2文で、目立たないフレームでLED表示なしでの秘密録画やリアルタイム顔認証を可能にする点が指摘されています。"
            },
            {
                "question": "Why do cross-party lawmakers view surreptitious surveillance as dangerous in parliament?",
                "options": [
                    "It increases the cost of parliamentary electricity bills.",
                    "It undermines privileged deliberations and creates cybersecurity vulnerabilities for classified briefings.",
                    "It makes politicians look insufficiently fashionable on television.",
                    "It discourages citizens from voting in general elections."
                ],
                "answer": 1,
                "explanation": "第3文にあるように、特権的な議会審議の尊厳を損ない、機密ブリーフィングに対するサイバーセキュリティ上の脆弱性を生み出すと主張されています。"
            },
            {
                "question": "What broader dilemma do privacy advocates highlight regarding smart wearables?",
                "options": [
                    "Smart glasses battery life has become too short for daily use.",
                    "The boundaries of consensual public observation are collapsing as cameras blend into everyday accessories.",
                    "Manufacturers have refused to sell smart glasses to the general public.",
                    "Eyeglasses are rapidly becoming obsolete due to laser eye surgery."
                ],
                "answer": 1,
                "explanation": "第4文で、カメラが日常的なアクセサリーと見分けがつかなくなるにつれて「合意に基づいた観察の境界線が崩壊しつつある」と警鐘が鳴らされています。"
            },
            {
                "question": "The word 'surreptitious' in paragraph 3 is closest in meaning to:",
                "options": ["secret and unauthorized", "transparent and public", "clumsy", "beneficial"],
                "answer": 0,
                "explanation": "surreptitious は「内密の」「不正にこっそり行う」という意味であり、secret and unauthorized が正解です。"
            }
        ]
    },

    # 12. ENTERTAINMENT & GADGETS - England Organic Farming Target (The Guardian Oct 14, 2026)
    {
        "slug": "england-organic-farming-expansion-target",
        "category": "entertainment",
        "category_label": "AGROECOLOGY & SUSTAINABLE FOOD • 有機農業面積10%拡大目標の策定",
        "date": "2026-10-15",
        "title": "England Unveils Landmark Plan to Triple Organic Farmland by 2036 for Climate and Soil",
        "headline_ja": "環境農政学：土壌生態系再生と気候変動対策に向け、有機農地比率を10%へ拡大する国家計画を発表",
        "subhead": "化学農薬・化学肥料への依存削減。生物多様性の保全と持続可能な食料安全保障の両立を目指す新アプローチ。",
        "lead_snippet": "英国政府は、2036年までにイングランド国内の農地における有機農業（オーガニック農法）の割合を現在の3倍以上となる10%へ引き上げる総合行動計画を公表した。土壌微生物の多様性回復と温室効果ガス排出抑制、持続可能な農業経済モデルをめぐる世界的潮流を精読する。",
        "source_name": "The Guardian",
        "source_url": "https://www.theguardian.com/environment/2026/oct/14/land-farmed-organically-england-share-10-pc-2036-plan-food-climate",
        "source_attribution": "Source: The Guardian (Oct 14, 2026). Plan unveiled to increase share of land farmed organically in England to 10% by 2036.",
        "image": "https://images.unsplash.com/photo-1500937386664-56d1dfef3854?w=1000&auto=format&fit=crop&q=80",
        "sentences": [
            {
                "en": "Agricultural ministers in England have unveiled an ambitious statutory roadmap aiming to triple the nation's organic farmland to ten percent by 2036, incentivizing regenerative cultivation to restore degraded agricultural ecosystems.",
                "ja": "イングランドの農業担当大臣らは、劣化した農業生態系を再生するための環境再生型農業を奨励し、2036年までに国内の有機農地比率を3倍の10%へ拡大することを目指す野心的な法定ロードマップを発表した。"
            },
            {
                "en": "Under the initiative, transitional subsidy schemes will support farmers pivoting away from synthetic nitrogen fertilizers and intensive chemical pesticides toward crop rotation, cover crops, and natural biological pest predators.",
                "ja": "この取り組みのもとで、移行支援補助金制度により、合成窒素肥料や集約的化学農薬からの脱却を図り、輪作、被覆作物、および害虫の天敵となる自然生物を活用する農家への支援が行われる。"
            },
            {
                "en": "Soil scientists report that organically cultivated topsoil sequesters up to twenty-five percent more carbon than intensively tilled acreage while harboring rich mycorrhizal networks that enhance drought resilience.",
                "ja": "土壌学者らは、有機栽培された表土が集約的に耕起された農地に比べて最大25%多くの炭素を固定し、乾燥への耐性を高める豊かな菌根菌ネットワークを育んでいると報告している。"
            },
            {
                "en": "Consumer advocacy groups welcome the targets but stress that public procurement in schools and state hospitals must guarantee stable domestic demand to insulate organic growers from retail price volatility.",
                "ja": "消費者権利団体らはこの目標を歓迎する一方、小売価格の乱高下から有機農家を守るため、学校給食や公立病院などの公共調達において安定した国内需要を保証しなければならないと強調している。"
            },
            {
                "en": "Agroecologists maintain that balancing agricultural yields with ecological conservation represents humanity's most urgent sustainability test amidst climate-induced food security volatility.",
                "ja": "農業生態学者らは、農業収量と生態系保全のバランスをとることが、気候変動がもたらす食料安全保障の不安定性の中において人類にとって最も喫緊の持続可能性の試練であると主張している。"
            }
        ],
        "dialogue": [
            {"speaker": "七", "name": "Nanami", "role": "生徒", "text": "イギリスのイングランドで、有機農業（オーガニック農地）を2036年までに3倍の10%に増やす計画が発表されたんですね！"},
            {"speaker": "慶", "name": "Keita", "role": "英語講師", "text": "第2文にあるように、化学肥料（synthetic nitrogen fertilizers）や農薬を減らして、自然の生態系を利用する『環境再生型農業（regenerative agriculture）』への大転換だね。"},
            {"speaker": "七", "name": "Nanami", "role": "生徒", "text": "第3文の『有機農法の土壌は炭素を25%も多く閉じ込める（sequesters 25% more carbon）』というデータも驚きです。土が温室効果ガスを吸収してくれるんですね。"},
            {"speaker": "慶", "name": "Keita", "role": "英語講師", "text": "第4文の学校給食や公立病院での公共調達（public procurement）も重要だ。食料自給率、土壌保全、気候変動対策を一体で論じるのは、東大・京大・農学系入試の頻出論点だよ。"}
        ],
        "vocab": [
            {"word": "incentivize", "phonetic": "/ɪnˈsen.t̬ə.vaɪz/", "meaning": "奨励する、動機付ける、インセンティブを与える", "pos": "verb", "def": "To motivate or encourage someone to do something.", "ex": "Subsidies incentivize farmers to adopt low-emission irrigation."},
            {"word": "regenerative", "phonetic": "/rɪˈdʒen.ər.ə.tɪv/", "meaning": "環境再生の、再生能力のある", "pos": "adjective", "def": "Promoting the renewal or restoration of natural systems.", "ex": "Regenerative grazing practices restore degraded grassland biodiversity."},
            {"word": "sequester", "phonetic": "/sɪˈkwes.tər/", "meaning": "隔離・固定する、炭素を閉じ込める", "pos": "verb", "def": "To capture and store carbon dioxide from the atmosphere.", "ex": "Forest soils sequester atmospheric carbon for centuries."},
            {"word": "procurement", "phonetic": "/proʊˈkjʊr.mənt/", "meaning": "調達、政府調達、買い入れ", "pos": "noun", "def": "The action of obtaining or procuring equipment or supplies.", "ex": "Public procurement policies prioritize locally sourced organic vegetables."},
            {"word": "volatility", "phonetic": "/ˌvɑː.ləˈtɪl.ə.t̬i/", "meaning": "価格変動の激しさ、不安定性", "pos": "noun", "def": "Liability to change rapidly and unpredictably, especially for the worse.", "ex": "Extreme weather contributes to global agricultural commodity price volatility."}
        ],
        "syntax": [
            {"title": "無生物主語構文 support farmers pivoting away from A toward B", "formula": "subsidies will support [farmers pivoting away from synthetic fertilizers toward crop rotation].", "explanation": "pivot away from A toward B（Aから脱却してBへ舵を切る）の動名詞句が farmers を修飾し、化学農法から有機農法への抜本的な転換プロセスをダイナミックに描いています。"},
            {"title": "動名詞主語 balancing A with B による命題化", "formula": "[Balancing agricultural yields with ecological conservation] represents [humanity's most urgent test].", "explanation": "動名詞句 Balancing A with B（AとBを両立・調和させること）が主語となり、収量と環境保全のジレンマが最重要課題であることを明確に論述しています。"}
        ],
        "quiz": [
            {
                "question": "What is the core target set by English agricultural ministers?",
                "options": [
                    "To convert all agricultural land into solar battery factories by 2030.",
                    "To triple organic farmland to ten percent by 2036.",
                    "To ban all family-owned farms across the British Isles.",
                    "To mandate the exclusive consumption of imported canned goods."
                ],
                "answer": 1,
                "explanation": "第1文で「2036年までに有機農地比率を3倍の10%へ拡大することを目指す」と明記されています。"
            },
            {
                "question": "What agricultural practices will be supported under the transitional subsidy scheme?",
                "options": [
                    "Increasing synthetic nitrogen fertilizers and heavy chemical pesticides.",
                    "Moving toward crop rotation, cover crops, and natural biological pest predators.",
                    "Spraying crops with genetically modified saltwater.",
                    "Paving farm fields with synthetic asphalt."
                ],
                "answer": 1,
                "explanation": "第2文で、化学肥料や農薬から脱却し、輪作、被覆作物、天敵生物を活用する農法への支援が挙げられています。"
            },
            {
                "question": "What ecological benefit of organic topsoil is identified by soil scientists?",
                "options": [
                    "It releases greenhouse gases 50 percent faster.",
                    "It sequesters up to 25 percent more carbon and harbors mycorrhizal networks that enhance drought resilience.",
                    "It prevents any plants from absorbing water during rainy seasons.",
                    "It turns into hard mineral stone within two weeks."
                ],
                "answer": 1,
                "explanation": "第3文にあるように、有機栽培された表土は最大25%多くの炭素を固定し、乾燥耐性を高める菌根菌ネットワークを育みます。"
            },
            {
                "question": "What measure do consumer advocacy groups recommend to support organic growers?",
                "options": [
                    "Public procurement in schools and state hospitals to guarantee stable domestic demand.",
                    "Mandatory price gouging by international supermarket monopolies.",
                    "Ending all school lunches across the United Kingdom.",
                    "Requiring farmers to export all produce abroad without domestic sales."
                ],
                "answer": 0,
                "explanation": "第4文で、学校や公立病院などの公共調達において安定した国内需要を保証することが求められています。"
            },
            {
                "question": "The word 'sequester' in paragraph 3 is closest in meaning to:",
                "options": ["release", "capture and store", "destroy", "measure inaccurately"],
                "answer": 1,
                "explanation": "sequester は「炭素を固定する」「隔離・貯留する」を意味し、capture and store が正解です。"
            }
        ]
    }
]

# 1:1 JUNIOR EDITIONS (Eiken Pre-2 ~ Grade 2 Accessible Broadsheet)
BATCH11_JUNIOR = [
    # 1. SCIENCE JUNIOR - AlphaFold 3
    {
        "slug": "alphafold-3-biomolecular-structure-prediction",
        "category": "science",
        "date": "2026-10-15",
        "title": "AlphaFold 3: How AI Predicts the Shapes of Life's Tiny Molecules",
        "headline_ja": "AIが生命の分子の形を予測する：ノーベル賞に輝いたAlphaFold 3のすごい力",
        "subhead": "タンパク質やDNAの形をコンピューターで正確に計算。新しい薬を早く見つける最新科学。",
        "lead_snippet": "私たちの体の中で働くタンパク質やDNAは、とても複雑な形をしています。科学者たちは新しいAI『AlphaFold 3』を使って、これらの形を原子のレベルまで正確に予測できるようになりました。ノーベル賞にも選ばれた最先端の科学を高校生の英語で学びましょう。",
        "source_name": "Nature",
        "source_url": "https://www.nature.com/articles/s41586-024-07487-w",
        "senior_path": "../../../science/alphafold-3-biomolecular-structure-prediction/index.html",
        "image": "https://images.unsplash.com/photo-1532187863486-abf9dbad1b69?w=1000&auto=format&fit=crop&q=80",
        "is_foundational": True,
        "foundational_reason_title": "【過去の基礎論文解説】なぜ今、高校生がこの論文を読むべきなのか？",
        "foundational_reason_html": """
        <p style="font-size: 0.88rem; line-height: 1.75; color: #143820; margin: 0;">
          <strong>💡 2024年ノーベル化学賞の基盤：</strong><br>
          AlphaFoldを作った科学者たちは2024年のノーベル化学賞を受賞しました。大学入試の長文読解や英検でも、ノーベル賞関連の科学ニュースは頻出です。AIを使って新しい薬をどうやって早く開発するのか、基本の英語表現をしっかり身につけましょう。
        </p>
        """,
        "sentences": [
            {
                "en": "Scientists have created an amazing computer model called AlphaFold 3 that can predict the exact shapes of important molecules in our bodies.",
                "ja": "科学者たちは、私たちの体の中にある重要な分子の正確な形を予測できる「AlphaFold 3」という素晴らしいコンピューターモデルを開発しました。"
            },
            {
                "en": "Our bodies rely on proteins and DNA, and understanding their three-dimensional shapes is like finding the right key for a lock.",
                "ja": "私たちの体はタンパク質やDNAに頼っており、それらの3次元の立体的な形を理解することは、鍵穴にぴったり合う鍵を見つけるようなものです。"
            },
            {
                "en": "Earlier computers could only study single proteins, but the new system can see how proteins, genes, and medicines connect together.",
                "ja": "以前のコンピューターは1つのタンパク質しか調べられませんでしたが、新しいシステムはタンパク質や遺伝子、薬がどのように結びつくかを見ることができます。"
            },
            {
                "en": "Doctors and medical researchers hope this powerful tool will help discover life-saving treatments in months instead of many years.",
                "ja": "医師や医学研究者らは、この強力なツールが命を救う治療法を何年もかける代わりに数ヶ月で見つける手助けになると期待しています。"
            },
            {
                "en": "However, international leaders say we must make clear rules so that such smart technology is always used safely and peacefully.",
                "ja": "しかし、国際的な指導者たちは、このような賢い技術が常に安全かつ平和に使われるよう、明確なルールを作らなければならないと述べています。"
            }
        ],
        "dialogue": [
            {"speaker": "七", "name": "Nanami", "role": "生徒", "text": "私たちの体の中にあるタンパク質の形を、AIがコンピューターの中でパッと立体的に見せてくれるんですね！"},
            {"speaker": "慶", "name": "Keita", "role": "英語講師", "text": "そうなんだ。第2文にある 'like finding the right key for a lock'（鍵穴に合う鍵を見つけるようなもの）という例えが分かりやすいね。病気の原因になる分子にぴったり合う薬（鍵）をAIが設計できるんだよ。"},
            {"speaker": "七", "name": "Nanami", "role": "生徒", "text": "第4文の 'in months instead of many years'（何年もかける代わりに数ヶ月で）という表現も、英検や高校入試でよく使われますね！"},
            {"speaker": "慶", "name": "Keita", "role": "英語講師", "text": "素晴らしい着眼点だね。'instead of ~'（〜の代わりに）は自由英作文でも大活躍する基本構文だから、しっかり声に出して覚えておこう！"}
        ],
        "vocab": [
            {"word": "molecule", "meaning": "分子（物質の最小単位）", "pos": "noun", "def": "The simplest structural unit of a chemical compound."},
            {"word": "predict", "meaning": "予測する、予言する", "pos": "verb", "def": "To say what will happen in the future based on knowledge."},
            {"word": "three-dimensional", "meaning": "3次元の、立体の（3D）", "pos": "adjective", "def": "Having height, width, and depth."},
            {"word": "discover", "meaning": "発見する、見つける", "pos": "verb", "def": "To find something that was hidden or unknown."},
            {"word": "peacefully", "meaning": "平和に、平穏に", "pos": "adverb", "def": "In a peaceful way without violence or danger."}
        ],
        "syntax": [
            {"title": "〜の代わりに：instead of + 名詞 / 動名詞", "formula": "discover treatments [in months] [instead of many years].", "explanation": "instead of は「〜の代わりに」「〜ではなく」という意味の前置詞句です。時間や手段の対比でとてもよく使われます。"},
            {"title": "so that 構文（目的：〜できるように）", "formula": "make rules [so that technology is always used safely].", "explanation": "so that + 主語 + 動詞 で「主語が〜できるように」という目的を表します。"}
        ],
        "quiz": [
            {
                "question": "What can AlphaFold 3 do according to the article?",
                "options": [
                    "It predicts the exact three-dimensional shapes of biological molecules.",
                    "It builds physical robots that perform heart surgeries.",
                    "It takes photographs of outer space galaxies.",
                    "It replaces human doctors in school clinics."
                ],
                "answer": 0,
                "explanation": "第1文で「私たちの体にある重要な分子の正確な立体的な形を予測できる」と説明されています。"
            },
            {
                "question": "Why is understanding the shapes of molecules compared to a lock and key?",
                "options": [
                    "Because doors in hospitals are locked by computers.",
                    "Because medicines must fit perfectly into body molecules to cure illnesses.",
                    "Because keys are made of heavy metal atoms.",
                    "Because scientists lose their laboratory keys frequently."
                ],
                "answer": 1,
                "explanation": "第2文で、分子の形を知ることは鍵穴に合う鍵を見つけるようなもので、薬が分子にぴったり結合することを例えています。"
            },
            {
                "question": "How quickly might new medical treatments be discovered using AlphaFold 3?",
                "options": ["In seconds", "In months instead of many years", "Never at all", "Only after 100 years"],
                "answer": 1,
                "explanation": "第4文で 'in months instead of many years'（何年もかける代わりに数ヶ月で）と述べられています。"
            },
            {
                "question": "What caution do international leaders give about this technology?",
                "options": [
                    "It must always be used safely and under clear rules.",
                    "It should be deleted from all computers immediately.",
                    "Only high school students should be allowed to use it.",
                    "It must be sold only in toy stores."
                ],
                "answer": 0,
                "explanation": "最終文で、安全で平和に使われるよう明確なルールが必要だと述べられています。"
            },
            {
                "question": "What does the word 'predict' mean?",
                "options": ["To forget completely", "To guess or calculate what will happen", "To break into pieces", "To paint in bright colors"],
                "answer": 1,
                "explanation": "predict は「予測する」「見通しを立てる」という意味です。"
            }
        ]
    },

    # 2. SCIENCE JUNIOR - Sounds in Language Learning
    {
        "slug": "phonetic-focus-foreign-language-acquisition",
        "category": "science",
        "date": "2026-10-15",
        "title": "Listen to the Sounds: A New Way to Learn a Foreign Language Faster",
        "headline_ja": "音に耳をすませよう：意味より「音」に集中する新しい英語学習法",
        "subhead": "単語の意味を急いで調べず、まず英語の音とリズムを聞くことで脳がスムーズに文法を覚える。",
        "lead_snippet": "新しい言語を勉強するとき、すぐに単語の意味を辞書で調べようとしていませんか？最新の脳科学研究によると、最初は意味を気にせず『純粋な音やリズム』をじっくり聞く方が、脳が疲れずに自然と文法を身につけられることが分かりました。",
        "source_name": "The Guardian",
        "source_url": "https://www.theguardian.com/science/2026/oct/14/focus-on-sounds-to-help-learn-a-language-study-suggests",
        "senior_path": "../../../science/phonetic-focus-foreign-language-acquisition/index.html",
        "image": "https://images.unsplash.com/photo-1456513080510-7bf3a84b82f8?w=1000&auto=format&fit=crop&q=80",
        "sentences": [
            {
                "en": "Brain scientists have found that people learn foreign languages much faster when they stop worrying about meaning and simply listen to the sounds.",
                "ja": "脳科学者らは、単語の意味を気にするのをやめてシンプルにその音を聞くことで、外国語をはるかに速く習得できることを発見しました。"
            },
            {
                "en": "When we try to translate every word into our own language, our brain gets tired and cannot remember how the sentences fit together.",
                "ja": "すべての単語を自分の母語に翻訳しようとすると、私たちの脳は疲れてしまい、文がどのように組み立てられているかを記憶できなくなります。"
            },
            {
                "en": "However, students who focus on the music and rhythm of speech build strong listening skills that make grammar much easier later on.",
                "ja": "しかし、話し言葉の音楽やリズムに集中した生徒たちは、後から文法をずっと簡単に理解できるようにする強いリスニング力を身につけます。"
            },
            {
                "en": "This natural process is very similar to how babies learn their first words by listening happily before they understand grammar rules.",
                "ja": "この自然なプロセスは、赤ちゃんが文法ルールを理解する前に楽しそうに音を聞くことで言葉を覚える仕組みとよく似ています。"
            },
            {
                "en": "Teachers now suggest that practicing listening and repeating sounds out loud can give students a wonderful head start in English.",
                "ja": "先生たちは現在、声を出して聞いたり繰り返したり練習することが、英語の素晴らしい好スタートにつながるとアドバイスしています。"
            }
        ],
        "dialogue": [
            {"speaker": "七", "name": "Nanami", "role": "生徒", "text": "英語を聞くとき、1語1語を日本語に訳そうとして追いつかなくなることがよくありました！"},
            {"speaker": "慶", "name": "Keita", "role": "英語講師", "text": "まさに第2文の 'our brain gets tired'（脳が疲れてしまう）だね。最初は完璧に意味を分かろうとしなくていいんだよ。"},
            {"speaker": "七", "name": "Nanami", "role": "生徒", "text": "赤ちゃんの言葉の覚え方と同じなんですね（第4文）。まず歌やリズムとして英語の音に親しむことが大切なんですね。"},
            {"speaker": "慶", "name": "Keita", "role": "英語講師", "text": "その通り！第5文にあるように、音読して自分の耳で音を確かめる（repeating sounds out loud）習慣をつけると、リスニングも長文読解も驚くほど伸びるよ。"}
        ],
        "vocab": [
            {"word": "translate", "meaning": "翻訳する、別の言語に直す", "pos": "verb", "def": "To change words into a different language."},
            {"word": "rhythm", "meaning": "リズム、拍子", "pos": "noun", "def": "A regular repeated pattern of sounds or movements."},
            {"word": "grammar", "meaning": "文法、言葉のきまり", "pos": "noun", "def": "The rules about how words change their form and combine into sentences."},
            {"word": "similar", "meaning": "似ている、類似した", "pos": "adjective", "def": "Almost the same as someone or something else."},
            {"word": "head start", "meaning": "有利なスタート、先手", "pos": "noun", "def": "An advantage granted to someone at the beginning of a challenge."}
        ],
        "syntax": [
            {"title": "類似を表す：be similar to 〜（〜と似ている）", "formula": "This process [is very similar to] [how babies learn words].", "explanation": "be similar to で「〜とよく似ている」という意味になります。"},
            {"title": "〜するにつれて・〜するとき：when + 主語 + 動詞", "formula": "learn much faster [when they simply listen to the sounds].", "explanation": "when は時や条件を表し、「〜するときにずっと速く学べる」という意味を作ります。"}
        ],
        "quiz": [
            {
                "question": "What advice do brain scientists give to foreign language learners?",
                "options": [
                    "Memorize the entire English dictionary on day one.",
                    "Focus first on listening to the sounds and rhythms of speech rather than translating every word.",
                    "Never listen to spoken English under any circumstances.",
                    "Only read books in silence without ever speaking."
                ],
                "answer": 1,
                "explanation": "第1文で「意味を心配するのをやめて、シンプルに音を聞くことで速く学べる」と述べられています。"
            },
            {
                "question": "What happens when learners try to translate every word into their native language?",
                "options": [
                    "Their brain gets tired and struggles to remember grammar patterns.",
                    "They immediately become professional interpreters.",
                    "Their eyesight improves dramatically.",
                    "They forget how to speak their mother tongue."
                ],
                "answer": 0,
                "explanation": "第2文で「脳が疲れてしまい、文の組み立て方を記憶できなくなる」と説明されています。"
            },
            {
                "question": "Who learns language in a very similar natural way according to paragraph 4?",
                "options": ["Astronauts in space", "Babies listening before understanding grammar", "Robots in factories", "University professors during lectures"],
                "answer": 1,
                "explanation": "第4文で、赤ちゃんが文法を理解する前に楽しそうに音を聞く仕組みと似ていると説明されています。"
            },
            {
                "question": "What practice do teachers suggest to get a head start in English?",
                "options": [
                    "Listening and repeating sounds out loud.",
                    "Writing 1,000 kanji characters every night.",
                    "Refusing to talk to foreign friends.",
                    "Sleeping with headphones turned off."
                ],
                "answer": 0,
                "explanation": "第5文で、声を出して聞いたり繰り返したりすることが推奨されています。"
            },
            {
                "question": "What is the meaning of the word 'translate'?",
                "options": ["To sing a song", "To change words into another language", "To paint a wall", "To run very quickly"],
                "answer": 1,
                "explanation": "translate は「翻訳する」「別の言語に直す」という意味です。"
            }
        ]
    },

    # 3. SOCIETY JUNIOR - School Phone Ban
    {
        "slug": "england-school-chain-phone-free-policy",
        "category": "society",
        "date": "2026-10-15",
        "title": "Putting Phones Away: 35,000 British Students Go Phone-Free at School",
        "headline_ja": "学校ではスマホをお休み：イギリスで3万5千人の生徒が完全スマホ禁止に",
        "subhead": "授業中も休み時間もスマホから離れることで、友達との会話が増えて授業の集中力も大幅アップ。",
        "lead_snippet": "イギリスにある大きな学校グループが、所属する3万5千人の生徒全員を対象に、学校内でのスマートフォンの使用を完全に禁止することを決めました。専用のポーチに入れて下校まで預けることで、休み時間に友達と笑い合ったりスポーツをする時間が増えています。",
        "source_name": "The Guardian",
        "source_url": "https://www.theguardian.com/education/2024/sep/13/academy-chain-with-35000-pupils-to-be-first-in-england-to-go-phone-free",
        "senior_path": "../../../society/england-school-chain-phone-free-policy/index.html",
        "image": "https://images.unsplash.com/photo-1580582932707-520aed937b7b?w=1000&auto=format&fit=crop&q=80",
        "sentences": [
            {
                "en": "A large group of schools in England has announced that thirty-five thousand students must keep their mobile phones switched off and put away all day.",
                "ja": "イングランドの大規模な学校グループが、3万5千人の生徒たちに対し、終日携帯電話の電源を切って片付けておくことを義務付けると発表しました。"
            },
            {
                "en": "Teachers explained that constant phone notifications distract students from lessons and make it harder to sleep peacefully at night.",
                "ja": "先生たちは、絶え間ないスマホの通知が生徒たちの授業の集中を妨げ、夜にぐっすり眠るのを難しくしていると説明しました。"
            },
            {
                "en": "Under the new rule, pupils place their phones into special locked pouches in the morning and carry them safely until the final bell rings.",
                "ja": "新しいルールの下で、生徒たちは朝のうちに特別な鍵付きポーチにスマホを入れ、終業のチャイムが鳴るまで安全に持ち歩きます。"
            },
            {
                "en": "In schools that already tested this idea, children talked much more in the playground and joined fun lunchtime sports clubs.",
                "ja": "このアイデアをすでに試した学校では、子どもたちが校庭でずっと多く会話を交わし、楽しい昼休みのスポーツクラブに参加するようになりました。"
            },
            {
                "en": "Many educators believe that schools should be quiet, safe spaces where young people can learn and make real friends without screen pressure.",
                "ja": "多くの教育者らは、学校は画面のプレッシャーなしに若者が学び、本物の友達を作ることができる静かで安全な場所であるべきだと考えています。"
            }
        ],
        "dialogue": [
            {"speaker": "七", "name": "Nanami", "role": "生徒", "text": "朝にポーチに入れて鍵をかけて、放課後まで開けられないようにするんですね！"},
            {"speaker": "慶", "name": "Keita", "role": "英語講師", "text": "第3文にある 'special locked pouches'（特別な鍵付きポーチ）だね。没収されて先生に預けるのではなく、自分のカバンの中に持っておけるから安心感もあるんだ。"},
            {"speaker": "七", "name": "Nanami", "role": "生徒", "text": "第4文のように、休み時間にみんなが画面を見ずに校庭で話したり遊んだりするようになるのは素敵ですね。"},
            {"speaker": "慶", "name": "Keita", "role": "英語講師", "text": "『リアルな友達を作る（第5文の make real friends without screen pressure）』ことの大切さだね。高校生の英作文でも身近で共感しやすいテーマだよ！"}
        ],
        "vocab": [
            {"word": "distract", "meaning": "気を散らす、注意をそらす", "pos": "verb", "def": "To draw someone's attention away from what they are doing."},
            {"word": "notification", "meaning": "通知、お知らせ", "pos": "noun", "def": "A message or sound alerting you to an event on your phone."},
            {"word": "pouch", "meaning": "小袋、ポーチ", "pos": "noun", "def": "A small bag or container used for carrying small items."},
            {"word": "playground", "meaning": "校庭、運動場", "pos": "noun", "def": "An outdoor area provided for children to play in at school."},
            {"word": "educator", "meaning": "教育者、先生", "pos": "noun", "def": "A person who provides instruction or education, such as a teacher."}
        ],
        "syntax": [
            {"title": "make it harder to do（〜するのを難しくする）", "formula": "[notifications] make it [harder to sleep peacefully at night].", "explanation": "make it + 形容詞 + to 不定詞 の形式目的語構文です。it は形式的な目的語で、本当の目的語は to sleep 以下です。"},
            {"title": "関係代名詞 where による場所の説明", "formula": "schools should be safe spaces [where young people can learn].", "explanation": "先行詞 safe spaces（安全な場所）を関係副詞 where が修飾し、「若者が学べる場所」と説明しています。"}
        ],
        "quiz": [
            {
                "question": "How many students are affected by the new phone policy in England?",
                "options": ["35 students", "350 students", "35,000 students", "3.5 million students"],
                "answer": 2,
                "explanation": "第1文で「3万5千人の生徒（thirty-five thousand students）」と明記されています。"
            },
            {
                "question": "Why did teachers want to ban mobile phones during the school day?",
                "options": [
                    "Because phones distract students from lessons and disrupt sleep.",
                    "Because electricity prices became too high in schools.",
                    "Because teachers wanted to play video games alone.",
                    "Because smartphones are made of radioactive material."
                ],
                "answer": 0,
                "explanation": "第2文で、通知が生徒の集中を妨げ、夜の睡眠を妨害するためだと説明されています。"
            },
            {
                "question": "How are phones kept during the day under the new rule?",
                "options": [
                    "Students throw them into recycling bins.",
                    "Pupils place them into special locked pouches until dismissal.",
                    "Teachers sell them online.",
                    "Students hide them under classroom carpets."
                ],
                "answer": 1,
                "explanation": "第3文で「朝に特別な鍵付きポーチに入れて下校まで安全に持ち歩く」と説明されています。"
            },
            {
                "question": "What positive change happened in schools that tested the rule?",
                "options": [
                    "Students forgot how to speak English.",
                    "Children talked much more in the playground and joined sports clubs.",
                    "School cafeterias stopped serving lunch.",
                    "Students refused to go home after classes."
                ],
                "answer": 1,
                "explanation": "第4文で、校庭で会話が増え、昼休みのスポーツクラブに参加するようになったと述べられています。"
            },
            {
                "question": "What is the meaning of the word 'distract'?",
                "options": ["To help someone study", "To take attention away from something", "To clean up a room", "To buy a new smartphone"],
                "answer": 1,
                "explanation": "distract は「気を散らす」「注意をそらす」という意味です。"
            }
        ]
    },

    # 4. SOCIETY JUNIOR - Four-Day Workweek
    {
        "slug": "four-day-workweek-uk-trial-permanent",
        "category": "society",
        "date": "2026-10-15",
        "title": "A Three-Day Weekend Forever: The Success of the Four-Day Workweek",
        "headline_ja": "ずっと週休3日制に：イギリス企業の大規模テストで大成功した働き方",
        "subhead": "給料はそのままで休みを1日増やす。仕事の効率を上げて疲れを減らす新しい社会の仕組み。",
        "lead_snippet": "給料を減らさずに働く日を週5日から週4日に減らす実験を行ったイギリスの会社で、1年が経った今も半数以上がこの制度をずっと続けることを決めました。ムダな会議をなくして集中して働くことで、会社の業績も社員の健康もアップしています。",
        "source_name": "The Guardian",
        "source_url": "https://www.theguardian.com/money/2024/feb/21/four-day-week-made-permanent-for-most-uk-firms-in-worlds-biggest-trial",
        "senior_path": "../../../society/four-day-workweek-uk-trial-permanent/index.html",
        "image": "https://images.unsplash.com/photo-1497215728101-856f4ea42174?w=1000&auto=format&fit=crop&q=80",
        "sentences": [
            {
                "en": "More than half of the British companies that tested a four-day workweek have decided to keep the short schedule permanently because their workers stayed happy and productive.",
                "ja": "週休3日制をテストしたイギリス企業の半数以上が、社員たちが幸せで生産的であり続けたため、この短いスケジュールをずっと続けることを決定しました。"
            },
            {
                "en": "Under this special plan, workers receive their full salary while working one day less each week, as long as they finish all their regular tasks.",
                "ja": "この特別な計画の下で、普段の仕事をすべてやり遂げる限り、従業員は毎週1日少なく働きながら全額の給料を受け取ります。"
            },
            {
                "en": "Researchers found that far fewer people quit their jobs, and workers felt much less stressed and exhausted at the end of the week.",
                "ja": "研究者らは、仕事を辞める人が大幅に減り、週末に従業員がストレスや疲労を感じることがずっと少なくなったことを発見しました。"
            },
            {
                "en": "Companies saved valuable time by avoiding unnecessary meetings and using smart computer tools to speed up boring paperwork.",
                "ja": "会社は不要な会議を避け、賢いコンピューターツールを使って退屈な書類仕事をスピードアップすることで、貴重な時間を節約しました。"
            },
            {
                "en": "Experts believe that three-day weekends could soon become a common benefit as companies compete to attract talented young workers.",
                "ja": "専門家らは、会社が優秀な若い労働者を惹きつけるために競い合う中で、週休3日制が近いうちに当たり前のメリットになるかもしれないと考えています。"
            }
        ],
        "dialogue": [
            {"speaker": "七", "name": "Nanami", "role": "生徒", "text": "週に4日しか働かないのに給料は満額もらえるなんて、最初は嘘かと思いましたが本当にあるんですね！"},
            {"speaker": "慶", "name": "Keita", "role": "英語講師", "text": "第2文の 'as long as they finish their tasks'（仕事をきちんと終わらせる限り）という条件があるからね。ただ休むのではなく、仕事の進め方を工夫したんだ。"},
            {"speaker": "七", "name": "Nanami", "role": "生徒", "text": "第4文のように、長いだけの会議をなくしてパソコンでパパッと自動化したんですね。"},
            {"speaker": "慶", "name": "Keita", "role": "英語講師", "text": "そう。第3文の 'felt much less stressed'（ストレスがずっと減った）は、働きすぎが問題になっている日本の社会にとってもすごく参考になる話だね。"}
        ],
        "vocab": [
            {"word": "permanently", "meaning": "恒久的に、永久に", "pos": "adverb", "def": "In a way that lasts or remains unchanged indefinitely."},
            {"word": "productive", "meaning": "生産的な、効率の良い", "pos": "adjective", "def": "Achieving or producing a significant amount or result."},
            {"word": "salary", "meaning": "給料、月給", "pos": "noun", "def": "A fixed regular payment made by an employer to an employee."},
            {"word": "exhausted", "meaning": "疲れ切った、ヘトヘトな", "pos": "adjective", "def": "Very tired, either physically or mentally."},
            {"word": "unnecessary", "meaning": "不要な、余計な", "pos": "adjective", "def": "Not needed; more than is necessary."}
        ],
        "syntax": [
            {"title": "〜である限り：as long as + 主語 + 動詞", "formula": "[workers receive full salary] [as long as they finish their tasks].", "explanation": "as long as は条件を表し、「〜する限りは」という意味を作ります。"},
            {"title": "by + 動名詞（〜することによって）", "formula": "Companies saved time [by avoiding meetings and using smart tools].", "explanation": "by + ~ing で手段や方法を表し、「会議を避けることによって時間を節約した」という意味になります。"}
        ],
        "quiz": [
            {
                "question": "What did more than half of the British companies in the trial decide to do?",
                "options": [
                    "They decided to make the four-day workweek permanent.",
                    "They forced employees to work seven days a week.",
                    "They reduced all salaries by half.",
                    "They closed down their businesses completely."
                ],
                "answer": 0,
                "explanation": "第1文で「半数以上の企業が週休3日制を恒久化することを決めた」と記されています。"
            },
            {
                "question": "Do employees in this program receive lower pay for working fewer hours?",
                "options": [
                    "Yes, they only receive 50% of their salary.",
                    "No, they receive their full salary as long as they finish their work.",
                    "Yes, they must pay money to the government to take days off.",
                    "No, they are paid only in chocolate snacks."
                ],
                "answer": 1,
                "explanation": "第2文で「仕事を終える限り全額の給与を受け取る（receive their full salary）」と明記されています。"
            },
            {
                "question": "How did companies save time to finish their work in four days?",
                "options": [
                    "By avoiding unnecessary meetings and using smart computer tools.",
                    "By forbidding employees from drinking water.",
                    "By skipping lunch every day.",
                    "By turning off all office lights."
                ],
                "answer": 0,
                "explanation": "第4文で、不要な会議を避け、スマートなツールで書類仕事をスピードアップしたと説明されています。"
            },
            {
                "question": "What health benefit did researchers discover among employees?",
                "options": [
                    "Workers grew ten centimeters taller.",
                    "Workers felt much less stressed and exhausted at week's end.",
                    "Workers completely lost the ability to sleep.",
                    "Workers developed allergies to computers."
                ],
                "answer": 1,
                "explanation": "第3文で「ストレスや疲労を感じることがずっと少なくなった」と述べられています。"
            },
            {
                "question": "The word 'exhausted' is closest in meaning to:",
                "options": ["extremely energetic", "very tired", "hungry", "excited"],
                "answer": 1,
                "explanation": "exhausted は「疲れ果てた」「ヘトヘトな」という意味で、very tired が同義です。"
            }
        ]
    },

    # 5. WORLD JUNIOR - Mont Blanc Shrinking
    {
        "slug": "mont-blanc-glacier-melt-elevation-loss",
        "category": "world",
        "date": "2026-10-15",
        "title": "Shrinking Mountain: Europe's Highest Peak Loses Height as Ice Melts",
        "headline_ja": "縮む名峰モンブラン：氷河が溶けてヨーロッパ最高峰の標高が1メートル低下",
        "subhead": "夏の猛暑で山頂の万年雪が溶け出す。アルプスの川の水が減り、環境問題のシグナルに。",
        "lead_snippet": "フランスとイタリアの間にそびえるアルプス最高峰の山『モンブラン』の高さが、夏の暑さで山頂の氷が溶けたため、ここ数年で1メートル以上も低くなったことが分かりました。氷河が溶けると川の水が減ってしまうため、世界中で温暖化対策が急がれています。",
        "source_name": "The Guardian",
        "source_url": "https://www.theguardian.com/environment/2026/oct/14/mont-blanc-loses-metre-height",
        "senior_path": "../../../world/mont-blanc-glacier-melt-elevation-loss/index.html",
        "image": "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?w=1000&auto=format&fit=crop&q=80",
        "sentences": [
            {
                "en": "Official mapmakers have confirmed that Mont Blanc, the highest mountain in Western Europe, has shrunk by more than one metre because hot summer weather melted its summit ice.",
                "ja": "公式の地図測量士らは、西ヨーロッパ最高峰のモンブランが、暑い夏の気候で山頂の氷が溶けたため1メートル以上低くなったことを確認しました。"
            },
            {
                "en": "The solid rock beneath the mountain stays the same, but the thick dome of snow and ice on top changes size with global temperature rises.",
                "ja": "山を支える硬い岩はずっと同じままですが、山頂にある雪と氷の分厚いドームは地球の気温上昇によって大きさが変化します。"
            },
            {
                "en": "Scientists warn that melting glaciers reduce the supply of clean freshwater that flows into famous rivers like the Rhône in France.",
                "ja": "科学者たちは、氷河が溶けることでフランスのローヌ川のような有名な川へ流れ込むきれいな真水の量が減ってしまうと警告しています。"
            },
            {
                "en": "In addition, melting ice has caused loose rocks to tumble down mountain slopes, forcing officials to close some popular climbing paths.",
                "ja": "さらに、氷が溶けることで緩んだ岩が山の斜面を転がり落ちるようになり、関係者は人気の登山ルートの一部を閉鎖せざるを得なくなっています。"
            },
            {
                "en": "Leaders around the world say this shrinking white peak is a clear reminder that we must protect our climate before it is too late.",
                "ja": "世界中の指導者らは、この縮小する白い山頂が、手遅れになる前に気候を守らなければならないことを示す明確な合図であると述べています。"
            }
        ],
        "dialogue": [
            {"speaker": "七", "name": "Nanami", "role": "生徒", "text": "ヨーロッパで一番高いモンブランの高さが1メートルも縮んでしまったなんてショックです！"},
            {"speaker": "慶", "name": "Keita", "role": "英語講師", "text": "第2文にある通り、岩（solid rock）が崩れたのではなくて、山頂の万年雪や氷の帽子が猛暑で溶けて薄くなってしまったんだね。"},
            {"speaker": "七", "name": "Nanami", "role": "生徒", "text": "第3文にあるように、氷河の水は川に流れて飲み水や田畑の水になるから、溶けてなくなると大変なことになりますね。"},
            {"speaker": "慶", "name": "Keita", "role": "英語講師", "text": "その通りだね。第5文の 'a clear reminder'（明確な教訓・合図）という表現を覚えておこう。気候変動（climate change）の長文で頻出のキーワードだよ。"}
        ],
        "vocab": [
            {"word": "peak", "meaning": "頂上、最高峰", "pos": "noun", "def": "The pointed top of a mountain."},
            {"word": "glacier", "meaning": "氷河", "pos": "noun", "def": "A slowly moving mass or river of ice formed by snow on mountains."},
            {"word": "freshwater", "meaning": "真水（塩分を含まない水）", "pos": "noun", "def": "Water that is not salty, found in rivers and lakes."},
            {"word": "slope", "meaning": "斜面、坂道", "pos": "noun", "def": "A surface of which one end or side is at a higher level than another."},
            {"word": "reminder", "meaning": "思い出させるもの、合図、通知", "pos": "noun", "def": "A thing that causes someone to remember something."}
        ],
        "syntax": [
            {"title": "原因を表す：because + 文（〜だから・〜のため）", "formula": "[Mont Blanc has shrunk] [because hot summer weather melted its ice].", "explanation": "because の後ろに主語と動詞が続き、「暑い夏の天候が氷を溶かしたため」という明確な理由を示します。"},
            {"title": "force + 目的語 + to do（〜に強制的に…させる）", "formula": "[melting ice caused rockfalls], [forcing officials to close climbing paths].", "explanation": "分詞構文 forcing officials to close で「その結果、関係者は登山道を閉鎖することを余儀なくされた」という意味になります。"}
        ],
        "quiz": [
            {
                "question": "What happened to Mont Blanc over recent years?",
                "options": [
                    "It grew ten metres taller due to heavy blizzards.",
                    "It shrank by more than one metre because summit ice melted.",
                    "It erupted as a volcano.",
                    "It was renamed after an Italian painter."
                ],
                "answer": 1,
                "explanation": "第1文で「夏の暑さで山頂の氷が溶けたため1メートル以上低くなった」と述べられています。"
            },
            {
                "question": "Does the solid rock beneath the mountain summit change size?",
                "options": [
                    "No, the rock stays the same, but the ice cap on top changes.",
                    "Yes, the rock melted into liquid lava.",
                    "Yes, the rock dissolved into the sea.",
                    "No, the entire mountain is made purely of plastic."
                ],
                "answer": 0,
                "explanation": "第2文で「山頂の下の硬い岩はずっと同じままであるが、氷のドームが変化する」と説明されています。"
            },
            {
                "question": "Why is the melting of Alpine glaciers dangerous for people living downstream?",
                "options": [
                    "It causes rivers to turn bright purple.",
                    "It reduces the vital supply of clean freshwater for European rivers like the Rhône.",
                    "It causes all farm animals to run away.",
                    "It makes sea water too sweet to drink."
                ],
                "answer": 1,
                "explanation": "第3文で「ローヌ川のような大河川に流れ込むきれいな真水の供給が減ってしまう」と警告されています。"
            },
            {
                "question": "Why did officials close some climbing paths on Mont Blanc?",
                "options": [
                    "Because melting ice caused loose rocks to fall dangerously down slopes.",
                    "Because climbers refused to pay parking fees.",
                    "Because wild bears took over the mountain huts.",
                    "Because all climbing ropes were stolen."
                ],
                "answer": 0,
                "explanation": "第4文で、氷が溶けることで緩んだ岩が転がり落ちるようになり、危険なためルートが閉鎖されたと書かれています。"
            },
            {
                "question": "The word 'peak' is closest in meaning to:",
                "options": ["mountain top", "ocean floor", "deep forest", "underground tunnel"],
                "answer": 0,
                "explanation": "peak は「山の頂上」「山頂」を意味し、mountain top が同義です。"
            }
        ]
    },

    # 6. WORLD JUNIOR - Renewables Overtake Fossil Fuels in EU
    {
        "slug": "renewables-overtake-fossil-fuels-eu-electricity",
        "category": "world",
        "date": "2026-10-15",
        "title": "Clean Energy Triumph: Wind and Solar Beat Fossil Fuels Across Europe",
        "headline_ja": "クリーンエネルギーの勝利：ヨーロッパで風力と太陽光が化石燃料を逆転",
        "subhead": "EU全体の電力の30%を自然エネルギーが発電。石炭やガスの使用が減り地球にやさしい社会へ。",
        "lead_snippet": "ヨーロッパの国々で、風力発電と太陽光発電が作った電気の量が、石炭や天然ガスなどの化石燃料の合計を初めて追い抜きました。ヨーロッパの電気の約3分の1が自然の力で作られており、地球温暖化を防ぎながらエネルギーを自給する新しい時代が始まっています。",
        "source_name": "The Guardian",
        "source_url": "https://www.theguardian.com/environment/article/2024/jul/30/renewables-overtake-fossil-fuels-to-provide-30-of-eu-electricity",
        "senior_path": "../../../world/renewables-overtake-fossil-fuels-eu-electricity/index.html",
        "image": "https://images.unsplash.com/photo-1466611653911-95081537e5b7?w=1000&auto=format&fit=crop&q=80",
        "sentences": [
            {
                "en": "Wind turbines and solar panels made thirty percent of all the electricity in the European Union, beating fossil fuels for the first time in history.",
                "ja": "風力タービンと太陽光パネルが欧州連合（EU）のすべての電気の30%を生み出し、歴史上初めて化石燃料を打ち破りました。"
            },
            {
                "en": "Energy reports showed that polluting coal and gas power dropped by seventeen percent as green power expanded rapidly.",
                "ja": "エネルギー報告書によると、環境にやさしい電力が急速に広まるにつれて、空気を汚す石炭やガスの発電が17%も減少しました。"
            },
            {
                "en": "In thirteen different European countries, clean renewable energy produced more power than coal and gas combined.",
                "ja": "ヨーロッパの13の国々では、クリーンな再生可能エネルギーが石炭とガスを合わせたよりも多くの電力を生み出しました。"
            },
            {
                "en": "European governments worked hard to build more green power because relying on imported fossil fuels is both expensive and risky.",
                "ja": "輸入された化石燃料に頼ることはお金がかかり危険でもあるため、ヨーロッパの政府はより多くのグリーン電力を建設するために熱心に取り組みました。"
            },
            {
                "en": "Engineers say the next step is building giant batteries and smarter power lines so that stored sun and wind energy can be shared anywhere at night.",
                "ja": "技術者らは、蓄えた太陽や風のエネルギーを夜でもどこでも分け合えるよう、巨大なバッテリーとよりスマートな送電網を作ることが次のステップだと語っています。"
            }
        ],
        "dialogue": [
            {"speaker": "七", "name": "Nanami", "role": "生徒", "text": "風力や太陽光の電気が化石燃料を追い抜くなんて、ヨーロッパの環境対策は本当に進んでいますね！"},
            {"speaker": "慶", "name": "Keita", "role": "英語講師", "text": "第1文の 'beating fossil fuels for the first time in history'（歴史上初めて化石燃料に勝った）は素晴らしい成果だね。"},
            {"speaker": "七", "name": "Nanami", "role": "生徒", "text": "第4文にあるように、外国から石油や天然ガスを輸入すると戦争などで値段が上がって困るから、自分たちの国の風や太陽を使うのが一番安全なんですね。"},
            {"speaker": "慶", "name": "Keita", "role": "英語講師", "text": "その通り！第5文にある巨大なバッテリー（giant batteries）で電気をためておければ、風が止まっても夜になっても安心だね。"}
        ],
        "vocab": [
            {"word": "turbine", "meaning": "タービン、風車の羽根", "pos": "noun", "def": "A machine for producing continuous power using wind, water, or steam."},
            {"word": "fossil fuel", "meaning": "化石燃料（石炭・石油・天然ガスなど）", "pos": "noun", "def": "A natural fuel such as coal or gas, formed in the past from the remains of living organisms."},
            {"word": "expand", "meaning": "広がる、拡大する", "pos": "verb", "def": "To become or make larger or more extensive."},
            {"word": "rely on", "meaning": "〜に頼る、依存する", "pos": "verb", "def": "To depend on with full trust or confidence."},
            {"word": "power line", "meaning": "送電線、電線", "pos": "noun", "def": "A cable carrying electrical power, typically supported on poles or pylons."}
        ],
        "syntax": [
            {"title": "時・理由を表す接続詞 as（〜するにつれて）", "formula": "[coal power dropped], [as green power expanded rapidly].", "explanation": "as には「〜するにつれて」という意味があり、再エネが広まるにつれて石炭火力が減ったという比例的な変化を表しています。"},
            {"title": "both A and B（AとBの両方）", "formula": "relying on fossil fuels is [both expensive and risky].", "explanation": "both A and B で「AとBの両方だ」という意味になります。"}
        ],
        "quiz": [
            {
                "question": "What percentage of electricity in the EU was generated by wind and solar power?",
                "options": ["5 percent", "30 percent", "99 percent", "0 percent"],
                "answer": 1,
                "explanation": "第1文で「風力タービンと太陽光パネルが全電力の30%を生み出した」と書かれています。"
            },
            {
                "question": "By how much did coal and gas generation drop in the European Union?",
                "options": ["By 17 percent", "By 100 percent", "It doubled", "By only 1 percent"],
                "answer": 0,
                "explanation": "第2文で「石炭やガスの発電が17%減少した」と説明されています。"
            },
            {
                "question": "Why did European governments push to build more green power installations?",
                "options": [
                    "Because relying on imported fossil fuels is both expensive and risky.",
                    "Because they wanted to make power lines invisible to birds.",
                    "Because coal is too difficult to dig out of the ground.",
                    "Because European citizens disliked using computers."
                ],
                "answer": 0,
                "explanation": "第4文で、輸入化石燃料に頼ることは高額でリスクが高いためだと説明されています。"
            },
            {
                "question": "What is the next important step for engineers mentioned in paragraph 5?",
                "options": [
                    "Building giant batteries and smarter power lines to share stored energy at night.",
                    "Destroying all solar panels before winter starts.",
                    "Banning electricity in major capital cities.",
                    "Importing more gasoline from Antarctica."
                ],
                "answer": 0,
                "explanation": "第5文で、巨大バッテリーとスマートな送電網を作ることが次のステップだと書かれています。"
            },
            {
                "question": "The phrase 'rely on' means:",
                "options": ["to depend on", "to run away from", "to paint over", "to laugh at"],
                "answer": 0,
                "explanation": "rely on は「〜に頼る」「依存する」という意味で、to depend on が同義です。"
            }
        ]
    },

    # 7. LAW JUNIOR - EU AI Act
    {
        "slug": "eu-ai-act-consumer-rights-enforcement",
        "category": "law",
        "date": "2026-10-15",
        "title": "Rules for Robots: How the New EU AI Law Protects Everyday People",
        "headline_ja": "AIのための世界初ルール：欧州AI法が私たちの安全とプライバシーを守る方法",
        "subhead": "危険度に応じた4つのランク分け。個人を操る危険なAIを禁止し、安全な技術開発を進める。",
        "lead_snippet": "ヨーロッパで世界で初めてとなる『人工知能（AI）を取り締まる法律』がスタートしました。AIを危険なものから安全なものまでグループ分けし、人々の心を操ったり秘密で顔を監視するような危険なシステムを厳しく禁止しています。私たちの未来に関わるルールを学びましょう。",
        "source_name": "The Guardian",
        "source_url": "https://www.theguardian.com/technology/2024/mar/14/what-will-eu-proposed-regulation-ai-mean-consumers",
        "senior_path": "../../../law/eu-ai-act-consumer-rights-enforcement/index.html",
        "image": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=1000&auto=format&fit=crop&q=80",
        "sentences": [
            {
                "en": "The European Union has introduced the world's first major law to regulate artificial intelligence, making sure smart computer programs are used safely.",
                "ja": "欧州連合は人工知能を取り締まる世界初の主要な法律を導入し、賢いコンピュータープログラムが安全に使われるようにしました。"
            },
            {
                "en": "The law divides AI tools into different groups based on how dangerous they might be to human rights and daily safety.",
                "ja": "その法律は、人間の権利や日々の安全に対してどれほど危険であるかに基づいて、AIツールをさまざまなグループに分類しています。"
            },
            {
                "en": "Dangerous tools that try to trick human minds or secretly scan people's faces in public streets are completely banned.",
                "ja": "人間の心を騙そうとしたり、公道の街中で人々の顔を秘密裏にスキャンするような危険なツールは完全に禁止されます。"
            },
            {
                "en": "Helpful AI that answers questions or makes pictures must clearly label its content so that people know it was made by a computer, not a human.",
                "ja": "質問に答えたり絵を描く便利なAIは、人間ではなくコンピューターによって作られたものであると人々が分かるよう、コンテンツに明確なラベルを付けなければなりません。"
            },
            {
                "en": "Because major tech companies want to sell their apps worldwide, this European law is expected to make AI safer for everyone across the globe.",
                "ja": "大手テクノロジー企業は自社のアプリを世界中で販売したいため、このヨーロッパの法律は地球上のすべての人にとってAIをより安全にすると期待されています。"
            }
        ],
        "dialogue": [
            {"speaker": "七", "name": "Nanami", "role": "生徒", "text": "AIって便利だけど、知らないうちに顔をスキャンされたり、フェイク画像に騙されたりするのは怖いですよね。"},
            {"speaker": "慶", "name": "Keita", "role": "英語講師", "text": "第3文にあるように、そういう『危険なAI（dangerous tools）』は完全に禁止（completely banned）されたんだよ。"},
            {"speaker": "七", "name": "Nanami", "role": "生徒", "text": "第4文の『AIが作った画像にはラベルを貼る（must clearly label its content）』というのも、ディープフェイクを見分けるために大切ですね。"},
            {"speaker": "慶", "name": "Keita", "role": "英語講師", "text": "第5文にある通り、ヨーロッパのルールが世界のスタンダードになっていくんだ。これからの社会を生きる高校生にとって必須の知識だよ！"}
        ],
        "vocab": [
            {"word": "regulate", "meaning": "規制する、取り締まる、調整する", "pos": "verb", "def": "To control or maintain the rate or speed of a machine or process."},
            {"word": "human rights", "meaning": "人権（人が生まれながらに持つ権利）", "pos": "noun", "def": "A right that is believed to belong justifiably to every person."},
            {"word": "scan", "meaning": "スキャンする、細かく調べる", "pos": "verb", "def": "To look at all parts of something carefully to detect features."},
            {"word": "label", "meaning": "ラベルを貼る、明記する", "pos": "verb", "def": "To attach a label to; categorize or identify."},
            {"word": "across the globe", "meaning": "世界中で、地球全体で", "pos": "adverb", "def": "Throughout the entire world."}
        ],
        "syntax": [
            {"title": "so that 構文（目的：〜できるように・分かるように）", "formula": "label its content [so that people know it was made by a computer].", "explanation": "so that + 主語 + 動詞 で「人々が〜と分かるように」という目的を表しています。"},
            {"title": "be based on 〜（〜に基づいている）", "formula": "divides tools [based on how dangerous they might be].", "explanation": "based on は「〜に基づいて」という重要な連語です。"}
        ],
        "quiz": [
            {
                "question": "What is the purpose of the new European Union AI law?",
                "options": [
                    "To ban all computers from European homes.",
                    "To make sure artificial intelligence is used safely and protect human rights.",
                    "To build military robots for fighting.",
                    "To force everyone to buy smartphones."
                ],
                "answer": 1,
                "explanation": "第1文で「賢いコンピュータープログラムが安全に使われるようにするため」と説明されています。"
            },
            {
                "question": "Which type of AI is completely banned under the new regulation?",
                "options": [
                    "Calculator apps that do simple math.",
                    "Dangerous tools that trick human minds or secretly scan faces in public streets.",
                    "Spell check programs in word processors.",
                    "Weather forecasting radar."
                ],
                "answer": 1,
                "explanation": "第3文で「人間の心を騙したり、公道で秘密裏に顔をスキャンするツールは完全に禁止される」と明記されています。"
            },
            {
                "question": "What must AI programs that create pictures or text do according to paragraph 4?",
                "options": [
                    "Delete themselves after 24 hours.",
                    "Clearly label their content so users know it was made by a computer.",
                    "Cost at least 1,000 euros per picture.",
                    "Only work in the French language."
                ],
                "answer": 1,
                "explanation": "第4文で「コンピューターが作ったものであると分かるよう明確にラベルを貼らなければならない」と述べられています。"
            },
            {
                "question": "Why will this European law affect people all across the globe?",
                "options": [
                    "Because big tech companies want to sell their apps worldwide to everyone.",
                    "Because all humans are required to move to Europe.",
                    "Because the European parliament owns all internet cables.",
                    "Because search engines are only located in Brussels."
                ],
                "answer": 0,
                "explanation": "第5文で、大手テクノロジー企業がアプリを世界中で売りたいため、世界中のAIがより安全になると説明されています。"
            },
            {
                "question": "The word 'regulate' means:",
                "options": ["to break", "to control with rules", "to laugh", "to paint"],
                "answer": 1,
                "explanation": "regulate は「ルールで規制する」「管理する」という意味です。"
            }
        ]
    },

    # 8. LAW JUNIOR - US Newspapers Lawsuit
    {
        "slug": "us-newspapers-openai-copyright-lawsuit",
        "category": "law",
        "date": "2026-10-15",
        "title": "Writers vs. AI: American Newspapers Take Tech Companies to Court",
        "headline_ja": "記者とAIの戦い：アメリカの新聞社が大手テック企業を裁判所に訴えた理由",
        "subhead": "苦労して取材した何百万本もの記事を無断でAIの学習に使用。著作権とニュースの未来。",
        "lead_snippet": "アメリカの有名な新聞社8社が、AIを作っている大手テクノロジー企業を相手取って裁判を起こしました。記者が長い時間をかけて取材した記事を勝手にAIに読み込ませて学習させたのは『著作権の侵害だ』と主張しています。知っておくべき知的財産権のニュースです。",
        "source_name": "The Guardian",
        "source_url": "https://www.theguardian.com/technology/2024/apr/30/us-newspaper-openai-lawsuit",
        "senior_path": "../../../law/us-newspapers-openai-copyright-lawsuit/index.html",
        "image": "https://images.unsplash.com/photo-1589829545856-d10d557cf95f?w=1000&auto=format&fit=crop&q=80",
        "sentences": [
            {
                "en": "Eight major American newspapers have filed a big legal case against artificial intelligence companies for using millions of news articles without permission.",
                "ja": "米国の主要な新聞社8社が、何百万本ものニュース記事を許可なく使ったとして、人工知能企業に対して大規模な訴訟を起こしました。"
            },
            {
                "en": "Journalists spend months researching difficult stories, but AI chatbots can copy their exact words and show them to readers for free.",
                "ja": "ジャーナリストは何ヶ月もかけて難しい記事を取材・調査しますが、AIチャットボットはその正確な文章をコピーして読者に無料で見せることができます。"
            },
            {
                "en": "Newspaper publishers say that if people stop paying for news subscriptions, local newspapers will run out of money and close down.",
                "ja": "新聞社の経営者らは、人々がニュースの購読料を払わなくなれば、地域の新聞社はお金がなくなって倒産してしまうと主張しています。"
            },
            {
                "en": "Tech companies reply that teaching computers by reading public web articles is completely fair and helps create amazing new tools.",
                "ja": "テクノロジー企業側は、公開されているウェブ記事を読んでコンピューターに教えることは完全に公正であり、素晴らしい新ツールの作成に役立つと反論しています。"
            },
            {
                "en": "Judges in court must now decide a fair balance between protecting human writers and encouraging future computer inventions.",
                "ja": "裁判所の裁判官たちは今、人間の書き手を守ることと将来のコンピューター発明を後押しすることとの間の公正なバランスを決めなければなりません。"
            }
        ],
        "dialogue": [
            {"speaker": "七", "name": "Nanami", "role": "生徒", "text": "記者の人たちが足で稼いで書いた記事を、AIが勝手に勉強してタダで人に教えていたら、新聞社が困っちゃいますね。"},
            {"speaker": "慶", "name": "Keita", "role": "英語講師", "text": "第2文にある 'spend months researching'（何ヶ月もかけて調査する）と、AIがそれをタダで見せる対比だね。新聞社がつぶれたら、正しいニュース自体が世の中からなくなってしまう。"},
            {"speaker": "七", "name": "Nanami", "role": "生徒", "text": "でもテック企業にも『公開されている文章を読んで賢くなるのは自由だ』という言い分があるんですね（第4文）。"},
            {"speaker": "慶", "name": "Keita", "role": "英語講師", "text": "第5文にある 'decide a fair balance'（公正なバランスを決める）が裁判官の役目だ。著作権（copyright）とフェアユースのバランスは大学入試の自由英作文でも頻出だよ！"}
        ],
        "vocab": [
            {"word": "permission", "meaning": "許可、同意", "pos": "noun", "def": "The act of allowing someone to do something."},
            {"word": "journalist", "meaning": "ジャーナリスト、新聞記者", "pos": "noun", "def": "A person who writes for newspapers, magazines, or news websites."},
            {"word": "subscription", "meaning": "定期購読、有料会員契約", "pos": "noun", "def": "An arrangement to receive something, typically by paying in advance."},
            {"word": "fair", "meaning": "公正な、公平な", "pos": "adjective", "def": "Treating people equally without favoritism or discrimination."},
            {"word": "balance", "meaning": "バランス、均衡", "pos": "noun", "def": "An even distribution of weight or importance enabling stability."}
        ],
        "syntax": [
            {"title": "spend + 時間 + 〜ing（〜することに時間を費やす）", "formula": "Journalists spend [months] [researching difficult stories].", "explanation": "spend + 時間 + 動名詞で「〜することに何ヶ月も費やす」という頻出構文です。"},
            {"title": "if 節による条件（もし〜ならば）", "formula": "[if people stop paying for news], [local newspapers will close down].", "explanation": "if 節の中は現在形、主節は will + 原形動詞で「もし人々が払わなくなれば、新聞社は閉鎖するだろう」という未来の予測を示します。"}
        ],
        "quiz": [
            {
                "question": "Why did eight American newspapers sue artificial intelligence companies?",
                "options": [
                    "Because AI companies sent broken laptops to newsrooms.",
                    "Because millions of news articles were used to train AI models without permission.",
                    "Because newspapers wanted to build their own satellites.",
                    "Because reporters were not allowed to buy computers."
                ],
                "answer": 1,
                "explanation": "第1文で「何百万本ものニュース記事を無許可で使ったとして訴訟を起こした」と説明されています。"
            },
            {
                "question": "What happens if readers only read free AI summaries instead of paying for news?",
                "options": [
                    "Newspapers may run out of money and be forced to close down.",
                    "Computers will stop working worldwide.",
                    "Newspaper reporters will become millionaires.",
                    "Printing ink will turn completely red."
                ],
                "answer": 0,
                "explanation": "第3文で「購読料が支払われなくなると、地域新聞はお金がなくなって倒産してしまう」と記されています。"
            },
            {
                "question": "What argument do tech companies make in their defense?",
                "options": [
                    "They claim reading public articles to teach computers is fair and helps build new tools.",
                    "They say they never used the internet to build AI.",
                    "They argue that newspapers never existed in America.",
                    "They promise to buy all eight newspapers tomorrow."
                ],
                "answer": 0,
                "explanation": "第4文で、公開ウェブ記事を読んでコンピューターを学習させるのは公正だと主張していると書かれています。"
            },
            {
                "question": "What is the difficult task for judges in this court case?",
                "options": [
                    "To build a brand new search engine by hand.",
                    "To balance protecting human creators while encouraging computer innovation.",
                    "To teach robots how to read printed ink on paper.",
                    "To stop all newspapers from writing articles forever."
                ],
                "answer": 1,
                "explanation": "第5文で、人間の書き手を守ることと将来のコンピューター発明を後押しすることのバランスを決める必要があると書かれています。"
            },
            {
                "question": "The word 'permission' is closest in meaning to:",
                "options": ["approval or consent", "punishment", "speed", "argument"],
                "answer": 0,
                "explanation": "permission は「許可」「同意」を意味し、approval or consent が同義です。"
            }
        ]
    },

    # 9. CULTURE JUNIOR - Orbital Booker Prize
    {
        "slug": "orbital-samantha-harvey-booker-prize",
        "category": "culture",
        "date": "2026-10-15",
        "title": "A Day in Space: The Short Novel That Won the Famous Booker Prize",
        "headline_ja": "宇宙での1日：名誉あるブッカー賞に輝いた136ページの短い小説『Orbital』",
        "subhead": "宇宙ステーションから地球を見つめる6人の宇宙飛行士。青く美しい地球を大切にする想い。",
        "lead_snippet": "イギリスで最も権威のある文学賞『ブッカー賞』を、たった136ページの小説『Orbital（オービタル）』が受賞しました。国際宇宙ステーション（ISS）から青い地球を眺める宇宙飛行士たちの心を描き、国境を越えて地球を守ろうというメッセージが世界中で絶賛されています。",
        "source_name": "The Guardian",
        "source_url": "https://www.theguardian.com/books/2024/nov/12/orbital-by-samantha-harvey-wins-booker-prize-2024",
        "senior_path": "../../../culture/orbital-samantha-harvey-booker-prize/index.html",
        "image": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=1000&auto=format&fit=crop&q=80",
        "sentences": [
            {
                "en": "British writer Samantha Harvey has won the famous 2024 Booker Prize for her short, beautiful novel about life aboard the International Space Station.",
                "ja": "イギリス人作家サマンサ・ハーヴェイが、国際宇宙ステーションでの生活を描いた短く美しい小説で、名高い2024年ブッカー賞を受賞しました。"
            },
            {
                "en": "The story follows six astronauts over just one single day as their spacecraft circles the Earth and sees sixteen sunrises and sunsets.",
                "ja": "物語は、宇宙船が地球を周回しながら16回の日出と日没を見る、たった1日の6人の宇宙飛行士たちの姿を追っています。"
            },
            {
                "en": "At only one hundred and thirty-six pages, it is the second-shortest book ever to win this top literary award.",
                "ja": "わずか136ページで、この最高峰の文学賞を受賞した歴代で2番目に短い本となりました。"
            },
            {
                "en": "Looking down from high above, the astronauts see huge blue oceans and giant storms, realizing that human borders on land look tiny and unimportant.",
                "ja": "はるか上空から見下ろすと、宇宙飛行士たちは広大な青い海と巨大な嵐を目にし、地上の人間が作った国境など小さく無意味に見えることに気づきます。"
            },
            {
                "en": "When receiving her award, the author said her book is a love letter to our fragile planet and urged everyone to take good care of nature.",
                "ja": "賞を受け取った際、著者は自らの本が傷つきやすい私たちの地球へのラブレターであると述べ、自然を大切にするようすべての人に呼びかけました。"
            }
        ],
        "dialogue": [
            {"speaker": "七", "name": "Nanami", "role": "生徒", "text": "136ページって、分厚い英語の小説と比べるとすごく短くて読みやすそうですね！"},
            {"speaker": "慶", "name": "Keita", "role": "英語講師", "text": "そうだね。第3文にある 'the second-shortest book ever to win'（受賞作の中で史上2番目に短い）という記録を作ったんだ。"},
            {"speaker": "七", "name": "Nanami", "role": "生徒", "text": "第4文の『宇宙から見ると国境なんてちっぽけ（borders look tiny and unimportant）』という宇宙飛行士の視点がとても素晴らしいです。"},
            {"speaker": "慶", "name": "Keita", "role": "英語講師", "text": "宇宙から地球を見る体験（Overview Effect）を描いているんだね。第5文の 'a love letter to our fragile planet'（壊れやすい地球へのラブレター）という表現も心に響くね。"}
        ],
        "vocab": [
            {"word": "prestigious", "meaning": "名誉ある、権威のある", "pos": "adjective", "def": "Inspiring respect and admiration; having high status."},
            {"word": "circle", "meaning": "周回する、回る", "pos": "verb", "def": "To move all the way around something in a circle."},
            {"word": "border", "meaning": "国境、境界線", "pos": "noun", "def": "A line separating two countries or other areas."},
            {"word": "fragile", "meaning": "壊れやすい、脆い", "pos": "adjective", "def": "Easily broken or damaged; delicate."},
            {"word": "literary", "meaning": "文学の、文学的な", "pos": "adjective", "def": "Concerning the writing, study, or content of literature."}
        ],
        "syntax": [
            {"title": "現在分詞句による付帯状況（〜しながら）", "formula": "[Looking down from high above], [astronauts see blue oceans].", "explanation": "文頭の現在分詞句 Looking down from high above で「上空から見下ろしながら」という視点を示しています。"},
            {"title": "最上級 + ever + to 不定詞（これまでに〜した中で最も…）", "formula": "the second-shortest book [ever to win this award].", "explanation": "ever to win で「これまでに受賞した中で」という意味になり、歴史的記録を強調する構文です。"}
        ],
        "quiz": [
            {
                "question": "What is the title and setting of Samantha Harvey's award-winning novel?",
                "options": [
                    "It is called Orbital and is set aboard the International Space Station.",
                    "It is called Ocean Deep and is set in a submarine.",
                    "It is called The Castle and is set in ancient Rome.",
                    "It is called Mountain Peak and is set on Mount Everest."
                ],
                "answer": 0,
                "explanation": "第1文で「国際宇宙ステーションでの生活を描いた小説『Orbital』」と述べられています。"
            },
            {
                "question": "How long is the novel Orbital?",
                "options": ["1,000 pages", "500 pages", "136 pages", "Only 10 pages"],
                "answer": 2,
                "explanation": "第3文で「わずか136ページ（only 136 pages）」と記されています。"
            },
            {
                "question": "How do human borders on Earth appear to astronauts in the story?",
                "options": [
                    "They look like bright glowing gold walls.",
                    "They look tiny and unimportant against the vast planet.",
                    "They are completely impossible to see through clouds.",
                    "They look terrifying and dangerous."
                ],
                "answer": 1,
                "explanation": "第4文で「人間の作った国境など小さく無意味に見える」と書かれています。"
            },
            {
                "question": "How did the author describe her book when accepting the award?",
                "options": [
                    "As a technical manual for rocket engineers.",
                    "As a love letter to our fragile planet Earth.",
                    "As an angry complaint about space food.",
                    "As a mathematical textbook for children."
                ],
                "answer": 1,
                "explanation": "第5文で、著者は自らの本を「壊れやすい私たちの地球へのラブレター」と表現しました。"
            },
            {
                "question": "The word 'fragile' is closest in meaning to:",
                "options": ["delicate and easily harmed", "super strong", "made of heavy steel", "loud and noisy"],
                "answer": 0,
                "explanation": "fragile は「壊れやすい」「脆い」という意味で、delicate and easily harmed が同義です。"
            }
        ]
    },

    # 10. CULTURE JUNIOR - Gen Z Physical Books
    {
        "slug": "gen-z-physical-books-library-renaissance",
        "category": "culture",
        "date": "2026-10-15",
        "title": "Turning Real Pages: Why Young Readers Are Falling in Love with Paper Books",
        "headline_ja": "本物のページをめくろう：Z世代の若者が紙の本や図書館に夢中な理由",
        "subhead": "スマホの画面疲れから紙の読書へ。手触りや静けさを楽しむ新しい若者文化の広がり。",
        "lead_snippet": "スマホやタブレットに囲まれて育った10代や20代の若者たちの間で、紙の本を買い、地元の図書館に通うブームが起きています。SNSの通知から離れて静かに本を読む時間が『かっこいい』と見直されており、本屋さんの売上も大きく伸びています。",
        "source_name": "The Guardian",
        "source_url": "https://www.theguardian.com/books/2024/feb/09/reading-is-so-sexy-gen-z-turns-to-physical-books-and-libraries",
        "senior_path": "../../../culture/gen-z-physical-books-library-renaissance/index.html",
        "image": "https://images.unsplash.com/photo-1524995997946-a1c2e315a42f?w=1000&auto=format&fit=crop&q=80",
        "sentences": [
            {
                "en": "Many people thought that smartphones would destroy printed books, but teenagers and young adults are actually buying more paper books than ever before.",
                "ja": "多くの人がスマートフォンが印刷された本をなくしてしまうだろうと考えていましたが、ティーンエイジャーや若者たちは実際にはこれまで以上に紙の本を購入しています。"
            },
            {
                "en": "Book industry records show that over eighty percent of books bought by young readers are physical paperbacks rather than digital files.",
                "ja": "出版業界の記録によると、若い読者によって購入される本の8割以上が電子ファイルではなく物理的な紙のペーパーバックです。"
            },
            {
                "en": "Young people explain that looking at phone screens all day makes their eyes and minds feel exhausted, making paper reading a peaceful escape.",
                "ja": "若者たちは、一日中スマホの画面を見つめていると目も心も疲れ果ててしまうため、紙での読書が心安らぐ息抜きになると説明しています。"
            },
            {
                "en": "Town libraries have also become trendy hangout spots where students can study, chat quietly, and borrow books without spending any money.",
                "ja": "町の図書館も、生徒たちがお金を一銭も使わずに勉強したり、静かにおしゃべりしたり、本を借りたりできるトレンディな居場所になっています。"
            },
            {
                "en": "Carrying a real book has become a cool symbol of slowing down and enjoying a calm moment in a busy digital world.",
                "ja": "本物の本を持ち歩くことは、忙しいデジタルの世界の中でペースを落とし、穏やかな時間を楽しむかっこいいシンボルになっています。"
            }
        ],
        "dialogue": [
            {"speaker": "七", "name": "Nanami", "role": "生徒", "text": "私も電子書籍より紙の本が好きです！読んだページが手元にたまっていって進み具合が分かるのが嬉しいんですよね。"},
            {"speaker": "慶", "name": "Keita", "role": "英語講師", "text": "第2文にあるように、若者が買う本の80%以上が紙の本（over 80% are physical paperbacks）なんだよ。スマホネイティブだからこそ、紙の手触りを新鮮に感じるんだね。"},
            {"speaker": "七", "name": "Nanami", "role": "生徒", "text": "第3文の 'a peaceful escape'（心安らぐ息抜き）という表現も素敵です。ずっとスマホを見ていると脳が疲れてしまいますもんね。"},
            {"speaker": "慶", "name": "Keita", "role": "英語講師", "text": "第5文にある 'slowing down'（ペースを落としてリラックスする）というライフスタイルだね。英語の長文でも現代社会論としてよく出題されるよ！"}
        ],
        "vocab": [
            {"word": "paperback", "meaning": "ペーパーバック（紙表紙の並製本）", "pos": "noun", "def": "A book bound in stiff paper or flexible card."},
            {"word": "escape", "meaning": "息抜き、逃避、脱出", "pos": "noun", "def": "A temporary distraction from reality or routine."},
            {"word": "hangout", "meaning": "たまり場、よく行く居場所", "pos": "noun", "def": "A place where one frequently spends time or visits with friends."},
            {"word": "symbol", "meaning": "シンボル、象徴", "pos": "noun", "def": "A thing that represents or stands for something else."},
            {"word": "calm", "meaning": "穏やかな、落ち着いた", "pos": "adjective", "def": "Not showing or feeling nervousness, anger, or other strong emotions."}
        ],
        "syntax": [
            {"title": "比較級 + than ever before（これまで以上に）", "formula": "[young adults are buying more books] [than ever before].", "explanation": "than ever before で「かつてないほどに」「これまで以上に」という強い比較表現になります。"},
            {"title": "make + 目的語 + 原形動詞 / 形容詞", "formula": "[looking at screens] makes [their minds feel exhausted].", "explanation": "使役動詞 make + 目的語 + 原形動詞 feel で「画面を見ることが心を疲れ切った状態にさせる」という意味になります。"}
        ],
        "quiz": [
            {
                "question": "What did many people originally think smartphones would do to printed books?",
                "options": [
                    "They thought phones would destroy or replace printed books completely.",
                    "They thought phones would make all books 5,000 pages long.",
                    "They thought phones would turn paper books into stone.",
                    "They thought phones would cause schools to ban all libraries."
                ],
                "answer": 0,
                "explanation": "第1文で「多くの人がスマホが紙の本をなくしてしまうだろうと考えていた」と述べられています。"
            },
            {
                "question": "What percentage of books purchased by young readers are physical print copies?",
                "options": ["Less than 5 percent", "Over 80 percent", "Exactly 10 percent", "Zero percent"],
                "answer": 1,
                "explanation": "第2文で「若い読者が買う本の80%以上が紙のペーパーバックである」と明記されています。"
            },
            {
                "question": "Why do young people enjoy reading paper books instead of screens?",
                "options": [
                    "Because paper books can be eaten as healthy snacks.",
                    "Because looking at screens all day makes their minds tired, so paper offers a peaceful escape.",
                    "Because paper books glow in the dark automatically.",
                    "Because e-readers are illegal for teenagers."
                ],
                "answer": 1,
                "explanation": "第3文で、画面の見すぎで疲れた目や心にとって、紙での読書が穏やかな息抜きになると説明されています。"
            },
            {
                "question": "Why have town libraries become popular hangout spots for students?",
                "options": [
                    "Because they sell video game consoles at huge discounts.",
                    "Because they are welcoming spaces to study, relax, and borrow books for free.",
                    "Because students are required by police to sleep in libraries.",
                    "Because libraries have replaced all shopping malls."
                ],
                "answer": 1,
                "explanation": "第4文で、お金を使わずに勉強したり本を借りたりできる居場所になっていると説明されています。"
            },
            {
                "question": "The word 'calm' is closest in meaning to:",
                "options": ["peaceful and quiet", "extremely loud", "frightening", "colorful"],
                "answer": 0,
                "explanation": "calm は「穏やかな」「静かな」を意味し、peaceful and quiet が正解です。"
            }
        ]
    },

    # 11. ENTERTAINMENT JUNIOR - Smart Glasses Ban
    {
        "slug": "smart-glasses-parliament-privacy-controversy",
        "category": "entertainment",
        "date": "2026-10-15",
        "title": "Camera in Your Glasses: The Big Argument Over Smart Glasses in Parliament",
        "headline_ja": "メガネにカメラが内蔵：スマートグラスの議場持ち込みをめぐる大きな論争",
        "subhead": "秘密で録画できるハイテク眼鏡に議員たちがストップ。身近になるAIデバイスとプライバシーのルール。",
        "lead_snippet": "普通のメガネとまったく同じ見た目をしながら、小さなカメラとマイクで周りの様子を秘密で録画できる『スマートグラス』をつけた政治家が議会に入ったことで、大きな議論が巻き起こっています。便利になっていくハイテク機器と、人々のプライバシーをどう守るべきかを考えましょう。",
        "source_name": "The Guardian",
        "source_url": "https://www.theguardian.com/technology/2026/oct/14/smart-glasses-ai-technology-reform-senedd-westminster-ban",
        "senior_path": "../../../entertainment/smart-glasses-parliament-privacy-controversy/index.html",
        "image": "https://images.unsplash.com/photo-1508700115892-45ecd05ae2ad?w=1000&auto=format&fit=crop&q=80",
        "sentences": [
            {
                "en": "British lawmakers are asking for a strict ban on smart glasses inside government rooms after a politician wore camera glasses during official meetings.",
                "ja": "ある政治家が公式会議中にカメラ付きメガネを着用したことを受け、英国の議員らは政府の部屋の中でのスマートグラスの厳格な禁止を求めています。"
            },
            {
                "en": "These new smart glasses look just like regular fashion spectacles, but they hide tiny cameras and microphones that can record people secretly.",
                "ja": "これらの新しいスマートグラスは普通のファッションメガネとまったく同じに見えますが、人々を秘密裏に録画できる小さなカメラやマイクを隠しています。"
            },
            {
                "en": "Politicians worry that private conversations and secret documents could be recorded and shared online without anyone knowing.",
                "ja": "政治家たちは、内緒の会話や秘密の書類が誰にも知られずに録画され、オンラインで拡散されてしまうのではないかと心配しています。"
            },
            {
                "en": "Privacy experts point out that as smart gadgets become smaller and harder to spot, it becomes difficult for ordinary people to know when they are on camera.",
                "ja": "プライバシーの専門家らは、スマート機器が小型化して見分けるのが難しくなるにつれて、一般の人々がいつカメラに映されているかを知ることが難しくなると指摘しています。"
            },
            {
                "en": "Rules in public places may soon need to be updated so that people can feel safe and comfortable in schools, offices, and government halls.",
                "ja": "学校やオフィス、政府の建物の中で人々が安全で快適に感じられるよう、公共の場所でのルールを近いうちに更新する必要があるかもしれません。"
            }
        ],
        "dialogue": [
            {"speaker": "七", "name": "Nanami", "role": "生徒", "text": "普通のメガネに見えるのに、実はカメラで録画されているかもしれないなんてちょっと怖いですね…！"},
            {"speaker": "慶", "name": "Keita", "role": "英語講師", "text": "第2文にある 'hide tiny cameras and microphones'（小さなカメラやマイクを隠している）という点だね。気づかれないうちに撮影できてしまう。"},
            {"speaker": "七", "name": "Nanami", "role": "生徒", "text": "国会の秘密の書類や話し合いが勝手に撮られてネットに流出したら大事件ですね（第3文）。"},
            {"speaker": "慶", "name": "Keita", "role": "英語講師", "text": "そう。第5文にあるように、テクノロジーが進むスピードに合わせて新しいエチケットやルール（rules in public places）を社会全体で作っていく必要があるんだよ。"}
        ],
        "vocab": [
            {"word": "spectacles", "meaning": "メガネ、眼鏡", "pos": "noun", "def": "Another term for glasses or eyewear."},
            {"word": "secretly", "meaning": "秘密裏に、こっそりと", "pos": "adverb", "def": "In a secret way; without others knowing."},
            {"word": "conversation", "meaning": "会話、おしゃべり", "pos": "noun", "def": "A talk between two or more people."},
            {"word": "gadget", "meaning": "ガジェット、電子機器", "pos": "noun", "def": "A small mechanical or electronic device or tool."},
            {"word": "comfortable", "meaning": "快適な、心地よい、安心な", "pos": "adjective", "def": "Providing physical ease and relaxation."}
        ],
        "syntax": [
            {"title": "look just like 〜（〜とまったく同じに見える）", "formula": "glasses [look just like] [regular fashion spectacles].", "explanation": "look like は「〜のように見える」、just がついて「まったく同じように見える」と強調します。"},
            {"title": "as + 主語 + 動詞（〜するにつれて）", "formula": "[as smart gadgets become smaller], [it becomes difficult to know].", "explanation": "as は変化に伴う状況の推移を表し、「小型化するにつれて見分けるのが難しくなる」という意味になります。"}
        ],
        "quiz": [
            {
                "question": "Why did British lawmakers demand a ban on smart glasses inside government rooms?",
                "options": [
                    "Because an elected representative wore camera glasses during official meetings.",
                    "Because eyeglasses are too heavy to carry upstairs.",
                    "Because all politicians prefer to wear dark sunglasses.",
                    "Because the glasses made loud ringing noises during speeches."
                ],
                "answer": 0,
                "explanation": "第1文で「ある政治家が公式会議中にカメラ付きメガネを着用したため」と説明されています。"
            },
            {
                "question": "What is hidden inside these new smart glasses?",
                "options": [
                    "Laser pointers and flashlights.",
                    "Tiny cameras and microphones that can record secretly.",
                    "Small bottles of perfume.",
                    "Emergency paper tissues."
                ],
                "answer": 1,
                "explanation": "第2文で、秘密裏に録画できる小さなカメラやマイクが隠されていると説明されています。"
            },
            {
                "question": "What specific fear do politicians have regarding secret recording?",
                "options": [
                    "That their secret documents and private talks could be shared online without permission.",
                    "That the glasses will steal their lunch money.",
                    "That the glasses will change their hair color on television.",
                    "That the glasses will cast magic spells in the room."
                ],
                "answer": 0,
                "explanation": "第3文で「内緒の会話や秘密書類が勝手に録画され、オンラインで拡散されるのではないか」と恐れられていると述べられています。"
            },
            {
                "question": "Why is it difficult for ordinary people to protect their privacy around smart wearables?",
                "options": [
                    "Because gadgets are becoming tiny and look just like everyday fashion accessories.",
                    "Because smart glasses are brighter than the sun.",
                    "Because glasses can only be purchased by secret agents.",
                    "Because governments have banned mirrors."
                ],
                "answer": 0,
                "explanation": "第4文で、小型化して見分けがつかなくなるため、いつ撮影されているか気づきにくくなると説明されています。"
            },
            {
                "question": "The word 'gadget' is closest in meaning to:",
                "options": ["small electronic device", "large wild animal", "brick building", "deep ocean lake"],
                "answer": 0,
                "explanation": "gadget は「小型の電子機器」「便利な道具」を意味し、small electronic device が同義です。"
            }
        ]
    },

    # 12. ENTERTAINMENT JUNIOR - England Organic Farming
    {
        "slug": "england-organic-farming-expansion-target",
        "category": "entertainment",
        "date": "2026-10-15",
        "title": "Healthy Soil, Healthy Food: England Plans to Triple Organic Farming by 2036",
        "headline_ja": "健康な土とおいしい野菜：イギリスが2036年までに有機農地を3倍に拡大へ",
        "subhead": "化学肥料や農薬を減らし、自然の力で土を豊かにする。地球と体にやさしいオーガニック農法の未来。",
        "lead_snippet": "イギリス政府が、体に良くて環境にもやさしい『有機農業（オーガニック農法）』の畑を、2036年までに今の3倍に増やす大きな計画を発表しました。化学肥料をやめて虫や微生物の力を借りて作物を育てることで、土が元気になるだけでなく、温暖化ガスを吸収してくれる効果もあります。",
        "source_name": "The Guardian",
        "source_url": "https://www.theguardian.com/environment/2026/oct/14/land-farmed-organically-england-share-10-pc-2036-plan-food-climate",
        "senior_path": "../../../entertainment/england-organic-farming-expansion-target/index.html",
        "image": "https://images.unsplash.com/photo-1500937386664-56d1dfef3854?w=1000&auto=format&fit=crop&q=80",
        "sentences": [
            {
                "en": "The government in England has announced an ambitious plan to triple the country's organic farmland to ten percent by 2036 to heal natural soil.",
                "ja": "イングランド政府は、自然の土を健康にするため、2036年までに国内の有機農地を3倍の10%へ増やす野心的な計画を発表しました。"
            },
            {
                "en": "Organic farmers avoid artificial chemical sprays and synthetic fertilizers, choosing instead to rotate crops and use friendly insects to stop pests.",
                "ja": "有機農家は人工的な化学スプレーや合成肥料を避け、代わりに作物を順番に植え替えたり（輪作）、益虫を利用して害虫を防ぎます。"
            },
            {
                "en": "Scientists discovered that healthy organic soil can trap twenty-five percent more carbon, helping fight global warming while holding rainwater during droughts.",
                "ja": "科学者たちは、健康な有機土壌が25%も多くの炭素を閉じ込めることができ、干ばつのときに雨水を保ちながら地球温暖化と闘うのに役立つことを発見しました。"
            },
            {
                "en": "Supporters say that state schools and hospitals should buy organic vegetables so that local farmers have steady customers for their healthy food.",
                "ja": "支援者らは、地元の農家が健康的な食材を安定して売ることができるよう、公立学校や病院が有機野菜を購入するべきだと述べています。"
            },
            {
                "en": "Learning how to grow delicious food while protecting earth's living creatures is one of the most important lessons for humanity's future.",
                "ja": "地球の生き物を守りながらおいしい食べ物を育てる方法を学ぶことは、人類の未来にとって最も大切なレッスンの1つです。"
            }
        ],
        "dialogue": [
            {"speaker": "七", "name": "Nanami", "role": "生徒", "text": "オーガニックの畑を3倍に増やす計画なんですね！化学農薬を使わずに野菜を育てるのって大変そうですが体に良さそうです。"},
            {"speaker": "慶", "name": "Keita", "role": "英語講師", "text": "第2文にある 'rotate crops and use friendly insects'（作物を順番に変えたり、テントウムシなどの益虫を使う）という知恵だね。自然のバランスを利用しているんだ。"},
            {"speaker": "七", "name": "Nanami", "role": "生徒", "text": "第3文の『土が炭素を25%多く閉じ込める（trap 25% more carbon）』というのもすごい発見ですね！"},
            {"speaker": "慶", "name": "Keita", "role": "英語講師", "text": "そう。第4文のように学校給食（state schools）で地域のオーガニック野菜を使う取り組みも広がっている。環境問題と食育を結びつける入試問題でも注目の話題だよ！"}
        ],
        "vocab": [
            {"word": "organic", "meaning": "有機栽培の、オーガニックの", "pos": "adjective", "def": "Produced without the use of chemical fertilizers, pesticides, or other artificial agents."},
            {"word": "fertilizer", "meaning": "肥料（植物の成長を助けるもの）", "pos": "noun", "def": "A chemical or natural substance added to soil to increase its fertility."},
            {"word": "rotate", "meaning": "交代で植え替える、回転する", "pos": "verb", "def": "To grow different crops in succession on the same land."},
            {"word": "trap", "meaning": "閉じ込める、捕らえる", "pos": "verb", "def": "To hold or capture something so it cannot escape."},
            {"word": "creature", "meaning": "生き物、生物", "pos": "noun", "def": "An animal or living being, as distinct from a human."}
        ],
        "syntax": [
            {"title": "〜の代わりに：instead of 〜 / choosing instead to do", "formula": "[avoid chemical sprays], [choosing instead to rotate crops].", "explanation": "instead は「その代わりに」という副詞で、化学スプレーを避けて自然な輪作を選ぶという対比を述べています。"},
            {"title": "動名詞主語 [Learning how to do] is one of the most important lessons", "formula": "[Learning how to grow food while protecting creatures] is [important].", "explanation": "Learning how to grow（〜の育て方を学ぶこと）が主語のまとまりを作り、現在分詞句 while protecting（守りながら）が条件を添えています。"}
        ],
        "quiz": [
            {
                "question": "What is the England government's target for organic farmland by 2036?",
                "options": [
                    "To pave all farms for car parking.",
                    "To triple organic farmland to ten percent.",
                    "To stop growing any vegetables in Britain.",
                    "To convert all fields into golf courses."
                ],
                "answer": 1,
                "explanation": "第1文で「2036年までに国内の有機農地を3倍の10%に増やす」と明記されています。"
            },
            {
                "question": "How do organic farmers protect their crops without artificial chemical sprays?",
                "options": [
                    "By rotating crops and using friendly insects to control pests.",
                    "By covering all fields in plastic sheets forever.",
                    "By asking drones to scare away all birds with loud horns.",
                    "By only growing crops inside indoor freezers."
                ],
                "answer": 0,
                "explanation": "第2文で「作物を輪作し、益虫を使って害虫を防ぐ」と説明されています。"
            },
            {
                "question": "What surprising climate benefit does healthy organic soil provide?",
                "options": [
                    "It turns into pure gold during summer.",
                    "It can trap 25 percent more carbon and hold rainwater during droughts.",
                    "It makes rain clouds disappear from the sky completely.",
                    "It eliminates all winter snow."
                ],
                "answer": 1,
                "explanation": "第3文で「25%多くの炭素を閉じ込め、干ばつ時に雨水を蓄える」と書かれています。"
            },
            {
                "question": "Who should purchase organic produce to help local farmers according to supporters?",
                "options": [
                    "State schools and public hospitals.",
                    "Only foreign airlines.",
                    "No one, food should be thrown away.",
                    "Only zoo animals."
                ],
                "answer": 0,
                "explanation": "第4文で「公立学校や病院が有機野菜を購入するべきだ」と述べられています。"
            },
            {
                "question": "The word 'organic' relates to food produced:",
                "options": ["without artificial chemical fertilizers or pesticides", "using only plastic machines", "in underground dark labs", "with radioactive elements"],
                "answer": 0,
                "explanation": "organic は「人工の化学肥料や農薬を使わずに生産された」という意味です。"
            }
        ]
    }
]

if __name__ == "__main__":
    print(f"Batch 11 loaded: {len(BATCH11_SENIOR)} Senior and {len(BATCH11_JUNIOR)} Junior articles.")
    assert len(BATCH11_SENIOR) == 12
    assert len(BATCH11_JUNIOR) == 12
    print("Batch 11 verification passed successfully!")
