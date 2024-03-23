# file src/blib2to3/pytree.py:177-190
# lines [177, 182, 183, 184, 185, 186, 187, 188, 189, 190]
# branches ['182->183', '182->190', '183->184', '183->190', '184->183', '184->185']

import pytest
from blib2to3.pytree import Base

class Node(Base):
    def __init__(self):
        self.parent = None
        self.children = []

    def changed(self):
        pass

    def invalidate_sibling_maps(self):
        pass

    def __eq__(self, other):
        return self is other

@pytest.fixture
def setup_tree():
    parent = Node()
    child1 = Node()
    child2 = Node()
    child3 = Node()
    parent.children = [child1, child2, child3]
    child1.parent = parent
    child2.parent = parent
    child3.parent = parent
    return parent, child1, child2, child3

def test_remove_node(setup_tree):
    parent, child1, child2, child3 = setup_tree

    # Remove child2 and check if it is removed from parent's children
    removed_index = child2.remove()
    assert removed_index == 1
    assert child2 not in parent.children
    assert child2.parent is None

    # Check the positions of the remaining children
    assert parent.children == [child1, child3]

    # Remove child1 and check if it is removed from parent's children
    removed_index = child1.remove()
    assert removed_index == 0
    assert child1 not in parent.children
    assert child1.parent is None

    # Check the positions of the remaining children
    assert parent.children == [child3]

    # Remove child3 and check if it is removed from parent's children
    removed_index = child3.remove()
    assert removed_index == 0
    assert child3 not in parent.children
    assert child3.parent is None

    # Check that there are no remaining children
    assert parent.children == []

    # Try to remove a node without a parent
    orphan = Node()
    removed_index = orphan.remove()
    assert removed_index is None
