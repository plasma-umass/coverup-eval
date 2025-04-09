# file: src/blib2to3/pytree.py:308-312
# asked: {"lines": [308, 310, 311, 312], "branches": [[310, 311], [310, 312]]}
# gained: {"lines": [308, 310, 311, 312], "branches": [[310, 311], [310, 312]]}

import pytest
from blib2to3.pytree import Node

class MockChild:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.parent = None

    def post_order(self):
        yield self

@pytest.fixture
def setup_node():
    child1 = MockChild("child1")
    child2 = MockChild("child2")
    node = Node(type=256, children=[child1, child2])
    return node, child1, child2

def test_post_order(setup_node):
    node, child1, child2 = setup_node
    result = list(node.post_order())
    assert result == [child1, child2, node]

def test_post_order_no_children():
    node = Node(type=256, children=[])
    result = list(node.post_order())
    assert result == [node]
