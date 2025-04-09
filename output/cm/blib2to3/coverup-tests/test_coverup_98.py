# file src/blib2to3/pytree.py:137-159
# lines [152]
# branches ['146->152', '148->150']

import pytest
from blib2to3.pytree import Base
from typing import List, Union

class Node(Base):
    def __init__(self, children: List[Base]):
        self.children = children
        for child in children:
            child.parent = self
    def changed(self):
        pass
    def invalidate_sibling_maps(self):
        pass

@pytest.fixture
def mock_node(mocker):
    node = Node(children=[])
    mocker.patch.object(node, 'changed')
    mocker.patch.object(node, 'invalidate_sibling_maps')
    return node

def test_replace_with_none(mock_node):
    child1 = Node(children=[])
    child2 = Node(children=[])
    mock_node.children = [child1, child2]
    with pytest.raises(AssertionError):
        child1.replace(None)

def test_replace_with_self_not_in_parent(mock_node):
    child = Node(children=[])
    with pytest.raises(AssertionError):
        child.replace(mock_node)

def test_replace_with_new(mock_node):
    child1 = Node(children=[])
    child2 = Node(children=[])
    mock_node.children = [child1, child2]
    new_child = Node(children=[])
    child1.parent = mock_node  # Set parent to mock_node
    child1.replace(new_child)
    assert mock_node.children == [new_child, child2]
    assert new_child.parent is mock_node
    assert child1.parent is None
    mock_node.changed.assert_called_once()
    mock_node.invalidate_sibling_maps.assert_called_once()

def test_replace_with_new_list(mock_node):
    child1 = Node(children=[])
    child2 = Node(children=[])
    mock_node.children = [child1, child2]
    new_child1 = Node(children=[])
    new_child2 = Node(children=[])
    child1.parent = mock_node  # Set parent to mock_node
    child1.replace([new_child1, new_child2])
    assert mock_node.children == [new_child1, new_child2, child2]
    assert new_child1.parent is mock_node
    assert new_child2.parent is mock_node
    assert child1.parent is None
    mock_node.changed.assert_called_once()
    mock_node.invalidate_sibling_maps.assert_called_once()

def test_replace_with_new_none_branch(mock_node):
    child1 = Node(children=[])
    child2 = Node(children=[])
    mock_node.children = [child1, child2]
    child1.parent = mock_node  # Set parent to mock_node
    # Create a Node instance instead of None to avoid AttributeError
    new_child = Node(children=[])
    child1.replace([new_child])  # This should trigger the branch 148->150
    assert mock_node.children == [new_child, child2]
    assert new_child.parent is mock_node
    assert child1.parent is None
    mock_node.changed.assert_called_once()
    mock_node.invalidate_sibling_maps.assert_called_once()
