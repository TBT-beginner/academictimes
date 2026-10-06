import asyncio
import edge_tts

async def test():
    t1 = "reverie. He was lost in reverie."
    t2 = "revery. He was lost in revery."
    
    c1 = edge_tts.Communicate(t1, "en-GB-RyanNeural")
    await c1.save("news_portal/culture/headphones-in-public/audio/test_reverie.mp3")
    print("reverie generated")

    # s4 with reverie
    s4_text = "Psychologists warn that constant auditory stimulation deprives the human mind of reverie, the unintentional daydreaming essential for creative thought."
    c4 = edge_tts.Communicate(s4_text, "en-GB-RyanNeural")
    await c4.save("news_portal/culture/headphones-in-public/audio/s4.mp3")
    print("s4 with reverie updated")

    # full body with reverie
    full_text = "In an essay for TIME, journalist Meehika Barua argues that our habitual use of headphones in public is quietly diminishing our engagement with the world. During her daily commute in London, Barua decided to ditch her wireless earbuds and immediately noticed a profound shift in her awareness. According to recent research by Ofcom, 93 percent of U.K. adults listen to some form of audio weekly, filling nearly every quiet lull of the day. Psychologists warn that constant auditory stimulation deprives the human mind of reverie, the unintentional daydreaming essential for creative thought. Furthermore, studies indicate that people routinely underestimate the emotional benefits of spontaneous, everyday interactions with strangers."
    c_full = edge_tts.Communicate(full_text, "en-GB-RyanNeural")
    await c_full.save("news_portal/culture/headphones-in-public/audio/full_body.mp3")
    print("full_body with reverie updated")

    # word and ex
    c_w = edge_tts.Communicate("reverie", "en-GB-RyanNeural")
    await c_w.save("news_portal/culture/headphones-in-public/audio/word_revery.mp3")

    c_ex = edge_tts.Communicate("He was lost in reverie and did not hear the door open.", "en-GB-RyanNeural")
    await c_ex.save("news_portal/culture/headphones-in-public/audio/ex_revery.mp3")

    c_pron = edge_tts.Communicate("reverie. rev-er-ie. lost in reverie.", "en-GB-RyanNeural")
    await c_pron.save("news_portal/culture/headphones-in-public/audio/pron_revery_accent.mp3")
    print("All reverie audio regenerated with native English pronunciation!")

if __name__ == "__main__":
    asyncio.run(test())
