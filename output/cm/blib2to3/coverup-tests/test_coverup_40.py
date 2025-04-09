# file src/blib2to3/pytree.py:314-318
# lines [314, 316, 317, 318]
# branches ['317->exit', '317->318']

import pytest
from blib2to3.pytree import Node

class TestNode(Node):
    def __init__(self, children=None):
        self.children = children if children else []

@pytest.fixture
def mock_node(mocker):
    return mocker.Mock(spec=Node)

def test_pre_order():
    # Create a tree structure
    leaf1 = TestNode()
    leaf2 = TestNode()
    child = TestNode(children=[leaf1, leaf2])
    root = TestNode(children=[child])

    # Collect nodes in pre-order
    nodes = list(root.pre_order())

    # Check if the pre-order traversal is correct
    assert nodes == [root, child, leaf1, leaf2]

    # Check if the pre-order traversal includes all children
    assert all(isinstance(node, Node) for node in nodes)
