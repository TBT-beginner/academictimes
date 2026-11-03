# -*- coding: utf-8 -*-
"""Generate Batch 30 (2026-11-03): 12 Senior + 12 Junior articles."""

import json

# Senior Articles
# 1. starwatch-catch-the-striking-trifecta-of-venus-the-moon-and-spica-at-break-of-dawn (science)
# 2. tender-bond-male-donkey-bull-baffles-scientists (science)
# 3. polar-vortex-disruption-colder-weather-europe (environment)
# 4. british-gas-resume-force-fitting-prepayment-meters-months-after-112m-settlement (environment)
# 5. nhs-early-warning-system-child-illness-england (society)
# 6. counsellors-psychotherapists-statutory-regulation-uk-professional-bodies (society)
# 7. nine-of-world-biggest-oil-firms-95bn-profit-third-quarter-iran-war (world)
# 8. hackers-fake-nuclear-chemical-threat-alert-kyiv-ukraine-emergency-app (world)
# 9. australia-social-media-ban-high-court-challenge-reddit-digital-freedom-project (law)
# 10. uk-making-up-china-policy-as-it-goes-along-mps (law)
# 11. bbc-young-musician-teenage-violinist-sofia-demetriades (culture)
# 12. john-lewis-christmas-advert-kristin-scott-thomas-glamorous-granny-gift-hunt (entertainment)

s1 = {
    "slug": "starwatch-catch-the-striking-trifecta-of-venus-the-moon-and-spica-at-break-of-dawn",
    "category": "science",
    "date": "2026-11-03",
    "pub_date": "2026-11-03",
    "source_url": "https://www.theguardian.com/science/2026/nov/02/starwatch-catch-the-striking-trifecta-of-venus-the-moon-and-spica-at-break-of-dawn",
    "source_name": "The Guardian",
    "source_media": "The Guardian",
    "source_domain": "theguardian.com",
    "source_attribution": "The Guardian (November 2, 2026)",
    "category_label": "SCIENCE • ASTRONOMY",
    "title": "Astronomers Highlight Spectacular Conjunction of Venus, Crescent Moon and Spica",
    "headline_ja": "天文学者が注目：夜明けの空を彩る金星・細い月・スピカの華麗な三連惑星直列",
    "lead_ja": "11月上旬の夜明け前の東の空において、眩しく輝く金星、細い三日月、そしておとめ座の1等星スピカが極めて狭い角度に並ぶ見事な合（コンジャンクション）が観測され、天文学愛好家や天体物理学者たちを魅了しています。",
    "subhead": "A rare dawn celestial alignment offers amateur stargazers and planetary scientists valuable orbital observation opportunities.",
    "lead_snippet": "Before daybreak this week, skywatchers across the northern hemisphere can witness an elegant celestial triad in the eastern sky.",
    "summary_points": [
        "明け方の東の空で、金星、三日月、恒星スピカが狭い視野内に大集結する稀有な天体ランデブー。",
        "月が太陽光を反射する地球照（アースシャイン）と、金星の圧倒的な光度が織りなす天体力学的現象。",
        "視差や軌道面の違いを理解する格好の天文教材として、高校地学や探究活動でも注目。"
    ],
    "image": "https://images.unsplash.com/photo-1506703719100-a0f3a48c0f86?w=1000&auto=format&fit=crop&q=80",
    "sentences": [
        {"en": "Before sunrise this week, stargazers across the temperate northern hemisphere are treated to a remarkable celestial trio in the east.", "ja": "今週の日の出前、温暖な北半球全域の星空観察者たちは、東の空に現れる見事な天体の三重奏を楽しんでいます。"},
        {"en": "Brilliant Venus, the crescent Moon showing faint earthshine, and the blue-white giant star Spica form a compact triangle in Virgo.", "ja": "輝かしい金星、かすかな地球照を見せる三日月、そして青白く輝く巨星スピカが、おとめ座の中で密集した三角形を形成しています。"},
        {"en": "Although these celestial bodies appear closely adjacent along our line of sight, they actually lie at vastly differing cosmic distances.", "ja": "これらの天体は我々の視線方向において近接して並んでいるように見えますが、実際には宇宙空間において大きく異なる距離に位置しています。"},
        {"en": "Planetary scientists emphasize that tracking such orbital conjunctions historically enabled Renaissance astronomers to measure astronomical parallax.", "ja": "惑星科学者らは、このような軌道上の合を追跡することが、歴史的にルネサンス期の天文学者が天体視差を測定することを可能にしたと強調しています。"},
        {"en": "Clear autumn dawns offer students an ideal practical exercise in observational astronomy and celestial coordinate mechanics.", "ja": "澄み切った秋の夜明けは、観測天文学や天球座標力学における理想的な実践学習の機会を学生たちに提供しています。"}
    ],
    "dialogue": [
        {"speaker": "Keita先生", "name": "Keita先生", "role": "英語講師", "text": "夜明け前の空で、金星と三日月、そしてスピカが一直線に並ぶ美しい天体ショーが見られるよ。"},
        {"speaker": "Nanami", "name": "Nanami", "role": "生徒・アシスタント", "text": "金星と遠くの恒星が隣り合って見えるのって、宇宙の奥行きを感じてロマンチックですね！"},
        {"speaker": "Keita先生", "name": "Keita先生", "role": "英語講師", "text": "見かけ上はすぐ隣に見えても、月までは約38万キロ、スピカは約250光年も離れているんだ。この視差の理解が天文学の原点だね。"},
        {"speaker": "Nanami", "name": "Nanami", "role": "生徒・アシスタント", "text": "早起きして空を見上げるだけで、教科書に載っている天体の運行が実感できますね！"}
    ],
    "quiz": [
        {
            "question": "Which celestial bodies comprise the striking dawn alignment described in the text?",
            "options": ["Venus, the crescent Moon, and the bright star Spica.", "Jupiter, Mars, and Saturn in the western sky.", "Mercury, the full Moon, and the star Polaris.", "Comet Halley, Venus, and Sirius at midnight."],
            "answer": 0,
            "explanation": "文2に「Venus, the crescent Moon showing faint earthshine, and the blue-white giant star Spica」と明記されており、金星・三日月・スピカの組み合わせが正解です。"
        },
        {
            "question": "What does the text clarify regarding the proximity of these celestial bodies?",
            "options": ["They appear close visually but lie at vastly differing distances from Earth.", "They have collided with each other within the constellation of Virgo.", "They are located at the exact same physical distance from our solar system.", "They orbit Earth inside the lower atmospheric layer."],
            "answer": 0,
            "explanation": "文3に「Although these celestial bodies appear closely adjacent along our line of sight, they actually lie at vastly differing cosmic distances」とある通り、見かけ上隣り合っているだけで実際の距離は大きく異なります。"
        },
        {
            "question": "Why did historical conjunction observations matter to Renaissance astronomers?",
            "options": ["They enabled the mathematical calculation and measurement of astronomical parallax.", "They allowed ancient sailors to build artificial magnetic compasses.", "They proved that all stars in the galaxy produce nuclear fission power.", "They caused the Earth to accelerate its annual rotational speed."],
            "answer": 0,
            "explanation": "文4に「tracking such orbital conjunctions historically enabled Renaissance astronomers to measure astronomical parallax（天体視差の測定を可能にした）」と記述されています。"
        }
    ],
    "vocab": [
        {"word": "conjunction", "meaning": "（天文学の）合、惑星の接近合致", "example": "A planetary conjunction occurs when two bodies share celestial longitude."},
        {"word": "earthshine", "meaning": "地球照（地球が反射した太陽光で月の影の部分がうっすら光る現象）", "example": "Earthshine illuminated the unlit crescent of the Moon."},
        {"word": "adjacent", "meaning": "隣接した、近接した", "example": "The two buildings are situated adjacent to the university library."},
        {"word": "parallax", "meaning": "視差（観測位置の違いによって天体の見える方向が変わる角度）", "example": "Stellar parallax helps astronomers calculate distances to nearby stars."}
    ]
}

# 2. tender-bond-male-donkey-bull-baffles-scientists (science)
s2 = {
    "slug": "tender-bond-male-donkey-bull-baffles-scientists",
    "category": "science",
    "date": "2026-11-03",
    "pub_date": "2026-11-03",
    "source_url": "https://www.theguardian.com/science/2026/nov/02/tender-bond-male-donkey-bull-baffles-scientists",
    "source_name": "The Guardian",
    "source_media": "The Guardian",
    "source_domain": "theguardian.com",
    "source_attribution": "The Guardian (November 2, 2026)",
    "category_label": "SCIENCE • ANIMAL BEHAVIOUR",
    "title": "Remarkable Interspecies Companionship Between Donkey and Bull Intrigues Biologists",
    "headline_ja": "ロバと雄牛の異種間における深い絆：動物行動学者たちを驚かせる共生愛着行動",
    "lead_ja": "英国の保護施設において、気性の荒い雄牛と年老いたオスのロバとの間に育まれた極めて親密な絆が報告され、異なる種の間で社会的絆や感情的安心感がどのように形成されるのかを巡り、動物行動学者が研究を進めています。",
    "subhead": "Ethologists investigate cross-species emotional attachments that challenge conventional evolutionary models of territorial herd instincts.",
    "lead_snippet": "An inseparable friendship between a rescue bull and an elderly donkey provides rare behavioral insights into mammalian empathy.",
    "summary_points": [
        "気性の荒い去勢雄牛が年老いたロバと常に寄り添い、互いを毛づくろいして守り合う異種間の深い愛情。",
        "従来の縄張り意識や同種間群れの利己的遺伝子仮説を超える、哺乳類の感情的愛着・共感機能の存在。",
        "動物福祉や家畜のメンタルケア、社会的知能の進化に関する新たな学術的示唆。"
    ],
    "image": "https://images.unsplash.com/photo-1548767797-d8c844163c4c?w=1000&auto=format&fit=crop&q=80",
    "sentences": [
        {"en": "At an animal sanctuary in northern England, an extraordinarily tender bond between a tempestuous bull and an elderly donkey has captivated ethologists.", "ja": "イングランド北部の動物保護施設で、気性の荒い雄牛と年老いたロバとの間に見られる極めて優しい絆が、動物行動学者たちを魅了しています。"},
        {"en": "Despite differing vocal signals and herd instincts, the pair graze in unison, groom each other, and exhibit acute distress whenever separated.", "ja": "発声シグナルや群れの生得的本能が異なるにもかかわらず、このペアは息を合わせて草を食み、互いを毛づくろいし、引き離されると激しい苦痛を示します。"},
        {"en": "Biologists note that interspecies companionships challenge rigid sociobiological assumptions that social cohesion exists solely to propagate shared genes.", "ja": "生物学者らは、異種間の仲間関係が、社会的結束は共有遺伝子を増殖させるためだけに存在する、という厳格な社会生物学的前提に異議を唱えるものだと指摘しています。"},
        {"en": "Neuroscientists suggest that oxytocin-driven emotional circuitry in domestic mammals can transcend taxonomic boundaries under low-stress conditions.", "ja": "神経科学者らは、低ストレス環境下では家畜哺乳類のオキシトシン主導の感情回路が分類学上の境界を超越し得ると示唆しています。"},
        {"en": "The study provides compelling empirical support for reassessing cognitive sentience and empathetic capacities across non-human species.", "ja": "この研究は、人間以外の生物種における認知的知覚力や共感能力を再評価するための説得力ある実証的知見を提供しています。"}
    ],
    "dialogue": [
        {"speaker": "Keita先生", "name": "Keita先生", "role": "英語講師", "text": "ロバと雄牛という全く別の種類の動物が、互いに寄り添って親友のようになっている研究報告だよ。"},
        {"speaker": "Nanami", "name": "Nanami", "role": "生徒・アシスタント", "text": "言葉も鳴き声も違うのに、どうしてそんなに仲良くなれるんでしょうか？"},
        {"speaker": "Keita先生", "name": "Keita先生", "role": "英語講師", "text": "遺伝子を残すためだけでなく、哺乳類が持つオキシトシンなどの安心・愛着ホルモンが種を超えて働いている可能性があるんだよ。"},
        {"speaker": "Nanami", "name": "Nanami", "role": "生徒・アシスタント", "text": "動物にも豊かな共感や友情の感情があるという証拠ですね。生物学の視野が広がります！"}
    ],
    "quiz": [
        {
            "question": "What unusual behavior between the bull and the donkey surprised biologists?",
            "options": ["They displayed deep emotional attachment, mutual grooming, and distress upon separation.", "They began mimicking human speech patterns during feeding time.", "They formed an aggressive partnership to drive away all human farmhands.", "They completely refused to eat grass and hunted wild waterfowl instead."],
            "answer": 0,
            "explanation": "文2に「graze in unison, groom each other, and exhibit acute distress whenever separated」とあり、深い愛着と相互毛づくろい、分離時のストレスが描かれています。"
        },
        {
            "question": "Which biological theory does this cross-species bond challenge?",
            "options": ["The belief that animal social cooperation occurs strictly to propagate shared genes.", "The theory that mammals require oxygen to generate cellular metabolic energy.", "The physical law governing thermal conduction in heavy livestock bodies.", "The concept that domestic farm animals inherit mitochondrial DNA from mothers."],
            "answer": 0,
            "explanation": "文3に「challenge rigid sociobiological assumptions that social cohesion exists solely to propagate shared genes（共有遺伝子の増殖のためだけに社会的結束が存在するという前提への挑戦）」と明記されています。"
        },
        {
            "question": "What neurochemical mechanism is suggested to explain their interspecies bond?",
            "options": ["Oxytocin-driven emotional circuitry operating under low-stress conditions.", "Elevated adrenaline levels induced by dangerous coastal predators.", "Complete absence of sensory neurotransmitters in brain receptors.", "Synthetic vitamin injections administered by sanctuary veterinarians."],
            "answer": 0,
            "explanation": "文4に「oxytocin-driven emotional circuitry in domestic mammals can transcend taxonomic boundaries under low-stress conditions」と説明されています。"
        }
    ],
    "vocab": [
        {"word": "ethologist", "meaning": "動物行動学者", "example": "Ethologists observe natural animal interactions without disrupting habitats."},
        {"word": "interspecies", "meaning": "異種間の", "example": "Interspecies communication remains an intriguing field of animal cognition."},
        {"word": "cohesion", "meaning": "結束、結合", "example": "Social cohesion in elephant herds ensures the protection of young calves."},
        {"word": "sentience", "meaning": "知覚力、感覚・感情を持つ能力", "example": "Modern animal protection laws increasingly recognize mammalian sentience."}
    ]
}

# 3. polar-vortex-disruption-colder-weather-europe (environment)
s3 = {
    "slug": "polar-vortex-disruption-colder-weather-europe",
    "category": "environment",
    "date": "2026-11-03",
    "pub_date": "2026-11-03",
    "source_url": "https://www.theguardian.com/environment/2026/nov/02/polar-vortex-disruption-colder-weather-europe",
    "source_name": "The Guardian",
    "source_media": "The Guardian",
    "source_domain": "theguardian.com",
    "source_attribution": "The Guardian (November 2, 2026)",
    "category_label": "ENVIRONMENT • CLIMATE DYNAMICS",
    "title": "Disruption to Arctic Polar Vortex Sparks Early Winter Freeze Warnings Across Europe",
    "headline_ja": "北極寒冷渦（極渦）の分裂が欧州全域に早期冬の寒波警報をもたらす気象学的メカニズム",
    "lead_ja": "成層圏上空の急激な昇温によって北極上空の極渦（ポーラー・ボルテックス）が蛇行・分裂し、シベリアや北極圏の凍てつく寒気が欧州中南部に南下することで、今冬の急激な寒波とエネルギー需要逼迫への懸念が高まっています。",
    "subhead": "Meteorologists model stratospheric warming events that weaken atmospheric jet streams and unleash severe sub-zero cold.",
    "lead_snippet": "A sudden disturbance in the upper atmosphere could plunge parts of Europe into an unseasonably frigid November freeze.",
    "summary_points": [
        "成層圏突然昇温により、北極圏の強風帯（極渦）が弱まり寒気が中緯度へと南下。",
        "地球温暖化による北極海の海氷減少がジェット気流の蛇行を助長している可能性。",
        "暖房需要の急増による電力グリッドへの負荷と、農業への霜害リスクへの警戒。"
    ],
    "image": "https://images.unsplash.com/photo-1483921020237-2ff51e8e4b22?w=1000&auto=format&fit=crop&q=80",
    "sentences": [
        {"en": "Climatologists across northern and western Europe have issued early winter advisories as sudden stratospheric warming disrupts the Arctic polar vortex.", "ja": "成層圏突然昇温が北極寒冷渦を混乱させる中、北欧および西欧の気候学者らは早期の冬期注意報を発令しました。"},
        {"en": "Under normal conditions, a robust circumpolar jet stream traps freezing air over the Arctic pole like a spinning atmospheric fence.", "ja": "通常の状態では、強固な周極ジェット気流が回転する大気の防壁のように極寒の空気を北極上空に閉じ込めています。"},
        {"en": "However, rising temperatures in the stratosphere have fractured this vortex, allowing tongue-like lobes of sub-zero arctic air to spill southward.", "ja": "しかし、成層圏の気温上昇がこの渦を分断し、氷点下の北極気団が舌状の突出部となって南下することを許してしまいました。"},
        {"en": "Environmental scientists suspect that dwindling Arctic sea ice and warmer ocean temperatures are destabilizing northern hemispheric wind patterns.", "ja": "環境科学者らは、減少する北極海氷と海水温の上昇が北半球の風速パターンを不安定化させているのではないかと推測しています。"},
        {"en": "Grid operators are preparing for sharp spikes in natural gas consumption as heating demand surges unexpectedly early in November.", "ja": "電力グリッド運営会社は、11月に暖房需要が予期せず早期に急増することを受け、天然ガス消費の急激な跳ね上がりに備えています。"}
    ],
    "dialogue": [
        {"speaker": "Keita先生", "name": "Keita先生", "role": "英語講師", "text": "北極の寒気を閉じ込めている『極渦（ポーラー・ボルテックス）』が崩れて、欧州に大寒波が来るという気象ニュースだよ。"},
        {"speaker": "Nanami", "name": "Nanami", "role": "生徒・アシスタント", "text": "地球温暖化が進んでいるのに、どうして異常な大寒波が起きるんですか？"},
        {"speaker": "Keita先生", "name": "Keita先生", "role": "英語講師", "text": "良い質問だね。北極の氷が溶けて海が暖まると、ジェット気流が蛇行して北極の極寒の空気が南へ漏れ出しやすくなるんだ。"},
        {"speaker": "Nanami", "name": "Nanami", "role": "生徒・アシスタント", "text": "地球全体の気候システムが狂って、寒暖の差が極端になっているんですね。入試の記述問題でも頻出のテーマです！"}
    ],
    "quiz": [
        {
            "question": "What normally prevents frigid Arctic air from moving south into Europe?",
            "options": ["A robust circumpolar jet stream acting like a spinning atmospheric barrier.", "A continuous line of artificial mountain tunnels along the Scandinavian border.", "Warm steam emissions from underground continental geothermal wells.", "High-altitude industrial satellites blowing heated air toward the pole."],
            "answer": 0,
            "explanation": "文2に「a robust circumpolar jet stream traps freezing air over the Arctic pole like a spinning atmospheric fence」と説明されています。"
        },
        {
            "question": "What meteorological event caused the polar vortex to fracture?",
            "options": ["Sudden stratospheric warming in the upper atmosphere.", "An enormous tsunami in the southern Pacific Ocean.", "A total eclipse of the sun lasting for several weeks.", "Heavy cloud seeding conducted by regional farming communities."],
            "answer": 0,
            "explanation": "文1および文3に「sudden stratospheric warming disrupts the Arctic polar vortex」「rising temperatures in the stratosphere have fractured this vortex」とあります。"
        },
        {
            "question": "What economic concern is highlighted due to this early cold snap?",
            "options": ["A sharp spike in natural gas consumption and strain on energy grids.", "A complete collapse in the international demand for winter clothing.", "An inability of cargo container ships to sail on warm ocean waters.", "A total shutdown of digital financial trading platforms across London."],
            "answer": 0,
            "explanation": "文5に「Grid operators are preparing for sharp spikes in natural gas consumption as heating demand surges」と明記されています。"
        }
    ],
    "vocab": [
        {"word": "polar vortex", "meaning": "極渦（極上空を取り囲む大規模な寒気循環）", "example": "A weakened polar vortex can bring severe snowstorms to mid-latitudes."},
        {"word": "stratosphere", "meaning": "成層圏（対流圏の上にある高度約10〜50kmの大気層）", "example": "Ozone molecules in the stratosphere absorb harmful ultraviolet radiation."},
        {"word": "destabilize", "meaning": "〜を不安定にする", "example": "Rapid industrial changes can destabilize local labour markets."},
        {"word": "spike", "meaning": "急増、急上昇", "example": "Cold weather triggered a sudden spike in household electricity use."}
    ]
}

