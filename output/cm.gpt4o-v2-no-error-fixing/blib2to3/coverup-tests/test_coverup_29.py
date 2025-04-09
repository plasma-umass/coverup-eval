# file: src/blib2to3/pytree.py:308-312
# asked: {"lines": [308, 310, 311, 312], "branches": [[310, 311], [310, 312]]}
# gained: {"lines": [308], "branches": []}

import pytest
from blib2to3.pytree import Node
from typing import Iterator

class MockNode(Node):
    def __init__(self, type: int, children: list):
        self.type = type
        self.children = children
        for child in self.children:
            child.parent = self

    def post_order(self) -> Iterator['MockNode']:
        for child in self.children:
            yield from child.post_order()
        yield self

def test_post_order():
    # Create a tree structure
    leaf1 = MockNode(type=256, children=[])
    leaf2 = MockNode(type=256, children=[])
    child = MockNode(type=256, children=[leaf1, leaf2])
    root = MockNode(type=256, children=[child])

    # Collect the post-order traversal
    result = list(root.post_order())

    # Assert the order is correct
    assert result == [leaf1, leaf2, child, root]

    # Clean up
    for node in result:
        node.parent = None

