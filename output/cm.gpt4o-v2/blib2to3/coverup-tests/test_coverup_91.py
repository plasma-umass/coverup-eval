# file: src/blib2to3/pytree.py:329-332
# asked: {"lines": [331, 332], "branches": [[331, 0], [331, 332]]}
# gained: {"lines": [331, 332], "branches": [[331, 0], [331, 332]]}

import pytest
from blib2to3.pytree import Node

def test_node_prefix_setter_with_children():
    # Create a mock child node
    class MockChild:
        def __init__(self):
            self.prefix = ""
            self.parent = None

    # Create a Node instance with a child
    child = MockChild()
    node = Node(type=256, children=[child])

    # Set the prefix and check if it propagates to the child
    node.prefix = "test_prefix"
    assert child.prefix == "test_prefix"

def test_node_prefix_setter_without_children():
    # Create a Node instance without children
    node = Node(type=256, children=[])

    # Set the prefix and ensure no errors occur
    node.prefix = "test_prefix"
    assert node.prefix == ""

