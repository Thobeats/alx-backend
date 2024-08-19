#!/usr/bin/env python3
"""Simple Pagination Module"""
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

    @staticmethod
    def index_range(page: int, page_size: int) -> Tuple[int, int]:
        """
            A function that gets the first and the last
            indices of a page.
        """
        first_index = (page - 1) * page_size
        last_index = first_index + page_size
        return (first_index, last_index)

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Get Pages

        Keyword arguments:
        page -- an integer: The starting page
        page_size -- an integer: The amount of records you want
        Return: List[List]
        """

        assert type(page) is int and type(page_size) is int
        assert page > 0 and page_size > 0

        # Read the CSV File and save it into a list of lists
        start, end = self.index_range(page, page_size)
        return self.dataset()[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """Get Hyper

        Keyword arguments:
        page -- an integer: The starting page
        page_size -- an integer: The amount of records you want
        Return: dict
        """

        assert type(page) is int and type(page_size) is int
        assert page > 0 and page_size > 0

        # Read the CSV File and save it into a list of lists
        start, end = self.index_range(page, page_size)
        result = self.get_page(page, page_size)
        next_page = page + 1 if end < len(self.dataset()) else None
        prev_page = page - 1 if page > 1 else None
        total_pages = len(self.dataset()) / page_size
        return {
            "page_size": len(result),
            "page": page,
            "data": result,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": math.ceil(total_pages)
        }
