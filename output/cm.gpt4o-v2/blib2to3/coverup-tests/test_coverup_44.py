# file: src/blib2to3/pytree.py:278-285
# asked: {"lines": [278, 280, 281, 282, 283, 284], "branches": []}
# gained: {"lines": [278, 280, 281, 282, 283, 284], "branches": []}

import pytest
from blib2to3.pytree import Node
from blib2to3.pytree import type_repr

class MockType:
    def __init__(self, value):
        self.value = value

def test_node_repr(monkeypatch):
    # Create a mock type and children for the Node
    mock_type = 256
    mock_children = []

    # Mock the type_repr function to avoid import error
    def mock_type_repr(type_num):
        return f"MockType({type_num})"
    
    monkeypatch.setattr("blib2to3.pytree.type_repr", mock_type_repr)

    # Create a Node instance
    node = Node(type=mock_type, children=mock_children)

    # Check the __repr__ output
    repr_output = repr(node)
    assert repr_output == "Node(MockType(256), [])"

    # Clean up
    del node
