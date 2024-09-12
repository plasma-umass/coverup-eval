# file: f105/__init__.py:1-21
# asked: {"lines": [1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21], "branches": [[16, 17], [16, 21]]}
# gained: {"lines": [1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21], "branches": [[16, 17], [16, 21]]}

import pytest
from f105 import by_length

def test_by_length_all_valid():
    result = by_length([1, 2, 3])
    assert result == ["Three", "Two", "One"]

def test_by_length_with_invalid():
    result = by_length([1, 2, 10])
    assert result == ["Two", "One"]

def test_by_length_empty():
    result = by_length([])
    assert result == []

def test_by_length_all_invalid():
    result = by_length([10, 11, 12])
    assert result == []

def test_by_length_mixed():
    result = by_length([3, 1, 4, 10])
    assert result == ["Four", "Three", "One"]
