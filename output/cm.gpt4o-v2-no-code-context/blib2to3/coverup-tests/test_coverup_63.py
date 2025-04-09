# file: src/blib2to3/pytree.py:432-438
# asked: {"lines": [432, 438], "branches": []}
# gained: {"lines": [432, 438], "branches": []}

import pytest
from blib2to3.pytree import Leaf
from blib2to3.pgen2.token import NAME

def test_leaf_str():
    # Create a Leaf object with type and value
    leaf = Leaf(NAME, "value")
    leaf.prefix = "prefix_"
    
    # Assert that the __str__ method returns the correct string
    assert str(leaf) == "prefix_value"
