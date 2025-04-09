# file flutes/iterator.py:316-328
# lines [316, 317, 318, 319, 320, 321, 322, 324, 325, 326, 327, 328]
# branches ['317->318', '317->319', '319->320', '319->324']

import pytest
from flutes.iterator import Range

def test_range_init():
    # Test with no arguments
    with pytest.raises(ValueError):
        Range()

    # Test with four arguments
    with pytest.raises(ValueError):
        Range(1, 2, 3, 4)

    # Test with one argument
    r = Range(5)
    assert r.l == 0
    assert r.r == 5
    assert r.step == 1
    assert r.val == 0
    assert r.length == 5

    # Test with two arguments
    r = Range(2, 5)
    assert r.l == 2
    assert r.r == 5
    assert r.step == 1
    assert r.val == 2
    assert r.length == 3

    # Test with three arguments
    r = Range(2, 10, 2)
    assert r.l == 2
    assert r.r == 10
    assert r.step == 2
    assert r.val == 2
    assert r.length == 4

    # Test with negative step
    r = Range(10, 2, -2)
    assert r.l == 10
    assert r.r == 2
    assert r.step == -2
    assert r.val == 10
    assert r.length == 4
