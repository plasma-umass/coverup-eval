# file src/blib2to3/pytree.py:320-327
# lines [320, 321, 325, 326, 327]
# branches ['325->326', '325->327']

import pytest
from blib2to3.pytree import Node
from blib2to3.pytree import Leaf

@pytest.fixture
def cleanup_leaves():
    created_leaves = []
    yield created_leaves
    for leaf in created_leaves:
        del leaf

def test_node_prefix_with_no_children(cleanup_leaves):
    node = Node(type=256, children=[])
    assert node.prefix == "", "Node prefix should be empty string when there are no children"

def test_node_prefix_with_children(cleanup_leaves):
    leaf = Leaf(type=1, value="", context=("", (1, 0)))
    cleanup_leaves.append(leaf)
    node = Node(type=256, children=[leaf])
    assert node.prefix == leaf.prefix, "Node prefix should match the prefix of the first child"
