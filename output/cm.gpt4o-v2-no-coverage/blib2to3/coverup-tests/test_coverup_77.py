# file: src/blib2to3/pytree.py:329-332
# asked: {"lines": [], "branches": [[331, 0]]}
# gained: {"lines": [], "branches": [[331, 0]]}

import pytest
from blib2to3.pytree import Node

class MockChild:
    def __init__(self):
        self.prefix = None
        self.parent = None

def test_node_prefix_setter_with_children():
    # Arrange
    child = MockChild()
    node = Node(type=256, children=[child])
    
    # Act
    node.prefix = "test_prefix"
    
    # Assert
    assert child.prefix == "test_prefix"

def test_node_prefix_setter_without_children():
    # Arrange
    node = Node(type=256, children=[])
    
    # Act
    node.prefix = "test_prefix"
    
    # Assert
    assert node.prefix == ""
