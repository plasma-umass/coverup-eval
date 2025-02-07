# file: flutes/iterator.py:23-44
# asked: {"lines": [23, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44], "branches": [[35, 36], [35, 37], [38, 39], [38, 43], [40, 38], [40, 41], [43, 0], [43, 44]]}
# gained: {"lines": [23, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44], "branches": [[35, 36], [35, 37], [38, 39], [38, 43], [40, 38], [40, 41], [43, 0], [43, 44]]}

import pytest
from flutes.iterator import chunk

def test_chunk_positive_n():
    result = list(chunk(3, range(10)))
    assert result == [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9]]

def test_chunk_n_greater_than_iterable_length():
    result = list(chunk(15, range(10)))
    assert result == [list(range(10))]

def test_chunk_n_equals_iterable_length():
    result = list(chunk(10, range(10)))
    assert result == [list(range(10))]

def test_chunk_n_is_one():
    result = list(chunk(1, range(3)))
    assert result == [[0], [1], [2]]

def test_chunk_n_is_zero():
    with pytest.raises(ValueError, match="`n` should be positive"):
        list(chunk(0, range(10)))

def test_chunk_n_is_negative():
    with pytest.raises(ValueError, match="`n` should be positive"):
        list(chunk(-1, range(10)))

def test_chunk_empty_iterable():
    result = list(chunk(3, []))
    assert result == []

