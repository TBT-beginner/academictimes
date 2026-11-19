# -*- coding: utf-8 -*-
"""Batch 44 Unified Loader (2026-11-20)"""

from data_batch44_part1 import SENIOR_PART1
from data_batch44_part2 import SENIOR_PART2
from data_batch44_junior_part1 import JUNIOR_PART1
from data_batch44_junior_part2 import JUNIOR_PART2

BATCH44_SENIOR = SENIOR_PART1 + SENIOR_PART2
BATCH44_JUNIOR = JUNIOR_PART1 + JUNIOR_PART2

assert len(BATCH44_SENIOR) == 12, f"Expected 12 Senior, got {len(BATCH44_SENIOR)}"
assert len(BATCH44_JUNIOR) == 12, f"Expected 12 Junior, got {len(BATCH44_JUNIOR)}"
assert [a['slug'] for a in BATCH44_SENIOR] == [a['slug'] for a in BATCH44_JUNIOR], "Slug mismatch!"
