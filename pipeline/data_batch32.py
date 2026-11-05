# -*- coding: utf-8 -*-
"""
Batch 32 Articles Data (2026-11-05)
12 Senior + 12 Junior Articles
All primary sources verified HTTP 200 OK from The Guardian (Nov 4-5, 2026).
"""

import os, sys
_dir = os.path.dirname(os.path.abspath(__file__))
if _dir not in sys.path:
    sys.path.insert(0, _dir)

from data_batch32_part1 import SENIOR_PART1
from data_batch32_part2 import SENIOR_PART2
from data_batch32_junior_part1 import JUNIOR_PART1
from data_batch32_junior_part2 import JUNIOR_PART2

BATCH32_SENIOR = SENIOR_PART1 + SENIOR_PART2
BATCH32_JUNIOR = JUNIOR_PART1 + JUNIOR_PART2

__all__ = ["BATCH32_SENIOR", "BATCH32_JUNIOR", "SENIOR_PART1", "SENIOR_PART2", "JUNIOR_PART1", "JUNIOR_PART2"]

if __name__ == "__main__":
    print(f"Batch 32 loaded: {len(BATCH32_SENIOR)} Senior, {len(BATCH32_JUNIOR)} Junior articles.")