# 4. british-gas-resume-force-fitting-prepayment-meters-months-after-112m-settlement (environment / energy)
s4 = {
    "slug": "british-gas-resume-force-fitting-prepayment-meters-months-after-112m-settlement",
    "category": "environment",
    "date": "2026-11-03",
    "pub_date": "2026-11-03",
    "source_url": "https://www.theguardian.com/money/2026/nov/02/british-gas-resume-force-fitting-prepayment-meters-months-after-112m-settlement",
    "source_name": "The Guardian",
    "source_media": "The Guardian",
    "source_domain": "theguardian.com",
    "source_attribution": "The Guardian (November 2, 2026)",
    "category_label": "ENVIRONMENT • ENERGY POVERTY",
    "title": "Energy Suppliers Face Renewed Scrutiny Over Compulsory Prepayment Meters for Vulnerable Homes",
    "headline_ja": "エネルギー供給大手の先払いメーター強制設置再開、生活困窮家庭保護を巡り激しい論争",
    "lead_ja": "英大手エネルギー会社が、過去の強制設置スキャンダルでの多額の和解金支払いからわずか数か月後に、滞納家庭への前払いメーターの裁判所令状による強制取り付けを再開する方針を固め、燃料貧困対策団体や議員から非難を浴びています。",
    "subhead": "Campaigners and welfare charities condemn court-warrant installations that risk leaving low-income households without heat.",
    "lead_snippet": "Britain's largest domestic supplier moves to reinstate involuntary smart-meter switching despite ongoing winter hardship.",
    "summary_points": [
        "料金滞納世帯に対して遠隔または令状で前払いメーターに強制変更する手法が再開方針へ。",
        "前払いメーターは残高が切れると即座に暖房や電気が止まり、高齢者や子育て世帯の健康危機に直結。",
        "企業の債権回収の権利と、生存権に関わるエネルギーアクセスの基本的人権との法的対立。"
    ],
    "image": "https://images.unsplash.com/photo-1473341304170-971dccb5ac1e?w=1000&auto=format&fit=crop&q=80",
    "sentences": [
        {"en": "Britain's leading energy supplier has provoked fierce public outrage after announcing plans to resume court-warranted prepayment meter installations for indebted households.", "ja": "英国大手のエネルギー供給会社が、負債を抱えた世帯に対して裁判所の令状に基づく前払いメーターの設置を再開する計画を発表し、激しい公衆の怒りを引き起こしました。"},
        {"en": "The controversial practice forces consumers who fall behind on bills onto pay-as-you-go systems where energy cuts off immediately when funds run dry.", "ja": "この物議を醸す慣行は、料金を滞納した消費者に、残高が尽きると直ちにエネルギー供給が遮断される都度払いシステムを強制するものです。"},
        {"en": "Poverty charities argue that compulsory disconnections during frigid winter months endanger vulnerable pensioners and infants living in damp accommodation.", "ja": "貧困救済団体は、極寒の冬期における強制的な遮断は、湿気の多い住環境で暮らす脆弱な年金受給者や乳幼児を危険にさらすと主張しています。"},
        {"en": "Energy executives counter that accumulating customer debt of billions of pounds forces suppliers to pass higher tariffs onto paying customers.", "ja": "エネルギー企業の幹部らは、何十億ポンドにも及ぶ顧客債務の累積により、料金を払っている他の顧客に高額な料金を転嫁せざるを得なくなると反論しています。"},
        {"en": "Consumer rights regulators are examining whether updated protection codes are sufficient to shield citizens with chronic medical vulnerabilities.", "ja": "消費者権利の規制当局は、更新された保護規範が慢性的な病気を持つ脆弱な市民を守るのに十分であるかどうかを精査しています。"}
    ],
    "dialogue": [
        {"speaker": "Keita先生", "name": "Keita先生", "role": "英語講師", "text": "ガス代や電気代を滞納した家庭に、お金をチャージしないと止まる『前払いメーター』を強制設置する動きが再開されて問題になっているよ。"},
        {"speaker": "Nanami", "name": "Nanami", "role": "生徒・アシスタント", "text": "冬にお金がなくて暖房が止まってしまったら、命に関わりますよね…。"},
        {"speaker": "Keita先生", "name": "Keita先生", "role": "英語講師", "text": "そうなんだ。一方で企業側も未払い金が巨額に膨らむと事業が成り立たないと主張していて、エネルギーへのアクセスを人権としてどう保障するかが問われているんだ。"},
        {"speaker": "Nanami", "name": "Nanami", "role": "生徒・アシスタント", "text": "公共インフラの維持と、弱者の生存権の保障という、現代福祉国家の重い課題ですね。"}
    ],
    "quiz": [
        {
            "question": "Why has the resumption of compulsory prepayment meter installations triggered backlash?",
            "options": ["It cuts off heating and electricity immediately when low-income families run out of money.", "It requires residents to replace all copper water pipes inside their homes.", "It forces consumers to pay their gas bills exclusively in foreign currencies.", "It allows energy companies to demolish old residential apartments without notice."],
            "answer": 0,
            "explanation": "文2に「forces consumers who fall behind on bills onto pay-as-you-go systems where energy cuts off immediately when funds run dry」と書かれています。"
        },
        {
            "question": "What argument do energy executives make in defense of prepayment meters?",
            "options": ["Massive unpaid debt forces suppliers to increase prices on paying customers.", "Smart prepayment meters automatically purify room air during the winter.", "They want all UK citizens to adopt off-grid solar energy systems.", "They are legally mandated to donate all gas company profits to local libraries."],
            "answer": 0,
            "explanation": "文4に「accumulating customer debt of billions of pounds forces suppliers to pass higher tariffs onto paying customers」とあります。"
        },
        {
            "question": "What are consumer regulators specifically investigating?",
            "options": ["Whether protection rules adequately shield citizens with chronic health conditions.", "Whether prepayment meters can be used to recharge electric scooters in the street.", "How to ban private companies from selling electricity across England.", "If households can generate nuclear energy in their private basements."],
            "answer": 0,
            "explanation": "文5に「whether updated protection codes are sufficient to shield citizens with chronic medical vulnerabilities」と述べられています。"
        }
    ],
    "vocab": [
        {"word": "prepayment meter", "meaning": "前払いメーター（料金事前支払い式計量器）", "example": "Prepayment meters require credit keys or cards to maintain electricity."},
        {"word": "warrant", "meaning": "（裁判所が発行する）令状、許可状", "example": "The magistrate issued a legal warrant for the premises inspection."},
        {"word": "indebted", "meaning": "負債を抱えた、借金のある", "example": "Many indebted households struggle to meet basic living costs."},
        {"word": "vulnerability", "meaning": "脆弱性、傷つきやすさ", "example": "Economic shocks worsen social vulnerability among low-income families."}
    ]
}

# 5. nhs-early-warning-system-child-illness-england (society)
s5 = {
    "slug": "nhs-early-warning-system-child-illness-england",
    "category": "society",
    "date": "2026-11-03",
    "pub_date": "2026-11-03",
    "source_url": "https://www.theguardian.com/society/2026/nov/02/nhs-early-warning-system-child-illness-england",
    "source_name": "The Guardian",
    "source_media": "The Guardian",
    "source_domain": "theguardian.com",
    "source_attribution": "The Guardian (November 2, 2026)",
    "category_label": "SOCIETY • HEALTHCARE REFORM",
    "title": "National Health Service Rolls Out Standardised Child Illness Early Warning Network",
    "headline_ja": "英国民保健サービス（NHS）、小児の急変を早期察知する全国統一警報システムを導入",
    "lead_ja": "英国全土の病院において、子どもの急激な体調悪化や敗血症などの致命的疾患を早期に発見するため、保護者の直感を臨床スコアに組み込む全国統一の小児早期警告システム（PEWS）の全面稼働が始まりました。",
    "subhead": "Standardised pediatric scoring incorporates parental intuition alongside vital clinical metrics to prevent avoidable hospital fatalities.",
    "lead_snippet": "A landmark clinical safety reform empowers parents and medical teams to detect acute deterioration in hospitalized children.",
    "summary_points": [
        "乳幼児の急激な容態悪化を見逃さないための全国標準化スコアリングシステムが導入。",
        "脈拍や血圧などのバイタルデータに加え、「親の違和感・直感（Parental Concern）」を正式指標に採用。",
        "医療従事者の経験不足や引継ぎミスによる防ぎ得た死亡事故の根絶を目指す先進的医療安全改革。"
    ],
    "image": "https://images.unsplash.com/photo-1579684385127-1ef15d508118?w=1000&auto=format&fit=crop&q=80",
    "sentences": [
        {"en": "Hospitals across England have commenced the nationwide rollout of a standardised pediatric early warning system to catch rapid physical deterioration in young patients.", "ja": "イングランド全土の病院は、若い患者の急速な身体的悪化を察知するための全国標準化された小児早期警告システムの運用を開始しました。"},
        {"en": "Under the new protocol, healthcare professionals measure respiratory rates and heart rhythm alongside formal documentation of parental anxiety.", "ja": "新たなプロトコルの下で、医療従事者は呼吸数や心拍リズムとともに、保護者の不安に関する正式な記録を測定します。"},
        {"en": "Medical audits revealed that parents frequently sensed subtle behavioral changes hours before standard biometric instruments detected life-threatening sepsis.", "ja": "医療監査により、標準的な生体測定器が生命を脅かす敗血症を検知する数時間前に、親たちが微細な行動の変化を頻繁に察知していたことが明らかになりました。"},
        {"en": "Senior pediatricians celebrate the reform as a cultural shift from paternalistic medical authority toward patient-family collaborative care.", "ja": "上級小児科医らはこの改革を、家父長的な医療権威から患者・家族との協働的ケアへの文化的な転換として称賛しています。"},
        {"en": "Health authorities anticipate that standardising alert thresholds across regional trusts will prevent dozens of avoidable child deaths annually.", "ja": "保健当局は、地域の医療トラスト全体で警告基準値を標準化することで、年間数十件の防ぎ得た小児死亡を防ぐことができると期待しています。"}
    ],
    "dialogue": [
        {"speaker": "Keita先生", "name": "Keita先生", "role": "英語講師", "text": "イギリスの病院で、子どもの容態急変を防ぐために『親の直感』を正式な診断データとして取り入れるシステムが始まったよ。"},
        {"speaker": "Nanami", "name": "Nanami", "role": "生徒・アシスタント", "text": "機械の数値だけでなく、いつも一緒にいる親の『いつもと様子が違う』という感覚を重視するんですね！"},
        {"speaker": "Keita先生", "name": "Keita先生", "role": "英語講師", "text": "その通り。敗血症などは数値に出る前のわずかな変化を親が一番早く気づくことが多いんだ。医療従事者と家族のチームワークだね。"},
        {"speaker": "Nanami", "name": "Nanami", "role": "生徒・アシスタント", "text": "患者家族の声を医療安全に生かす素晴らしいアプローチですね！"}
    ],
    "quiz": [
        {
            "question": "What novel factor is explicitly included in the new pediatric early warning system?",
            "options": ["Formal clinical documentation of parental concern and anxiety.", "The educational level and university degrees of the child's grandparents.", "The speed at which children can perform mental arithmetic exercises.", "The brand of clothing the child was wearing upon hospital admission."],
            "answer": 0,
            "explanation": "文2に「alongside formal documentation of parental anxiety」とあり、保護者の不安や懸念が正式な指標に含まれています。"
        },
        {
            "question": "What did medical audits uncover about parental observations during sepsis onset?",
            "options": ["Parents often noticed subtle behavioral changes hours before monitors detected sepsis.", "Parents were completely unable to recognize severe physical symptoms in infants.", "Parents insisted that children should leave intensive care units immediately.", "Parents preferred herbal remedies over standard intravenous antibiotics."],
            "answer": 0,
            "explanation": "文3に「parents frequently sensed subtle behavioral changes hours before standard biometric instruments detected life-threatening sepsis」と書かれています。"
        },
        {
            "question": "How do senior pediatricians describe the broader significance of this reform?",
            "options": ["A cultural shift from paternalistic authority toward collaborative family care.", "A practical method to reduce hospital doctor salaries by half.", "An encouragement for all nurses to abandon physical clinical checkups.", "A mandatory requirement for parents to administer injections themselves."],
            "answer": 0,
            "explanation": "文4に「a cultural shift from paternalistic medical authority toward patient-family collaborative care」と述べられています。"
        }
    ],
    "vocab": [
        {"word": "pediatric", "meaning": "小児科の、小児治療の", "example": "Pediatric nurses receive specialized training in treating young infants."},
        {"word": "deterioration", "meaning": "悪化、退廃", "example": "Early detection prevents the rapid deterioration of chronic illness."},
        {"word": "sepsis", "meaning": "敗血症（全身に炎症が広がる生命を脅かす感染症）", "example": "Immediate antibiotic treatment is critical in reversing severe sepsis."},
        {"word": "paternalistic", "meaning": "家父長的な、パターナリズムの（強者が弱者に一方的に決定を下す）", "example": "Modern medical ethics rejects paternalistic decision-making by doctors."}
    ]
}

# 6. counsellors-psychotherapists-statutory-regulation-uk-professional-bodies (society)
s6 = {
    "slug": "counsellors-psychotherapists-statutory-regulation-uk-professional-bodies",
    "category": "society",
    "date": "2026-11-03",
    "pub_date": "2026-11-03",
    "source_url": "https://www.theguardian.com/society/2026/nov/02/counsellors-psychotherapists-statutory-regulation-uk-professional-bodies",
    "source_name": "The Guardian",
    "source_media": "The Guardian",
    "source_domain": "theguardian.com",
    "source_attribution": "The Guardian (November 2, 2026)",
    "category_label": "SOCIETY • MENTAL HEALTH LAW",
    "title": "Therapists and Patient Groups Demand Statutory Regulation of Psychological Counselling",
    "headline_ja": "心理カウンセラー・セラピストの国家資格化を要求：無資格開業から患者を守る法規制論争",
    "lead_ja": "英国では現在、誰でも法的な資格なしに「心理療法士」や「カウンセラー」を名乗って開業できる抜け穴が存在しており、不適切なセラピーによる精神的トラウマを防ぐため、公的団体が法定規制（国家資格化）の導入を政府に強く求めています。",
    "subhead": "Professional bodies warn that the lack of legal title protection allows unqualified practitioners to exploit vulnerable clients.",
    "lead_snippet": "Campaigners urge ministers to close loopholes that permit anyone to set up practice as a psychotherapist without verified credentials.",
    "summary_points": [
        "英国では「カウンセラー」という肩書が法的に保護されておらず、無資格者による開業が可能。",
        "短時間の民間オンライン講座を受けただけの施術者が重度トラウマ患者を担当し、被害が拡大。",
        "医師や看護師と同様に、法定登録制度と懲戒規定を義務づける法改正を求める声が高まる。"
    ],
    "image": "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=1000&auto=format&fit=crop&q=80",
    "sentences": [
        {"en": "Leading mental health organizations in the United Kingdom are urging parliament to introduce statutory regulation for all counsellors and psychotherapists.", "ja": "英国の主要なメンタルヘルス団体は、すべてのカウンセラーおよび心理療法士に対する法定規制を導入するよう議会に強く求めています。"},
        {"en": "Under current British law, the professional titles of therapist and counsellor are entirely unprotected, permitting anyone to practice without credentials.", "ja": "現行の英国法の下では、セラピストやカウンセラーという職業肩書は一切保護されておらず、資格のない者でも誰でも開業することが認められています。"},
        {"en": "Patient advocacy groups report alarming cases where predatory practitioners with minimal online training caused severe psychological re-traumatisation.", "ja": "患者支援団体は、最低限のオンライン研修しか受けていない悪質な施術者が、深刻な心理的再トラウマを引き起こした憂慮すべき事例を報告しています。"},
        {"en": "Regulated clinical psychologists argue that statutory licensing would establish enforceable ethical standards and protect vulnerable people seeking trauma therapy.", "ja": "公的資格を持つ臨床心理士らは、法定免許制度が強制力のある倫理基準を確立し、トラウマ治療を求める脆弱な人々を保護することになると主張しています。"},
        {"en": "Government ministers acknowledged the concerns and confirmed that independent regulatory reviews will assess mandatory national registration schemes.", "ja": "政府閣僚らはこれらの懸念を認識し、独立した規制検証において義務的な全国登録制度の導入を評価することを確認しました。"}
    ],
    "dialogue": [
        {"speaker": "Keita先生", "name": "Keita先生", "role": "英語講師", "text": "イギリスでは『カウンセラー』という肩書に法的な資格要件がなく、誰でも名乗れてしまう抜け穴が問題になっているよ。"},
        {"speaker": "Nanami", "name": "Nanami", "role": "生徒・アシスタント", "text": "えっ、資格がなくてもカウンセラーとして心療クリニックを開けちゃうんですか？"},
        {"speaker": "Keita先生", "name": "Keita先生", "role": "英語講師", "text": "そうなんだ。ネットの数時間講習を受けただけの人が深刻な心の病の人を診て、かえって症状を悪化させるケースがあるため、国家資格化が求められているんだ。"},
        {"speaker": "Nanami", "name": "Nanami", "role": "生徒・アシスタント", "text": "心の健康を守るためにも、医師と同じように国による厳格な資格認定と倫理基準が不可欠ですね。"}
    ],
    "quiz": [
        {
            "question": "What legal loophole currently exists in the UK regarding psychological therapy?",
            "options": ["Anyone can call themselves a counsellor or therapist without official credentials.", "Only lawyers are permitted to offer psychological therapy sessions.", "Mental health treatment is strictly banned outside royal palaces.", "All counselling sessions must be broadcast live on national television."],
            "answer": 0,
            "explanation": "文2に「the professional titles of therapist and counsellor are entirely unprotected, permitting anyone to practice without credentials」とあります。"
        },
        {
            "question": "What harm has resulted from this lack of regulatory title protection?",
            "options": ["Unqualified practitioners with minimal training have caused severe re-traumatisation.", "Patients have stopped buying prescription glasses from opticians.", "Universities have been forced to close down all medical libraries.", "Hospitals have run out of clean drinking water in emergency rooms."],
            "answer": 0,
            "explanation": "文3に「predatory practitioners with minimal online training caused severe psychological re-traumatisation」と明記されています。"
        },
        {
            "question": "What solution are regulated clinical psychologists demanding from parliament?",
            "options": ["Statutory licensing and mandatory national registration schemes.", "A complete ban on discussing emotional trauma in private conversations.", "Replacing all human counsellors with automated banking software.", "Requiring all therapy clients to pay ten thousand pounds in cash."],
            "answer": 0,
            "explanation": "文4および文5に「statutory licensing would establish enforceable ethical standards」「mandatory national registration schemes」と述べられています。"
        }
    ],
    "vocab": [
        {"word": "statutory", "meaning": "法定の、法律で定められた", "example": "Companies must follow statutory safety regulations in the workplace."},
        {"word": "credential", "meaning": "資格証明書、経歴", "example": "The hospital verifies every doctor's medical credentials before hiring."},
        {"word": "predatory", "meaning": "略奪的な、他者を利用・搾取するような", "example": "Regulators cracked down on predatory lending practices."},
        {"word": "traumatisation", "meaning": "心的外傷の発生、トラウマ化", "example": "Improper questioning during trials can lead to re-traumatisation of victims."}
    ]
}

