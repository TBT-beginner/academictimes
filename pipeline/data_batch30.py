# -*- coding: utf-8 -*-
"""
Batch 30 Articles Data (2026-11-03)
12 Senior + 12 Junior Articles
All primary sources verified HTTP 200 OK from The Guardian (Nov 1-3, 2026).
"""

import os, sys
_dir = os.path.dirname(os.path.abspath(__file__))
if _dir not in sys.path:
    sys.path.insert(0, _dir)

from data_batch30_part1 import SENIOR_PART1
from data_batch30_part2 import SENIOR_PART2
from data_batch30_junior_part1 import JUNIOR_PART1
from data_batch30_junior_part2 import JUNIOR_PART2

BATCH30_SENIOR = SENIOR_PART1 + SENIOR_PART2
BATCH30_JUNIOR = JUNIOR_PART1 + JUNIOR_PART2

__all__ = ["BATCH30_SENIOR", "BATCH30_JUNIOR", "SENIOR_PART1", "SENIOR_PART2", "JUNIOR_PART1", "JUNIOR_PART2"]

if __name__ == "__main__":
    print(f"Batch 30 loaded: {len(BATCH30_SENIOR)} Senior, {len(BATCH30_JUNIOR)} Junior articles.")
