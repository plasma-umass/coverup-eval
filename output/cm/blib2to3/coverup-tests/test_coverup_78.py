# file src/blib2to3/pytree.py:295-297
# lines [295, 297]
# branches []

import pytest
from blib2to3.pytree import Node, Leaf

@pytest.fixture
def cleanup_nodes():
    # Fixture to clean up any created nodes after the test
    created_nodes = []

    yield created_nodes

    # Cleanup code
    for node in created_nodes:
        del node

def test_node_eq(cleanup_nodes):
    # Create two nodes with the same type and children
    # Use a type constant >= 256 for Node as per the assertion in the Node class
    node1 = Node(type=256, children=[Leaf(type=2, value=''), Leaf(type=3, value='')])  # Use Leaf for children
    node2 = Node(type=256, children=[Leaf(type=2, value=''), Leaf(type=3, value='')])  # Use Leaf for children
    cleanup_nodes.extend([node1, node2])

    # Create a third node with different type
    node3 = Node(type=257, children=[Leaf(type=2, value=''), Leaf(type=3, value='')])  # Use Leaf for children
    cleanup_nodes.append(node3)

    # Create a fourth node with different children
    node4 = Node(type=256, children=[Leaf(type=5, value='')])  # Use Leaf for children
    cleanup_nodes.append(node4)

    # Assert that node1 is equal to node2
    assert node1._eq(node2)

    # Assert that node1 is not equal to node3 (different type)
    assert not node1._eq(node3)

    # Assert that node1 is not equal to node4 (different children)
    assert not node1._eq(node4)
