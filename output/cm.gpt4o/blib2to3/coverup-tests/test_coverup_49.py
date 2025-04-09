# file src/blib2to3/pytree.py:314-318
# lines [314, 316, 317, 318]
# branches ['317->exit', '317->318']

import pytest
from blib2to3.pytree import Node, Leaf
from blib2to3.pgen2 import token

def test_node_pre_order():
    # Create nodes with required arguments
    mock_node = Node(type=256, children=[])
    mock_child1 = Node(type=257, children=[])
    mock_child2 = Node(type=258, children=[])
    
    # Set up the children for the mock_node
    mock_node.children = [mock_child1, mock_child2]
    
    # Collect the nodes in pre-order
    pre_order_nodes = list(mock_node.pre_order())
    
    # Assertions to verify the pre-order traversal
    assert pre_order_nodes == [mock_node, mock_child1, mock_child2]

    # Clean up
    del mock_node
    del mock_child1
    del mock_child2
