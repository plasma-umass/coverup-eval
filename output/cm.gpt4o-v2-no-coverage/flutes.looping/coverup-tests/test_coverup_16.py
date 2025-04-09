# file: flutes/iterator.py:333-338
# asked: {"lines": [333, 334, 335, 336, 337, 338], "branches": [[334, 335], [334, 336]]}
# gained: {"lines": [333, 334, 335, 336, 337, 338], "branches": [[334, 335], [334, 336]]}

import pytest
from flutes.iterator import Range

def test_range_next():
    r = Range(1, 5)
    assert next(r) == 1
    assert next(r) == 2
    assert next(r) == 3
    assert next(r) == 4
    with pytest.raises(StopIteration):
        next(r)

def test_range_init():
    r1 = Range(5)
    assert r1.l == 0
    assert r1.r == 5
    assert r1.step == 1

    r2 = Range(1, 5)
    assert r2.l == 1
    assert r2.r == 5
    assert r2.step == 1

    r3 = Range(1, 5, 2)
    assert r3.l == 1
    assert r3.r == 5
    assert r3.step == 2

    with pytest.raises(ValueError):
        Range()
    with pytest.raises(ValueError):
        Range(1, 2, 3, 4)
