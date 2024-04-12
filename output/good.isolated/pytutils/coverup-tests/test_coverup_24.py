# file pytutils/trees.py:59-61
# lines [59, 61]
# branches []

import pytest
from pytutils.trees import tree
from collections import defaultdict

def test_tree():
    # Create a tree and assert it's a defaultdict
    t = tree()
    assert isinstance(t, defaultdict)

    # Add some nested items to the tree
    t['root']['child1']['grandchild1'] = 'value1'
    t['root']['child2'] = 'value2'

    # Assert that the items are in the tree
    assert t['root']['child1']['grandchild1'] == 'value1'
    assert t['root']['child2'] == 'value2'

    # Assert that accessing a non-existent item creates a new tree
    assert isinstance(t['root']['child3'], defaultdict)
    assert isinstance(t['root']['child1']['grandchild2'], defaultdict)

    # Clean up after the test
    del t
