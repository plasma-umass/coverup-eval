# file: flutes/iterator.py:352-357
# asked: {"lines": [352, 353, 354, 355, 356, 357], "branches": [[353, 354], [353, 355], [355, 356], [355, 357]]}
# gained: {"lines": [352, 353, 354, 355, 356, 357], "branches": [[353, 354], [353, 355], [355, 356], [355, 357]]}

import pytest
from flutes.iterator import Range

def test_range_getitem_with_slice():
    r = Range(1, 10, 2)
    result = r[1:5]
    assert result == [3, 5, 7]

def test_range_getitem_with_negative_index():
    r = Range(1, 10)
    result = r[-1]
    assert result == 9

def test_range_getitem_with_positive_index():
    r = Range(1, 10)
    result = r[2]
    assert result == 3
