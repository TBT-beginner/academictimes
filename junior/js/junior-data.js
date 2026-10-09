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
  },
  {
    "slug": "smart-glasses-ai-privacy",
    "category": "entertainment",
    "category_label": "ENTERTAINMENT & GADGETS • 英検準2級〜2級",
    "date": "2026-10-09",
    "title": "Smart Glasses and AI: The Exciting Future and Privacy Rules We Need",
    "headline_ja": "スマートグラスとAI：未来のワクワクする技術とみんなで考えるプライバシーのルール",
    "subhead": "メガネをかけるだけでAIが道を案内してくれる時代へ！便利さと周囲への思いやりについて考えよう。",
    "lead_snippet": "最新のスマートグラスは、見た目は普通のメガネなのに、小さなカメラと人工知能（AI）が入っています。看板の外国語を自動で翻訳してくれるなど便利な反面、まわりの人のプライバシーを守るルール作りが求められています。",
    "source_name": "GetNews Japan (Adapted for Eiken Grade Pre-2 - 2)",
    "source_media_key": "getnews",
    "image": "https://images.unsplash.com/photo-1593508512255-86ab42a8e620?w=1000&auto=format&fit=crop&q=80",
    "path": "entertainment/smart-glasses-ai-privacy/index.html",
    "senior_path": "../entertainment/smart-glasses-ai-privacy/index.html"
  },
  {
    "slug": "japan-semiconductor-revival-rapidus",
    "category": "science",
    "category_label": "SCIENCE & TECH • 英検準2級〜2級",
    "date": "2026-10-09",
    "title": "Japan's Big Plan to Make Super-Fast Computer Chips",
    "headline_ja": "日本の大きな挑戦：世界で一番速い超小型コンピューターチップをつくる！",
    "subhead": "スマホやAIの頭脳となる「半導体」。北海道で進む新しい工場づくりのニュースをやさしい英語で学びます。",
    "lead_snippet": "コンピューターやスマートフォン、電気自動車の頭脳である「半導体チップ」。日本は世界で最も進んだ2ナノメートルの極小チップを国内で作るため、北海道に巨大な工場を建設する国家プロジェクトを進めています。",
    "source_name": "Jiji Press (Adapted for Eiken Grade Pre-2 - 2)",
    "source_media_key": "jiji",
    "image": "https://images.unsplash.com/photo-1518770660439-4636190af475?w=1000&auto=format&fit=crop&q=80",
    "path": "science/japan-semiconductor-revival-rapidus/index.html",
    "senior_path": "../science/japan-semiconductor-revival-rapidus/index.html"
  },
  {
    "slug": "digital-school-backpack-reform",
    "category": "society",
    "category_label": "SOCIETY & EDUCATION • 英検準2級〜2級",
    "date": "2026-10-09",
    "title": "Heavy School Bags and Digital Tablets: How Classrooms in Japan Are Changing",
    "headline_ja": "重いランドセルとタブレット端末：日本の学校はどう変わっていくのか？",
    "subhead": "教科書とタブレットでカバンが重すぎる！生徒たちの体を守りながら楽しく勉強するためのアイデアを読みます。",
    "lead_snippet": "全国の小中学校でタブレット端末が配られましたが、紙の教科書も一緒に持ち運ぶためカバンが重すぎる問題が発生しています。生徒の健康を守るため、軽量リュックサックを認める学校が増えています。",
    "source_name": "Yahoo! News Japan (Adapted for Eiken Grade Pre-2 - 2)",
    "source_media_key": "yahoo",
    "image": "https://images.unsplash.com/photo-1503676260728-1c00da094a0b?w=1000&auto=format&fit=crop&q=80",
    "path": "society/digital-school-backpack-reform/index.html",
    "senior_path": "../society/digital-school-backpack-reform/index.html"
  },
  {
    "slug": "regulatory-t-cells-nobel-breakthrough",
    "category": "science",
    "category_label": "SCIENCE & HEALTH • 英検準2級〜2級",
    "date": "2026-10-09",
    "title": "How a Japanese Scientist Discovered the Body's Natural Brake Cells",
    "headline_ja": "日本の科学者が発見した体のブレーキ役：暴走する免疫をコントロールする仕組み",
    "subhead": "病気のウイルスと戦う免疫システムが、自分の体を傷つけないように見守る「ブレーキ細胞」。世界的発見をやさしい英語で読み解きます。",
    "lead_snippet": "大阪大学の坂口志文教授は、私たちの体に備わっている「免疫のブレーキ役」となる特別な細胞を発見しました。この発見によって、アレルギーや自己免疫疾患の原因が解明され、新しいがんの治療薬の開発につながっています。",
    "source_name": "Jiji Press & Nature (Adapted for Eiken Grade Pre-2 - 2)",
    "source_media_key": "jiji",
    "image": "https://images.unsplash.com/photo-1532187863486-abf9dbad1b69?w=1000&auto=format&fit=crop&q=80",
    "path": "science/regulatory-t-cells-nobel-breakthrough/index.html",
    "senior_path": "../science/regulatory-t-cells-nobel-breakthrough/index.html"
  },
  {
    "slug": "soai-reaction-nobel-chemistry",
    "category": "science",
    "category_label": "SCIENCE & DISCOVERY • 英検準2級〜2級",
    "date": "2026-10-09",
    "title": "The Mystery of Right and Left Molecules: Japanese Professor Wins the 2026 Nobel Prize in Chemistry",
    "headline_ja": "右手と左手の分子のふしぎ：東京理科大の硤合先生が2026年ノーベル化学賞を受賞！",
    "subhead": "私たちの体を形づくるアミノ酸はなぜ「左手型」ばかりなのか？世界中の科学者を驚かせた「硤合反応」をやさしい英語で学びます。",
    "lead_snippet": "スウェーデン王立科学アカデミーは、2026年のノーベル化学賞を東京理科大学名誉教授の硤合憲三（そあい・けんぞう）先生らに授与すると発表しました。生命の分子がなぜ一方向の「利き手」を選んだのかという最大の謎を解いた大発見です。",
    "source_name": "Jiji Press & Nobel Prize (Adapted for Eiken Grade Pre-2 - 2)",
    "source_media_key": "jiji",
    "image": "https://images.unsplash.com/photo-1532094349884-543bc11b234d?w=1000&auto=format&fit=crop&q=80",
    "path": "science/soai-reaction-nobel-chemistry/index.html",
    "senior_path": "../science/soai-reaction-nobel-chemistry/index.html"
  },
  {
    "slug": "esports-highschool-education",
    "category": "entertainment",
    "category_label": "ENTERTAINMENT & SCHOOL • 英検準2級〜2級",
    "date": "2026-10-09",
    "title": "From Video Games to School Clubs: How High School Esports Helps Students Grow",
    "headline_ja": "ゲームから学校の部活動へ：高校の「eスポーツ部」がチームワークを育てる理由",
    "subhead": "放課後のゲームが学校教育の新しい形に！仲間と協力して勝利を目指す中で身につくスキルをやさしい英語で学びます。",
    "lead_snippet": "日本全国の高校で「eスポーツ部」を創部する動きが急速に広がっています。ゲームを単なる遊びで終わらせず、戦術の話し合いや大会の運営を通じて、社会で役立つ協調性や問題解決能力を身につける生徒たちが増えています。",
    "source_name": "GetNews Japan & Yahoo! News (Adapted for Eiken Grade Pre-2 - 2)",
    "source_media_key": "getnews",
    "image": "https://images.unsplash.com/photo-1542751371-adc38448a05e?w=1000&auto=format&fit=crop&q=80",
    "path": "entertainment/esports-highschool-education/index.html",
    "senior_path": "../entertainment/esports-highschool-education/index.html"
  },
  {
    "slug": "global-plastics-treaty-negotiations",
    "category": "world",
    "category_label": "WORLD & NATURE • 英検準2級〜2級",
    "date": "2026-10-09",
    "title": "Saving Our Oceans: World Leaders Work on a Global Treaty to Stop Plastic Waste",
    "headline_ja": "海を守る世界共通のルール：プラスチックゴミを減らす国連条約の誕生へ",
    "subhead": "海を漂うプラスチックや魚の体内のマイクロプラスチック。美しい海を未来に残すための国際協定をやさしい英語で学びます。",
    "lead_snippet": "世界170カ国以上の代表が国連に集まり、川や海に流れ出るプラスチックゴミを減らすための世界条約を作っています。プラスチックを作る量そのものを減らしたい国と、リサイクルを進めたい国との話し合いが続いています。",
    "source_name": "Jiji Press & UN News (Adapted for Eiken Grade Pre-2 - 2)",
    "source_media_key": "jiji",
    "image": "https://images.unsplash.com/photo-1618477461853-cf6ed80faba5?w=1000&auto=format&fit=crop&q=80",
    "path": "world/global-plastics-treaty-negotiations/index.html",
    "senior_path": "../world/global-plastics-treaty-negotiations/index.html"
  },
  {
    "slug": "cashless-society-local-bus-crisis",
    "category": "society",
    "category_label": "SOCIETY & LIVING • 英検準2級〜2級",
    "date": "2026-10-09",
    "title": "Cashless Buses on Country Roads: Solving Driver Shortages While Helping the Elderly",
    "headline_ja": "地方バスの完全キャッシュレス化：便利さと高齢者の乗りやすさのバランス",
    "subhead": "小銭の両替ができないバスが増加中？運転手さんの負担を減らしながら、誰もが安心して乗れる交通の未来を考えます。",
    "lead_snippet": "全国の路線バスで、運賃の支払いをICカードやクレジットカードなどの「キャッシュレス決済」だけに限定する実験が始まっています。両替の手間や人手不足を解決できる一方、スマホを持たないお年寄りが困らない工夫が求められています。",
    "source_name": "Yahoo! News Japan & Jiji Press (Adapted for Eiken Grade Pre-2 - 2)",
    "source_media_key": "yahoo",
    "image": "https://images.unsplash.com/photo-1570125909232-eb263c188f7e?w=1000&auto=format&fit=crop&q=80",
    "path": "society/cashless-society-local-bus-crisis/index.html",
    "senior_path": "../society/cashless-society-local-bus-crisis/index.html"
  },
  {
    "slug": "perovskite-solar-cells-commercialization",
    "category": "science",
    "category_label": "SCIENCE & FUTURE • 英検準2級〜2級",
    "date": "2026-10-09",
    "title": "Bendable Solar Power: How Japanese Technology Is Changing Clean Energy",
    "headline_ja": "曲がる太陽電池：日本の技術がひらく新しいクリーンエネルギーの未来",
    "subhead": "ビルの壁や車の屋根にも貼れる！超軽量で曲がる「ペロブスカイト太陽電池」の秘密をやさしい英語で読み解きます。",
    "lead_snippet": "日本で発明された「ペロブスカイト太陽電池」の実用化が急ピッチで進んでいます。従来の重い黒いパネルと違って、薄いフィルムのように曲がるため、ビルの壁や車のボディにも貼ることができます。日本の豊富なヨウ素資源を活かした新技術です。",
    "source_name": "Jiji Press & Nikkei Science (Adapted for Eiken Grade Pre-2 - 2)",
    "source_media_key": "jiji",
    "image": "https://images.unsplash.com/photo-1509391365360-2e959784a276?w=1000&auto=format&fit=crop&q=80",
    "path": "science/perovskite-solar-cells-commercialization/index.html",
    "senior_path": "../science/perovskite-solar-cells-commercialization/index.html"
  },
  {
    "slug": "space-debris-corporate-liability",
    "category": "law",
    "category_label": "LAW & SPACE • 英検準2級〜2級",
    "date": "2026-10-09",
    "title": "Cleaning Up Space: Who Is Responsible for Broken Satellites in Orbit?",
    "headline_ja": "宇宙ゴミの責任はだれに？人工衛星の安全な飛行を守る新しいルール作り",
    "subhead": "夜空を回る何万個もの衛星と宇宙ゴミ。衝突事故を防ぐための国際的な法律の動きをやさしい英語で学びます。",
    "lead_snippet": "通信やGPSのために、民間企業が打ち上げる人工衛星の数が急増しています。役目を終えた衛星やロケットの破片が宇宙ゴミ（スペースデブリ）となり、他の衛星にぶつかる危険が高まっています。企業にゴミ回収の責任を求める新しい宇宙法が求められています。",
    "source_name": "Financial Times & Jiji Press (Adapted for Eiken Grade Pre-2 - 2)",
    "source_media_key": "ft",
    "image": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=1000&auto=format&fit=crop&q=80",
    "path": "law/space-debris-corporate-liability/index.html",
    "senior_path": "../law/space-debris-corporate-liability/index.html"
  },
  {
    "slug": "handwriting-cognitive-benefits",
    "category": "culture",
    "category_label": "CULTURE & BRAIN • 英検準2級〜2級",
    "date": "2026-10-09",
    "title": "The Power of the Pen: Why Writing by Hand Is Better for Your Memory",
    "headline_ja": "手書きの力：ペンでノートをとることが記憶力と勉強を高める科学的な理由",
    "subhead": "タブレットやスマホばかり使っていませんか？手で文字を書くことが脳のネットワークを活性化させる理由をやさしい英語で読み解きます。",
    "lead_snippet": "パソコンやタブレットでノートをとる学生が増える中、最新の脳科学研究が「手書き」の驚くべき効果を証明しました。指先を使って文字を書くことで、脳の広い範囲が刺激され、タイピングよりも記憶に残りやすくなることが分かっています。",
    "source_name": "TIME Magazine & Frontiers (Adapted for Eiken Grade Pre-2 - 2)",
    "source_media_key": "time",
    "image": "https://images.unsplash.com/photo-1455390582262-044cdead277a?w=1000&auto=format&fit=crop&q=80",
    "path": "culture/handwriting-cognitive-benefits/index.html",
    "senior_path": "../culture/handwriting-cognitive-benefits/index.html"
  },
  {
    "slug": "remote-work-suburban-revitalization",
    "category": "society",
    "category_label": "SOCIETY & LIFE • 英検準2級〜2級",
    "date": "2026-10-09",
    "title": "Living by the Sea: How Hybrid Work Is Bringing Young Families to Country Towns",
    "headline_ja": "海のそばで働く心地よさ：ハイブリッドワークが若者を引き寄せる地方の魅力",
    "subhead": "週に2日だけ都会へ通い、残りは豊かな自然の中で仕事と子育て。新しい働き方が日本の地方都市を元気にする物語。",
    "lead_snippet": "完全出社でも完全テレワークでもない「ハイブリッドワーク」が定着しています。週2日程度東京のオフィスに通い、残りの日は新幹線や特急で通える海沿いや山あいの町で暮らす子育て世代が増加。空き家がステキなカフェやオフィスに生まれ変わっています。",
    "source_name": "Yahoo! News Japan (Adapted for Eiken Grade Pre-2 - 2)",
    "source_media_key": "yahoo",
    "image": "https://images.unsplash.com/photo-1503899036084-c55cdd92da26?w=1000&auto=format&fit=crop&q=80",
    "path": "society/remote-work-suburban-revitalization/index.html",
    "senior_path": "../society/remote-work-suburban-revitalization/index.html"
  },
  {
    "slug": "ai-music-copyright-royalties",
    "category": "entertainment",
    "category_label": "ENTERTAINMENT & MUSIC • 英検準2級〜2級",
    "date": "2026-10-09",
    "title": "Robots in the Recording Studio: Why Famous Musicians Are Worried About AI Songs",
    "headline_ja": "音楽スタジオの人工知能：有名アーティストが「AI作曲」に危機感を抱く理由",
    "subhead": "大好きな歌手のそっくりな声で新曲が作れる時代に？クリエイターの権利と最新テクノロジーのルールをやさしい英語で考えます。",
    "lead_snippet": "人気歌手の歌声や歌い方をそっくりに真似て作られた「AI楽曲」がインターネット上に溢れ、何百万回も再生されています。音楽業界は、本物の歌手や作曲家にお金が支払われないのは不公平だと抗議し、世界中でルール作りが進んでいます。",
    "source_name": "GetNews Japan & Billboard (Adapted for Eiken Grade Pre-2 - 2)",
    "source_media_key": "getnews",
    "image": "https://images.unsplash.com/photo-1511671782779-c97d3d27a1d4?w=1000&auto=format&fit=crop&q=80",
    "path": "entertainment/ai-music-copyright-royalties/index.html",
    "senior_path": "../entertainment/ai-music-copyright-royalties/index.html"
  },
  {
    "slug": "ai-energy-nuclear-data-centers",
    "category": "world",
    "category_label": "WORLD & ENERGY • 英検準2級〜2級",
    "date": "2026-10-09",
    "title": "Powering the AI Revolution: Why Big Tech Is Choosing Nuclear Energy",
    "headline_ja": "AIを動かす巨大な電力：アメリカのIT企業が原子力エネルギーを選ぶ理由",
    "subhead": "質問に答えてくれる生成AIは大量の電気を消費する？24時間休まず動くサーバーと地球温暖化対策のジレンマをやさしい英語で読み解きます。",
    "lead_snippet": "ChatGPTなどの生成AIを使う人が世界中で増えた結果、データセンターが消費する電力が爆発的に増えています。太陽光や風力は天気に左右されるため、GoogleやMicrosoftなどの巨大企業が、24時間安定して二酸化炭素を出さない「原子力発電」に巨額の投資を始めています。",
    "source_name": "Reuters & Jiji Press (Adapted for Eiken Grade Pre-2 - 2)",
    "source_media_key": "reuters",
    "image": "https://images.unsplash.com/photo-1513836279014-a89f7a76ae86?w=1000&auto=format&fit=crop&q=80",
    "path": "world/ai-energy-nuclear-data-centers/index.html",
    "senior_path": "../world/ai-energy-nuclear-data-centers/index.html"
  }
];

