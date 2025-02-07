# file: pymonet/either.py:48-57
# asked: {"lines": [48, 55, 57], "branches": []}
# gained: {"lines": [48, 55, 57], "branches": []}

import pytest
from pymonet.either import Either
from pymonet.box import Box

def test_either_to_box():
    # Create an instance of Either with a sample value
    either_instance = Either("test_value")
    
    # Convert Either to Box
    box_instance = either_instance.to_box()
    
    # Assert that the returned instance is of type Box
    assert isinstance(box_instance, Box)
    
    # Assert that the value inside the Box is the same as the value inside the Either
    assert box_instance.value == "test_value"
