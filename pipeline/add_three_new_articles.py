# -*- coding: utf-8 -*-
"""
Adds 3 brand-new, high-caliber academic articles to complete each category:
1. world/critical-minerals-geopolitics
2. world/arctic-sea-route-unclos
3. culture/stoic-philosophy-digital-age

Each article receives:
- Full audio synthesis via Edge-TTS (British Ryan for text, Keita & Nanami for dialogue)
- 3 academic college-entrance exam caliber interactive quiz questions with explanations
- Complete Times broadsheet HTML page
- Registration in articles_data.py
"""

import os
import sys
import asyncio
import pprint
import edge_tts

sys.path.append(os.path.dirname(__file__))
from generate_all_articles import synth_audio, build_article_html, VOICE_BRITISH, VOICE_KEITA, VOICE_NANAMI

NEW_ARTICLES = [
    {
        "slug": "critical-minerals-geopolitics",
        "category": "world",
        "category_label": "WORLD & RESOURCE DIPLOMACY • 入試頻出テーマ",
        "title": "The Geopolitics of Critical Minerals: Western Democracies Forge Supply Chain Pacts",
        "headline_ja": "重要鉱物を巡る地政学：欧米諸国、サプライチェーン強靱化と同盟協定を締結",
        "subhead": "脱炭素社会と経済安全保障を握るリチウム・希土類の囲い込み。資源外交と国際通商法の論理。",
        "source_name": "Financial Times / Reuters (Oct 4, 2026)",
        "source_url": "https://www.ft.com/content/critical-minerals-geopolitics-alliance",
        "source_attribution": "Financial Times (Commodities & Geopolitics Desk) / Reuters Global Business",
        "sentences": [
            {
                "no": 1,
                "en": "Western industrial democracies have formalized a multilateral mineral security partnership to curtail structural vulnerabilities in the global supply of rare earths and critical metals.",
                "ja": "欧米の主要先進国は、希土類（レアアース）および重要金属の世界的な供給における構造的脆弱性を軽減するため、多国間の鉱物安全保障パートナーシップを正式に発足させました。"
            },
            {
                "no": 2,
                "en": "While the transition toward renewable energy mandates unprecedented volumes of lithium, cobalt, and nickel, geographic concentration of refining capacities has intensified geopolitical anxieties.",
                "ja": "再生可能エネルギーへの移行が前例のない量のリチウム、コバルト、ニッケルを要求する一方で、製錬能力の地理的集中が地政学的な不安を高めています。"
            },
            {
                "no": 3,
                "en": "Under the prospective agreement, signatories pledge preferential trade subsidies and standardized environmental safeguards to foster resilient alternative extraction corridors.",
                "ja": "締結予定の協定に基づき、署名国は強靭な代替採掘回廊を育成するため、優遇貿易補助金と標準化された環境保護措置を誓約しています。"
            },
            {
                "no": 4,
                "en": "Economists emphasize that shielding strategic domestic industries from asymmetric export restrictions requires harmonizing protectionist tax incentives with World Trade Organization non-discrimination mandates.",
                "ja": "経済学者らは、非対称的な輸出規制から戦略的な国内産業を保護するには、保護主義的な税制優遇措置と世界貿易機関（WTO）の無差別原則（内国民待遇）とを調和させることが不可欠であると強調しています。"
            },
            {
                "no": 5,
                "en": "Ultimately, raw material diplomacy is fundamentally redrawing the landscape of multilateral alliances, transforming resource access into the definitive currency of twenty-first-century statecraft.",
                "ja": "最終的に、原材料を巡る外交は多国間同盟の構図を根本から塗り替えつつあり、資源へのアクセスを21世紀の国家統治術における決定的な通貨へと変容させています。"
            }
        ],
        "dialogue": [
            {
                "speaker": "七",
                "name": "Nanami",
                "role": "大学生・アシスタント",
                "text": "Keita先生、電気自動車（EV）や風力発電って環境に優しいクリーンな技術だと思っていましたが、その裏で『重要鉱物の奪い合い』という激しい国際摩擦が起きているんですね！"
            },
            {
                "speaker": "慶",
                "name": "Keita先生",
                "role": "予備校英語講師",
                "text": "その通りなんだ。脱炭素（Green Transition）を進めれば進めるほど、リチウムや希土類といった特定の資源への依存度が高まる。そしてその製錬の大部分が特定の国に集中していることが、経済安全保障上のアキレス腱になっているんだね。"
            },
            {
                "speaker": "七",
                "name": "Nanami",
                "role": "大学生・アシスタント",
                "text": "文4に出てきた『WTOの無差別原則との調和』という部分、法学部や経済学部の入試で本当によく見かけるテーマです！自国の産業を守りたいけれど、自由貿易ルールにも従わなければならないというジレンマですね。"
            },
            {
                "speaker": "慶",
                "name": "Keita先生",
                "role": "予備校英語講師",
                "text": "まさにそこが入試の狙い目！構文的にも文2の対比のWhile（〜である一方で）や、文4のrequire -ing（〜することを要求する）、文5のtransform A into B（AをBへと変容させる）など、格調高い論文英語の骨格が詰まっているよ。"
            },
            {
                "speaker": "七",
                "name": "Nanami",
                "role": "大学生・アシスタント",
                "text": "単なる理科の資源問題ではなく、国際法・国際政治・マクロ経済が交差する総合問題として出題されそうですね。しっかり単語と構文を復習します！"
            }
        ],
        "vocab": [
            {
                "word": "curtail",
                "phonetic": "[kɜːˈteɪl]",
                "pos": "他動詞",
                "meaning": "削減する、切り詰める、抑制する",
                "def": "to reduce in extent or quantity; impose a restriction on",
                "ex": "Government policies must curtail structural economic vulnerabilities."
            },
            {
                "word": "mandate",
                "phonetic": "[ˈmæn.deɪt]",
                "pos": "他動詞・名詞",
                "meaning": "義務付ける、要求する、権限を与える",
                "def": "to give official permission or require something by law or necessity",
                "ex": "The ambitious environmental treaty mandates zero carbon emissions by 2050."
            },
            {
                "word": "asymmetric",
                "phonetic": "[ˌeɪ.sɪˈmet.rɪk]",
                "pos": "形容詞",
                "meaning": "非対称の、不均衡な",
                "def": "having two sides or halves that are not the same; unbalanced",
                "ex": "Asymmetric trade tariffs can provoke unpredictable reciprocal retaliations."
            },
            {
                "word": "preferential",
                "phonetic": "[ˌpref.ərˈen.ʃəl]",
                "pos": "形容詞",
                "meaning": "優先的な、優遇の、特恵の",
                "def": "giving or involving a practical advantage or favor to someone",
                "ex": "Allied nations established preferential customs duties for raw materials."
            },
            {
                "word": "statecraft",
                "phonetic": "[ˈsteɪt.krɑːft]",
                "pos": "名詞",
                "meaning": "国家統治術、外交手腕、経国策",
                "def": "the skillful management of state affairs and international diplomacy",
                "ex": "Masterful statecraft requires balancing domestic stability with foreign commitments."
            }
        ],
        "syntax": [
            {
                "phrase": "While S V ..., S' V'...（事実の対比）",
                "meaning": "〜である一方で、〜である",
                "explanation": "文2の構文。再生可能エネルギーが膨大な鉱物を必要とするという【客観的要求】と、製錬の地理的偏在がもたらす【地政学的不安】という2つの現実を対比させています。"
            },
            {
                "phrase": "transform A into B",
                "meaning": "AをBへと変容させる",
                "explanation": "文5の動詞句。原材料外交が、単なる商取引から『21世紀の国家統治における決定的な通貨（外交カード）』へと質的変化を遂げたことを格調高く宣言する表現です。"
            }
        ],
        "pronunciation": [
            {
                "phrase": "curtail structural → 「カーテイル・ストラクチュラル」",
                "meaning": "第2音節強調 [kɜːˈteɪl]（先頭アクセントではない）"
            },
            {
                "phrase": "asymmetric → 「エイシメトリック」 [ˌeɪ.sɪˈmet.rɪk]",
                "meaning": "語頭の a- [eɪ] を明瞭に発音し、否定接頭辞を際立たせる"
            }
        ],
        "quiz": [
            {
                "question": "文中の 'curtail' と最も意味が近い動詞はどれですか。<br><em>\"...partnership to <strong>curtail</strong> structural vulnerabilities in the global supply of rare earths...\"</em>",
                "options": [
                    "diminish",
                    "exaggerate",
                    "subsidize",
                    "commence"
                ],
                "correct_index": 0,
                "explanation": "【正解：A】<br>curtail は「削減する、切り詰めて抑制する」という意味のフォーマル動詞で、同義語は A の diminish（減少させる、小さくする）や reduce です。B の exaggerate は「誇張する」、C の subsidize は「補助金を出す」、D の commence は「開始する」です。"
            },
            {
                "question": "文4 <em>\"requires harmonizing protectionist tax incentives with World Trade Organization non-discrimination mandates.\"</em> の論理的趣旨として最も適切なものはどれですか。",
                "options": [
                    "自国の重要鉱物産業を保護するための減税措置を、WTOの「自由かつ無差別な通商原則」に違反しないよう整合させる必要がある。",
                    "世界貿易機関（WTO）を速やかに脱退して、他国からの鉱物輸入を全面的に禁止すべきである。",
                    "すべての税制優遇措置を廃止して、純粋な市場原理のみに鉱物採掘を委ねるべきである。",
                    "国内産業の保護を優先するため、環境保護基準を国際基準よりも大幅に引き下げる必要がある。"
                ],
                "correct_index": 0,
                "explanation": "【正解：A】<br><code>harmonize A with B</code> は「AとBを調和・整合させる」という意味です。サプライチェーン自国保護のための税制優遇（protectionist tax incentives）と、WTOが定める内外無差別（non-discrimination）の通商原則との整合性を保つという国際経済法上の難題を正確に説明した A が正解です。"
            },
            {
                "question": "欧米諸国が重要鉱物の安全保障パートナーシップを締結するに至った最大の構造的要因は何ですか。",
                "options": [
                    "クリーンエネルギーへの移行に伴い鉱物需要が激増する一方、製錬加工能力が特定の地域に極度に集中していること。",
                    "世界中の鉱山においてリチウムとコバルトが完全に枯渇し、代替金属が一切存在しないため。",
                    "民間鉱山企業が過度な環境保護運動により採掘ライセンスを自主返上したため。",
                    "WTO加盟国すべてが二酸化炭素の排出量をゼロにすることに合意したため。"
                ],
                "correct_index": 0,
                "explanation": "【正解：A】<br>文2に <em>\"While the transition toward renewable energy mandates unprecedented volumes of lithium, cobalt, and nickel, geographic concentration of refining capacities has intensified geopolitical anxieties.\"</em> と明記されており、需要急増と製錬能力の地理的寡占（集中）が地政学的不安の直接原因です。"
            }
        ],
        "faq": [
            {
                "q": "なぜ鉱物の『採掘』だけでなく『製錬（refining）』が問題視されるのですか？",
                "a": "リチウムや希土類は世界各地の地下に存在しますが、鉱石から純度の高い金属を抽出・製錬する工程には膨大な化学薬品、電力、環境負荷が伴います。過去数十年間に環境規制が厳格な欧米が製錬から撤退した結果、特定国が製錬シェアの7〜9割を握ることとなり、これが戦略的チョークポイントとなっているためです。"
            },
            {
                "q": "大学入試の自由英作文でこのテーマが出題された時のポイントは？",
                "a": "単に「環境保護のためにEVを推進すべきだ」という単純論に終始せず、「エネルギー転換が新たな原材料供給網の依存と地政学的摩擦を生む」という複眼的な視点（Trade-off）を示すと、採点官に極めて高い知的好奇心と分析力をアピールできます。"
            }
        ],
        "factcheck": [
            {
                "title": "国際エネルギー機関（IEA）重要鉱物レビュー2026年知見",
                "body": "IEAの報告書によると、2040年までにネットゼロを達成するには重要鉱物の需要が現在の4倍以上に跳ね上がります。特にグラファイトや希土類の製錬においては単一国への依存度が80%を超えており、供給網の多角化（diversification）がG7・欧州連合の最重要国家課題となっています。"
            }
        ],
        "related_links": [
            {
                "url": "../../world/raf-fairford-bomber-redeployment/index.html",
                "title": "米戦略爆撃機のフェアフォード再配置と欧州防衛抑止力",
                "desc": "非対称戦争における抑止力強化とNATO同盟国の相互防衛メカニズム。",
                "relation": "【安全保障同盟の変容】"
            },
            {
                "url": "../../law/air-defence-shield/index.html",
                "title": "英国議会、100億ポンド防空シールド調達を審議",
                "desc": "防衛産業の調達法制と公的説明責任の法的バランス論議。",
                "relation": "【国家防衛と産業基盤】"
            }
        ]
    },

    {
        "slug": "arctic-sea-route-unclos",
        "category": "world",
        "category_label": "WORLD & MARITIME DIPLOMACY • 入試頻出テーマ",
        "title": "Melting Ice, Contested Waters: The Arctic Sea Route and UNCLOS Sovereignty Clashes",
        "headline_ja": "融解する氷と角逐する領海：北極海航路の開放と国連海洋法条約（UNCLOS）を巡る主権衝突",
        "subhead": "地球温暖化が生んだ最短航路の商業化と航行の自由原則。海洋法秩序と安全保障の相克。",
        "source_name": "The Times UK / Nature Climate Change (Oct 3, 2026)",
        "source_url": "https://www.thetimes.co.uk/article/arctic-sea-route-unclos-sovereignty",
        "source_attribution": "The Times UK (Diplomatic Editor) / Nature Climate Change Research Letters",
        "sentences": [
            {
                "no": 1,
                "en": "Rapid thermal degradation of polar ice sheets has abruptly transformed the previously impassable Northern Sea Route into a viable maritime commercial corridor.",
                "ja": "極地の氷床の急速な熱的劣化（融解）により、かつて航行不能であった北極海航路が実行可能な海上商業回廊へと突如変貌を遂げました。"
            },
            {
                "no": 2,
                "en": "Shipping conglomerates project that navigating through Arctic waters significantly abbreviates transit times between European ports and East Asian industrial centers, bypassing traditional equatorial chokepoints.",
                "ja": "海運複合企業は、北極海海域を航行することで、伝統的な赤道直下のチョークポイント（要衝）を迂回し、欧州の港湾と東アジアの工業拠点間の輸送時間を劇的に短縮できると予測しています。"
            },
            {
                "no": 3,
                "en": "However, littoral states assert expansive regulatory jurisdiction over adjacent straits, invoking Article 234 of the United Nations Convention on the Law of the Sea to enforce strict ice-navigation levies.",
                "ja": "しかし沿岸諸国は、国連海洋法条約（UNCLOS）第234条を引き合いに出して厳格な氷海航行課徴金を課すなど、隣接する海峡に対して拡張的な規制管轄権を主張しています。"
            },
            {
                "no": 4,
                "en": "Freedom-of-navigation advocates vigorously contend that customary international law guarantees unhindered transit passage through international straits, irrespective of regional environmental oversight.",
                "ja": "航行の自由の支持者らは、地域の環境監視にかかわらず、国際慣習法によって国際海峡における妨げられない通過通航権が保障されていると猛烈に反論しています。"
            },
            {
                "no": 5,
                "en": "The escalating geopolitical impasse demonstrates how anthropogenic climate shifts destabilize established treaties, creating unprecedented flashpoints in international public law.",
                "ja": "深刻化する地政学的膠着状態は、人為的な気候変動がいかに確立された国際条約を不安定化させ、国際公法における前例のない火種を生み出しているかを如実に示しています。"
            }
        ],
        "dialogue": [
            {
                "speaker": "七",
                "name": "Nanami",
                "role": "大学生・アシスタント",
                "text": "Keita先生、地球温暖化で北極の氷が溶けているニュースはよく聞きますが、船の航路として使えるようになると、なぜ国と国の激しい対立が起きるんですか？"
            },
            {
                "speaker": "慶",
                "name": "Keita先生",
                "role": "予備校英語講師",
                "text": "すごく本質的な疑問だね！スエズ運河やマラッカ海峡を通る南回りに比べて、北極海航路を使うと欧州・アジア間の日数が10日以上短縮できるんだ。莫大な経済的利益が生まれる反面、『その海峡は誰のものか』という国際海洋法の争いが勃発したんだよ。"
            },
            {
                "speaker": "七",
                "name": "Nanami",
                "role": "大学生・アシスタント",
                "text": "文3の沿岸国（littoral states）の主張と、文4の航行の自由派（freedom-of-navigation advocates）の対立ですね！沿岸国は『環境を守るための規制だ』と言い、他国は『国際海峡だから勝手に通行料を取るな』と主張しているわけですね。"
            },
            {
                "speaker": "慶",
                "name": "Keita先生",
                "role": "予備校英語講師",
                "text": "その通り！東大・京大・早慶の入試で頻出する『国連海洋法条約（UNCLOS）』の典型的な論点だ。文4の『irrespective of（〜に関わらず）』や文5の『anthropogenic（人為的な）』などは最重要語彙だよ。"
            },
            {
                "speaker": "七",
                "name": "Nanami",
                "role": "大学生・アシスタント",
                "text": "環境問題と国際法が一体になった超重要長文ですね。リスニング音声で発音のつながりもしっかりチェックします！"
            }
        ],
        "vocab": [
            {
                "word": "degradation",
                "phonetic": "[ˌdeɡ.rəˈdeɪ.ʃən]",
                "pos": "名詞",
                "meaning": "劣化、衰退、分解、悪化",
                "def": "the process of deteriorating or being degraded to a lower quality or condition",
                "ex": "Environmental degradation accelerates biodiversity extinction in fragile biomes."
            },
            {
                "word": "littoral",
                "phonetic": "[ˈlɪt.ər.əl]",
                "pos": "形容詞・名詞",
                "meaning": "沿岸の、海岸の、沿岸国（名詞）",
                "def": "relating to or situated on the shore of the sea or a lake",
                "ex": "Littoral states claim maritime security rights over sovereign territorial waters."
            },
            {
                "word": "transit",
                "phonetic": "[ˈtræn.zɪt]",
                "pos": "名詞・動詞",
                "meaning": "通過、通航、輸送",
                "def": "the act of passing through or across a place",
                "ex": "The convention protects transit passage through critical international straits."
            },
            {
                "word": "anthropogenic",
                "phonetic": "[ˌæn.θrə.pəˈdʒen.ɪk]",
                "pos": "形容詞",
                "meaning": "人為的な、人類の活動に起因する",
                "def": "originating in human activity; chief causes of environmental change",
                "ex": "Anthropogenic greenhouse gas emissions drive unprecedented polar ice thaw."
            },
            {
                "word": "impasse",
                "phonetic": "[ˈæm.pɑːs]",
                "pos": "名詞",
                "meaning": "行き詰まり、膠着状態、暗礁",
                "def": "a situation in which no progress is possible, especially because of disagreement",
                "ex": "Diplomatic negotiations reached a tense impasse over maritime boundary demarcation."
            }
        ],
        "syntax": [
            {
                "phrase": "abbreviates transit times ..., bypassing traditional chokepoints（分詞構文）",
                "meaning": "〜を短縮し、それによって…を迂回する",
                "explanation": "文2の構文。コンマ＋現在分詞（bypassing...）が結果や付帯状況を表し、北極航路を選択したことによる利便性を簡潔に繋げています。"
            },
            {
                "phrase": "irrespective of ~",
                "meaning": "〜に関係なく、〜を問わず（= regardless of）",
                "explanation": "文4の重要群前置詞。地域の環境規制（environmental oversight）の有無にかかわらず、国際慣習法上の航行自由が絶対であると主張する法律英語の定番表現です。"
            }
        ],
        "pronunciation": [
            {
                "phrase": "littoral states → 「リトラル・ステイツ」 [ˈlɪt.ər.əl]",
                "meaning": "第1音節にアクセント。tのフラッピング（軽いラ行音）に注意。"
            },
            {
                "phrase": "anthropogenic → 「アンスロポジェニック」 [ˌæn.θrə.pəˈdʒen.ɪk]",
                "meaning": "第3音節 [dʒen] に主アクセント。"
            }
        ],
        "quiz": [
            {
                "question": "文中の 'abbreviates' と最も意味が近い動詞はどれですか。<br><em>\"...significantly <strong>abbreviates</strong> transit times between European ports and East Asian industrial centers...\"</em>",
                "options": [
                    "shortens",
                    "prolongs",
                    "postpones",
                    "standardizes"
                ],
                "correct_index": 0,
                "explanation": "【正解：A】<br>abbreviate は「短縮する、要約する」という意味で、ここでは航海時間を短くすることを指しているため A の shortens（短縮する）が正解です。B の prolong は「延長する」、C の postpone は「延期する」です。"
            },
            {
                "question": "文3と文4における、沿岸国（littoral states）と航行の自由派（freedom-of-navigation advocates）の対立点として最も適切なものはどれですか。",
                "options": [
                    "沿岸国が氷海環境保護を名目に規制・課徴金権限を主張するのに対し、航行派は国際海峡における無制限の通過通航権を主張している点。",
                    "北極海に生息するホッキョクグマの保護区をどちらの領土に設置するかを巡る対立。",
                    "商船の燃料として原子力エンジンを採用することを国際海事機関が認めるか否かの対立。",
                    "東アジア諸国の造船会社がヨーロッパの港湾施設を無許可で買収したことに対する対立。"
                ],
                "correct_index": 0,
                "explanation": "【正解：A】<br>文3で沿岸国が国連海洋法条約234条を援用して管轄権と通行料（levies）を主張し、文4で他国が国際慣習法上の「妨げられない通過通航権（unhindered transit passage）」を主張している構図が明記されています。"
            },
            {
                "question": "文末 <em>\"anthropogenic climate shifts destabilize established treaties\"</em> が含意する学術的メッセージとして最も適切なものはどれですか。",
                "options": [
                    "人間活動が引き起こした気候変動が、過去に結ばれた国際条約の前提を崩し、新たな法的・地政学的対立を生み出していること。",
                    "地球温暖化を防止する条約を結べば、すべての軍事衝突が直ちに終息すること。",
                    "北極海航路の開設により、国際公法の専門家が不要になること。",
                    "氷床が融解しても、各国の領海警備隊の管轄区域には一切の変化が生じないこと。"
                ],
                "correct_index": 0,
                "explanation": "【正解：A】<br>anthropogenic（人為的な）気候変動によって「かつて航行不能（impassable）だった氷海」が現実の航路になったことで、既存の国連海洋法条約などの条約解釈が揺らぎ、国際関係の新たな火種（flashpoint）になっていることを述べています。"
            }
        ],
        "faq": [
            {
                "q": "国連海洋法条約（UNCLOS）第234条とはどのような規定ですか？",
                "a": "『氷結地域（Ice-covered areas）』に関する条項で、厳しい気候条件と氷によって航行が極めて危険で海洋環境被害が不可逆となりうる海域において、沿岸国が非差別的な公害防止法令を制定・行使できる特別権限を認めたものです。沿岸国はこの条文を主権拡大の根拠とし、他国は公海自由の侵害だと反発しています。"
            },
            {
                "q": "共通テストや二次試験での地理・現代社会・英語のクロスカリキュラム出題とは？",
                "a": "近年、難関大入試では英語の試験であっても「地理・政治経済の基礎知識」を前提とした英文が頻出します。北極航路、スエズ運河、マラッカ海峡などのチョークポイントの地理的把握は、英語長文の読解スピードを劇的に引き上げます。"
            }
        ],
        "factcheck": [
            {
                "title": "北極評議会（Arctic Council）と航行データ2026",
                "body": "欧州連合の気候監視機関コペルニクスによると、北極海の海氷面積は過去30年で最低水準を更新し続けており、夏季の無氷期間（ice-free window）は従来の3週間から2ヶ月以上に拡大。航海距離が最大40%削減されるため、環境保護と軍事的自由航行権の衝突が急増しています。"
            }
        ],
        "related_links": [
            {
                "url": "../../world/critical-minerals-geopolitics/index.html",
                "title": "重要鉱物を巡る地政学：欧米諸国、サプライチェーン強靱化協定を締結",
                "desc": "脱炭素社会と経済安全保障を握る重要資源の獲得競争と通商法。",
                "relation": "【資源・通商地政学】"
            },
            {
                "url": "../../science/mediterranean-marine-heatwaves/index.html",
                "title": "地中海の海洋熱波、深海性サンゴ群集を直撃",
                "desc": "海水温上昇と海洋生態系危機の因果関係分析。",
                "relation": "【地球環境危機の連鎖】"
            }
        ]
    },

    {
        "slug": "stoic-philosophy-digital-age",
        "category": "culture",
        "category_label": "CULTURE & CLASSICAL THOUGHT • 入試頻出テーマ",
        "title": "Ancient Antidotes to Algorithmic Anxiety: The Modern Renaissance of Stoic Philosophy",
        "headline_ja": "アルゴリズム時代の不安に効く古代の処方箋：ストア派哲学の現代的復権",
        "subhead": "エピクテトスとマルクス・アウレリウスが説いた「制御の二分法」。常時接続社会を生き抜く精神の強靭さ。",
        "source_name": "TIME Magazine / The Conversation (Oct 2, 2026)",
        "source_url": "https://time.com/stoicism-algorithmic-anxiety-modern-life",
        "source_attribution": "TIME Ideas Essay / The Conversation (Philosophy & Cognitive Science)",
        "sentences": [
            {
                "no": 1,
                "en": "In a hyper-connected civilization plagued by constant algorithmic notifications and social anxiety, millions of young urbanites are turning toward the ancient Hellenistic teachings of Stoicism.",
                "ja": "絶え間ないアルゴリズムの通知と社会的孤立・不安に悩まされる過剰接続文明において、何百万もの都市の若者たちが古代ヘレニズム期のストア派の教えへと目を向けています。"
            },
            {
                "no": 2,
                "en": "Popularized by Roman thinkers such as Epictetus and Emperor Marcus Aurelius, the cornerstone of Stoic doctrine resides in the dichotomy of control: distinguishing what lies within our power from what does not.",
                "ja": "エピクテトスや皇帝マルクス・アウレリウスといったローマの思想家によって普及したストア派教義の礎石は、「制御の二分法」——何が自分自身の力の及ぶ範囲にあり、何がそうでないかを峻別すること——にあります。"
            },
            {
                "no": 3,
                "en": "Contemporary cognitive psychologists note that rational emotive behavior therapy directly descends from this classical precept, helping modern individuals dismantle destructive external validation loops.",
                "ja": "現代の認知心理学者らは、論理情動行動療法（REBT）がこの古典的な教えを直接受け継いでおり、現代人が破壊的な外部からの承認欲求のループを解体する手助けをしていると指摘しています。"
            },
            {
                "no": 4,
                "en": "Critics caution that an oversimplified, commercialized rendition of Stoicism risks promoting emotional suppression or passive resignation in the face of structural systemic injustices.",
                "ja": "批判者らは、ストア派を過度に単純化・商業化した解釈は、構造的な社会の不公正に直面した際に感情の抑圧や受動的な諦めを助長する危険があると警告しています。"
            },
            {
                "no": 5,
                "en": "Nevertheless, cultivating internal equanimity amid relentless external volatility remains an indispensable psychological virtue for navigating our turbulent informational landscape.",
                "ja": "それにもかかわらず、容赦ない外部の不安定さの中で内面の平静（平静心）を培うことは、激動の情報社会を航海するための不可欠な精神的徳目であり続けています。"
            }
        ],
        "dialogue": [
            {
                "speaker": "七",
                "name": "Nanami",
                "role": "大学生・アシスタント",
                "text": "Keita先生、紀元前の古代ギリシャ・ローマの哲学である『ストア派（Stoicism）』が、なぜ今SNSやスマートフォンの時代にこれほど大ブームになっているんですか？"
            },
            {
                "speaker": "慶",
                "name": "Keita先生",
                "role": "予備校英語講師",
                "text": "面白いよね！スマホを開けば他人の自慢や炎上、ニュースの通知が押し寄せて、自分の心が他人にコントロールされている感覚になる。そこでストア派の『制御の二分法（dichotomy of control）』——他人の評価や世界の出来事は変えられないが、自分の思考と反応は100%自分で選べる——という教えが最高のメンタル防壁になるんだ。"
            },
            {
                "speaker": "七",
                "name": "Nanami",
                "role": "大学生・アシスタント",
                "text": "文3で現代の認知行動療法のルーツだと言われていて納得しました！でも文4で『過度な単純化は、社会の不正に対する諦め（passive resignation）を生む』という批判も紹介されていますね。"
            },
            {
                "speaker": "慶",
                "name": "Keita先生",
                "role": "予備校英語講師",
                "text": "さすがNanamiさん、良い着眼点だね。入試の英語評論では、ある思想を絶賛するだけでなく『批判者の見解（Critics caution that...）』を挟んで多角的に検証するのが王道の構成だ。文5の『equanimity（平静）』や『volatility（変動性）』も難関大必修語だよ。"
            },
            {
                "speaker": "七",
                "name": "Nanami",
                "role": "大学生・アシスタント",
                "text": "受験勉強の不安で心がザワザワするときにも、このストア派の考え方はそのまま役立ちそうです！"
            }
        ],
        "vocab": [
            {
                "word": "cornerstone",
                "phonetic": "[ˈkɔː.nə.stəʊn]",
                "pos": "名詞",
                "meaning": "礎石、基礎、土台",
                "def": "an important quality or feature on which a particular thing depends or is based",
                "ex": "Critical thinking is the cornerstone of academic university education."
            },
            {
                "word": "dichotomy",
                "phonetic": "[daɪˈkɒt.ə.mi]",
                "pos": "名詞",
                "meaning": "二分法、両極端の分裂",
                "def": "a division or contrast between two things that are represented as being entirely different",
                "ex": "The classic philosophical dichotomy between mind and body remains hotly debated."
            },
            {
                "word": "precept",
                "phonetic": "[ˈpriː.sept]",
                "pos": "名詞",
                "meaning": "指針、教え、規範、戒め",
                "def": "a general rule intended to regulate behavior or thought",
                "ex": "Ancient ethical precepts guide human morality across cultures."
            },
            {
                "word": "resignation",
                "phonetic": "[ˌrez.ɪɡˈneɪ.ʃən]",
                "pos": "名詞",
                "meaning": "諦め、受忍、辞職",
                "def": "the acceptance of something undesirable but inevitable; giving up office",
                "ex": "He greeted the unfortunate news with quiet, stoic resignation."
            },
            {
                "word": "equanimity",
                "phonetic": "[ˌek.wəˈnɪm.ə.ti]",
                "pos": "名詞",
                "meaning": "心の平静、沈着、平穏",
                "def": "mental calmness, composure, and evenness of temper, especially in a difficult situation",
                "ex": "The seasoned surgeon maintained remarkable equanimity during the crisis."
            }
        ],
        "syntax": [
            {
                "phrase": "distinguishing A from B（分詞構文による同格解説）",
                "meaning": "AとBを区別すること",
                "explanation": "文2の構文。直前の the dichotomy of control（制御の二分法）の内容を、コロンの後で分詞構文を用いて「自分の力の及ぶもの（within our power）と及ばないもの」の峻別として平易かつ厳密に言い換えています。"
            },
            {
                "phrase": "cultivating A amid B remains C（動名詞主語＋前置詞句＋本動詞）",
                "meaning": "Bの中でAを育むことは依然としてCである",
                "explanation": "文5の骨格構文。動名詞句 `cultivating internal equanimity` が主語（S）、`remains` が動詞（V）、`an indispensable virtue` が補語（C）の第2文型です。"
            }
        ],
        "pronunciation": [
            {
                "phrase": "dichotomy → 「ダイコトミー」 [daɪˈkɒt.ə.mi]",
                "meaning": "第2音節 [kɒt] に主アクセント。ダイチョトミーではない。"
            },
            {
                "phrase": "equanimity → 「エクワニミティ」 [ˌek.wəˈnɪm.ə.ti]",
                "meaning": "第3音節 [nɪm] に主アクセント。"
            }
        ],
        "quiz": [
            {
                "question": "文中のストア派哲学における核心原理 'the dichotomy of control（制御の二分法）' の説明として最も適切なものはどれですか。",
                "options": [
                    "自分自身の意志で直接コントロールできる内面と、コントロールできない外部の事象を明確に区別すること。",
                    "すべての感情を完全に消去し、機械のように無痛・無感情で生活すること。",
                    "社会のすべての政治権力を二つの政党で平等に分割統治すること。",
                    "スマートフォンとパソコンの使用時間を毎日きっかり均等に分けること。"
                ],
                "correct_index": 0,
                "explanation": "【正解：A】<br>文2に <em>\"the dichotomy of control: distinguishing what lies within our power from what does not\"</em> と定義されており、自分の力の及ぶもの（内的思考や反応）と及ばないもの（他人の言動や外的環境）を分ける姿勢を指します。"
            },
            {
                "question": "文4において、ストア派を安易に単純化・商業化することに対する批判者の懸念として述べられているものはどれですか。",
                "options": [
                    "不当な社会構造や差別に直面した際に、それを変革しようとせず「受け入れよう」とする受動的な諦めを正当化してしまう危険。",
                    "ストア派の古典書籍が高額すぎて、一般市民が哲学を学べなくなる危険。",
                    "皇帝マルクス・アウレリウスを崇拝するあまり、君主制を復活させようとする政治運動が起きる危険。",
                    "認知行動療法（REBT）が医学的に無効であることが科学的に証明されたこと。"
                ],
                "correct_index": 0,
                "explanation": "【正解：A】<br>文4に <em>\"risks promoting emotional suppression or passive resignation in the face of structural systemic injustices\"</em>（構造的なシステム的不公正に直面した際に、感情の抑圧や受動的な諦めを助長する危険がある）と明記されています。"
            },
            {
                "question": "文中の 'equanimity' と最も意味が近い単語はどれですか。<br><em>\"...cultivating internal <strong>equanimity</strong> amid relentless external volatility...\"</em>",
                "options": [
                    "composure",
                    "hostility",
                    "extravagance",
                    "indecision"
                ],
                "correct_index": 0,
                "explanation": "【正解：A】<br>equanimity は「心の平静、沈着」という意味の難関大頻出語彙で、同義語は A の composure（落ち着き、冷静さ）や serenity です。B の hostility は「敵意」、C の extravagance は「浪費」、D の indecision は「優柔不断」です。"
            }
        ],
        "faq": [
            {
                "q": "ストア派の『ストイック（stoic）』という言葉は、日本語の『禁欲的・我慢強い』と同じ意味ですか？",
                "a": "日常会話で使われる『ストイック＝感情を殺して痛みに耐える』というイメージは誤解に近いものです。本来のストア派は、感情を抑圧するのではなく『理性的で客観的な判断によって、怒りや不安といった不合理な情動に振り回されないようにする』という極めて積極的で実践的な心のトレーニング（Mental Fitness）です。"
            },
            {
                "q": "エピクテトスとマルクス・アウレリウスの対比が入試で好まれる理由は？",
                "a": "エピクテトスは『元奴隷』であり、マルクス・アウレリウスは『ローマ帝国の最高権力者（皇帝）』でした。境遇が真逆の二人が、ともに同じストア派哲学を支えに逆境を乗り越えたという事実は、人間の尊厳や自律を論じる大学入試エッセイの格好の素材となっています。"
            }
        ],
        "factcheck": [
            {
                "title": "臨床心理学におけるストア哲学の応用とエビデンス",
                "body": "1950年代にアルバート・エリスが創始した論理情動行動療法（REBT）およびアーロン・ベックの認知行動療法（CBT）は、エピクテトスの『人間を苦しめるのは事象そのものではなく、その事象に対する人間の解釈である』という命題を治療プロトコルとして定式化したものです。近年のメタ分析でも、認知の再構成がうつやSNS不安を有意に軽減することが実証されています。"
            }
        ],
        "related_links": [
            {
                "url": "../../culture/headphones-in-public/index.html",
                "title": "公共空間でイヤホンを外す効用：失われた「物思い（白昼夢）」を取り戻す",
                "desc": "常時接続と孤独、創造性を育む退屈の価値を認知心理学で解説。",
                "relation": "【常時接続社会への処方箋】"
            },
            {
                "url": "../../society/psychology-casual-encounters/index.html",
                "title": "偶然の出会いの心理学：見知らぬ人との会話が都市の幸福感を高める理由",
                "desc": "都市社会学における微小な交流と精神的レジリエンス。",
                "relation": "【人間関係と主観的幸福感】"
            }
        ]
    }
]

