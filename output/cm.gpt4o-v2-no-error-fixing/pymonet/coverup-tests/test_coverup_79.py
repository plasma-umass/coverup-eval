# file: pymonet/box.py:48-57
# asked: {"lines": [48, 57], "branches": []}
# gained: {"lines": [48, 57], "branches": []}

import pytest
from pymonet.box import Box

def test_box_ap():
    # Create a Box containing a function
    box_with_function = Box(lambda x: x + 1)
    
    # Create a Box containing a value
    box_with_value = Box(1)
    
    # Apply the function inside box_with_function to the value inside box_with_value
    result = box_with_function.ap(box_with_value)
    
    # Verify the result is as expected
    assert result == Box(2)
