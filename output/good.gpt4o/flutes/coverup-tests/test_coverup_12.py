# file flutes/iterator.py:47-66
# lines [47, 59, 60, 61, 62, 63, 64, 65, 66]
# branches ['59->60', '59->61', '63->exit', '63->64']

import pytest
from flutes.iterator import take

def test_take():
    # Test taking elements from a range
    result = list(take(5, range(1000000)))
    assert result == [0, 1, 2, 3, 4]

    # Test taking more elements than available in the iterable
    result = list(take(5, range(3)))
    assert result == [0, 1, 2]

    # Test taking zero elements
    result = list(take(0, range(1000000)))
    assert result == []

    # Test taking elements from an empty iterable
    result = list(take(5, []))
    assert result == []

    # Test negative n value
    with pytest.raises(ValueError, match="`n` should be non-negative"):
        list(take(-1, range(1000000)))

    # Test taking elements from a non-range iterable
    result = list(take(3, iter([10, 20, 30, 40, 50])))
    assert result == [10, 20, 30]
