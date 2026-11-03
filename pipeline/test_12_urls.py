import urllib.request

candidate_urls = [
    ("science", "nasa-telescope-neil-gehrels-swift-observatory", "https://www.theguardian.com/science/2026/nov/03/nasa-telescope-neil-gehrels-swift-observatory"),
    ("science", "ai-godfather-geoffrey-hinton-better-off-without-ai", "https://www.theguardian.com/uk-news/2026/nov/03/ai-godfather-geoffrey-hinton-better-off-without-ai"),
    ("environment", "uk-drax-power-station-ai-datacentre", "https://www.theguardian.com/business/2026/nov/03/uk-drax-power-station-ai-datacentre"),
    ("environment", "denmark-pushes-for-eu-ban-on-turbo-chickens-as-secret-footage-causes-outrage", "https://www.theguardian.com/world/2026/nov/03/denmark-pushes-for-eu-ban-on-turbo-chickens-as-secret-footage-causes-outrage"),
    ("society", "pension-income-retirement-for-17m-private-sector-workers", "https://www.theguardian.com/business/2026/nov/03/pension-income-retirement-for-17m-private-sector-workers"),
    ("society", "kelloggs-rice-krispies-coco-pops-reformulated-rice-shortage", "https://www.theguardian.com/food/2026/nov/03/kelloggs-rice-krispies-coco-pops-reformulated-rice-shortage"),
    ("world", "midterm-voters-republican-democrats-trump-second-term", "https://www.theguardian.com/us-news/2026/nov/03/midterm-voters-republican-democrats-trump-second-term"),
    ("world", "four-planes-flying-across-europe-targeted-by-bomb-threats", "https://www.theguardian.com/world/2026/nov/03/four-planes-flying-across-europe-targeted-by-bomb-threats"),
    ("law", "uk-meat-processing-firms-fridges-heat-up-cyber-attacks", "https://www.theguardian.com/technology/2026/nov/03/uk-meat-processing-firms-fridges-heat-up-cyber-attacks"),
    ("law", "well-known-individual-fails-injunction-bid-guardian-itn", "https://www.theguardian.com/uk-news/2026/nov/03/well-known-individual-fails-injunction-bid-guardian-itn"),
    ("culture", "mogging-crowned-collins-word-of-the-year", "https://www.theguardian.com/uk-news/2026/nov/03/mogging-crowned-collins-word-of-the-year"),
    ("entertainment", "china-first-ai-generated-film-flops-cinema-future", "https://www.theguardian.com/film/2026/nov/03/china-first-ai-generated-film-flops-cinema-future")
]

headers = {'User-Agent': 'Mozilla/5.0'}
for cat, slug, u in candidate_urls:
    try:
        r = urllib.request.Request(u, headers=headers)
        with urllib.request.urlopen(r, timeout=5) as res:
            print(f'[{res.status}] {cat}/{slug} -> {u}')
    except Exception as e:
        print(f'[FAIL: {e}] {cat}/{slug} -> {u}')
