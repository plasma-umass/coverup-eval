# file: flutes/iterator.py:349-350
# asked: {"lines": [349, 350], "branches": []}
# gained: {"lines": [349, 350], "branches": []}

import pytest
from flutes.iterator import Range

def test_range_getitem_slice():
    r = Range(1, 11, 2)
    result = r[1:4]
    assert result == [3, 5, 7]

def test_range_getitem_slice_empty():
    r = Range(1, 11, 2)
    result = r[10:20]
    assert result == []

def test_range_getitem_slice_step():
    r = Range(1, 11, 2)
    result = r[::2]
    assert result == [1, 5, 9]

def test_range_getitem_slice_negative_step():
    r = Range(1, 11, 2)
    result = r[4:1:-1]
    assert result == [9, 7, 5]

def test_range_getitem_slice_negative_indices():
    r = Range(1, 11, 2)
    result = r[-3:-1]
    assert result == [5, 7]
