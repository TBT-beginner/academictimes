# -*- coding: utf-8 -*-
"""
Generates high-quality Edge-TTS audio for Batch 23 articles (Senior and Junior).
- Senior English: en-GB-RyanNeural (standard pace)
- Junior English: en-GB-RyanNeural (-10% pace)
- Nanami (Dialogue): ja-JP-NanamiNeural
- Keita (Dialogue): ja-JP-KeitaNeural
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
    print(f"=== Synthesizing Edge-TTS Audio for Batch 23 (2026-10-27) ===")
    tasks = []

    # 1. Senior Articles
    for art in data_batch23.BATCH23_SENIOR:
        cat = art["category"]
        slug = art["slug"]
        audio_dir = os.path.join(PORTAL_DIR, "audio", cat, slug)

        # Sentences (1-5)
        for idx, s in enumerate(art["sentences"]):
            out_file = os.path.join(audio_dir, f"sentence_{idx+1}.mp3")
            tasks.append(generate_audio_file(s["en"], VOICE_EN, out_file))

        # Dialogue (1-4)
        for idx, d in enumerate(art["dialogue"]):
            out_file = os.path.join(audio_dir, f"dialogue_{idx+1}.mp3")
            voice = VOICE_NANAMI if d["speaker"] == "七" else VOICE_KEITA
            tasks.append(generate_audio_file(d["text"], voice, out_file))

        # Full English Narration
        full_text = " ".join([s["en"] for s in art["sentences"]])
        full_file = os.path.join(audio_dir, "full_audio.mp3")
        tasks.append(generate_audio_file(full_text, VOICE_EN, full_file))

        # Full Dialogue
        full_dlg_file = os.path.join(audio_dir, "dialogue_full.mp3")
        # In portal, dialogue_full is typically a single speech or synthesized
        first_dlg_voice = VOICE_NANAMI if art["dialogue"][0]["speaker"] == "七" else VOICE_KEITA
        full_dlg_text = " ".join([f"{d['name']}：{d['text']}" for d in art["dialogue"]])
        tasks.append(generate_audio_file(full_dlg_text, first_dlg_voice, full_dlg_file))

    # 2. Junior Articles
    for art in data_batch23.BATCH23_JUNIOR:
        cat = art["category"]
        slug = art["slug"]
        audio_dir = os.path.join(PORTAL_DIR, "junior", "audio", cat, slug)

        # Sentences (1-5) at -10% pace
        for idx, s in enumerate(art["sentences"]):
            out_file = os.path.join(audio_dir, f"sentence_{idx+1}.mp3")
            tasks.append(generate_audio_file(s["en"], VOICE_EN, out_file, rate="-10%"))

        # Dialogue (1-4)
        for idx, d in enumerate(art["dialogue"]):
            out_file = os.path.join(audio_dir, f"dialogue_{idx+1}.mp3")
            voice = VOICE_NANAMI if d["speaker"] == "七" else VOICE_KEITA
            tasks.append(generate_audio_file(d["text"], voice, out_file))

        # Full English Narration
        full_text = " ".join([s["en"] for s in art["sentences"]])
        full_file = os.path.join(audio_dir, "full_audio.mp3")
        tasks.append(generate_audio_file(full_text, VOICE_EN, full_file, rate="-10%"))

        # Full Dialogue
        full_dlg_file = os.path.join(audio_dir, "dialogue_full.mp3")
        first_dlg_voice = VOICE_NANAMI if art["dialogue"][0]["speaker"] == "七" else VOICE_KEITA
        full_dlg_text = " ".join([f"{d['name']}：{d['text']}" for d in art["dialogue"]])
        tasks.append(generate_audio_file(full_dlg_text, first_dlg_voice, full_dlg_file))

    print(f"Total audio tracks to synthesize: {len(tasks)}")
    
    # Process in batches of 15
    batch_size = 15
    success_count = 0
    for i in range(0, len(tasks), batch_size):
        chunk = tasks[i:i+batch_size]
        results = await asyncio.gather(*chunk)
        success_count += sum(1 for r in results if r)
        print(f"Synthesized {min(i+batch_size, len(tasks))}/{len(tasks)} tracks...")

    print(f"Audio synthesis complete: {success_count}/{len(tasks)} files ready.")

if __name__ == "__main__":
    asyncio.run(main())
