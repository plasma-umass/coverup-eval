# file: src/blib2to3/pytree.py:177-190
# asked: {"lines": [177, 182, 183, 184, 185, 186, 187, 188, 189, 190], "branches": [[182, 183], [182, 190], [183, 184], [183, 190], [184, 183], [184, 185]]}
# gained: {"lines": [177, 182, 183, 184, 185, 186, 187, 188, 189, 190], "branches": [[182, 183], [182, 190], [183, 184], [184, 185]]}

import pytest
from blib2to3.pytree import Base

class Node(Base):
    def __init__(self):
        self.children = []
        self.parent = None

    def changed(self):
        self.was_changed = True

    def invalidate_sibling_maps(self):
        self.was_checked = True

@pytest.fixture
def setup_tree():
    parent = Node()
    child = Node()
    parent.children.append(child)
    child.parent = parent
    return parent, child

def test_remove_node(setup_tree):
    parent, child = setup_tree
    assert child.remove() == 0
    assert child.parent is None
    assert len(parent.children) == 0
    assert parent.was_changed
    assert parent.was_checked

def test_remove_node_without_parent():
    node = Node()
    assert node.remove() is None
