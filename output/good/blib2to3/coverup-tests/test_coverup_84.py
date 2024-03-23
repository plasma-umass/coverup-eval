# file src/blib2to3/pytree.py:329-332
# lines [331, 332]
# branches ['331->exit', '331->332']

import pytest
from blib2to3.pytree import Node, Leaf

@pytest.fixture
def mock_node(mocker):
    # Create a mock node with children
    node = Node(type=256, children=[])
    child = mocker.Mock(spec=Leaf)
    node.children.append(child)
    return node, child

def test_node_prefix_setter_with_children(mock_node):
    node, child = mock_node
    # Set the prefix, which should trigger the setter and set the child's prefix
    node.prefix = "new_prefix"
    # Assert that the child's prefix was set
    assert child.prefix == "new_prefix"
