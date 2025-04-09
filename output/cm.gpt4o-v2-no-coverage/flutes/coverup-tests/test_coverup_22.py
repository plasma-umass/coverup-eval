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
    r = Range(1, 11, 2)
    assert r[0:3] == [1, 3, 5]
    assert r[1:4] == [3, 5, 7]
    assert r[::2] == [1, 5, 9]
    assert r[1::2] == [3, 7]

def test_range_getitem_slice_negative():
    r = Range(1, 11, 2)
    assert r[-1] == 9
    assert r[-2] == 7
    assert r[-3] == 5
    assert r[-4] == 3
    assert r[-5] == 1

def test_range_getitem_slice_step():
    r = Range(1, 11, 2)
    assert r[0:5:2] == [1, 5, 9]
    assert r[1:5:2] == [3, 7]
    assert r[::3] == [1, 7]
    assert r[1::3] == [3, 9]

def test_range_getitem_slice_negative_step():
    r = Range(1, 11, 2)
    assert r[::-1] == [9, 7, 5, 3, 1]
    assert r[4:0:-1] == [9, 7, 5, 3]
    assert r[3:0:-2] == [7, 3]
    assert r[4:1:-2] == [9, 5]

@pytest.fixture(autouse=True)
def run_around_tests():
    # Code that will run before each test
    yield
    # Code that will run after each test
    # Clean up any state here
