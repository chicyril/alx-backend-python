#!/usr/bin/env python3
"""This module define a type-annotated function `sum_list`."""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Sum up list of floats."""
    return sum(x for x in input_list)
