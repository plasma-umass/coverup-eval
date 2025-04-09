# file: src/blib2to3/pytree.py:454-455
# asked: {"lines": [454, 455], "branches": []}
# gained: {"lines": [454, 455], "branches": []}

import pytest
from blib2to3.pytree import Leaf

def test_leaf_leaves():
    leaf = Leaf(type=1, value='test')
    leaves = list(leaf.leaves())
    assert len(leaves) == 1
    assert leaves[0] is leaf
