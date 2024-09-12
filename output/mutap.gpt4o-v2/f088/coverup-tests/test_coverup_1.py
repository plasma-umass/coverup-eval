# file: f088/__init__.py:1-3
# asked: {"lines": [1, 3], "branches": []}
# gained: {"lines": [1, 3], "branches": []}

import pytest
from f088 import sort_array

def test_sort_array_empty():
    assert sort_array([]) == []

def test_sort_array_even_sum():
    array = [2, 4, 6]
    sorted_array = sort_array(array)
    assert sorted_array == [6, 4, 2]

def test_sort_array_odd_sum():
    array = [1, 3, 5]
    sorted_array = sort_array(array)
    assert sorted_array == [5, 3, 1]

def test_sort_array_mixed_sum_even():
    array = [1, 2, 3]
    sorted_array = sort_array(array)
    assert sorted_array == [3, 2, 1]

def test_sort_array_mixed_sum_odd():
    array = [1, 2, 4]
    sorted_array = sort_array(array)
    assert sorted_array == [1, 2, 4]
