# file pymonet/utils.py:59-61
# lines [59, 60, 61]
# branches []

import pytest
from pymonet.utils import curried_filter

def test_curried_filter():
    is_even = lambda x: x % 2 == 0
    numbers = [1, 2, 3, 4, 5, 6]

    # Test the curried filter with a list of numbers
    filtered_numbers = curried_filter(is_even)(numbers)
    assert filtered_numbers == [2, 4, 6]

    # Test the curried filter with an empty list
    filtered_empty = curried_filter(is_even)([])
    assert filtered_empty == []

    # Test the curried filter with no matching items
    no_evens = curried_filter(lambda x: False)(numbers)
    assert no_evens == []
