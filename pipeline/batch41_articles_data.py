# -*- coding: utf-8 -*-
"""Batch 41 Unified Loader (2026-11-17)"""

from data_batch41_part1 import SENIOR_PART1
from data_batch41_part2 import SENIOR_PART2
from data_batch41_junior_part1 import JUNIOR_PART1
from data_batch41_junior_part2 import JUNIOR_PART2

BATCH41_SENIOR = SENIOR_PART1 + SENIOR_PART2
BATCH41_JUNIOR = JUNIOR_PART1 + JUNIOR_PART2

assert len(BATCH41_SENIOR) == 12, f"Expected 12 Senior, got {len(BATCH41_SENIOR)}"
assert len(BATCH41_JUNIOR) == 12, f"Expected 12 Junior, got {len(BATCH41_JUNIOR)}"
assert [a['slug'] for a in BATCH41_SENIOR] == [a['slug'] for a in BATCH41_JUNIOR], "Slug mismatch!"
