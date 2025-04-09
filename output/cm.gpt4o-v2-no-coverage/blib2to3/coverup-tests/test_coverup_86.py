# file: src/blib2to3/pytree.py:314-318
# asked: {"lines": [316, 317, 318], "branches": [[317, 0], [317, 318]]}
# gained: {"lines": [316, 317, 318], "branches": [[317, 0], [317, 318]]}

import pytest
from blib2to3.pytree import Node

class MockNode(Node):
    def __init__(self, type, children=None):
        if children is None:
            children = []
        super().__init__(type, children)
        self.parent = None

def test_pre_order():
    # Create a tree structure
    child_node1 = MockNode(257)
    child_node2 = MockNode(258)
    parent_node = MockNode(256, [child_node1, child_node2])

    # Collect nodes in pre-order
    result = list(parent_node.pre_order())

    # Verify the order is correct
    assert result == [parent_node, child_node1, child_node2]

    # Verify parent pointers
    assert child_node1.parent == parent_node
    assert child_node2.parent == parent_node

    # Clean up
    child_node1.parent = None
    child_node2.parent = None
