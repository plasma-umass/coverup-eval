# file: src/blib2to3/pytree.py:287-293
# asked: {"lines": [287, 293], "branches": []}
# gained: {"lines": [287, 293], "branches": []}

import pytest
from unittest.mock import MagicMock

from blib2to3.pytree import Node

class TestNode:
    def test_str_method(self, monkeypatch):
        # Create a mock child node with a __str__ method and a parent attribute
        mock_child = MagicMock()
        mock_child.__str__.return_value = "child_str"
        mock_child.parent = None

        # Patch the invalidate_sibling_maps method to do nothing
        monkeypatch.setattr(Node, "invalidate_sibling_maps", lambda self: None)

        # Create a Node instance with the mock child
        node = Node(type=256, children=[mock_child])

        # Verify the __str__ method output
        assert str(node) == "child_str"

        # Clean up
        del node
        del mock_child
