#!/usr/bin/env python3

from typing import Union, Tuple

FloatInt = Union[int, float]
x = Tuple[str, float]
def to_kv(k: str, v: FloatInt) -> x:
    return (k, v)
