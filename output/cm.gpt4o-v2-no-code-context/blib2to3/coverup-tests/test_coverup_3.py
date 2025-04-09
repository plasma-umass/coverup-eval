# file: src/blib2to3/pytree.py:248-276
# asked: {"lines": [248, 252, 253, 254, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 276], "branches": [[267, 268], [267, 270], [271, 272], [271, 273], [273, 274], [273, 276]]}
# gained: {"lines": [248, 252, 253, 254, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 276], "branches": [[267, 268], [267, 270], [271, 272], [271, 273], [273, 274], [273, 276]]}

import pytest
from blib2to3.pytree import Node

class MockChild:
    def __init__(self):
        self.parent = None

def test_node_initialization_with_context():
    children = [MockChild(), MockChild()]
    node = Node(type=256, children=children, context="some_context")
    assert node.type == 256
    assert node.children == children
    assert all(child.parent == node for child in children)

def test_node_initialization_with_prefix():
    children = [MockChild(), MockChild()]
    node = Node(type=256, children=children, prefix="some_prefix")
    assert node.prefix == "some_prefix"

def test_node_initialization_with_fixers_applied():
    children = [MockChild(), MockChild()]
    fixers = ["fixer1", "fixer2"]
    node = Node(type=256, children=children, fixers_applied=fixers)
    assert node.fixers_applied == fixers

def test_node_initialization_without_fixers_applied():
    children = [MockChild(), MockChild()]
    node = Node(type=256, children=children)
    assert node.fixers_applied is None

def test_node_initialization_with_all_parameters():
    children = [MockChild(), MockChild()]
    fixers = ["fixer1", "fixer2"]
    node = Node(type=256, children=children, context="some_context", prefix="some_prefix", fixers_applied=fixers)
    assert node.type == 256
    assert node.children == children
    assert node.prefix == "some_prefix"
    assert node.fixers_applied == fixers
    assert all(child.parent == node for child in children)
