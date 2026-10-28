# -*- coding: utf-8 -*-
"""
Batch 25 Articles Data (2026-10-29)
12 Senior + 12 Junior Articles
All primary sources verified HTTP 200 OK from The Guardian (Oct 27-28, 2026).
"""

from data_batch25_part1 import SENIOR_PART1
from data_batch25_part2 import SENIOR_PART2
from data_batch25_junior_part1 import JUNIOR_PART1
from data_batch25_junior_part2 import JUNIOR_PART2

BATCH25_SENIOR = SENIOR_PART1 + SENIOR_PART2
BATCH25_JUNIOR = JUNIOR_PART1 + JUNIOR_PART2

__all__ = ["BATCH25_SENIOR", "BATCH25_JUNIOR", "SENIOR_PART1", "SENIOR_PART2", "JUNIOR_PART1", "JUNIOR_PART2"]

if __name__ == "__main__":
    print(f"Batch 25 loaded: {len(BATCH25_SENIOR)} Senior, {len(BATCH25_JUNIOR)} Junior articles.")
