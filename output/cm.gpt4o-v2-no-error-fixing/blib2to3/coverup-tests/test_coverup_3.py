# file: src/blib2to3/pytree.py:161-168
# asked: {"lines": [161, 163, 164, 165, 166, 167, 168], "branches": [[164, 165], [164, 168], [165, 166], [165, 167]]}
# gained: {"lines": [161, 163, 164, 165, 166, 167, 168], "branches": [[164, 165], [164, 168], [165, 166], [165, 167]]}

import pytest
from blib2to3.pytree import Base, Leaf

class MockNode(Base):
    def __init__(self, children=None):
        self.children = children if children is not None else []

def test_get_lineno_with_leaf():
    leaf = Leaf(1, "value")
    assert leaf.get_lineno() == 0

def test_get_lineno_with_non_leaf():
    leaf = Leaf(1, "value")
    node = MockNode(children=[leaf])
    assert node.get_lineno() == 0

def test_get_lineno_with_empty_children():
    node = MockNode(children=[])
    assert node.get_lineno() is None

def test_get_lineno_with_nested_nodes():
    leaf = Leaf(1, "value")
    inner_node = MockNode(children=[leaf])
    outer_node = MockNode(children=[inner_node])
    assert outer_node.get_lineno() == 0
