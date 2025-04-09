# file src/blib2to3/pytree.py:220-222
# lines [220, 221, 222]
# branches ['221->exit', '221->222']

import pytest
from blib2to3.pytree import Base, Leaf

class LeafChild(Leaf):
    def __init__(self, value):
        self.value = value

    def leaves(self):
        yield self

class NonLeafChild(Base):
    def __init__(self, children):
        self.children = children

@pytest.fixture
def leaf_children():
    return [LeafChild("leaf1"), LeafChild("leaf2")]

@pytest.fixture
def non_leaf_child(leaf_children):
    return NonLeafChild(leaf_children)

def test_base_leaves(non_leaf_child):
    leaves = list(non_leaf_child.leaves())
    assert len(leaves) == 2
    assert all(isinstance(leaf, LeafChild) for leaf in leaves)
    assert leaves[0].value == "leaf1"
    assert leaves[1].value == "leaf2"
