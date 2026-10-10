# -*- coding: utf-8 -*-
"""
Batch 7 Articles Aggregator
Contains all 18 new articles for 2026-10-09 (bringing 10/9 to 30 articles total).
"""

from batch7_science import BATCH7_SCIENCE_SENIOR, BATCH7_SCIENCE_JUNIOR
from batch7_society import BATCH7_SOCIETY_SENIOR, BATCH7_SOCIETY_JUNIOR
from batch7_world import BATCH7_WORLD_SENIOR, BATCH7_WORLD_JUNIOR
from batch7_law import BATCH7_LAW_SENIOR, BATCH7_LAW_JUNIOR
from batch7_culture import BATCH7_CULTURE_SENIOR, BATCH7_CULTURE_JUNIOR
from batch7_entertainment import BATCH7_ENTERTAINMENT_SENIOR, BATCH7_ENTERTAINMENT_JUNIOR

BATCH7_SENIOR = (
    BATCH7_SCIENCE_SENIOR +
    BATCH7_SOCIETY_SENIOR +
    BATCH7_WORLD_SENIOR +
    BATCH7_LAW_SENIOR +
    BATCH7_CULTURE_SENIOR +
    BATCH7_ENTERTAINMENT_SENIOR
)

BATCH7_JUNIOR = (
    BATCH7_SCIENCE_JUNIOR +
    BATCH7_SOCIETY_JUNIOR +
    BATCH7_WORLD_JUNIOR +
    BATCH7_LAW_JUNIOR +
    BATCH7_CULTURE_JUNIOR +
    BATCH7_ENTERTAINMENT_JUNIOR
)

if __name__ == "__main__":
    print(f"Loaded {len(BATCH7_SENIOR)} Senior and {len(BATCH7_JUNIOR)} Junior articles for Batch 7.")
