# file: src/blib2to3/pytree.py:329-332
# asked: {"lines": [329, 330, 331, 332], "branches": [[331, 0], [331, 332]]}
# gained: {"lines": [329, 330, 331, 332], "branches": [[331, 332]]}

import pytest
from blib2to3.pytree import Node, Base

class MockChild:
    def __init__(self):
        self.prefix = None
        self.parent = None

def test_node_prefix_setter():
    # Create a mock child and a Node instance
    child = MockChild()
    node = Node(type=256, children=[child])

    # Set the prefix and check if it propagates to the child
    node.prefix = "test_prefix"
    assert child.prefix == "test_prefix"

    # Clean up
    node.children = []
    del node
    del child
