// THE JUNIOR - Master Portal Data & High School Study Knowledge Base
// Contains all 15 Junior articles, daily editions, and Eiken study resources.

const JUNIOR_ARTICLES = [
  {
    "slug": "headphones-in-public",
    "category": "culture",
    "category_label": "CULTURE & DAILY LIFE • 英検準2級〜2級",
    "date": "2026-10-06",
    "title": "The Power of Quiet Moments: Why We Should Sometimes Take Off Our Headphones",
    "headline_ja": "公共の場でイヤホンを外すことの良さ：静かな時間が心にアイデアをもたらす理由",
    "subhead": "通学中ずっと音楽や動画を聴いていませんか？『ぼーっとする時間』が人間の創造性を育てる理由を、高校生向けのやさしい英語で読み解きます。",
    "lead_snippet": "イギリスの調査では、90%以上の大人が毎週スマートフォンなどで音声を聴いています。しかし専門家は、『静かな余白の時間』をなくしてしまうと、脳が新しいアイデアを思いつくチャンスが減ってしまうと警告しています。",
    "source_name": "TIME Magazine (Adapted for Eiken Grade Pre-2 - 2)",
    "source_media_key": "time",
    "image": "https://static.time.com/v3/assets/bltea6093859af6183b/blt96d6f358ea9d50b0/6abfba6215869b08e9e95a32/headphones.jpg?branch=production&width=1200&quality=80&auto=webp",
    "path": "culture/headphones-in-public/index.html",
    "senior_path": "../culture/headphones-in-public/index.html"
  },
  {
    "slug": "colorectal-cancer-under-50s",
    "category": "science",
    "category_label": "SCIENCE & HEALTH • 英検準2級〜2級",
    "date": "2026-10-04",
    "title": "A Medical Mystery: Why Young People Are Getting Sick",
    "headline_ja": "若い世代に広がる病気の謎：超加工食品と腸の健康について知っておくべきこと",
    "subhead": "大腸がんは以前は高齢者の病気と考えられていましたが、今世界中で若い患者が増えています。最新の科学が注目する『食生活と環境の変化』を読み解きます。",
    "lead_snippet": "世界中の医師たちが、50歳未満の若い世代で大腸がんが増えている現象に注目しています。研究者たちは、毎日のスナック菓子や冷凍食品、そして微小なプラスチックの影響を詳しく調べています。",
    "source_name": "Nature Medicine / BBC Health (Adapted for Junior)",
    "source_media_key": "nature",
    "image": "https://images.unsplash.com/photo-1532938911079-1b06ac7ceec7?w=1000&auto=format&fit=crop&q=80",
    "path": "science/colorectal-cancer-under-50s/index.html",
    "senior_path": "../science/colorectal-cancer-under-50s/index.html"
  },
  {
    "slug": "psychology-casual-encounters",
    "category": "society",
    "category_label": "SOCIETY & MIND • 英検準2級〜2級",
    "date": "2026-10-06",
    "title": "The Magic of a Simple Hello: Why Small Talks Bring Big Smiles",
    "headline_ja": "ちょっとした挨拶の魔法：知らない人との短い会話が私たちを幸せにする理由",
    "subhead": "コンビニの店員さんに『ありがとう』と言ったり、駅員さんに会釈したり。ささやかな交流が街の孤独感を癒やす心理学の実験を英語で学びます。",
    "lead_snippet": "アメリカの大学の研究で、通学や通勤の途中で周りの人に少し話しかけるだけで、人は予想以上に幸せな気持ちになれることが分かりました。人見知りな人でも実践できる『会話の力』を解説します。",
    "source_name": "Journal of Personality & Social Psychology (Adapted for Junior)",
    "source_media_key": "the-conversation",
    "image": "https://images.unsplash.com/photo-1522202176988-66273c2fd55f?w=1000&auto=format&fit=crop&q=80",
    "path": "society/psychology-casual-encounters/index.html",
    "senior_path": "../society/psychology-casual-encounters/index.html"
  },
  {
    "slug": "air-defence-shield",
    "category": "law",
    "category_label": "LAW & SOCIETY • 英検準2級〜2級",
    "date": "2026-10-05",
    "title": "Protecting the Skies: UK Parliament Discusses New Defence Plans",
    "headline_ja": "空の安全を守る：英国議会が話し合う新しい防衛計画と国民の税金",
    "subhead": "安価なドローンの登場で、国の空を守る仕組みが大きく変わろうとしています。巨額の税金を使うとき、国会でどのようなルールが必要かをやさしく学びます。",
    "lead_snippet": "イギリス議会で、国全体を守る新しい防衛シールド計画の話し合いが始まりました。最新の技術を取り入れるスピードと、国民の大切な税金を慎重に使うルールとのバランスを考えます。",
    "source_name": "Financial Times / The Times (Adapted for Junior)",
    "source_media_key": "the-times",
    "image": "https://images.unsplash.com/photo-1541872703-74c5e44368f9?w=1000&auto=format&fit=crop&q=80",
    "path": "law/air-defence-shield/index.html",
    "senior_path": "../law/air-defence-shield/index.html"
  },
  {
    "slug": "critical-minerals-geopolitics",
    "category": "world",
    "category_label": "WORLD & ENVIRONMENT • 英検準2級〜2級",
    "date": "2026-10-06",
    "title": "The Race for Green Energy Minerals: How Countries Work Together",
    "headline_ja": "クリーンエネルギーに必要な鉱物の争奪戦：各国が協力する理由と貿易のルール",
    "subhead": "電気自動車（EV）やスマホに欠かせない希少な鉱物。特定の一国に頼りすぎないよう、日本や欧米が手を取り合う国際ニュースを読み解きます。",
    "lead_snippet": "電気自動車や風力発電を増やすために、リチウムやレアアースといった特別な鉱物が世界中で必要とされています。友好国同士でサプライチェーン（供給網）を強化する新しい動きを解説します。",
    "source_name": "Financial Times / Reuters (Adapted for Junior)",
    "source_media_key": "ft",
    "image": "https://images.unsplash.com/photo-1578328819058-b69f3a3b0f6b?w=1000&auto=format&fit=crop&q=80",
    "path": "world/critical-minerals-geopolitics/index.html",
    "senior_path": "../world/critical-minerals-geopolitics/index.html"
  },
  {
    "slug": "jeffrey-archer-obituary",
    "category": "culture",
    "category_label": "CULTURE & LITERATURE • 英検準2級〜2級",
    "date": "2026-10-01",
    "title": "A Storyteller Who Never Gave Up: Remembering Jeffrey Archer",
    "headline_ja": "諦めなかった物語作家：ベストセラー作家ジェフリー・アーチャーの生涯",
    "subhead": "世界中で3億冊以上の本が読まれた作家ジェフリー・アーチャー。失敗から立ち上がり、人々をワクワクさせる物語を書き続けた波乱万丈の人生を高校英語で学びます。",
    "lead_snippet": "イギリスの著名な小説家ジェフリー・アーチャーが86歳で亡くなりました。彼は政治家としての挫折や投獄という大きな困難を経験しながらも、世界中の読者を夢中にさせるベストセラーを書き続けました。",
    "source_name": "The Times / BBC News (Adapted for Junior)",
    "source_media_key": "the-guardian",
    "image": "https://images.unsplash.com/photo-1457369804613-52c61a468e7d?w=1000&auto=format&fit=crop&q=80",
    "path": "culture/jeffrey-archer-obituary/index.html",
    "senior_path": "../culture/jeffrey-archer-obituary/index.html"
  },
  {
    "slug": "stoic-philosophy-digital-age",
    "category": "culture",
    "category_label": "CULTURE & PHILOSOPHY • 英検準2級〜2級",
    "date": "2026-10-02",
    "title": "Calm in a Busy World: Ancient Greek Wisdom for Modern Students",
    "headline_ja": "忙しい世界で心を落ち着かせる：高校生に役立つ古代ギリシャ・ローマの知恵",
    "subhead": "スマホの通知やSNSの周りの目が気になりませんか？古代ストア派の哲学者たちが教える『変えられるものと変えられないものを分ける』知恵を英語で学びます。",
    "lead_snippet": "SNSの通知や試験のプレッシャーに追われる現代において、古代の『ストア哲学』が若い世代の間で再び人気を集めています。自分の力で変えられることだけに集中し、心の平和を保つ方法を高校英語で読み解きます。",
    "source_name": "TIME Magazine / The Conversation (Adapted for Junior)",
    "source_media_key": "time",
    "image": "https://images.unsplash.com/photo-1544717305-2782549b5136?w=1000&auto=format&fit=crop&q=80",
    "path": "culture/stoic-philosophy-digital-age/index.html",
    "senior_path": "../culture/stoic-philosophy-digital-age/index.html"
  },
  {
    "slug": "generative-ai-paleontology",
    "category": "science",
    "category_label": "SCIENCE & AI • 英検準2級〜2級",
    "date": "2026-10-03",
    "title": "How AI Helps Scientists Bring Dinosaurs Back to Life",
    "headline_ja": "AIが恐竜の動きを現代に蘇らせる：化石と最新テクノロジーの出会い",
    "subhead": "映画の恐竜は本当にあんなに速く走れたのでしょうか？骨の化石から生前の筋肉の動きを計算する最新AIの科学研究を英語で読み解きます。",
    "lead_snippet": "コンピュータサイエンティストと古生物学者が協力し、最新のAIを使って太古の恐竜がどのように歩き、走っていたかを正確に計算する研究が進んでいます。映画のイメージを覆す驚きの科学的発見を解説します。",
    "source_name": "Nature / Science Magazine (Adapted for Junior)",
    "source_media_key": "science-mag",
    "image": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=1000&auto=format&fit=crop&q=80",
    "path": "science/generative-ai-paleontology/index.html",
    "senior_path": "../science/generative-ai-paleontology/index.html"
  },
  {
    "slug": "mediterranean-marine-heatwaves",
    "category": "science",
    "category_label": "ENVIRONMENT & OCEANS • 英検準2級〜2級",
    "date": "2026-10-04",
    "title": "Hot Water in the Deep Ocean: Why Mediterranean Corals Need Help",
    "headline_ja": "深海に忍び寄る海の熱波：地中海のサンゴを守るための新しい挑戦",
    "subhead": "海面の温度が上がるだけでなく、光の届かない深い海まで水温が上昇していることが分かりました。海の環境問題と地球温暖化の最新ニュースを学びます。",
    "lead_snippet": "地中海の深海調査により、地球温暖化による『海洋熱波』が水深数百メートルの暗い深海にまで達していることが明らかになりました。成長に何百年もかかる貴重な深海サンゴを守るための国際的な取り組みを解説します。",
    "source_name": "Nature Climate Change / BBC Science (Adapted for Junior)",
    "source_media_key": "nature",
    "image": "https://images.unsplash.com/photo-1544551763-46a013bb70d5?w=1000&auto=format&fit=crop&q=80",
    "path": "science/mediterranean-marine-heatwaves/index.html",
    "senior_path": "../science/mediterranean-marine-heatwaves/index.html"
  },
  {
    "slug": "clarkson-business-red-tape",
    "category": "society",
    "category_label": "SOCIETY & ECONOMY • 英検準2級〜2級",
    "date": "2026-10-05",
    "title": "Starting a Business in the Countryside: The Challenge of Rules",
    "headline_ja": "田舎でビジネスを始める難しさ：クラークソン農場が教えてくれる起業のリアル",
    "subhead": "英国の人気司会者が農場を開き、地元の特産品を売ろうとしたときに直面した様々な規制。地域経済の発展とルールのあり方を英語で考えます。",
    "lead_snippet": "イギリスの人気テレビ司会者ジェレミー・クラークソンが自らの農場経営を通じて、『田舎で新しいビジネスを立ち上げようとすると、複雑すぎる役所のルールに阻まれる』と訴え、大きな社会的議論を巻き起こしています。",
    "source_name": "The Sunday Times / BBC News (Adapted for Junior)",
    "source_media_key": "ft",
    "image": "https://images.unsplash.com/photo-1500382017468-9049fed747ef?w=1000&auto=format&fit=crop&q=80",
    "path": "society/clarkson-business-red-tape/index.html",
    "senior_path": "../society/clarkson-business-red-tape/index.html"
  },
  {
    "slug": "inheritance-tax-reform-debate",
    "category": "society",
    "category_label": "SOCIETY & TAXES • 英検準2級〜2級",
    "date": "2026-10-02",
    "title": "Fairness for All: Britain Debates the Future of Family Taxes",
    "headline_ja": "みんなにとっての公平とは？：英国で議論される家族の税金と社会の仕組み",
    "subhead": "親が一生懸命働いて残した家や貯金に税金をかけるべきか？貧富の差を小さくすることと、家族を大切にすることのバランスを高校英語で学びます。",
    "lead_snippet": "イギリスの政治で、亡くなった親から財産を受け継ぐ際にかかる『相続税（Inheritance Tax）』を見直すべきかどうかの大激論が起きています。税金の公平さと家族の想いについて、高校生向けのやさしい英語で考えます。",
    "source_name": "Financial Times / The Times (Adapted for Junior)",
    "source_media_key": "ft",
    "image": "https://images.unsplash.com/photo-1554224155-8d04cb21cd6c?w=1000&auto=format&fit=crop&q=80",
    "path": "society/inheritance-tax-reform-debate/index.html",
    "senior_path": "../society/inheritance-tax-reform-debate/index.html"
  },
  {
    "slug": "ai-pediatric-diagnosis-consent",
    "category": "law",
    "category_label": "LAW & BIOETHICS • 英検準2級〜2級",
    "date": "2026-10-03",
    "title": "When AI Advises Doctors: Parents and Healthcare Decisions",
    "headline_ja": "AIが治療方針を提案するとき：子どもの命と親の同意を巡るルール",
    "subhead": "難しい病気の赤ちゃんを救うため、最新のAIが手術を提案しました。親の意見とAIの診断結果が食い違ったとき、法律はどう判断するのかを学びます。",
    "lead_snippet": "ロンドンの裁判所で、『医師が使うAIの診断結果に基づいた手術を、親が拒否できるか』という歴史的な裁判が始まりました。子どもの命を救う最善の道と、親の決定権のバランスを高校生向けの平易な英語で解説します。",
    "source_name": "The Guardian / BBC Health (Adapted for Junior)",
    "source_media_key": "the-guardian",
    "image": "https://images.unsplash.com/photo-1516549655169-df83a0774514?w=1000&auto=format&fit=crop&q=80",
    "path": "law/ai-pediatric-diagnosis-consent/index.html",
    "senior_path": "../law/ai-pediatric-diagnosis-consent/index.html"
  },
  {
    "slug": "royal-security-judicial-review",
    "category": "law",
    "category_label": "LAW & GOVERNMENT • 英検準2級〜2級",
    "date": "2026-10-05",
    "title": "Safety and the Law: Who Decides Protection for the Royal Family?",
    "headline_ja": "安全と法律の境界線：王室の警護費用を決める国のルール",
    "subhead": "英国王室のメンバーが公の場に出るとき、その警護費用は誰が払うべきなのか？国民の税金の使い方と公平な法手続きの議論を英語で学びます。",
    "lead_snippet": "イギリスで、公務から退いた王族の警察警護費用をめぐり、高等法院で法律の解釈を争う裁判が行われています。『国民の税金の使い方』と『法の下の平等』という民主主義の基本ルールを高校英語で読み解きます。",
    "source_name": "The Times / BBC News (Adapted for Junior)",
    "source_media_key": "the-times",
    "image": "https://images.unsplash.com/photo-1529655683826-aba9b3e77383?w=1000&auto=format&fit=crop&q=80",
    "path": "law/royal-security-judicial-review/index.html",
    "senior_path": "../law/royal-security-judicial-review/index.html"
  },
  {
    "slug": "arctic-sea-route-unclos",
    "category": "world",
    "category_label": "WORLD & ENVIRONMENT • 英検準2級〜2級",
    "date": "2026-10-03",
    "title": "Ships in the Cold North: Melting Ice and New Trade Routes",
    "headline_ja": "氷が解ける北極海を渡る船：地球温暖化と新しい国際貿易ルート",
    "subhead": "北極の氷が解けたことで、ヨーロッパとアジアを結ぶ新しい近道航路が生まれました。船の移動時間が短くなる利点と、環境を守るための国際ルールを学びます。",
    "lead_snippet": "地球温暖化によって北極海の氷が急速に解け、これまでは通れなかった北極海航路が新しい海のハイウェイとして注目されています。航路が大幅に短縮される期待と、沿岸国の領海主張を巡る国際摩擦をわかりやすく解説します。",
    "source_name": "The Times / Reuters (Adapted for Junior)",
    "source_media_key": "the-times",
    "image": "https://images.unsplash.com/photo-1483181957632-8bda974cbc91?w=1000&auto=format&fit=crop&q=80",
    "path": "world/arctic-sea-route-unclos/index.html",
    "senior_path": "../world/arctic-sea-route-unclos/index.html"
  },
  {
    "slug": "raf-fairford-bomber-redeployment",
    "category": "world",
    "category_label": "WORLD & DEFENCE • 英検準2級〜2級",
    "date": "2026-10-01",
    "title": "Keeping the Skies Safe: Moving Military Aircraft in Europe",
    "headline_ja": "空の安全を守るために：ヨーロッパで航空機を分散配置する理由",
    "subhead": "小型ドローンの登場など新しい危険に備えて、基地の航空機を別の場所へ移動させる作戦。国際的な防衛協力と平和を守る仕組みを英語で解説します。",
    "lead_snippet": "イギリスにある米空軍基地から大型爆撃機が別の安全な施設へと一時的に移動されました。安価なドローンの脅威から重要な防衛機材を守り、地域の平和と抑止力を維持するための最新の作戦を高校英語で学びます。",
    "source_name": "Reuters / AP News (Adapted for Junior)",
    "source_media_key": "reuters",
    "image": "https://images.unsplash.com/photo-1519074069444-1ba4ea16e6f1?w=1000&auto=format&fit=crop&q=80",
    "path": "world/raf-fairford-bomber-redeployment/index.html",
    "senior_path": "../world/raf-fairford-bomber-redeployment/index.html"
  }
];

