# file src/blib2to3/pytree.py:137-159
# lines [137, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 152, 153, 154, 155, 156, 157, 158, 159]
# branches ['141->142', '141->143', '145->146', '145->153', '146->147', '146->152', '148->149', '148->150', '157->158', '157->159']

import pytest
from blib2to3.pytree import Base
from typing import Union, List

class Node(Base):
    def __init__(self, children=None):
        self.children = children if children else []
        self.parent = None

    def changed(self):
        pass

    def invalidate_sibling_maps(self):
        pass

@pytest.fixture
def mock_node(mocker):
    node = Node()
    node.parent = mocker.Mock(spec=Node)
    node.parent.children = [node]
    return node

def test_replace_node_with_none(mock_node):
    with pytest.raises(AssertionError):
        mock_node.replace(None)

def test_replace_node_not_in_parent_children(mock_node):
    mock_node.parent.children = []
    with pytest.raises(AssertionError):
        mock_node.replace(Node())

def test_replace_node_with_new(mock_node):
    new_node = Node()
    parent_mock = mock_node.parent
    mock_node.replace(new_node)
    assert new_node.parent == parent_mock
    assert parent_mock.children == [new_node]
    assert mock_node.parent is None

def test_replace_node_with_new_list(mock_node):
    new_nodes = [Node(), Node()]
    parent_mock = mock_node.parent
    mock_node.replace(new_nodes)
    assert all(node.parent == parent_mock for node in new_nodes)
    assert parent_mock.children == new_nodes
    assert mock_node.parent is None
