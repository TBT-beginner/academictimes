# -*- coding: utf-8 -*-
"""
Batch 8 Articles Aggregator
Contains all 30 new articles for 2026-10-11 (today's daily edition).
"""

from batch8_science import BATCH8_SENIOR_SCIENCE, BATCH8_JUNIOR_SCIENCE
from batch8_society import BATCH8_SENIOR_SOCIETY, BATCH8_JUNIOR_SOCIETY
from batch8_world import BATCH8_SENIOR_WORLD, BATCH8_JUNIOR_WORLD
from batch8_law import BATCH8_SENIOR_LAW, BATCH8_JUNIOR_LAW
from batch8_culture import BATCH8_SENIOR_CULTURE, BATCH8_JUNIOR_CULTURE
from batch8_entertainment import BATCH8_SENIOR_ENTERTAINMENT, BATCH8_JUNIOR_ENTERTAINMENT

BATCH8_SENIOR = (
    BATCH8_SENIOR_SCIENCE +
    BATCH8_SENIOR_SOCIETY +
    BATCH8_SENIOR_WORLD +
    BATCH8_SENIOR_LAW +
    BATCH8_SENIOR_CULTURE +
    BATCH8_SENIOR_ENTERTAINMENT
)

BATCH8_JUNIOR = (
    BATCH8_JUNIOR_SCIENCE +
    BATCH8_JUNIOR_SOCIETY +
    BATCH8_JUNIOR_WORLD +
    BATCH8_JUNIOR_LAW +
    BATCH8_JUNIOR_CULTURE +
    BATCH8_JUNIOR_ENTERTAINMENT
)

if __name__ == "__main__":
    print(f"Loaded {len(BATCH8_SENIOR)} Senior and {len(BATCH8_JUNIOR)} Junior articles for Batch 8.")
