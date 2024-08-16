#!/usr/bin/env python3
"""This module defines a function `sum_mixed_list`."""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Sum up list of int and float."""
    return sum(x for x in mxd_lst)
