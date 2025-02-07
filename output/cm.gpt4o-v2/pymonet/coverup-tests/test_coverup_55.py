# file: pymonet/box.py:70-79
# asked: {"lines": [70, 77, 79], "branches": []}
# gained: {"lines": [70, 77, 79], "branches": []}

import pytest
from pymonet.box import Box
from pymonet.either import Right

def test_box_to_either():
    # Create a Box instance with a test value
    box = Box(42)
    
    # Convert the Box to an Either
    either = box.to_either()
    
    # Assert that the result is a Right instance
    assert isinstance(either, Right)
    
    # Assert that the value inside the Right is the same as the Box value
    assert either.value == 42
