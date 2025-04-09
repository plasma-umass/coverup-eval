# file: pymonet/box.py:37-46
# asked: {"lines": [37, 46], "branches": []}
# gained: {"lines": [37, 46], "branches": []}

import pytest
from pymonet.box import Box

def test_box_bind():
    # Create a Box instance with an initial value
    box = Box(10)
    
    # Define a mapper function
    def mapper(x):
        return x * 2
    
    # Use the bind method
    result = box.bind(mapper)
    
    # Assert the result is as expected
    assert result == 20

    # Clean up
    del box
    del mapper
