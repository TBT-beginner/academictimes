# -*- coding: utf-8 -*-
"""Generate data_batch29_junior_part1.py and data_batch29_junior_part2.py."""
import json
import sys

def write_junior_files():
    from data_batch29_part1 import SENIOR_PART1
    from data_batch29_part2 import SENIOR_PART2

    # Article 1: rare-short-necked-oil-beetle-rediscovered-wales
    j1 = {
        "slug": "rare-short-necked-oil-beetle-rediscovered-wales",
        "category": "science",
        "date": "2026-11-02",
        "pub_date": "2026-11-02",
        "source_url": "https://www.theguardian.com/environment/2026/nov/01/rare-short-necked-oil-beetle-rediscovered-wales",
        "source_name": "The Guardian",
        "source_media": "The Guardian",
        "source_domain": "theguardian.com",
        "source_attribution": "The Guardian (November 1, 2026)",
        "category_label": "SCIENCE • ENTOMOLOGY",
        "title": "Rare Short-Necked Oil Beetle Found Again on the Welsh Coast",
        "headline_ja": "絶滅と考えられていた珍しいツチハンミョウ、ウェールズ沿岸で再発見される",
        "lead_ja": "ウェールズ西部の海岸で、半世紀以上にわたり地域絶滅したと恐れられていた非常に珍しいツチハンミョウ（コビトツチハンミョウ）の生息が確認され、自然保護活動家たちを驚かせています。",
        "subhead": "Conservationists celebrate the rediscovery of a rare insect thought to have disappeared from Wales.",
        "lead_snippet": "A rare flightless beetle with a remarkable life cycle has been rediscovered on the coast of Wales.",
        "summary_points": [
            "半世紀以上ウェールズで記録が途絶えていた珍しい甲虫が海辺の崖で再発見された。",
            "この甲虫は羽がなく飛べないため、野生のハナバチの背中に乗って巣へ移動して育つ。",
            "沿岸の草原や砂浜が守られていたことが、生き残りに重要な役割を果たしていた。"
        ],
        "image": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=1000&auto=format&fit=crop&q=80",
        "sentences": [
            {
                "num": 1,
                "en": "Nature experts in Wales have rediscovered a rare insect called the short-necked oil beetle on coastal cliffs.",
                "ja": "ウェールズの自然の専門家たちが、海岸の崖でコビトツチハンミョウと呼ばれる珍しい昆虫を再発見しました。"
            },
            {
                "num": 2,
                "en": "The flightless black insect had not been seen in the region for over fifty years and was feared extinct.",
                "ja": "飛ぶことができないこの黒い昆虫は、50年以上もこの地域で目撃されておらず、絶滅したと恐れられていました。"
            },
            {
                "num": 3,
                "en": "This beetle has an unusual life cycle, as tiny young larvae climb wild bees to reach their nests.",
                "ja": "この甲虫は珍しい生活環を持っており、小さな幼虫が野生のハナバチの体によじ登ってハチの巣へと運ばれます。"
            },
            {
                "num": 4,
                "en": "Researchers say careful management of coastal wild flower grasslands helped the tiny population survive quietly.",
                "ja": "研究者らは、海岸沿いの野生の花が咲く草原を慎重に管理したことが、わずかな個体数が静かに生き残るのを助けたと述べています。"
            },
            {
                "num": 5,
                "en": "Scientists will now study the cliffs further to protect these precious beetles and their native bee hosts.",
                "ja": "科学者たちは今後、この貴重な甲虫と宿主となる在来種のハチを守るため、崖の調査をさらに進める予定です。"
            }
        ],
        "quiz": [
            {
                "question": "Why was the rediscovery of the short-necked oil beetle surprising?",
                "options": [
                    "It had not been seen in Wales for more than fifty years.",
                    "It can fly faster than most other coastal birds.",
                    "It only lives inside cold, dark underground caves.",
                    "It was brought from another country by researchers."
                ],
                "answer": 0,
                "explanation": "本文第2文に「had not been seen in the region for over fifty years and was feared extinct（50年以上目撃されておらず地域絶滅が恐れられていた）」とあるため、50年以上見られなかったことが再発見の驚きとなった理由です。"
            },
            {
                "question": "How do the beetle's tiny larvae travel to wild bee nests?",
                "options": [
                    "By climbing directly onto the bodies of wild bees.",
                    "By swimming across small streams near the sea.",
                    "By flying through the air using small black wings.",
                    "By being carried in the warm wind during summer."
                ],
                "answer": 0,
                "explanation": "本文第3文に「tiny young larvae climb wild bees to reach their nests（小さな幼虫が野生のハチによじ登って巣へ到達する）」と説明されています。"
            },
            {
                "question": "What helped this rare beetle survive on the Welsh coast?",
                "options": [
                    "The careful protection and management of coastal grasslands.",
                    "Artificial food provided every day by local scientists.",
                    "Building concrete walls around the coastal sandy beaches.",
                    "Keeping them in modern greenhouses during the winter season."
                ],
                "answer": 0,
                "explanation": "本文第4文に「careful management of coastal wild flower grasslands helped the tiny population survive quietly（沿岸の草原の慎重な管理が生き残りを助けた）」と明記されています。"
            }
        ],
        "vocab": [
            {"word": "rediscover", "meaning": "〜を再発見する", "example": "Experts rediscovered a rare insect on the cliffs."},
            {"word": "flightless", "meaning": "飛べない", "example": "Penguins and some beetles are flightless animals."},
            {"word": "larva", "meaning": "幼虫（複数形はlarvae）", "example": "The larva climbs onto the bee's back."},
            {"word": "host", "meaning": "宿主、寄生される生物", "example": "Wild bees serve as hosts for the young beetle larvae."}
        ],
        "dialog": [
            {
                "speaker": "Keita",
                "text": "半世紀も見つかっていなかったツチハンミョウが、ウェールズの海岸で奇跡的に再発見されたんだよ。"
            },
            {
                "speaker": "Nanami",
                "text": "50年も！飛べない虫なのに、今までどうやって生き残っていたんですか？"
            },
            {
                "speaker": "Keita",
                "text": "幼虫が野生のハナバチの体にしがみついて巣へ運ばれ、花粉を食べて育つんだ。海岸の草原が手つかずで守られていたおかげだね。"
            },
            {
                "speaker": "Nanami",
                "text": "昆虫とハチの共生関係と、豊かな自然環境の両方が揃って初めて命がつながるんですね！"
            }
        ]
    }

    # Article 2: tech-stocks-drop-earnings-report
    j2 = {
        "slug": "tech-stocks-drop-earnings-report",
        "category": "science",
        "date": "2026-11-02",
        "pub_date": "2026-11-02",
        "source_url": "https://www.theguardian.com/business/2026/nov/01/tech-stocks-drop-earnings-report",
        "source_name": "The Guardian",
        "source_media": "The Guardian",
        "source_domain": "theguardian.com",
        "source_attribution": "The Guardian (November 1, 2026)",
        "category_label": "SCIENCE • TECH ECONOMY",
        "title": "Tech Stocks Fall as Investors Worry About Huge Artificial Intelligence Costs",
        "headline_ja": "巨額のAI投資コストへの懸念からハイテク企業の株価が下落",
        "lead_ja": "世界の大手IT企業が人工知能（AI）開発に巨額の資金を投じ続けているものの、期待通りの利益が出るまでに時間がかかるのではないかという不安から、ハイテク株が急落しました。",
        "subhead": "Global stock markets wobble as massive spending on data centres and AI chips raises investor concerns.",
        "lead_snippet": "Leading technology companies saw their share prices dip following questions about the rapid return on AI investments.",
        "summary_points": [
            "米国の巨大IT企業がデータセンターや半導体に何兆円もの資金を投じている。",
            "投資額の大きさに比べて短期的な利益の伸びが追いつかないとの見方が広がった。",
            "AI技術自体は進歩しているが、ビジネスとしての採算性が厳しく評価されている。"
        ],
        "image": "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=1000&auto=format&fit=crop&q=80",
        "sentences": [
            {
                "num": 1,
                "en": "Shares of major technology companies dropped sharply after their latest financial results were released this week.",
                "ja": "今週最新の決算発表が行われた後、主要ハイテク企業の株価が急激に下落しました。"
            },
            {
                "num": 2,
                "en": "Tech giants are spending hundreds of billions of dollars on data centres and specialized microchips for artificial intelligence.",
                "ja": "ハイテク大手は、人工知能用のデータセンターや特化したマイクロチップに何千億ドルもの資金を費やしています。"
            },
            {
                "num": 3,
                "en": "However, many investors are worried that it will take many years to turn these huge costs into steady profits.",
                "ja": "しかし多くの投資家は、これらの巨額の費用を安定した利益に変えるには何年もかかるのではないかと心配しています。"
            },
            {
                "num": 4,
                "en": "Some company leaders explained that building advanced technology requires patience and long-term thinking.",
                "ja": "一部の企業経営者は、高度な技術を構築するには忍耐と長期的な視点が必要だと説明しました。"
            },
            {
                "num": 5,
                "en": "Financial analysts believe stock markets will remain cautious until AI software shows clear commercial success.",
                "ja": "金融アナリストは、AIソフトウェアが明確な商業的成功を示すまで、株式市場は慎重な姿勢を保つだろうと考えています。"
            }
        ],
        "quiz": [
            {
                "question": "Why did major technology stock prices drop?",
                "options": [
                    "Investors worried about the enormous spending on AI without quick profits.",
                    "The companies decided to stop developing artificial intelligence altogether.",
                    "Governments ordered all tech companies to close their global data centres.",
                    "Smartphones and personal computers were banned in several large markets."
                ],
                "answer": 0,
                "explanation": "本文第3文に「many investors are worried that it will take many years to turn these huge costs into steady profits（巨額の費用が安定した利益に変わるまで何年もかかると懸念した）」とある通り、投資回収の遅れへの懸念が原因です。"
            },
            {
                "question": "What are technology giants spending hundreds of billions of dollars on?",
                "options": [
                    "Data centres and specialized microchips for artificial intelligence.",
                    "Building traditional diesel locomotives for cross-country railways.",
                    "Buying oil refineries and gold mines around the world.",
                    "Opening physical bookstores in every major European town."
                ],
                "answer": 0,
                "explanation": "本文第2文に「spending hundreds of billions of dollars on data centres and specialized microchips for artificial intelligence」と明記されています。"
            },
            {
                "question": "What do financial analysts think is needed for markets to become confident again?",
                "options": [
                    "Clear commercial success and profits from AI software.",
                    "A complete stop to all technological research in universities.",
                    "Lowering the price of internet services to zero globally.",
                    "Replacing all human employees with robot workers immediately."
                ],
                "answer": 0,
                "explanation": "本文第5文に「until AI software shows clear commercial success（AIソフトウェアが明確な商業的成功を示すまで）」と述べられています。"
            }
        ],
        "vocab": [
            {"word": "financial results", "meaning": "決算、業績報告", "example": "The company reported strong financial results for October."},
            {"word": "microchip", "meaning": "超小型半導体チップ", "example": "AI software requires fast and powerful microchips."},
            {"word": "patience", "meaning": "忍耐、辛抱強さ", "example": "Scientific breakthroughs require patience and hard work."},
            {"word": "cautious", "meaning": "用心深い、慎重な", "example": "Investors remain cautious about spending too much money."}
        ],
        "dialog": [
            {
                "speaker": "Keita",
                "text": "最新の決算発表を受けて、巨大IT企業の株価が一時的に大きく下がったニュースだよ。"
            },
            {
                "speaker": "Nanami",
                "text": "AIって今すごく流行っているのに、どうして株価が下がってしまったんですか？"
            },
            {
                "speaker": "Keita",
                "text": "データセンターや半導体の整備に兆単位のお金がかかっていて、投資に見合う利益がいつ出るのか不安視されたんだ。"
            },
            {
                "speaker": "Nanami",
                "text": "なるほど、技術の進歩だけでなく、持続可能なビジネスとして成り立つかが問われているんですね。"
            }
        ]
    }

    # Article 3: finland-criminal-investigation-google-clearing-forest-datacentre
    j3 = {
        "slug": "finland-criminal-investigation-google-clearing-forest-datacentre",
        "category": "environment",
        "date": "2026-11-02",
        "pub_date": "2026-11-02",
        "source_url": "https://www.theguardian.com/technology/2026/nov/01/finland-criminal-investigation-google-clearing-forest-datacentre",
        "source_name": "The Guardian",
        "source_media": "The Guardian",
        "source_domain": "theguardian.com",
        "source_attribution": "The Guardian (November 1, 2026)",
        "category_label": "ENVIRONMENT • FORESTRY LAW",
        "title": "Finland Opens Criminal Investigation into Forest Clearing for Tech Giant Data Centre",
        "headline_ja": "フィンランド当局、データセンター建設に伴う森林伐採で刑事捜査を開始",
        "lead_ja": "フィンランド警察は、巨大IT企業のデータセンター拡張工事において、保護対象の森林や野生動物の生息地が無許可で伐採された疑いがあるとして、刑事捜査を開始しました。",
        "subhead": "Authorities examine whether environmental laws were broken during land preparation for a major cloud facility.",
        "lead_snippet": "Finnish environmental inspectors have launched an investigation into the felling of trees for a server site.",
        "summary_points": [
            "フィンランドでデータセンター用地を造成する際、保護林が伐採された疑いが浮上。",
            "警察と環境当局が自然保護法違反の可能性があるとして捜査をスタートさせた。",
            "脱炭素やAIのインフラ建設と、地域の自然保護との摩擦が浮き彫りになっている。"
        ],
        "image": "https://images.unsplash.com/photo-1542273917363-3b1817f69a2d?w=1000&auto=format&fit=crop&q=80",
        "sentences": [
            {
                "num": 1,
                "en": "Police in Finland have opened a criminal investigation into the clearing of protected forest land for a new data centre.",
                "ja": "フィンランド警察は、新しいデータセンターのための保護森林の伐採に関して刑事捜査を開始しました。"
            },
            {
                "num": 2,
                "en": "Environmental inspectors noticed that several hectares of old trees were cut down without proper municipal permits.",
                "ja": "環境調査官は、正規の自治体許可なしに数ヘクタールの原生林が伐採されたことに気づきました。"
            },
            {
                "num": 3,
                "en": "The area is home to endangered flying squirrels and rare birds that rely on undisturbed pine and birch forests.",
                "ja": "この地域は、手つかずの松や白樺の森を頼りに生きている絶滅危惧種のムササビや珍しい鳥類の生息地です。"
            },
            {
                "num": 4,
                "en": "The technology company stated that it takes local rules seriously and is fully cooperating with the authorities.",
                "ja": "そのIT企業は地域の規則を真摯に受け止めており、当局に全面的に協力していると述べました。"
            },
            {
                "num": 5,
                "en": "This case highlights the growing conflict between building digital infrastructure and preserving natural habitats.",
                "ja": "この事件は、デジタルインフラの建設と自然生息地の保護との間で高まる対立を浮き彫りにしています。"
            }
        ],
        "quiz": [
            {
                "question": "Why did Finnish police launch a criminal investigation?",
                "options": [
                    "Protected forest land was cleared without proper permits for a data centre.",
                    "Computers were stolen from an elementary school computer room.",
                    "Tourists were feeding bread to bears in a national wildlife park.",
                    "A chemical factory spilled toxic waste into the Baltic Sea."
                ],
                "answer": 0,
                "explanation": "本文第1文および第2文に「clearing of protected forest land for a new data centre」「cut down without proper municipal permits」とあり、適切な許可なく保護林を伐採した疑いが持たれています。"
            },
            {
                "question": "Which animal lives in the forest area that was cleared?",
                "options": [
                    "Endangered flying squirrels.",
                    "Wild desert camels.",
                    "Tropical marine turtles.",
                    "Mountain gorillas."
                ],
                "answer": 0,
                "explanation": "本文第3文に「home to endangered flying squirrels and rare birds」と明記されています。"
            },
            {
                "question": "What larger issue does this Finnish investigation highlight?",
                "options": [
                    "The conflict between building digital facilities and protecting natural habitats.",
                    "The difficulty of teaching computer science in rural Scandinavian schools.",
                    "The lack of renewable wind energy resources in northern Europe.",
                    "The need to replace all paper books with electronic tablet screens."
                ],
                "answer": 0,
                "explanation": "本文第5文に「conflict between building digital infrastructure and preserving natural habitats」と述べられています。"
            }
        ],
        "vocab": [
            {"word": "investigation", "meaning": "捜査、調査", "example": "The police launched an official investigation into the incident."},
            {"word": "permit", "meaning": "許可証、認可", "example": "You need a special permit to cut down trees in this forest."},
            {"word": "endangered", "meaning": "絶滅の危機に瀕した", "example": "Flying squirrels are protected as endangered animals."},
            {"word": "infrastructure", "meaning": "社会基盤、インフラ", "example": "High-speed internet is an essential part of modern infrastructure."}
        ],
        "dialog": [
            {
                "speaker": "Keita",
                "text": "フィンランドで巨大IT企業のデータセンター建設を巡り、保護林の無許可伐採の疑いで捜査が始まったよ。"
            },
            {
                "speaker": "Nanami",
                "text": "クリーンなイメージのある北欧でも、森林伐採が問題になっているんですね。"
            },
            {
                "speaker": "Keita",
                "text": "AIやクラウドのためのデータセンター需要が世界中で急増していて、野生生物の生息地とぶつかってしまうケースが増えているんだ。"
            },
            {
                "speaker": "Nanami",
                "text": "便利なデジタル社会と環境保護のバランスをどう取るか、世界共通の課題ですね。"
            }
        ]
    }

    # Article 4: indonesia-protests-fire-haze-economy
    j4 = {
        "slug": "indonesia-protests-fire-haze-economy",
        "category": "environment",
        "date": "2026-11-02",
        "pub_date": "2026-11-02",
        "source_url": "https://www.theguardian.com/world/2026/nov/01/indonesia-protests-fire-haze-economy",
        "source_name": "The Guardian",
        "source_media": "The Guardian",
        "source_domain": "theguardian.com",
        "source_attribution": "The Guardian (November 1, 2026)",
        "category_label": "ENVIRONMENT • AIR QUALITY",
        "title": "Citizens Protest in Indonesia as Toxic Smoke and Forest Fires Hurt Health and Economy",
        "headline_ja": "インドネシアで市民抗議：森林火災による有害煙が健康と経済に深刻な被害",
        "lead_ja": "インドネシア各地で泥炭地や森林の火災による煙害（ヘイズ）が深刻化し、市民や学生たちが呼吸器被害の防止と企業の違法な野焼きの厳罰化を求めてデモを行いました。",
        "subhead": "Demonstrators demand stronger government action to stop peatland burning that chokes cities with heavy smog.",
        "lead_snippet": "Thousands of residents have protested across Indonesian cities over hazardous air caused by agricultural fires.",
        "summary_points": [
            "農地拡大のための泥炭地火災により、煙害が広がり多くの住民が呼吸器疾患を訴えた。",
            "学校の休校や航空便の欠航など、日常生活と地域経済に大きな打撃を与えている。",
            "市民たちは違法な火入れを行う大企業への厳しい取り締まりと罰則を求めている。"
        ],
        "image": "https://images.unsplash.com/photo-1542601906990-b4d3fb778b09?w=1000&auto=format&fit=crop&q=80",
        "sentences": [
            {
                "num": 1,
                "en": "Thousands of people across Indonesia joined public demonstrations to protest against dangerous smoke caused by forest fires.",
                "ja": "インドネシア全土で数千人の人々が、森林火災による危険な煙に抗議する街頭デモに参加しました。"
            },
            {
                "num": 2,
                "en": "Fires used to clear land for palm oil and paper farms have spread out of control across dried peatlands.",
                "ja": "パーム油や製紙用農地のために土地を切り開く火入れが、乾燥した泥炭地に燃え広がって制御不能になっています。"
            },
            {
                "num": 3,
                "en": "The heavy yellow haze forced schools to shut down and caused tens of thousands of children to suffer from coughs and asthma.",
                "ja": "濃い黄色の煙霧によって学校は休校を余儀なくされ、何万人もの子どもたちが咳や喘息に苦しんでいます。"
            },
            {
                "num": 4,
                "en": "Protesters demanded that the government punish big agricultural corporations that ignore environmental safety rules.",
                "ja": "抗議者らは、環境安全規則を無視する大手農業企業を政府が処罰するよう要求しました。"
            },
            {
                "num": 5,
                "en": "Neighbouring Southeast Asian countries also urged faster action to prevent transboundary air pollution across the region.",
                "ja": "東南アジアの近隣諸国も、地域をまたぐ国境を越えた大気汚染を防ぐため、迅速な対応を強く求めました。"
            }
        ],
        "quiz": [
            {
                "question": "What is the main cause of the heavy smoke and forest fires in Indonesia?",
                "options": [
                    "Fires set to clear land for palm oil and paper plantations.",
                    "Sparks from old tourist steam trains running in the jungle.",
                    "Lightning storms hitting wooden houses in coastal villages.",
                    "Bonfires lit by mountain climbers during the rainy season."
                ],
                "answer": 0,
                "explanation": "本文第2文に「Fires used to clear land for palm oil and paper farms have spread out of control」とある通り、農地開墾のための火入れが原因です。"
            },
            {
                "question": "How has the thick smoke affected local residents and children?",
                "options": [
                    "It caused schools to close and led to widespread coughs and asthma.",
                    "It made all tap water freeze into solid ice cubes.",
                    "It improved outdoor visibility and made driving much easier.",
                    "It attracted rare migratory birds from northern countries."
                ],
                "answer": 0,
                "explanation": "本文第3文に「forced schools to shut down and caused tens of thousands of children to suffer from coughs and asthma」と書かれています。"
            },
            {
                "question": "Why are neighbouring countries in Southeast Asia concerned?",
                "options": [
                    "The toxic air pollution travels across national borders.",
                    "They want to buy all the timber from the burning forests.",
                    "They are planning to build new international airports in the area.",
                    "The smoke is creating heavy snowstorms across the tropics."
                ],
                "answer": 0,
                "explanation": "本文第5文に「prevent transboundary air pollution across the region（地域全体の国境を越えた大気汚染を防ぐ）」と説明されています。"
            }
        ],
        "vocab": [
            {"word": "demonstration", "meaning": "デモ行進、抗議行動", "example": "Thousands gathered in the capital for a peaceful demonstration."},
            {"word": "peatland", "meaning": "泥炭地（炭素を多く含む湿地帯）", "example": "Drained peatlands can catch fire easily during dry seasons."},
            {"word": "haze", "meaning": "もや、煙霧", "example": "The city was covered in a thick haze of smoke."},
            {"word": "transboundary", "meaning": "国境を越える", "example": "Air pollution has become a serious transboundary issue."}
        ],
        "dialog": [
            {
                "speaker": "Keita",
                "text": "インドネシアで泥炭地火災の煙害（ヘイズ）がひどく、市民たちが抗議デモを起こしているんだ。"
            },
            {
                "speaker": "Nanami",
                "text": "煙で学校が休みになったり、子どもたちが喘息になったりしているんですね…。"
            },
            {
                "speaker": "Keita",
                "text": "パーム油などの農園を広げるための違法な野焼きが原因で、国境を越えてシンガポールやマレーシアにも届いてしまうんだよ。"
            },
            {
                "speaker": "Nanami",
                "text": "環境被害と住民の健康を守るために、企業への厳しい罰則や国際的な協力が不可欠ですね。"
            }
        ]
    }

    # Article 5: sadiq-khan-calls-cap-numbers-robotaxis-london-streets
    j5 = {
        "slug": "sadiq-khan-calls-cap-numbers-robotaxis-london-streets",
        "category": "society",
        "date": "2026-11-02",
        "pub_date": "2026-11-02",
        "source_url": "https://www.theguardian.com/uk-news/2026/nov/01/sadiq-khan-calls-cap-numbers-robotaxis-london-streets",
        "source_name": "The Guardian",
        "source_media": "The Guardian",
        "source_domain": "theguardian.com",
        "source_attribution": "The Guardian (November 1, 2026)",
        "category_label": "SOCIETY • URBAN TRANSPORT",
        "title": "London Mayor Calls for Limits on Driverless Robotaxis on City Streets",
        "headline_ja": "ロンドン市長、市街地を走る自動運転「ロボタクシー」の台数制限を要求",
        "lead_ja": "ロンドン市長のサディク・カーン氏は、完全自動運転タクシー（ロボタクシー）の導入によって渋滞が悪化し、伝統的な黒塗りタクシー運転手の職が脅かされるのを防ぐため、台数上限を設けるよう求めました。",
        "subhead": "Concerns over traffic congestion and pedestrian safety prompt calls for strict licensing of autonomous vehicles.",
        "lead_snippet": "London's mayor wants power to control the number of autonomous vehicles permitted to operate in the capital.",
        "summary_points": [
            "自動運転タクシーがロンドン中心部に大量に流入することへの懸念が高まっている。",
            "カーン市長は交通渋滞、歩行者の安全、伝統的タクシー運転手の雇用保護を主張。",
            "新技術の利便性と都市の公共交通秩序の調和に向けたルール作りが求められている。"
        ],
        "image": "https://images.unsplash.com/photo-1549317661-bd32c8ce0db2?w=1000&auto=format&fit=crop&q=80",
        "sentences": [
            {
                "num": 1,
                "en": "The Mayor of London, Sadiq Khan, has urged the government to set a strict limit on the number of driverless robotaxis in the capital.",
                "ja": "ロンドン市長のサディク・カーン氏は、首都における無人ロボタクシーの台数に厳格な上限を設けるよう政府に要請しました。"
            },
            {
                "num": 2,
                "en": "Technology companies hope to launch fleets of autonomous electric vehicles across London over the next few years.",
                "ja": "テクノロジー企業は今後数年間で、ロンドン全域に自動運転電気自動車の大規模フリートを展開することを望んでいます。"
            },
            {
                "num": 3,
                "en": "However, the mayor warned that an uncontrolled influx of self-driving cars could cause severe traffic jams and endanger cyclists.",
                "ja": "しかし市長は、自動運転車の野放図な流入が深刻な交通渋滞を引き起こし、自転車利用者を危険にさらしかねないと警告しました。"
            },
            {
                "num": 4,
                "en": "Traditional black-cab drivers also expressed fear that cheap autonomous services would take away their hard-earned livelihoods.",
                "ja": "伝統的なブラックキャブ（黒塗りタクシー）の運転手たちも、安価な自動運転サービスによって苦労して得た生計が奪われると恐れを表明しました。"
            },
            {
                "num": 5,
                "en": "Transport officials say new regulations must balance modern technological innovation with public safety and fairness.",
                "ja": "交通当局は、新しい規制は現代の技術革新と公共の安全および公平性とのバランスを取る必要があると述べています。"
            }
        ],
        "quiz": [
            {
                "question": "What did London's mayor ask the government to do?",
                "options": [
                    "Put a strict limit on the number of driverless robotaxis.",
                    "Ban all bicycles and buses from the city centre immediately.",
                    "Make all public transport completely free for everyone.",
                    "Paint all private cars bright yellow by the end of the year."
                ],
                "answer": 0,
                "explanation": "本文第1文に「set a strict limit on the number of driverless robotaxis in the capital」とあります。"
            },
            {
                "question": "What is one concern raised about having too many self-driving vehicles?",
                "options": [
                    "They could cause severe traffic jams and endanger cyclists.",
                    "They will consume too much fresh drinking water from rivers.",
                    "They will make loud music play all night in quiet neighborhoods.",
                    "They cannot be driven on paved asphalt roads."
                ],
                "answer": 0,
                "explanation": "本文第3文に「could cause severe traffic jams and endanger cyclists」と述べられています。"
            },
            {
                "question": "Why are traditional black-cab drivers worried about robotaxis?",
                "options": [
                    "Cheap autonomous vehicles could threaten their jobs and livelihoods.",
                    "The government will force taxi drivers to become software engineers.",
                    "Black-cab vehicles will not be allowed to enter airports.",
                    "They will have to share their cars with robots sitting in the front seat."
                ],
                "answer": 0,
                "explanation": "本文第4文に「cheap autonomous services would take away their hard-earned livelihoods」と書かれています。"
            }
        ],
        "vocab": [
            {"word": "robotaxi", "meaning": "ロボタクシー（自動運転タクシー）", "example": "Robotaxis are being tested in several major cities."},
            {"word": "fleet", "meaning": "（車両などの）船団、全保有車両群", "example": "The company operates a large fleet of electric delivery vans."},
            {"word": "influx", "meaning": "流入、殺到", "example": "The sudden influx of tourists crowded the historic streets."},
            {"word": "livelihood", "meaning": "生計、暮らし", "example": "Many fishermen depend on the river for their livelihood."}
        ],
        "dialog": [
            {
                "speaker": "Keita",
                "text": "ロンドン市長が、自動運転ロボタクシーの街中での台数制限を政府に求めたよ。"
            },
            {
                "speaker": "Nanami",
                "text": "自動運転タクシーって便利そうですが、何が問題になっているんですか？"
            },
            {
                "speaker": "Keita",
                "text": "台数が増えすぎると道路が大渋滞するし、伝統的なタクシー運転手の仕事が奪われてしまう心配があるんだ。"
            },
            {
                "speaker": "Nanami",
                "text": "最新技術を取り入れる便利さと、街の安全性や働く人の暮らしを守るバランスが大切なんですね。"
            }
        ]
    }

    # Article 6: chancellor-fails-to-guarantee-minimum-wage-pledge-younger-workers-kuenssberg
    j6 = {
        "slug": "chancellor-fails-to-guarantee-minimum-wage-pledge-younger-workers-kuenssberg",
        "category": "society",
        "date": "2026-11-02",
        "pub_date": "2026-11-02",
        "source_url": "https://www.theguardian.com/politics/2026/nov/01/chancellor-fails-to-guarantee-minimum-wage-pledge-younger-workers-kuenssberg",
        "source_name": "The Guardian",
        "source_media": "The Guardian",
        "source_domain": "theguardian.com",
        "source_attribution": "The Guardian (November 1, 2026)",
        "category_label": "SOCIETY • YOUTH WAGES",
        "title": "UK Chancellor Faces Criticism Over Delayed Equal Minimum Wage for Young Workers",
        "headline_ja": "若年労働者への最低賃金同額化の公約先送りで英財務相に批判",
        "lead_ja": "イギリスのレイチェル・リーブス財務相はテレビ番組で、若者と大人の最低賃金を同額にするという政権公約について、企業の雇用コスト負担を考慮して慎重に段階的導入すると述べ、若者団体から失望の声が上がっています。",
        "subhead": "Young workers express frustration after the government hesitates on immediate wage parity with older adults.",
        "lead_snippet": "The chancellor declined to guarantee a rapid timeline for ending lower minimum wage tiers for 18-to-20-year-olds.",
        "summary_points": [
            "英国では18〜20歳の最低賃金が成人の基準より低く抑えられている。",
            "総選挙で掲げられた同一賃金の即時実現について、財務相は慎重な姿勢を示した。",
            "若年層の生活苦への支援と、企業の採用抑制への警戒との間で議論が白熱している。"
        ],
        "image": "https://images.unsplash.com/photo-1526304640581-d334cdbbf45e?w=1000&auto=format&fit=crop&q=80",
        "sentences": [
            {
                "num": 1,
                "en": "Britain's Chancellor, Rachel Reeves, has faced questions after refusing to promise an immediate end to lower minimum wages for younger staff.",
                "ja": "イギリスのレイチェル・リーブス財務相は、若年労働者向けの低い最低賃金の即時撤廃を約束しなかったことで疑問の声に直面しました。"
            },
            {
                "num": 2,
                "en": "Currently, workers aged eighteen to twenty in the United Kingdom are legally paid less per hour than older colleagues.",
                "ja": "現在、英国では18歳から20歳の労働者は年上の同僚よりも時給が法的に低く設定されています。"
            },
            {
                "num": 3,
                "en": "Ministers had pledged to create a single wage rate for all adults, but business owners warned that quick changes could hurt youth hiring.",
                "ja": "閣僚らは全成人に単一の賃金率を創設すると公約していましたが、企業経営者らは急速な変更は若者の採用を損なうと警告しました。"
            },
            {
                "num": 4,
                "en": "Youth advocacy groups argued that young workers pay the same rent and grocery bills as everyone else and deserve fair pay.",
                "ja": "若者支援団体は、若年労働者も他のみんなと同じ家賃や食費を支払っており、公平な賃金を受け取る価値があると主張しました。"
            },
            {
                "num": 5,
                "en": "The government insisted that it will raise wages gradually to support the economy while protecting business stability.",
                "ja": "政府は、企業の安定を守りつつ経済を支えるため、賃金を段階的に引き上げると主張しました。"
            }
        ],
        "quiz": [
            {
                "question": "What issue caused debate regarding younger workers in the UK?",
                "options": [
                    "They are legally paid a lower minimum wage than older adult workers.",
                    "They are not allowed to attend university lectures after age eighteen.",
                    "They have to work ten hours more per week without any breaks.",
                    "They are banned from opening personal bank accounts in London."
                ],
                "answer": 0,
                "explanation": "本文第2文に「workers aged eighteen to twenty in the United Kingdom are legally paid less per hour than older colleagues」と説明されています。"
            },
            {
                "question": "Why did business owners urge caution regarding an immediate wage increase?",
                "options": [
                    "They worried sudden pay rises might hurt hiring opportunities for youth.",
                    "They wanted to hire only workers who have retired from full-time jobs.",
                    "They planned to shut down all retail shops and work online permanently.",
                    "They wanted to replace money payments with gift coupons."
                ],
                "answer": 0,
                "explanation": "本文第3文に「business owners warned that quick changes could hurt youth hiring」と書かれています。"
            },
            {
                "question": "What is the main argument made by youth advocacy groups?",
                "options": [
                    "Young people pay the same living costs like rent and food, so they deserve fair pay.",
                    "Young workers should only work during school summer holidays.",
                    "Young employees should receive completely free transport everywhere.",
                    "Employers should pay students in foreign currencies instead of pounds."
                ],
                "answer": 0,
                "explanation": "本文第4文に「young workers pay the same rent and grocery bills as everyone else and deserve fair pay」と述べられています。"
            }
        ],
        "vocab": [
            {"word": "minimum wage", "meaning": "最低賃金", "example": "The government raised the national minimum wage this autumn."},
            {"word": "parity", "meaning": "同等、均等", "example": "Campaigners are fighting for wage parity between age groups."},
            {"word": "advocacy", "meaning": "権利擁護、提唱", "example": "She joined a youth advocacy group to help local students."},
            {"word": "gradually", "meaning": "徐々に、段階的に", "example": "The new policy will be implemented gradually over three years."}
        ],
        "dialog": [
            {
                "speaker": "Keita",
                "text": "イギリスで、18〜20歳の最低賃金を大人と同額にする公約が先送りされそうで議論が起きているよ。"
            },
            {
                "speaker": "Nanami",
                "text": "同じ仕事をしているのに、年齢が若いというだけで時給が低く設定されているんですか？"
            },
            {
                "speaker": "Keita",
                "text": "そうなんだ。生活費は大人と同じだから不公平だという声と、急に賃金を上げると企業が若者を雇わなくなるという懸念で揺れているんだよ。"
            },
            {
                "speaker": "Nanami",
                "text": "若者の生活支援と雇用の維持、どちらも大事だからこそ段階的な調整が必要なんですね。"
            }
        ]
    }

    # Write Part 1
    content1 = "# -*- coding: utf-8 -*-\\n\"\"\"Batch 29 Part 1: Articles 1-6 (Junior) Date: 2026-11-02\"\"\"\\n\\nJUNIOR_PART1 = "
    # We will serialize nicely
    with open("news_portal/pipeline/data_batch29_junior_part1.py", "w", encoding="utf-8") as f:
        f.write("# -*- coding: utf-8 -*-\n")
        f.write('"""Batch 29 Part 1: Articles 1-6 (Junior) Date: 2026-11-02"""\n\n')
        f.write("JUNIOR_PART1 = ")
        f.write(json.dumps([j1, j2, j3, j4, j5, j6], ensure_ascii=False, indent=4))
        f.write('\n\n__all__ = ["JUNIOR_PART1"]\n')

    print("Wrote data_batch29_junior_part1.py successfully.")

    # Article 7: investors-take-out-36bn-from-binance-after-record-hack-that-stole-billions
    j7 = {
        "slug": "investors-take-out-36bn-from-binance-after-record-hack-that-stole-billions",
        "category": "world",
        "date": "2026-11-02",
        "pub_date": "2026-11-02",
        "source_url": "https://www.theguardian.com/technology/2026/nov/01/investors-take-out-36bn-from-binance-after-record-hack-that-stole-billions",
        "source_name": "The Guardian",
        "source_media": "The Guardian",
        "source_domain": "theguardian.com",
        "source_attribution": "The Guardian (November 1, 2026)",
        "category_label": "WORLD • CYBERSECURITY",
        "title": "Investors Withdraw Billions from Crypto Exchange Following Major Security Breach",
        "headline_ja": "巨額ハッキング被害を受け、暗号資産取引所から数十億ドルの資金が流出",
        "lead_ja": "世界最大級の暗号資産（仮想通貨）取引所がサイバー攻撃を受け多額のデジタル資産が盗難されたことを受け、利用者が不安から36億ドル（約5,500億円）以上の資金を一斉に引き出しました。",
        "subhead": "A massive cyber-attack shakes digital currency markets as customers rush to secure their deposits.",
        "lead_snippet": "Users moved huge amounts of money away from the platform following a breach of smart contract bridges.",
        "summary_points": [
            "暗号資産取引所のシステムがハッカーに突破され、巨額のトークンが盗まれた。",
            "預金者の不安が急拡大し、短期間で36億ドルを超える出金ラッシュが発生。",
            "デジタル金融におけるサイバーセキュリティ対策と顧客資産の保護が改めて問われている。"
        ],
        "image": "https://images.unsplash.com/photo-1518770660439-4636190af475?w=1000&auto=format&fit=crop&q=80",
        "sentences": [
            {
                "num": 1,
                "en": "Investors pulled more than 3.6 billion dollars out of a leading cryptocurrency platform following a record cyber-attack.",
                "ja": "記録的なサイバー攻撃を受けて、投資家たちは大手暗号資産プラットフォームから36億ドル以上を引き出しました。"
            },
            {
                "num": 2,
                "en": "Clever hackers exploited a software weakness in a blockchain bridge to steal valuable digital tokens.",
                "ja": "巧妙なハッカーたちがブロックチェーン・ブリッジのソフトウェアの弱点を突いて、貴重なデジタルトークンを盗み出しました。"
            },
            {
                "num": 3,
                "en": "Exchange operators quickly suspended deposit and withdrawal services to patch their systems and prevent further losses.",
                "ja": "取引所の運営者は、システムを修正してさらなる損失を防ぐため、入出金サービスを速やかに一時停止しました。"
            },
            {
                "num": 4,
                "en": "Although company leaders assured customers that private savings were safe, worried users rushed to transfer their money.",
                "ja": "企業経営陣は顧客の個人預金は安全だと安心させようとしましたが、不安を感じた利用者たちは急いで資金を移動させました。"
            },
            {
                "num": 5,
                "en": "International regulators stressed that digital financial services must adopt much stronger security protections.",
                "ja": "各国の規制当局は、デジタル金融サービスははるかに強固なセキュリティ保護を採用しなければならないと強調しました。"
            }
        ],
        "quiz": [
            {
                "question": "What caused investors to withdraw over 3.6 billion dollars from the crypto exchange?",
                "options": [
                    "A massive cyber-attack that exploited a software weakness.",
                    "A decision by the platform to charge a fee on every email sent.",
                    "A complete shutdown of the global internet due to solar storms.",
                    "The company decided to convert all digital coins into gold bars."
                ],
                "answer": 0,
                "explanation": "本文第1文および第2文に「following a record cyber-attack」「hackers exploited a software weakness」とある通り、ハッキング被害による不安が原因です。"
            },
            {
                "question": "What action did the exchange take immediately after noticing the hack?",
                "options": [
                    "They temporarily suspended deposit and withdrawal services to patch the system.",
                    "They deleted all user accounts and closed down the business forever.",
                    "They called the police to arrest everyone who owned a computer.",
                    "They lowered the price of electricity across the country."
                ],
                "answer": 0,
                "explanation": "本文第3文に「suspended deposit and withdrawal services to patch their systems」と明記されています。"
            },
            {
                "question": "What did international regulators emphasize after the incident?",
                "options": [
                    "Digital financial systems must enforce much stronger cybersecurity protections.",
                    "People should only use copper coins for shopping in supermarkets.",
                    "Banks must never use computers to manage customer accounts.",
                    "All software engineers should be required to work without salaries."
                ],
                "answer": 0,
                "explanation": "本文第5文に「digital financial services must adopt much stronger security protections」と述べられています。"
            }
        ],
        "vocab": [
            {"word": "cryptocurrency", "meaning": "暗号資産、仮想通貨", "example": "Bitcoin and Ethereum are well-known types of cryptocurrency."},
            {"word": "exploit", "meaning": "〜の弱点を突く、悪用する", "example": "Hackers exploit security bugs to enter computer systems."},
            {"word": "suspend", "meaning": "〜を一時中断・停止する", "example": "The ferry service was suspended because of the stormy sea."},
            {"word": "regulator", "meaning": "規制当局、監督官庁", "example": "Financial regulators ensure that banks treat customers fairly."}
        ],
        "dialog": [
            {
                "speaker": "Keita",
                "text": "暗号資産の大手取引所でハッキング被害が起き、不安になった利用者が巨額の資金を引き出したよ。"
            },
            {
                "speaker": "Nanami",
                "text": "36億ドルって、日本円で5,000億円以上ですよね！そんな大金が動いたんですか？"
            },
            {
                "speaker": "Keita",
                "text": "ブロックチェーンの接続部分の弱点を突かれたんだ。運営側は個人の預金は保証すると発表したけれど、信用が揺らいでしまったね。"
            },
            {
                "speaker": "Nanami",
                "text": "デジタルのお金は送金が手軽な分、サイバー攻撃から守る鉄壁のセキュリティが欠かせないんですね。"
            }
        ]
    }

    # Article 8: uk-willing-to-spend-450m-a-year-on-eu-students-if-it-can-join-made-in-europe-scheme
    j8 = {
        "slug": "uk-willing-to-spend-450m-a-year-on-eu-students-if-it-can-join-made-in-europe-scheme",
        "category": "world",
        "date": "2026-11-02",
        "pub_date": "2026-11-02",
        "source_url": "https://www.theguardian.com/politics/2026/nov/01/uk-willing-to-spend-450m-a-year-on-eu-students-if-it-can-join-made-in-europe-scheme",
        "source_name": "The Guardian",
        "source_media": "The Guardian",
        "source_domain": "theguardian.com",
        "source_attribution": "The Guardian (November 1, 2026)",
        "category_label": "WORLD • EUROPEAN DIPLOMACY",
        "title": "UK Offers £450 Million for European Student Exchanges to Rebuild Ties with EU",
        "headline_ja": "英国、欧州連合との関係修復に向けEU留学生支援に年4億5000万ポンドの拠出を提案",
        "lead_ja": "英国政府は、EUの製造業支援計画への参加を認める見返りとして、ヨーロッパの学生が英国で学びやすくするための支援策に年間4億5000万ポンド（約900億円）を投じる意向を表明しました。",
        "subhead": "Ministers seek access to strategic green-energy funds in exchange for welcoming young EU scholars.",
        "lead_snippet": "The UK is negotiating with Brussels over mutual student exchange and industrial cooperation.",
        "summary_points": [
            "ブレグジット後に対立していた英EU関係を改善するため、英国が大規模な学生支援を提案。",
            "EUからの留学生に対する授業料優遇や奨学金として年4億5,000万ポンドを拠出する計画。",
            "英国の先端製造業やEV産業が欧州の共同基金に参加できる道筋を開く狙いがある。"
        ],
        "image": "https://images.unsplash.com/photo-1523240795612-9a054b0db644?w=1000&auto=format&fit=crop&q=80",
        "sentences": [
            {
                "num": 1,
                "en": "The United Kingdom has offered to spend 450 million pounds a year to support European students studying at British universities.",
                "ja": "英国は、英国の大学で学ぶヨーロッパの学生を支援するために年間4億5000万ポンドを支出することを提案しました。"
            },
            {
                "num": 2,
                "en": "In return, British ministers hope the European Union will let UK companies join a major industrial funding program.",
                "ja": "その見返りとして英国の閣僚らは、欧州連合が英国企業を大規模な産業資金プログラムに参加させることを望んでいます。"
            },
            {
                "num": 3,
                "en": "Since Brexit, high international tuition fees caused the number of EU students in the UK to drop significantly.",
                "ja": "ブレグジット以降、高額な留学生向け授業料が原因で、英国に在籍するEU留学生の数は著しく減少していました。"
            },
            {
                "num": 4,
                "en": "University leaders welcomed the plan, saying international young people enrich university life and scientific research.",
                "ja": "大学の指導者たちはこの計画を歓迎し、国際的な若者たちが大学生活や科学研究を豊かにすると述べました。"
            },
            {
                "num": 5,
                "en": "Diplomats in Brussels and London will hold further discussions to finalize the details of this new partnership.",
                "ja": "ブリュッセルとロンドンの外交官らは、この新たなパートナーシップの詳細を詰めるため、さらなる協議を行う予定です。"
            }
        ],
        "quiz": [
            {
                "question": "What is the UK government offering to European students?",
                "options": [
                    "A £450 million yearly fund to help them study at British universities.",
                    "Free housing in the royal palaces of London for three years.",
                    "An automatic pass on all final school examinations.",
                    "Free flights across the Atlantic Ocean on British airlines."
                ],
                "answer": 0,
                "explanation": "本文第1文に「spend 450 million pounds a year to support European students studying at British universities」とあります。"
            },
            {
                "question": "What does the UK hope to receive in exchange from the European Union?",
                "options": [
                    "Access for UK businesses to participate in a major European industrial scheme.",
                    "Ownership of several famous historical castles in southern France.",
                    "A supply of free olive oil and cheese for all UK citizens.",
                    "A promise to change the official currency of the UK to the euro."
                ],
                "answer": 0,
                "explanation": "本文第2文に「hope the European Union will let UK companies join a major industrial funding program」と書かれています。"
            },
            {
                "question": "Why did university leaders welcome the proposal?",
                "options": [
                    "International students bring diverse energy and help advance scientific research.",
                    "British professors want to teach only in foreign languages.",
                    "Universities plan to cancel all science courses and focus on sports.",
                    "They will no longer need to grade homework papers for students."
                ],
                "answer": 0,
                "explanation": "本文第4文に「international young people enrich university life and scientific research」と述べられています。"
            }
        ],
        "vocab": [
            {"word": "tuition fee", "meaning": "授業料、学費", "example": "Universities use tuition fees to maintain classrooms and labs."},
            {"word": "enrich", "meaning": "〜を豊かにする", "example": "Reading good literature enriches our understanding of the world."},
            {"word": "diplomat", "meaning": "外交官", "example": "Diplomats worked late into the night to negotiate a peace agreement."},
            {"word": "partnership", "meaning": "協力関係、提携", "example": "The two countries built a strong trading partnership."}
        ],
        "dialog": [
            {
                "speaker": "Keita",
                "text": "イギリスがEUからの留学生支援に年4億5000万ポンドを拠出する提案をしたよ。"
            },
            {
                "speaker": "Nanami",
                "text": "ブレグジットでEUとの間に壁ができていましたが、関係を良くしようとしているんですね。"
            },
            {
                "speaker": "Keita",
                "text": "その通り。ヨーロッパの優秀な学生を受け入れつつ、英国企業がEUの産業支援ファンドに参加できるように交渉しているんだ。"
            },
            {
                "speaker": "Nanami",
                "text": "若い世代の学術交流が、国どうしの関係を修復する架け橋になるのは素晴らしいですね。"
            }
        ]
    }

    # Article 9: police-detain-325-people-at-pro-palestine-action-protest-at-us-embassy-in-london
    j9 = {
        "slug": "police-detain-325-people-at-pro-palestine-action-protest-at-us-embassy-in-london",
        "category": "law",
        "date": "2026-11-02",
        "pub_date": "2026-11-02",
        "source_url": "https://www.theguardian.com/uk-news/2026/nov/01/police-detain-325-people-at-pro-palestine-action-protest-at-us-embassy-in-london",
        "source_name": "The Guardian",
        "source_media": "The Guardian",
        "source_domain": "theguardian.com",
        "source_attribution": "The Guardian (November 1, 2026)",
        "category_label": "LAW • PROTEST POLICING",
        "title": "London Police Detain Over 300 Protesters Near US Embassy During Demonstration",
        "headline_ja": "ロンドン警察、米大使館周辺でのデモで抗議者300人以上を一時拘束",
        "lead_ja": "ロンドン南部の米国大使館周辺で行われた親パレスチナの抗議行動において、道路封鎖や警察の指示に従わなかったとして、警察がデモ参加者325人を一時拘束しました。",
        "subhead": "Officers intervene to clear major roadways as activists stage sit-in against arms shipments.",
        "lead_snippet": "Metropolitan Police arrested activists who blocked roads outside the embassy in Nine Elms.",
        "summary_points": [
            "米大使館前の幹線道路でデモ隊が座り込みを行い、交通が長時間遮断された。",
            "警察は公共秩序法に基づき、指定エリアからの移動を拒んだ325人を拘束。",
            "表現やデモの自由と、都市機能の維持・治安確保の境界をめぐり議論が起きている。"
        ],
        "image": "https://images.unsplash.com/photo-1589829545856-d10d557cf95f?w=1000&auto=format&fit=crop&q=80",
        "sentences": [
            {
                "num": 1,
                "en": "Metropolitan police officers in London detained more than three hundred people during a protest outside the United States Embassy.",
                "ja": "ロンドン警視庁の警察官らは、米国大使館の外で行われた抗議デモの最中に300人以上の人々を拘束しました。"
            },
            {
                "num": 2,
                "en": "Activists had gathered on major roads to call for an immediate stop to international arms sales and weapons shipments.",
                "ja": "活動家らは、国際的な武器売却や兵器輸送の即時停止を訴えるため、主要な道路に集まっていました。"
            },
            {
                "num": 3,
                "en": "Police commanded the crowd to move to designated protest spaces, but many participants chose to stage a peaceful sit-in.",
                "ja": "警察は群衆に指定された抗議スペースへ移動するよう命じましたが、多くの参加者は平和的な座り込みを行うことを選びました。"
            },
            {
                "num": 4,
                "en": "Authorities explained that blocking critical highways disrupts ambulances and prevents thousands of citizens from travelling.",
                "ja": "当局は、主要な幹線道路を封鎖することは救急車の運行を妨げ、何千人もの市民の移動を阻害すると説明しました。"
            },
            {
                "num": 5,
                "en": "Civil rights lawyers remarked that citizens have a right to protest, while the legal debate over public order laws continues.",
                "ja": "市民の権利を擁護する弁護士らは、市民には抗議する権利があると指摘し、公共秩序法をめぐる法的議論が続いています。"
            }
        ],
        "quiz": [
            {
                "question": "Why did police detain more than three hundred people near the US Embassy?",
                "options": [
                    "They blocked major roadways and refused to move to designated protest zones.",
                    "They were throwing stones through the glass windows of private shops.",
                    "They were driving cars without valid national driving licences.",
                    "They entered the embassy building without showing passports."
                ],
                "answer": 0,
                "explanation": "本文第1文、第3文、第4文に「blocked roads」「refused to move to designated spaces」「blocking critical highways」とあり、道路封鎖と移動命令拒否が理由です。"
            },
            {
                "question": "What reason did the police give for clearing the roadway?",
                "options": [
                    "Roadblocks disrupt emergency ambulances and stop citizens from moving.",
                    "They needed the road to film a high-budget Hollywood action movie.",
                    "The city council wanted to plant flower gardens in the middle of the street.",
                    "Heavy snow was predicted to cover the entire city by evening."
                ],
                "answer": 0,
                "explanation": "本文第4文に「blocking critical highways disrupts ambulances and prevents thousands of citizens from travelling」と明記されています。"
            },
            {
                "question": "What fundamental debate does this event highlight?",
                "options": [
                    "The balance between democratic protest rights and maintaining public order.",
                    "Whether embassies should be moved far away into remote forests.",
                    "The rule that police officers must never wear yellow protective jackets.",
                    "How to build high-speed trains beneath historic river bridges."
                ],
                "answer": 0,
                "explanation": "本文第5文に「citizens have a right to protest, while the legal debate over public order laws continues」とあり、表現の自由と公共秩序の維持とのバランスが焦点です。"
            }
        ],
        "vocab": [
            {"word": "detain", "meaning": "〜を一時拘束・留置する", "example": "Police detained the suspect for questioning at the station."},
            {"word": "designated", "meaning": "指定された", "example": "Please wait in the designated waiting area until called."},
            {"word": "sit-in", "meaning": "座り込み抗議", "example": "Students organized a peaceful sit-in outside the university hall."},
            {"word": "disrupt", "meaning": "〜を混乱させる、中断させる", "example": "The stormy weather disrupted train services across the country."}
        ],
        "dialog": [
            {
                "speaker": "Keita",
                "text": "ロンドンの米大使館前で道路を塞いで座り込みを行った抗議者300人以上が警察に拘束されたよ。"
            },
            {
                "speaker": "Nanami",
                "text": "平和的な抗議デモでも、道路を塞ぐと拘束されてしまうことがあるんですね。"
            },
            {
                "speaker": "Keita",
                "text": "救急車が通れなくなったり大混乱が起きるのを防ぐため、警察が指定した場所への移動を命じたのに応じなかったからなんだ。"
            },
            {
                "speaker": "Nanami",
                "text": "自分の意見を主張するデモの自由と、周りの市民生活の安全や秩序を守ることの難しさを感じます。"
            }
        ]
    }

    # Article 10: home-secretary-shabana-mahmood-immigration-leave-to-remain-windrush
    j10 = {
        "slug": "home-secretary-shabana-mahmood-immigration-leave-to-remain-windrush",
        "category": "law",
        "date": "2026-11-02",
        "pub_date": "2026-11-02",
        "source_url": "https://www.theguardian.com/uk-news/2026/nov/01/home-secretary-shabana-mahmood-immigration-leave-to-remain-windrush",
        "source_name": "The Guardian",
        "source_media": "The Guardian",
        "source_domain": "theguardian.com",
        "source_attribution": "The Guardian (November 1, 2026)",
        "category_label": "LAW • CITIZENSHIP REFORM",
        "title": "UK Justice Secretary Announces Fairer Citizenship Rules for Windrush Generation",
        "headline_ja": "英司法相、ウィンドラッシュ世代のための公正な在留・市民権ルールを発表",
        "lead_ja": "英国政府は、かつてカリブ海地域から移住し不当に在留資格を剥奪された「ウィンドラッシュ世代」とその家族に対し、無期限在留資格と市民権の取得手続きを大幅に簡素化・迅速化する改革方針を発表しました。",
        "subhead": "Government promises to resolve long-standing immigration injustices with streamlined paperwork.",
        "lead_snippet": "New measures aim to grant permanent residency without costly administrative fees for affected families.",
        "summary_points": [
            "戦後英国の復興を支えたカリブ海系移民が書類不備で不当に扱われた歴史を是正。",
            "シャバナ・マフムード司法相らが、在留資格確認の手続きと補償を迅速化すると表明。",
            "過去の行政ミスによる被害者の尊厳回復と、公平な移民制度の構築を目指す。"
        ],
        "image": "https://images.unsplash.com/photo-1450133064473-71024230f91b?w=1000&auto=format&fit=crop&q=80",
        "sentences": [
            {
                "num": 1,
                "en": "The United Kingdom has unveiled new plans to grant permanent residency and citizenship to victims of the Windrush scandal.",
                "ja": "英国は、ウィンドラッシュ・スキャンダルの被害者に対して永住権と市民権を付与する新たな計画を発表しました。"
            },
            {
                "num": 2,
                "en": "Decades ago, thousands of citizens from Commonwealth countries in the Caribbean arrived to help rebuild Britain after the war.",
                "ja": "数十年前、カリブ海の英連邦諸国から何千人もの市民が、戦後の英国復興を助けるために渡来しました。"
            },
            {
                "num": 3,
                "en": "However, strict immigration paperwork rules introduced later caused many elder residents to wrongfully lose their jobs and homes.",
                "ja": "しかし、後に導入された厳格な移民書類ルールにより、多くの高齢居住者が不当に仕事や住居を失うことになりました。"
            },
            {
                "num": 4,
                "en": "Justice officials announced that difficult document tests and expensive processing fees will now be removed.",
                "ja": "司法当局は、過酷な書類証明手続きや高額な処理手数料が今後は廃止されると発表しました。"
            },
            {
                "num": 5,
                "en": "Community leaders welcomed the changes as an essential step toward restoring dignity and fairness to long-time residents.",
                "ja": "地域コミュニティの指導者らは、長年の居住者に対する尊厳と公平性を回復するための不可欠な一歩として、この変更を歓迎しました。"
            }
        ],
        "quiz": [
            {
                "question": "Who are the Windrush generation in British history?",
                "options": [
                    "People who moved from Caribbean nations to help rebuild Britain after World War II.",
                    "Astronauts who built the first international satellite tracking station.",
                    "Sailors who discovered new islands in the Arctic Ocean in the 18th century.",
                    "Engineers who invented the modern steam engine in northern England."
                ],
                "answer": 0,
                "explanation": "本文第2文に「citizens from Commonwealth countries in the Caribbean arrived to help rebuild Britain after the war」と説明されています。"
            },
            {
                "question": "What injustice did many Windrush residents face in recent years?",
                "options": [
                    "They wrongfully lost jobs and homes due to overly strict immigration paperwork.",
                    "They were forced to learn five foreign languages before retiring.",
                    "They were banned from buying British newspaper subscriptions.",
                    "Their pensions were paid only in antique coins."
                ],
                "answer": 0,
                "explanation": "本文第3文に「strict immigration paperwork rules introduced later caused many elder residents to wrongfully lose their jobs and homes」とあります。"
            },
            {
                "question": "What change will the new government plan introduce?",
                "options": [
                    "Removing difficult document tests and expensive application fees.",
                    "Asking elderly residents to take difficult driving tests again.",
                    "Requiring all historical paperwork to be written by hand in fountain pen.",
                    "Moving all citizenship offices to an island far from London."
                ],
                "answer": 0,
                "explanation": "本文第4文に「difficult document tests and expensive processing fees will now be removed」と明記されています。"
            }
        ],
        "vocab": [
            {"word": "permanent residency", "meaning": "永住権", "example": "He applied for permanent residency after living in the country for ten years."},
            {"word": "commonwealth", "meaning": "連邦、英連邦", "example": "Athletes from many Commonwealth countries compete in the games."},
            {"word": "wrongfully", "meaning": "不当に、誤って", "example": "The court found that he had been wrongfully dismissed from his job."},
            {"word": "dignity", "meaning": "尊厳、気品", "example": "Every human being deserves to be treated with respect and dignity."}
        ],
        "dialog": [
            {
                "speaker": "Keita",
                "text": "戦後の英国を支えた『ウィンドラッシュ世代』の在留資格問題を解決するため、政府が手続きを大幅に見直す方針を発表したよ。"
            },
            {
                "speaker": "Nanami",
                "text": "カリブ海から移住して何十年も真面目に暮らしてきた方たちが、書類の不備だけで不当な扱いを受けていた問題ですね。"
            },
            {
                "speaker": "Keita",
                "text": "その通り。長年暮らしてきた高齢者に対して法外な手数料や証明書類を求めず、公平に市民権や在留資格を認めるんだ。"
            },
            {
                "speaker": "Nanami",
                "text": "国の歴史を支えてくれた人々の尊厳を取り戻すための、とても大切な前進ですね。"
            }
        ]
    }

    # Article 11: bedouin-women-success-arab-parties-israel-election
    j11 = {
        "slug": "bedouin-women-success-arab-parties-israel-election",
        "category": "culture",
        "date": "2026-11-02",
        "pub_date": "2026-11-02",
        "source_url": "https://www.theguardian.com/world/2026/nov/01/bedouin-women-success-arab-parties-israel-election",
        "source_name": "The Guardian",
        "source_media": "The Guardian",
        "source_domain": "theguardian.com",
        "source_attribution": "The Guardian (November 1, 2026)",
        "category_label": "CULTURE • SOCIAL CHANGE",
        "title": "Bedouin Women Lead New Political Wave in Desert Communities",
        "headline_ja": "ベドウィンの女性たち、砂漠の伝統的コミュニティで新たな政治参加の波を主導",
        "lead_ja": "イスラエル南部のネゲブ砂漠に暮らす先住遊牧民ベドウィンの女性たちが、教育向上や医療・インフラ改善を掲げて地方政治で次々と躍進し、伝統的な保守社会に大きな変革をもたらしています。",
        "subhead": "Female candidates break historic cultural barriers to win council seats and champion local public services.",
        "lead_snippet": "In the Negev desert, educated women are transforming local government and inspiring youth.",
        "summary_points": [
            "伝統的に男性優位だったベドウィン社会で、高学歴の女性たちが選挙で次々と当選。",
            "学校教育の改善や道路・水道などの基本インフラ整備を力強く訴え支持を集めた。",
            "伝統文化を尊重しながら女性のリーダーシップを発揮する新しい生き方が広がっている。"
        ],
        "image": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=1000&auto=format&fit=crop&q=80",
        "sentences": [
            {
                "num": 1,
                "en": "In the desert towns of southern Israel, Bedouin women are winning local elections and transforming traditional politics.",
                "ja": "イスラエル南部の砂漠の町で、ベドウィンの女性たちが地方選挙で勝利を収め、伝統的な政治を変革しています。"
            },
            {
                "num": 2,
                "en": "For generations, leadership decisions in these nomadic communities were made exclusively by male clan elders.",
                "ja": "何世代にもわたり、これらの遊牧民コミュニティにおける指導的決定は、男性の氏族の長老たちだけで下されていました。"
            },
            {
                "num": 3,
                "en": "A new generation of educated female candidates campaigned passionately for better local schools, clean water, and healthcare clinics.",
                "ja": "教育を受けた新世代の女性候補者たちは、より良い地元の学校、清潔な水、そして診療所の整備を情熱的に訴えて選挙運動を行いました。"
            },
            {
                "num": 4,
                "en": "Their historic election victories have inspired hundreds of young girls across the region to pursue higher education.",
                "ja": "彼女たちの歴史的な選挙勝利は、この地域の何百人もの少女たちに高等教育を目指す勇気を与えています。"
            },
            {
                "num": 5,
                "en": "Community leaders say these courageous women are showing how traditional customs and modern progress can flourish together.",
                "ja": "地域の指導者らは、これら勇敢な女性たちが、伝統的な慣習と現代の進歩がいかに共存して発展できるかを示していると述べています。"
            }
        ],
        "quiz": [
            {
                "question": "What historic change is taking place among Bedouin communities in southern Israel?",
                "options": [
                    "Educated women are winning local political elections and leading communities.",
                    "Nomadic families have decided to stop herding animals completely.",
                    "All desert towns are being replaced with floating solar power plants.",
                    "Traditional folklore stories are now forbidden from being told to children."
                ],
                "answer": 0,
                "explanation": "本文第1文に「Bedouin women are winning local elections and transforming traditional politics」と明記されています。"
            },
            {
                "question": "What issues did the female candidates focus on during their campaigns?",
                "options": [
                    "Better schools, clean water access, and healthcare clinics.",
                    "Building luxury shopping malls and sports car race tracks.",
                    "Selling desert sand to construction companies abroad.",
                    "Making video games part of compulsory military training."
                ],
                "answer": 0,
                "explanation": "本文第3文に「campaigned passionately for better local schools, clean water, and healthcare clinics」と書かれています。"
            },
            {
                "question": "How have their victories influenced young girls in the region?",
                "options": [
                    "They have inspired hundreds of young girls to pursue higher university education.",
                    "They convinced young girls to avoid using mobile phones and computers.",
                    "They made girls leave their home villages to move to faraway countries.",
                    "They made sports lessons unnecessary in regional primary schools."
                ],
                "answer": 0,
                "explanation": "本文第4文に「inspired hundreds of young girls across the region to pursue higher education」と述べられています。"
            }
        ],
        "vocab": [
            {"word": "nomadic", "meaning": "遊牧の、放浪する", "example": "Nomadic tribes moved across the grasslands following animal herds."},
            {"word": "clan", "meaning": "氏族、一族", "example": "Clan members gathered once a year to celebrate family history."},
            {"word": "candidate", "meaning": "立候補者、候補者", "example": "She was the youngest candidate in the town council election."},
            {"word": "flourish", "meaning": "繁栄する、栄える", "example": "Art and literature flourished during that peaceful century."}
        ],
        "dialog": [
            {
                "speaker": "Keita",
                "text": "砂漠に暮らす伝統的なベドウィン社会で、女性たちが地方選挙に次々と当選して注目を集めているよ。"
            },
            {
                "speaker": "Nanami",
                "text": "昔からの男性中心のしきたりが強い地域で、女性が政治のリーダーになるのはすごい変化ですね！"
            },
            {
                "speaker": "Keita",
                "text": "そうだね。大学で学んだ女性たちが、子どもたちの学校や清潔な水、医療の充実を訴えて多くの支持を集めたんだ。"
            },
            {
                "speaker": "Nanami",
                "text": "伝統的な誇りを守りながら、教育や生活環境を女性の力で良くしていく姿は、次の世代の大きな希望になりますね。"
            }
        ]
    }

    # Article 12: hello-kitty-japanese-spy-show-vivant-china-outcry
    j12 = {
        "slug": "hello-kitty-japanese-spy-show-vivant-china-outcry",
        "category": "entertainment",
        "date": "2026-11-02",
        "pub_date": "2026-11-02",
        "source_url": "https://www.theguardian.com/world/2026/nov/01/hello-kitty-japanese-spy-show-vivant-china-outcry",
        "source_name": "The Guardian",
        "source_media": "The Guardian",
        "source_domain": "theguardian.com",
        "source_attribution": "The Guardian (November 1, 2026)",
        "category_label": "ENTERTAINMENT • POP CULTURE",
        "title": "Japanese TV Drama's Clever Spy Gadgets Spark Viral Debates Across Asia",
        "headline_ja": "日本の人気スパイサスペンスドラマの小道具、アジア各地のSNSで話題沸騰",
        "lead_ja": "日本の大ヒットスパイドラマに登場した可愛らしいキャラクターグッズ型のハイテク秘密スパイ道具が、アジアのSNS上で『意外性と緊張感のギャップが面白い』と大反響を呼んでいます。",
        "subhead": "Fans across social media analyze the unexpected mix of cute pop culture icons and secret intelligence thrillers.",
        "lead_snippet": "A popular Japanese television drama has captured viewers across the region with imaginative gadgetry.",
        "summary_points": [
            "大ヒットテレビドラマで、可愛いキャラクターグッズが秘密通信機器として登場。",
            "アジア各国のネットユーザーの間で、スパイ劇とカワイイ文化の融合が大きな話題に。",
            "日本のポップカルチャーと本格的なサスペンス演出の相乗効果が世界的な注目を集めている。"
        ],
        "image": "https://images.unsplash.com/photo-1511512578047-dfb367046420?w=1000&auto=format&fit=crop&q=80",
        "sentences": [
            {
                "num": 1,
                "en": "A popular Japanese television spy thriller has become an unexpected viral sensation across social media platforms in Asia.",
                "ja": "日本の人気テレビ・スパイサスペンス劇が、アジアのソーシャルメディア上で予想外の大きな話題を呼んでいます。"
            },
            {
                "num": 2,
                "en": "In a climactic episode, secret agents communicated using tiny transmitters hidden inside cute character merchandise.",
                "ja": "クライマックスのエピソードで、秘密工作員たちは可愛いキャラクターグッズの中に隠された極小送信機を使って通信を行いました。"
            },
            {
                "num": 3,
                "en": "Viewers were delighted by the clever contrast between adorable toy figures and intense international espionage.",
                "ja": "視聴者たちは、愛らしい玩具フィギュアと緊迫した国際スパイ活動との間の巧妙な対比に大喜びしました。"
            },
            {
                "num": 4,
                "en": "While some critics debated whether the scenes were realistic, millions of fans shared entertaining clips online.",
                "ja": "一部の批評家はそのシーンが現実的かどうかを議論しましたが、何百万人ものファンが面白い動画クリップをネット上で共有しました。"
            },
            {
                "num": 5,
                "en": "Media scholars noted that combining beloved pop culture symbols with serious drama creates a uniquely engaging viewing experience.",
                "ja": "メディア研究者らは、愛されるポップカルチャーのシンボルと本格的なドラマを組み合わせることで、独自に引き込まれる視聴体験が生まれると指摘しました。"
            }
        ],
        "quiz": [
            {
                "question": "What made the Japanese spy drama go viral across Asian social media?",
                "options": [
                    "The surprising contrast of cute character toys being used as secret spy transmitters.",
                    "The main character decided to sing nursery songs instead of speaking English.",
                    "The entire season was filmed underwater without any lighting equipment.",
                    "All dialogue was replaced with mechanical robot beeps and sound effects."
                ],
                "answer": 0,
                "explanation": "本文第2文および第3文に「secret agents communicated using tiny transmitters hidden inside cute character merchandise」「clever contrast between adorable toy figures and intense international espionage」と書かれています。"
            },
            {
                "question": "How did viewers react to the clever scene?",
                "options": [
                    "They were delighted and shared millions of video clips online.",
                    "They wrote letters asking television channels to delete all episodes.",
                    "They stopped watching television and bought only comic books.",
                    "They demanded that the government ban all secret agent stories."
                ],
                "answer": 0,
                "explanation": "本文第3文および第4文に「Viewers were delighted」「millions of fans shared entertaining clips online」とあります。"
            },
            {
                "question": "What did media scholars say about this storytelling technique?",
                "options": [
                    "Combining familiar pop culture with serious drama creates a unique and engaging experience.",
                    "Spies in real life always wear animal costumes to disguise themselves.",
                    "Television shows should avoid using characters that appeal to children.",
                    "Action dramas are only successful if they are filmed in historical castles."
                ],
                "answer": 0,
                "explanation": "本文第5文に「combining beloved pop culture symbols with serious drama creates a uniquely engaging viewing experience」と述べられています。"
            }
        ],
        "vocab": [
            {"word": "thriller", "meaning": "スリラー、サスペンス作品", "example": "The detective novel was an exciting psychological thriller."},
            {"word": "transmitter", "meaning": "送信機、発信機", "example": "Radio transmitters send signals across hundreds of miles."},
            {"word": "espionage", "meaning": "スパイ活動、諜報活動", "example": "The cold war era was marked by intense international espionage."},
            {"word": "engaging", "meaning": "魅力的な、人を引きつける", "example": "Her speech was so engaging that the entire audience listened closely."}
        ],
        "dialog": [
            {
                "speaker": "Keita",
                "text": "日本の大人気スパイドラマで、可愛いキャラクターグッズが秘密のスパイ道具として登場して海外でも大バズりしているよ。"
            },
            {
                "speaker": "Nanami",
                "text": "シリアスなスパイの世界に可愛いマスコットが登場するなんて、ギャップが面白すぎますね！"
            },
            {
                "speaker": "Keita",
                "text": "そうなんだ。日本が誇る『カワイイ文化』と骨太なサスペンス演出が融合して、アジア中のSNSで動画が拡散されているんだ。"
            },
            {
                "speaker": "Nanami",
                "text": "日本のポップカルチャーの魅力とドラマのクオリティの高さが、世界中のファンの心を掴んでいるんですね！"
            }
        ]
    }

    with open("news_portal/pipeline/data_batch29_junior_part2.py", "w", encoding="utf-8") as f:
        f.write("# -*- coding: utf-8 -*-\n")
        f.write('"""Batch 29 Part 2: Articles 7-12 (Junior) Date: 2026-11-02"""\n\n')
        f.write("JUNIOR_PART2 = ")
        f.write(json.dumps([j7, j8, j9, j10, j11, j12], ensure_ascii=False, indent=4))
        f.write('\n\n__all__ = ["JUNIOR_PART2"]\n')

    print("Wrote data_batch29_junior_part2.py successfully.")

if __name__ == "__main__":
    write_junior_files()
