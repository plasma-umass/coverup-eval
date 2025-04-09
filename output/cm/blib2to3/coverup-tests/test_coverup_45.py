# file src/blib2to3/pytree.py:440-442
# lines [440, 442]
# branches []

import pytest
from blib2to3.pytree import Leaf

@pytest.fixture
def leaf_pair():
    leaf1 = Leaf(1, "leaf")
    leaf2 = Leaf(1, "leaf")
    leaf3 = Leaf(2, "leaf")
    leaf4 = Leaf(1, "not_leaf")
    return leaf1, leaf2, leaf3, leaf4

def test_leaf_equality(leaf_pair):
    leaf1, leaf2, leaf3, leaf4 = leaf_pair
    assert leaf1._eq(leaf2), "Identical leaves should be equal"
    assert not leaf1._eq(leaf3), "Leaves with different types should not be equal"
    assert not leaf1._eq(leaf4), "Leaves with different values should not be equal"
