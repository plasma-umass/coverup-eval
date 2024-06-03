# file src/blib2to3/pytree.py:295-297
# lines [297]
# branches []

import pytest
from blib2to3.pytree import Node

def test_node_eq():
    class MockNode(Node):
        def __init__(self, type, children):
            self.type = type
            self.children = children

    node1 = MockNode(type=1, children=[MockNode(type=2, children=[])])
    node2 = MockNode(type=1, children=[MockNode(type=2, children=[])])
    node3 = MockNode(type=1, children=[MockNode(type=3, children=[])])

    assert node1._eq(node2) is True
    assert node1._eq(node3) is False
