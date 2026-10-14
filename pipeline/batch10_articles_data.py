# -*- coding: utf-8 -*-
"""
Batch 10 Master Aggregator (2026-10-14 Edition - 本日付・最新)
Aggregates all 30 Senior and 30 Junior articles across 6 categories.
"""

import os
import sys

_curr_dir = os.path.dirname(os.path.abspath(__file__))
if _curr_dir not in sys.path:
    sys.path.insert(0, _curr_dir)

from batch10_science import BATCH10_SENIOR_SCIENCE, BATCH10_JUNIOR_SCIENCE
from batch10_society import BATCH10_SENIOR_SOCIETY, BATCH10_JUNIOR_SOCIETY
from batch10_world import BATCH10_SENIOR_WORLD, BATCH10_JUNIOR_WORLD
from batch10_law import BATCH10_SENIOR_LAW, BATCH10_JUNIOR_LAW
from batch10_culture import BATCH10_SENIOR_CULTURE, BATCH10_JUNIOR_CULTURE
from batch10_entertainment import BATCH10_SENIOR_ENTERTAINMENT, BATCH10_JUNIOR_ENTERTAINMENT

BATCH10_SENIOR = (
    BATCH10_SENIOR_SCIENCE +
    BATCH10_SENIOR_SOCIETY +
    BATCH10_SENIOR_WORLD +
    BATCH10_SENIOR_LAW +
    BATCH10_SENIOR_CULTURE +
    BATCH10_SENIOR_ENTERTAINMENT
)

BATCH10_JUNIOR = (
    BATCH10_JUNIOR_SCIENCE +
    BATCH10_JUNIOR_SOCIETY +
    BATCH10_JUNIOR_WORLD +
    BATCH10_JUNIOR_LAW +
    BATCH10_JUNIOR_CULTURE +
    BATCH10_JUNIOR_ENTERTAINMENT
)

if __name__ == "__main__":
    print(f"Batch 10 Aggregated: {len(BATCH10_SENIOR)} Senior articles, {len(BATCH10_JUNIOR)} Junior articles.")
    assert len(BATCH10_SENIOR) == 30, f"Expected 30 Senior articles, got {len(BATCH10_SENIOR)}"
    assert len(BATCH10_JUNIOR) == 30, f"Expected 30 Junior articles, got {len(BATCH10_JUNIOR)}"
    print("Batch 10 verification PASSED!")
