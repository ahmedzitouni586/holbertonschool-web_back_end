#!/usr/bin/env python3
"""module to return sum of mixed list"""
from typing import Union

FloatInt = Union[int, float]

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """return sum of mixed list"""
    return sum(mxd_lst)
