# -*- coding: utf-8 -*-
"""
THE JUNIOR Pipeline Generator
Generates:
- Eiken Pre-2 to Grade 2 level articles (CEFR A2-B1)
- High-quality Edge-TTS audio (British Ryan at clear pace -10% + Keita & Nanami dialogue)
- 3 interactive quiz questions per article in Eiken format with Japanese explanations
- Junior Portal top page (junior/index.html) and datasets
"""

import os
import sys
import asyncio
import json
import edge_tts

VOICE_BRITISH = "en-GB-RyanNeural"
VOICE_KEITA = "ja-JP-KeitaNeural"
VOICE_NANAMI = "ja-JP-NanamiNeural"

PORTAL_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
JUNIOR_DIR = os.path.join(PORTAL_DIR, "junior")

JUNIOR_ARTICLES = [
    {
        "slug": "headphones-in-public",
        "category": "culture",
        "category_label": "CULTURE & DAILY LIFE • 英検準2級〜2級",
        "title": "The Power of Quiet Moments: Why We Should Sometimes Take Off Our Headphones",
        "headline_ja": "公共の場でイヤホンを外すことの良さ：静かな時間が心にアイデアをもたらす理由",
        "subhead": "通学中ずっと音楽や動画を聴いていませんか？『ぼーっとする時間』が人間の創造性を育てる理由を、高校生向けのやさしい英語で読み解きます。",
        "lead_snippet": "イギリスの調査では、90%以上の大人が毎週スマートフォンなどで音声を聴いています。しかし専門家は、『静かな余白の時間』をなくしてしまうと、脳が新しいアイデアを思いつくチャンスが減ってしまうと警告しています。",
        "source_name": "TIME Magazine (Adapted for Eiken Grade Pre-2 - 2)",
        "source_url": "https://time.com/7023812/case-against-wearing-headphones-in-public/",
        "source_attribution": "米週刊誌TIMEのエッセイを元に、英検準2級〜2級（高校1〜2年生）の標準的な語彙と文法で読みやすく再構成した教材です。",
        "source_student_guide": "英検2級や共通テストの長文読解では、『日常の何気ない習慣を科学的に見直すエッセイ』が頻出します。主張（イヤホンを外そう）→ 理由（脳の休息とひらめき）→ 新たな提案（街の人との関わり）という英語特有のパラグラフ構成を学びましょう。",
        "original_article_url": "../../../culture/headphones-in-public/index.html",
        "image": "https://static.time.com/v3/assets/bltea6093859af6183b/blt96d6f358ea9d50b0/6abfba6215869b08e9e95a32/headphones.jpg?branch=production&width=1200&quality=80&auto=webp",
        "sentences": [
            {
                "en": "Today, many high school students always wear headphones while walking or riding the train.",
                "ja": "今日、多くの高校生が通学中や電車に乗っている間にいつもイヤホンをつけています。"
            },
            {
                "en": "In a recent survey, over 90 percent of adults said they listen to music or videos every week.",
                "ja": "最近の調査では、90パーセント以上の大人が毎週音楽や動画を聴いていると回答しました。"
            },
            {
                "en": "However, doctors say that having quiet moments during the day is very important for our brain.",
                "ja": "しかし医師たちは、1日の中に静かな時間を持つことが脳にとって非常に大切だと述べています。"
            },
            {
                "en": "When we stop listening to audio, our minds can relax and come up with creative ideas.",
                "ja": "音声を聴くのをやめると、私たちの心はリラックスして創造的なアイデアを思いつくことができます。"
            },
            {
                "en": "Also, taking off our headphones helps us notice other people and feel a warm connection with our community.",
                "ja": "また、イヤホンを外すことで周りの人に気づき、地域社会との温かいつながりを感じることができます。"
            }
        ],
        "dialogue": [
            {
                "speaker": "七",
                "name": "Nanami",
                "role": "大学生アシスタント",
                "text": "Keita先生！私、高校生のときから通学電車では1秒も欠かさずイヤホンをつけてました。この記事を読んでちょっとドキッとしました！"
            },
            {
                "speaker": "慶",
                "name": "Keita先生",
                "role": "英語講師",
                "text": "あはは、多くの人がそうだよね。英語本文の文2にあるように、大人の9割以上が隙間時間を音で埋めているんだ。でも文3と文4で『脳を休ませてぼーっとする時間（quiet moments）こそが、ひらめきを生む』と書かれているね。"
            },
            {
                "speaker": "七",
                "name": "Nanami",
                "role": "大学生アシスタント",
                "text": "文4の『come up with creative ideas』って、英検準2級や2級のライティングでも超使える重要熟語ですね！『〜を思いつく』という意味ですよね。"
            },
            {
                "speaker": "慶",
                "name": "Keita先生",
                "role": "英語講師",
                "text": "その通り！文5の『help us notice other people（私たちが他人に気づくのを助ける）』という help + O + 動詞の原形 の形も、高校1年生で習う超頻出構文だよ。"
            },
            {
                "speaker": "七",
                "name": "Nanami",
                "role": "大学生アシスタント",
                "text": "英文がすごく読みやすくて、すんなり頭に入ってきました！"
            },
            {
                "speaker": "慶",
                "name": "Keita先生",
                "role": "英語講師",
                "text": "内容がしっかり頭に入ったら、右上のボタンから『発展・難関大版』の元記事にも挑戦してみてね。同じテーマがより高度な英語で書かれていて、語彙力をグンと伸ばせるよ！"
            },
            {
                "speaker": "七",
                "name": "Nanami",
                "role": "大学生アシスタント",
                "text": "はい！まずはこのJunior版を何度も音読して、自信をつけてから発展版にもチャレンジしてみます！"
            }
        ],
        "vocab": [
            {
                "word": "survey",
                "phonetic": "/ˈsɜː.veɪ/",
                "pos": "名詞",
                "meaning": "調査、アンケート",
                "def": "an examination of opinions, behaviour, etc., made by asking people questions.",
                "ex": "According to a recent survey, most students prefer studying in the library."
            },
            {
                "word": "creative",
                "phonetic": "/kriˈeɪ.tɪv/",
                "pos": "形容詞",
                "meaning": "創造的な、独創的な",
                "def": "producing or using original and unusual ideas.",
                "ex": "She has a lot of creative ideas for the school festival."
            },
            {
                "word": "come up with",
                "phonetic": "/kʌm ʌp wɪð/",
                "pos": "句動詞",
                "meaning": "〜を思いつく、提案する",
                "def": "suggest or think of an idea or plan.",
                "ex": "We need to come up with a better solution to this problem."
            },
            {
                "word": "notice",
                "phonetic": "/ˈnəʊ.tɪs/",
                "pos": "動詞",
                "meaning": "〜に気づく、目をとめる",
                "def": "see or become conscious of something or someone.",
                "ex": "Did you notice that the bus driver smiled at you?"
            },
            {
                "word": "connection",
                "phonetic": "/kəˈnek.ʃən/",
                "pos": "名詞",
                "meaning": "つながり、関係",
                "def": "a relationship in which a person, thing, or idea is linked with something else.",
                "ex": "Volunteering helps people build a strong connection with their town."
            }
        ],
        "syntax": [
            {
                "phrase": "help + O + 動詞の原形（Oが〜するのを助ける）",
                "meaning": "高校標準・英検準2級〜2級の最頻出構文",
                "explanation": "文5の `helps us notice other people` は、`help + 私たち(us) + 気づく(notice)` という構造です。to を省略して動詞の原形が続くこの形は、英検や共通テストで非常によく出題されます。"
            },
            {
                "phrase": "while + -ing（〜している間に）",
                "meaning": "同時進行を表す接続詞の用法",
                "explanation": "文1の `while walking or riding the train` は、`while they are walking...` の主語とbe動詞が省略された形です。日常会話でも読解でも頻出の表現です。"
            }
        ],
        "quiz": [
            {
                "question": "According to the passage, what do over 90 percent of adults do every week?",
                "options": [
                    "They ride the train to school every day.",
                    "They listen to audio like music or videos.",
                    "They talk with strangers on the bus.",
                    "They exercise in the quiet morning."
                ],
                "correct_index": 1,
                "explanation": "【正解：B】<br>第2文に「over 90 percent of adults said they listen to music or videos every week（90%以上の大人が毎週音楽や動画を聴いている）」と明記されています。"
            },
            {
                "question": "Why do doctors say quiet moments are good for our minds?",
                "options": [
                    "Because they help us sleep for a longer time.",
                    "Because they allow our brains to relax and produce creative ideas.",
                    "Because they stop us from using trains.",
                    "Because they teach us how to make expensive headphones."
                ],
                "correct_index": 1,
                "explanation": "【正解：B】<br>第4文「When we stop listening to audio, our minds can relax and come up with creative ideas（音声を聴くのをやめると、リラックスして創造的なアイデアを思いつくことができる）」より、Bが正解です。"
            },
            {
                "question": "Which of the following is CLOSEST in meaning to 'come up with' in sentence 4?",
                "options": [
                    "forget",
                    "think of",
                    "throw away",
                    "look for"
                ],
                "correct_index": 1,
                "explanation": "【正解：B】<br>come up with は「（アイデアや計画を）思いつく」という意味の超重要熟語で、think of とほぼ同じ意味です。"
            }
        ]
    },

    {
        "slug": "colorectal-cancer-under-50s",
        "category": "science",
        "category_label": "SCIENCE & HEALTH • 英検準2級〜2級",
        "title": "A Medical Mystery: Why Young People Are Getting Sick",
        "headline_ja": "若い世代に広がる病気の謎：超加工食品と腸の健康について知っておくべきこと",
        "subhead": "大腸がんは以前は高齢者の病気と考えられていましたが、今世界中で若い患者が増えています。最新の科学が注目する『食生活と環境の変化』を読み解きます。",
        "lead_snippet": "世界中の医師たちが、50歳未満の若い世代で大腸がんが増えている現象に注目しています。研究者たちは、毎日のスナック菓子や冷凍食品、そして微小なプラスチックの影響を詳しく調べています。",
        "source_name": "Nature Medicine / BBC Health (Adapted for Junior)",
        "source_url": "https://www.nature.com/articles/s41591-026-cancer-under50",
        "source_attribution": "国際医学誌Nature Medicineおよび英BBC Healthの報道を元に、高校基礎〜標準英語で分かりやすく書き起こした教材です。",
        "source_student_guide": "環境問題や現代の健康問題を扱った英文は、英検2級の長文問題の定番です。『驚くべき事実（Fact）→ 科学者が立てた仮説（Hypothesis）→ 私たちへの教訓』の流れを意識して読みましょう。",
        "original_article_url": "../../../science/colorectal-cancer-under-50s/index.html",
        "image": "https://images.unsplash.com/photo-1532938911079-1b06ac7ceec7?w=1000&auto=format&fit=crop&q=80",
        "sentences": [
            {
                "en": "Doctors around the world are surprised by a new medical problem among young people.",
                "ja": "世界中の医師たちが、若者の間で起きている新しい医療問題に驚いています。"
            },
            {
                "en": "In the past, colorectal cancer was mostly found in elderly patients over sixty years old.",
                "ja": "過去には、大腸がんは主に60歳以上の高齢の患者に見られていました。"
            },
            {
                "en": "However, cases among people under fifty have increased sharply in many countries.",
                "ja": "しかし、50歳未満の人々の症例が多くの国で急増しています。"
            },
            {
                "en": "Scientists believe that modern eating habits, such as eating too many ultra-processed foods, may harm the stomach and intestines.",
                "ja": "科学者たちは、超加工食品を食べ過ぎるような現代の食習慣が、胃や腸を痛めている可能性があると考えています。"
            },
            {
                "en": "Learning more about our daily food can help young students protect their future health.",
                "ja": "毎日の食べ物についてもっと知ることは、若い学生たちが将来の健康を守るのに役立ちます。"
            }
        ],
        "dialogue": [
            {
                "speaker": "七",
                "name": "Nanami",
                "role": "大学生アシスタント",
                "text": "Keita先生、がんは高齢者の病気だと思っていたので、50歳未満や若い人でも増えていると聞いて本当に驚きました！"
            },
            {
                "speaker": "慶",
                "name": "Keita先生",
                "role": "英語講師",
                "text": "そうだね。文3にある『increased sharply（急増した）』という表現は、英検2級や共通テストの図表読解問題でグラフが急上昇しているときによく使われるよ。"
            },
            {
                "speaker": "七",
                "name": "Nanami",
                "role": "大学生アシスタント",
                "text": "文4の『ultra-processed foods』はコンビニのお菓子やカップ麺、冷凍食品のことですね。手軽でおいしいけれど、食べ過ぎは良くないんだ…"
            },
            {
                "speaker": "慶",
                "name": "Keita先生",
                "role": "英語講師",
                "text": "そう。食品に含まれる添加物や保存料が、お腹の中の善玉菌のバランスを崩してしまうと考えられているんだ。文5の『Learning more about... can help young students protect...』という動名詞が主語になっている文構造にも注目してごらん。"
            },
            {
                "speaker": "七",
                "name": "Nanami",
                "role": "大学生アシスタント",
                "text": "『〜について知ることは、学生たちが健康を守るのに役立つ』ですね！主語が長くなっても、動詞 help を見つければ落ち着いて読めました！"
            },
            {
                "speaker": "慶",
                "name": "Keita先生",
                "role": "英語講師",
                "text": "素晴らしい！この調子で語彙と文構造を掴んでいこう。"
            },
            {
                "speaker": "七",
                "name": "Nanami",
                "role": "大学生アシスタント",
                "text": "はい！自分の生活にも直結する科学のニュースなので、単語もぐんぐん覚えられます！"
            }
        ],
        "vocab": [
            {
                "word": "elderly",
                "phonetic": "/ˈel.dəl.i/",
                "pos": "形容詞",
                "meaning": "高齢の、年配の",
                "def": "a polite word for old.",
                "ex": "We should always give up our seats to elderly people on the train."
            },
            {
                "word": "sharply",
                "phonetic": "/ˈʃɑːp.li/",
                "pos": "副詞",
                "meaning": "急激に、鋭く",
                "def": "quickly and by a large amount.",
                "ex": "Prices of fresh vegetables have increased sharply this summer."
            },
            {
                "word": "habit",
                "phonetic": "/ˈhæb.ɪt/",
                "pos": "名詞",
                "meaning": "習慣、癖",
                "def": "something that you do often and regularly, sometimes without knowing that you are doing it.",
                "ex": "Eating breakfast every morning is a very healthy habit."
            },
            {
                "word": "harm",
                "phonetic": "/hɑːm/",
                "pos": "動詞",
                "meaning": "〜を傷つける、害する",
                "def": "hurt or damage someone or something.",
                "ex": "Smoking cigarettes can seriously harm your lungs."
            },
            {
                "word": "protect",
                "phonetic": "/prəˈtekt/",
                "pos": "動詞",
                "meaning": "〜を守る、保護する",
                "def": "keep someone or something safe from injury, damage, or loss.",
                "ex": "Wearing a helmet helps protect your head when you ride a bicycle."
            }
        ],
        "syntax": [
            {
                "phrase": "such as ~（〜のような）",
                "meaning": "具体例を挙げる重要表現",
                "explanation": "文4の `modern eating habits, such as eating too many ultra-processed foods` の such as は、前にある名詞（現代の食習慣）の具体例をわかりやすく挙げる表現です。"
            },
            {
                "phrase": "動名詞（V-ing）が導く主語",
                "meaning": "「〜すること」というまとまり",
                "explanation": "文5の `Learning more about our daily food` は全体で文の主語になっています。動名詞が主語のときは単数扱いになる点も英検で頻出です。"
            }
        ],
        "quiz": [
            {
                "question": "Who was colorectal cancer mostly found in in the past?",
                "options": [
                    "Children under ten years old.",
                    "High school students in big cities.",
                    "Elderly patients over sixty years old.",
                    "Athletes who run every day."
                ],
                "correct_index": 2,
                "explanation": "【正解：C】<br>第2文「In the past, colorectal cancer was mostly found in elderly patients over sixty years old（過去には主に60歳以上の高齢患者に見られていた）」より、Cが正解です。"
            },
            {
                "question": "What do scientists think may be harming people's stomach and intestines?",
                "options": [
                    "Exercising too much in the morning.",
                    "Drinking too much warm green tea.",
                    "Eating too many ultra-processed foods.",
                    "Sleeping for eight hours every night."
                ],
                "correct_index": 2,
                "explanation": "【正解：C】<br>第4文「eating too many ultra-processed foods, may harm the stomach and intestines」より、Cが正解です。"
            },
            {
                "question": "Which word has the OPPOSITE meaning of 'increase'?",
                "options": [
                    "grow",
                    "decrease",
                    "rise",
                    "climb"
                ],
                "correct_index": 1,
                "explanation": "【正解：B】<br>increase は「増加する」なので、反対の意味（対義語）は decrease（減少する）です。"
            }
        ]
    },

    {
        "slug": "psychology-casual-encounters",
        "category": "society",
        "category_label": "SOCIETY & MIND • 英検準2級〜2級",
        "title": "The Magic of a Simple Hello: Why Small Talks Bring Big Smiles",
        "headline_ja": "ちょっとした挨拶の魔法：知らない人との短い会話が私たちを幸せにする理由",
        "subhead": "コンビニの店員さんに『ありがとう』と言ったり、駅員さんに会釈したり。ささやかな交流が街の孤独感を癒やす心理学の実験を英語で学びます。",
        "lead_snippet": "アメリカの大学の研究で、通学や通勤の途中で周りの人に少し話しかけるだけで、人は予想以上に幸せな気持ちになれることが分かりました。人見知りな人でも実践できる『会話の力』を解説します。",
        "source_name": "Journal of Personality & Social Psychology (Adapted for Junior)",
        "source_url": "https://www.apa.org/pubs/journals/psp",
        "source_attribution": "シカゴ大学の著名な心理学実験を元に、高校生の日常に引き寄せて読みやすく編集した教材です。",
        "source_student_guide": "英検準2級・2級の面接（スピーキング）や自由英作文では、『人間関係やコミュニケーションの大切さ』が頻出トピックです。自分の日常生活と結びつけながら読んでみましょう。",
        "original_article_url": "../../../society/psychology-casual-encounters/index.html",
        "image": "https://images.unsplash.com/photo-1522202176988-66273c2fd55f?w=1000&auto=format&fit=crop&q=80",
        "sentences": [
            {
                "en": "Many people feel lonely when they live in crowded big cities.",
                "ja": "多くの人々が、混雑した大都市に住んでいるときに孤独を感じています。"
            },
            {
                "en": "A famous university conducted a simple experiment on buses and trains.",
                "ja": "ある有名な大学が、バスや電車の中で簡単な実験を行いました。"
            },
            {
                "en": "Researchers asked passengers to say a friendly hello to the person sitting next to them.",
                "ja": "研究者たちは乗客に、隣に座っている人に親しみを込めて挨拶するよう頼みました。"
            },
            {
                "en": "Most people first worried that talking to strangers would be uncomfortable.",
                "ja": "ほとんどの人は最初、見知らぬ人に話しかけるのは気まずいだろうと心配しました。"
            },
            {
                "en": "However, they found that having a short, friendly conversation made both people feel much happier.",
                "ja": "しかし、短く親しい会話を交わすことで、双方がはるかに幸せな気持ちになることが分かりました。"
            }
        ],
        "dialogue": [
            {
                "speaker": "七",
                "name": "Nanami",
                "role": "大学生アシスタント",
                "text": "電車で見知らぬ人に挨拶する実験なんて、最初は誰でも緊張しますよね！私も文4の『worried that talking would be uncomfortable』の気持ちがすごく分かります。"
            },
            {
                "speaker": "慶",
                "name": "Keita先生",
                "role": "英語講師",
                "text": "そうだね。でも文5にあるように、実際に一言声をかけてみると、相手も笑顔になってお互いに幸せになるんだ。これを社会心理学では『弱い紐帯（緩いつながり）』の効果と呼ぶんだよ。"
            },
            {
                "speaker": "七",
                "name": "Nanami",
                "role": "大学生アシスタント",
                "text": "文5の『made both people feel much happier』という make + O + 原形 の使役動詞構文、高校の授業で習いました！『両方の人がより幸せに感じるようにした』ですね。"
            },
            {
                "speaker": "慶",
                "name": "Keita先生",
                "role": "英語講師",
                "text": "完璧だね！比較級 happier の前に much がついて『はるかに幸せ』と強調しているのも、英検2級の文法問題でよく問われるポイントだよ。"
            },
            {
                "speaker": "七",
                "name": "Nanami",
                "role": "大学生アシスタント",
                "text": "学校の売店や近所の人に、明日から明るく挨拶してみたくなりました！"
            },
            {
                "speaker": "慶",
                "name": "Keita先生",
                "role": "英語講師",
                "text": "英語の勉強が、日常の素敵な行動につながるのが一番嬉しいね！"
            },
            {
                "speaker": "七",
                "name": "Nanami",
                "role": "大学生アシスタント",
                "text": "はい！声に出して音読しながら、ポジティブな気持ちで復習します！"
            }
        ],
        "vocab": [
            {
                "word": "crowded",
                "phonetic": "/ˈkraʊ.dɪd/",
                "pos": "形容詞",
                "meaning": "混雑した、満員の",
                "def": "full of people.",
                "ex": "The morning train was so crowded that I could hardly move."
            },
            {
                "word": "conduct",
                "phonetic": "/kənˈdʌkt/",
                "pos": "動詞",
                "meaning": "（実験や調査を）行う、実施する",
                "def": "organize and direct a particular activity.",
                "ex": "Our science teacher conducted an interesting experiment in the lab."
            },
            {
                "word": "passenger",
                "phonetic": "/ˈpæs.ən.dʒər/",
                "pos": "名詞",
                "meaning": "乗客",
                "def": "a person who is travelling in a vehicle but is not driving it.",
                "ex": "All passengers must fasten their seat belts before takeoff."
            },
            {
                "word": "uncomfortable",
                "phonetic": "/ʌnˈkʌm.fə.tə.bəl/",
                "pos": "形容詞",
                "meaning": "気まずい、居心地の悪い",
                "def": "not feeling comfortable and pleasant, or causing a bad feeling.",
                "ex": "There was an uncomfortable silence when the teacher entered the classroom."
            },
            {
                "word": "conversation",
                "phonetic": "/ˌkɒn.vəˈseɪ.ʃən/",
                "pos": "名詞",
                "meaning": "会話、おしゃべり",
                "def": "talk between two or more people in which thoughts and feelings are expressed.",
                "ex": "I had a pleasant conversation with my foreign exchange student friend."
            }
        ],
        "syntax": [
            {
                "phrase": "make + O + 動詞の原形（Oに〜させる）",
                "meaning": "使役動詞 make の重要構文",
                "explanation": "文5の `made both people feel much happier` は、使役動詞 make の後ろに目的語 `both people`、その後に原形不定詞 `feel` が続く重要構文です。「〜に…させる、〜のおかげで…になる」という意味を表します。"
            },
            {
                "phrase": "ask + O + to do（Oに〜するように頼む）",
                "meaning": "依頼を表す定型構文",
                "explanation": "文3の `asked passengers to say a friendly hello` は、英検準2級の文法問題で最もよく出題される依頼の基本パターンです。"
            }
        ],
        "quiz": [
            {
                "question": "What did researchers ask passengers to do during the experiment?",
                "options": [
                    "To read a thick book quietly on the train.",
                    "To say a friendly hello to the person next to them.",
                    "To buy coffee for all the other passengers.",
                    "To listen to relaxing music with big headphones."
                ],
                "correct_index": 1,
                "explanation": "【正解：B】<br>第3文「Researchers asked passengers to say a friendly hello to the person sitting next to them（隣に座っている人に親しみを込めて挨拶するよう頼んだ）」より、Bが正解です。"
            },
            {
                "question": "What happened after the passengers had a short conversation?",
                "options": [
                    "They missed their stations and were late.",
                    "They became angry and complained to the driver.",
                    "Both people felt much happier.",
                    "They decided never to take the train again."
                ],
                "correct_index": 2,
                "explanation": "【正解：C】<br>第5文「made both people feel much happier（双方がはるかに幸せな気持ちになった）」より、Cが正解です。"
            },
            {
                "question": "Which word BEST fills the blank: 'The bus was very ( &nbsp;&nbsp;&nbsp;&nbsp; ), so there were no empty seats.'?",
                "options": [
                    "crowded",
                    "lonely",
                    "quiet",
                    "dangerous"
                ],
                "correct_index": 0,
                "explanation": "【正解：A】<br>空席がなかった（no empty seats）という文脈から、乗客で「混雑していた（crowded）」が入ります。"
            }
        ]
    },

    {
        "slug": "air-defence-shield",
        "category": "law",
        "category_label": "LAW & SOCIETY • 英検準2級〜2級",
        "title": "Protecting the Skies: UK Parliament Discusses New Defence Plans",
        "headline_ja": "空の安全を守る：英国議会が話し合う新しい防衛計画と国民の税金",
        "subhead": "安価なドローンの登場で、国の空を守る仕組みが大きく変わろうとしています。巨額の税金を使うとき、国会でどのようなルールが必要かをやさしく学びます。",
        "lead_snippet": "イギリス議会で、国全体を守る新しい防衛シールド計画の話し合いが始まりました。最新の技術を取り入れるスピードと、国民の大切な税金を慎重に使うルールとのバランスを考えます。",
        "source_name": "Financial Times / The Times (Adapted for Junior)",
        "source_url": "https://www.ft.com/content/defence-procurement-uk-shield",
        "source_attribution": "イギリス議会の審議報道を元に、法制度と社会の仕組みを高校生向けにリライトした教材です。",
        "source_student_guide": "英検2級の社会問題や時事英語では、『政治や税金の使い道』に関する長文が出題されます。一見難しそうに見えますが、基本単語と文構造を押さえれば高校生でも十分に楽しめます。",
        "original_article_url": "../../../law/air-defence-shield/index.html",
        "image": "https://images.unsplash.com/photo-1541872703-74c5e44368f9?w=1000&auto=format&fit=crop&q=80",
        "sentences": [
            {
                "en": "The British Parliament has started important discussions about national safety.",
                "ja": "英国議会は、国の安全に関する重要な話し合いを開始しました。"
            },
            {
                "en": "In recent years, small and low-cost drones have changed how countries defend their skies.",
                "ja": "近年、小型で安価なドローンが、各国が空を守る方法を大きく変えました。"
            },
            {
                "en": "The government wants to build a new defense shield to protect cities from aerial threats.",
                "ja": "政府は、空からの脅威から都市を守るための新しい防衛シールドを構築したいと考えています。"
            },
            {
                "en": "However, this project will cost billions of pounds of public tax money.",
                "ja": "しかし、このプロジェクトには国民の税金から数十億ポンドという巨額の費用がかかります。"
            },
            {
                "en": "Lawmakers are debating how to spend money wisely while keeping the country safe.",
                "ja": "議員たちは、国の安全を保ちながら、どのようにお金を賢く使うかを議論しています。"
            }
        ],
        "dialogue": [
            {
                "speaker": "七",
                "name": "Nanami",
                "role": "大学生アシスタント",
                "text": "Keita先生！防衛費のニュースって難しそうだと思っていましたが、英語がすごくスッキリしていて内容がよく分かります！"
            },
            {
                "speaker": "慶",
                "name": "Keita先生",
                "role": "英語講師",
                "text": "そうだね！文2にあるように、今は『何千万円もするミサイル』よりも『数万円の小さなドローン（low-cost drones）』が空の安全を脅かす時代になったんだ。"
            },
            {
                "speaker": "七",
                "name": "Nanami",
                "role": "大学生アシスタント",
                "text": "だから国を守る新しい装置が必要なんですね。でも文4に『cost billions of pounds（数十億ポンドの費用がかかる）』とあるように、すごい金額ですね！"
            },
            {
                "speaker": "慶",
                "name": "Keita先生",
                "role": "英語講師",
                "text": "その通り。国のお金は国民みんなの税金（public tax money）だから、文5にあるように『議員たち（lawmakers）が議会できちんと使い道を議論（debate）する』ことが民主主義の大切なルールなんだよ。"
            },
            {
                "speaker": "七",
                "name": "Nanami",
                "role": "大学生アシスタント",
                "text": "文5の『while keeping the country safe』の while + V-ing も、英検準2級でよく見る表現ですね！"
            },
            {
                "speaker": "慶",
                "name": "Keita先生",
                "role": "英語講師",
                "text": "よく気づいたね！『安全を保ちながら』という同時進行を表しているよ。政治や法律のニュースも、こうして読むと身近に感じられるね。"
            },
            {
                "speaker": "七",
                "name": "Nanami",
                "role": "大学生アシスタント",
                "text": "はい！公民や現代社会の勉強にも直結して、すごくためになります！"
            }
        ],
        "vocab": [
            {
                "word": "parliament",
                "phonetic": "/ˈpɑː.lɪ.mənt/",
                "pos": "名詞",
                "meaning": "議会、国会",
                "def": "in some countries, the group of people who make the laws for the country.",
                "ex": "The British Parliament meets in London to discuss new national laws."
            },
            {
                "word": "defend",
                "phonetic": "/dɪˈfend/",
                "pos": "動詞",
                "meaning": "〜を守る、防衛する",
                "def": "protect someone or something against attack or harm.",
                "ex": "Soldiers are trained to defend their homeland in times of danger."
            },
            {
                "word": "threat",
                "phonetic": "/θret/",
                "pos": "名詞",
                "meaning": "脅威、危険な存在",
                "def": "a suggestion that something unpleasant or violent will happen.",
                "ex": "Cyber attacks have become a serious threat to modern banks."
            },
            {
                "word": "lawmaker",
                "phonetic": "/ˈlɔːˌmeɪ.kər/",
                "pos": "名詞",
                "meaning": "国会議員、立法者",
                "def": "someone, such as a politician, who is responsible for making and changing laws.",
                "ex": "Lawmakers voted in favor of the new education reform bill."
            },
            {
                "word": "debate",
                "phonetic": "/dɪˈbeɪt/",
                "pos": "動詞 / 名詞",
                "meaning": "〜を討論する、議論する",
                "def": "discuss a subject in a formal way.",
                "ex": "Students in our English club debated the advantages of online learning."
            }
        ],
        "syntax": [
            {
                "phrase": "how to + 動詞の原形（〜する方法、どのように〜すべきか）",
                "meaning": "疑問詞 + to不定詞の重要構文",
                "explanation": "文5の `debating how to spend money wisely` は、「どのようにお金を賢く使うべきか」という意味です。英検準2級・2級の並び替え問題やライティングで必須の構文です。"
            },
            {
                "phrase": "cost + 金額（〜の費用がかかる）",
                "meaning": "動詞 cost の重要用法",
                "explanation": "文4の `will cost billions of pounds` の cost は、「費用がかかる」という意味の動詞です。主語に「物や計画」、後ろに「金額」が来ます。"
            }
        ],
        "quiz": [
            {
                "question": "What has changed the way countries defend their skies in recent years?",
                "options": [
                    "Small and low-cost drones.",
                    "Traditional passenger airplanes.",
                    "New space rockets.",
                    "Bicycles used by soldiers."
                ],
                "correct_index": 0,
                "explanation": "【正解：A】<br>第2文「In recent years, small and low-cost drones have changed how countries defend their skies」より、Aが正解です。"
            },
            {
                "question": "What are lawmakers debating in Parliament?",
                "options": [
                    "How to build faster trains for tourists.",
                    "How to spend tax money wisely while keeping the country safe.",
                    "How to stop people from using smartphones.",
                    "How to make tickets cheaper for movie theaters."
                ],
                "correct_index": 1,
                "explanation": "【正解：B】<br>第5文「Lawmakers are debating how to spend money wisely while keeping the country safe」より、Bが正解です。"
            },
            {
                "question": "Which word is CLOSEST in meaning to 'wisely' in sentence 5?",
                "options": [
                    "cleverly and carefully",
                    "quickly and carelessly",
                    "noisily",
                    "dangerously"
                ],
                "correct_index": 0,
                "explanation": "【正解：A】<br>wisely は「賢く、慎重に」という意味なので、cleverly and carefully（利口に、慎重に）が最も近い意味です。"
            }
        ]
    },

    {
        "slug": "critical-minerals-geopolitics",
        "category": "world",
        "category_label": "WORLD & ENVIRONMENT • 英検準2級〜2級",
        "title": "The Race for Green Energy Minerals: How Countries Work Together",
        "headline_ja": "クリーンエネルギーに必要な鉱物の争奪戦：各国が協力する理由と貿易のルール",
        "subhead": "電気自動車（EV）やスマホに欠かせない希少な鉱物。特定の一国に頼りすぎないよう、日本や欧米が手を取り合う国際ニュースを読み解きます。",
        "lead_snippet": "電気自動車や風力発電を増やすために、リチウムやレアアースといった特別な鉱物が世界中で必要とされています。友好国同士でサプライチェーン（供給網）を強化する新しい動きを解説します。",
        "source_name": "Financial Times / Reuters (Adapted for Junior)",
        "source_url": "https://www.ft.com/content/commodities-critical-minerals-2026",
        "source_attribution": "国際通商報道を元に、高校英語の標準レベルで環境・経済のつながりを学べるよう編集した教材です。",
        "source_student_guide": "『環境保全のための新技術』と『国際社会の協力・対立』は、英検2級から大学入試まで超頻出の現代的テーマです。環境用語と国際貿易の基本を押さえましょう。",
        "original_article_url": "../../../world/critical-minerals-geopolitics/index.html",
        "image": "https://images.unsplash.com/photo-1578328819058-b69f3a3b0f6b?w=1000&auto=format&fit=crop&q=80",
        "sentences": [
            {
                "en": "Electric cars and solar panels are very important for fighting climate change.",
                "ja": "電気自動車や太陽光パネルは、気候変動と戦うために非常に重要です。"
            },
            {
                "en": "To build these green technologies, factories need rare minerals like lithium and cobalt.",
                "ja": "これらの環境技術を作るために、工場はリチウムやコバルトのような希少な鉱物を必要としています。"
            },
            {
                "en": "However, most of these minerals come from only a few specific countries.",
                "ja": "しかし、これらの鉱物の大部分は、わずか数カ国の特定の国からしか採れません。"
            },
            {
                "en": "Therefore, many countries, including Japan, the US, and European nations, are working together to share resources.",
                "ja": "そのため、日本、アメリカ、ヨーロッパ諸国を含む多くの国々が、資源を分け合うために協力しています。"
            },
            {
                "en": "International cooperation will be the key to creating a clean and peaceful future.",
                "ja": "国際的な協力こそが、クリーンで平和な未来を創るための鍵となるでしょう。"
            }
        ],
        "dialogue": [
            {
                "speaker": "七",
                "name": "Nanami",
                "role": "大学生アシスタント",
                "text": "Keita先生、スマートフォンや電気自動車のバッテリーに使われるリチウムって、採れる国が偏っているんですね！"
            },
            {
                "speaker": "慶",
                "name": "Keita先生",
                "role": "英語講師",
                "text": "そうなんだ。文3にあるように『come from only a few specific countries』だから、もしその国から買えなくなったら、世界中でエコカーやスマホが作れなくなってしまうんだよ。"
            },
            {
                "speaker": "七",
                "name": "Nanami",
                "role": "大学生アシスタント",
                "text": "だから文4で、日本やアメリカ、ヨーロッパが『are working together to share resources（資源を共有するために協力している）』んですね！"
            },
            {
                "speaker": "慶",
                "name": "Keita先生",
                "role": "英語講師",
                "text": "その通り！文4の『including Japan, the US, and European nations』の including ~（〜を含めて）という前置詞は、英検準2級や2級の長文で必ず登場する最重要単語だよ。"
            },
            {
                "speaker": "七",
                "name": "Nanami",
                "role": "大学生アシスタント",
                "text": "文5の『the key to creating a clean future』の the key to ~ もよく見かけます！『〜への鍵、〜のための秘訣』ですね！"
            },
            {
                "speaker": "慶",
                "name": "Keita先生",
                "role": "英語講師",
                "text": "素晴らしい！to の後ろに名詞や動名詞（creating）が来る点まで見抜けているね。英作文でそのまま使える表現だよ。"
            },
            {
                "speaker": "七",
                "name": "Nanami",
                "role": "大学生アシスタント",
                "text": "理科や地理で習った知識と英語がつながって、読んでいてとても面白いです！"
            }
        ],
        "vocab": [
            {
                "word": "mineral",
                "phonetic": "/ˈmɪn.ər.əl/",
                "pos": "名詞",
                "meaning": "鉱物、無機物",
                "def": "a valuable or useful chemical substance that is formed naturally in the ground.",
                "ex": "This mountain region is rich in gold, copper, and other natural minerals."
            },
            {
                "word": "rare",
                "phonetic": "/reər/",
                "pos": "形容詞",
                "meaning": "希少な、めったにない",
                "def": "not common or frequent; very unusual.",
                "ex": "It is very rare to see this kind of wild bird in the city."
            },
            {
                "word": "specific",
                "phonetic": "/spəˈsɪf.ɪk/",
                "pos": "形容詞",
                "meaning": "特定の、具体的な",
                "def": "relating to one particular thing or type of thing.",
                "ex": "The doctor gave me specific instructions on when to take the medicine."
            },
            {
                "word": "including",
                "phonetic": "/ɪnˈkluː.dɪŋ/",
                "pos": "前置詞",
                "meaning": "〜を含めて",
                "def": "used for saying that something is part of something else.",
                "ex": "Ten students, including Sarah and Ken, passed the English exam."
            },
            {
                "word": "cooperation",
                "phonetic": "/kəʊˌɒp.ərˈeɪ.ʃən/",
                "pos": "名詞",
                "meaning": "協力、協調",
                "def": "the act of working together with someone or doing what they ask you.",
                "ex": "The science project was successful thanks to the close cooperation among students."
            }
        ],
        "syntax": [
            {
                "phrase": "including ~（〜を含めて）",
                "meaning": "具体例を付け加える前置詞",
                "explanation": "文4の `many countries, including Japan, the US, and European nations` は、「日本、米国、欧州諸国を含めた多くの国々」という意味です。英検の読解で主語を正確に捉えるために重要です。"
            },
            {
                "phrase": "the key to + 名詞 / 動名詞（〜のための鍵、秘訣）",
                "meaning": "重要度・解決策を表す最重要構文",
                "explanation": "文5の `the key to creating a clean and peaceful future` の to は前置詞なので、後ろに動名詞 `creating` が続きます。「〜を成し遂げるための鍵」という意味で、英作文のまとめ文で大活躍します。"
            }
        ],
        "quiz": [
            {
                "question": "Why are electric cars and solar panels important today?",
                "options": [
                    "Because they make roads quieter at night.",
                    "Because they are very important for fighting climate change.",
                    "Because they can fly in the sky without gasoline.",
                    "Because they are cheaper than old bicycles."
                ],
                "correct_index": 1,
                "explanation": "【正解：B】<br>第1文「Electric cars and solar panels are very important for fighting climate change」より、Bが正解です。"
            },
            {
                "question": "What is the problem with rare minerals like lithium and cobalt?",
                "options": [
                    "They are too heavy to carry on ships.",
                    "Most of them come from only a few specific countries.",
                    "They can only be found under deep ice in the Arctic.",
                    "They disappear when they touch water."
                ],
                "correct_index": 1,
                "explanation": "【正解：B】<br>第3文「most of these minerals come from only a few specific countries（ほとんどがわずか数カ国からしか採れない）」より、Bが正解です。"
            },
            {
                "question": "Which of the following is CLOSEST in meaning to 'work together' in sentence 4?",
                "options": [
                    "compete",
                    "cooperate",
                    "disagree",
                    "separate"
                ],
                "correct_index": 1,
                "explanation": "【正解：B】<br>work together は「協力する」という意味なので、cooperate が最も適しています。"
            }
        ]
    }
]

