# file src/blib2to3/pytree.py:287-293
# lines [293]
# branches []

import pytest
from blib2to3.pytree import Node, Leaf
from blib2to3.pgen2 import token

def test_node_str_with_children():
    # Create a mock for the children
    child1 = Leaf(token.NAME, "child1")
    child2 = Leaf(token.NAME, "child2")
    
    # Create a Node instance with a valid type and children
    node = Node(256, [child1, child2])
    
    # Assert the string representation of the node
    assert str(node) == "child1child2"
