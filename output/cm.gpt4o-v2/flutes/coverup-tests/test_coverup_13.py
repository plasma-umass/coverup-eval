# file: flutes/iterator.py:119-121
# asked: {"lines": [119, 120, 121], "branches": []}
# gained: {"lines": [119, 120, 121], "branches": []}

import pytest
from flutes.iterator import split_by

def test_split_by_with_separator():
    iterable = [1, 2, 3, 0, 4, 5, 0, 6]
    separator = 0
    result = list(split_by(iterable, separator=separator))
    assert result == [[1, 2, 3], [4, 5], [6]]

def test_split_by_with_empty_segments():
    iterable = [1, 0, 2, 0, 3, 0, 0, 4]
    separator = 0
    result = list(split_by(iterable, empty_segments=True, separator=separator))
    assert result == [[1], [2], [3], [], [4]]
