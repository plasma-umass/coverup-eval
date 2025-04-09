# file src/blib2to3/pytree.py:432-438
# lines [432, 438]
# branches []

import pytest
from blib2to3.pytree import Leaf

def test_leaf_str():
    # Create a Leaf instance with a prefix and a value
    prefix = " "
    value = "test_value"
    leaf = Leaf(type=0, value=value, context=("", (1, 0)), prefix=prefix)

    # Convert the Leaf instance to a string
    leaf_str = str(leaf)

    # Check that the string representation matches the expected format
    assert leaf_str == prefix + str(value), "Leaf string representation is incorrect"
