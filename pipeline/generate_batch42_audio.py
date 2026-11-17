# -*- coding: utf-8 -*-
"""Generate Edge-TTS audio for Batch 42 (12 Senior + 12 Junior = 24 articles, 264 MP3s)."""

import asyncio
import os
import sys
import edge_tts

PIPELINE_DIR = os.path.dirname(os.path.abspath(__file__))
PORTAL_DIR = os.path.abspath(os.path.join(PIPELINE_DIR, ".."))
sys.path.insert(0, PIPELINE_DIR)

from batch42_articles_data import BATCH42_SENIOR, BATCH42_JUNIOR

VOICE_EN = "en-GB-RyanNeural"
VOICE_KEITA = "ja-JP-KeitaNeural"
VOICE_NANAMI = "ja-JP-NanamiNeural"


async def synth(sem: asyncio.Semaphore, text: str, voice: str, out_path: str, rate: str = "+0%"):
    if os.path.exists(out_path) and os.path.getsize(out_path) > 500:
        return True
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    async with sem:
        for attempt in range(4):
            try:
                comm = edge_tts.Communicate(text, voice, rate=rate)
                await comm.save(out_path)
                if os.path.exists(out_path) and os.path.getsize(out_path) > 500:
                    return True
            except Exception as e:
                if attempt == 3:
                    print(f"[ERROR] {out_path}: {e}", flush=True)
                    return False
                await asyncio.sleep(1.5 * (attempt + 1))
    return False


def build_jobs(articles, is_junior: bool):
    jobs = []
    rate = "-10%" if is_junior else "+0%"
    base_prefix = os.path.join(PORTAL_DIR, "junior") if is_junior else PORTAL_DIR
    for art in articles:
        cat = art["category"]
        slug = art["slug"]
        audio_dir = os.path.join(base_prefix, cat, slug, "audio")
        jobs.append((art["title"], VOICE_EN, os.path.join(audio_dir, "headline.mp3"), rate))
        sents = art["sentences"]
        for i, s in enumerate(sents, 1):
            jobs.append((s["en"], VOICE_EN, os.path.join(audio_dir, f"s{i}.mp3"), rate))
        full_text = " ".join(s["en"] for s in sents)
        jobs.append((full_text, VOICE_EN, os.path.join(audio_dir, "full_body.mp3"), rate))
        for i, d in enumerate(art["dialogue"], 1):
            spk = str(d.get("speaker", "")).lower()
            voice = VOICE_KEITA if ("keita" in spk or "慶" in spk) else VOICE_NANAMI
            jobs.append((d["text"], voice, os.path.join(audio_dir, f"dlg_{i:02d}.mp3"), "+0%"))
    return jobs


async def main():
    jobs = build_jobs(BATCH42_SENIOR, is_junior=False) + build_jobs(BATCH42_JUNIOR, is_junior=True)
    print(f"Total audio jobs queued: {len(jobs)} (24 articles)", flush=True)
    sem = asyncio.Semaphore(12)
    results = await asyncio.gather(*(synth(sem, t, v, p, r) for (t, v, p, r) in jobs))
    ok = sum(1 for r in results if r)
    print(f"Completed: {ok}/{len(jobs)} MP3 files.", flush=True)
    if ok != len(jobs):
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())
