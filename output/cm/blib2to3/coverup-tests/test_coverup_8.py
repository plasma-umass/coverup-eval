# file src/blib2to3/pytree.py:161-168
# lines [161, 163, 164, 165, 166, 167, 168]
# branches ['164->165', '164->168', '165->166', '165->167']

import pytest
from blib2to3.pytree import Base, Leaf, Node

class LeafChild(Leaf):
    def __init__(self, lineno):
        super().__init__(type=0, value="")
        self.lineno = lineno

class NodeChild(Node):
    def __init__(self, children):
        # Use a valid type number (>= 256) for Node
        super().__init__(type=256, children=children)

@pytest.fixture
def cleanup():
    # Setup if necessary
    yield
    # Cleanup if necessary

def test_get_lineno_with_leaf_child(cleanup):
    leaf = LeafChild(lineno=42)
    assert leaf.get_lineno() == 42

def test_get_lineno_with_node_child_no_children(cleanup):
    node = NodeChild(children=[])
    assert node.get_lineno() is None

def test_get_lineno_with_node_child_with_leaf(cleanup):
    leaf = LeafChild(lineno=99)
    node = NodeChild(children=[leaf])
    assert node.get_lineno() == 99

def test_get_lineno_with_nested_nodes(cleanup):
    leaf = LeafChild(lineno=123)
    inner_node = NodeChild(children=[leaf])
    outer_node = NodeChild(children=[inner_node])
    assert outer_node.get_lineno() == 123