# 7. nine-of-world-biggest-oil-firms-95bn-profit-third-quarter-iran-war (world)
s7 = {
    "slug": "nine-of-world-biggest-oil-firms-95bn-profit-third-quarter-iran-war",
    "category": "world",
    "date": "2026-11-03",
    "pub_date": "2026-11-03",
    "source_url": "https://www.theguardian.com/business/2026/nov/02/nine-of-world-biggest-oil-firms-95bn-profit-third-quarter-iran-war",
    "source_name": "The Guardian",
    "source_media": "The Guardian",
    "source_domain": "theguardian.com",
    "source_attribution": "The Guardian (November 2, 2026)",
    "category_label": "WORLD • ENERGY GEOPOLITICS",
    "title": "Global Oil Majors Post Record $95 Billion Quarterly Profits Amid Middle East Conflict",
    "headline_ja": "国際石油メジャー9社、中東紛争による原油高騰で四半期純利益950億ドルの空前記録",
    "lead_ja": "世界の大手石油会社9社が2026年第3四半期の決算を発表し、中東情勢の緊迫化に伴う原油価格の高騰により合計950億ドル（約14兆6,000億円）の純利益を計上したことで、超過利潤税（連帯税）の導入を求める世論が再燃しています。",
    "subhead": "Surging energy prices deliver massive corporate bonanzas while households face mounting cost-of-living strain.",
    "lead_snippet": "Supermajors announce mammoth dividend payouts as geopolitical tensions around maritime oil transit drive crude prices higher.",
    "summary_points": [
        "ホルムズ海峡などを巡る中東リスクを背景に、原油先物と精製マージンが跳ね上がり石油メジャーが空前の利益。",
        "一般家庭が光熱費高騰やインフレに直面する中、巨額の自社株買いや株主配当を実施していることに批判が集中。",
        "化石燃料依存からの脱却と、戦争利得（ウィンドフォール）に対する税制改革の是非が世界的な政治論争に。"
    ],
    "image": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=1000&auto=format&fit=crop&q=80",
    "sentences": [
        {"en": "Nine of the world's largest fossil fuel conglomerates generated a combined ninety-five billion dollars in net profits during the third quarter.", "ja": "世界最大手クラスの化石燃料コングロマリット9社は、第3四半期中に合計950億ドルの純利益を生み出しました。"},
        {"en": "Intensifying geopolitical confrontation across the Middle East triggered sharp spikes in international crude benchmarks and refining margins.", "ja": "中東全域で激化する地政学的対立が、国際原油の指標価格や精製マージンの急激な跳ね上がりを引き起こしました。"},
        {"en": "While multi-billion-dollar shareholder dividends were celebrated in financial capitals, anti-poverty charities condemned the bonanza amid household inflation.", "ja": "金融街では数十億ドル規模の株主配当が称賛された一方で、貧困撲滅団体は家庭のインフレ下におけるこの巨額の利益を非難しました。"},
        {"en": "Opposition lawmakers in Europe renewed calls for windfall taxes to channel surplus fossil fuel revenue directly into renewable transition infrastructure.", "ja": "欧州の野党議員らは、余剰の化石燃料収益を直接再生可能エネルギーへの移行インフラに振り向けるため、超過利潤税の導入要求を再燃させました。"},
        {"en": "Energy analysts warn that enduring volatility in maritime trade routes will keep global energy prices elevated throughout the coming fiscal year.", "ja": "エネルギーアナリストらは、海上貿易航路における継続的な不安定さが、来年度を通じて世界のエネルギー価格を高止まりさせると警告しています。"}
    ],
    "dialogue": [
        {"speaker": "Keita先生", "name": "Keita先生", "role": "英語講師", "text": "中東の情勢不安による原油高で、石油メジャー9社が3か月で約15兆円もの巨額利益を上げたニュースだよ。"},
        {"speaker": "Nanami", "name": "Nanami", "role": "生徒・アシスタント", "text": "15兆円！一般の市民はガソリン代や電気代が高くて苦しんでいるのに、企業だけがそんなに儲かっているんですか？"},
        {"speaker": "Keita先生", "name": "Keita先生", "role": "英語講師", "text": "その通り。だからこそ『戦争や危機で得た超過利潤（Windfall Profit）に特別税をかけて、市民の生活支援や再エネ投資に回すべきだ』という議論が起きているんだ。"},
        {"speaker": "Nanami", "name": "Nanami", "role": "生徒・アシスタント", "text": "企業の利益追求の自由と、社会の公平な富の再配分のあり方を考えさせられますね。"}
    ],
    "quiz": [
        {
            "question": "What factor drove the $95 billion profit surge for major oil companies?",
            "options": ["Geopolitical conflicts in the Middle East that spiked crude oil prices and refining margins.", "A worldwide ban on solar panels and electric passenger cars.", "An agreement by all governments to subsidize luxury private jets.", "A massive discovery of gold reserves inside drilling platforms."],
            "answer": 0,
            "explanation": "文2に「Intensifying geopolitical confrontation across the Middle East triggered sharp spikes in international crude benchmarks and refining margins」とあります。"
        },
        {
            "question": "Why did anti-poverty charities condemn the record corporate profits?",
            "options": ["Ordinary households are suffering from severe cost-of-living inflation and high energy bills.", "Oil companies refused to hire workers who graduated from universities.", "The profits were paid in physical silver bars instead of paper banknotes.", "Charities wanted all oil refineries to be converted into art museums."],
            "answer": 0,
            "explanation": "文3に「anti-poverty charities condemned the bonanza amid household inflation」と述べられています。"
        },
        {
            "question": "What policy proposal was revived by European lawmakers in response?",
            "options": ["Enacting windfall taxes to fund renewable transition infrastructure.", "Abolishing all taxes on corporate fossil fuel dividends permanently.", "Banning private ownership of public electricity networks.", "Forcing citizens to walk instead of taking public transportation."],
            "answer": 0,
            "explanation": "文4に「renewed calls for windfall taxes to channel surplus fossil fuel revenue directly into renewable transition infrastructure」と明記されています。"
        }
    ],
    "vocab": [
        {"word": "conglomerate", "meaning": "複合企業、コングロマリット", "example": "The multinational conglomerate operates across energy, mining, and shipping."},
        {"word": "refining margin", "meaning": "精製マージン（原油から石油製品を精製する際の利幅）", "example": "Higher refining margins boosted refinery profitability this quarter."},
        {"word": "bonanza", "meaning": "思いがけない大幸運、大もうけ", "example": "The real estate boom proved to be a financial bonanza for early investors."},
        {"word": "windfall tax", "meaning": "超過利潤税、横光税（予期せぬ外部要因で生じた莫大な利益への課税）", "example": "Ministers introduced a windfall tax on excessive energy trading profits."}
    ]
}

# 8. hackers-fake-nuclear-chemical-threat-alert-kyiv-ukraine-emergency-app (world)
s8 = {
    "slug": "hackers-fake-nuclear-chemical-threat-alert-kyiv-ukraine-emergency-app",
    "category": "world",
    "date": "2026-11-03",
    "pub_date": "2026-11-03",
    "source_url": "https://www.theguardian.com/world/2026/nov/02/hackers-fake-nuclear-chemical-threat-alert-kyiv-ukraine-emergency-app",
    "source_name": "The Guardian",
    "source_media": "The Guardian",
    "source_domain": "theguardian.com",
    "source_attribution": "The Guardian (November 2, 2026)",
    "category_label": "WORLD • HYBRID CYBERWARFARE",
    "title": "State-Sponsored Hackers Breach Kyiv Emergency Warning App to Broadcast False Chemical Threat",
    "headline_ja": "サイバー攻撃でキーウ市民防衛アプリが侵入被害：偽の核・化学兵器警報で心理的混乱狙う",
    "lead_ja": "ウクライナの首都キーウにおいて、数百万人の市民が空襲警報を受信する公式スマートフォンアプリが不正アクセスを受け、放射性物質や化学兵器の攻撃が切迫しているとする偽警報が一斉配信され、治安機関が緊急調査を開始しました。",
    "subhead": "Digital saboteurs target municipal civil defence infrastructure to induce public panic and undermine wartime communication resilience.",
    "lead_snippet": "A malicious intrusion into an official civil alert application triggered false evacuation sirens across the Ukrainian capital.",
    "summary_points": [
        "市民の命を守る公的防衛警報アプリがサイバー侵入され、虚偽の化学兵器攻撃通知が拡散。",
        "重要インフラや緊急通報網を標的にして社会不安を煽る『ハイブリッド認知戦』の典型例。",
        "サイバーセキュリティと公的通知システムの暗号化・二重認証の緊急強化が急務に。"
    ],
    "image": "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=1000&auto=format&fit=crop&q=80",
    "sentences": [
        {"en": "State-sponsored cyber saboteurs infiltrated the official emergency alert mobile application used by millions of residents in Ukraine's capital.", "ja": "国家支援を受けたサイバー妨害工作員が、ウクライナ首都の何百万人もの住民が利用する公式緊急警報モバイルアプリに侵入しました。"},
        {"en": "The rogue breach triggered fraudulent push notifications warning of an imminent chemical and radioactive strike across downtown Kyiv.", "ja": "この不正侵入により、キーウ中心街全域に化学物質や放射性物質による攻撃が切迫していると警告する虚偽のプッシュ通知が発出されました。"},
        {"en": "Although cybersecurity defenders neutralized the unauthorized access within minutes, the incident caused intense temporary panic among civilians.", "ja": "サイバーセキュリティの防御担当者が数分以内に不正アクセスを無力化したものの、この事件は民間人の間に激しい一時的パニックを引き起こしました。"},
        {"en": "Military intelligence analysts characterised the assault as cognitive hybrid warfare designed to erode institutional trust in civil defence channels.", "ja": "軍事情報アナリストらはこの攻撃を、民間防衛ルートに対する公的信頼を損なうよう企図された認知的ハイブリッド戦争であると位置づけました。"},
        {"en": "International cybersecurity agencies are assisting municipal engineers to implement decentralized cryptographic verification for all national alert broadcasts.", "ja": "国際サイバーセキュリティ機関は、すべての国家警報配信に対して分散型の暗号化検証を導入するよう、自治体のエンジニアを支援しています。"}
    ],
    "dialogue": [
        {"speaker": "Keita先生", "name": "Keita先生", "role": "英語講師", "text": "ウクライナの避難警報アプリがハッキングされ、偽の化学兵器警報が何百万人にも届いたニュースだよ。"},
        {"speaker": "Nanami", "name": "Nanami", "role": "生徒・アシスタント", "text": "防空警報アプリが乗っ取られるなんて、市民にとっては本当に恐ろしいですね…！"},
        {"speaker": "Keita先生", "name": "Keita先生", "role": "英語講師", "text": "そうなんだ。実際の兵器だけでなく、偽情報でパニックを起こして社会を混乱させる『ハイブリッド認知戦』の脅威が現実化しているんだよ。"},
        {"speaker": "Nanami", "name": "Nanami", "role": "生徒・アシスタント", "text": "防災アプリのセキュリティや暗号化が、命を守る最前線になっているんですね。"}
    ],
    "quiz": [
        {
            "question": "What false message was sent through the hacked Ukrainian emergency app?",
            "options": ["A warning claiming that an imminent chemical and radioactive strike was taking place.", "An announcement that public transport buses would be free of charge forever.", "A notice telling all citizens to plant sunflower seeds in municipal parks.", "An alert that national currency banknotes were being replaced with stamps."],
            "answer": 0,
            "explanation": "文2に「fraudulent push notifications warning of an imminent chemical and radioactive strike」と明記されています。"
        },
        {
            "question": "How did military intelligence analysts describe the nature of this cyber-attack?",
            "options": ["Cognitive hybrid warfare intended to damage institutional trust in civil alerts.", "An innocent technical malfunction caused by cold weather on antennas.", "A routine software update performed by private app store developers.", "An experimental advertising campaign created by mobile phone companies."],
            "answer": 0,
            "explanation": "文4に「cognitive hybrid warfare designed to erode institutional trust in civil defence channels」と書かれています。"
        },
        {
            "question": "What measure are cybersecurity agencies assisting local engineers to implement?",
            "options": ["Decentralized cryptographic verification for all emergency broadcasts.", "Removing all computers from municipal government buildings.", "Requiring citizens to uninstall emergency mobile applications.", "Replacing all digital communications with printed daily pamphlets."],
            "answer": 0,
            "explanation": "文5に「implement decentralized cryptographic verification for all national alert broadcasts」と説明されています。"
        }
    ],
    "vocab": [
        {"word": "infiltrate", "meaning": "〜に侵入する、潜入する", "example": "Malware infiltrated the central hospital database through an email link."},
        {"word": "fraudulent", "meaning": "詐欺的な、不正な、虚偽の", "example": "The bank blocked fraudulent credit transactions immediately."},
        {"word": "hybrid warfare", "meaning": "ハイブリッド戦争（正規戦・サイバー戦・情報心理戦を組み合わせた複合戦）", "example": "Modern conflicts combine economic sanctions with digital hybrid warfare."},
        {"word": "cryptographic", "meaning": "暗号技術の、暗号学の", "example": "Cryptographic keys protect digital communication between servers."}
    ]
}

