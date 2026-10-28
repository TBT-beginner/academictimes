# -*- coding: utf-8 -*-
"""
Robust audio generator for Batch 25 with timeout, retries, and semaphore concurrency.
"""

import os
import sys
import asyncio
import edge_tts

PIPELINE_DIR = os.path.dirname(os.path.abspath(__file__))
PORTAL_DIR = os.path.abspath(os.path.join(PIPELINE_DIR, ".."))

import data_batch25

VOICE_EN = "en-GB-RyanNeural"
VOICE_NANAMI = "ja-JP-NanamiNeural"
VOICE_KEITA = "ja-JP-KeitaNeural"

sem = asyncio.Semaphore(6)

async def generate_audio_file(text, voice, out_path, rate=None):
    if os.path.exists(out_path) and os.path.getsize(out_path) > 500:
        return True
    os.makedirs(os.path.dirname(out_path), exist_ok=True)

    for attempt in range(3):
        async with sem:
            try:
                kwargs = {"voice": voice}
                if rate:
                    kwargs["rate"] = rate
                communicate = edge_tts.Communicate(text, **kwargs)
                await asyncio.wait_for(communicate.save(out_path), timeout=15)
                if os.path.exists(out_path) and os.path.getsize(out_path) > 500:
                    return True
            except Exception as e:
                if attempt == 2:
                    print(f"[ERR] Failed {os.path.basename(out_path)} after 3 attempts: {e}", flush=True)
                await asyncio.sleep(1)
    return False

async def main():
    print("=== Robust Synthesizing Standard Format Audio for Batch 25 ===", flush=True)
    tasks = []

    # 1. Senior Articles
    for art in data_batch25.BATCH25_SENIOR:
        cat = art["category"]
        slug = art["slug"]
        audio_dir = os.path.join(PORTAL_DIR, cat, slug, "audio")

        # headline.mp3
        tasks.append(generate_audio_file(art["title"], VOICE_EN, os.path.join(audio_dir, "headline.mp3")))

        # full_body.mp3
        full_text = " ".join([s["en"] for s in art["sentences"]])
        tasks.append(generate_audio_file(full_text, VOICE_EN, os.path.join(audio_dir, "full_body.mp3")))

        # s1.mp3 to s5.mp3
        for idx, s in enumerate(art["sentences"]):
            out_file = os.path.join(audio_dir, f"s{idx+1}.mp3")
            tasks.append(generate_audio_file(s["en"], VOICE_EN, out_file))

        # dlg_01.mp3 to dlg_04.mp3
        for idx, d in enumerate(art["dialogue"]):
            out_file = os.path.join(audio_dir, f"dlg_{idx+1:02d}.mp3")
            voice = VOICE_NANAMI if d["speaker"] in ["七", "ナナミ", "Nanami"] else VOICE_KEITA
            tasks.append(generate_audio_file(d["text"], voice, out_file))

    # 2. Junior Articles
    for art in data_batch25.BATCH25_JUNIOR:
        cat = art["category"]
        slug = art["slug"]
        audio_dir = os.path.join(PORTAL_DIR, "junior", cat, slug, "audio")

        # headline.mp3 (-10%)
        tasks.append(generate_audio_file(art["title"], VOICE_EN, os.path.join(audio_dir, "headline.mp3"), rate="-10%"))

        # full_body.mp3 (-10%)
        full_text = " ".join([s["en"] for s in art["sentences"]])
        tasks.append(generate_audio_file(full_text, VOICE_EN, os.path.join(audio_dir, "full_body.mp3"), rate="-10%"))

        # s1.mp3 to s5.mp3 (-10%)
        for idx, s in enumerate(art["sentences"]):
            out_file = os.path.join(audio_dir, f"s{idx+1}.mp3")
            tasks.append(generate_audio_file(s["en"], VOICE_EN, out_file, rate="-10%"))

        # dlg_01.mp3 to dlg_04.mp3
        for idx, d in enumerate(art["dialogue"]):
            out_file = os.path.join(audio_dir, f"dlg_{idx+1:02d}.mp3")
            voice = VOICE_NANAMI if d["speaker"] in ["七", "ナナミ", "Nanami"] else VOICE_KEITA
            tasks.append(generate_audio_file(d["text"], voice, out_file))

    print(f"Total audio tracks to synthesize: {len(tasks)}", flush=True)
    results = await asyncio.gather(*tasks)
    success_count = sum(1 for r in results if r)
    print(f"Standard audio synthesis complete: {success_count}/{len(tasks)} files ready.", flush=True)

if __name__ == "__main__":
    asyncio.run(main())
