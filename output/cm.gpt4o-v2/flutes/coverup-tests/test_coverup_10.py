# file: flutes/iterator.py:313-314
# asked: {"lines": [313, 314], "branches": []}
# gained: {"lines": [313, 314], "branches": []}

import pytest
from flutes.iterator import Range

def test_range_init_with_start_stop_step():
    r = Range(1, 10, 2)
    assert r.l == 1
    assert r.r == 10
    assert r.step == 2
    assert r.val == 1
    assert r.length == (10 - 1) // 2

def test_range_init_with_stop():
    r = Range(10)
    assert r.l == 0
    assert r.r == 10
    assert r.step == 1
    assert r.val == 0
    assert r.length == (10 - 0) // 1

def test_range_init_with_start_stop():
    r = Range(1, 10)
    assert r.l == 1
    assert r.r == 10
    assert r.step == 1
    assert r.val == 1
    assert r.length == (10 - 1) // 1

def test_range_init_invalid_args():
    with pytest.raises(ValueError, match='Range should be called the same way as the builtin `range`'):
        Range()
    with pytest.raises(ValueError, match='Range should be called the same way as the builtin `range`'):
        Range(1, 2, 3, 4)
