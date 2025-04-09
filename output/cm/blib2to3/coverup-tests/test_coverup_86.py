# file src/blib2to3/pytree.py:345-353
# lines [350, 351, 352, 353]
# branches []

import pytest
from blib2to3.pytree import Node

@pytest.fixture
def mock_node(mocker):
    node = Node(type=256, children=[])
    mocker.patch.object(node, 'changed')
    mocker.patch.object(node, 'invalidate_sibling_maps')
    return node

def test_insert_child(mock_node):
    child_node = Node(type=256, children=[])
    index_to_insert = 0

    mock_node.insert_child(index_to_insert, child_node)

    assert child_node.parent is mock_node
    assert mock_node.children[index_to_insert] is child_node
    mock_node.changed.assert_called_once()
    mock_node.invalidate_sibling_maps.assert_called_once()
