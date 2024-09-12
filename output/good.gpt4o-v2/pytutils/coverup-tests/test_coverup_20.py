# file: pytutils/trees.py:59-61
# asked: {"lines": [59, 61], "branches": []}
# gained: {"lines": [59, 61], "branches": []}

import pytest
import collections
from pytutils.trees import tree

def test_tree_function():
    # Create a tree
    t = tree()
    
    # Check if the tree is an instance of defaultdict
    assert isinstance(t, collections.defaultdict)
    
    # Check if the default factory is the tree function itself
    assert t.default_factory == tree
    
    # Add a nested key to the tree
    t['a']['b'] = 'value'
    
    # Verify the nested structure
    assert t['a']['b'] == 'value'
    assert isinstance(t['a'], collections.defaultdict)
    assert isinstance(t['a']['b'], str)

    # Clean up
    t.clear()

