# -*- coding: utf-8 -*-
"""
Batch 26 Articles Data (2026-10-30)
12 Senior + 12 Junior Articles
All primary sources verified HTTP 200 OK from The Guardian (Oct 28-29, 2026).
"""

from data_batch26_part1 import SENIOR_PART1
from data_batch26_part2 import SENIOR_PART2
from data_batch26_junior_part1 import JUNIOR_PART1
from data_batch26_junior_part2 import JUNIOR_PART2

BATCH26_SENIOR = SENIOR_PART1 + SENIOR_PART2
BATCH26_JUNIOR = JUNIOR_PART1 + JUNIOR_PART2

__all__ = ["BATCH26_SENIOR", "BATCH26_JUNIOR", "SENIOR_PART1", "SENIOR_PART2", "JUNIOR_PART1", "JUNIOR_PART2"]

if __name__ == "__main__":
    print(f"Batch 26 loaded: {len(BATCH26_SENIOR)} Senior, {len(BATCH26_JUNIOR)} Junior articles.")
