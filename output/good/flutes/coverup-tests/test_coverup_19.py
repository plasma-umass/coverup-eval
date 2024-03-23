# file flutes/iterator.py:310-311
# lines [310, 311]
# branches []

import pytest
from flutes.iterator import Range

def test_range_init_overload():
    # Test the overload with two arguments
    r = Range(1, 5)
    assert r[0] == 1
    assert r[-1] == 4
    assert len(r) == 4
    assert list(r) == [1, 2, 3, 4]

    # Test the overload with a single argument
    r = Range(5)
    assert r[0] == 0
    assert r[-1] == 4
    assert len(r) == 5
    assert list(r) == [0, 1, 2, 3, 4]