const JUNIOR_EDITIONS = {
  "2026-10-09": {
    "dateStr": "Friday October 9 2026",
    "editionLabel": "2026年10月9日 (金) 号 【本日最新版】",
    "tagline": "特集：スマホ時代の不安を和らげる哲学とイヤホンを外す小さな勇気",
    "topLeadSlug": "stoic-philosophy-digital-age",
    "subLeadSlugs": [
      "headphones-in-public",
      "psychology-casual-encounters"
    ],
    "leftDispatches": [
      "critical-minerals-geopolitics",
      "colorectal-cancer-under-50s",
      "air-defence-shield"
    ],
    "rightDigestSlugs": [
      "mediterranean-marine-heatwaves",
      "ai-pediatric-diagnosis-consent",
      "clarkson-business-red-tape",
      "generative-ai-paleontology"
    ]
  },
  "2026-10-08": {
    "dateStr": "Thursday October 8 2026",
    "editionLabel": "2026年10月8日 (木) 号 【バックナンバー】",
    "tagline": "特集：クリーンエネルギーに必要な鉱物の争奪戦とスマホ時代の心の整理",
    "topLeadSlug": "critical-minerals-geopolitics",
    "subLeadSlugs": [
      "stoic-philosophy-digital-age",
      "mediterranean-marine-heatwaves"
    ],
    "leftDispatches": [
      "psychology-casual-encounters",
      "air-defence-shield",
      "colorectal-cancer-under-50s"
    ],
    "rightDigestSlugs": [
      "headphones-in-public",
      "clarkson-business-red-tape",
      "inheritance-tax-reform-debate",
      "ai-pediatric-diagnosis-consent"
    ]
  },
  "2026-10-07": {
    "dateStr": "Wednesday October 7 2026",
    "editionLabel": "2026年10月7日 (水) 号 【バックナンバー】",
    "tagline": "特集：ちょっとした挨拶の魔法と氷が解ける北極海航路のルール",
    "topLeadSlug": "psychology-casual-encounters",
    "subLeadSlugs": [
      "arctic-sea-route-unclos",
      "generative-ai-paleontology"
    ],
    "leftDispatches": [
      "critical-minerals-geopolitics",
      "royal-security-judicial-review",
      "raf-fairford-bomber-redeployment"
    ],
    "rightDigestSlugs": [
      "headphones-in-public",
      "stoic-philosophy-digital-age",
      "colorectal-cancer-under-50s",
      "air-defence-shield"
    ]
  },
  "2026-10-06": {
    "dateStr": "Tuesday October 6 2026",
    "editionLabel": "2026年10月6日 (火) 号 【バックナンバー】",
    "tagline": "特集：静かな時間の力（イヤホン論争）と見知らぬ人への挨拶の魔法",
    "topLeadSlug": "headphones-in-public",
    "subLeadSlugs": [
      "colorectal-cancer-under-50s",
      "psychology-casual-encounters"
    ],
    "leftDispatches": [
      "air-defence-shield",
      "critical-minerals-geopolitics",
      "raf-fairford-bomber-redeployment"
    ],
    "rightDigestSlugs": [
      "clarkson-business-red-tape",
      "inheritance-tax-reform-debate",
      "ai-pediatric-diagnosis-consent",
      "mediterranean-marine-heatwaves"
    ]
  },
  "2026-10-05": {
    "dateStr": "Monday October 5 2026",
    "editionLabel": "2026年10月5日 (月) 号 【バックナンバー】",
    "tagline": "特集：国の空を守る防衛計画と王室警護・お役所ルール論争",
    "topLeadSlug": "air-defence-shield",
    "subLeadSlugs": [
      "royal-security-judicial-review",
      "clarkson-business-red-tape"
    ],
    "leftDispatches": [
      "headphones-in-public",
      "inheritance-tax-reform-debate",
      "mediterranean-marine-heatwaves"
    ],
    "rightDigestSlugs": [
      "jeffrey-archer-obituary",
      "ai-pediatric-diagnosis-consent",
      "colorectal-cancer-under-50s",
      "raf-fairford-bomber-redeployment"
    ]
  },
  "2026-10-04": {
    "dateStr": "Sunday October 4 2026",
    "editionLabel": "2026年10月4日 (日) 号 【バックナンバー】",
    "tagline": "特集：若い世代の病気の謎と地中海の海の温暖化・魚たちの危機",
    "topLeadSlug": "colorectal-cancer-under-50s",
    "subLeadSlugs": [
      "mediterranean-marine-heatwaves",
      "generative-ai-paleontology"
    ],
    "leftDispatches": [
      "ai-pediatric-diagnosis-consent",
      "psychology-casual-encounters",
      "inheritance-tax-reform-debate"
    ],
    "rightDigestSlugs": [
      "headphones-in-public",
      "air-defence-shield",
      "clarkson-business-red-tape",
      "jeffrey-archer-obituary"
    ]
  },
  "2026-10-03": {
    "dateStr": "Saturday October 3 2026",
    "editionLabel": "2026年10月3日 (土) 号 【バックナンバー】",
    "tagline": "特集：子どものAI診断と恐竜の歩き方・氷が解ける北極海航路",
    "topLeadSlug": "ai-pediatric-diagnosis-consent",
    "subLeadSlugs": [
      "generative-ai-paleontology",
      "arctic-sea-route-unclos"
    ],
    "leftDispatches": [
      "clarkson-business-red-tape",
      "colorectal-cancer-under-50s",
      "jeffrey-archer-obituary"
    ],
    "rightDigestSlugs": [
      "headphones-in-public",
      "mediterranean-marine-heatwaves",
      "psychology-casual-encounters",
      "critical-minerals-geopolitics"
    ]
  },
  "2026-10-02": {
    "dateStr": "Friday October 2 2026",
    "editionLabel": "2026年10月2日 (金) 号 【バックナンバー】",
    "tagline": "特集：相続税をめぐる議論と古代ストア哲学・スマホ時代の心の整理",
    "topLeadSlug": "inheritance-tax-reform-debate",
    "subLeadSlugs": [
      "stoic-philosophy-digital-age",
      "psychology-casual-encounters"
    ],
    "leftDispatches": [
      "raf-fairford-bomber-redeployment",
      "royal-security-judicial-review",
      "generative-ai-paleontology"
    ],
    "rightDigestSlugs": [
      "air-defence-shield",
      "colorectal-cancer-under-50s",
      "headphones-in-public",
      "critical-minerals-geopolitics"
    ]
  },
  "2026-10-01": {
    "dateStr": "Thursday October 1 2026",
    "editionLabel": "2026年10月1日 (木) 号 【創刊バックナンバー】",
    "tagline": "特集：ヨーロッパの空の安全とベストセラー作家J・アーチャーの生涯",
    "topLeadSlug": "raf-fairford-bomber-redeployment",
    "subLeadSlugs": [
      "jeffrey-archer-obituary",
      "generative-ai-paleontology"
    ],
    "leftDispatches": [
      "air-defence-shield",
      "inheritance-tax-reform-debate",
      "mediterranean-marine-heatwaves"
    ],
    "rightDigestSlugs": [
      "clarkson-business-red-tape",
      "psychology-casual-encounters",
      "royal-security-judicial-review",
      "critical-minerals-geopolitics"
    ]
  }
};

