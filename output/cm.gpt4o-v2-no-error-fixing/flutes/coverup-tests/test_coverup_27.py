# file: flutes/iterator.py:349-350
# asked: {"lines": [349, 350], "branches": []}
# gained: {"lines": [349, 350], "branches": []}

import pytest
from flutes.iterator import Range

def test_range_getitem_slice():
    r = Range(1, 10, 2)
    result = r[1:4]
    assert result == [3, 5, 7], f"Expected [3, 5, 7], but got {result}"

    r = Range(0, 20, 3)
    result = r[2:5]
    assert result == [6, 9, 12], f"Expected [6, 9, 12], but got {result}"

    r = Range(5)
    result = r[1:3]
    assert result == [1, 2], f"Expected [1, 2], but got {result}"
