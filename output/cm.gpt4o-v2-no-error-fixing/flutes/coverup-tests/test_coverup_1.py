# file: flutes/iterator.py:340-341
# asked: {"lines": [340, 341], "branches": []}
# gained: {"lines": [340, 341], "branches": []}

import pytest
from flutes.iterator import Range

def test_range_len():
    r = Range(1, 10, 2)
    assert len(r) == 4

    r = Range(10)
    assert len(r) == 10

    r = Range(1, 10)
    assert len(r) == 9

    r = Range(1, 11, 2)
    assert len(r) == 5