from junior_articles_batch2 import JUNIOR_ARTICLES_BATCH2
from junior_articles_batch3 import JUNIOR_ARTICLES_BATCH3
from junior_articles_batch4 import JUNIOR_ARTICLES_BATCH4
from batch6_articles_data import BATCH6_JUNIOR

JUNIOR_ARTICLES.extend(JUNIOR_ARTICLES_BATCH2)
JUNIOR_ARTICLES.extend(JUNIOR_ARTICLES_BATCH3)
JUNIOR_ARTICLES.extend(JUNIOR_ARTICLES_BATCH4)
JUNIOR_ARTICLES.extend(BATCH6_JUNIOR)

_DATE_MAP = {
    "soai-reaction-nobel-chemistry": "2026-10-10",
    "regulatory-t-cells-nobel-breakthrough": "2026-10-10",
    "smart-glasses-ai-privacy": "2026-10-09",
    "japan-semiconductor-revival-rapidus": "2026-10-09",
    "digital-school-backpack-reform": "2026-10-09",
    "esports-highschool-education": "2026-10-09",
    "global-plastics-treaty-negotiations": "2026-10-09",
    "cashless-society-local-bus-crisis": "2026-10-09",
    "perovskite-solar-cells-commercialization": "2026-10-09",
    "space-debris-corporate-liability": "2026-10-09",
    "handwriting-cognitive-benefits": "2026-10-09",
    "remote-work-suburban-revitalization": "2026-10-09",
    "ai-music-copyright-royalties": "2026-10-09",
    "ai-energy-nuclear-data-centers": "2026-10-09",
    "headphones-in-public": "2026-10-06",
    "psychology-casual-encounters": "2026-10-06",
    "critical-minerals-geopolitics": "2026-10-06",
    "air-defence-shield": "2026-10-05",
    "royal-security-judicial-review": "2026-10-05",
    "clarkson-business-red-tape": "2026-10-05",
    "colorectal-cancer-under-50s": "2026-10-04",
    "mediterranean-marine-heatwaves": "2026-10-04",
    "ai-pediatric-diagnosis-consent": "2026-10-03",
    "generative-ai-paleontology": "2026-10-03",
    "arctic-sea-route-unclos": "2026-10-03",
    "inheritance-tax-reform-debate": "2026-10-02",
    "stoic-philosophy-digital-age": "2026-10-02",
    "jeffrey-archer-obituary": "2026-10-01",
    "raf-fairford-bomber-redeployment": "2026-10-01"
}
for _a in JUNIOR_ARTICLES:
    _slug = _a.get("slug")
    if _slug in _DATE_MAP:
        _a["date"] = _DATE_MAP[_slug]
        _a["pub_date"] = _DATE_MAP[_slug]

DAILY_MAX_UPDATE = 30  # 1日あたりの最大追加・更新記事数（アーカイブ総ページ数に上限はありません）
print(f"Loaded {len(JUNIOR_ARTICLES)} Junior articles successfully (Daily update capacity: {DAILY_MAX_UPDATE}/day).")

