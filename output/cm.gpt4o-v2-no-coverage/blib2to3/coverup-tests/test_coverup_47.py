# file: src/blib2to3/pytree.py:320-327
# asked: {"lines": [320, 321, 325, 326, 327], "branches": [[325, 326], [325, 327]]}
# gained: {"lines": [320, 321, 325, 326, 327], "branches": [[325, 326], [325, 327]]}

import pytest
from blib2to3.pytree import Node

class MockChild:
    def __init__(self, prefix):
        self.prefix = prefix
        self.parent = None

def test_node_prefix_no_children():
    node = Node(type=256, children=[])
    assert node.prefix == ""

def test_node_prefix_with_children():
    child = MockChild(prefix=" ")
    node = Node(type=256, children=[child])
    assert node.prefix == " "

@pytest.fixture
def mock_node(monkeypatch):
    def mock_init(self, type, children, context=None, prefix=None, fixers_applied=None):
        self.type = type
        self.children = children
        for ch in self.children:
            ch.parent = self
        self._prefix = prefix if prefix is not None else ""
        self.fixers_applied = fixers_applied if fixers_applied else None

    def mock_prefix_getter(self):
        if not self.children:
            return self._prefix
        return self.children[0].prefix

    monkeypatch.setattr(Node, "__init__", mock_init)
    monkeypatch.setattr(Node, "prefix", property(mock_prefix_getter))
    yield
    monkeypatch.undo()

def test_node_prefix_with_monkeypatch(mock_node):
    child = MockChild(prefix=" ")
    node = Node(type=256, children=[child])
    assert node.prefix == " "
