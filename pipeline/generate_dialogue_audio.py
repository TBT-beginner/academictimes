import asyncio
import os
import edge_tts

VOICE_MALE = "ja-JP-KeitaNeural"    # ケンジ先生（男性講師）
VOICE_FEMALE = "ja-JP-NanamiNeural" # アオイさん（女性アシスタント）
OUTPUT_DIR = r"c:\Users\teacher\Documents\lessonfactory\news_portal\culture\headphones-in-public\audio"

dialogue_lines = [
    {
        "id": "dlg_01.mp3",
        "speaker": "Aoi",
        "voice": VOICE_FEMALE,
        "text": "先生、今日のTIME誌の記事、タイトルを見てびっくりしました。『公共の場でイヤホンをつけるな』って…私、登下校の電車の中では1秒も欠かさず音楽や動画を聴いてますよ！"
    },
    {
        "id": "dlg_02.mp3",
        "speaker": "Kenji",
        "voice": VOICE_MALE,
        "text": "あはは、アオイさんだけじゃないよ。記事にあるイギリスの調査だと、大人の9割以上が毎週音声を聴いていて、4人に1人はポッドキャストを聴いてるんだ。現代人って『日常のちょっとした隙間時間』を音で埋め尽くしちゃうんだよね。"
    },
    {
        "id": "dlg_03.mp3",
        "speaker": "Aoi",
        "voice": VOICE_FEMALE,
        "text": "でも、退屈な時間を好きな音楽で埋めるのって、時間を有効に使えて良いことじゃないんですか？"
    },
    {
        "id": "dlg_04.mp3",
        "speaker": "Kenji",
        "voice": VOICE_MALE,
        "text": "それがね、心理学の研究によると大きな落とし穴があるんだ。人間って、何も聴かずに『ぼーっとする時間、レベリー』があるからこそ、頭の中でアイデアが結びついたり、新しい発想が生まれたりする。ずっと音を流していると、その大切な創造の時間を脳から奪ってしまうんだね。"
    },
    {
        "id": "dlg_05.mp3",
        "speaker": "Aoi",
        "voice": VOICE_FEMALE,
        "text": "なるほど…！あと記事に『見知らぬ人との関わり』の話もありましたよね？"
    },
    {
        "id": "dlg_06.mp3",
        "speaker": "Kenji",
        "voice": VOICE_MALE,
        "text": "そう！電車で隣の人にちょっと会釈したり、店員さんと一言交わしたりするだけで、人は予想以上に心が温まるという実験結果が出ているんだ。イヤホンは『話しかけないで』という見えない壁を作っちゃう。だから筆者は『たまにはイヤホンを外して、街の息づかいに意識を向けてみよう』と提案しているんだよ。"
    },
    {
        "id": "dlg_07.mp3",
        "speaker": "Aoi",
        "voice": VOICE_FEMALE,
        "text": "すごく納得しました！入試の自由英作文でも『デジタル機器と孤独』は定番テーマですし、私も明日の通学、片道だけイヤホンを外して歩いてみます！"
    }
]

async def generate_dialogue():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    print("Generating Japanese dialogue audio with edge-tts...")
    
    # Generate individual lines
    for item in dialogue_lines:
        filepath = os.path.join(OUTPUT_DIR, item["id"])
        comm = edge_tts.Communicate(item["text"], item["voice"])
        await comm.save(filepath)
        print(f"Generated {item['speaker']}: {item['id']}")
        
    print("All dialogue audios generated!")

if __name__ == "__main__":
    asyncio.run(generate_dialogue())
