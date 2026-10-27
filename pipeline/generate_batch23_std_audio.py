# -*- coding: utf-8 -*-
"""
Generates proper audio files for Batch 23 matching the schema expected by source_verifier:
Files per article:
- headline.mp3
- full_body.mp3
- s1.mp3, s2.mp3, s3.mp3, s4.mp3, s5.mp3
- dlg_01.mp3, dlg_02.mp3, dlg_03.mp3, dlg_04.mp3

Paths:
- Senior: news_portal/{cat}/{slug}/audio/
- Junior: news_portal/junior/{cat}/{slug}/audio/
"""

import os
import sys
import asyncio
import edge_tts

PIPELINE_DIR = os.path.dirname(os.path.abspath(__file__))
PORTAL_DIR = os.path.abspath(os.path.join(PIPELINE_DIR, ".."))

import data_batch23

VOICE_EN = "en-GB-RyanNeural"
VOICE_NANAMI = "ja-JP-NanamiNeural"
VOICE_KEITA = "ja-JP-KeitaNeural"

async def generate_audio_file(text, voice, out_path, rate=None):
    if os.path.exists(out_path) and os.path.getsize(out_path) > 500:
        return True
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    try:
        kwargs = {"voice": voice}
        if rate:
            kwargs["rate"] = rate
        communicate = edge_tts.Communicate(text, **kwargs)
        await communicate.save(out_path)
        return True
    except Exception as e:
        print(f"[ERR] Failed {out_path}: {e}")
        return False

async def main():
    print(f"=== Synthesizing Standard Format Audio for Batch 23 ===")
    tasks = []

    # 1. Senior Articles
    for art in data_batch23.BATCH23_SENIOR:
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
            voice = VOICE_NANAMI if d["speaker"] == "七" else VOICE_KEITA
            tasks.append(generate_audio_file(d["text"], voice, out_file))

    # 2. Junior Articles
    for art in data_batch23.BATCH23_JUNIOR:
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
            voice = VOICE_NANAMI if d["speaker"] == "七" else VOICE_KEITA
            tasks.append(generate_audio_file(d["text"], voice, out_file))

    print(f"Total audio tracks to synthesize: {len(tasks)}")
    batch_size = 15
    success_count = 0
    for i in range(0, len(tasks), batch_size):
        chunk = tasks[i:i+batch_size]
        results = await asyncio.gather(*chunk)
        success_count += sum(1 for r in results if r)
        print(f"Synthesized {min(i+batch_size, len(tasks))}/{len(tasks)} tracks...")

    print(f"Standard audio synthesis complete: {success_count}/{len(tasks)} files ready.")

if __name__ == "__main__":
    asyncio.run(main())
