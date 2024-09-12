# file: f122/__init__.py:1-3
# asked: {"lines": [1, 3], "branches": []}
# gained: {"lines": [1, 3], "branches": []}

import pytest
from f122 import add_elements

def test_add_elements():
    # Test case where arr has elements with length <= 2 and k is within the range of arr
    arr = [1, 22, 333, 4]
    k = 3
    result = add_elements(arr, k)
    assert result == 23  # 1 + 22

    # Test case where arr has elements with length > 2 and k is within the range of arr
    arr = [123, 456, 78, 9]
    k = 2
    result = add_elements(arr, k)
    assert result == 0  # No elements with length <= 2

    # Test case where k is larger than the length of arr
    arr = [1, 2, 3]
    k = 5
    result = add_elements(arr, k)
    assert result == 6  # 1 + 2 + 3

    # Test case where arr is empty
    arr = []
    k = 3
    result = add_elements(arr, k)
    assert result == 0  # No elements to sum

    # Test case where k is 0
    arr = [1, 2, 3]
    k = 0
    result = add_elements(arr, k)
    assert result == 0  # No elements to sum
