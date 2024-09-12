# file: src/blib2to3/pytree.py:161-168
# asked: {"lines": [161, 163, 164, 165, 166, 167, 168], "branches": [[164, 165], [164, 168], [165, 166], [165, 167]]}
# gained: {"lines": [161, 163, 164, 165, 166, 167, 168], "branches": [[164, 165], [164, 168], [165, 166], [165, 167]]}

import pytest
from blib2to3.pytree import Base, Leaf

class MockNode(Base):
    def __init__(self, children=None):
        self.children = children or []

def test_get_lineno_with_leaf_node():
    leaf = Leaf(type=1, value='value')
    leaf.lineno = 10
    assert leaf.get_lineno() == 10

def test_get_lineno_with_non_leaf_node():
    leaf = Leaf(type=1, value='value')
    leaf.lineno = 10
    non_leaf = MockNode(children=[leaf])
    assert non_leaf.get_lineno() == 10

def test_get_lineno_with_empty_children():
    non_leaf = MockNode(children=[])
    assert non_leaf.get_lineno() is None

def test_get_lineno_with_nested_non_leaf_nodes():
    leaf = Leaf(type=1, value='value')
    leaf.lineno = 10
    non_leaf_inner = MockNode(children=[leaf])
    non_leaf_outer = MockNode(children=[non_leaf_inner])
    assert non_leaf_outer.get_lineno() == 10
