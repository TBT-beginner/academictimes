# -*- coding: utf-8 -*-
"""Generate Audio for Batch 22 (Senior & Junior)"""
import os
import sys
import asyncio
import edge_tts

PIPELINE_DIR = os.path.dirname(os.path.abspath(__file__))
PORTAL_DIR = os.path.abspath(os.path.join(PIPELINE_DIR, ".."))

sys.path.insert(0, PIPELINE_DIR)
from data_batch22 import BATCH22_SENIOR, BATCH22_JUNIOR

VOICE_BRITISH = "en-GB-RyanNeural"
VOICE_KEITA = "ja-JP-KeitaNeural"
VOICE_NANAMI = "ja-JP-NanamiNeural"

async def synth(text, voice, out_path, sem, rate="+0%"):
    async with sem:
        if os.path.exists(out_path) and os.path.getsize(out_path) > 500:
            return
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        for attempt in range(4):
            try:
                comm = edge_tts.Communicate(text, voice, rate=rate)
                await asyncio.wait_for(comm.save(out_path), timeout=25)
                if os.path.exists(out_path) and os.path.getsize(out_path) > 500:
                    print(f"[OK] {os.path.relpath(out_path, PORTAL_DIR)}")
                    return
            except Exception as e:
                if os.path.exists(out_path) and os.path.getsize(out_path) <= 500:
                    try:
                        os.remove(out_path)
                    except OSError:
                        pass
                if attempt == 3:
                    print(f"[ERR] {out_path}: {e}")
                else:
                    await asyncio.sleep(1.5 * (attempt + 1))

async def generate_batch_audio():
    sem = asyncio.Semaphore(5)
    tasks = []

    # 1. Senior articles
    for art in BATCH22_SENIOR:
        cat = art["category"]
        slug = art["slug"]
        audio_dir = os.path.join(PORTAL_DIR, cat, slug, "audio")
        
        # headline
        tasks.append(synth(art["title"], VOICE_BRITISH, os.path.join(audio_dir, "headline.mp3"), sem))
        # full body
        body = " ".join([s["en"] for s in art["sentences"]])
        tasks.append(synth(body, VOICE_BRITISH, os.path.join(audio_dir, "full_body.mp3"), sem))
        # sentences
        for i, s in enumerate(art["sentences"]):
            tasks.append(synth(s["en"], VOICE_BRITISH, os.path.join(audio_dir, f"s{i+1}.mp3"), sem))
        # dialogue
        for i, dlg in enumerate(art["dialogue"]):
            v = VOICE_KEITA if dlg["speaker"] == "慶" else VOICE_NANAMI
            tasks.append(synth(dlg["text"], v, os.path.join(audio_dir, f"dlg_{i+1:02d}.mp3"), sem))

    # 2. Junior articles
    for art in BATCH22_JUNIOR:
        cat = art["category"]
        slug = art["slug"]
        audio_dir = os.path.join(PORTAL_DIR, "junior", cat, slug, "audio")
        
        # headline (rate -10%)
        tasks.append(synth(art["title"], VOICE_BRITISH, os.path.join(audio_dir, "headline.mp3"), sem, rate="-10%"))
        # full body (rate -10%)
        body = " ".join([s["en"] for s in art["sentences"]])
        tasks.append(synth(body, VOICE_BRITISH, os.path.join(audio_dir, "full_body.mp3"), sem, rate="-10%"))
        # sentences (rate -10%)
        for i, s in enumerate(art["sentences"]):
            tasks.append(synth(s["en"], VOICE_BRITISH, os.path.join(audio_dir, f"s{i+1}.mp3"), sem, rate="-10%"))
        # dialogue
        for i, dlg in enumerate(art["dialogue"]):
            v = VOICE_KEITA if dlg["speaker"] == "慶" else VOICE_NANAMI
            tasks.append(synth(dlg["text"], v, os.path.join(audio_dir, f"dlg_{i+1:02d}.mp3"), sem))

    print(f"Total audio synthesis tasks queued: {len(tasks)}")
    await asyncio.gather(*tasks)
    print("All Batch 22 audio generated successfully!")

if __name__ == "__main__":
    asyncio.run(generate_batch_audio())
