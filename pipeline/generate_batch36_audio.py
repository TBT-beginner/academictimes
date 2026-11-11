# -*- coding: utf-8 -*-
"""Generate audio for Batch 36 (2026-11-12)."""

import os
import sys
import asyncio
import edge_tts

PIPELINE_DIR = os.path.dirname(os.path.abspath(__file__))
PORTAL_DIR = os.path.abspath(os.path.join(PIPELINE_DIR, ".."))
if PIPELINE_DIR not in sys.path:
    sys.path.insert(0, PIPELINE_DIR)

from batch36_articles_data import BATCH36_SENIOR, BATCH36_JUNIOR

VOICE_EN = "en-GB-RyanNeural"
VOICE_NANAMI = "ja-JP-NanamiNeural"
VOICE_KEITA = "ja-JP-KeitaNeural"

sem = asyncio.Semaphore(8)

async def generate_audio_file(text, voice, out_path, rate=None):
    if not text or not text.strip():
        return True
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
                await asyncio.wait_for(communicate.save(out_path), timeout=30)
                if os.path.exists(out_path) and os.path.getsize(out_path) > 500:
                    return True
            except Exception as e:
                if attempt == 2:
                    print(f"[FAIL] {out_path}: {e}")
                await asyncio.sleep(1)
    return False

async def generate_for_article(art, is_junior=False):
    cat = art["category"]
    slug = art["slug"]
    rate = "-10%" if is_junior else None

    if is_junior:
        audio_dir = os.path.join(PORTAL_DIR, "junior", cat, slug, "audio")
    else:
        audio_dir = os.path.join(PORTAL_DIR, cat, slug, "audio")
    os.makedirs(audio_dir, exist_ok=True)

    tasks = []

    # 1. Headline
    headline_text = art.get("title", "")
    tasks.append(generate_audio_file(headline_text, VOICE_EN, os.path.join(audio_dir, "headline.mp3"), rate=rate))

    # 2. Sentences s1..s5
    sentences = art.get("sentences", [])
    full_text_list = []
    for idx, s_obj in enumerate(sentences, start=1):
        s_text = s_obj.get("en") or s_obj.get("s", "")
        full_text_list.append(s_text)
        tasks.append(generate_audio_file(s_text, VOICE_EN, os.path.join(audio_dir, f"s{idx}.mp3"), rate=rate))

    # 3. Full body
    full_body_text = " ".join(full_text_list)
    tasks.append(generate_audio_file(full_body_text, VOICE_EN, os.path.join(audio_dir, "full_body.mp3"), rate=rate))

    # 4. Dialogue dlg_01..dlg_06
    dialogue = art.get("dialogue", [])
    for idx, d_turn in enumerate(dialogue, start=1):
        spk = d_turn.get("speaker", "").lower()
        d_text = d_turn.get("text", "")
        voice = VOICE_KEITA if ("keita" in spk or "慶" in spk) else VOICE_NANAMI
        d_ja_text = d_turn.get("translation", d_text)
        tasks.append(generate_audio_file(d_ja_text, voice, os.path.join(audio_dir, f"dlg_{idx:02d}.mp3")))

    results = await asyncio.gather(*tasks)
    return all(results)

async def main():
    all_articles = [
        (BATCH36_SENIOR, False, "Batch 36 Senior"),
        (BATCH36_JUNIOR, True, "Batch 36 Junior"),
    ]

    for arts, is_junior, label in all_articles:
        print(f"Generating audio for {label} ({len(arts)} articles)...")
        tasks = [generate_for_article(a, is_junior=is_junior) for a in arts]
        results = await asyncio.gather(*tasks)
        success = sum(1 for r in results if r)
        print(f"[{label}] {success}/{len(arts)} articles complete.")

if __name__ == "__main__":
    asyncio.run(main())
