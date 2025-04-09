# file: src/blib2to3/pytree.py:465-470
# asked: {"lines": [465, 466, 470], "branches": []}
# gained: {"lines": [465, 466, 470], "branches": []}

import pytest
from blib2to3.pytree import Leaf

def test_leaf_prefix_property():
    # Create a Leaf instance with a specific prefix
    leaf = Leaf(type=1, value='value', prefix='test_prefix')
    
    # Assert that the prefix property returns the correct value
    assert leaf.prefix == 'test_prefix'
    
    # Change the prefix and assert the change is reflected
    leaf.prefix = 'new_prefix'
    assert leaf.prefix == 'new_prefix'
