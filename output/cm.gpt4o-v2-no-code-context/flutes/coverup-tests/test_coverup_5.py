# file: flutes/iterator.py:47-66
# asked: {"lines": [47, 59, 60, 61, 62, 63, 64, 65, 66], "branches": [[59, 60], [59, 61], [63, 0], [63, 64]]}
# gained: {"lines": [47, 59, 60, 61, 62, 63, 64, 65, 66], "branches": [[59, 60], [59, 61], [63, 0], [63, 64]]}

import pytest
from flutes.iterator import take

def test_take_positive_n():
    result = list(take(5, range(10)))
    assert result == [0, 1, 2, 3, 4]

def test_take_zero_n():
    result = list(take(0, range(10)))
    assert result == []

def test_take_negative_n():
    with pytest.raises(ValueError, match="`n` should be non-negative"):
        list(take(-1, range(10)))

def test_take_less_elements_than_n():
    result = list(take(5, range(3)))
    assert result == [0, 1, 2]

def test_take_empty_iterable():
    result = list(take(5, []))
    assert result == []

def test_take_exhausted_iterable():
    it = iter([1, 2, 3])
    next(it)
    next(it)
    next(it)
    result = list(take(2, it))
    assert result == []
