# file: flutes/iterator.py:313-314
# asked: {"lines": [313, 314], "branches": []}
# gained: {"lines": [313, 314], "branches": []}

import pytest
from flutes.iterator import Range

def test_range_init_single_argument():
    r = Range(10)
    assert r.l == 0
    assert r.r == 10
    assert r.step == 1
    assert r.val == 0
    assert r.length == 10

def test_range_init_two_arguments():
    r = Range(1, 10)
    assert r.l == 1
    assert r.r == 10
    assert r.step == 1
    assert r.val == 1
    assert r.length == 9

def test_range_init_three_arguments():
    r = Range(1, 11, 2)
    assert r.l == 1
    assert r.r == 11
    assert r.step == 2
    assert r.val == 1
    assert r.length == 5

def test_range_init_invalid_arguments():
    with pytest.raises(ValueError, match='Range should be called the same way as the builtin `range`'):
        Range()
    with pytest.raises(ValueError, match='Range should be called the same way as the builtin `range`'):
        Range(1, 2, 3, 4)