# 9. australia-social-media-ban-high-court-challenge-reddit-digital-freedom-project (law)
s9 = {
    "slug": "australia-social-media-ban-high-court-challenge-reddit-digital-freedom-project",
    "category": "law",
    "date": "2026-11-03",
    "pub_date": "2026-11-03",
    "source_url": "https://www.theguardian.com/australia-news/2026/nov/03/australia-social-media-ban-high-court-challenge-reddit-digital-freedom-project",
    "source_name": "The Guardian",
    "source_media": "The Guardian",
    "source_domain": "theguardian.com",
    "source_attribution": "The Guardian (November 3, 2026)",
    "category_label": "LAW • DIGITAL CONSTITUTIONAL RIGHTS",
    "title": "Australia's Youth Social Media Ban Faces Landmark Constitutional Challenge in High Court",
    "headline_ja": "オーストラリアの未成年SNS禁止法、憲法違反を巡り最高裁で歴史的法廷闘争へ",
    "lead_ja": "オーストラリア連邦政府が可決した16歳未満のSNS利用全面禁止法について、デジタル権利団体や利用者が「表現の自由の暗黙の保障や政治的対話の権利を侵害している」として、最高裁判所に違憲訴訟を提起しました。",
    "subhead": "Civil liberties advocates contest strict age-verification mandates, citing implicit constitutional protections for political discourse.",
    "lead_snippet": "A historic constitutional showdown begins as youth advocacy groups take Australia's age-limit internet legislation to the High Court.",
    "summary_points": [
        "豪州政府が可決した16歳未満のソーシャルメディア完全禁止法に対し、最高裁で違憲審査の申し立て。",
        "オーストラリア憲法が保障する『政治的コミュニケーションの暗黙の自由』を侵害しているかが最大の争点。",
        "未成年者のメンタルヘルス保護と、青少年の情報アクセス権・プライバシー権との法益衡量。"
    ],
    "image": "https://images.unsplash.com/photo-1589829545856-d10d557cf95f?w=1000&auto=format&fit=crop&q=80",
    "sentences": [
        {"en": "A coalition of civil rights advocates and digital platforms has launched a constitutional challenge against Australia's blanket social media ban for minors.", "ja": "市民の権利擁護派とデジタルプラットフォームの連合体が、オーストラリアの未成年者に対するソーシャルメディア全面禁止令に対し違憲訴訟を開始しました。"},
        {"en": "The legislation requires global tech platforms to enforce biometric age verification to prevent anyone under sixteen from holding active accounts.", "ja": "この法律は、16歳未満の者がアクティブなアカウントを保持することを防ぐため、グローバルなIT企業に生体認証による年齢確認の実施を義務付けています。"},
        {"en": "Plaintiffs argue in the High Court that the law infringes upon the constitutionally implied freedom of political communication and civic participation.", "ja": "原告らは最高裁において、この法律が憲法上暗黙に保障されている政治的コミュニケーションの自由や市民参加の権利を侵害していると主張しています。"},
        {"en": "Government lawyers contend that the state possesses a compelling public interest in shielding young brains from addictive algorithms and cyberbullying.", "ja": "政府側弁護団は、中毒性のあるアルゴリズムやネットいじめから若者の脳を保護することに国家は強い公益上の利益を有していると反論しています。"},
        {"en": "Constitutional scholars around the democratic world are closely monitoring the case as a bellwether for state intervention in digital cyberspace.", "ja": "民主主義各国の憲法学者らは、デジタルサイバースペースに対する国家介入の先駆的事例として、この訴訟を注視しています。"}
    ],
    "dialogue": [
        {"speaker": "Keita先生", "name": "Keita先生", "role": "英語講師", "text": "オーストラリアで16歳未満のSNS利用を禁止する法律が成立したけれど、憲法違反だとして最高裁で裁判が始まったよ。"},
        {"speaker": "Nanami", "name": "Nanami", "role": "生徒・アシスタント", "text": "16歳未満が全員SNS禁止ってすごく思い切った法律ですね！何が憲法違反なんですか？"},
        {"speaker": "Keita先生", "name": "Keita先生", "role": "英語講師", "text": "若者のメンタルを守る目的はわかるけれど、政治的な意見を発信したり情報を得る権利を奪い、生体認証でプライバシーも侵害するという主張だね。"},
        {"speaker": "Nanami", "name": "Nanami", "role": "生徒・アシスタント", "text": "青少年の保護と、表現の自由のどちらを優先すべきか、世界中が注目する裁判ですね。"}
    ],
    "quiz": [
        {
            "question": "What does Australia's contested legislation mandate regarding young social media users?",
            "options": ["A blanket prohibition on active accounts for individuals under sixteen years of age.", "A requirement that all teenagers post only positive school news on public forums.", "An order forcing social networks to give free smartphones to primary school children.", "A rule that all social media posts must be translated into Latin before sharing."],
            "answer": 0,
            "explanation": "文1および文2に「blanket social media ban for minors」「prevent anyone under sixteen from holding active accounts」と明記されています。"
        },
        {
            "question": "What primary constitutional argument do the plaintiffs advance in the High Court?",
            "options": ["The ban infringes upon the implied freedom of political communication and civic dialogue.", "The federal constitution forbids the use of computers inside state libraries.", "High technology companies are exempt from all national legal jurisdictions.", "Minors have an absolute right to purchase commercial digital software without parental consent."],
            "answer": 0,
            "explanation": "文3に「infringes upon the constitutionally implied freedom of political communication and civic participation」とあります。"
        },
        {
            "question": "How does the Australian government justify the restrictive measure?",
            "options": ["By citing a compelling state interest in protecting adolescent mental health from harmful algorithms.", "By arguing that banning phones reduces the consumption of domestic electricity.", "By claiming that social media prevents children from learning traditional sports.", "By proving that algorithms cause physical damage to telecommunication cables."],
            "answer": 0,
            "explanation": "文4に「compelling public interest in shielding young brains from addictive algorithms and cyberbullying」と書かれています。"
        }
    ],
    "vocab": [
        {"word": "blanket ban", "meaning": "全面禁止、一律禁止", "example": "The government imposed a blanket ban on single-use plastics."},
        {"word": "biometric", "meaning": "生体認証の（指紋・顔・虹彩などの身体特徴による）", "example": "Biometric scanners are used at airport security gates."},
        {"word": "implied freedom", "meaning": "（憲法上の）暗黙の自由", "example": "Australian courts recognize an implied freedom of political communication."},
        {"word": "bellwether", "meaning": "先導者、指標、動向を占う試金石", "example": "The state election is considered a bellwether for the upcoming national vote."}
    ]
}

# 10. uk-making-up-china-policy-as-it-goes-along-mps (law / politics)
s10 = {
    "slug": "uk-making-up-china-policy-as-it-goes-along-mps",
    "category": "law",
    "date": "2026-11-03",
    "pub_date": "2026-11-03",
    "source_url": "https://www.theguardian.com/politics/2026/nov/02/uk-making-up-china-policy-as-it-goes-along-mps",
    "source_name": "The Guardian",
    "source_media": "The Guardian",
    "source_domain": "theguardian.com",
    "source_attribution": "The Guardian (November 2, 2026)",
    "category_label": "LAW • FOREIGN POLICY & STATUTORY SCRUTINY",
    "title": "Parliamentary Committee Condemns Ad-Hoc Foreign Policy and Lack of Statutory Framework on Strategic Trade",
    "headline_ja": "英議会委員会、対中外交政策の場当たり主義を厳しく批判：明確な法定枠組みの策定を勧告",
    "lead_ja": "英国下院の超党派外交委員会は、安全保障上の脅威と経済貿易の利益の間で政府が『場当たり的な対応』を繰り返していると批判し、先端半導体やインフラ投資に関する明確な法定基準と長期的戦略を法制化するよう求めました。",
    "subhead": "Cross-party lawmakers warn that inconsistent diplomatic directives compromise national security while confusing vital industrial investors.",
    "lead_snippet": "A scathing parliamentary report urges ministers to establish a coherent, legally grounded strategy balancing trade and security.",
    "summary_points": [
        "英議会外交特別委員会が、政府の対外政策において一貫した法的基準が欠如していると報告書で指摘。",
        "安全保障上の防衛懸念と、クリーンエネルギーやサプライチェーンにおける経済依存との間のジレンマ。",
        "閣僚の裁量頼みから、透明性の高い法定審査システム（スクリーニング法制）の整備へ移行を要求。"
    ],
    "image": "https://images.unsplash.com/photo-1526304640581-d334cdbbf45e?w=1000&auto=format&fit=crop&q=80",
    "sentences": [
        {"en": "A cross-party parliamentary committee has issued a sharply critical report accusing the UK government of conducting incoherent foreign policy without a coherent legal framework.", "ja": "超党派の議会特別委員会は、英国政府が一貫した法的枠組みを持たずに支離滅裂な外交政策を行っていると非難する痛烈な報告書を発表しました。"},
        {"en": "Lawmakers testified that vacillating diplomatic positions create acute uncertainty for domestic manufacturers and international investors in strategic technology.", "ja": "議員らは、揺れ動く外交姿勢が戦略的テクノロジー分野における国内製造業者や海外投資家に深刻な不確実性を生み出していると証言しました。"},
        {"en": "The inquiry emphasized that balancing sovereign economic interests with national security risks requires statutory clarity rather than discretionary ministerial announcements.", "ja": "調査委員会は、主権的な経済利益と国家安全保障上のリスクのバランスを取るには、閣僚の裁量による発表ではなく法定の明確性が必要であると強調しました。"},
        {"en": "Defence specialists stressed that critical supply chains, including green energy minerals and digital telecommunications, must be safeguarded under transparent legislation.", "ja": "防衛専門家らは、グリーンエネルギー鉱物やデジタル電気通信を含む重要サプライチェーンは、透明性のある法律の下で保護されなければならないと力説しました。"},
        {"en": "The committee demanded an immediate comprehensive review to enshrine robust national resilience protocols into formal statutory law.", "ja": "委員会は、強固な国家回復力プロトコルを正式な制定法として確立するため、即座の包括的見直しを要求しました。"}
    ],
    "dialogue": [
        {"speaker": "Keita先生", "name": "Keita先生", "role": "英語講師", "text": "イギリス議会の委員会が、政府の外交や貿易政策が『場当たり的でブレている』と厳しく批判したニュースだよ。"},
        {"speaker": "Nanami", "name": "Nanami", "role": "生徒・アシスタント", "text": "経済的な貿易もしたいけれど、安全保障上のリスクも心配で、方針が定まっていないんですね。"},
        {"speaker": "Keita先生", "name": "Keita先生", "role": "英語講師", "text": "その通り。大臣の気分やその場の都合で決めるのではなく、どの分野の技術を守るべきか法律で明確なルールを作るよう求めているんだ。"},
        {"speaker": "Nanami", "name": "Nanami", "role": "生徒・アシスタント", "text": "法の支配（Rule of Law）に基づいて予測可能性を高めることが、経済と国防の両立に必要なんですね。"}
    ],
    "quiz": [
        {
            "question": "What primary criticism did the parliamentary committee level against the government?",
            "options": ["Conducting inconsistent and ad-hoc foreign policy without a coherent statutory framework.", "Spending all national tax revenue exclusively on foreign military bases.", "Banning all domestic technology companies from trading with European neighbors.", "Forcing British diplomats to live permanently inside overseas embassies."],
            "answer": 0,
            "explanation": "文1に「accusing the UK government of conducting incoherent foreign policy without a coherent legal framework」とあります。"
        },
        {
            "question": "Why does a vacillating foreign policy cause problems for domestic manufacturers?",
            "options": ["It generates acute market uncertainty and complicates long-term technology investments.", "It forces factories to replace automated robotic machines with manual hand tools.", "It requires companies to pay their employees only in antique gold sovereigns.", "It prohibits private corporations from applying for registered trademarks."],
            "answer": 0,
            "explanation": "文2に「vacillating diplomatic positions create acute uncertainty for domestic manufacturers and international investors」と述べられています。"
        },
        {
            "question": "What specific remedy does the committee demand from ministers?",
            "options": ["Enshrining transparent, legally grounded security frameworks into formal statutory law.", "Allowing individual cabinet ministers to make private treaties without parliament.", "Shutting down the Foreign Office and replacing it with an artificial intelligence algorithm.", "Cancelling all national trade negotiations for the next thirty years."],
            "answer": 0,
            "explanation": "文3および文5に「requires statutory clarity rather than discretionary ministerial announcements」「enshrine robust national resilience protocols into formal statutory law」と書かれています。"
        }
    ],
    "vocab": [
        {"word": "cross-party", "meaning": "超党派の、全政党合同の", "example": "A cross-party committee examined the government's healthcare reforms."},
        {"word": "vacillating", "meaning": "動揺する、優柔不断に揺れ動く", "example": "His vacillating decisions damaged public confidence in leadership."},
        {"word": "discretionary", "meaning": "裁量による、任意の", "example": "Ministers held discretionary power over the emergency budget allocation."},
        {"word": "enshrine", "meaning": "（権利や原則を法などに）明記する、刻み込む", "example": "Fundamental civil rights were enshrined in the post-war constitution."}
    ]
}

# 11. bbc-young-musician-teenage-violinist-sofia-demetriades (culture)
s11 = {
    "slug": "bbc-young-musician-teenage-violinist-sofia-demetriades",
    "category": "culture",
    "date": "2026-11-03",
    "pub_date": "2026-11-03",
    "source_url": "https://www.theguardian.com/music/2026/nov/01/bbc-young-musician-teenage-violinist-sofia-demetriades",
    "source_name": "The Guardian",
    "source_media": "The Guardian",
    "source_domain": "theguardian.com",
    "source_attribution": "The Guardian (November 1, 2026)",
    "category_label": "CULTURE • CLASSICAL MUSIC EXCELLENCE",
    "title": "Teenage Prodigy Sofia Demetriades Wins BBC Young Musician Title with Captivating Violin Concertos",
    "headline_ja": "10代の新星ソフィア・デメトリアデスさん、圧巻のヴァイオリン演奏でBBCヤング・ミュージシャン賞を獲得",
    "lead_ja": "若手クラシック音楽家の登竜門として知られる英国BBCヤング・ミュージシャンコンクール決勝において、圧倒的な技巧と豊かな感情表現でシベリウスの協奏曲を奏でた17歳のヴァイオリニストが栄冠を手にしました。",
    "subhead": "Adjudicators praise exceptional interpretive maturity and tonal precision as the biennial showcase celebrates emerging virtuosity.",
    "lead_snippet": "A seventeen-year-old violinist has captured one of classical music's most prestigious youth honours at Symphony Hall.",
    "summary_points": [
        "数々の世界的ソリストを輩出してきた英国の名門コンクールで17歳が優勝。",
        "難曲として知られるシベリウスのヴァイオリン協奏曲を、繊細な音色と力強い集中力で見事に演奏。",
        "青少年の芸術教育への公的支援と、音楽を通じた世代を超えた対話の重要性を再認識。"
    ],
    "image": "https://images.unsplash.com/photo-1511671782779-c97d3d27a1d4?w=1000&auto=format&fit=crop&q=80",
    "sentences": [
        {"en": "Seventeen-year-old violinist Sofia Demetriades has been crowned BBC Young Musician of the Year following an electrifying grand final performance.", "ja": "17歳のヴァイオリニスト、ソフィア・デメトリアデスさんが、圧巻の決勝演奏を経てBBCヤング・ミュージシャン・オブ・ザ・イヤーの栄冠に輝きました。"},
        {"en": "Performing Sibelius's demanding Violin Concerto alongside the BBC Philharmonic Orchestra, she displayed breathtaking technical virtuosity and emotional depth.", "ja": "BBCフィルハーモニック管弦楽団とともにシベリウスの難曲ヴァイオリン協奏曲を演奏し、彼女は息をのむような超絶技巧と感情の深みを示しました。"},
        {"en": "The judging panel commended her extraordinary ability to weave lyrical tenderness with fierce dramatic intensity across complex orchestral passages.", "ja": "審査員団は、複雑な管弦楽のパッセージの中で、叙情的な優しさと激しい劇的な迫力を織り交ぜる彼女の並外れた能力を称賛しました。"},
        {"en": "Music educators highlighted that access to subsidised local youth orchestras was instrumental in nurturing her talent from an early age.", "ja": "音楽教育者らは、公的補助金を受けた地域の青少年オーケストラに参加できたことが、幼少期から彼女の才能を育てるのに不可欠だったと指摘しました。"},
        {"en": "Her triumph underscores the enduring transformative power of arts education in inspiring next-generation cultural creativity.", "ja": "彼女の勝利は、次世代の文化的な創造性を刺激する芸術教育の永続的な変革力を浮き彫りにしています。"}
    ],
    "dialogue": [
        {"speaker": "Keita先生", "name": "Keita先生", "role": "英語講師", "text": "17歳のヴァイオリニストが、イギリスの有名コンクールで優勝して世界中から大絶賛されているよ。"},
        {"speaker": "Nanami", "name": "Nanami", "role": "生徒・アシスタント", "text": "17歳でプロのオーケストラと一緒にシベリウスを完璧に弾きこなすなんて、本当にすごいですね！"},
        {"speaker": "Keita先生", "name": "Keita先生", "role": "英語講師", "text": "そうだね。本人の努力はもちろん、地域で子どもたちが音楽を学べる公的な支援プログラムがあったからこそ才能が開花したと評価されているんだ。"},
        {"speaker": "Nanami", "name": "Nanami", "role": "生徒・アシスタント", "text": "若者の才能を育てる文化的な環境づくりが、素晴らしい芸術を生み出す土台になっているんですね。"}
    ],
    "quiz": [
        {
            "question": "Which musical piece did Sofia Demetriades perform during the competition final?",
            "options": ["Sibelius's Violin Concerto.", "Beethoven's Moonlight Sonata on piano.", "Tchaikovsky's 1812 Overture on solo trumpet.", "Mozart's Requiem on a wooden flute."],
            "answer": 0,
            "explanation": "文2に「Performing Sibelius's demanding Violin Concerto alongside the BBC Philharmonic Orchestra」と書かれています。"
        },
        {
            "question": "What quality did the adjudicators particularly praise in her violin performance?",
            "options": ["Her ability to balance lyrical tenderness with dramatic musical intensity.", "Her skill in playing the violin with only one hand behind her back.", "Her decision to play modern pop songs instead of classical concertos.", "Her fast costume changes during orchestral interludes."],
            "answer": 0,
            "explanation": "文3に「ability to weave lyrical tenderness with fierce dramatic intensity across complex orchestral passages」とあります。"
        },
        {
            "question": "What factor was cited by music educators as essential to her early development?",
            "options": ["Early access to subsidized community youth orchestra programs.", "Winning a private corporate lottery at the age of five.", "Moving to live in an isolated mountain cabin without electricity.", "Practicing exclusively on electronic synthesizers instead of wooden violins."],
            "answer": 0,
            "explanation": "文4に「access to subsidised local youth orchestras was instrumental in nurturing her talent」と述べられています。"
        }
    ],
    "vocab": [
        {"word": "virtuosity", "meaning": "超絶技巧、卓越した芸術的手腕", "example": "The pianist demonstrated stunning virtuosity in the difficult cadenza."},
        {"word": "concerto", "meaning": "協奏曲（独奏楽器とオーケストラの合奏曲）", "example": "The cello concerto was warmly received by the concert hall audience."},
        {"word": "lyrical", "meaning": "叙情的な、メロディアスで情緒豊かな", "example": "The slow movement features a lyrical theme played by the oboe."},
        {"word": "instrumental", "meaning": "（目的達成に）不可欠な、役立つ（※楽器の意もある）", "example": "Her guidance was instrumental in helping the project succeed."}
    ]
}

