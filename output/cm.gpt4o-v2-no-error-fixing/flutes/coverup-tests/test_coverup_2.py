# file: flutes/iterator.py:330-331
# asked: {"lines": [330, 331], "branches": []}
# gained: {"lines": [330, 331], "branches": []}

import pytest
from flutes.iterator import Range

def test_range_iter():
    # Create a Range object
    r = Range(0, 10, 1)
    
    # Use the iterator
    iter_r = iter(r)
    
    # Collect all items from the iterator
    items = list(iter_r)
    
    # Assert the items are as expected
    assert items == list(range(0, 10, 1))

    # Clean up
    del r
    del iter_r
    del items
