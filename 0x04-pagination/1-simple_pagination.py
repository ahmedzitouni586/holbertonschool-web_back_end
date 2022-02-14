#!/usr/bin/env python3
"""Simple pagination"""
import csv
import math
from typing import List, Tuple


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """return list"""
        assert type(page) is int
        assert type(page_size) is int
        assert page > 0
        assert page > page_size
        self.dataset()
        a = index_range(page, page_size)
        if a[0] >= len(self.__dataset):
            return []
        else:
            return self.__dataset[a[0]:a[1]]


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """return a tuple of size two containing a start index and an end index"""
    total_size = page * page_size
    page_n = total_size - page_size
    return (page_n, page)
