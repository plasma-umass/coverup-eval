# file flutes/iterator.py:349-350
# lines [349, 350]
# branches []

import pytest
from flutes.iterator import Range

def test_range_getitem_slice():
    r = Range(10)
    slice_result = r[2:5]
    assert slice_result == [2, 3, 4], "The slice of the Range did not return the expected list"

    # Cleanup is not necessary here as we are not modifying any external state or resources.
