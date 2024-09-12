# file: src/blib2to3/pytree.py:299-306
# asked: {"lines": [299, 300, 301, 302, 303, 304, 305], "branches": []}
# gained: {"lines": [299, 300, 301, 302, 303, 304, 305], "branches": []}

import pytest
from blib2to3.pytree import Node

def test_node_clone():
    # Create a mock child node
    child_node = Node(type=256, children=[])
    
    # Create a Node instance with a child
    node = Node(type=256, children=[child_node], fixers_applied=['fixer1'])
    
    # Clone the node
    cloned_node = node.clone()
    
    # Assertions to verify the clone
    assert cloned_node.type == node.type
    assert cloned_node.fixers_applied == node.fixers_applied
    assert len(cloned_node.children) == len(node.children)
    assert cloned_node.children[0].type == node.children[0].type
    assert cloned_node.children[0] is not node.children[0]  # Ensure it's a deep copy

    # Clean up
    del child_node
    del node
    del cloned_node
