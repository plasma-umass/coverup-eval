# file src/blib2to3/pytree.py:432-438
# lines [438]
# branches []

import pytest
from blib2to3.pytree import Leaf

def test_leaf_str():
    # Create a mock object for the value
    mock_value = "mock_value"
    mock_prefix = "mock_prefix"
    
    # Create an instance of Leaf with the required arguments
    leaf = Leaf(type=0, value=mock_value)
    leaf.prefix = mock_prefix
    
    # Call the __str__ method and assert the result
    result = str(leaf)
    assert result == mock_prefix + mock_value
