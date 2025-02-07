# file: pymonet/box.py:48-57
# asked: {"lines": [48, 57], "branches": []}
# gained: {"lines": [48, 57], "branches": []}

import pytest
from pymonet.box import Box

def test_box_ap():
    # Create a Box containing a function
    box_function = Box(lambda x: x * 2)
    
    # Create a Box containing a value
    box_value = Box(5)
    
    # Apply the function inside box_function to the value inside box_value
    result = box_function.ap(box_value)
    
    # Assert the result is as expected
    assert result == Box(10)
