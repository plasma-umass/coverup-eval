# file: src/blib2to3/pytree.py:287-293
# asked: {"lines": [293], "branches": []}
# gained: {"lines": [293], "branches": []}

import pytest
from blib2to3.pytree import Node

def test_node_str_with_children(monkeypatch):
    class MockChild:
        def __str__(self):
            return "child"

    mock_children = [MockChild(), MockChild()]

    def mock_init(self, *args, **kwargs):
        self.children = mock_children

    monkeypatch.setattr(Node, "__init__", mock_init)

    node = Node()
    result = str(node)
    assert result == "childchild"

    # Clean up
    monkeypatch.undo()

def test_node_str_without_children(monkeypatch):
    def mock_init(self, *args, **kwargs):
        self.children = []

    monkeypatch.setattr(Node, "__init__", mock_init)

    node = Node()
    result = str(node)
    assert result == ""

    # Clean up
    monkeypatch.undo()
