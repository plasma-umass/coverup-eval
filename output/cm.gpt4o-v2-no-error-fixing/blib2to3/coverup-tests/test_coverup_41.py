# file: src/blib2to3/pytree.py:295-297
# asked: {"lines": [295, 297], "branches": []}
# gained: {"lines": [295, 297], "branches": []}

import pytest
from blib2to3.pytree import Node

def test_node_eq():
    # Create two nodes with the same type and children
    node1 = Node(type=256, children=[])
    node2 = Node(type=256, children=[])
    
    # Test equality
    assert node1._eq(node2) == True
    
    # Create a node with different type
    node3 = Node(type=257, children=[])
    
    # Test inequality due to different type
    assert node1._eq(node3) == False
    
    # Create a node with different children
    child_node = Node(type=256, children=[])
    node4 = Node(type=256, children=[child_node])
    
    # Test inequality due to different children
    assert node1._eq(node4) == False

