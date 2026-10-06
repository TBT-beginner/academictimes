import asyncio
import os
import edge_tts

VOICE = "en-GB-RyanNeural"
OUTPUT_DIR = r"c:\Users\teacher\Documents\lessonfactory\news_portal\culture\headphones-in-public\audio"

pronunciation_items = {
    # 1. hの脱落・連結 (ditch her -> "ditch-er")
    "pron_ditch_her.mp3": "ditch her. She decided to ditch her earbuds.",
    # 2. リンキング (lull of -> "lull-ov")
    "pron_lull_of.mp3": "lull of. Every quiet lull of the day.",
    # 3. 破裂音tの脱落 (against wearing -> "agains-wearing")
    "pron_against_wearing.mp3": "against wearing. The case against wearing headphones.",
    # 4. カタカナと違うアクセント (revery vs diminish)
    "pron_revery_accent.mp3": "revery. revery. lost in revery.",
    "pron_diminish_accent.mp3": "diminish. di-min-ish. It will diminish over time."
}

async def generate_pron():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    print("Generating pronunciation guide audio files...")
    for filename, text in pronunciation_items.items():
        filepath = os.path.join(OUTPUT_DIR, filename)
        comm = edge_tts.Communicate(text, VOICE)
        await comm.save(filepath)
        print(f"Generated: {filename}")
    print("Pronunciation audio files ready!")

if __name__ == "__main__":
    asyncio.run(generate_pron())
