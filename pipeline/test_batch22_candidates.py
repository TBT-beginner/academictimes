import urllib.request
import ssl
import json

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

redirects = [
    ("kim_china", "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHP9bs4smkP3MtIeQxw9dvs9z3uavjyY8LMnwCTdfXkOqUFvZFG5Q4VdB-ofBuHqMS2GkckDAkjuvqS-CBnxtgEInkM2yXP4MA4EPDIvYZNswJCzzQdDpOkZaa9aT703ZzcneU_r95uRyKIH6J2hpQdcfAGBS_WIErTZ8GfacJkr5ts3WGCR1KbZH3MxMCDR2Yd2yy54J4="),
    ("france_protest", "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGebwaJDuor5m2w0c42kwyW7qa4Ld0mDwnUYPMywHuEQAXJCfFnbXVbpBxbyiVLJT-PcJgQOlHgAVJqGIcLOaXts5sVLyUAglQnVNjGdZFwiLnJv94w1RF2Db1VxV8tS-CsTOSGrxBCRdIeClPgpaYkAMxrhZaF8p0NcGXujUrzkqEWm4id6tl-6AAdSrmwozTaFlIuJqEtn0tHm1KppWRhP3EsTkdQ0m7qhFrPHxwXJNVUJA=="),
    ("ca_voting", "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHoiKKUeDaFp2w5gtZp96cW4hhZBvj-b4kYcyeJj4quVT5WhwxcL6wua5D4Ei-2BmGX8-nj0XUzFD6sDL_KCxt3YPmGls4J4nSAchsyu4MgB_TYMx2544GDfdU6gHn3g4ITNwlZHrcBRDnNWQYQIoZQEORc70xQCEf93jjxktHybdTJ9nNksYaMn5L1S69zF3kjICqB36Xn"),
    ("icc_sanctions", "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFe7rBgI-SVgdY4QQ07fJqqCLNG4os6f1GSxI6DQRoskTNwdG8ewEqb3cBPbNYSFIYVU1VumvjRgze6h3pueZ8oxj3ved-2uegz3bHDMwIFfJSgHbWgWs6SQWTNkeNlTAGhAepnGsB4x4cWTCB8PZpib1wA6MWbFqvX-zYnUlly3gETCRe_OXNw8emaGKXDv8ZVVyWoEgRz5KLsnLIYsCYqu-Pg1Q=="),
    ("sally_rooney", "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHaTUvmFGKMati35ETRHIGf8rfIuR-FXVwewzNkGi3P0BRiOy_8gz0OHX02WApLyGCk9RgGIB1hHroGuhFPPW231bBdqAvGruhPheHBh0YWx6K1oPSsbHOMPJjtUiwJcxxa8nK8EK4nN0NCfNBbuyQgSFQ-8Xw6aVgriCVXo_pwKfitFGGXv2w3KfnZ9HBIqBfPSP9JYs4Hv000HszIkg905Qeopy5acpu3MFXdviTRlFTPBtgX7XDNlpUBwP1kc1O_5vB6wROShWY="),
    ("stephen_fry", "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHYW4Q3S-xLFperLtBUNkcwdOQ18KaV_dBB35BBvTwiVVrWJO8KnRpzvkIKKsfCTSXBDXnWgqTdSQh5TJ8lKDCp1Btfcw0xQjB0eCU29PUAPDWLiRXUGLka5vKHXhgsBw4czqNASW9fpWxOY6f44H5vfyytXBpC-tdFhrCAj8U0adQe7unsJgZRXnLSvwFpUox8GT3gUXCe0DV-4MNFgJqXdCRU"),
    ("rosebank", "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGE0WbyUFJxKNgbOX7n8_5abs7fmYld7QDiusB28zpvBdv_4g6nl-EFHuI3CsdSHhwO-pkaKa_FC9cJmLd4OdI5pvzAU71GbbVFTJsSYjZYwrnEBmYOKTjuKjUojXkE2um0d50SL58ChnVZDJIpgjyQODZQ0dlFS9uMO0o8liRiCEBMk9Cym8sIYnE1iwtHn8ALLY4_a9D4RiWEFmM--byov1EGOjfVHnS1fcK70w=="),
    ("seabirds_dark", "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFnQEyZYmsCmz6xCyG_Nv_0NygMYOKgjKo9WoTS1g7Kzeg42pm0hQr5JYqXIJo0mLSPidd51FAjOdheHZ5JQXLL5_FJdNw_Vg30jxph2SLm4TiblMEvsICnRp0cmWUYb9I="),
    ("synthetic_twin", "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF5YBPeiPWKYcgwXyn6DyykP42CtorT3zrx6WnA7ZO6uq-XIQ3UCFYHv-JtKJdSXlebFIBHHQgrdhBb4v0MViC2j9-HS2N8rhBJjgET0-xMXF2MXds74azETtH1Sxh9J6E25BQnWy1jVombukhi4oUzJZtHNk1L8bM6FX7CqqfW_PmCdcqiSHKuOoR1N5_qwwKjETS9vPpUNmyYJwaX7OsGk1Wph9lVBDWNkL-kveBGvFKxJhYZtmJaa4UDDG0A5Dky6TwWGQis"),
    ("traintok", "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE_uI41VM1p1LJeeHFFr8zWFQpAIG1ML3URWtfDEWr7ncfT_Z8Y3BpVC3-IvjYchQNhpmisL9tTMfsKlr2lW9nUyNOAs1BUyKebYEFYMmwtzQQQDhFulFYrGrKM673HRN8eQi00XmWFjXjnPuex5OA_F09Tcmx4SmN4JJSChPorNTQh18XBihWrhZmAxQat_yvE0Ttx2ZdVvg=="),
    ("cookie_theft", "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG4zRudVW0v0-0HAsWgoy2zGRHJP0mfObJF_E5cqWRwosL9gpavsK65lP1gaAQxkJTsWeZz1XugNo0xJcCJ2vLDCAL6vWi39aQSuqsCFJFKm1SN--mvYkSrYfm7Pf6jNkk="),
    ("healey_budget", "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG8Gt6DAvouimKTUn3LMBa539rE3cBdbNNRiGDDPki9EBi7EK4b6PS0cw76tw6p_w4aQ3lWE3D7Ys9J53_qWjkjTv5xN4r8XcFsF5t7PEDkQ9OU7mkB32egm7w7ZPKBQ6N1mePXvpiMStcviCOXGaB6rWpiBNtCnFj3ZVTk489d2aEOnfosZAt-72SVkBeonni8DDf9kRTeBe4z17Ne1z9qAKrZTN-GMrCbSl_94ZSsr1GE")
]

resolved = []
for tag, url in redirects:
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10, context=ctx) as r:
            final_url = r.geturl()
            code = r.status
            print(f"[{code}] {tag}: {final_url}", flush=True)
            resolved.append((tag, final_url, code))
    except Exception as e:
        print(f"[FAIL] {tag}: {e}", flush=True)

with open("c:/Users/teacher/Documents/lessonfactory/news_portal/pipeline/resolved_batch22_urls.json", "w", encoding="utf-8") as f:
    json.dump(resolved, f, indent=2)
