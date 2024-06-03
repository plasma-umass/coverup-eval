# file pymonet/utils.py:59-61
# lines [59, 60, 61]
# branches []

import pytest
from pymonet.utils import curried_filter

def test_curried_filter():
    # Define a simple filter function
    def is_even(x):
        return x % 2 == 0

    # Create a curried filter function
    filter_even = curried_filter(is_even)

    # Test the curried filter function with a sample collection
    collection = [1, 2, 3, 4, 5, 6]
    filtered_collection = filter_even(collection)

    # Assert the filtered collection is as expected
    assert filtered_collection == [2, 4, 6]

    # Test with an empty collection
    empty_collection = []
    filtered_empty_collection = filter_even(empty_collection)

    # Assert the filtered empty collection is as expected
    assert filtered_empty_collection == []

    # Test with a collection that has no items matching the filter
    no_match_collection = [1, 3, 5]
    filtered_no_match_collection = filter_even(no_match_collection)

    # Assert the filtered no match collection is as expected
    assert filtered_no_match_collection == []

    # Test with a collection that has all items matching the filter
    all_match_collection = [2, 4, 6]
    filtered_all_match_collection = filter_even(all_match_collection)

    # Assert the filtered all match collection is as expected
    assert filtered_all_match_collection == [2, 4, 6]
