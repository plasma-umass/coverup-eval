# file: src/blib2to3/pytree.py:432-438
# asked: {"lines": [432, 438], "branches": []}
# gained: {"lines": [432, 438], "branches": []}

import pytest
from blib2to3.pytree import Leaf

def test_leaf_str():
    # Create a Leaf instance with specific prefix and value
    leaf = Leaf(type=1, value="value", prefix="prefix")
    
    # Verify the __str__ method output
    assert str(leaf) == "prefixvalue"

    # Clean up
    del leaf
