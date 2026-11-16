# -*- coding: utf-8 -*-
"""Batch 40 Unified Loader (2026-11-16)"""

from data_batch40_part1 import SENIOR_PART1
from data_batch40_part2 import SENIOR_PART2
from data_batch40_junior_part1 import JUNIOR_PART1
from data_batch40_junior_part2 import JUNIOR_PART2

BATCH40_SENIOR = SENIOR_PART1 + SENIOR_PART2
BATCH40_JUNIOR = JUNIOR_PART1 + JUNIOR_PART2

assert len(BATCH40_SENIOR) == 12, f"Expected 12 Senior, got {len(BATCH40_SENIOR)}"
assert len(BATCH40_JUNIOR) == 12, f"Expected 12 Junior, got {len(BATCH40_JUNIOR)}"
assert [a['slug'] for a in BATCH40_SENIOR] == [a['slug'] for a in BATCH40_JUNIOR], "Slug mismatch!"
