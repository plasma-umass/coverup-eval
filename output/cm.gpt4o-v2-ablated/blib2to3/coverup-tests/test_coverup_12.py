# file: src/blib2to3/pytree.py:314-318
# asked: {"lines": [314, 316, 317, 318], "branches": [[317, 0], [317, 318]]}
# gained: {"lines": [314, 316, 317, 318], "branches": [[317, 0], [317, 318]]}

import pytest
from blib2to3.pytree import Node

class MockNode(Node):
    def __init__(self, children=None):
        self.children = children if children is not None else []

def test_pre_order_single_node():
    node = MockNode()
    result = list(node.pre_order())
    assert result == [node]

def test_pre_order_with_children():
    child1 = MockNode()
    child2 = MockNode()
    node = MockNode(children=[child1, child2])
    result = list(node.pre_order())
    assert result == [node, child1, child2]

def test_pre_order_with_nested_children():
    grandchild = MockNode()
    child = MockNode(children=[grandchild])
    node = MockNode(children=[child])
    result = list(node.pre_order())
    assert result == [node, child, grandchild]
