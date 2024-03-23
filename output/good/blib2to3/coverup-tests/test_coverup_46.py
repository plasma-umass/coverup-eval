# file src/blib2to3/pytree.py:454-455
# lines [454, 455]
# branches []

import pytest
from blib2to3.pytree import Leaf

def test_leaf_leaves():
    leaf = Leaf(type=0, value="")
    leaves = list(leaf.leaves())
    assert leaves == [leaf], "The leaves method should yield the leaf itself"
