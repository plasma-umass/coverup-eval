# file: flutes/iterator.py:330-331
# asked: {"lines": [331], "branches": []}
# gained: {"lines": [331], "branches": []}

import pytest
from flutes.iterator import Range

def test_range_iter():
    r = Range(1, 5)
    it = iter(r)
    assert next(it) == 1
    assert next(it) == 2
    assert next(it) == 3
    assert next(it) == 4
    with pytest.raises(StopIteration):
        next(it)

def test_range_single_arg():
    r = Range(5)
    assert list(r) == [0, 1, 2, 3, 4]

def test_range_two_args():
    r = Range(1, 5)
    assert list(r) == [1, 2, 3, 4]

def test_range_three_args():
    r = Range(1, 10, 2)
    assert list(r) == [1, 3, 5, 7, 9]

def test_range_invalid_args():
    with pytest.raises(ValueError):
        Range()
    with pytest.raises(ValueError):
        Range(1, 2, 3, 4)
