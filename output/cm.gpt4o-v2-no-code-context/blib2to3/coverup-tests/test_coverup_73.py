# file: src/blib2to3/pytree.py:320-327
# asked: {"lines": [326], "branches": [[325, 326]]}
# gained: {"lines": [326], "branches": [[325, 326]]}

import pytest
from blib2to3.pytree import Node

class MockBase:
    def __init__(self, children=None):
        self.children = children or []

class TestNode:
    def test_prefix_no_children(self):
        node = Node.__new__(Node)
        node.children = []
        assert node.prefix == ""

    def test_prefix_with_children(self, mocker):
        mock_child = mocker.Mock()
        mock_child.prefix = " "
        node = Node.__new__(Node)
        node.children = [mock_child]
        assert node.prefix == " "
