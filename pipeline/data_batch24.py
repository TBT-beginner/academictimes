# -*- coding: utf-8 -*-
"""
Batch 24 Articles Data (2026-10-28)
12 Senior + 12 Junior Articles
All primary sources verified HTTP 200 OK from The Guardian (Oct 24-27, 2026).
"""

from data_batch24_part1 import SENIOR_PART1
from data_batch24_part2 import SENIOR_PART2
from data_batch24_junior_part1 import JUNIOR_PART1
from data_batch24_junior_part2 import JUNIOR_PART2

BATCH24_SENIOR = SENIOR_PART1 + SENIOR_PART2
BATCH24_JUNIOR = JUNIOR_PART1 + JUNIOR_PART2

__all__ = ["BATCH24_SENIOR", "BATCH24_JUNIOR", "SENIOR_PART1", "SENIOR_PART2", "JUNIOR_PART1", "JUNIOR_PART2"]

if __name__ == "__main__":
    print(f"Batch 24 loaded: {len(BATCH24_SENIOR)} Senior, {len(BATCH24_JUNIOR)} Junior articles.")
