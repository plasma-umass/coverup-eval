# file: src/blib2to3/pytree.py:295-297
# asked: {"lines": [295, 297], "branches": []}
# gained: {"lines": [295, 297], "branches": []}

import pytest
from blib2to3.pytree import Node

class MockBase:
    pass

class MockNode(Node, MockBase):
    def __init__(self, type, children):
        self.type = type
        self.children = children

@pytest.fixture
def node1():
    return MockNode(type=1, children=[1, 2, 3])

@pytest.fixture
def node2():
    return MockNode(type=1, children=[1, 2, 3])

@pytest.fixture
def node3():
    return MockNode(type=2, children=[1, 2, 3])

@pytest.fixture
def node4():
    return MockNode(type=1, children=[4, 5, 6])

def test_node_eq_same(node1, node2):
    assert node1._eq(node2) is True

def test_node_eq_different_type(node1, node3):
    assert node1._eq(node3) is False

def test_node_eq_different_children(node1, node4):
    assert node1._eq(node4) is False
