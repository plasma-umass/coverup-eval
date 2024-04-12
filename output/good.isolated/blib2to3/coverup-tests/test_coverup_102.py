# file src/blib2to3/pytree.py:308-312
# lines [310, 311, 312]
# branches ['310->311', '310->312']

import pytest
from blib2to3.pytree import Node

class SimpleNode(Node):
    def __init__(self, children=None):
        self.children = children or []

@pytest.fixture
def simple_tree():
    # Create a simple tree structure with two child nodes
    child1 = SimpleNode()
    child2 = SimpleNode()
    parent = SimpleNode(children=[child1, child2])
    return parent, child1, child2

def test_post_order_with_children(simple_tree):
    parent, child1, child2 = simple_tree
    # Convert the post_order generator to a list to force iteration over all items
    post_order_list = list(parent.post_order())
    
    # Assert that the post_order_list contains the children and the node itself in the correct order
    assert post_order_list == [child1, child2, parent]
