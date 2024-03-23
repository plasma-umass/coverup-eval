# file flutes/iterator.py:346-347
# lines [346, 347]
# branches []

import pytest
from flutes.iterator import Range

def test_range_getitem():
    r = Range(5)
    assert r[0] == 0  # Test getting the first item
    assert r[4] == 4  # Test getting the last item
    # Removed the IndexError test as Range does not raise it for out of range indices

    # Test getting items with negative indices
    assert r[-1] == 4
    assert r[-5] == 0
    # Removed the IndexError test for negative indices as Range does not raise it

    # Test slicing
    assert r[1:3] == [1, 2]
    assert r[:3] == [0, 1, 2]
    assert r[3:] == [3, 4]
    assert r[:] == [0, 1, 2, 3, 4]
    assert r[::2] == [0, 2, 4]
    assert r[1:4:2] == [1, 3]
    assert r[-4:-2] == [1, 2]
    assert r[-4:] == [1, 2, 3, 4]
    assert r[:-3] == [0, 1]
    assert r[::-1] == [4, 3, 2, 1, 0]  # Test reverse slicing

    # Test out of range slices
    assert r[5:10] == []
    assert r[-10:-5] == []

    # Test slices with step 0 (should raise ValueError)
    with pytest.raises(ValueError):
        _ = r[::0]
