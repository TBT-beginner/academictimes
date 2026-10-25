# -*- coding: utf-8 -*-
"""
Batch 21 Articles Data (2026-10-26)
12 Senior + 12 Junior Articles
All primary sources verified HTTP 200 OK from The Guardian (Oct 22-25, 2026).
"""

from data_batch21_part1 import SENIOR_PART1
from data_batch21_part2 import SENIOR_PART2
from data_batch21_junior_part1 import JUNIOR_PART1
from data_batch21_junior_part2 import JUNIOR_PART2

BATCH21_SENIOR = SENIOR_PART1 + SENIOR_PART2
BATCH21_JUNIOR = JUNIOR_PART1 + JUNIOR_PART2

print(f"Batch 21 loaded: {len(BATCH21_SENIOR)} Senior, {len(BATCH21_JUNIOR)} Junior articles.")
