#!/usr/bin/env python3
"""Corrected Annotated function"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Make a tuple from list."""
    return [(i, len(i)) for i in lst]
