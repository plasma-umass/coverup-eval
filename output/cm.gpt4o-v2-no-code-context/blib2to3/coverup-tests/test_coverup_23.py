# file: src/blib2to3/pytree.py:177-190
# asked: {"lines": [177, 182, 183, 184, 185, 186, 187, 188, 189, 190], "branches": [[182, 183], [182, 190], [183, 184], [183, 190], [184, 183], [184, 185]]}
# gained: {"lines": [177, 182, 183, 184, 185, 186, 187, 188, 189, 190], "branches": [[182, 183], [182, 190], [183, 184], [184, 185]]}

import pytest
from blib2to3.pytree import Node, Leaf

class MockParent(Node):
    def __init__(self):
        super().__init__(type=256, children=[])
        self.changed_called = False
        self.invalidate_sibling_maps_called = False

    def changed(self):
        self.changed_called = True

    def invalidate_sibling_maps(self):
        self.invalidate_sibling_maps_called = True

@pytest.fixture
def node_with_parent():
    parent = MockParent()
    node = Leaf(type=1, value='test')
    node.parent = parent
    parent.children.append(node)
    return node, parent

def test_remove_node_with_parent(node_with_parent):
    node, parent = node_with_parent
    position = node.remove()
    
    assert position == 0
    assert node.parent is None
    assert len(parent.children) == 0
    assert parent.changed_called
    assert parent.invalidate_sibling_maps_called

def test_remove_node_without_parent():
    node = Leaf(type=1, value='test')
    position = node.remove()
    
    assert position is None
