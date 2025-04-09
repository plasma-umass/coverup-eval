# file: src/blib2to3/pytree.py:334-343
# asked: {"lines": [339, 340, 341, 342, 343], "branches": []}
# gained: {"lines": [339, 340, 341, 342, 343], "branches": []}

import pytest
from blib2to3.pytree import Node as RealNode

class MockNode(RealNode):
    def __init__(self):
        super().__init__(256, [])
        self.parent = None
        self.children = []
        self.changed_called = False
        self.invalidate_sibling_maps_called = False

    def changed(self):
        self.changed_called = True

    def invalidate_sibling_maps(self):
        self.invalidate_sibling_maps_called = True

@pytest.fixture
def setup_node():
    parent_node = MockNode()
    child_node = MockNode()
    parent_node.children.append(child_node)
    return parent_node, child_node

def test_set_child(setup_node):
    parent_node, child_node = setup_node
    new_child = MockNode()

    parent_node.set_child(0, new_child)

    assert new_child.parent == parent_node
    assert child_node.parent is None
    assert parent_node.children[0] == new_child
    assert parent_node.changed_called
    assert parent_node.invalidate_sibling_maps_called
