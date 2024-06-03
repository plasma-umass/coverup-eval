# file pytutils/trees.py:59-61
# lines [59, 61]
# branches []

import pytest
import collections
from pytutils.trees import tree

def test_tree():
    # Create a tree
    t = tree()
    
    # Test that the tree is a defaultdict
    assert isinstance(t, collections.defaultdict)
    
    # Test that the tree's default factory is the tree function itself
    assert t.default_factory == tree
    
    # Test adding a nested key
    t['a']['b'] = 1
    assert t['a']['b'] == 1
    
    # Test that accessing a non-existent key creates a new tree
    assert isinstance(t['c'], collections.defaultdict)
    assert t['c'].default_factory == tree
    
    # Clean up by clearing the tree
    t.clear()
    assert len(t) == 0
