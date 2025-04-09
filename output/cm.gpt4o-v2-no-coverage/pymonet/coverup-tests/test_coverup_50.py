# file: pymonet/box.py:70-79
# asked: {"lines": [70, 77, 79], "branches": []}
# gained: {"lines": [70, 77, 79], "branches": []}

import pytest
from pymonet.box import Box
from pymonet.either import Right

def test_box_to_either():
    # Create a Box with a value
    box = Box(42)
    
    # Transform Box to Right either
    either = box.to_either()
    
    # Assert that the result is an instance of Right
    assert isinstance(either, Right)
    
    # Assert that the value inside Right is the same as the original Box value
    assert either.value == 42
