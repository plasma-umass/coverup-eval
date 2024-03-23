# file src/blib2to3/pytree.py:299-306
# lines [300, 301, 302, 303, 304, 305]
# branches []

import pytest
from blib2to3.pytree import Node

class SimpleNode(Node):
    def __init__(self, type, children, fixers_applied):
        super().__init__(type, children, fixers_applied=fixers_applied)

@pytest.fixture
def simple_node():
    child_node = SimpleNode(type=256, children=[], fixers_applied=[])
    return SimpleNode(type=257, children=[child_node], fixers_applied=[])

def test_node_clone(simple_node):
    cloned_node = simple_node.clone()
    assert cloned_node.type == simple_node.type
    assert cloned_node.fixers_applied == simple_node.fixers_applied
    assert cloned_node.children != simple_node.children
    assert all(isinstance(child, Node) for child in cloned_node.children)
    assert cloned_node.children[0].type == simple_node.children[0].type
