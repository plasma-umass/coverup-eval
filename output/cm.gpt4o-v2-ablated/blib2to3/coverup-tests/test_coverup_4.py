# file: src/blib2to3/pytree.py:248-276
# asked: {"lines": [248, 252, 253, 254, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 276], "branches": [[267, 268], [267, 270], [271, 272], [271, 273], [273, 274], [273, 276]]}
# gained: {"lines": [248, 252, 253, 254, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 276], "branches": [[267, 268], [267, 270], [271, 272], [271, 273], [273, 274], [273, 276]]}

import pytest
from unittest.mock import Mock

# Assuming NL and Base are defined somewhere in the module
# Mocking them for the purpose of this test
class Base:
    pass

class NL:
    def __init__(self):
        self.parent = None

from blib2to3.pytree import Node

@pytest.fixture
def mock_node():
    return NL()

def test_node_initialization_with_prefix_and_fixers(mock_node):
    children = [mock_node, NL()]
    node = Node(type=256, children=children, prefix="test_prefix", fixers_applied=["fixer1", "fixer2"])
    
    assert node.type == 256
    assert node.children == children
    assert node.prefix == "test_prefix"
    assert node.fixers_applied == ["fixer1", "fixer2"]
    for child in children:
        assert child.parent == node

def test_node_initialization_without_prefix_and_fixers(mock_node):
    children = [mock_node, NL()]
    node = Node(type=256, children=children)
    
    assert node.type == 256
    assert node.children == children
    assert not hasattr(node, 'prefix')
    assert node.fixers_applied is None
    for child in children:
        assert child.parent == node

def test_node_initialization_with_prefix_without_fixers(mock_node):
    children = [mock_node, NL()]
    node = Node(type=256, children=children, prefix="test_prefix")
    
    assert node.type == 256
    assert node.children == children
    assert node.prefix == "test_prefix"
    assert node.fixers_applied is None
    for child in children:
        assert child.parent == node

def test_node_initialization_without_prefix_with_fixers(mock_node):
    children = [mock_node, NL()]
    node = Node(type=256, children=children, fixers_applied=["fixer1", "fixer2"])
    
    assert node.type == 256
    assert node.children == children
    assert not hasattr(node, 'prefix')
    assert node.fixers_applied == ["fixer1", "fixer2"]
    for child in children:
        assert child.parent == node

def test_node_initialization_with_invalid_type():
    with pytest.raises(AssertionError):
        Node(type=255, children=[])

def test_node_initialization_with_non_none_parent(mock_node):
    child = NL()
    child.parent = mock_node
    with pytest.raises(AssertionError):
        Node(type=256, children=[child])
