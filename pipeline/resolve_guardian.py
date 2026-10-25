import urllib.request
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

redirect_urls = [
    "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF_95Ij-2Dy-B6ClVJNT5oLdixFRObEJai71HSDIAg1cF9ws5-cYA2Ne3lmz-ZFTnAZ0gwdgrSgHJ_XmtMzjO_VzvxdH5jXUCahtPDk-Ne3jK5DSfeb50V6aDnvVcTPN14gfKoqMVhZv93hxiqNeKKTjxOPSe0QgBCclpttB-fatov1Shc6ei_D87WTztmKyaqeNbHq-4Qu0gneokmFfw4=",
    "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHkRSnZ85s65AyreGJuCzhAPgV1WVq-AUed5C9MtH0NGEk9Mdwze4QlF0FSn7fRhN1eLJypAgfKJrxLFZAG2t2UAONPZ9_6HRct2oPcEj43Xp9JrvOQSRJH6TPdjX_YJrPuK_cD9GJzULiuIzmoy7AFVLoJGjiMGROOME6jE2HsfAU34YucwmX9kFyZF3wqsoFfFJ2d_ESsGG6IF9BweRM=",
    "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG1nhtusm_W8bRnfLV5mooNwsFOPtrAr1bdNjYl_Orv4-UspRVcBa8YiIyGHfWUM41Z_4RUkjo_wLgYYfkAPwk50K6k9-KStm7cjUQjf9j-L2HUf_nIniNhHdnR5t2-IOyPXXlKBz8k8Av8hv2CYIVF0wjsv7AoiB1YDd2Aowyk",
    "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGlW-rNax1G5wiCJA_ffxrNeCOxntzyguTg1KMJCsU9qDpusqELrpypWFwqQoSjqXbkV3g2VQXNfL9dltbmEAyeKOw1o-Sg8oZjDmnsb4IpUMT2ubVjbqInAnH5o5D-wezzaIp7bItDZ3VQlbVqgaIpaoNDOvKgx5MWYbrUuViDPWN3-8hY1mKsjdDnY-So1hmdrsIPPq2r9jemL7FR8ew1IuZTp9chJI5zHg4vECOuo5jGWp8opQRuqo3iSXyTf-A=",
    "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHa3mwTRGiGDgvm3ykDePWsg_nveENHF4uoXWw5_z0szx_n6teoE5T9s4f0Rc5U4fMkFnF_VJktPXCUsmSZ2oeCAwkpoPY0kx2SJSIkx09OQxAIA_tia7G-niG4Guu5PvyeJ91L0lo6L-XnUxiOcJ_UhkRGAMWj0MTWhugHEroNNZpKuGllRM2ElbpH0PSjg7biKzAp4QLIjEiDhZWLoONWPlh9OgUwk9K4-vQbOspImmsY9Sa0_O6V0l4sucjozYzucSY=",
    "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGYnbvRrdbTDJEr4-bxvVzZowuI_4Gq1t-gejCjmiTV6ySpIdlM8FB1fxYdv1ZrBrmAdpsUZALYljsvTY0m3Q74lDBGEYIZpKPwnqP1etinfWKmSKd9T3ts184xLiplPWSYZpQDILj0qXvW1azBWHr2Q-KuSZM0FtXjc68BuMYlbTGhPOOLMuzCYEF9eavfb6c2lrGUclAY26QcNm8rU-gu4Q==",
    "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHp6td8eXYROyUXZ-iMB7_HaykSnnVm10-6YqOUc7Pz5PUv0NeoaFAkvIKHfM3sKpHC2tKGC1DgDMlIn8q8PGrZ6u8X3D1jY1fy0lO7xwJGqov3uuqWKkBqfzI2G8DSE7IPSrWOrX5KEMnisHCepiUFq3Sbh9jxI-CRTThfNYQgnhF3YNT_w_RpCnudjVQi55C_PXh7I43Sa_0ntNebtXAm3f37a3SH82Myo53_fykI3Us=",
    "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGGstlw2bJsOrtFKEotnrn1rjma3NKXEKJWVh8TmRqXO_cEGZKE3ClDrF5jihbJ9bZNl-NKnnkOO0vp2gbATXZsvpukM06R4zyfSSQV1D5bwA2nlnsik93KZ5CRCRTY67XAIJ9hM4tlIF7NqDUFt6bpTWNe3aE4O5zAQB8564f8NEenVo3QJnmKBeL9yhNjrti3olZ9HRiYRUk_dS_l5w-3b3IFTQ==",
    "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG2U3AjIsPfsPZ9lY1mc3zdmTscMmzJRuBzoweSMGnM4QhtoGgGCpnUvvkcI_TRThuqrsvBTBH3sdsyqGhEHu5Bp980OcNJ5Bv0C1cT6SeFwY3ST-YyG1BbnZS3FHWl48nBGX0f-UTzCw2XTbvG82VuC7dcjw-LAqIGIGgoAHR4lcVmICHoZLGy7fEufHZ_r-1lPPEX2BMejLnsbRxGZjfTb9We_GPa0btbYhr2AhB2hzg=",
    "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQExHP-Y3-gXPg7AmudcjJ6M4-PZrXqgqtFEC5JlUuIKHC2HXe1hFg6rJ4ii_wEyJ-8phhKDP7GS2NPHM6PNIpjdJQeQjMERvx0Lnw8-3lyL7XV1WeEEmQBsQa0yYi9dWi8IAySbz22KdEPFAUAzbO0RxdvRkruo9lyijJPShch-3hpPYGmfuXBg6UyMdbFKeu6M3xVHeFwfe8x3Ris="
]

results = []
for u in redirect_urls:
    try:
        req = urllib.request.Request(u, headers=headers)
        with urllib.request.urlopen(req, timeout=8, context=ctx) as resp:
            final_url = resp.geturl()
            results.append({"redirect": u, "final_url": final_url, "status": resp.status})
            print(f"[OK] {final_url}")
    except Exception as e:
        print(f"[ERR] {e}")

with open("c:/Users/teacher/Documents/lessonfactory/news_portal/pipeline/resolved_urls.json", "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2)
print("Done resolving!")
