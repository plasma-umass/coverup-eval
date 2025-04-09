# file flutes/iterator.py:333-338
# lines [333, 334, 335, 336, 337, 338]
# branches ['334->335', '334->336']

import pytest
from flutes.iterator import Range

def test_range_next():
    # Create a Range object with start=0, end=5, step=1
    r = Range(0, 5, 1)

    # Test __next__ method
    assert next(r) == 0
    assert next(r) == 1
    assert next(r) == 2
    assert next(r) == 3
    assert next(r) == 4

    # Test that StopIteration is raised after the end is reached
    with pytest.raises(StopIteration):
        next(r)

    # Test that the Range object is now exhausted
    with pytest.raises(StopIteration):
        next(r)
