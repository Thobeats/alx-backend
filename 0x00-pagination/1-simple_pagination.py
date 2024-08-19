#!/usr/bin/env python3
"""Simple Pagination Module"""
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """
        A function that gets the first and the last
        indices of a page.
    """
    first_index = (page - 1) * page_size
    last_index = first_index + page_size
    return (first_index, last_index)


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
        assert type(page) is int
        assert type(page_size) is int
        assert page > 0
        assert page_size > 0

        # Read the CSV File and save it into a list of lists
        pages = list()
        indexRange = index_range(page, page_size)

        with open('popular_baby_names.csv', 'r', newline='') as babyNames:
            name_reader = csv.reader(babyNames, delimiter=",", quotechar="|")
            counter = 0
            page_range = range(indexRange[0] + 1, indexRange[1] + 2)
            for row in name_reader:
                counter += 1
                if counter in page_range:
                    # name_reader_list = row.split(',')
                    pages.append(row)
        return pages
