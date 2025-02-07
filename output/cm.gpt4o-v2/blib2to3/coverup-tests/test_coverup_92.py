# file: src/blib2to3/pytree.py:248-276
# asked: {"lines": [272], "branches": [[271, 272]]}
# gained: {"lines": [272], "branches": [[271, 272]]}

import pytest
from unittest.mock import Mock

from blib2to3.pytree import Node

class TestNode:
    def test_node_initialization_with_prefix(self):
        # Mock child node
        child = Mock()
        child.parent = None
        child.prefix = ""

        # Initialize Node with prefix
        node = Node(type=256, children=[child], prefix="test_prefix")

        # Assertions
        assert node.prefix == "test_prefix"
        assert child.parent == node

    def test_node_initialization_without_prefix(self):
        # Mock child node
        child = Mock()
        child.parent = None
        child.prefix = ""

        # Initialize Node without prefix
        node = Node(type=256, children=[child])

        # Assertions
        assert node.prefix == ""
        assert child.parent == node

    def test_node_initialization_with_fixers_applied(self):
        # Mock child node
        child = Mock()
        child.parent = None
        child.prefix = ""

        # Initialize Node with fixers_applied
        fixers = [Mock()]
        node = Node(type=256, children=[child], fixers_applied=fixers)

        # Assertions
        assert node.fixers_applied == fixers
        assert child.parent == node

    def test_node_initialization_without_fixers_applied(self):
        # Mock child node
        child = Mock()
        child.parent = None
        child.prefix = ""

        # Initialize Node without fixers_applied
        node = Node(type=256, children=[child])

        # Assertions
        assert node.fixers_applied is None
        assert child.parent == node