const JUNIOR_STUDY_RESOURCES = [
  {
    "key": "time",
    "name": "TIME Magazine (米・オピニオン週刊誌)",
    "badge": "英検2級・準1級・共通テスト最頻出",
    "point": "日常の習慣（イヤホン、スマホ、睡眠）を題材にしながら、社会の大きな変化を分かりやすく問いかけるエッセイの宝庫です。段落ごとの主張の流れがとてもクリアで、自由英作文のお手本になります。"
  },
  {
    "key": "the-times",
    "name": "The Times (英・本格高級日刊紙)",
    "badge": "英語の標準スタイル・英検準1級〜",
    "point": "英語圏で最も伝統ある新聞。ルールや法律、社会制度の議論を正確な言葉で伝えます。受動態や関係詞のきれいな構文が多く、高校の文法知識がどう使われているかを実感できます。"
  },
  {
    "key": "the-guardian",
    "name": "The Guardian (英・国際的リベラル紙)",
    "badge": "医療倫理・環境問題・人権テーマ",
    "point": "AIと医療、気候変動など、教科書で習うSDGsや現代社会のテーマを深く掘り下げます。登場人物の生の声（インタビュー）が豊富で、会話表現の読解にも役立ちます。"
  },
  {
    "key": "nature",
    "name": "Nature & Science News (国際科学誌)",
    "badge": "理科・生物・環境の入試頻出",
    "point": "「なぜ病気が増えているのか」「海で何が起きているのか」という謎解きの面白さを学べます。図表問題や共通テストの科学パッセージで求められる論理的思考力が身につきます。"
  }
];
