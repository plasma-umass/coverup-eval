# file: src/blib2to3/pytree.py:299-306
# asked: {"lines": [299, 300, 301, 302, 303, 304, 305], "branches": []}
# gained: {"lines": [299, 300, 301, 302, 303, 304, 305], "branches": []}

import pytest
from blib2to3.pytree import Node

class MockChild:
    def __init__(self):
        self.parent = None

    def clone(self):
        return MockChild()

def test_node_clone():
    # Arrange
    child1 = MockChild()
    child2 = MockChild()
    node = Node(type=256, children=[child1, child2], fixers_applied=['fixer1'])

    # Act
    cloned_node = node.clone()

    # Assert
    assert cloned_node.type == node.type
    assert cloned_node.fixers_applied == node.fixers_applied
    assert len(cloned_node.children) == len(node.children)
    for cloned_child in cloned_node.children:
        assert isinstance(cloned_child, MockChild)
        assert cloned_child.parent == cloned_node

    # Clean up
    del node
    del cloned_node
    del child1
    del child2