# 12. john-lewis-christmas-advert-kristin-scott-thomas-glamorous-granny-gift-hunt (entertainment)
s12 = {
    "slug": "john-lewis-christmas-advert-kristin-scott-thomas-glamorous-granny-gift-hunt",
    "category": "entertainment",
    "date": "2026-11-03",
    "pub_date": "2026-11-03",
    "source_url": "https://www.theguardian.com/media/2026/nov/03/john-lewis-christmas-advert-kristin-scott-thomas-glamorous-granny-gift-hunt",
    "source_name": "The Guardian",
    "source_media": "The Guardian",
    "source_domain": "theguardian.com",
    "source_attribution": "The Guardian (November 3, 2026)",
    "category_label": "ENTERTAINMENT • CONSUMER CULTURE & ADVERTISING",
    "title": "Annual Festive Television Commercials Pivot Toward Multi-Generational Warmth and Humor",
    "headline_ja": "英国名物クリスマス商戦CMが解禁：多世代の家族の絆とユーモアを描く心温まる広告戦略",
    "lead_ja": "イギリスのホリデー商戦の幕開けを告げる伝統的な百貨店クリスマスCMが公開され、大御所女優を起用したスタイリッシュな祖母と孫の心温まるギフト探しを通じて、デジタル消費時代における家族の絆が描かれ話題を呼んでいます。",
    "subhead": "Department store giant unveils nostalgic winter campaign celebrating authentic familial connection over sheer commercial materialism.",
    "lead_snippet": "The much-anticipated British festive commercial season begins with cinematic storytelling focused on grandmotherly affection.",
    "summary_points": [
        "英国の年末の風物詩である大手百貨店のクリスマスCMが公開され、全国的な話題に。",
        "派手な消費喚起ではなく、祖父母と孫世代の心の通い合いや思い出の共有をテーマにした映画的演出。",
        "インフレ下における消費者の共感を呼ぶブランディング戦略として、メディア研究者からも注目。"
    ],
    "image": "https://images.unsplash.com/photo-1512389142860-9c449e58a543?w=1000&auto=format&fit=crop&q=80",
    "sentences": [
        {"en": "Britain's premier department store has launched its keenly anticipated annual Christmas commercial, signaling the unofficial beginning of the holiday shopping season.", "ja": "英国トップの百貨店が、心待ちにされていた毎冬恒例のクリスマスCMを公開し、ホリデー商戦の非公式な幕開けを告げました。"},
        {"en": "Starring celebrated actress Kristin Scott Thomas, the cinematic advertisement depicts a spirited grandmother on a whimsical mission to uncover the ideal thoughtful gift.", "ja": "著名な女優クリスティン・スコット・トーマスが出演するこの映画風の広告は、相手を思いやる理想のギフトを見つけ出す風変わりな使命に挑む元気な祖母を描いています。"},
        {"en": "Departing from high-concept computer-generated fantasy, the narrative focuses on affectionate multi-generational bonds and subtle British comedic warmth.", "ja": "高度なCGファンタジーから離れ、この物語は多世代間の愛情深い絆と控えめな英国流コメディの温かさに焦点を当てています。"},
        {"en": "Marketing analysts observed that brands are consciously pivoting toward emotional authenticity as consumers navigate persistent household budget pressures.", "ja": "マーケティングアナリストらは、消費者が長引く家計の予算圧迫に直面する中、ブランド各社が感情的な本物感へと意識的に軸足を移していると観察しました。"},
        {"en": "The commercial has quickly accumulated millions of online views, reigniting cultural conversations regarding family togetherness during the festive winter period.", "ja": "このCMは瞬く間にネット上で何百万回もの再生数を集め、冬の祝祭期における家族の団らんに関する文化的な対話を再燃させています。"}
    ],
    "dialogue": [
        {"speaker": "Keita先生", "name": "Keita先生", "role": "英語講師", "text": "イギリスの冬の風物詩であるデパートのクリスマスCMが公開されて、大きな話題になっているよ。"},
        {"speaker": "Nanami", "name": "Nanami", "role": "生徒・アシスタント", "text": "ただのCMが全国的なニュースになるなんて、イギリスらしい文化ですね！"},
        {"speaker": "Keita先生", "name": "Keita先生", "role": "英語講師", "text": "そうだね。派手にモノを買わせるのではなく、おばあちゃんと孫の温かい絆を描いていて、映画のような物語性が人々の心を打つんだ。"},
        {"speaker": "Nanami", "name": "Nanami", "role": "生徒・アシスタント", "text": "モノがあふれる時代だからこそ、家族への想いや心のつながりが一番大切だと気づかせてくれますね。"}
    ],
    "quiz": [
        {
            "question": "What is the central narrative of this year's widely discussed Christmas advert?",
            "options": ["A spirited grandmother seeking a thoughtful and meaningful gift for family.", "A team of astronauts building a retail store on the lunar surface.", "Robotic delivery drones replacing all traditional delivery workers in London.", "A magical penguin competing in an international soccer tournament."],
            "answer": 0,
            "explanation": "文2に「depicts a spirited grandmother on a whimsical mission to uncover the ideal thoughtful gift」とあります。"
        },
        {
            "question": "How does this commercial differ stylistically from previous holiday campaigns?",
            "options": ["It moves away from computer fantasy toward authentic multi-generational family warmth.", "It features only heavy techno music without any speaking characters.", "It was filmed entirely in black-and-white silent movie style.", "It advertises industrial manufacturing machinery instead of retail items."],
            "answer": 0,
            "explanation": "文3に「Departing from high-concept computer-generated fantasy, the narrative focuses on affectionate multi-generational bonds」と明記されています。"
        },
        {
            "question": "Why are retail brands prioritizing emotional authenticity in modern advertisements?",
            "options": ["Consumers are seeking genuine emotional resonance amid lingering household budget strain.", "Governments have made emotional advertising compulsory by statutory law.", "Young shoppers refuse to watch commercials that feature colorful holiday trees.", "Department stores plan to shut down all physical retail premises by next year."],
            "answer": 0,
            "explanation": "文4に「brands are consciously pivoting toward emotional authenticity as consumers navigate persistent household budget pressures」と述べられています。"
        }
    ],
    "vocab": [
        {"word": "premier", "meaning": "最高の、第一位の", "example": "The city welcomed guests to its premier concert hall."},
        {"word": "whimsical", "meaning": "風変わりな、お茶目な、ユーモアのある", "example": "The children's book was illustrated with whimsical animal drawings."},
        {"word": "pivot", "meaning": "方向転換する、方針を大きく変える", "example": "The tech firm pivoted toward artificial intelligence software."},
        {"word": "togetherness", "meaning": "団らん、一体感、親密な絆", "example": "Holidays provide a welcome opportunity for family togetherness."}
    ]
}

SENIOR_PART1 = [s1, s2, s3, s4, s5, s6]
SENIOR_PART2 = [s7, s8, s9, s10, s11, s12]

# Write Senior Part 1 & Part 2
with open("news_portal/pipeline/data_batch30_part1.py", "w", encoding="utf-8") as f:
    f.write("# -*- coding: utf-8 -*-\n")
    f.write('"""Batch 30 Part 1: Articles 1-6 (Senior) Date: 2026-11-03"""\n\n')
    f.write("SENIOR_PART1 = ")
    f.write(json.dumps(SENIOR_PART1, ensure_ascii=False, indent=4))
    f.write('\n\n__all__ = ["SENIOR_PART1"]\n')

with open("news_portal/pipeline/data_batch30_part2.py", "w", encoding="utf-8") as f:
    f.write("# -*- coding: utf-8 -*-\n")
    f.write('"""Batch 30 Part 2: Articles 7-12 (Senior) Date: 2026-11-03"""\n\n')
    f.write("SENIOR_PART2 = ")
    f.write(json.dumps(SENIOR_PART2, ensure_ascii=False, indent=4))
    f.write('\n\n__all__ = ["SENIOR_PART2"]\n')

print("Wrote Senior Part 1 and Part 2.")


# Junior Articles
# 1. starwatch-catch-the-striking-trifecta-of-venus-the-moon-and-spica-at-break-of-dawn (science)
j1 = {
    "slug": "starwatch-catch-the-striking-trifecta-of-venus-the-moon-and-spica-at-break-of-dawn",
    "category": "science",
    "date": "2026-11-03",
    "pub_date": "2026-11-03",
    "source_url": "https://www.theguardian.com/science/2026/nov/02/starwatch-catch-the-striking-trifecta-of-venus-the-moon-and-spica-at-break-of-dawn",
    "source_name": "The Guardian",
    "source_media": "The Guardian",
    "source_domain": "theguardian.com",
    "source_attribution": "The Guardian (November 2, 2026)",
    "category_label": "SCIENCE • ASTRONOMY",
    "title": "Venus, Crescent Moon and Bright Star Create Beautiful Morning Sight",
    "headline_ja": "明け方の東の空に金星・三日月・スピカが並ぶ美しい天体ショー",
    "lead_ja": "今週の夜明け前の東の空で、ひときわ明るく輝く金星、細い三日月、そして青白く光る星スピカが寄り添うように並び、早起きした人々を楽しませています。",
    "subhead": "Stargazers enjoy a rare view of three famous celestial bodies shining together in the dawn sky.",
    "lead_snippet": "Before sunrise this week, people across the northern world can see Venus, the Moon, and Spica close together.",
    "summary_points": [
        "日の出前の東の空で、金星、三日月、おとめ座のスピカが三角形を作って輝いている。",
        "隣同士に見える星たちも、実際には地球から大きく離れた宇宙の深くに位置している。",
        "天眼鏡や望遠鏡がなくても、肉眼で手軽に楽しめる秋の素晴らしい天体観測のチャンス。"
    ],
    "image": "https://images.unsplash.com/photo-1506703719100-a0f3a48c0f86?w=1000&auto=format&fit=crop&q=80",
    "sentences": [
        {"num": 1, "en": "Before sunrise this week, people looking at the eastern sky can see a lovely show of three bright objects.", "ja": "今週の日の出前、東の空を見上げた人々は、3つの明るい天体が織りなす素晴らしいショーを見ることができます。"},
        {"num": 2, "en": "Bright planet Venus, a thin crescent Moon, and the shiny star Spica appear close together in the constellation Virgo.", "ja": "明るい惑星の金星、細い三日月、そして輝く星スピカがおとめ座の中で寄り添うように見えます。"},
        {"num": 3, "en": "Even though they look very close in the morning sky, they are actually located at very different distances from Earth.", "ja": "朝の空では非常に近くに見えますが、実際には地球から全く異なる距離に位置しています。"},
        {"num": 4, "en": "Centuries ago, ancient astronomers used similar planetary meetings to learn how planets travel through space.", "ja": "何百年も前、古代の天文学者たちはこのような惑星の接近を利用して、天体が宇宙をどのように進むかを学びました。"},
        {"num": 5, "en": "Science teachers encourage students to step outside early in the morning and enjoy this natural autumn wonder.", "ja": "理科の先生たちは、早朝に外へ出てこの秋の自然の神秘を楽しむよう生徒たちに勧めています。"}
    ],
    "dialogue": [
        {"speaker": "Keita先生", "name": "Keita先生", "role": "英語講師", "text": "早朝の空で、金星と三日月、そしてスピカが並んで光っているよ。"},
        {"speaker": "Nanami", "name": "Nanami", "role": "生徒・アシスタント", "text": "望遠鏡がなくても肉眼で見られるんですか？"},
        {"speaker": "Keita先生", "name": "Keita先生", "role": "英語講師", "text": "うん！金星はとても明るいから、東の空が開けた場所ならすぐに見つけられるよ。"},
        {"speaker": "Nanami", "name": "Nanami", "role": "生徒・アシスタント", "text": "明日の朝、いつもより少し早く起きて空を見上げてみます！"}
    ],
    "quiz": [
        {
            "question": "What can people see together in the eastern sky before sunrise?",
            "options": ["Venus, the crescent Moon, and the star Spica.", "Mars, Jupiter, and a green flying comet.", "The Sun, the full Moon, and seven satellites.", "Saturn, Mercury, and the northern polar lights."],
            "answer": 0,
            "explanation": "本文第2文に「Bright planet Venus, a thin crescent Moon, and the shiny star Spica」と明記されています。"
        },
        {
            "question": "Are these three celestial objects actually close to each other in space?",
            "options": ["No, they only look close from Earth but are at very different distances.", "Yes, they are touching each other inside the Moon's clouds.", "Yes, they are all orbiting inside Earth's blue sky.", "No, they have all disappeared into black holes."],
            "answer": 0,
            "explanation": "本文第3文に「they are actually located at very different distances from Earth」と説明されています。"
        },
        {
            "question": "What do science teachers encourage students to do?",
            "options": ["Go outside early in the morning and enjoy this autumn wonder.", "Stay inside their classrooms and avoid looking at the sky.", "Buy expensive electronic space telescopes immediately.", "Travel to the South Pole to observe polar bears."],
            "answer": 0,
            "explanation": "本文第5文に「encourage students to step outside early in the morning and enjoy this natural autumn wonder」と述べられています。"
        }
    ],
    "vocab": [
        {"word": "crescent", "meaning": "三日月形の、三日月", "example": "A thin crescent Moon was visible in the twilight."},
        {"word": "constellation", "meaning": "星座", "example": "Orion is one of the easiest constellations to identify in winter."},
        {"word": "astronomer", "meaning": "天文学者", "example": "The astronomer used a large telescope to study distant galaxies."},
        {"word": "wonder", "meaning": "驚異、神秘、素晴らしいもの", "example": "The Grand Canyon is a famous natural wonder of the world."}
    ]
}

# 2. tender-bond-male-donkey-bull-baffles-scientists (science)
j2 = {
    "slug": "tender-bond-male-donkey-bull-baffles-scientists",
    "category": "science",
    "date": "2026-11-03",
    "pub_date": "2026-11-03",
    "source_url": "https://www.theguardian.com/science/2026/nov/02/tender-bond-male-donkey-bull-baffles-scientists",
    "source_name": "The Guardian",
    "source_media": "The Guardian",
    "source_domain": "theguardian.com",
    "source_attribution": "The Guardian (November 2, 2026)",
    "category_label": "SCIENCE • ANIMAL BEHAVIOUR",
    "title": "Surprising Friendship Between a Big Bull and a Donkey Amazes Scientists",
    "headline_ja": "大きな雄牛とロバの意外な友情：動物学者を驚かせる優しい絆",
    "lead_ja": "イギリスの動物保護施設で、普段は怒りっぽい大きな雄牛と年老いた小さなロバが親友のように寄り添い、互いを助け合う姿が見つかり、動物の優しい心について話題になっています。",
    "subhead": "Animal researchers study how two completely different animals formed a loving companionship.",
    "lead_snippet": "A gentle bond between an unruly bull and a calm donkey shows that animals can feel empathy across species.",
    "summary_points": [
        "気性の荒い雄牛が、おとなしい年老いたロバとだけは穏やかに寄り添って暮らしている。",
        "別の種類の動物同士でも、互いを毛づくろいして安心し合う友情が生まれることが判明。",
        "動物たちにも人間と同じように思いやりや仲間を大切にする感情があることを示す発見。"
    ],
    "image": "https://images.unsplash.com/photo-1548767797-d8c844163c4c?w=1000&auto=format&fit=crop&q=80",
    "sentences": [
        {"num": 1, "en": "At a farm sanctuary in England, animal experts are watching a wonderful friendship between a large bull and an old donkey.", "ja": "イングランドの農場保護施設で、動物の専門家たちが大きな雄牛と年老いたロバの素晴らしい友情を見守っています。"},
        {"num": 2, "en": "The bull was often angry around other cows, but he became calm and gentle whenever he stayed near the donkey.", "ja": "その雄牛は他の牛の周りではよく怒っていましたが、ロバのそばにいる時はいつも穏やかで優しくなりました。"},
        {"num": 3, "en": "The two animals eat grass side by side, clean each other's coats, and become worried if they are separated.", "ja": "2頭の動物は並んで草を食べ、互いの毛をきれいにし、引き離されると心配そうにします。"},
        {"num": 4, "en": "Scientists say this shows that animals can form deep friendships even when they belong to totally different species.", "ja": "科学者らは、このことは動物が全く異なる種に属していても深い友情を結べることを示していると述べています。"},
        {"num": 5, "en": "This touching story helps people understand that animals have feelings and deserve our kind protection.", "ja": "この心温まる物語は、動物にも感情があり、私たちの優しい保護を受ける価値があることを人々が理解する助けになります。"}
    ],
    "dialogue": [
        {"speaker": "Keita先生", "name": "Keita先生", "role": "英語講師", "text": "怒りっぽかった雄牛が、おじいさんロバと仲良くなって穏やかになったんだよ。"},
        {"speaker": "Nanami", "name": "Nanami", "role": "生徒・アシスタント", "text": "牛とロバが親友になるなんて、まるで絵本のようなお話ですね！"},
        {"speaker": "Keita先生", "name": "Keita先生", "role": "英語講師", "text": "そうだね。互いに寄り添うことで安心できるんだ。動物にも優しい心や思いやりがあるんだね。"},
        {"speaker": "Nanami", "name": "Nanami", "role": "生徒・アシスタント", "text": "種類が違っても仲良くなれる姿に、人間も学ぶことがたくさんありますね！"}
    ],
    "quiz": [
        {
            "question": "How did the big bull change when he was near the donkey?",
            "options": ["He became calm and gentle instead of angry.", "He learned how to climb tall wooden farm fences.", "He started running away from the green pasture.", "He began barking loudly like a guard dog."],
            "answer": 0,
            "explanation": "本文第2文に「he became calm and gentle whenever he stayed near the donkey」と書かれています。"
        },
        {
            "question": "What do the bull and the donkey do together every day?",
            "options": ["They eat grass together, groom each other, and stay close.", "They pull heavy tourist carriages through city streets.", "They swim across cold rivers to find fresh hay.", "They hide inside underground tunnels during the day."],
            "answer": 0,
            "explanation": "本文第3文に「eat grass side by side, clean each other's coats, and become worried if they are separated」とあります。"
        },
        {
            "question": "What does this friendship teach people about animals?",
            "options": ["Animals have feelings and can make friends across different species.", "Large bulls should never be kept in grassy pastures.", "Donkeys prefer living alone in dry desert regions.", "Farm animals cannot feel sadness when separated from friends."],
            "answer": 0,
            "explanation": "本文第4文および第5文に「animals can form deep friendships even when they belong to totally different species」「animals have feelings」と述べられています。"
        }
    ],
    "vocab": [
        {"word": "sanctuary", "meaning": "保護施設、自然保護区", "example": "The injured birds were cared for at a wildlife sanctuary."},
        {"word": "gentle", "meaning": "優しい、穏やかな", "example": "She has a very gentle voice when speaking to children."},
        {"word": "species", "meaning": "（生物の）種", "example": "Lions and tigers are two different species of big cats."},
        {"word": "touching", "meaning": "感動的な、心温まる", "example": "It was a touching story about a loyal rescue dog."}
    ]
}

