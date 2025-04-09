# file: src/blib2to3/pytree.py:308-312
# asked: {"lines": [310, 311, 312], "branches": [[310, 311], [310, 312]]}
# gained: {"lines": [310, 311, 312], "branches": [[310, 311], [310, 312]]}

import pytest
from blib2to3.pytree import Node, Leaf
from blib2to3.pgen2 import token

def test_post_order_single_node():
    node = Node(type=256, children=[])
    result = list(node.post_order())
    assert result == [node]

def test_post_order_multiple_nodes():
    child1 = Node(type=256, children=[])
    child2 = Node(type=256, children=[])
    parent = Node(type=256, children=[child1, child2])
    result = list(parent.post_order())
    assert result == [child1, child2, parent]

def test_post_order_nested_nodes():
    grandchild = Node(type=256, children=[])
    child1 = Node(type=256, children=[grandchild])
    child2 = Node(type=256, children=[])
    parent = Node(type=256, children=[child1, child2])
    result = list(parent.post_order())
    assert result == [grandchild, child1, child2, parent]
