import asyncio
import os
import edge_tts

# Voice configuration - using high-quality British English voice for scholarly newspaper aesthetic
VOICE = "en-GB-RyanNeural"
OUTPUT_DIR = r"c:\Users\teacher\Documents\lessonfactory\news_portal\culture\headphones-in-public\audio"

audio_items = {
    # Headline
    "headline.mp3": "The Case Against Wearing Headphones in Public",
    
    # Sentences in article
    "s1.mp3": "In an essay for TIME, journalist Meehika Barua argues that our habitual use of headphones in public is quietly diminishing our engagement with the world.",
    "s2.mp3": "During her daily commute in London, Barua decided to ditch her wireless earbuds and immediately noticed a profound shift in her awareness.",
    "s3.mp3": "According to recent research by Ofcom, 93 percent of U.K. adults listen to some form of audio weekly, filling nearly every quiet lull of the day.",
    "s4.mp3": "Psychologists warn that constant auditory stimulation deprives the human mind of revery, the unintentional daydreaming essential for creative thought.",
    "s5.mp3": "Furthermore, studies indicate that people routinely underestimate the emotional benefits of spontaneous, everyday interactions with strangers.",
    
    # Full article read-through
    "full_body.mp3": "In an essay for TIME, journalist Meehika Barua argues that our habitual use of headphones in public is quietly diminishing our engagement with the world. During her daily commute in London, Barua decided to ditch her wireless earbuds and immediately noticed a profound shift in her awareness. According to recent research by Ofcom, 93 percent of U.K. adults listen to some form of audio weekly, filling nearly every quiet lull of the day. Psychologists warn that constant auditory stimulation deprives the human mind of revery, the unintentional daydreaming essential for creative thought. Furthermore, studies indicate that people routinely underestimate the emotional benefits of spontaneous, everyday interactions with strangers.",

    # Vocabulary & example sentences
    "word_diminish.mp3": "diminish",
    "ex_diminish.mp3": "His influence began to diminish over time.",
    
    "word_ditch.mp3": "ditch",
    "ex_ditch.mp3": "She decided to ditch her old habits and embrace a healthier lifestyle.",
    
    "word_lull.mp3": "lull",
    "ex_lull.mp3": "There was a brief lull in the conversation before the meeting resumed.",
    
    "word_revery.mp3": "revery",
    "ex_revery.mp3": "He was lost in revery and did not hear the door open.",
    
    "word_underestimate.mp3": "underestimate",
    "ex_underestimate.mp3": "Never underestimate the power of small daily habits.",
    
    "word_spontaneous.mp3": "spontaneous",
    "ex_spontaneous.mp3": "We took a spontaneous trip to the coast over the weekend."
}

async def generate_all():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    print(f"Generating {len(audio_items)} audio files with voice '{VOICE}'...")
    for filename, text in audio_items.items():
        filepath = os.path.join(OUTPUT_DIR, filename)
        comm = edge_tts.Communicate(text, VOICE)
        await comm.save(filepath)
        print(f"Generated: {filename}")
    print("All audio generated successfully!")

if __name__ == "__main__":
    asyncio.run(generate_all())