# 3. polar-vortex-disruption-colder-weather-europe (environment)
j3 = {
    "slug": "polar-vortex-disruption-colder-weather-europe",
    "category": "environment",
    "date": "2026-11-03",
    "pub_date": "2026-11-03",
    "source_url": "https://www.theguardian.com/environment/2026/nov/02/polar-vortex-disruption-colder-weather-europe",
    "source_name": "The Guardian",
    "source_media": "The Guardian",
    "source_domain": "theguardian.com",
    "source_attribution": "The Guardian (November 2, 2026)",
    "category_label": "ENVIRONMENT • CLIMATE DYNAMICS",
    "title": "Arctic Cold Winds Bring Early Winter Chill to Many European Towns",
    "headline_ja": "北極からの冷たい風が欧州各地に早くも冬の寒さをもたらす",
    "lead_ja": "北極上空の冷たい空気の渦が崩れたことにより、凍てつくような寒気が南のヨーロッパへ流れ込み、例年より早く厳しい冷え込みが訪れると警告されています。",
    "subhead": "Changes in high-altitude polar winds allow freezing arctic air to travel down across Europe.",
    "lead_snippet": "A sudden shift in northern atmospheric winds could bring freezing temperatures to several European nations this week.",
    "summary_points": [
        "北極上空で冷気を閉じ込めていた強風の壁が崩れ、寒気が南下している。",
        "ヨーロッパ各地で11月前半としては異例の氷点下の冷え込みが予想される。",
        "暖房用の電気やガスの需要が急増するため、エネルギーの節約と備えが呼びかけられている。"
    ],
    "image": "https://images.unsplash.com/photo-1483921020237-2ff51e8e4b22?w=1000&auto=format&fit=crop&q=80",
    "sentences": [
        {"num": 1, "en": "Weather forecasters in Europe are warning people to prepare for an early blast of freezing winter cold.", "ja": "ヨーロッパの気象予報士らは、例年より早い厳しい冬の寒波に備えるよう人々に警告しています。"},
        {"num": 2, "en": "Normally, strong winds high above the North Pole act like a spinning wall to keep freezing air trapped in the Arctic.", "ja": "通常、北極のはるか上空にある強風が回転する壁のように働き、極寒の空気を北極圏に閉じ込めています。"},
        {"num": 3, "en": "Recently, warm temperatures in the upper sky weakened these winds, allowing ice-cold air to slide south into European countries.", "ja": "最近、上空の気温上昇がこれらの風を弱め、氷のように冷たい空気が南のヨーロッパ諸国へと滑り込むことを許してしまいました。"},
        {"num": 4, "en": "Scientists believe that melting sea ice caused by global climate change might be making these cold wind shifts happen more often.", "ja": "科学者らは、地球規模の気候変動による海氷の減少が、このような寒気の移動をより頻繁に引き起こしている可能性があると考えています。"},
        {"num": 5, "en": "Cities are opening warm community centres to help elderly residents stay safe and warm during the chilly nights.", "ja": "各都市は、寒い夜の間、高齢の住民が安全に暖かく過ごせるよう、温かい地域センターを開放しています。"}
    ],
    "dialogue": [
        {"speaker": "Keita先生", "name": "Keita先生", "role": "英語講師", "text": "北極の寒気を閉じ込めていた風の渦が崩れて、ヨーロッパに早い寒波が来るんだよ。"},
        {"speaker": "Nanami", "name": "Nanami", "role": "生徒・アシスタント", "text": "地球が温暖化しているのに、冬にすごく寒くなることがあるのはどうしてですか？"},
        {"speaker": "Keita先生", "name": "Keita先生", "role": "英語講師", "text": "北極の氷が溶けると気流のバランスが崩れて、北極の冷たい空気が南に漏れ出しやすくなるからなんだ。"},
        {"speaker": "Nanami", "name": "Nanami", "role": "生徒・アシスタント", "text": "温暖化が寒暖差を極端にしているんですね。お年寄りの暖房支援などもしっかり必要ですね！"}
    ],
    "quiz": [
        {
            "question": "What normally keeps freezing air trapped around the North Pole?",
            "options": ["Strong spinning winds high above the Arctic.", "A ring of tall brick chimneys built on icebergs.", "Warm steam coming from passenger aeroplanes.", "Enormous metal fans blowing air into the sky."],
            "answer": 0,
            "explanation": "本文第2文に「strong winds high above the North Pole act like a spinning wall to keep freezing air trapped」とあります。"
        },
        {
            "question": "Why did the ice-cold air move south into Europe?",
            "options": ["Warm temperatures in the upper sky weakened the polar winds.", "All European mountains were flattened by construction workers.", "The sun stopped shining over Europe completely.", "The North Pole moved closer to the equator."],
            "answer": 0,
            "explanation": "本文第3文に「warm temperatures in the upper sky weakened these winds, allowing ice-cold air to slide south」と書かれています。"
        },
        {
            "question": "What are European cities doing to protect elderly citizens from the freeze?",
            "options": ["Opening warm community centres where they can stay comfortable.", "Giving everyone free train tickets to South America.", "Asking them to turn off their indoor heaters during the night.", "Painting all private house roofs bright green."],
            "answer": 0,
            "explanation": "本文第5文に「opening warm community centres to help elderly residents stay safe and warm」と述べられています。"
        }
    ],
    "vocab": [
        {"word": "forecaster", "meaning": "（天気などの）予報士", "example": "The weather forecaster predicted heavy snow for tomorrow morning."},
        {"word": "chilly", "meaning": "肌寒い、ひんやりとした", "example": "It is quite chilly outside, so please take a warm jacket."},
        {"word": "trap", "meaning": "〜を閉じ込める、捕らえる", "example": "Greenhouse gases trap heat inside Earth's atmosphere."},
        {"word": "elderly", "meaning": "高齢の、年配の", "example": "Volunteers helped elderly neighbours clear snow from driveways."}
    ]
}

# 4. british-gas-resume-force-fitting-prepayment-meters-months-after-112m-settlement (environment / energy)
j4 = {
    "slug": "british-gas-resume-force-fitting-prepayment-meters-months-after-112m-settlement",
    "category": "environment",
    "date": "2026-11-03",
    "pub_date": "2026-11-03",
    "source_url": "https://www.theguardian.com/money/2026/nov/02/british-gas-resume-force-fitting-prepayment-meters-months-after-112m-settlement",
    "source_name": "The Guardian",
    "source_media": "The Guardian",
    "source_domain": "theguardian.com",
    "source_attribution": "The Guardian (November 2, 2026)",
    "category_label": "ENVIRONMENT • ENERGY POVERTY",
    "title": "UK Energy Company Criticized for Forcing Pay-As-You-Go Meters on Poor Homes",
    "headline_ja": "光熱費滞納家庭への前払いメーター強制設置再開に批判の声",
    "lead_ja": "イギリスの大手エネルギー会社が、ガス代や電気代を払えない家庭に対して、事前にお金を入れないと止まる『前払いメーター』の強制取り付けを再開すると発表し、生活支援団体から心配の声が上がっています。",
    "subhead": "Charities warn that vulnerable families could be left without heat during cold winter months.",
    "lead_snippet": "A major supplier plans to resume installing prepayment meters for customers who struggle to pay energy debts.",
    "summary_points": [
        "料金の支払いが遅れた家庭に、事前チャージ式のメーターを強制的に取り付ける動きが再開。",
        "お金がなくなると即座に電気や暖房が止まるため、病気の人や赤ちゃんのいる家庭が危険にさらされる。",
        "企業の売上回収と、生活に困っている人たちの健康と命を守るルールのあり方が議論されている。"
    ],
    "image": "https://images.unsplash.com/photo-1473341304170-971dccb5ac1e?w=1000&auto=format&fit=crop&q=80",
    "sentences": [
        {"num": 1, "en": "A major energy supplier in Britain is facing public anger for planning to force prepayment meters on families who owe money.", "ja": "英国の大手エネルギー供給会社が、料金滞納のある家庭に前払いメーターを強制設置する計画について公衆の怒りに直面しています。"},
        {"num": 2, "en": "With prepayment meters, customers must pay in advance using cards or keys, and heat stops immediately when the money runs out.", "ja": "前払いメーターでは、利用者はカードや鍵を使って事前にお金を支払わねばならず、お金が尽きると暖房は直ちに止まります。"},
        {"num": 3, "en": "Charity groups warn that poor households and sick children could be left in freezing cold rooms this winter.", "ja": "慈善団体は、今冬、貧しい世帯や病気の子どもたちが凍えるように寒い部屋に取り残される恐れがあると警告しています。"},
        {"num": 4, "en": "The energy company argues that huge unpaid bills make it harder to keep prices fair for customers who pay on time.", "ja": "そのエネルギー会社は、巨額の未払い請求書があることで期日通りに支払っている利用者に公正な価格を保つのが難しくなると主張しています。"},
        {"num": 5, "en": "Government officials are checking the rules to ensure that families with serious health problems receive extra protection.", "ja": "政府関係者は、深刻な健康問題を抱える家庭が特別な保護を受けられるよう規則を確認しています。"}
    ],
    "dialogue": [
        {"speaker": "Keita先生", "name": "Keita先生", "role": "英語講師", "text": "ガス代が払えない家庭に、チャージしないと止まる前払いメーターを強制的に取り付ける問題だよ。"},
        {"speaker": "Nanami", "name": "Nanami", "role": "生徒・アシスタント", "text": "冬にお金がなくて暖房が止まったら、病気になったりして命に関わりますよね…。"},
        {"speaker": "Keita先生", "name": "Keita先生", "role": "英語講師", "text": "そうだね。会社のお金回収のルールよりも、まず人の命や暖をとる権利を守るべきだという批判が高まっているんだ。"},
        {"speaker": "Nanami", "name": "Nanami", "role": "生徒・アシスタント", "text": "誰にとっても欠かせないライフラインだからこそ、困っている人を守る仕組みが必要ですね。"}
    ],
    "quiz": [
        {
            "question": "What happens when money runs out on a prepayment energy meter?",
            "options": ["Heat and electricity stop immediately until more money is added.", "The energy company automatically sends free chocolate bars.", "The meter plays cheerful music for twenty-four hours.", "The government pays all remaining household utility bills."],
            "answer": 0,
            "explanation": "本文第2文に「heat stops immediately when the money runs out」と明記されています。"
        },
        {
            "question": "Why are charity groups worried about this installation practice in winter?",
            "options": ["Vulnerable families and sick children might be left in freezing cold homes.", "Residents will not be able to watch winter football matches on television.", "Old houses will become too warm and uncomfortable for sleeping.", "People will buy too many blankets from local department stores."],
            "answer": 0,
            "explanation": "本文第3文に「poor households and sick children could be left in freezing cold rooms this winter」と書かれています。"
        },
        {
            "question": "What are government officials checking regarding energy rules?",
            "options": ["Making sure families with serious health needs are properly protected.", "Checking that all meters are painted bright purple before winter.", "Ordering every citizen to cook food only on campfire wood.", "Making gas bills three times more expensive for students."],
            "answer": 0,
            "explanation": "本文第5文に「ensure that families with serious health problems receive extra protection」と述べられています。"
        }
    ],
    "vocab": [
        {"word": "in advance", "meaning": "前もって、事前に", "example": "Please book your concert tickets well in advance."},
        {"word": "owe", "meaning": "（お金を）借りている、滞納している", "example": "He owes fifty pounds to the local bookstore."},
        {"word": "charity", "meaning": "慈善団体、思いやり", "example": "She volunteers every Saturday at an animal charity."},
        {"word": "household", "meaning": "世帯、家庭", "example": "Average household energy consumption drops during summer months."}
    ]
}

# 5. nhs-early-warning-system-child-illness-england (society)
j5 = {
    "slug": "nhs-early-warning-system-child-illness-england",
    "category": "society",
    "date": "2026-11-03",
    "pub_date": "2026-11-03",
    "source_url": "https://www.theguardian.com/society/2026/nov/02/nhs-early-warning-system-child-illness-england",
    "source_name": "The Guardian",
    "source_media": "The Guardian",
    "source_domain": "theguardian.com",
    "source_attribution": "The Guardian (November 2, 2026)",
    "category_label": "SOCIETY • HEALTHCARE REFORM",
    "title": "English Hospitals Use Parents' Intuition to Catch Child Illness Early",
    "headline_ja": "イングランドの病院、子どもの急病を早期発見するため『親の直感』を医療データに導入",
    "lead_ja": "イギリスの病院で、子どもの容態が急に悪化するのを防ぐため、体温や心拍数だけでなく『親が感じる違和感や心配』を正式な診断基準にする新しい仕組みが始まりました。",
    "subhead": "A new hospital system helps doctors and parents work together to save young lives from severe infections.",
    "lead_snippet": "Doctors across England are using a nationwide scoring alert system that listens carefully to parents' concerns.",
    "summary_points": [
        "子どもの容態急変を見逃さないため、全国統一の小児早期警戒システムがスタート。",
        "機械の測定値だけでなく、『いつもと様子が違う』という親の不安の声を正式スコアに記録。",
        "医師と家族が協力して治療にあたることで、防ぐことができる子どもの重症化を防ぐ。"
    ],
    "image": "https://images.unsplash.com/photo-1579684385127-1ef15d508118?w=1000&auto=format&fit=crop&q=80",
    "sentences": [
        {"num": 1, "en": "Hospitals across England have introduced a new system to detect serious illnesses in sick children much faster.", "ja": "イングランド全土の病院は、病気の子どもの深刻な疾患をはるかに素早く発見するための新しいシステムを導入しました。"},
        {"num": 2, "en": "Nurses now measure breathing and heart rates while also asking parents whether their child seems different from normal.", "ja": "看護師たちは現在、呼吸や心拍数を測るとともに、子どもがいつもと違って見えないかを親たちに尋ねています。"},
        {"num": 3, "en": "Studies showed that parents often notice tiny changes in energy or behavior hours before machines show danger.", "ja": "研究によると、機械が危険を示す何時間も前に、親たちは元気や行動のわずかな変化に気づくことが多いことが分かりました。"},
        {"num": 4, "en": "Doctors say listening to family members creates a strong partnership that improves hospital safety for every child.", "ja": "医師らは、家族の声に耳を傾けることで、すべての子どもに対する病院の安全性を高める強い協力関係が生まれると述べています。"},
        {"num": 5, "en": "Health experts hope this simple communication checklist will save dozens of young lives every year.", "ja": "医療の専門家らは、この簡単な対話チェックリストが毎年何十人もの幼い命を救うことを願っています。"}
    ],
    "dialogue": [
        {"speaker": "Keita先生", "name": "Keita先生", "role": "英語講師", "text": "病院で子どもの治療をするとき、機械の数値だけでなく『親の直感』をデータとして取り入れるシステムだよ。"},
        {"speaker": "Nanami", "name": "Nanami", "role": "生徒・アシスタント", "text": "毎日一緒にいるお母さんやお父さんだからこそ、ちょっとした元気のなさにも気づけますもんね！"},
        {"speaker": "Keita先生", "name": "Keita先生", "role": "英語講師", "text": "その通り。お医者さん任せにするのではなく、家族の気付きをチーム医療に組み込むことで助かる命が増えるんだ。"},
        {"speaker": "Nanami", "name": "Nanami", "role": "生徒・アシスタント", "text": "患者さんの家族を大切にする温かい医療改革ですね！"}
    ],
    "quiz": [
        {
            "question": "What is unique about the new hospital child safety system in England?",
            "options": ["It officially records and values parents' feelings and concerns alongside medical tests.", "It allows children to eat ice cream instead of taking prescription medicine.", "It trains robotic nurses to replace human doctors completely.", "It asks patients to solve math problems before seeing a pediatrician."],
            "answer": 0,
            "explanation": "本文第2文に「asking parents whether their child seems different from normal」と書かれています。"
        },
        {
            "question": "What did research studies reveal about parents of sick children?",
            "options": ["They frequently notice tiny changes in behavior hours before medical machines detect danger.", "They prefer leaving hospitals immediately without speaking to any doctors.", "They never pay attention to their child's energy levels.", "They cannot understand simple thermometer readings."],
            "answer": 0,
            "explanation": "本文第3文に「parents often notice tiny changes in energy or behavior hours before machines show danger」とあります。"
        },
        {
            "question": "What do medical experts hope this new system will achieve?",
            "options": ["Save dozens of young children's lives every year across England.", "Close down all pediatric hospital departments in northern cities.", "Make hospital stays twice as expensive for ordinary families.", "Prevent parents from visiting their children in hospital rooms."],
            "answer": 0,
            "explanation": "本文第5文に「save dozens of young lives every year」と述べられています。"
        }
    ],
    "vocab": [
        {"word": "detect", "meaning": "〜を発見する、感知する", "example": "Smoke alarms are designed to detect fire early."},
        {"word": "normal", "meaning": "普通の、通常の", "example": "Her body temperature returned to normal after three days."},
        {"word": "partnership", "meaning": "協力関係、パートナーシップ", "example": "Effective learning requires a strong partnership between teachers and students."},
        {"word": "checklist", "meaning": "点検表、チェックリスト", "example": "Pilots review a safety checklist before every flight."}
    ]
}

# 6. counsellors-psychotherapists-statutory-regulation-uk-professional-bodies (society)
j6 = {
    "slug": "counsellors-psychotherapists-statutory-regulation-uk-professional-bodies",
    "category": "society",
    "date": "2026-11-03",
    "pub_date": "2026-11-03",
    "source_url": "https://www.theguardian.com/society/2026/nov/02/counsellors-psychotherapists-statutory-regulation-uk-professional-bodies",
    "source_name": "The Guardian",
    "source_media": "The Guardian",
    "source_domain": "theguardian.com",
    "source_attribution": "The Guardian (November 2, 2026)",
    "category_label": "SOCIETY • MENTAL HEALTH LAW",
    "title": "Calls in Britain to Make Counsellors and Therapists Hold Official Government Licences",
    "headline_ja": "心の悩みを聴くカウンセラーに国家資格を：患者の安全を守る新ルールを求める声",
    "lead_ja": "イギリスでは現在、誰でも試験や資格なしに『カウンセラー』を名乗れてしまうため、十分な訓練を受けていない人による不適切な治療から患者を守るため、公的な免許制度を作るよう求める運動が起きています。",
    "subhead": "Mental health groups urge lawmakers to protect vulnerable patients from unqualified therapists.",
    "lead_snippet": "Campaigners say anyone can currently call themselves a psychotherapist in the UK without proper training.",
    "summary_points": [
        "英国では『カウンセラー』の肩書が法律で守られておらず、誰でも開業できる抜け穴がある。",
        "短時間の講習を受けただけの人が心の治療を行い、患者が余計につらい思いをするケースが問題視。",
        "医師や看護師のように、正式な国家資格と厳しい倫理基準を設けるよう求める声が高まっている。"
    ],
    "image": "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=1000&auto=format&fit=crop&q=80",
    "sentences": [
        {"num": 1, "en": "Mental health charities in the UK are asking the government to create official licences for all therapy counsellors.", "ja": "英国のメンタルヘルス慈善団体は、すべての心理カウンセラーに公的な免許を設けるよう政府に求めています。"},
        {"num": 2, "en": "Under current laws, anyone can advertise themselves as a therapist or counsellor without proving their qualifications.", "ja": "現行法の下では、誰でも自分の資格を証明することなくセラピストやカウンセラーとして広告を出すことができます。"},
        {"num": 3, "en": "Some patients suffered more emotional pain after receiving bad advice from people with only a few hours of online training.", "ja": "数時間のオンライン研修しか受けていない人から不適切な助言を受け、より多くの心の痛みに苦しんだ患者もいます。"},
        {"num": 4, "en": "Professional psychologists say official laws would ensure that every therapist follows strict safety and privacy rules.", "ja": "専門の心理学者らは、公的な法律によってすべてのセラピストが厳格な安全およびプライバシーの規則を守るようになると述べています。"},
        {"num": 5, "en": "Ministers promised to review the system so people seeking emotional help can feel completely confident and safe.", "ja": "閣僚らは、心の助けを求める人々が完全に安心で安全だと感じられるよう、制度を見直すことを約束しました。"}
    ],
    "dialogue": [
        {"speaker": "Keita先生", "name": "Keita先生", "role": "英語講師", "text": "イギリスで、カウンセラーを名乗る人たちに公的な国家資格を義務付けようという動きがあるよ。"},
        {"speaker": "Nanami", "name": "Nanami", "role": "生徒・アシスタント", "text": "今まで資格がなくてもカウンセラーを名乗れたなんて驚きです！"},
        {"speaker": "Keita先生", "name": "Keita先生", "role": "英語講師", "text": "そうなんだ。心療の専門知識がない人が適当なアドバイスをして症状が悪化するのを防ぐために、免許が必要だと訴えているんだよ。"},
        {"speaker": "Nanami", "name": "Nanami", "role": "生徒・アシスタント", "text": "体の病気を治すお医者さんと同じように、心の病をケアする人にもしっかりとした資格が必要ですね！"}
    ],
    "quiz": [
        {
            "question": "What problem exists under current UK laws regarding counsellors?",
            "options": ["Anyone can call themselves a therapist without proving their official qualifications.", "All therapists must work in royal hospitals without receiving pay.", "Therapists are only allowed to speak to patients using text messages.", "Only people over eighty years old can become professional psychologists."],
            "answer": 0,
            "explanation": "本文第2文に「anyone can advertise themselves as a therapist or counsellor without proving their qualifications」とあります。"
        },
        {
            "question": "What bad outcome happened to some patients who visited unqualified practitioners?",
            "options": ["They suffered more emotional pain due to poor advice from untrained people.", "They were forced to buy expensive wooden musical instruments.", "They had to take five school examinations on the same day.", "Their private personal smartphones were taken away by the police."],
            "answer": 0,
            "explanation": "本文第3文に「suffered more emotional pain after receiving bad advice from people with only a few hours of online training」と書かれています。"
        },
        {
            "question": "Why do professional psychologists support creating official laws?",
            "options": ["To ensure every therapist follows strict safety, training, and privacy standards.", "To ban people from seeking help for mental health challenges.", "To close down all psychological research departments in universities.", "To force counsellors to work only during night hours."],
            "answer": 0,
            "explanation": "本文第4文に「ensure that every therapist follows strict safety and privacy rules」と述べられています。"
        }
    ],
    "vocab": [
        {"word": "qualification", "meaning": "資格、免許、能力", "example": "She has all the necessary qualifications to teach English."},
        {"word": "advertise", "meaning": "〜を広告・宣伝する", "example": "The company advertised its new smartphone on public billboards."},
        {"word": "emotional", "meaning": "感情の、精神的な", "example": "Good friends provide strong emotional support during difficult times."},
        {"word": "confident", "meaning": "確信して、自信がある、安心している", "example": "He felt confident that he would pass the final exam."}
    ]
}

