# file: src/blib2to3/pytree.py:320-327
# asked: {"lines": [320, 321, 325, 326, 327], "branches": [[325, 326], [325, 327]]}
# gained: {"lines": [320, 321, 325, 326, 327], "branches": [[325, 326], [325, 327]]}

import pytest
from blib2to3.pytree import Node

class MockChild:
    def __init__(self, prefix):
        self.prefix = prefix
        self.parent = None

def test_node_prefix_with_children():
    # Arrange
    child = MockChild(prefix=" ")
    node = Node(type=256, children=[child])

    # Act
    result = node.prefix

    # Assert
    assert result == " "

def test_node_prefix_without_children():
    # Arrange
    node = Node(type=256, children=[])

    # Act
    result = node.prefix

    # Assert
    assert result == ""
