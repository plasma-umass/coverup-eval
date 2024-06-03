# file src/blib2to3/pytree.py:248-276
# lines [272, 274]
# branches ['271->272', '273->274']

import pytest
from blib2to3.pytree import Node

class MockChild:
    def __init__(self):
        self.parent = None
        self.prefix = ""

def test_node_initialization_with_prefix_and_fixers_applied():
    type = 256
    children = [MockChild(), MockChild()]
    context = None
    prefix = "test_prefix"
    fixers_applied = ["fixer1", "fixer2"]

    node = Node(type, children, context, prefix, fixers_applied)

    assert node.prefix == prefix
    assert node.fixers_applied == fixers_applied
    assert all(child.parent == node for child in children)

def test_node_initialization_without_prefix_and_fixers_applied():
    type = 256
    children = [MockChild(), MockChild()]
    context = None

    node = Node(type, children, context)

    assert node.prefix == ""
    assert node.fixers_applied is None
    assert all(child.parent == node for child in children)
