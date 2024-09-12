# file: f043/__init__.py:1-7
# asked: {"lines": [1, 3, 4, 5, 6, 7], "branches": [[3, 4], [3, 7], [4, 3], [4, 5], [5, 4], [5, 6]]}
# gained: {"lines": [1, 3, 4, 5, 6, 7], "branches": [[3, 4], [3, 7], [4, 3], [4, 5], [5, 4], [5, 6]]}

import pytest
from f043 import pairs_sum_to_zero

def test_pairs_sum_to_zero_with_pairs():
    assert pairs_sum_to_zero([1, -1, 2, 3]) == True

def test_pairs_sum_to_zero_without_pairs():
    assert pairs_sum_to_zero([1, 2, 3, 4]) == False

def test_pairs_sum_to_zero_empty_list():
    assert pairs_sum_to_zero([]) == False

def test_pairs_sum_to_zero_single_element():
    assert pairs_sum_to_zero([1]) == False

def test_pairs_sum_to_zero_multiple_zeros():
    assert pairs_sum_to_zero([0, 0, 1, 2]) == True
