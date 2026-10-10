# -*- coding: utf-8 -*-
"""
Synthesizes missing audio files for Senior articles:
- headline.mp3
- full_body.mp3 (copies from full.mp3 or synthesizes)
- dlg_01.mp3 to dlg_04.mp3 (copies from d1.mp3 or synthesizes)
"""

import os
import sys
import shutil
import asyncio
import edge_tts

sys.path.append(os.path.dirname(__file__))
from articles_data import ARTICLES

PORTAL_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
VOICE_BRITISH = "en-GB-RyanNeural"
VOICE_KEITA = "ja-JP-KeitaNeural"
VOICE_NANAMI = "ja-JP-NanamiNeural"

async def ensure_senior_audio():
    sem = asyncio.Semaphore(5)
    tasks = []

    async def synth_if_missing(text, voice, path):
        async with sem:
            if os.path.exists(path) and os.path.getsize(path) > 500:
                return
            try:
                comm = edge_tts.Communicate(text, voice)
                await comm.save(path)
                print(f"[SYNTH] {os.path.basename(path)} for {os.path.basename(os.path.dirname(os.path.dirname(path)))}")
            except Exception as e:
                print(f"[ERR] Failed {path}: {e}")

    for art in ARTICLES:
        cat = art["category"]
        slug = art["slug"]
        audio_dir = os.path.join(PORTAL_DIR, cat, slug, "audio")
        os.makedirs(audio_dir, exist_ok=True)

        # 1. Headline
        headline_path = os.path.join(audio_dir, "headline.mp3")
        if not os.path.exists(headline_path) or os.path.getsize(headline_path) < 500:
            tasks.append(synth_if_missing(art["title"], VOICE_BRITISH, headline_path))

        # 2. Full Body
        full_body_path = os.path.join(audio_dir, "full_body.mp3")
        full_path = os.path.join(audio_dir, "full.mp3")
        if not os.path.exists(full_body_path) or os.path.getsize(full_body_path) < 500:
            if os.path.exists(full_path) and os.path.getsize(full_path) > 500:
                shutil.copyfile(full_path, full_body_path)
            else:
                body_text = " ".join([s["en"] for s in art["sentences"]])
                tasks.append(synth_if_missing(body_text, VOICE_BRITISH, full_body_path))

        # 3. Sentences s1..s5
        for i, s in enumerate(art["sentences"]):
            s_path = os.path.join(audio_dir, f"s{i+1}.mp3")
            if not os.path.exists(s_path) or os.path.getsize(s_path) < 500:
                tasks.append(synth_if_missing(s["en"], VOICE_BRITISH, s_path))

        # 4. Dialogues (both dlg_0x.mp3 and dx.mp3)
        for i, dlg in enumerate(art.get("dialogue", [])):
            dlg_num = i + 1
            dlg_path = os.path.join(audio_dir, f"dlg_{dlg_num:02d}.mp3")
            d_short_path = os.path.join(audio_dir, f"d{dlg_num}.mp3")

            if not os.path.exists(dlg_path) and os.path.exists(d_short_path):
                shutil.copyfile(d_short_path, dlg_path)
            elif not os.path.exists(d_short_path) and os.path.exists(dlg_path):
                shutil.copyfile(dlg_path, d_short_path)
            elif not os.path.exists(dlg_path) and not os.path.exists(d_short_path):
                voice = VOICE_KEITA if dlg["speaker"] == "慶" else VOICE_NANAMI
                tasks.append(synth_if_missing(dlg["text"], voice, dlg_path))

    if tasks:
        print(f"Synthesizing {len(tasks)} missing Senior audio files...")
        await asyncio.gather(*tasks)
    print("All Senior audio files synchronized!")

if __name__ == "__main__":
    asyncio.run(ensure_senior_audio())
