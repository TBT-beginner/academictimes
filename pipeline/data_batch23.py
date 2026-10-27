# -*- coding: utf-8 -*-
"""
Batch 23 Articles Data (2026-10-27)
12 Senior + 12 Junior Articles
All primary sources verified HTTP 200 OK from The Guardian (Oct 25-26, 2026).
"""

from data_batch23_part1 import SENIOR_PART1
from data_batch23_part2 import SENIOR_PART2
from data_batch23_junior_part1 import JUNIOR_PART1
from data_batch23_junior_part2 import JUNIOR_PART2

BATCH23_SENIOR = SENIOR_PART1 + SENIOR_PART2
BATCH23_JUNIOR = JUNIOR_PART1 + JUNIOR_PART2

__all__ = ["BATCH23_SENIOR", "BATCH23_JUNIOR", "SENIOR_PART1", "SENIOR_PART2", "JUNIOR_PART1", "JUNIOR_PART2"]

if __name__ == "__main__":
    print(f"Batch 23 loaded: {len(BATCH23_SENIOR)} Senior, {len(BATCH23_JUNIOR)} Junior articles.")
