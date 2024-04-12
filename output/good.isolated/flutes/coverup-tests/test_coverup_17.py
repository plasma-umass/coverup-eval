# file flutes/iterator.py:343-344
# lines [343, 344]
# branches []

import pytest
from flutes.iterator import Range

def test_range_get_idx():
    # Create a Range instance with specific parameters
    r = Range(0, 10, 2)
    
    # Test _get_idx method with a valid index
    assert r._get_idx(0) == 0
    assert r._get_idx(1) == 2
    assert r._get_idx(4) == 8
    
    # The Range class does not raise IndexError for negative or out-of-bounds indices
    # in the _get_idx method, so we remove the incorrect tests
