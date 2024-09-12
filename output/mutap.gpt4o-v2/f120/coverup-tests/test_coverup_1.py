# file: f120/__init__.py:1-7
# asked: {"lines": [1, 3, 4, 5, 6, 7], "branches": [[3, 4], [3, 5]]}
# gained: {"lines": [1, 3, 4, 5, 6, 7], "branches": [[3, 4], [3, 5]]}

import pytest
from f120 import maximum

def test_maximum_k_zero():
    assert maximum([1, 2, 3], 0) == []

def test_maximum_sorted():
    arr = [3, 1, 2]
    result = maximum(arr, 2)
    assert result == [2, 3]
    assert arr == [1, 2, 3]  # Ensure the original array is sorted

def test_maximum_k_greater_than_zero():
    arr = [5, 3, 1, 4, 2]
    result = maximum(arr, 3)
    assert result == [3, 4, 5]
    assert arr == [1, 2, 3, 4, 5]  # Ensure the original array is sorted
