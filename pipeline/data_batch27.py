# -*- coding: utf-8 -*-
"""
Batch 27 Articles Data (2026-10-31)
12 Senior + 12 Junior Articles
All primary sources verified HTTP 200 OK from The Guardian (Oct 29-30, 2026).
"""

import os, sys
_dir = os.path.dirname(os.path.abspath(__file__))
if _dir not in sys.path:
    sys.path.insert(0, _dir)

from data_batch27_part1 import SENIOR_PART1
from data_batch27_part2 import SENIOR_PART2
from data_batch27_junior_part1 import JUNIOR_PART1
from data_batch27_junior_part2 import JUNIOR_PART2

BATCH27_SENIOR = SENIOR_PART1 + SENIOR_PART2
BATCH27_JUNIOR = JUNIOR_PART1 + JUNIOR_PART2

__all__ = ["BATCH27_SENIOR", "BATCH27_JUNIOR", "SENIOR_PART1", "SENIOR_PART2", "JUNIOR_PART1", "JUNIOR_PART2"]

if __name__ == "__main__":
    print(f"Batch 27 loaded: {len(BATCH27_SENIOR)} Senior, {len(BATCH27_JUNIOR)} Junior articles.")
