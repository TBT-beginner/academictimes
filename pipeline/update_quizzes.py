# -*- coding: utf-8 -*-
"""
Expands interactive quizzes across all articles in articles_data.py
to 3 high-caliber, academic university entrance-exam standard questions per article.
"""
import sys
import os
import pprint

sys.path.append(os.path.dirname(__file__))
from articles_data import ARTICLES

QUIZ_UPDATES = {
    "air-defence-shield": [
        {
            "question": "文中の 'render' と文法構造・意味が最も近い動詞の用法はどれですか。<br><em>\"Defence analysts testify that the unprecedented proliferation of low-cost autonomous drones has <strong>rendered</strong> conventional radar networks largely obsolete.\"</em>",
            "options": [
                "He made his opinion clear to the committee.",
                "She gave a memorable performance on stage.",
                "They translated the ancient document into English.",
                "The court provided legal counsel for the defendant."
            ],
            "correct_index": 0,
            "explanation": "【正解：A】<br>文中の render は make O C と同様に「OをC（の状態）にする」という第5文型（SVOC）の使役的用法です（conventional radar networks が O、obsolete が C）。選択肢 A の <em>made his opinion clear</em> も同一の SVOC 構造（his opinion が O、clear が C）です。"
        },
        {
            "question": "文4の <em>\"allocating emergency funds requires balancing sovereign security prerogatives against long-standing principles of public accountability\"</em> の論理的骨格として最も適切な解釈はどれですか。",
            "options": [
                "緊急資金の配分においては、国家の防衛権限の行使が議会の公的説明責任よりも常に優先されるべきである。",
                "安全保障上の主権的特権を維持することと、国民に対する財政的説明責任を果たすことの双方の釣り合い（比較衡量）をとる必要がある。",
                "従来の公的説明責任の原則を完全に破棄しなければ、迅速な主権防衛の資金を確保することは不可能である。",
                "議会の法定監視を強めすぎると、国家主権に基づく緊急配分の正当性が法的に損なわれてしまう。"
            ],
            "correct_index": 1,
            "explanation": "【正解：B】<br><code>balance A against B</code> は「AとBを天秤にかける・比較衡量して調和させる」という法学・政策論述の最重要構文です。主権に基づく安全保障の要請（A）と、長年培われた公的説明責任の原則（B）の両立・均衡が求められていることを述べています。一方を完全に犠牲にするAやCは文意と矛盾します。"
        },
        {
            "question": "英国議会で100億ポンド規模の防空シールド計画に対して反対派議員が懸念を示している最大の論点は何ですか。",
            "options": [
                "安価なドローンの技術が不十分であり、従来のレーダー網の方が信頼性が高いため。",
                "巨額に膨らむ財政負担が、確立された議会の厳格な法的監視手続きを骨抜き（回避）にすること。",
                "欧州諸国との集団安全保障協定に違反して、英国独自の防衛網を単独で構築しようとしていること。",
                "民間防衛企業への過度な補助金支出により、行政法上の透明性が完全に喪失していること。"
            ],
            "correct_index": 1,
            "explanation": "【正解：B】<br>文3に <em>\"ballooning fiscal commitments must not circumvent established parliamentary scrutiny\"</em>（膨らみ続ける財政負担が確立された議会の精査を回避してはならない）と明記されており、Bが正解です。安価なドローンによって旧来のレーダー網が無力化（obsolete）されているため、Aは本文と真逆です。"
        }
    ],

    "colorectal-cancer-under-50s": [
        {
            "question": "文中の 'ubiquitous' と最も近い意味を持つ単語はどれですか。<br><em>\"...hypothesize that the <strong>ubiquitous</strong> consumption of ultra-processed foods disrupts the delicate equilibrium...\"</em>",
            "options": [
                "pervasive",
                "nutritious",
                "sporadic",
                "confidential"
            ],
            "correct_index": 0,
            "explanation": "【正解：A】<br>ubiquitous は「至る所にある、広く行き渡った」という意味の学術形容詞で、同義語は A の pervasive（充満した、浸透した）です。C の sporadic（散発的な、時々起こる）は反意語です。"
        },
        {
            "question": "文2 <em>\"While historical data correlated gastrointestinal malignancies primarily with cellular senescence, younger patients now present with biologically aggressive, late-stage tumors.\"</em> における接続詞 <strong>While</strong> の用法・意味として最も適切なものはどれですか。",
            "options": [
                "「〜している間に」（時間を表す従属接続詞）",
                "「〜である一方で」（事実や学説の対比・譲歩を示す接続詞）",
                "「〜である限りは」（条件・期間を表す接続詞）",
                "「〜であるにもかかわらず」（原因・結果の因果関係を示す接続詞）"
            ],
            "correct_index": 1,
            "explanation": "【正解：B】<br>ここでの While は時間を表すものではなく、「従来の知見（高齢者の細胞老化との相関）がある一方で、若年層の患者はそれとは異なり進行の速い末期腫瘍を呈している」という【事実の対比（contrast）】を表しています。大学入試の学術論説文で最も狙われる While の用法です。"
        },
        {
            "question": "若年層における大腸がん急増の要因として、本文中で臨床研究者や毒性学者から提起されている仮説の組み合わせとして最も適切なものはどれですか。",
            "options": [
                "高齢化による免疫機能の自然低下と、遺伝子治療薬の副作用",
                "超加工食品の日常的摂取による腸内細菌叢の乱れと、微小プラスチック蓄積による慢性的な潜在性炎症",
                "運動不足による消化管運動の低下と、抗生物質の過剰処方によるアレルギー反応",
                "早期検診政策の不備による発見遅れと、大気汚染物質の直接吸入"
            ],
            "correct_index": 1,
            "explanation": "【正解：B】<br>文3に <em>\"ultra-processed foods disrupts the delicate equilibrium of the human gut microbiome\"</em>（超加工食品による腸内細菌叢の破壊）、文4に <em>\"chronic microplastic accumulation induces persistent subclinical inflammation\"</em>（慢性的なマイクロプラスチック蓄積による潜在性炎症）が明記されています。"
        }
    ],

    "raf-fairford-bomber-redeployment": [
        {
            "question": "文脈上、米欧州軍による 'dispersal doctrines（兵力分散ドクトリン）' が実施された真の目的として最も適切なものはどれですか。<br><em>\"Strategic scholars observe that dispersal doctrines are intended not to signal retreat, but rather to reinforce deterrence by denying adversaries an easy preemptive strike.\"</em>",
            "options": [
                "To permanently dismantle long-range bomber capabilities in Europe.",
                "To avoid preemptive attacks and maintain credible defensive deterrence.",
                "To protest against the bilateral Visiting Forces Act framework.",
                "To cut military expenditure during peacetime operations."
            ],
            "correct_index": 1,
            "explanation": "【正解：B】<br>文4に <em>\"intended not to signal retreat, but rather to reinforce deterrence by denying adversaries an easy preemptive strike\"</em> と明記されており、B（敵による先制攻撃を阻止し、確実な防衛的抑止力を維持すること）が正解です。"
        },
        {
            "question": "文3の <em>\"foreign military assets stationed on sovereign British soil operate within a tightly <strong>delineated</strong> framework of mutual jurisdictional consent.\"</em> における <strong>delineated</strong> と最も意味が近いものはどれですか。",
            "options": [
                "clearly defined",
                "randomly chosen",
                "repeatedly abolished",
                "financially supported"
            ],
            "correct_index": 0,
            "explanation": "【正解：A】<br>delineate は「（境界線や規則を）明確に画定する、輪郭をはっきり描く」という意味の学術語彙です。文脈上、英国内に駐留する米軍資産が「厳密に画定された法的枠組みの中で」運用されていることを示しており、A（clearly defined）が同義です。"
        },
        {
            "question": "文4の構文 <em>\"are intended not to signal retreat, but rather to reinforce deterrence...\"</em> に関する文法・論理の説明として最も適切なものはどれですか。",
            "options": [
                "敵に対する全面的な降伏を偽装して、相手を奇襲するための欺瞞工作を表している。",
                "「Aではなく、むしろBである」という対比構造（not A, but rather B）を用い、世間の誤解（撤退）を否定して真の軍事的意図（抑止力の強化）を強調している。",
                "過去の作戦方針と現在の作戦方針が完全に一致していることを証明する同格構文である。",
                "条件節の if が省略された仮定法過去完了の倒置構文である。"
            ],
            "correct_index": 1,
            "explanation": "【正解：B】<br><code>not A, but rather B</code> は「AではなくむしろBである」という対比構文です。世間や敵対者が「爆撃機の移動＝英欧からの撤退・弱腰」と受け取る可能性（A）を明確に退け、「先制攻撃を阻止して抑止力を盤石にするための再配置（B）」であることを論理的に際立たせています。"
        }
    ],

    "psychology-casual-encounters": [
        {
            "question": "文中の 'pluralistic ignorance（多元的無知）' の定義として最も合致するものはどれですか。<br><em>\"Sociologists attribute this chronic reluctance to pluralistic ignorance, a cognitive paradox wherein mutual desire for connection is masked by outward indifference.\"</em>",
            "options": [
                "A mental state where passengers refuse to use modern navigation systems.",
                "A situation where individuals hide their wish to connect because they assume others do not care.",
                "A lack of education among urban citizens regarding public transportation rules.",
                "An economic gap resulting from insufficient municipal investments."
            ],
            "correct_index": 1,
            "explanation": "【正解：B】<br>文3の <em>\"a cognitive paradox wherein mutual desire for connection is masked by outward indifference\"</em> から、B（他者が無関心だと思い込むあまり、自身もつながりたいという欲求を外面的な無関心で覆い隠してしまう状況）が正解です。"
        },
        {
            "question": "文3 <em>\"Sociologists attribute this chronic reluctance to pluralistic ignorance...\"</em> における動詞句 <strong>attribute A to B</strong> の解釈として最も適切なものはどれですか。",
            "options": [
                "見知らぬ他者に話しかけるのをためらう原因は、「多元的無知」という心理現象にあると考えている。",
                "「多元的無知」を解決するためには、他者へのためらいを完全に排除しなければならないと主張している。",
                "多元的無知という結果が生じたのは、人々が日常的に他者と積極的に対話したからだと結論づけている。",
                "他者とのつながりを求める欲求が、社会学研究の慢性的停滞を引き起こしていると批判している。"
            ],
            "correct_index": 0,
            "explanation": "【正解：A】<br><code>attribute A to B</code> は「A（結果・状態）をB（原因・理由）に帰する」「Aの原因はBにあると考える」という入試最頻出の因果関係構文です。ここでは「他人に話しかけようとしない慢性的ためらい（A）」の根本原因が「多元的無知（B）」にあると論じています。因果の向きを取り違えないことが極めて重要です。"
        },
        {
            "question": "空所に当てはまる語として文脈上最も適切なものを選択してください。<br><em>\"Researchers found that brief, casual interactions with store clerks and train conductors act as a powerful ( &nbsp;&nbsp;&nbsp;&nbsp; ) to urban loneliness.\"</em>",
            "options": [
                "deterrent",
                "catalyst",
                "antidote",
                "obstacle"
            ],
            "correct_index": 2,
            "explanation": "【正解：C】<br>文5にある <code>antidote to the pervasive loneliness epidemic</code>（孤独の蔓延に対する解毒剤・対抗手段）に基づいた問題です。antidote は「解毒剤、解決策」の意味。Aの deterrent（抑止力）、Bの catalyst（触媒・促進要因）、Dの obstacle（障害物）は文脈に合いません。"
        }
    ],

    "jeffrey-archer-obituary": [
        {
            "question": "文中の 'conceded' と最も近い意味の動詞はどれですか。<br><em>\"Literary critics who once dismissed his prose as formulaic melodrama eventually <strong>conceded</strong> that his mastery of unputdownable narrative suspense remained fundamentally unsurpassed.\"</em>",
            "options": [
                "acknowledged",
                "fabricated",
                "diminished",
                "prosecuted"
            ],
            "correct_index": 0,
            "explanation": "【正解：A】<br>concede は「（しぶしぶ事実を）認める、承認する」という意味で、同義語は A の acknowledge です。Bの fabricate は「捏造する」、Cの diminish は「縮小する」、Dの prosecute は「起訴する」です。"
        },
        {
            "question": "文2 <em>\"Having weathered acute financial ruin and subsequent imprisonment for perjury, Archer demonstrated an astonishing capacity for personal and professional resurrection.\"</em> の文頭にある完了分詞構文 <strong>Having weathered</strong> が表す意味・論理関係として最も適切なものはどれですか。",
            "options": [
                "破産と服役を「回避するために」、復活の能力を発揮した（目的）。",
                "深刻な経済的破綻と服役という逆境を「経験したにもかかわらず（乗り越えた上で）」、劇的な復活を遂げた（先行する事実・譲歩的背景）。",
                "もし破綻や服役を「経験していなかったならば」、決して作家として成功しなかっただろう（仮定法過去完了）。",
                "経済的成功を収めながら「同時に」、刑務所での服役を開始した（同時進行）。"
            ],
            "correct_index": 1,
            "explanation": "【正解：B】<br><code>Having + 過去分詞</code> は完了分詞構文で、主節の時制（demonstrated）よりも前の過去の出来事・経験を表します。ここでは「破産と服役という底知れぬ挫折を経験し、それを乗り越えた上で、驚くべき復活の力を発揮した」という時間の前後関係と背景を格調高く示しています。"
        },
        {
            "question": "ジェフリー・アーチャー氏の作家活動に対する批評家たちの評価の変遷として、本文の記述と合致するものはどれですか。",
            "options": [
                "当初から純文学の巨匠として激賞されていたが、晩年はマンネリ化を酷評された。",
                "初期の政治小説のみが高く評価され、その後の家族大河小説は完全に無視された。",
                "当初は型通りの陳腐なメロドラマと見なされていたが、やがて読者を引き込む圧倒的なサスペンス描写の手腕が認められた。",
                "偽証罪での服役以降、文芸批評界から永久に追放され、商業的にも大失敗した。"
            ],
            "correct_index": 2,
            "explanation": "【正解：C】<br>文3に <em>\"Literary critics who once dismissed his prose as formulaic melodrama eventually conceded that his mastery of unputdownable narrative suspense remained fundamentally unsurpassed.\"</em> とあり、かつて型通りのメロドラマと見限っていた批評家たちも、本を置かせないサスペンス構成の卓越性を認めざるを得なくなったと記述されています。"
        }
    ],

    "royal-security-judicial-review": [
        {
            "question": "文中の 'finite' と反意語の関係にある単語はどれですか。<br><em>\"...when apportioning <strong>finite</strong> taxpayer resources for domestic counter-terrorism operations.\"</em>",
            "options": [
                "boundless",
                "scarce",
                "statutory",
                "arbitrary"
            ],
            "correct_index": 0,
            "explanation": "【正解：A】<br>finite は「有限の、限られた」という意味なので、反意語は A の boundless（無限の、果てしない）です。B の scarce は「乏しい、不足した」で類義語です。"
        },
        {
            "question": "文末の <em>\"The eventual High Court precedent will critically delineate where constitutional privilege ends and the egalitarian rule of public law begins.\"</em> の意図する憲法上の論点として最も適切なものはどれですか。",
            "options": [
                "王室のメンバーには英国憲法上、いかなる場合も一般市民以上の恒久的特権が保障されるべきであるという主張。",
                "司法審査を通じて、王族であっても法の下の平等の原則に従うべきか、あるいは伝統的特権が優先されるべきかという境界線を確定すること。",
                "警察組織に対する民間警護会社の優位性を法律によって明確に確立すること。",
                "国王個人が司法府の決定をいつでも無効化できる新たな大権を制定すること。"
            ],
            "correct_index": 1,
            "explanation": "【正解：B】<br><code>where A ends and B begins</code> は「どこでAが終わり、Bが始まるか（二者の境界線・分水嶺）」を示す重要構文です。王族としての特権（constitutional privilege）と、すべての国民に公費が平等に扱われるべきという公法の支配（egalitarian rule of public law）の境界線を高等法院が判例として画定することを指しています。"
        },
        {
            "question": "内務省・政府側（Crown attorneys）が、警護体制の縮小・見直しを正当化するために主張している根拠は何ですか。",
            "options": [
                "王室メンバーが自ら警護を辞退し、民間警備会社との専属契約を希望したため。",
                "国内の対テロ作戦において、限られた納税者の資金を配分するための自由で柔軟な行政裁量を保持する必要があるため。",
                "過去の判例により、王位継承順位の低い王族には一切の公的警護が禁止されているため。",
                "警察官の不足により、ロンドン市外での武装警護が物理的に不可能になったため。"
            ],
            "correct_index": 1,
            "explanation": "【正解：B】<br>文4に <em>\"Crown attorneys insist that the executive branch must retain unhindered flexibility when apportioning finite taxpayer resources for domestic counter-terrorism operations.\"</em> と明記されています。納税者の有限な資源を対テロ作戦に配分する際、行政に柔軟な裁量（flexibility）が必要であるという主張が根拠です。"
        }
    ],

    "clarkson-business-red-tape": [
        {
            "question": "文中の 'regulatory sclerosis' が指す状態として最も適切なものはどれですか。<br><em>\"...noting that <strong>regulatory sclerosis</strong> disproportionately penalizes agile rural cooperatives...\"</em>",
            "options": [
                "Physical damage to public railway tracks.",
                "A medical disease affecting agricultural cattle.",
                "Inflexible and suffocating bureaucratic regulations.",
                "A successful tax incentive for new farm shops."
            ],
            "correct_index": 2,
            "explanation": "【正解：C】<br>文脈上、sclerosis は本来「硬化症」を意味しますが、ここでは官僚主義的な規則の硬直化・融通の利かなさを指しており、C（柔軟性を欠き、事業を息苦しくさせる官僚的規制）が正解です。"
        },
        {
            "question": "文1 <em>\"broadcaster Jeremy Clarkson queries why any rational entrepreneur would inaugurate a new enterprise in contemporary Britain.\"</em> における修辞の意図（含意）として最も適切なものはどれですか。",
            "options": [
                "現代の英国には起業を志す優秀な若者が極めて多く存在していることを賞賛している。",
                "「まともな思考力がある起業家なら、今の英国で新規開業などするはずがない」という、過酷な規制環境に対する痛烈な反語的批判。",
                "農業分野における起業家に対して、政府が多額の起業準備金を支給している事実を紹介している。",
                "どのような事業計画が最も銀行融資を受けやすいかを行政に問い合わせている。"
            ],
            "correct_index": 1,
            "explanation": "【正解：B】<br><code>queries why any rational entrepreneur would...</code> は修辞的疑問（反語）のニュアンスを含んでおり、「合理的な起業家が今の英国で会社や農場を立ち上げようとするだろうか、いや誰もしない（するわけがない）」という、官僚主義と規制だらけの英国経済に対する辛辣な批判を表現しています。"
        },
        {
            "question": "記事で指摘されている、英国の地方経済が直面している「マクロ経済的難題（perennial macroeconomic conundrum）」とはどのようなものですか。",
            "options": [
                "外国からの安価な農産物輸入を禁止すべきか、自由貿易協定を推進すべきかという対立。",
                "美しい手つかずの自然環境を景観保全することと、草の根の起業家精神や商業競争力を育てることの両立の難しさ。",
                "都市部への人口集中を是正するために、地方の農民に重税を課すべきか否かという議論。",
                "テレビ番組のロケ地としての観光収入と、地元住民の静穏な生活環境をめぐる対立。"
            ],
            "correct_index": 1,
            "explanation": "【正解：B】<br>文5に <em>\"the perennial macroeconomic conundrum between preserving pristine countryside environments and fostering grassroots commercial competitiveness\"</em>（手つかずの田園環境を保護することと、草の根の商業的競争力を育むこととの間の永遠のマクロ経済的難題）と明記されています。"
        }
    ],

    "inheritance-tax-reform-debate": [
        {
            "question": "文中の 'entrenches' と最も近い意味の動詞はどれですか。<br><em>\"...cautioning that repealing estate duties inevitably <strong>entrenches</strong> dynastic wealth disparities across generations.\"</em>",
            "options": [
                "solidifies",
                "eliminates",
                "fluctuates",
                "disguises"
            ],
            "correct_index": 0,
            "explanation": "【正解：A】<br>entrench は「（制度や格差を）強固に固定化する、定着させる」という意味で、同義語は A の solidifies です。Bの eliminate は「排除する」、Cの fluctuate は「変動する」、Dの disguise は「偽装する」です。"
        },
        {
            "question": "文4 <em>\"With unindexed tax thresholds pulling thousands of modest homeowners into higher fiscal brackets via fiscal drag, public resentment has intensified dramatically.\"</em> における <strong>With + 名詞 + 分詞</strong> の構文的役割として最も適切なものはどれですか。",
            "options": [
                "「〜という理由で / 〜の状況下で」という付帯状況・原因を表し、課税基準額の固定が引き起こした現実と市民の怒りの因果関係を説明している。",
                "主節の主語（public resentment）と意味上の主語が一致していることを表す同格構文である。",
                "「もし〜でなければ」という過去の事実に反する仮定法の条件節を導いている。",
                "手段や道具（with a knife など）を表す純粋な道具格の前置詞句である。"
            ],
            "correct_index": 0,
            "explanation": "【正解：A】<br><code>With + O + 分詞（〜ing / p.p.）</code> は「Oが〜している状態で / Oが〜であるため」という付帯状況や背景・原因を表す大学入試頻出構文です。ここではインフレ局面で税率の基準額が据え置かれたため、多くの一般的な持ち家層が増税枠に引き込まれているという客観的事実が、市民の強い不満の原因となっていることを端的に記述しています。"
        },
        {
            "question": "相続税の廃止または減税を主張する保守派・擁護論者の根拠として、本文で挙げられているものはどれですか。",
            "options": [
                "相続税を廃止すれば、海外からの富裕層移民が急増して労働力不足が解消されるから。",
                "生涯にわたり懸命に稼いだ所得に対してすでに納税してきた堅実な家庭に対する「不道徳な二重課税」であるから。",
                "ピケティの理論によれば、相続税が存在することで世襲的な格差がより一層固定化してしまうから。",
                "地方自治体が独自に相続税を徴収する方が、福祉国家の再分配機能が高まるから。"
            ],
            "correct_index": 1,
            "explanation": "【正解：B】<br>文2に <em>\"denounce it as an immoral double taxation on prudent households who have already paid lifetime levies on hard-earned earnings\"</em>（懸命に稼いだ所得に対して既に生涯課税を納めてきた堅実な世帯に対する不道徳な二重課税であると非難している）と明記されています。ピケティを引用しているのは格差固定化を懸念する「進歩派の経済学者（文3）」です。"
        }
    ],

    "ai-pediatric-diagnosis-consent": [
        {
            "question": "英国家族法理において、裁判所が親の意思を無効化（override）できる最大の法的正当化事由は何ですか。<br><em>\"Under British family jurisprudence, judicial authorities are empowered to override parental prerogatives whenever necessary to safeguard the paramount best interests of the child.\"</em>",
            "options": [
                "The proprietary profit margins of AI software developers.",
                "The paramount best interests of the child.",
                "The religious beliefs held by the presiding judges.",
                "The hospital's insurance reimbursement requirements."
            ],
            "correct_index": 1,
            "explanation": "【正解：B】<br>文4の <em>\"to safeguard the paramount best interests of the child\"</em> から、B（子どもの最優先の最善の利益を守ること）が正解です。"
        },
        {
            "question": "文2 <em>\"At issue is a proprietary deep-learning model whose predictive trajectory advocated urgent, high-risk surgical intervention...\"</em> の文頭に見られる文法構造（At issue is...）の説明として最も適切なものはどれですか。",
            "options": [
                "疑問文を作るための助動詞の倒置であり、文末にクエスチョンマークが省略されている。",
                "前置詞句（At issue：争点となって）が文頭に出て、補語と動詞が主語の前に置かれた「C + V + S」の倒置構文である。",
                "形式主語 it が省略された従属接続詞節である。",
                "関係代名詞 whose が先行詞を欠いているため生じた文法破格である。"
            ],
            "correct_index": 1,
            "explanation": "【正解：B】<br><code>At issue is X</code> は法学・政治論説の定型表現で、「争点となっているのはXである」という意味の倒置構文（C + V + S）です。本来の語順は <em>A proprietary deep-learning model ... is at issue.</em> ですが、主語が修飾節を伴って非常に長いため、文末重心の原則および争点の強調のために補語 <code>At issue</code> が文頭に配置されています。"
        },
        {
            "question": "文5の <em>\"governing physician accountability, informed consent, and the <strong>epistemic</strong> authority of artificial intelligence in clinical medicine.\"</em> における <strong>epistemic</strong> という学術語の意味として最も適切なものはどれですか。",
            "options": [
                "経済的・商業的な",
                "知識や認識に関する（認識論的な）",
                "外科的・解剖学的な",
                "秘密裏の・非公開の"
            ],
            "correct_index": 1,
            "explanation": "【正解：B】<br>epistemic は哲学・倫理学用語の epistemology（認識論）から派生した形容詞で、「知識の、認識論的な、正当化された知識に関する」という意味です。AIが出力した推論結果が「人間医師の医学的知見と同等の正当な知識的権威を持ち得るのか」という、極めて現代的な医療倫理の核心概念を指しています。"
        }
    ],

    "mediterranean-marine-heatwaves": [
        {
            "question": "文中の 'irreparable' の反意語として最も適切なものはどれですか。<br><em>\"...localized mortality events threaten <strong>irreparable</strong> biodiversity loss across continental shelf ecosystems.\"</em>",
            "options": [
                "remediable",
                "unprecedented",
                "catastrophic",
                "subterranean"
            ],
            "correct_index": 0,
            "explanation": "【正解：A】<br>irreparable は「修復できない、回復不能の」という意味なので、反意語は A の remediable（治療・修復可能な、改善できる）です。"
        },
        {
            "question": "文2 <em>\"Traditionally considered thermal refuges insulated from atmospheric volatility, deep-water cold-water coral reefs now face catastrophic physiological necrosis.\"</em> の文頭構文に関する説明として最も適切なものはどれですか。",
            "options": [
                "「〜を伝統的に考慮した後に」という能動の分詞構文である。",
                "過去分詞（considered）から始まる分詞構文で、「従来は〜と考えられていたが、現在は…に直面している」という過去の常識と現在の危機的現実との対比を際立たせている。",
                "主節の動詞 face の目的語が文頭に移動した目的語倒置である。",
                "条件を表す if 節の倒置であり、仮定法過去を表している。"
            ],
            "correct_index": 1,
            "explanation": "【正解：B】<br><code>Traditionally considered ..., S now face ...</code> は科学論説で頻出する「通説・従来の前提（過去分詞構文）」と「最新の発見・深刻な異変（主節）」を鮮やかに対比させるレトリックです。「大気変動の影響を受けない安全な熱的避難所だと伝統的に信じられていたが、実際には深海サンゴ礁が壊死の危機に瀕している」という劇的な転換を表しています。"
        },
        {
            "question": "地中海の深海サンゴ群において、局所的な死滅が「修復不可能な生物多様性の喪失（irreparable biodiversity loss）」につながる主な生物学的理由は何ですか。",
            "options": [
                "サンゴを捕食する新種の深海魚が異常繁殖しているため。",
                "石灰化生物である深海サンゴの年間成長速度が極めて微小（infinitesimal）であり、一度破壊されると再生に膨大な年月を要するため。",
                "海洋熱波によって海水の塩分濃度がゼロになってしまうため。",
                "地中海の海底火山活動が活発化し、有毒ガスを噴出しているため。"
            ],
            "correct_index": 1,
            "explanation": "【正解：B】<br>文4に <em>\"Because these ancient calcifying organisms grow at infinitesimal annual rates, localized mortality events threaten irreparable biodiversity loss...\"</em>（これらの古代の石灰化生物は年間ごく微小な速度でしか成長しないため、局所的な死滅現象が回復不能の喪失を脅かす）と明記されており、成長速度の遅さが回復不能な被害の直接要因です。"
        }
    ],

    "generative-ai-paleontology": [
        {
            "question": "文中の 'debunk' の意味として最も適切なものはどれですか。<br><em>\"The computational findings <strong>debunk</strong> long-standing cinematic caricatures, demonstrating that massive predatory carnivores prioritized energy conservation...\"</em>",
            "options": [
                "Expose the falseness of a widely held misconception.",
                "Replicate an ancient fossil using 3D printing tools.",
                "Extrapolate future climate changes from historic rocks.",
                "Celebrate the achievements of cinematic entertainment."
            ],
            "correct_index": 0,
            "explanation": "【正解：A】<br>debunk は「誤りや俗説の化けの皮を暴く」という意味なので、A（広く信じられている誤解の虚偽性を暴く）が正解です。"
        },
        {
            "question": "文4 <em>\"demonstrating that massive predatory carnivores prioritized energy conservation over breakneck pursuit speeds.\"</em> における <strong>prioritized A over B</strong> の意味として最も適切なものはどれですか。",
            "options": [
                "猛烈な追跡速度を出すために、エネルギーの節約を完全に犠牲にした。",
                "追跡速度の速さとエネルギーの節約を同等に重要視していた。",
                "猛スピードでの獲物の追跡よりも、エネルギーの効率的節約を優先させていた。",
                "映画のような迫力ある動きを再現するために、筋肉の質量を優先させた。"
            ],
            "correct_index": 2,
            "explanation": "【正解：C】<br><code>prioritize A over B</code> は「BよりもAを優先する」という基本かつ重要構文です。巨大な肉食恐竜（ティラノサウルス等）が、映画で描かれるような「時速50キロで疾走する描写」とは異なり、無駄なエネルギー浪費を抑える生体力学的制約を優先していたことが計算科学によって示されたと述べています。"
        },
        {
            "question": "古生物学において深層学習（生成AI）を導入したことの学術的意義として、文末で述べられているものはどれですか。",
            "options": [
                "化石を物理的に発掘する必要が完全に不要になったこと。",
                "単なる化石の外見を記述・スケッチする従来の「記述的自然史」から、仮説を検証・予測できる「実験的科学」へと学問を進化させたこと。",
                "絶滅した恐竜のクローンを遺伝子工学によって実際に再生することに成功したこと。",
                "映画産業向けに、よりリアルで恐ろしいCGモンスターを安価に制作できるようになったこと。"
            ],
            "correct_index": 1,
            "explanation": "【正解：B】<br>文5に <em>\"transforming descriptive natural history into a predictive experimental discipline\"</em>（記述的な自然史を予測的な実験科学へと変革している）と明記されています。過去の骨格標本を分類・スケッチするだけの学問から、物理シミュレーションとAIによって機能や運動を予測・検証する学問への質的転換が強調されています。"
        }
    ]
}

def update_articles():
    articles_data_path = os.path.join(os.path.dirname(__file__), 'articles_data.py')
    
    # Update in memory
    for art in ARTICLES:
        slug = art['slug']
        if slug in QUIZ_UPDATES:
            art['quiz'] = QUIZ_UPDATES[slug]
            print(f"Updated quiz for {slug}: {len(art['quiz'])} questions")
            
    # Serialize back to articles_data.py
    with open(articles_data_path, 'w', encoding='utf-8') as f:
        f.write('# -*- coding: utf-8 -*-\n\nARTICLES = ')
        f.write(pprint.pformat(ARTICLES, indent=2, width=120, sort_dicts=False))
        f.write('\n')
        
    print(f"Successfully saved updated ARTICLES to {articles_data_path}")

if __name__ == '__main__':
    update_articles()
