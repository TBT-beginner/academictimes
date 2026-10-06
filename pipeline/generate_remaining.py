# -*- coding: utf-8 -*-
import os
import asyncio
import edge_tts
import sys
sys.path.append(os.path.dirname(__file__))
from articles_data import ARTICLES
from generate_all_articles import build_article_html, VOICE_BRITISH, VOICE_KEITA, VOICE_NANAMI

async def save_tts(text, voice, out_path, sem):
    if os.path.exists(out_path) and os.path.getsize(out_path) > 100:
        return
    for attempt in range(3):
        async with sem:
            try:
                communicate = edge_tts.Communicate(text, voice)
                await asyncio.wait_for(communicate.save(out_path), timeout=12.0)
                return
            except Exception as e:
                print(f"Retry {attempt+1} for {out_path}: {e}")
                await asyncio.sleep(1)

async def generate_remaining():
    sem = asyncio.Semaphore(4)
    missing_slugs = ['mediterranean-marine-heatwaves', 'generative-ai-paleontology']
    for art in ARTICLES:
        if art['slug'] not in missing_slugs:
            continue
        cat = art['category']
        slug = art['slug']
        art_dir = os.path.join("news_portal", cat, slug)
        audio_dir = os.path.join(art_dir, "audio")
        os.makedirs(audio_dir, exist_ok=True)
        
        # 1. HTML
        html_content = build_article_html(art)
        html_path = os.path.join(art_dir, "index.html")
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(html_content)
        print(f"Generated HTML for {cat}/{slug}")
        
        # 2. Audio tasks
        tasks = []
        tasks.append(save_tts(art['title'], VOICE_BRITISH, os.path.join(audio_dir, "headline.mp3"), sem))
        full_text = " ".join([s['en'] for s in art['sentences']])
        tasks.append(save_tts(full_text, VOICE_BRITISH, os.path.join(audio_dir, "full_body.mp3"), sem))
        for idx, s in enumerate(art['sentences'], 1):
            tasks.append(save_tts(s['en'], VOICE_BRITISH, os.path.join(audio_dir, f"s{idx}.mp3"), sem))
        for idx, t in enumerate(art['dialogue'], 1):
            v = VOICE_NANAMI if t['speaker'] == "Nanami" else VOICE_KEITA
            tasks.append(save_tts(t['text'], v, os.path.join(audio_dir, f"dlg_{idx:02d}.mp3"), sem))
            
        await asyncio.gather(*tasks)
        print(f"Generated Audio for {cat}/{slug}")

if __name__ == "__main__":
    asyncio.run(generate_remaining())
