# -*- coding: utf-8 -*-
"""Batch 42 Unified Loader (2026-11-18)"""

from data_batch42_part1 import SENIOR_PART1
from data_batch42_part2 import SENIOR_PART2
from data_batch42_junior_part1 import JUNIOR_PART1
from data_batch42_junior_part2 import JUNIOR_PART2

BATCH42_SENIOR = SENIOR_PART1 + SENIOR_PART2
BATCH42_JUNIOR = JUNIOR_PART1 + JUNIOR_PART2

assert len(BATCH42_SENIOR) == 12, f"Expected 12 Senior, got {len(BATCH42_SENIOR)}"
assert len(BATCH42_JUNIOR) == 12, f"Expected 12 Junior, got {len(BATCH42_JUNIOR)}"
assert [a['slug'] for a in BATCH42_SENIOR] == [a['slug'] for a in BATCH42_JUNIOR], "Slug mismatch!"
