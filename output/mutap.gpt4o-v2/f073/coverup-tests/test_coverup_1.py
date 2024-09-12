# file: f073/__init__.py:1-7
# asked: {"lines": [1, 3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}
# gained: {"lines": [1, 3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}

import pytest
from f073 import smallest_change

def test_smallest_change_empty_array():
    assert smallest_change([]) == 0

def test_smallest_change_single_element():
    assert smallest_change([1]) == 0

def test_smallest_change_no_change_needed():
    assert smallest_change([1, 2, 3, 2, 1]) == 0

def test_smallest_change_one_change_needed():
    assert smallest_change([1, 2, 3, 4, 1]) == 1

def test_smallest_change_multiple_changes_needed():
    assert smallest_change([1, 2, 3, 4, 5]) == 2