JUNIOR_PART1 = [j1, j2, j3, j4, j5, j6]

with open("news_portal/pipeline/data_batch30_junior_part1.py", "w", encoding="utf-8") as f:
    f.write("# -*- coding: utf-8 -*-\n")
    f.write('"""Batch 30 Part 1: Articles 1-6 (Junior) Date: 2026-11-03"""\n\n')
    f.write("JUNIOR_PART1 = ")
    f.write(json.dumps(JUNIOR_PART1, ensure_ascii=False, indent=4))
    f.write('\n\n__all__ = ["JUNIOR_PART1"]\n')

print("Wrote Junior Part 1.")


# Junior Articles Part 2 (7-12)
# 7. nine-of-world-biggest-oil-firms-95bn-profit-third-quarter-iran-war (world)
j7 = {
    "slug": "nine-of-world-biggest-oil-firms-95bn-profit-third-quarter-iran-war",
    "category": "world",
    "date": "2026-11-03",
    "pub_date": "2026-11-03",
    "source_url": "https://www.theguardian.com/business/2026/nov/02/nine-of-world-biggest-oil-firms-95bn-profit-third-quarter-iran-war",
    "source_name": "The Guardian",
    "source_media": "The Guardian",
    "source_domain": "theguardian.com",
    "source_attribution": "The Guardian (November 2, 2026)",
    "category_label": "WORLD • ENERGY GEOPOLITICS",
    "title": "Major Oil Companies Make Huge $95 Billion Profits as Energy Prices Rise",
    "headline_ja": "エネルギー価格の高騰で大手石油9社が950億ドルの巨額利益を記録",
    "lead_ja": "中東での争いにより原油価格が値上がりした結果、世界の大手石油会社9社が3か月間で約15兆円もの記録的な利益を上げたため、困窮する市民への支援に使うべきだという議論が起きています。",
    "subhead": "Big profits for oil giants spark debate as ordinary households struggle with high living expenses.",
    "lead_snippet": "Nine global oil corporations earned ninety-five billion dollars following sharp spikes in worldwide oil prices.",
    "summary_points": [
        "国際情勢の緊迫化で原油の値段が上がり、大手石油会社が莫大な利益を上げた。",
        "一般の家庭がガソリンや電気代の高さに苦しむ中で、企業だけが大儲けしていると批判。",
        "得られた余剰利益に特別な税金をかけ、クリーンエネルギー開発や生活支援に回す案が出ている。"
    ],
    "image": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=1000&auto=format&fit=crop&q=80",
    "sentences": [
        {"num": 1, "en": "Nine of the biggest oil corporations in the world earned ninety-five billion dollars in profits over the past three months.", "ja": "世界最大手クラスの石油企業9社が、過去3か月間で950億ドルの利益を上げました。"},
        {"num": 2, "en": "Tensions and conflicts in the Middle East caused international oil and fuel prices to jump significantly.", "ja": "中東における緊張や紛争により、国際的な石油や燃料の価格が著しく跳ね上がりました。"},
        {"num": 3, "en": "While company shareholders celebrated, charities pointed out that ordinary families are struggling to afford heating bills.", "ja": "企業の株主たちが喜んだ一方で、慈善団体は一般の家庭が暖房費の支払いに苦しんでいると指摘しました。"},
        {"num": 4, "en": "Some politicians in Europe want governments to place special taxes on these unexpected profits to help poor communities.", "ja": "ヨーロッパの一部の政治家は、貧しいコミュニティを助けるため、これらの予想外の利益に特別な税金を課すことを政府に求めています。"},
        {"num": 5, "en": "Campaigners say using this money to build solar and wind power will lower bills and protect the environment.", "ja": "活動家らは、この資金を使って太陽光や風力発電を建設することが光熱費を下げ環境を守ることにつながると述べています。"}
    ],
    "dialogue": [
        {"speaker": "Keita先生", "name": "Keita先生", "role": "英語講師", "text": "石油会社9社が3か月で約15兆円もの利益を出して、公平さについての議論が起きているよ。"},
        {"speaker": "Nanami", "name": "Nanami", "role": "生徒・アシスタント", "text": "ガソリン代が高くてみんな困っているのに、会社だけがそんなに儲かるのは不公平に感じますね。"},
        {"speaker": "Keita先生", "name": "Keita先生", "role": "英語講師", "text": "そうだね。だから特別に税金をかけて、電気代の補助や太陽光発電の整備に使うべきだという提案が出ているんだ。"},
        {"speaker": "Nanami", "name": "Nanami", "role": "生徒・アシスタント", "text": "社会全体のバランスと、将来のクリーンエネルギーのための知恵が問われているんですね。"}
    ],
    "quiz": [
        {
            "question": "Why did major oil companies make ninety-five billion dollars in profits?",
            "options": ["Tensions in the Middle East caused global crude oil prices to rise sharply.", "They started selling electric cars to school children.", "They closed all their oil wells and became farming businesses.", "All taxes on petrol were completely eliminated worldwide."],
            "answer": 0,
            "explanation": "本文第2文に「Tensions and conflicts in the Middle East caused international oil and fuel prices to jump significantly」と書かれています。"
        },
        {
            "question": "What concern did charity groups raise about ordinary families?",
            "options": ["Ordinary households are struggling to pay for expensive heating and living costs.", "Families have too much money and do not know how to spend it.", "Children are refusing to go to school because the weather is too warm.", "People are driving too many sports cars on highways."],
            "answer": 0,
            "explanation": "本文第3文に「ordinary families are struggling to afford heating bills」とあります。"
        },
        {
            "question": "How do campaigners suggest using the extra tax money collected from oil profits?",
            "options": ["Building renewable solar and wind energy to lower bills and protect the planet.", "Giving free luxury holidays to oil company executives.", "Buying thousands of diesel generators for city offices.", "Moving all coastal towns to the tops of high mountains."],
            "answer": 0,
            "explanation": "本文第5文に「using this money to build solar and wind power will lower bills and protect the environment」と述べられています。"
        }
    ],
    "vocab": [
        {"word": "profit", "meaning": "利益、もうけ", "example": "The company reported a healthy profit at the end of the year."},
        {"word": "afford", "meaning": "〜を買う（支払う）余裕がある", "example": "We cannot afford to buy a new car right now."},
        {"word": "unexpected", "meaning": "予期しない、思いがけない", "example": "The sudden rain was an unexpected surprise on our picnic."},
        {"word": "renewable", "meaning": "再生可能な（エネルギーなど）", "example": "Solar and wind are key forms of renewable energy."}
    ]
}

# 8. hackers-fake-nuclear-chemical-threat-alert-kyiv-ukraine-emergency-app (world)
j8 = {
    "slug": "hackers-fake-nuclear-chemical-threat-alert-kyiv-ukraine-emergency-app",
    "category": "world",
    "date": "2026-11-03",
    "pub_date": "2026-11-03",
    "source_url": "https://www.theguardian.com/world/2026/nov/02/hackers-fake-nuclear-chemical-threat-alert-kyiv-ukraine-emergency-app",
    "source_name": "The Guardian",
    "source_media": "The Guardian",
    "source_domain": "theguardian.com",
    "source_attribution": "The Guardian (November 2, 2026)",
    "category_label": "WORLD • HYBRID CYBERWARFARE",
    "title": "Hackers Send False Chemical Attack Alert Through Kyiv Emergency Phone App",
    "headline_ja": "ウクライナの避難警報アプリがハッキングされ、偽の危険通知が送信される",
    "lead_ja": "ウクライナの首都キーウで、市民が避難のために使っている公式アプリがサイバー攻撃を受け、偽の化学兵器警報がスマートフォンに送られて一時的なパニックを引き起こしました。",
    "subhead": "Cyber experts quickly stop a dangerous fake alert sent to millions of mobile phone users.",
    "lead_snippet": "A malicious intrusion into an official civil defence application caused temporary fear across the city of Kyiv.",
    "summary_points": [
        "市民が命を守るために登録している公式警報アプリが不正アクセスを受けた。",
        "化学物質による攻撃があるという嘘のメッセージが送られ、社会を不安に陥れた。",
        "専門家が数分で遮断したが、緊急アプリの暗号化と安全性の強化が急がれている。"
    ],
    "image": "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=1000&auto=format&fit=crop&q=80",
    "sentences": [
        {"num": 1, "en": "Cyber attackers broke into an official emergency alert application used by millions of people in Ukraine's capital city.", "ja": "サイバー攻撃者が、ウクライナの首都で何百万人もの人々が利用している公式緊急警報アプリに侵入しました。"},
        {"num": 2, "en": "The hackers sent out scary false notifications claiming that a dangerous chemical attack was happening right away.", "ja": "ハッカーたちは、危険な化学攻撃が今すぐ起きていると主張する恐ろしい虚偽の通知を送り出しました。"},
        {"num": 3, "en": "Security teams acted within minutes to stop the unauthorized access and tell citizens that the message was a fake.", "ja": "セキュリティチームは数分以内に対処して不正アクセスを止め、市民にそのメッセージは偽物であると伝えました。"},
        {"num": 4, "en": "Military experts said this cyber-attack was meant to cause public fear and make people distrust official civil announcements.", "ja": "軍事専門家らは、このサイバー攻撃は人々に恐怖を与え、公式の民間発表を信用できなくさせることを目的としたものだと述べました。"},
        {"num": 5, "en": "Engineers are now adding stronger security codes to ensure that emergency broadcast messages can never be changed by criminals.", "ja": "技術者らは現在、緊急配信メッセージが犯罪者によって改ざんされることが決してないよう、より強力なセキュリティ暗号を追加しています。"}
    ],
    "dialogue": [
        {"speaker": "Keita先生", "name": "Keita先生", "role": "英語講師", "text": "市民が避難するためにスマホに入れている防災アプリがハッキングされたニュースだよ。"},
        {"speaker": "Nanami", "name": "Nanami", "role": "生徒・アシスタント", "text": "本物のアプリから『危険な攻撃が起きた』と通知が来たら、信じてパニックになってしまいますね。"},
        {"speaker": "Keita先生", "name": "Keita先生", "role": "英語講師", "text": "そうなんだ。実際の武力だけでなく、偽情報で人々を不安にさせるサイバー攻撃の怖さを示しているね。"},
        {"speaker": "Nanami", "name": "Nanami", "role": "生徒・アシスタント", "text": "防災アプリの安全を守るセキュリティ技術が、市民の命を守るために本当に大切ですね。"}
    ],
    "quiz": [
        {
            "question": "What false message did hackers send using the mobile emergency app?",
            "options": ["A fake notification claiming that a dangerous chemical attack was happening.", "A message inviting all citizens to a free public concert in the park.", "An alert telling people that all schools would be closed during summer.", "A notice asking residents to update their phone games."],
            "answer": 0,
            "explanation": "本文第2文に「false notifications claiming that a dangerous chemical attack was happening right away」と明記されています。"
        },
        {
            "question": "What did the security team do as soon as they discovered the intrusion?",
            "options": ["They blocked the attackers within minutes and announced that the alert was fake.", "They shut down the entire national electricity network for three days.", "They deleted all user accounts and closed the emergency service permanently.", "They asked residents to throw away their mobile phones."],
            "answer": 0,
            "explanation": "本文第3文に「Security teams acted within minutes to stop the unauthorized access and tell citizens that the message was a fake」とあります。"
        },
        {
            "question": "Why do cyber attackers target civil emergency alert systems?",
            "options": ["To spread panic and make people doubt official government announcements.", "To test whether smartphone batteries last longer during alarms.", "To help city police clean up historical monument statues.", "To practice writing short English stories for young children."],
            "answer": 0,
            "explanation": "本文第4文に「meant to cause public fear and make people distrust official civil announcements」と書かれています。"
        }
    ],
    "vocab": [
        {"word": "attacker", "meaning": "攻撃者、襲撃者", "example": "Cyber attackers target computer systems with weak passwords."},
        {"word": "notification", "meaning": "通知、お知らせ", "example": "She turned off app notifications while studying for exams."},
        {"word": "distrust", "meaning": "〜を疑う、信用しない", "example": "False news stories cause people to distrust media reports."},
        {"word": "broadcast", "meaning": "放送する、広く配信する", "example": "The radio station broadcasts weather alerts every hour."}
    ]
}

# 9. australia-social-media-ban-high-court-challenge-reddit-digital-freedom-project (law)
j9 = {
    "slug": "australia-social-media-ban-high-court-challenge-reddit-digital-freedom-project",
    "category": "law",
    "date": "2026-11-03",
    "pub_date": "2026-11-03",
    "source_url": "https://www.theguardian.com/australia-news/2026/nov/03/australia-social-media-ban-high-court-challenge-reddit-digital-freedom-project",
    "source_name": "The Guardian",
    "source_media": "The Guardian",
    "source_domain": "theguardian.com",
    "source_attribution": "The Guardian (November 3, 2026)",
    "category_label": "LAW • DIGITAL CONSTITUTIONAL RIGHTS",
    "title": "Australia's Social Media Ban for Teenagers Taken to the High Court",
    "headline_ja": "オーストラリアの16歳未満SNS禁止令、憲法違反を巡り最高裁判所へ",
    "lead_ja": "オーストラリア政府が決めた『16歳未満のSNS利用禁止』の法律に対し、若者の権利を守る団体が『意見を言ったり学んだりする自由を奪っており憲法違反だ』と最高裁に訴え出ました。",
    "subhead": "Digital rights groups question whether banning teenagers from social media breaks democratic freedoms.",
    "lead_snippet": "A landmark legal battle begins as youth advocates contest a blanket social media age limit in court.",
    "summary_points": [
        "オーストラリアで16歳未満のSNSアカウントを全面禁止する新法が成立。",
        "デジタル人権団体が、若者の表現の自由や情報アクセス権を侵害しているとして違憲訴訟。",
        "スマホ依存やネットいじめからの保護と、若者の自由なコミュニケーションの権利の対立。"
    ],
    "image": "https://images.unsplash.com/photo-1589829545856-d10d557cf95f?w=1000&auto=format&fit=crop&q=80",
    "sentences": [
        {"num": 1, "en": "Civil rights groups in Australia have challenged a new law that bans anyone under sixteen from using social media.", "ja": "オーストラリアの市民権団体が、16歳未満の者がソーシャルメディアを利用することを禁じる新しい法律に異議を唱えました。"},
        {"num": 2, "en": "The government passed the strict law to protect young people from cyberbullying and harmful internet habits.", "ja": "政府は、ネットいじめや有害なネット習慣から若者を守るためにこの厳格な法律を可決しました。"},
        {"num": 3, "en": "However, lawyers argue that the law stops teenagers from expressing their political ideas and sharing news with friends.", "ja": "しかし弁護士らは、この法律が10代の若者が自分の政治的な考えを表現したり友達とニュースを共有したりするのを妨げていると主張しています。"},
        {"num": 4, "en": "They also worry that requiring face scans or identity cards to verify age will threaten everyone's online privacy.", "ja": "彼らはまた、年齢を確認するために顔スキャンや身分証を要求することが、全員のネット上のプライバシーを脅かすと心配しています。"},
        {"num": 5, "en": "Judges in the High Court will decide whether the ban is lawful or if it goes too far in limiting personal freedom.", "ja": "最高裁判所の裁判官らは、この禁止が合法であるか、あるいは個人の自由を過度に制限しているかを判断する予定です。"}
    ],
    "dialogue": [
        {"speaker": "Keita先生", "name": "Keita先生", "role": "英語講師", "text": "オーストラリアで16歳未満のSNS利用が禁止された法律について、最高裁判所で裁判が始まったよ。"},
        {"speaker": "Nanami", "name": "Nanami", "role": "生徒・アシスタント", "text": "SNSを使えないようにするのは、ネットいじめやスマホ中毒から守るためですよね？"},
        {"speaker": "Keita先生", "name": "Keita先生", "role": "英語講師", "text": "そうなんだ。でも、自分の意見を言ったりニュースを知る自由まで一律に奪ってしまうのは憲法違反じゃないか、と争われているんだよ。"},
        {"speaker": "Nanami", "name": "Nanami", "role": "生徒・アシスタント", "text": "子どもを守ることと、子どもの権利を認めることのバランスは、とても難しい問題ですね！"}
    ],
    "quiz": [
        {
            "question": "What does Australia's new social media law prohibit?",
            "options": ["Anyone under sixteen years old from holding active social media accounts.", "Primary school students from doing their homework on computers.", "Adults from using smartphones during working hours.", "Universities from teaching computer programming courses."],
            "answer": 0,
            "explanation": "本文第1文に「bans anyone under sixteen from using social media」と明記されています。"
        },
        {
            "question": "What is one main argument against this social media ban?",
            "options": ["It stops teenagers from sharing ideas, expressing views, and connecting with peers.", "It makes video game consoles much more expensive for families.", "It requires all schools to replace paper notebooks with tablets.", "It forces children to watch five hours of television each evening."],
            "answer": 0,
            "explanation": "本文第3文に「stops teenagers from expressing their political ideas and sharing news with friends」とあります。"
        },
        {
            "question": "What privacy concern do lawyers highlight regarding age checks?",
            "options": ["Demanding face scans or identity cards could compromise citizens' online privacy.", "Smartphones will become too heavy to carry in school bags.", "Websites will charge a thousand dollars for opening an account.", "Computers will stop working whenever it rains outside."],
            "answer": 0,
            "explanation": "本文第4文に「requiring face scans or identity cards to verify age will threaten everyone's online privacy」と書かれています。"
        }
    ],
    "vocab": [
        {"word": "challenge", "meaning": "〜に異議を唱える、挑戦する", "example": "Lawyers challenged the new council tax in the high court."},
        {"word": "habit", "meaning": "習慣、癖", "example": "Reading for twenty minutes before bed is a healthy habit."},
        {"word": "verify", "meaning": "〜を確認する、実証する", "example": "Please verify your email address to complete registration."},
        {"word": "lawful", "meaning": "合法の、法律にかなった", "example": "The police confirmed that the protest was entirely lawful."}
    ]
}

