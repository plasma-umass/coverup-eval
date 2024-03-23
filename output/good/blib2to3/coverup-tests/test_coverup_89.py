# file src/blib2to3/pytree.py:248-276
# lines [272, 274]
# branches ['271->272', '273->274']

import pytest
from blib2to3.pytree import Node, Leaf

@pytest.fixture
def cleanup_nodes():
    created_nodes = []

    yield created_nodes

    for node in created_nodes:
        node.parent = None

def test_node_init_with_prefix_and_fixers_applied(cleanup_nodes):
    prefix = "test_prefix"
    fixers_applied = ["fixer1", "fixer2"]
    leaf = Leaf(255, "")  # Use a valid token number for Leaf (less than 256)
    cleanup_nodes.append(leaf)
    node = Node(256, [leaf], prefix=prefix, fixers_applied=fixers_applied)
    cleanup_nodes.append(node)

    assert node.prefix == prefix
    assert node.fixers_applied == fixers_applied
    assert node.fixers_applied is not fixers_applied  # Ensure a copy was made
    assert all(child.parent is node for child in node.children)
