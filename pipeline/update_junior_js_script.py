# -*- coding: utf-8 -*-
import re

junior_file = 'news_portal/pipeline/build_junior_data_js.py'
with open(junior_file, 'r', encoding='utf-8') as f:
    content = f.read()

new_junior_block = '''EDITIONS_DATA = {
    "2026-11-04": {
        "dateStr": "Wednesday November 4 2026",
        "editionLabel": "2026年11月4日 (水) 号 【本日・最新・全12記事】",
        "tagline": "特集：NASAスウィフト望遠鏡復活・ヒントン教授のAI警告・米中間選挙・工場の冷蔵庫サイバー攻撃・今年のことばMogging",
        "topLeadSlug": "nasa-telescope-neil-gehrels-swift-observatory",
        "subLeadSlugs": [
            "ai-godfather-geoffrey-hinton-better-off-without-ai",
            "midterm-voters-republican-democrats-trump-second-term",
            "uk-meat-processing-firms-fridges-heat-up-cyber-attacks"
        ],
        "leftDispatches": [
            "uk-drax-power-station-ai-datacentre",
            "denmark-pushes-for-eu-ban-on-turbo-chickens-as-secret-footage-causes-outrage",
            "pension-income-retirement-for-17m-private-sector-workers",
            "kelloggs-rice-krispies-coco-pops-reformulated-rice-shortage"
        ],
        "rightDigestSlugs": [
            "four-planes-flying-across-europe-targeted-by-bomb-threats",
            "well-known-individual-fails-injunction-bid-guardian-itn",
            "mogging-crowned-collins-word-of-the-year",
            "china-first-ai-generated-film-flops-cinema-future"
        ]
    },
'''

content = content.replace('EDITIONS_DATA = {\n', new_junior_block)
content = re.sub(r'("2026-11-03":\s*\{\s*"dateStr":\s*"[^"]+",\s*"editionLabel":\s*")[^"]+(")', r'\g<1>2026年11月3日 (火) 号 【全12記事】\g<2>', content)

with open(junior_file, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated build_junior_data_js.py successfully!")
