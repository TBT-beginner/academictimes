# -*- coding: utf-8 -*-
"""
Batch 22 Articles Data (2026-10-25)
12 Senior + 12 Junior Articles
All primary sources verified HTTP 200 OK from The Guardian (Oct 24-25, 2026).
"""

from data_batch22_part1 import SENIOR_PART1
from data_batch22_part2 import SENIOR_PART2
from data_batch22_junior_part1 import JUNIOR_PART1
from data_batch22_junior_part2 import JUNIOR_PART2

BATCH22_SENIOR = SENIOR_PART1 + SENIOR_PART2
BATCH22_JUNIOR = JUNIOR_PART1 + JUNIOR_PART2

print(f"Batch 22 loaded: {len(BATCH22_SENIOR)} Senior, {len(BATCH22_JUNIOR)} Junior articles.")
