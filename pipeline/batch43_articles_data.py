# -*- coding: utf-8 -*-
"""Batch 43 Unified Loader (2026-11-19)"""

from data_batch43_part1 import SENIOR_PART1
from data_batch43_part2 import SENIOR_PART2
from data_batch43_junior_part1 import JUNIOR_PART1
from data_batch43_junior_part2 import JUNIOR_PART2

BATCH43_SENIOR = SENIOR_PART1 + SENIOR_PART2
BATCH43_JUNIOR = JUNIOR_PART1 + JUNIOR_PART2

assert len(BATCH43_SENIOR) == 12, f"Expected 12 Senior, got {len(BATCH43_SENIOR)}"
assert len(BATCH43_JUNIOR) == 12, f"Expected 12 Junior, got {len(BATCH43_JUNIOR)}"
assert [a['slug'] for a in BATCH43_SENIOR] == [a['slug'] for a in BATCH43_JUNIOR], "Slug mismatch!"
