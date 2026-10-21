import urllib.request

urls = [
    "https://www.theguardian.com/science/2026/oct/21/orangutans-prefer-food-laughter-sounds-study",
    "https://www.theguardian.com/science/2026/oct/21/do-people-become-less-creative-as-they-get-older-research",
    "https://www.theguardian.com/science/2026/oct/21/bad-apples-rule-breaking-study",
    "https://www.theguardian.com/technology/2026/oct/21/flaw-in-php-computer-language-leads-to-shutdown-of-websites-around-world",
    "https://www.theguardian.com/books/2026/oct/21/new-prize-launches-books-co-written-with-ai-france",
    "https://www.theguardian.com/music/2026/oct/21/artificial-intelligence-music-grimes-asap-rocky",
    "https://www.theguardian.com/environment/2026/oct/21/world-cut-emissions-un-climate-crisis",
    "https://www.theguardian.com/environment/2026/oct/21/norway-svalbard-environment-longyearbyen-climate-heating-glacier-permafrost",
    "https://www.theguardian.com/world/2026/oct/21/taiwan-five-men-plot-run-over-comedian-huang-yi-hao-xi-jinping-jokes",
    "https://www.theguardian.com/world/2026/oct/21/youtube-watch-over-shark-stuck-south-korea-canal-busan-bukang-i",
    "https://www.theguardian.com/australia-news/2026/oct/22/penicillin-allergy-australia-doctors-antibiotic-guidelines",
    "https://www.theguardian.com/australia-news/2026/oct/22/nsw-passes-human-compost-laws-with-several-mps-saying-they-will-utilise-practice-after-they-die"
]

headers = {'User-Agent': 'Mozilla/5.0'}

all_ok = True
for u in urls:
    try:
        req = urllib.request.Request(u, headers=headers)
        res = urllib.request.urlopen(req, timeout=8)
        print(f"[STATUS {res.status}] {u}")
    except Exception as e:
        print(f"[FAIL] {u} -> {e}")
        all_ok = False

if all_ok:
    print("\nALL 12 URLS ARE 100% LIVE (HTTP 200 OK)!")
else:
    print("\nSOME URLS FAILED!")
