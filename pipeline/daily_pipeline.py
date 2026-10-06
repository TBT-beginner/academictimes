"""
Daily 10+ Article Semi-Automated News Pipeline
Architecture & CLI Runner for THE ACADEMIC TIMES
"""

import os
import json
import asyncio
import edge_tts

# Default TTS Voice settings
VOICE_BRITISH = "en-GB-RyanNeural"
VOICE_AMERICAN = "en-US-GuyNeural"

# Target Categories for University Entrance English
CATEGORIES = {
    "society": "社会・心理・教育（孤独、都市論、認知心理学、格差、行動経済学）",
    "science": "科学・医学・環境（気候変動、AI・技術倫理、生物多様性、宇宙物理）",
    "culture": "文化・思想・文学（言語論、哲学、芸術、歴史的評伝、メディア論）",
    "law": "法律・司法・制度（基本的人権、憲法判断、国際法、バイオエシックス）",
    "world": "国際情勢・安全保障（条約、地政学、外交交渉、紛争の客観的解説）"
}

ARTICLE_SCHEMA = {
    "title": "記事タイトル（英語）",
    "headline_ja": "見出し和訳",
    "category": "society | science | culture | law | world",
    "source_name": "TIME | The Times | BBC | Reuters | Nature など",
    "source_url": "元記事のURL",
    "source_attribution": "「TIME誌（2026年10月5日号）にて〜が報じるところによると...」",
    "sentences": [
        {"en": "英文1", "ja": "和訳1"},
        {"en": "英文2", "ja": "和訳2"},
        {"en": "英文3", "ja": "和訳3"},
        {"en": "英文4", "ja": "和訳4"},
        {"en": "英文5", "ja": "和訳5"}
    ],
    "vocabulary": [
        {
            "word": "単語",
            "phonetic": "発音記号",
            "pos": "品詞",
            "meaning_ja": "日本語の意味",
            "definition_en": "英英定義",
            "example_en": "入試頻出例文",
            "example_ja": "例文和訳"
        }
    ],
    "syntax_points": [
        {
            "phrase": "注目構文・語法",
            "meaning": "要点",
            "explanation": "入試で問われる理由・関連表現（同格、分離のof、倒置など）"
        }
    ],
    "fact_check_notes": [
        "元記事に記載された正確な数値・固有名詞・研究論文出典の箇条書き"
    ],
    "quiz": [
        {
            "question": "問題文",
            "options": ["A", "B", "C", "D"],
            "correct_index": 1,
            "explanation": "正解の根拠と誤答の解説"
        }
    ],
    "faq": [
        {
            "q": "質問",
            "a": "回答"
        }
    ]
}

async def generate_article_audio(slug, category_dir, text_dict, voice=VOICE_BRITISH):
    """Generates all mp3 files for an article using edge-tts"""
    audio_dir = os.path.join(category_dir, slug, "audio")
    os.makedirs(audio_dir, exist_ok=True)
    
    for filename, text in text_dict.items():
        filepath = os.path.join(audio_dir, filename)
        comm = edge_tts.Communicate(text, voice)
        await comm.save(filepath)
    print(f"Generated {len(text_dict)} audio files for {slug}")

if __name__ == "__main__":
    print("THE ACADEMIC TIMES - Semi-Automated Pipeline Ready")
    print(f"Supported categories: {list(CATEGORIES.keys())}")
