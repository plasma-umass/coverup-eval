# file: flutes/iterator.py:349-350
# asked: {"lines": [349, 350], "branches": []}
# gained: {"lines": [349, 350], "branches": []}

import pytest
from flutes.iterator import Range

def test_range_getitem_int():
    r = Range(1, 10, 2)
    assert r[0] == 1
    assert r[1] == 3
    assert r[2] == 5
    assert r[3] == 7
    assert r[4] == 9

def test_range_getitem_slice():
    r = Range(1, 10, 2)
    assert r[0:3] == [1, 3, 5]
    assert r[1:4] == [3, 5, 7]
    assert r[::2] == [1, 5]
    assert r[::-1] == [7, 5, 3, 1]
