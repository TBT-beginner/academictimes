# -*- coding: utf-8 -*-
"""Generate audio for Batch 30 (2026-11-03)."""

import os
import sys
import asyncio
import edge_tts

PIPELINE_DIR = os.path.dirname(os.path.abspath(__file__))
PORTAL_DIR = os.path.abspath(os.path.join(PIPELINE_DIR, ".."))
if PIPELINE_DIR not in sys.path:
    sys.path.insert(0, PIPELINE_DIR)

from data_batch30 import BATCH30_SENIOR, BATCH30_JUNIOR

VOICE_EN = "en-GB-RyanNeural"
VOICE_NANAMI = "ja-JP-NanamiNeural"
VOICE_KEITA = "ja-JP-KeitaNeural"

sem = asyncio.Semaphore(8)

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
                await asyncio.wait_for(communicate.save(out_path), timeout=20)
                if os.path.exists(out_path) and os.path.getsize(out_path) > 500:
                    return True
            except Exception as e:
                if attempt == 2:
                    print(f"[ERR] Failed {os.path.basename(out_path)} after 3 attempts: {e}", flush=True)
                await asyncio.sleep(1)
    return False

async def main():
    print("=== Synthesizing Standard Audio for Batch 30 ===", flush=True)
    tasks = []

    # 1. Senior Articles
    for art in BATCH30_SENIOR:
        cat = art["category"]
        slug = art["slug"]
        audio_dir = os.path.join(PORTAL_DIR, cat, slug, "audio")

        tasks.append(generate_audio_file(art["title"], VOICE_EN, os.path.join(audio_dir, "headline.mp3")))
        full_text = " ".join([s["en"] for s in art["sentences"]])
        tasks.append(generate_audio_file(full_text, VOICE_EN, os.path.join(audio_dir, "full_body.mp3")))

        for idx, s in enumerate(art["sentences"]):
            out_file = os.path.join(audio_dir, f"s{idx+1}.mp3")
            tasks.append(generate_audio_file(s["en"], VOICE_EN, out_file))

        dialogue = art.get("dialogue") or art.get("dialog", [])
        for idx, d in enumerate(dialogue):
            out_file = os.path.join(audio_dir, f"dlg_{idx+1:02d}.mp3")
            spk = d.get("speaker", "")
            voice = VOICE_NANAMI if ("nanami" in spk.lower() or "七" in spk) else VOICE_KEITA
            tasks.append(generate_audio_file(d["text"], voice, out_file))

    # 2. Junior Articles
    for art in BATCH30_JUNIOR:
        cat = art["category"]
        slug = art["slug"]
        audio_dir = os.path.join(PORTAL_DIR, "junior", cat, slug, "audio")

        tasks.append(generate_audio_file(art["title"], VOICE_EN, os.path.join(audio_dir, "headline.mp3"), rate="-10%"))
        full_text = " ".join([s["en"] for s in art["sentences"]])
        tasks.append(generate_audio_file(full_text, VOICE_EN, os.path.join(audio_dir, "full_body.mp3"), rate="-10%"))

        for idx, s in enumerate(art["sentences"]):
            out_file = os.path.join(audio_dir, f"s{idx+1}.mp3")
            tasks.append(generate_audio_file(s["en"], VOICE_EN, out_file, rate="-10%"))

        dialogue = art.get("dialogue") or art.get("dialog", [])
        for idx, d in enumerate(dialogue):
            out_file = os.path.join(audio_dir, f"dlg_{idx+1:02d}.mp3")
            spk = d.get("speaker", "")
            voice = VOICE_NANAMI if ("nanami" in spk.lower() or "七" in spk) else VOICE_KEITA
            tasks.append(generate_audio_file(d["text"], voice, out_file))

    print(f"Total audio tracks to synthesize: {len(tasks)}", flush=True)
    results = await asyncio.gather(*tasks)
    success_count = sum(1 for r in results if r)
    print(f"Standard audio synthesis complete: {success_count}/{len(tasks)} files ready.", flush=True)

if __name__ == "__main__":
    asyncio.run(main())
