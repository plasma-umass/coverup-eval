# file: src/blib2to3/pytree.py:334-343
# asked: {"lines": [334, 339, 340, 341, 342, 343], "branches": []}
# gained: {"lines": [334, 339, 340, 341, 342, 343], "branches": []}

import pytest
from blib2to3.pytree import Node

class MockChild:
    def __init__(self):
        self.parent = None

@pytest.fixture
def node_with_children():
    child1 = MockChild()
    child2 = MockChild()
    node = Node(type=256, children=[child1, child2])
    return node, child1, child2

def test_set_child(node_with_children):
    node, child1, child2 = node_with_children
    new_child = MockChild()
    
    node.set_child(1, new_child)
    
    assert node.children[1] is new_child
    assert new_child.parent is node
    assert child2.parent is None

    # Clean up
    node.children[1] = child2
    child2.parent = node
    new_child.parent = None

