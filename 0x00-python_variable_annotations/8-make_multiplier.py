#!/usr/bin/env python3
"""This module defines a function `make_multiplier`."""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a float multiplier function."""
    def multiplier_func(inner_multiplier: float) -> float:
        return multiplier * inner_multiplier

    return multiplier_func
