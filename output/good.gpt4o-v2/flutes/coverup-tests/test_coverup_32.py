# file: flutes/iterator.py:346-347
# asked: {"lines": [346, 347], "branches": []}
# gained: {"lines": [346, 347], "branches": []}

import pytest
from flutes.iterator import Range

def test_range_getitem_int():
    r = Range(1, 11, 2)
    assert r[0] == 1
    assert r[1] == 3
    assert r[2] == 5
    assert r[3] == 7
    assert r[4] == 9

def test_range_getitem_slice():
    r = Range(1, 11, 2)
    assert r[0:3] == [1, 3, 5]
    assert r[1:4] == [3, 5, 7]

def test_range_getitem_negative_index():
    r = Range(1, 11, 2)
    assert r[-1] == 9
    assert r[-2] == 7
    assert r[-3] == 5
    assert r[-4] == 3
    assert r[-5] == 1

def test_range_getitem_slice_negative_index():
    r = Range(1, 11, 2)
    assert r[-5:-2] == [1, 3, 5]
    assert r[-4:-1] == [3, 5, 7]
