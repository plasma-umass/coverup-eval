# file: src/blib2to3/pytree.py:248-276
# asked: {"lines": [248, 252, 253, 254, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 276], "branches": [[267, 268], [267, 270], [271, 272], [271, 273], [273, 274], [273, 276]]}
# gained: {"lines": [248, 252, 253, 254, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 276], "branches": [[267, 268], [267, 270], [271, 272], [271, 273], [273, 274], [273, 276]]}

import pytest
from blib2to3.pytree import Node
from typing import Any, List, Optional

class MockChild:
    def __init__(self):
        self.parent = None

def test_node_init_with_prefix_and_fixers_applied():
    children = [MockChild(), MockChild()]
    node = Node(type=256, children=children, prefix="test_prefix", fixers_applied=["fixer1", "fixer2"])
    
    assert node.type == 256
    assert node.children == children
    assert all(child.parent == node for child in children)
    assert node.prefix == "test_prefix"
    assert node.fixers_applied == ["fixer1", "fixer2"]
    assert node.prev_sibling_map is None
    assert node.next_sibling_map is None

def test_node_init_without_prefix_and_fixers_applied():
    children = [MockChild(), MockChild()]
    node = Node(type=256, children=children)
    
    assert node.type == 256
    assert node.children == children
    assert all(child.parent == node for child in children)
    assert not hasattr(node, 'prefix')
    assert node.fixers_applied is None
    assert node.prev_sibling_map is None
    assert node.next_sibling_map is None

def test_node_init_with_invalid_type():
    children = [MockChild(), MockChild()]
    with pytest.raises(AssertionError):
        Node(type=255, children=children)

def test_node_init_with_child_having_parent():
    child_with_parent = MockChild()
    child_with_parent.parent = "existing_parent"
    children = [child_with_parent]
    with pytest.raises(AssertionError):
        Node(type=256, children=children)
