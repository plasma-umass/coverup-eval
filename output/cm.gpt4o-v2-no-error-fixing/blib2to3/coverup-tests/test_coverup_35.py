# file: src/blib2to3/pytree.py:355-363
# asked: {"lines": [355, 360, 361, 362, 363], "branches": []}
# gained: {"lines": [355, 360, 361, 362, 363], "branches": []}

import pytest
from blib2to3.pytree import Node

class MockChild:
    def __init__(self):
        self.parent = None

def test_append_child():
    # Create a Node instance with mock children
    node = Node(type=256, children=[])
    
    # Create a mock child
    child = MockChild()
    
    # Append the child to the node
    node.append_child(child)
    
    # Assertions to verify the postconditions
    assert child.parent == node
    assert child in node.children

    # Clean up
    node.children.remove(child)
    child.parent = None
