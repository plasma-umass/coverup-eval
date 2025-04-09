# file: src/blib2to3/pytree.py:299-306
# asked: {"lines": [300, 301, 302, 303, 304, 305], "branches": []}
# gained: {"lines": [300, 301, 302, 303, 304, 305], "branches": []}

import pytest
from blib2to3.pytree import Node

def test_node_clone():
    # Create a mock child node
    class MockChildNode(Node):
        def __init__(self, type, children, fixers_applied=None):
            super().__init__(type, children, fixers_applied=fixers_applied)
        
        def clone(self):
            return MockChildNode(self.type, [ch.clone() for ch in self.children], fixers_applied=self.fixers_applied)

    # Create a node with a type and children
    node = Node(type=256, children=[MockChildNode(type=257, children=[])], fixers_applied=[])
    
    # Clone the node
    cloned_node = node.clone()
    
    # Assertions to verify the clone
    assert cloned_node is not node
    assert cloned_node.type == node.type
    assert cloned_node.fixers_applied == node.fixers_applied
    assert len(cloned_node.children) == len(node.children)
    assert cloned_node.children[0] is not node.children[0]
    assert cloned_node.children[0].type == node.children[0].type

@pytest.fixture(autouse=True)
def cleanup():
    yield
    # Cleanup code if necessary
