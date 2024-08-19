#!/usr/bin/env python3
"""A module to paginate API results"""


def index_range(page: int, page_size: int) -> tuple:
    """
        A function that gets the first and the last
        indices of a page.
    """
    first_index = (page - 1) * page_size
    last_index = first_index + page_size
    return (first_index, last_index)
