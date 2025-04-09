# file flutes/iterator.py:47-66
# lines [47, 59, 60, 61, 62, 63, 64, 65, 66]
# branches ['59->60', '59->61', '63->exit', '63->64']

import pytest
from flutes.iterator import take

def test_take_negative_n():
    with pytest.raises(ValueError):
        list(take(-1, range(10)))

def test_take_more_than_exists():
    result = list(take(10, range(5)))
    assert result == [0, 1, 2, 3, 4]

def test_take_less_than_exists():
    result = list(take(3, range(5)))
    assert result == [0, 1, 2]

def test_take_empty_iterable():
    result = list(take(3, []))
    assert result == []

def test_take_zero_n():
    result = list(take(0, range(5)))
    assert result == []
