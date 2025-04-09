# file: pymonet/utils.py:54-56
# asked: {"lines": [54, 55, 56], "branches": []}
# gained: {"lines": [54, 55, 56], "branches": []}

import pytest
from pymonet.utils import curried_map

def test_curried_map():
    # Test the curried_map function with a simple mapper and collection
    mapper = lambda x: x * 2
    collection = [1, 2, 3]
    expected_result = [2, 4, 6]
    
    # Apply the curried_map function
    result = curried_map(mapper, collection)
    
    # Assert the result is as expected
    assert result == expected_result

    # Test the curried_map function with currying
    curried_function = curried_map(mapper)
    result = curried_function(collection)
    
    # Assert the result is as expected
    assert result == expected_result