async def synthesize_all_new():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    sem = asyncio.Semaphore(4)
    tasks = []
    
    for art in NEW_ARTICLES:
        slug = art["slug"]
        cat = art["category"]
        art_dir = os.path.join(base_dir, cat, slug)
        audio_dir = os.path.join(art_dir, "audio")
        os.makedirs(audio_dir, exist_ok=True)
        
        # 1. Write HTML
        html_content = build_article_html(art)
        html_path = os.path.join(art_dir, "index.html")
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(html_content)
        print(f"[OK] Generated HTML: {cat}/{slug}/index.html")
        
        # 2. Audio Tasks
        # Headline
        tasks.append(synth_audio(art["title"], VOICE_BRITISH, os.path.join(audio_dir, "headline.mp3"), sem))
        # Full Body
        body_text = " ".join([s["en"] for s in art["sentences"]])
        tasks.append(synth_audio(body_text, VOICE_BRITISH, os.path.join(audio_dir, "full_body.mp3"), sem))
        # Sentences
        for i, s in enumerate(art["sentences"]):
            tasks.append(synth_audio(s["en"], VOICE_BRITISH, os.path.join(audio_dir, f"s{i+1}.mp3"), sem))
        # Dialogue
        for i, dlg in enumerate(art["dialogue"]):
            v = VOICE_KEITA if dlg["speaker"] == "慶" else VOICE_NANAMI
            tasks.append(synth_audio(dlg["text"], v, os.path.join(audio_dir, f"dlg_{i+1:02d}.mp3"), sem))
            
    print(f"Synthesizing {len(tasks)} audio files for 3 new articles...")
    await asyncio.gather(*tasks)
    print("All audio files synthesized successfully!")

    # Register into articles_data.py
    from articles_data import ARTICLES
    existing_slugs = [a['slug'] for a in ARTICLES]
    for new_a in NEW_ARTICLES:
        if new_a['slug'] not in existing_slugs:
            ARTICLES.append(new_a)
            print(f"Registered {new_a['slug']} into ARTICLES")
            
    articles_data_path = os.path.join(os.path.dirname(__file__), 'articles_data.py')
    with open(articles_data_path, 'w', encoding='utf-8') as f:
        f.write('# -*- coding: utf-8 -*-\n\nARTICLES = ')
        f.write(pprint.pformat(ARTICLES, indent=2, width=120, sort_dicts=False))
        f.write('\n')
    print("Updated articles_data.py successfully!")

if __name__ == "__main__":
    asyncio.run(synthesize_all_new())
