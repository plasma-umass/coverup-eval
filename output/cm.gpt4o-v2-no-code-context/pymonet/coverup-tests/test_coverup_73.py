# file: pymonet/box.py:37-46
# asked: {"lines": [37, 46], "branches": []}
# gained: {"lines": [37, 46], "branches": []}

import pytest
from pymonet.box import Box

def test_box_bind():
    # Create a Box instance with an initial value
    box = Box(5)
    
    # Define a mapper function
    def mapper(x):
        return x * 2
    
    # Use the bind method and assert the result
    result = box.bind(mapper)
    assert result == 10

    # Test with a different mapper function
    def another_mapper(x):
        return x + 3
    
    result = box.bind(another_mapper)
    assert result == 8

    # Test with a more complex mapper function
    def complex_mapper(x):
        return f"Value is {x}"
    
    result = box.bind(complex_mapper)
    assert result == "Value is 5"
