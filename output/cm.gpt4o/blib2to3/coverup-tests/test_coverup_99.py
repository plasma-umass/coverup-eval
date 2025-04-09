# file src/blib2to3/pytree.py:334-343
# lines [339, 340, 341, 342, 343]
# branches []

import pytest
from blib2to3.pytree import Node, Leaf

class MockNode:
    def __init__(self):
        self.parent = None

@pytest.fixture
def node_with_children(mocker):
    node = Node(type=256, children=[])
    child1 = MockNode()
    child2 = MockNode()
    node.children = [child1, child2]
    mocker.patch.object(node, 'changed')
    mocker.patch.object(node, 'invalidate_sibling_maps')
    return node, child1, child2

def test_set_child(node_with_children):
    node, child1, child2 = node_with_children
    new_child = MockNode()
    
    node.set_child(1, new_child)
    
    assert new_child.parent == node
    assert child2.parent is None
    assert node.children[1] == new_child
    node.changed.assert_called_once()
    node.invalidate_sibling_maps.assert_called_once()
