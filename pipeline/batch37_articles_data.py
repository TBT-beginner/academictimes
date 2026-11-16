# -*- coding: utf-8 -*-
"""Batch 37 Unified Loader (2026-11-13)"""

from data_batch37_part1 import SENIOR_PART1
from data_batch37_part2 import SENIOR_PART2
from data_batch37_junior_part1 import JUNIOR_PART1
from data_batch37_junior_part2 import JUNIOR_PART2

BATCH37_SENIOR = SENIOR_PART1 + SENIOR_PART2
BATCH37_JUNIOR = JUNIOR_PART1 + JUNIOR_PART2

assert len(BATCH37_SENIOR) == 12, f"Expected 12 Senior, got {len(BATCH37_SENIOR)}"
assert len(BATCH37_JUNIOR) == 12, f"Expected 12 Junior, got {len(BATCH37_JUNIOR)}"
assert [a['slug'] for a in BATCH37_SENIOR] == [a['slug'] for a in BATCH37_JUNIOR], "Slug mismatch!"
