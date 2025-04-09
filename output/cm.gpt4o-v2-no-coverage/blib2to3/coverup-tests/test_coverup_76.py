# file: src/blib2to3/pytree.py:334-343
# asked: {"lines": [339, 340, 341, 342, 343], "branches": []}
# gained: {"lines": [339, 340, 341, 342, 343], "branches": []}

import pytest
from blib2to3.pytree import Node, Base

class MockChild(Base):
    def __init__(self):
        self.parent = None

    def changed(self):
        pass

    def invalidate_sibling_maps(self):
        pass

@pytest.fixture
def node():
    child1 = MockChild()
    child2 = MockChild()
    return Node(type=256, children=[child1, child2])

def test_set_child(node):
    new_child = MockChild()
    node.set_child(1, new_child)
    
    assert node.children[1] is new_child
    assert new_child.parent is node
    assert node.children[0].parent is node
    assert node.children[1].parent is node
    assert node.children[0].parent is not None
    assert node.children[1].parent is not None
