# file: f090/__init__.py:1-4
# asked: {"lines": [1, 3, 4], "branches": []}
# gained: {"lines": [1, 3, 4], "branches": []}

import pytest
from f090 import next_smallest

def test_next_smallest_empty_list():
    assert next_smallest([]) is None

def test_next_smallest_single_element():
    assert next_smallest([1]) is None

def test_next_smallest_two_elements():
    assert next_smallest([2, 1]) == 2

def test_next_smallest_multiple_elements():
    assert next_smallest([4, 2, 5, 1, 3]) == 2

def test_next_smallest_duplicates():
    assert next_smallest([4, 2, 2, 5, 1, 3, 3]) == 2
