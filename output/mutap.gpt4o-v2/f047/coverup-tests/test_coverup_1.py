# file: f047/__init__.py:1-7
# asked: {"lines": [1, 3, 4, 5, 7], "branches": [[4, 5], [4, 7]]}
# gained: {"lines": [1, 3, 4, 5, 7], "branches": [[4, 5], [4, 7]]}

import pytest
from f047 import median

def test_median_odd_length():
    assert median([3, 1, 2]) == 2

def test_median_even_length():
    assert median([4, 1, 3, 2]) == 2.5

def test_median_empty_list():
    with pytest.raises(IndexError):
        median([])

def test_median_single_element():
    assert median([1]) == 1

def test_median_two_elements():
    assert median([1, 2]) == 1.5
