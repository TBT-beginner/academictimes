# -*- coding: utf-8 -*-
"""
Batch 6: Master aggregation of 28 verified articles for 2026-10-10.
Combined with the 2 existing articles for 2026-10-10, this brings 2026-10-10 to exactly 30 unique articles:
- Science: 2 existing + 3 new = 5 articles
- Society: 5 new articles
- World: 5 new articles
- Law: 5 new articles
- Culture: 5 new articles
- Entertainment: 5 new articles
Total for 2026-10-10: 30 articles!
"""

from batch6_science import SCIENCE_SENIOR, SCIENCE_JUNIOR
from batch6_society import SOCIETY_SENIOR, SOCIETY_JUNIOR
from batch6_world import WORLD_SENIOR, WORLD_JUNIOR
from batch6_law import LAW_SENIOR, LAW_JUNIOR
from batch6_culture import CULTURE_SENIOR, CULTURE_JUNIOR
from batch6_entertainment import ENTERTAINMENT_SENIOR, ENTERTAINMENT_JUNIOR

BATCH6_SENIOR = (
    SCIENCE_SENIOR +
    SOCIETY_SENIOR +
    WORLD_SENIOR +
    LAW_SENIOR +
    CULTURE_SENIOR +
    ENTERTAINMENT_SENIOR
)

BATCH6_JUNIOR = (
    SCIENCE_JUNIOR +
    SOCIETY_JUNIOR +
    WORLD_JUNIOR +
    LAW_JUNIOR +
    CULTURE_JUNIOR +
    ENTERTAINMENT_JUNIOR
)

if __name__ == "__main__":
    print(f"Batch 6 Loaded Successfully:")
    print(f"  - Senior Articles: {len(BATCH6_SENIOR)} articles")
    print(f"  - Junior Articles: {len(BATCH6_JUNIOR)} articles")
