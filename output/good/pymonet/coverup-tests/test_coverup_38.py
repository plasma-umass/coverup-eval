# file pymonet/box.py:70-79
# lines [70, 77, 79]
# branches []

import pytest
from pymonet.box import Box
from pymonet.either import Right, Left

def test_box_to_either():
    # Create a Box with a value
    box = Box(10)
    
    # Transform Box into Right either
    either_result = box.to_either()
    
    # Check if the result is an instance of Right
    assert isinstance(either_result, Right)
    
    # Check if the value inside Right is the same as the one in the Box
    assert either_result.value == box.value
