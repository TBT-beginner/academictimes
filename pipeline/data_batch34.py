# -*- coding: utf-8 -*-
"""
Batch 34 Articles Data (2026-11-09)
12 Senior + 12 Junior Articles
All primary sources verified HTTP 200 OK from The Guardian (Nov 7-8, 2026).
"""

import os, sys
_dir = os.path.dirname(os.path.abspath(__file__))
if _dir not in sys.path:
    sys.path.insert(0, _dir)

from data_batch34_part1 import SENIOR_PART1
from data_batch34_part2 import SENIOR_PART2
from data_batch34_junior_part1 import JUNIOR_PART1
from data_batch34_junior_part2 import JUNIOR_PART2

BATCH34_SENIOR = SENIOR_PART1 + SENIOR_PART2
BATCH34_JUNIOR = JUNIOR_PART1 + JUNIOR_PART2

__all__ = ["BATCH34_SENIOR", "BATCH34_JUNIOR", "SENIOR_PART1", "SENIOR_PART2", "JUNIOR_PART1", "JUNIOR_PART2"]

if __name__ == "__main__":
    print(f"Batch 34 loaded: {len(BATCH34_SENIOR)} Senior, {len(BATCH34_JUNIOR)} Junior articles.")
