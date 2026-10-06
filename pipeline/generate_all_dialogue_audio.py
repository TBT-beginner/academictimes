# -*- coding: utf-8 -*-
"""
Synthesizes high-quality Edge-TTS audio for all 14 articles' new dialogues.
Keita: ja-JP-KeitaNeural
Nanami: ja-JP-NanamiNeural
"""
import asyncio
import os
import sys
import edge_tts
sys.path.insert(0, os.path.dirname(__file__))
from articles_data import ARTICLES

VOICE_KEITA = "ja-JP-KeitaNeural"
VOICE_NANAMI = "ja-JP-NanamiNeural"

PORTAL_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

async def synth_line(text, voice, out_path, sem):
    async with sem:
        for attempt in range(3):
            try:
                comm = edge_tts.Communicate(text, voice)
                await comm.save(out_path)
                return
            except Exception as e:
                if attempt == 2:
                    print(f"[ERR] Failed {out_path}: {e}")
                else:
                    await asyncio.sleep(1)

async def main():
    sem = asyncio.Semaphore(5)
    tasks = []
    
    print(f"Synthesizing dialogue audio for {len(ARTICLES)} articles...")
    
    for art in ARTICLES:
        slug = art["slug"]
        cat = art["category"]
        audio_dir = os.path.join(PORTAL_DIR, cat, slug, "audio")
        os.makedirs(audio_dir, exist_ok=True)
        
        for i, dlg in enumerate(art["dialogue"]):
            voice = VOICE_KEITA if (dlg["speaker"] == "慶" or "Keita" in dlg["name"]) else VOICE_NANAMI
            out_file = os.path.join(audio_dir, f"dlg_{i+1:02d}.mp3")
            tasks.append(synth_line(dlg["text"], voice, out_file, sem))
            
    total = len(tasks)
    print(f"Total audio files to generate: {total}")
    await asyncio.gather(*tasks)
    print("All dialogue audio generated successfully!")

if __name__ == "__main__":
    asyncio.run(main())
