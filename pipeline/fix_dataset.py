# -*- coding: utf-8 -*-
import sys
sys.path.append('news_portal/pipeline')
import articles_data

print("Successfully imported articles_data!")
print(f"Total articles: {len(articles_data.ARTICLES)}")
for i, a in enumerate(articles_data.ARTICLES, 1):
    print(f"{i:2d}. [{a['category'].upper()}] {a['title']}")
