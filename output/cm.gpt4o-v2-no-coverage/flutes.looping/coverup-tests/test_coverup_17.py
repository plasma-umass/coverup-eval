# file: flutes/iterator.py:340-341
# asked: {"lines": [340, 341], "branches": []}
# gained: {"lines": [340, 341], "branches": []}

import pytest
from flutes.iterator import Range

def test_range_len():
    r1 = Range(10)
    assert len(r1) == 10

    r2 = Range(1, 10)
    assert len(r2) == 9

    r3 = Range(1, 10, 2)
    assert len(r3) == 4

    with pytest.raises(ValueError):
        Range()

    with pytest.raises(ValueError):
        Range(1, 2, 3, 4)
