# file: f135/__init__.py:1-9
# asked: {"lines": [1, 3, 4, 5, 6, 7, 8, 9], "branches": [[5, 6], [5, 9], [6, 7], [6, 8]]}
# gained: {"lines": [1, 3, 4, 5, 6, 7, 8, 9], "branches": [[5, 6], [5, 9], [6, 7], [6, 8]]}

import pytest

from f135 import can_arrange

def test_can_arrange_sorted_list():
    arr = [1, 2, 3, 4, 5]
    result = can_arrange(arr)
    assert result == -1

def test_can_arrange_unsorted_list():
    arr = [1, 3, 2, 4, 5]
    result = can_arrange(arr)
    assert result == 2

def test_can_arrange_empty_list():
    arr = []
    result = can_arrange(arr)
    assert result == -1

def test_can_arrange_single_element_list():
    arr = [1]
    result = can_arrange(arr)
    assert result == -1

def test_can_arrange_all_elements_same():
    arr = [2, 2, 2, 2]
    result = can_arrange(arr)
    assert result == -1
