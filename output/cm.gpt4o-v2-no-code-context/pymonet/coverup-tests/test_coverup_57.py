# file: pymonet/utils.py:59-61
# asked: {"lines": [59, 60, 61], "branches": []}
# gained: {"lines": [59, 60, 61], "branches": []}

import pytest
from pymonet.utils import curried_filter
from pymonet.utils import curry

def test_curried_filter():
    # Test curried_filter with a simple filter function and collection
    filterer = lambda x: x % 2 == 0
    collection = [1, 2, 3, 4, 5, 6]
    expected_result = [2, 4, 6]
    
    # Apply the curried filter
    result = curried_filter(filterer)(collection)
    
    # Assert the result is as expected
    assert result == expected_result

    # Test curried_filter with an empty collection
    collection = []
    expected_result = []
    
    # Apply the curried filter
    result = curried_filter(filterer)(collection)
    
    # Assert the result is as expected
    assert result == expected_result

    # Test curried_filter with a filter function that filters out all items
    filterer = lambda x: False
    collection = [1, 2, 3, 4, 5, 6]
    expected_result = []
    
    # Apply the curried filter
    result = curried_filter(filterer)(collection)
    
    # Assert the result is as expected
    assert result == expected_result

    # Test curried_filter with a filter function that keeps all items
    filterer = lambda x: True
    collection = [1, 2, 3, 4, 5, 6]
    expected_result = [1, 2, 3, 4, 5, 6]
    
    # Apply the curried filter
    result = curried_filter(filterer)(collection)
    
    # Assert the result is as expected
    assert result == expected_result
