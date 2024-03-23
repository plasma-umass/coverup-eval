# file pymonet/utils.py:54-56
# lines [54, 55, 56]
# branches []

import pytest
from pymonet.utils import curried_map

def test_curried_map():
    # Test the curried_map function with a mapper and a collection
    mapper = lambda x: x * 2
    collection = [1, 2, 3]
    expected_result = [2, 4, 6]

    # Test the curried version by passing one argument at a time
    curried_version = curried_map(mapper)
    assert callable(curried_version), "curried_map should return a callable when partially applied"

    result = curried_version(collection)
    assert result == expected_result, "curried_map did not correctly map the collection"

    # Test the non-curried version by passing both arguments at once
    result_direct = curried_map(mapper, collection)
    assert result_direct == expected_result, "curried_map did not correctly map the collection when fully applied"

    # Clean up is not necessary as no external state is modified
