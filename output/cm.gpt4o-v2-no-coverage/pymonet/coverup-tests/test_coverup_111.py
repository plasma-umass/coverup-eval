# file: pymonet/box.py:48-57
# asked: {"lines": [48, 57], "branches": []}
# gained: {"lines": [48, 57], "branches": []}

import pytest
from pymonet.box import Box

def test_box_ap():
    # Create a Box containing a value
    box_value = Box(1)
    
    # Create a Box containing a function
    box_func = Box(lambda x: x + 1)
    
    # Apply the function inside box_func to the value inside box_value
    result = box_func.ap(box_value)
    
    # Assert the result is as expected
    assert result == Box(2)

    # Clean up
    del box_func
    del box_value
    del result
