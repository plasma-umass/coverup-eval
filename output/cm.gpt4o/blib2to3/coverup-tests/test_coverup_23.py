# file src/blib2to3/pytree.py:308-312
# lines [308, 310, 311, 312]
# branches ['310->311', '310->312']

import pytest
from blib2to3.pytree import Node

class MockNode(Node):
    def __init__(self, children=None):
        self.children = children or []

def test_post_order():
    # Create a tree structure
    leaf1 = MockNode()
    leaf2 = MockNode()
    child = MockNode(children=[leaf1, leaf2])
    root = MockNode(children=[child])

    # Collect the post-order traversal
    result = list(root.post_order())

    # Verify the post-order traversal
    assert result == [leaf1, leaf2, child, root]

    # Clean up
    del leaf1, leaf2, child, root, result
