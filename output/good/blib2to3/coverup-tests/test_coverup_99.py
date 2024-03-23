# file src/blib2to3/pytree.py:177-190
# lines []
# branches ['183->190']

import pytest
from blib2to3.pytree import Base

class Node(Base):
    def __init__(self):
        self.parent = None
        self.children = []
        self._changed = False
        self._invalidate_sibling_maps_called = False

    def changed(self):
        self._changed = True

    def invalidate_sibling_maps(self):
        self._invalidate_sibling_maps_called = True

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

def test_remove_node_without_parent():
    node = Node()
    assert node.remove() is None

def test_remove_node_with_parent(setup_tree):
    parent, child1, child2, child3 = setup_tree
    index = child2.remove()
    assert index == 1
    assert child2 not in parent.children
    assert child2.parent is None
    assert parent._changed
    assert parent._invalidate_sibling_maps_called

def test_remove_node_not_in_parent_children(setup_tree):
    parent, child1, child2, child3 = setup_tree
    parent.children = [child1, child3]  # Remove child2 from the list
    assert child2.remove() is None
    assert child2.parent is parent  # child2 still has its parent because it wasn't found in the parent's children
