# file: flutes/iterator.py:119-121
# asked: {"lines": [119, 120, 121], "branches": []}
# gained: {"lines": [119, 120, 121], "branches": []}

import pytest
from typing import List
from flutes.iterator import split_by

def test_split_by_with_separator():
    iterable = [1, 2, 0, 3, 0, 4, 5]
    separator = 0
    result = list(split_by(iterable, separator=separator))
    expected = [[1, 2], [3], [4, 5]]
    assert result == expected

def test_split_by_with_empty_segments():
    iterable = [1, 2, 0, 3, 0, 4, 5]
    separator = 0
    result = list(split_by(iterable, empty_segments=True, separator=separator))
    expected = [[1, 2], [3], [4, 5]]
    assert result == expected

def test_split_by_with_criterion():
    iterable = [1, 2, 0, 3, 0, 4, 5]
    criterion = lambda x: x == 0
    result = list(split_by(iterable, criterion=criterion))
    expected = [[1, 2], [3], [4, 5]]
    assert result == expected

def test_split_by_with_empty_segments_and_criterion():
    iterable = [1, 2, 0, 3, 0, 4, 5]
    criterion = lambda x: x == 0
    result = list(split_by(iterable, empty_segments=True, criterion=criterion))
    expected = [[1, 2], [3], [4, 5]]
    assert result == expected
