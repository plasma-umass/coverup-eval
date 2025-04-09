# file pymonet/box.py:70-79
# lines [70, 77, 79]
# branches []

import pytest
from pymonet.box import Box
from pymonet.either import Right

def test_box_to_either():
    # Create an instance of Box with a sample value
    box = Box(42)
    
    # Transform Box into Right either
    result = box.to_either()
    
    # Assert that the result is an instance of Right
    assert isinstance(result, Right)
    
    # Assert that the value inside Right is the same as the value inside Box
    assert result.value == 42
