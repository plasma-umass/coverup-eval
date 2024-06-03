# file src/blib2to3/pytree.py:161-168
# lines [161, 163, 164, 165, 166, 167, 168]
# branches ['164->165', '164->168', '165->166', '165->167']

import pytest
from blib2to3.pytree import Base, Leaf

class MockLeaf(Leaf):
    def __init__(self, lineno):
        self.lineno = lineno

class MockNode(Base):
    def __init__(self, children=None):
        self.children = children or []

def test_get_lineno_with_leaf():
    leaf = MockLeaf(lineno=10)
    assert leaf.get_lineno() == 10

def test_get_lineno_with_nested_nodes():
    leaf = MockLeaf(lineno=20)
    node = MockNode(children=[leaf])
    assert node.get_lineno() == 20

def test_get_lineno_with_empty_node():
    node = MockNode(children=[])
    assert node.get_lineno() is None

def test_get_lineno_with_deeply_nested_nodes():
    leaf = MockLeaf(lineno=30)
    inner_node = MockNode(children=[leaf])
    outer_node = MockNode(children=[inner_node])
    assert outer_node.get_lineno() == 30
