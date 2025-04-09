# file: pytutils/trees.py:59-61
# asked: {"lines": [59, 61], "branches": []}
# gained: {"lines": [59, 61], "branches": []}

import collections
from pytutils.trees import tree

def test_tree():
    # Create a tree
    t = tree()
    
    # Access a non-existent key to trigger the defaultdict behavior
    t['new_branch']
    
    # Assert that the new branch is indeed a tree (defaultdict)
    assert isinstance(t['new_branch'], collections.defaultdict)
    assert t['new_branch'].default_factory == tree

    # Clean up by clearing the tree
    t.clear()
