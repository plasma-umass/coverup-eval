# file: src/blib2to3/pytree.py:308-312
# asked: {"lines": [308, 310, 311, 312], "branches": [[310, 311], [310, 312]]}
# gained: {"lines": [308, 310, 311, 312], "branches": [[310, 311], [310, 312]]}

import pytest
from blib2to3.pytree import Node

class MockChild(Node):
    def __init__(self, type, children):
        super().__init__(type, children)

    def post_order(self):
        yield "child"

def test_post_order():
    # Create a mock child node
    child_node = MockChild(256, [])
    
    # Create a parent node with the child node
    parent_node = Node(256, [child_node])
    
    # Collect the post_order traversal
    result = list(parent_node.post_order())
    
    # Assert the result is as expected
    assert result == ["child", parent_node]

    # Clean up
    child_node.parent = None
    parent_node.children = []