const JUNIOR_EDITIONS = {
  "2026-10-09": {
    "dateStr": "Friday October 9 2026",
    "editionLabel": "2026年10月9日 (金) 号 【本日最新版】",
    "tagline": "特集：東京理科大・硤合先生ノーベル化学賞受賞・坂口教授のブレーキ細胞・スマートグラスとAI",
    "topLeadSlug": "soai-reaction-nobel-chemistry",
    "subLeadSlugs": [
      "regulatory-t-cells-nobel-breakthrough",
      "smart-glasses-ai-privacy"
    ],
    "leftDispatches": [
      "japan-semiconductor-revival-rapidus",
      "digital-school-backpack-reform",
      "global-plastics-treaty-negotiations"
    ],
    "rightDigestSlugs": [
      "critical-minerals-geopolitics",
      "colorectal-cancer-under-50s",
      "air-defence-shield",
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
    "title_en": "TIME Magazine",
    "title_ja": "米・オピニオン週刊誌",
    "name": "TIME Magazine (米・オピニオン週刊誌)",
    "badge": "🎯 英検2級・準1級・共通テスト最頻出",
    "point": "日常の習慣（イヤホン、スマホ、睡眠）を題材にしながら、社会の大きな変化を分かりやすく問いかけるエッセイの宝庫です。段落ごとの主張の流れがとてもクリアで、自由英作文のお手本になります。",
    "tip": "各段落の第1文（トピックセンテンス）を拾い読みするだけで、全体の論理展開が掴めるようになります。"
  },
  {
    "key": "the-times",
    "title_en": "The Times",
    "title_ja": "英・本格高級日刊紙",
    "name": "The Times (英・本格高級日刊紙)",
    "badge": "🏛️ 英語の標準スタイル・英検準1級〜",
    "point": "英語圏で最も伝統ある新聞。ルールや法律、社会制度の議論を正確な言葉で伝えます。受動態や関係詞のきれいな構文が多く、高校の文法知識がどう使われているかを実感できます。",
    "tip": "関係代名詞や分詞構文が多用されるため、主語と述語を正確に捉える英文解釈力の強化に最適です。"
  },
  {
    "key": "the-guardian",
    "title_en": "The Guardian",
    "title_ja": "英・国際的リベラル日刊紙",
    "name": "The Guardian (英・国際的リベラル紙)",
    "badge": "🌍 医療倫理・環境問題・人権テーマ",
    "point": "AIと医療、気候変動など、教科書で習うSDGsや現代社会のテーマを深く掘り下げます。登場人物の生の声（インタビュー）が豊富で、会話表現の読解にも役立ちます。",
    "tip": "小論文や自由英作文で問われる『現代社会の論点・背景知識』を英語と日本語の両面から学べます。"
  },
  {
    "key": "nature",
    "title_en": "Nature & Science News",
    "title_ja": "英米・国際総合科学学術誌",
    "name": "Nature & Science News (国際科学誌)",
    "badge": "🔬 理科・生物・環境の入試頻出",
    "point": "「なぜ病気が増えているのか」「海で何が起きているのか」という謎解きの面白さを学べます。図表問題や共通テストの科学パッセージで求められる論理的思考力が身につきます。",
    "tip": "『仮説→実験手法→結果→考察』という理系論文の王道展開パターンを英語で掴むことができます。"
  },
  {
    "key": "jiji",
    "title_en": "Jiji Press",
    "title_ja": "時事通信（国内総合通信社）",
    "name": "Jiji Press (時事通信社)",
    "badge": "🇯🇵 日本の重要ニュース・国際経済・政策",
    "point": "日本の国策や半導体産業（ラピダス）、安全保障の最前線を客観的に伝える通信社です。日本語の重要ニュースを高校生レベルの標準英語に翻訳した記事を読むことで、日本の課題を世界に発信する表現力が身につきます。",
    "tip": "ニュースでよく聞くカタカナ語や政策用語（サプライチェーン、半導体など）が英語でどう表現されるかに注目しましょう。"
  },
  {
    "key": "yahoo",
    "title_en": "Yahoo! News Japan",
    "title_ja": "Yahoo!ニュース（教育・社会特集）",
    "name": "Yahoo! News Japan (Yahoo!ニュース)",
    "badge": "🎒 教育・健康・身近な生活課題",
    "point": "ランドセルの重さやタブレット端末の活用など、中高生自身の生活に密着したホットな話題を扱います。身近な問題だからこそ英語でも共感しやすく、英検の意見論述で自分の考えを述べる材料になります。",
    "tip": "『賛成の理由・反対の理由』を整理しながら読むと、自由英作文のライティング力が劇的にアップします。"
  },
  {
    "key": "getnews",
    "title_en": "GetNews Japan",
    "title_ja": "ガジェット通信（エンタメ・新技術）",
    "name": "GetNews Japan (ガジェット通信)",
    "badge": "🕶️ 最新ガジェット・AI・エンタメ",
    "point": "スマートグラスや最新AIツール、ポップカルチャーのワクワクする進化をいち早くレポートします。『テクノロジーの便利さ』と『使う側のマナー・ルール』の両面を楽しく学べます。",
    "tip": "新しいデジタル機器の説明に出てくる最新のIT英語やカタカナ言葉を、高校基本英語と結びつけて覚えられます。"
  }
];
