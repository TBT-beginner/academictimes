# -*- coding: utf-8 -*-
"""
Batch 9 Master Aggregator (2026-10-13 Edition)
Aggregates all 30 Senior and 30 Junior articles across 6 categories.
"""

import os
import sys

_curr_dir = os.path.dirname(os.path.abspath(__file__))
if _curr_dir not in sys.path:
    sys.path.insert(0, _curr_dir)

from batch9_science import BATCH9_SENIOR_SCIENCE, BATCH9_JUNIOR_SCIENCE
from batch9_society import BATCH9_SENIOR_SOCIETY, BATCH9_JUNIOR_SOCIETY
from batch9_world import BATCH9_SENIOR_WORLD, BATCH9_JUNIOR_WORLD
from batch9_law import BATCH9_SENIOR_LAW, BATCH9_JUNIOR_LAW
from batch9_culture import BATCH9_SENIOR_CULTURE, BATCH9_JUNIOR_CULTURE
from batch9_entertainment import BATCH9_SENIOR_ENTERTAINMENT, BATCH9_JUNIOR_ENTERTAINMENT

BATCH9_SENIOR = (
    BATCH9_SENIOR_SCIENCE +
    BATCH9_SENIOR_SOCIETY +
    BATCH9_SENIOR_WORLD +
    BATCH9_SENIOR_LAW +
    BATCH9_SENIOR_CULTURE +
    BATCH9_SENIOR_ENTERTAINMENT
)

BATCH9_JUNIOR = (
    BATCH9_JUNIOR_SCIENCE +
    BATCH9_JUNIOR_SOCIETY +
    BATCH9_JUNIOR_WORLD +
    BATCH9_JUNIOR_LAW +
    BATCH9_JUNIOR_CULTURE +
    BATCH9_JUNIOR_ENTERTAINMENT
)

if __name__ == "__main__":
    print(f"Batch 9 Aggregated: {len(BATCH9_SENIOR)} Senior articles, {len(BATCH9_JUNIOR)} Junior articles.")
    assert len(BATCH9_SENIOR) == 30, f"Expected 30 Senior articles, got {len(BATCH9_SENIOR)}"
    assert len(BATCH9_JUNIOR) == 30, f"Expected 30 Junior articles, got {len(BATCH9_JUNIOR)}"
    print("Batch 9 verification PASSED!")