# 10. uk-making-up-china-policy-as-it-goes-along-mps (law / politics)
j10 = {
    "slug": "uk-making-up-china-policy-as-it-goes-along-mps",
    "category": "law",
    "date": "2026-11-03",
    "pub_date": "2026-11-03",
    "source_url": "https://www.theguardian.com/politics/2026/nov/02/uk-making-up-china-policy-as-it-goes-along-mps",
    "source_name": "The Guardian",
    "source_media": "The Guardian",
    "source_domain": "theguardian.com",
    "source_attribution": "The Guardian (November 2, 2026)",
    "category_label": "LAW • FOREIGN POLICY & STATUTORY SCRUTINY",
    "title": "UK Parliament Calls for Clear Laws and Strategy on Foreign Trade and Security",
    "headline_ja": "英議会、安全保障と国際貿易に関する明確な法律と戦略の制定を要求",
    "lead_ja": "イギリス議会の議員たちが、国の安全保障と外国との貿易についての政府の方針が定まっておらず混乱を招いていると批判し、明確な法律に基づく長期的なルールを作るよう求めました。",
    "subhead": "Politicians say businesses need predictable legal rules when dealing with high-tech materials and foreign investment.",
    "lead_snippet": "A parliamentary inquiry urges ministers to write consistent laws balancing trade opportunities with national security.",
    "summary_points": [
        "英議会の特別委員会が、政府の貿易や外交の方針がブレていて混乱していると指摘。",
        "先端技術や重要鉱物の取引について、その場の判断ではなく明確な法律ルールが必要。",
        "国の安全保障を守りながら、企業が安心して計画を立てられる予測可能性の確保を求めた。"
    ],
    "image": "https://images.unsplash.com/photo-1526304640581-d334cdbbf45e?w=1000&auto=format&fit=crop&q=80",
    "sentences": [
        {"num": 1, "en": "A committee of British lawmakers has warned that the government lacks a clear and steady plan for international trade and security.", "ja": "英国議員の委員会は、政府が国際貿易と安全保障に関する明確で安定した計画を欠いていると警告しました。"},
        {"num": 2, "en": "The inquiry found that changing diplomatic decisions have made it difficult for UK businesses to plan long-term factory investments.", "ja": "調査によると、変化する外交的判断が、英国企業にとって長期的な工場投資の計画を立てることを難しくしています。"},
        {"num": 3, "en": "Politicians explained that protecting critical computer chips and clean energy materials requires clear statutory rules rather than quick promises.", "ja": "政治家らは、重要コンピュータチップやクリーンエネルギー材料を保護するには、その場の約束ではなく明確な法律のルールが必要だと説明しました。"},
        {"num": 4, "en": "Clear guidelines would help companies trade safely while ensuring that sensitive technologies do not end up in hostile hands.", "ja": "明確な指針があれば、企業は安全に貿易を行いながら、機密技術が敵対的な手に渡らないようにすることができます。"},
        {"num": 5, "en": "The committee asked ministers to draft a comprehensive national strategy bill before the end of the parliamentary year.", "ja": "委員会は、議会年度の終了前に包括的な国家戦略法案を起草するよう閣僚らに求めました。"}
    ],
    "dialogue": [
        {"speaker": "Keita先生", "name": "Keita先生", "role": "英語講師", "text": "イギリスの議会が、政府の外交方針がブレていて企業が困っていると指摘したニュースだよ。"},
        {"speaker": "Nanami", "name": "Nanami", "role": "生徒・アシスタント", "text": "貿易をして経済を良くしたいけれど、ハイテク技術が奪われるのも心配で迷っているんですね。"},
        {"speaker": "Keita先生", "name": "Keita先生", "role": "英語講師", "text": "その通り。だから大臣の気分で決めるのではなく、何を守るべきか法律でしっかりルール化して予測できるようにすべきだと言っているんだ。"},
        {"speaker": "Nanami", "name": "Nanami", "role": "生徒・アシスタント", "text": "法律のルールがはっきりしていると、会社も安心して将来の計画を立てられますね！"}
    ],
    "quiz": [
        {
            "question": "What did British lawmakers say about the government's current foreign trade approach?",
            "options": ["It lacks a clear, steady plan and creates uncertainty for domestic businesses.", "It spends too much money building wooden sailboats for world trade.", "It forces all technology companies to close their overseas offices.", "It forbids British citizens from learning foreign languages in school."],
            "answer": 0,
            "explanation": "本文第1文および第2文に「lacks a clear and steady plan」「made it difficult for UK businesses to plan long-term」とあります。"
        },
        {
            "question": "Why do politicians want clear statutory laws for sensitive technologies?",
            "options": ["To protect critical computer microchips and keep trade safe under clear rules.", "To make all computer software free for foreign governments.", "To prevent domestic companies from selling anything abroad.", "To encourage engineers to destroy their research laboratories."],
            "answer": 0,
            "explanation": "本文第3文および第4文に「protecting critical computer chips and clean energy materials requires clear statutory rules」と述べられています。"
        },
        {
            "question": "What did the committee request ministers to produce before the end of the year?",
            "options": ["A comprehensive national trade and security strategy bill.", "A plan to move the parliament building to a new island.", "An order banning all private smartphone manufacturing.", "A new national anthem written entirely in Latin."],
            "answer": 0,
            "explanation": "本文第5文に「draft a comprehensive national strategy bill before the end of the parliamentary year」と書かれています。"
        }
    ],
    "vocab": [
        {"word": "committee", "meaning": "委員会", "example": "The school sports committee organized the autumn sports day."},
        {"word": "guideline", "meaning": "指針、ガイドライン", "example": "Follow the safety guidelines when conducting science experiments."},
        {"word": "sensitive", "meaning": "機密の、慎重な扱いを要する", "example": "Medical records contain sensitive personal information."},
        {"word": "comprehensive", "meaning": "包括的な、総合的な", "example": "The university library offers a comprehensive collection of history books."}
    ]
}

# 11. bbc-young-musician-teenage-violinist-sofia-demetriades (culture)
j11 = {
    "slug": "bbc-young-musician-teenage-violinist-sofia-demetriades",
    "category": "culture",
    "date": "2026-11-03",
    "pub_date": "2026-11-03",
    "source_url": "https://www.theguardian.com/music/2026/nov/01/bbc-young-musician-teenage-violinist-sofia-demetriades",
    "source_name": "The Guardian",
    "source_media": "The Guardian",
    "source_domain": "theguardian.com",
    "source_attribution": "The Guardian (November 1, 2026)",
    "category_label": "CULTURE • CLASSICAL MUSIC EXCELLENCE",
    "title": "Seventeen-Year-Old Violinist Sofia Wins Prestigious BBC Music Award",
    "headline_ja": "17歳のヴァイオリニスト、ソフィアさんが名門BBC音楽コンクールで優勝",
    "lead_ja": "イギリスの名門クラシック音楽コンクールで、17歳のソフィア・デメトリアデスさんがオーケストラとの見事なヴァイオリン演奏を披露し、最優秀若手音楽家の栄冠に輝きました。",
    "subhead": "A talented high school musician wins nationwide praise for her expressive and skilled violin concerto.",
    "lead_snippet": "Seventeen-year-old Sofia Demetriades has won the BBC Young Musician title after an outstanding final performance.",
    "summary_points": [
        "17歳のヴァイオリニストが、英国で最も権威ある若手音楽コンクールの決勝で優勝。",
        "難易度の高いシベリウスの協奏曲を、美しい音色と力強い表現力で見事に弾きこなした。",
        "地域で子どもたちが楽器を学べる公的な支援プログラムが、才能の開花に大きく役立った。"
    ],
    "image": "https://images.unsplash.com/photo-1511671782779-c97d3d27a1d4?w=1000&auto=format&fit=crop&q=80",
    "sentences": [
        {"num": 1, "en": "Seventeen-year-old violinist Sofia Demetriades has won Britain's top award for young classical musicians.", "ja": "17歳のヴァイオリニスト、ソフィア・デメトリアデスさんが、若手クラシック音楽家に贈られる英国最高峰の賞を受賞しました。"},
        {"num": 2, "en": "She performed a challenging violin concerto with a famous professional orchestra and amazed the entire concert audience.", "ja": "彼女は有名なプロのオーケストラとともに難易度の高いヴァイオリン協奏曲を演奏し、コンサートの観客全員を驚かせました。"},
        {"num": 3, "en": "The judges praised her gentle musical tone as well as her strong confidence during the fast parts of the piece.", "ja": "審査員らは、曲の速い部分での強い自信とともに、彼女の優しい音楽的音色を称賛しました。"},
        {"num": 4, "en": "Music teachers mentioned that joining a local youth orchestra when she was young helped her develop her wonderful talent.", "ja": "音楽の先生たちは、幼い頃に地元の青少年オーケストラに参加したことが彼女の素晴らしい才能を伸ばす助けになったと述べました。"},
        {"num": 5, "en": "Sofia hopes her victory will encourage other high school students to explore the joy of playing classical music.", "ja": "ソフィアさんは、自分の勝利が他の高校生たちにもクラシック音楽を演奏する喜びを探求する励みになることを願っています。"}
    ],
    "dialogue": [
        {"speaker": "Keita先生", "name": "Keita先生", "role": "英語講師", "text": "17歳の高校生ヴァイオリニストが、イギリスの伝統ある音楽コンクールで優勝したよ。"},
        {"speaker": "Nanami", "name": "Nanami", "role": "生徒・アシスタント", "text": "同世代の人がプロのオーケストラをバックに堂々と演奏して優勝するなんて、すごくかっこいいですね！"},
        {"speaker": "Keita先生", "name": "Keita先生", "role": "英語講師", "text": "そうだね。子どもの頃に地域の手頃なユースオーケストラで学べたことが大きかったんだ。文化の支援が大事だね。"},
        {"speaker": "Nanami", "name": "Nanami", "role": "生徒・アシスタント", "text": "夢中になれるものを見つけて努力する姿に、大きな勇気をもらえますね！"}
    ],
    "quiz": [
        {
            "question": "What major achievement did seventeen-year-old Sofia accomplish?",
            "options": ["She won Britain's top prestigious competition for young classical musicians.", "She painted a portrait of the royal family in London.", "She built a full-size wooden sailboat in her school workshop.", "She won a national swimming championship for teenagers."],
            "answer": 0,
            "explanation": "本文第1文に「won Britain's top award for young classical musicians」と明記されています。"
        },
        {
            "question": "What did the judging panel especially praise about her playing?",
            "options": ["Her gentle tone and strong musical confidence during difficult passages.", "Her ability to balance a book on her head while bowing the violin.", "Her choice to wear bright pink athletic shoes on stage.", "Her speed in tuning all four strings in two seconds."],
            "answer": 0,
            "explanation": "本文第3文に「praised her gentle musical tone as well as her strong confidence」とあります。"
        },
        {
            "question": "What helped Sofia develop her violin skills when she was younger?",
            "options": ["Participating in a subsidized local youth orchestra program.", "Listening to rock music on headphones while studying geography.", "Traveling abroad without taking any violin lessons.", "Reading silent comic books during school summer holidays."],
            "answer": 0,
            "explanation": "本文第4文に「joining a local youth orchestra when she was young helped her develop her wonderful talent」と書かれています。"
        }
    ],
    "vocab": [
        {"word": "award", "meaning": "賞、栄誉", "example": "She received an award for academic excellence at graduation."},
        {"word": "challenging", "meaning": "やりがいのある、難易度の高い", "example": "Learning a new language is challenging but very rewarding."},
        {"word": "audience", "meaning": "聴衆、観客", "example": "The audience applauded warmly after the violin solo."},
        {"word": "victory", "meaning": "勝利、栄冠", "example": "The soccer team celebrated their hard-fought victory."}
    ]
}

# 12. john-lewis-christmas-advert-kristin-scott-thomas-glamorous-granny-gift-hunt (entertainment)
j12 = {
    "slug": "john-lewis-christmas-advert-kristin-scott-thomas-glamorous-granny-gift-hunt",
    "category": "entertainment",
    "date": "2026-11-03",
    "pub_date": "2026-11-03",
    "source_url": "https://www.theguardian.com/media/2026/nov/03/john-lewis-christmas-advert-kristin-scott-thomas-glamorous-granny-gift-hunt",
    "source_name": "The Guardian",
    "source_media": "The Guardian",
    "source_domain": "theguardian.com",
    "source_attribution": "The Guardian (November 3, 2026)",
    "category_label": "ENTERTAINMENT • CONSUMER CULTURE & ADVERTISING",
    "title": "Popular British Department Store Releases Heartwarming Christmas Advert",
    "headline_ja": "英国名物デパートのクリスマスCM解禁：おばあちゃんと家族の温かい絆を描く",
    "lead_ja": "イギリスの冬の始まりを告げる有名デパートのクリスマスCMが公開され、孫のために特別なプレゼントを探す元気なおばあちゃんのユーモラスな冒険が、多くの人々の心を温めています。",
    "subhead": "A famous holiday commercial celebrates family affection and humor over expensive luxury spending.",
    "lead_snippet": "Britain's traditional festive commercial season has begun with a touching story about a grandmother's love.",
    "summary_points": [
        "イギリスの年末の風物詩であるデパートのクリスマスCMが公開され、全国で話題に。",
        "ただモノを買わせるのではなく、孫を思いやるおばあちゃんの愛情と家族の温もりを描く演出。",
        "ネットで何百万回も再生され、大切な人への気持ちを思い出すきっかけとして人気を呼んでいる。"
    ],
    "image": "https://images.unsplash.com/photo-1512389142860-9c449e58a543?w=1000&auto=format&fit=crop&q=80",
    "sentences": [
        {"num": 1, "en": "Britain's most famous department store has released its annual Christmas commercial, starting the holiday season for many people.", "ja": "英国で最も有名な百貨店が恒例のクリスマスCMを公開し、多くの人々にとってホリデーシーズンが始まりました。"},
        {"num": 2, "en": "The short movie tells the amusing story of an energetic grandmother searching for the perfect thoughtful gift for her grandchild.", "ja": "そのショートフィルムは、孫のための完璧で心のこもったギフトを探す元気なおばあちゃんの楽しい物語を描いています。"},
        {"num": 3, "en": "Instead of showing expensive gadgets, the advert focuses on funny family moments and warm connections between generations.", "ja": "高価なガジェットを見せる代わりに、この広告は楽しい家族のひとときや世代間の温かい絆に焦点を当てています。"},
        {"num": 4, "en": "Millions of people have watched the commercial on the internet and shared comments about their own family memories.", "ja": "何百万人もの人々がインターネットでこのCMを視聴し、自分自身の家族の思い出についてのコメントを共有しました。"},
        {"num": 5, "en": "The story reminds everyone that caring for family and friends is the most meaningful part of the winter holidays.", "ja": "この物語は、家族や友人を思いやることが冬の休日の最も意義ある部分であることを皆に思い出させてくれます。"}
    ],
    "dialogue": [
        {"speaker": "Keita先生", "name": "Keita先生", "role": "英語講師", "text": "イギリスのデパートのクリスマスCMが公開されて、家族の温かさが話題になっているよ。"},
        {"speaker": "Nanami", "name": "Nanami", "role": "生徒・アシスタント", "text": "おばあちゃんが孫のために一生懸命プレゼントを探す姿が、すごく微笑ましいですね！"},
        {"speaker": "Keita先生", "name": "Keita先生", "role": "英語講師", "text": "そうだね。高いモノをアピールするのではなく、相手を思いやる気持ちを描くことで、多くの人の共感を呼んでいるんだ。"},
        {"speaker": "Nanami", "name": "Nanami", "role": "生徒・アシスタント", "text": "クリスマスや年末は、家族への感謝を伝えるのに一番良い季節ですね。"}
    ],
    "quiz": [
        {
            "question": "What is the story of this popular British holiday advertisement?",
            "options": ["A lively grandmother on a mission to find a meaningful gift for her grandchild.", "A group of robots taking over a toy store on Christmas Eve.", "A young student flying a hot-air balloon across the English Channel.", "A chef trying to bake the world's largest chocolate cake."],
            "answer": 0,
            "explanation": "本文第2文に「tells the amusing story of an energetic grandmother searching for the perfect thoughtful gift for her grandchild」とあります。"
        },
        {
            "question": "What does the commercial focus on instead of expensive gadgets?",
            "options": ["Warm family moments and caring connections between generations.", "Computer games that require high-speed internet connections.", "Modern sports cars that travel faster than express trains.", "Luxury jewelry made with diamonds and solid gold."],
            "answer": 0,
            "explanation": "本文第3文に「focuses on funny family moments and warm connections between generations」と明記されています。"
        },
        {
            "question": "What message does the festive commercial remind people of?",
            "options": ["Caring for family and loved ones is the most meaningful part of the holidays.", "People should buy as many electric toys as possible before winter ends.", "Schools should give students homework during the Christmas holiday.", "Towns should turn off all holiday street lights after sunset."],
            "answer": 0,
            "explanation": "本文第5文に「caring for family and friends is the most meaningful part of the winter holidays」と述べられています。"
        }
    ],
    "vocab": [
        {"word": "annual", "meaning": "毎年の、年1回の", "example": "The school holds its annual sports festival in October."},
        {"word": "amusing", "meaning": "面白い、楽しい", "example": "The teacher told an amusing story to introduce the lesson."},
        {"word": "generation", "meaning": "世代", "example": "Stories and traditions are passed down from generation to generation."},
        {"word": "meaningful", "meaning": "意義のある、心に残る", "example": "Volunteering was a very meaningful experience for her."}
    ]
}

JUNIOR_PART2 = [j7, j8, j9, j10, j11, j12]

with open("news_portal/pipeline/data_batch30_junior_part2.py", "w", encoding="utf-8") as f:
    f.write("# -*- coding: utf-8 -*-\n")
    f.write('"""Batch 30 Part 2: Articles 7-12 (Junior) Date: 2026-11-03"""\n\n')
    f.write("JUNIOR_PART2 = ")
    f.write(json.dumps(JUNIOR_PART2, ensure_ascii=False, indent=4))
    f.write('\n\n__all__ = ["JUNIOR_PART2"]\n')

print("Wrote Junior Part 2.")
