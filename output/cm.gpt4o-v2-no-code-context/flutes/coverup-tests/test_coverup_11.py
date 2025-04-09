# file: flutes/iterator.py:23-44
# asked: {"lines": [23, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44], "branches": [[35, 36], [35, 37], [38, 39], [38, 43], [40, 38], [40, 41], [43, 0], [43, 44]]}
# gained: {"lines": [23, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44], "branches": [[35, 36], [35, 37], [38, 39], [38, 43], [40, 38], [40, 41], [43, 0], [43, 44]]}

import pytest
from flutes.iterator import chunk

def test_chunk_with_positive_n():
    result = list(chunk(3, range(10)))
    assert result == [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9]]

def test_chunk_with_exact_multiple():
    result = list(chunk(2, range(6)))
    assert result == [[0, 1], [2, 3], [4, 5]]

def test_chunk_with_non_multiple():
    result = list(chunk(4, range(10)))
    assert result == [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9]]

def test_chunk_with_single_element_chunks():
    result = list(chunk(1, range(5)))
    assert result == [[0], [1], [2], [3], [4]]

def test_chunk_with_large_n():
    result = list(chunk(10, range(5)))
    assert result == [[0, 1, 2, 3, 4]]

def test_chunk_with_zero_n():
    with pytest.raises(ValueError, match="`n` should be positive"):
        list(chunk(0, range(5)))

def test_chunk_with_negative_n():
    with pytest.raises(ValueError, match="`n` should be positive"):
        list(chunk(-1, range(5)))
