# file: src/blib2to3/pytree.py:465-470
# asked: {"lines": [465, 466, 470], "branches": []}
# gained: {"lines": [465, 466, 470], "branches": []}

import pytest
from blib2to3.pytree import Leaf

def test_leaf_prefix():
    # Create a Leaf instance with a specific prefix
    leaf = Leaf(type=1, value='value', prefix=' ')
    
    # Assert that the prefix property returns the correct value
    assert leaf.prefix == ' '
    
    # Change the prefix and assert the change
    leaf.prefix = '\t'
    assert leaf.prefix == '\t'
