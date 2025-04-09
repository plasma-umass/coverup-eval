# file: flutes/iterator.py:333-338
# asked: {"lines": [333, 334, 335, 336, 337, 338], "branches": [[334, 335], [334, 336]]}
# gained: {"lines": [333, 334, 335, 336, 337, 338], "branches": [[334, 335], [334, 336]]}

import pytest
from flutes.iterator import Range

def test_range_next():
    # Test case where the range is exhausted
    r = Range(1, 3)
    assert next(r) == 1
    assert next(r) == 2
    with pytest.raises(StopIteration):
        next(r)

    # Test case with step
    r = Range(1, 5, 2)
    assert next(r) == 1
    assert next(r) == 3
    with pytest.raises(StopIteration):
        next(r)

    # Test case with single argument
    r = Range(3)
    assert next(r) == 0
    assert next(r) == 1
    assert next(r) == 2
    with pytest.raises(StopIteration):
        next(r)
