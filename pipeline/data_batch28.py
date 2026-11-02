# -*- coding: utf-8 -*-
"""
Batch 28 Articles Data (2026-11-01)
12 Senior + 12 Junior Articles
All primary sources verified HTTP 200 OK from The Guardian (Oct 29-31, 2026).
"""

import os, sys
_dir = os.path.dirname(os.path.abspath(__file__))
if _dir not in sys.path:
    sys.path.insert(0, _dir)

from data_batch28_part1 import SENIOR_PART1
from data_batch28_part2 import SENIOR_PART2
from data_batch28_junior_part1 import JUNIOR_PART1
from data_batch28_junior_part2 import JUNIOR_PART2

BATCH28_SENIOR = SENIOR_PART1 + SENIOR_PART2
BATCH28_JUNIOR = JUNIOR_PART1 + JUNIOR_PART2

__all__ = ["BATCH28_SENIOR", "BATCH28_JUNIOR", "SENIOR_PART1", "SENIOR_PART2", "JUNIOR_PART1", "JUNIOR_PART2"]

if __name__ == "__main__":
    print(f"Batch 28 loaded: {len(BATCH28_SENIOR)} Senior, {len(BATCH28_JUNIOR)} Junior articles.")
