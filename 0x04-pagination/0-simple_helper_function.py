#!/usr/bin/env python3
"""helper function"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """return a tuple of size two containing a start index and an end index"""
    total_size = page * page_size
    page_n = total_size - page_size
    return (page_n, page)
