# file: f126/__init__.py:1-11
# asked: {"lines": [1, 3, 4, 5, 6, 7, 8, 9, 11], "branches": [[4, 5], [4, 6], [6, 7], [6, 8], [8, 9], [8, 11]]}
# gained: {"lines": [1, 3, 4, 5, 6, 7, 8, 9, 11], "branches": [[4, 5], [4, 6], [6, 7], [6, 8], [8, 9], [8, 11]]}

import pytest
from f126 import is_sorted

def test_is_sorted_empty_list():
    assert is_sorted([]) == True

def test_is_sorted_single_element():
    assert is_sorted([1]) == True

def test_is_sorted_two_elements_sorted():
    assert is_sorted([1, 2]) == True

def test_is_sorted_two_elements_unsorted():
    assert is_sorted([2, 1]) == False

def test_is_sorted_multiple_elements_sorted():
    assert is_sorted([1, 2, 3, 4, 5]) == True

def test_is_sorted_multiple_elements_unsorted():
    assert is_sorted([1, 3, 2, 4, 5]) == False

def test_is_sorted_with_duplicates():
    assert is_sorted([1, 2, 2, 3, 4]) == True

def test_is_sorted_with_more_than_two_duplicates():
    assert is_sorted([1, 2, 2, 2, 3, 4]) == False

def test_is_sorted_with_all_elements_same():
    assert is_sorted([2, 2, 2, 2]) == False
