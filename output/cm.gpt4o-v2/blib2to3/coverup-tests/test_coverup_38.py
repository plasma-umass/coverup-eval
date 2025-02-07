# file: src/blib2to3/pytree.py:345-353
# asked: {"lines": [345, 350, 351, 352, 353], "branches": []}
# gained: {"lines": [345, 350, 351, 352, 353], "branches": []}

import pytest
from blib2to3.pytree import Node

class MockChild:
    def __init__(self):
        self.parent = None

@pytest.fixture
def node():
    return Node(type=256, children=[])

def test_insert_child(node):
    child = MockChild()
    node.insert_child(0, child)
    
    assert child.parent == node
    assert node.children[0] == child
    # Assuming changed() and invalidate_sibling_maps() have side effects we can check
    # For now, we will just call them to ensure they don't raise exceptions
    node.changed()
    node.invalidate_sibling_maps()

def test_insert_child_with_existing_children(node):
    child1 = MockChild()
    child2 = MockChild()
    node.insert_child(0, child1)
    node.insert_child(1, child2)
    
    assert child1.parent == node
    assert child2.parent == node
    assert node.children[0] == child1
    assert node.children[1] == child2
    # Assuming changed() and invalidate_sibling_maps() have side effects we can check
    # For now, we will just call them to ensure they don't raise exceptions
    node.changed()
    node.invalidate_sibling_maps()
