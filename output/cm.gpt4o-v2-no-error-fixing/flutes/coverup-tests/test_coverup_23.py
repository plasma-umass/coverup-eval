# file: flutes/iterator.py:23-44
# asked: {"lines": [23, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44], "branches": [[35, 36], [35, 37], [38, 39], [38, 43], [40, 38], [40, 41], [43, 0], [43, 44]]}
# gained: {"lines": [23, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44], "branches": [[35, 36], [35, 37], [38, 39], [38, 43], [40, 38], [40, 41], [43, 0], [43, 44]]}

import pytest
from flutes.iterator import chunk

def test_chunk_with_positive_n():
    result = list(chunk(3, range(10)))
    assert result == [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9]]

def test_chunk_with_remainder():
    result = list(chunk(4, range(10)))
    assert result == [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9]]

def test_chunk_with_exact_division():
    result = list(chunk(5, range(10)))
    assert result == [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]]

def test_chunk_with_n_greater_than_length():
    result = list(chunk(15, range(10)))
    assert result == [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]

def test_chunk_with_n_equal_to_zero():
    with pytest.raises(ValueError, match="`n` should be positive"):
        list(chunk(0, range(10)))

def test_chunk_with_n_less_than_zero():
    with pytest.raises(ValueError, match="`n` should be positive"):
        list(chunk(-1, range(10)))
