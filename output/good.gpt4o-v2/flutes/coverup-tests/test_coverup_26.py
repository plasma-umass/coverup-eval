# file: flutes/iterator.py:333-338
# asked: {"lines": [333, 334, 335, 336, 337, 338], "branches": [[334, 335], [334, 336]]}
# gained: {"lines": [333, 334, 335, 336, 337, 338], "branches": [[334, 335], [334, 336]]}

import pytest
from flutes.iterator import Range

def test_range_next_within_bounds():
    r = Range(1, 5)
    assert next(r) == 1
    assert next(r) == 2
    assert next(r) == 3
    assert next(r) == 4

def test_range_next_out_of_bounds():
    r = Range(1, 2)
    next(r)  # This should be 1
    with pytest.raises(StopIteration):
        next(r)

def test_range_next_with_step():
    r = Range(1, 10, 3)
    assert next(r) == 1
    assert next(r) == 4
    assert next(r) == 7
    with pytest.raises(StopIteration):
        next(r)
