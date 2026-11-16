# -*- coding: utf-8 -*-
"""Batch 39 Unified Loader (2026-11-15)"""

from data_batch39_part1 import SENIOR_PART1
from data_batch39_part2 import SENIOR_PART2
from data_batch39_junior_part1 import JUNIOR_PART1
from data_batch39_junior_part2 import JUNIOR_PART2

BATCH39_SENIOR = SENIOR_PART1 + SENIOR_PART2
BATCH39_JUNIOR = JUNIOR_PART1 + JUNIOR_PART2

assert len(BATCH39_SENIOR) == 12, f"Expected 12 Senior, got {len(BATCH39_SENIOR)}"
assert len(BATCH39_JUNIOR) == 12, f"Expected 12 Junior, got {len(BATCH39_JUNIOR)}"
assert [a['slug'] for a in BATCH39_SENIOR] == [a['slug'] for a in BATCH39_JUNIOR], "Slug mismatch!"
