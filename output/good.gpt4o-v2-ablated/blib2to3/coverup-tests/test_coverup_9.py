# file: src/blib2to3/pytree.py:308-312
# asked: {"lines": [308, 310, 311, 312], "branches": [[310, 311], [310, 312]]}
# gained: {"lines": [308, 310, 311, 312], "branches": [[310, 311], [310, 312]]}

import pytest
from blib2to3.pytree import Node, Base

class MockNode(Node):
    def __init__(self, children=None):
        self.children = children or []

def test_post_order_no_children():
    node = MockNode()
    result = list(node.post_order())
    assert result == [node]

def test_post_order_with_children():
    child1 = MockNode()
    child2 = MockNode()
    parent = MockNode(children=[child1, child2])
    
    result = list(parent.post_order())
    
    assert result == [child1, child2, parent]

def test_post_order_nested_children():
    grandchild = MockNode()
    child = MockNode(children=[grandchild])
    parent = MockNode(children=[child])
    
    result = list(parent.post_order())
    
    assert result == [grandchild, child, parent]
