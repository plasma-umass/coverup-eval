# file: pymonet/utils.py:59-61
# asked: {"lines": [59, 60, 61], "branches": []}
# gained: {"lines": [59, 60, 61], "branches": []}

import pytest
from pymonet.utils import curried_filter, curry

def test_curried_filter():
    # Test with a simple filter function and collection
    filter_func = lambda x: x % 2 == 0
    collection = [1, 2, 3, 4, 5, 6]
    expected_result = [2, 4, 6]
    
    curried = curried_filter(filter_func)
    result = curried(collection)
    
    assert result == expected_result

    # Test with an empty collection
    collection = []
    expected_result = []
    
    result = curried(collection)
    
    assert result == expected_result

    # Test with a filter function that filters out all items
    filter_func = lambda x: False
    collection = [1, 2, 3, 4, 5, 6]
    expected_result = []
    
    curried = curried_filter(filter_func)
    result = curried(collection)
    
    assert result == expected_result

    # Test with a filter function that keeps all items
    filter_func = lambda x: True
    collection = [1, 2, 3, 4, 5, 6]
    expected_result = [1, 2, 3, 4, 5, 6]
    
    curried = curried_filter(filter_func)
    result = curried(collection)
    
    assert result == expected_result

    # Test currying with multiple arguments
    filter_func = lambda x: x > 3
    collection = [1, 2, 3, 4, 5, 6]
    expected_result = [4, 5, 6]
    
    curried = curried_filter(filter_func)
    result = curried(collection)
    
    assert result == expected_result
