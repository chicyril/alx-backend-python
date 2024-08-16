#!/usr/bin/env python3
"""Annotate function"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Make Union from list."""
    if lst:
        return lst[0]
    else:
        return None
