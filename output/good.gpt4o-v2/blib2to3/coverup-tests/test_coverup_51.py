# file: src/blib2to3/pytree.py:287-293
# asked: {"lines": [287, 293], "branches": []}
# gained: {"lines": [287, 293], "branches": []}

import pytest
from blib2to3.pytree import Node

class MockChild:
    def __init__(self, value):
        self.value = value
        self.parent = None

    def __str__(self):
        return self.value

def test_node_str():
    # Create mock children
    child1 = MockChild("child1")
    child2 = MockChild("child2")
    
    # Create a Node with these children
    node = Node(type=256, children=[child1, child2])
    
    # Verify the __str__ method
    assert str(node) == "child1child2"
    
    # Clean up
    del node
    del child1
    del child2
