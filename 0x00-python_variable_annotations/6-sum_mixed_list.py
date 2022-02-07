#!/usr/bin/env python3
"""module to return sum of mixed list"""
from typing import Union

FloatInt = Union[int, float]

def sum_mixed_list(mxd_lst: FloatInt) -> float:
    """return sum of mixed list"""
    sum = 0.0
    for val in mxd_lst:
        sum += val
    return sum
