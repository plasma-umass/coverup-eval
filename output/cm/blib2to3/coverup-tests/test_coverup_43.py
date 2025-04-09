# file src/blib2to3/pytree.py:334-343
# lines [334, 339, 340, 341, 342, 343]
# branches []

import pytest
from blib2to3.pytree import Node, Leaf

@pytest.fixture
def mock_node(mocker):
    # Node type should be >= 256 according to the assertion in the Node class
    node = Node(type=256, children=[Leaf(type=2, value='leaf1'), Leaf(type=3, value='leaf2')])
    mocker.spy(node, 'changed')
    mocker.spy(node, 'invalidate_sibling_maps')
    return node

def test_set_child(mock_node):
    new_child = Leaf(type=4, value='new_leaf')
    old_child = mock_node.children[1]

    assert old_child.parent is mock_node
    mock_node.set_child(1, new_child)
    assert mock_node.children[1] is new_child
    assert new_child.parent is mock_node
    assert old_child.parent is None
    mock_node.changed.assert_called_once()
    mock_node.invalidate_sibling_maps.assert_called_once()
