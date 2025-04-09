# file: src/blib2to3/pytree.py:287-293
# asked: {"lines": [287, 293], "branches": []}
# gained: {"lines": [287, 293], "branches": []}

import pytest
from blib2to3.pytree import Node, Leaf
from blib2to3.pgen2 import token

def test_node_str():
    # Create a mock child node
    child1 = Leaf(token.NAME, "child1")
    child2 = Leaf(token.NAME, "child2")
    
    # Create a Node with children
    node = Node(256, [child1, child2])
    
    # Verify the __str__ method
    assert str(node) == "child1child2"
