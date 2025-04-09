# file: flutes/iterator.py:307-308
# asked: {"lines": [307, 308], "branches": []}
# gained: {"lines": [307, 308], "branches": []}

import pytest
from flutes.iterator import Range

def test_range_single_argument():
    r = Range(10)
    assert len(r) == 10
    assert r[0] == 0
    assert r[9] == 9

def test_range_cleanup():
    r = Range(10)
    del r

@pytest.mark.parametrize("stop", [5, 10, 15])
def test_range_various_stops(stop):
    r = Range(stop)
    assert len(r) == stop
    assert r[0] == 0
    assert r[-1] == stop - 1
