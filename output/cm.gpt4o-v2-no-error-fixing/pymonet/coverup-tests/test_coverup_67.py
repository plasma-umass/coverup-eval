# file: pymonet/box.py:92-101
# asked: {"lines": [92, 99, 101], "branches": []}
# gained: {"lines": [92, 99, 101], "branches": []}

import pytest
from pymonet.box import Box
from pymonet.monad_try import Try

def test_box_to_try():
    # Create a Box instance with a sample value
    box = Box(42)
    
    # Convert the Box to a Try
    result = box.to_try()
    
    # Assert that the result is a Try instance
    assert isinstance(result, Try)
    
    # Assert that the Try instance is successful
    assert result.is_success
    
    # Assert that the value inside the Try is the same as the Box value
    assert result.value == 42
