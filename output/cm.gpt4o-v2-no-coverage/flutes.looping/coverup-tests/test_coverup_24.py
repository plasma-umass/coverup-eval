# file: flutes/iterator.py:204-205
# asked: {"lines": [204, 205], "branches": []}
# gained: {"lines": [204, 205], "branches": []}

import pytest
from flutes.iterator import scanr

def test_scanr_no_initial():
    result = scanr(lambda x, y: x + y, [1, 2, 3])
    assert result == [6, 5, 3]

def test_scanr_with_initial():
    result = scanr(lambda x, y: x + y, [1, 2, 3], 10)
    assert result == [16, 15, 13, 10]

def test_scanr_empty_iterable():
    result = scanr(lambda x, y: x + y, [], 10)
    assert result == [10]

def test_scanr_single_element():
    result = scanr(lambda x, y: x + y, [5], 10)
    assert result == [15, 10]
