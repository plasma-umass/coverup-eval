# file: src/blib2to3/pytree.py:278-285
# asked: {"lines": [278, 280, 281, 282, 283, 284], "branches": []}
# gained: {"lines": [278, 280, 281, 282, 283, 284], "branches": []}

import pytest
from unittest.mock import Mock

from blib2to3.pytree import Node, type_repr

@pytest.fixture
def mock_base():
    class MockBase:
        pass
    return MockBase

def test_node_repr(mock_base, monkeypatch):
    # Mocking the Base class
    monkeypatch.setattr("blib2to3.pytree.Base", mock_base)
    
    # Creating a mock Node instance
    node = Node(type=256, children=[])
    node.children = []

    # Mocking type_repr function
    monkeypatch.setattr("blib2to3.pytree.type_repr", lambda x: "MOCK_TYPE")

    # Testing __repr__ method
    result = repr(node)
    assert result == "Node(MOCK_TYPE, [])"

    # Testing assertion error when type is None
    node.type = None
    with pytest.raises(AssertionError):
        repr(node)
