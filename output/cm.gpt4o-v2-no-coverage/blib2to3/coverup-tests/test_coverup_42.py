# file: src/blib2to3/pytree.py:248-276
# asked: {"lines": [248, 252, 253, 254, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 276], "branches": [[267, 268], [267, 270], [271, 272], [271, 273], [273, 274], [273, 276]]}
# gained: {"lines": [248, 252, 253, 254, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 276], "branches": [[267, 268], [267, 270], [271, 272], [271, 273], [273, 274], [273, 276]]}

import pytest
from unittest.mock import Mock

from blib2to3.pytree import Node

class TestNode:
    def test_node_initialization(self):
        # Mock child node
        child1 = Mock()
        child1.parent = None
        child1.prefix = ''
        child2 = Mock()
        child2.parent = None
        child2.prefix = ''

        # Initialize Node
        node = Node(type=256, children=[child1, child2], context=None, prefix="test_prefix", fixers_applied=["fixer1"])

        # Assertions
        assert node.type == 256
        assert node.children == [child1, child2]
        assert node.prefix == "test_prefix"
        assert node.fixers_applied == ["fixer1"]
        assert child1.parent == node
        assert child2.parent == node

    def test_node_initialization_no_prefix(self):
        # Mock child node
        child1 = Mock()
        child1.parent = None
        child1.prefix = ''
        child2 = Mock()
        child2.parent = None
        child2.prefix = ''

        # Initialize Node without prefix
        node = Node(type=256, children=[child1, child2], context=None)

        # Assertions
        assert node.type == 256
        assert node.children == [child1, child2]
        assert node.prefix == ''
        assert node.fixers_applied is None
        assert child1.parent == node
        assert child2.parent == node

    def test_node_initialization_no_fixers_applied(self):
        # Mock child node
        child1 = Mock()
        child1.parent = None
        child1.prefix = ''
        child2 = Mock()
        child2.parent = None
        child2.prefix = ''

        # Initialize Node without fixers_applied
        node = Node(type=256, children=[child1, child2], context=None, prefix="test_prefix")

        # Assertions
        assert node.type == 256
        assert node.children == [child1, child2]
        assert node.prefix == "test_prefix"
        assert node.fixers_applied is None
        assert child1.parent == node
        assert child2.parent == node

    def test_node_initialization_with_invalid_type(self):
        # Mock child node
        child1 = Mock()
        child1.parent = None
        child1.prefix = ''

        # Initialize Node with invalid type
        with pytest.raises(AssertionError):
            Node(type=255, children=[child1], context=None)

    def test_node_initialization_with_child_having_parent(self):
        # Mock child node
        child1 = Mock()
        child1.parent = Mock()
        child1.prefix = ''

        # Initialize Node with child already having a parent
        with pytest.raises(AssertionError):
            Node(type=256, children=[child1], context=None)
