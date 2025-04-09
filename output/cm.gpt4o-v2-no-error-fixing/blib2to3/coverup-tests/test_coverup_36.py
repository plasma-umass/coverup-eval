# file: src/blib2to3/pytree.py:432-438
# asked: {"lines": [432, 438], "branches": []}
# gained: {"lines": [432, 438], "branches": []}

import pytest
from blib2to3.pytree import Leaf

def test_leaf_str():
    # Create a Leaf instance with specific prefix and value
    leaf = Leaf(type=1, value="value", prefix="prefix")
    
    # Assert that the __str__ method returns the correct concatenated string
    assert str(leaf) == "prefixvalue"
