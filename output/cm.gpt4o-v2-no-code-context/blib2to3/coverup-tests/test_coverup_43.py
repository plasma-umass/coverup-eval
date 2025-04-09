# file: src/blib2to3/pytree.py:278-285
# asked: {"lines": [278, 280, 281, 282, 283, 284], "branches": []}
# gained: {"lines": [278, 280, 281, 282, 283, 284], "branches": []}

import pytest
from blib2to3.pytree import Node, type_repr

class MockType:
    def __repr__(self):
        return "MockType"

class MockNode(Node):
    def __init__(self, type, children):
        self.type = type
        self.children = children

def mock_type_repr(type_num):
    return "MockType"

@pytest.fixture
def mock_type_repr_fixture(monkeypatch):
    monkeypatch.setattr("blib2to3.pytree.type_repr", mock_type_repr)

def test_node_repr(mock_type_repr_fixture):
    mock_type = MockType()
    children = ["child1", "child2"]
    node = MockNode(mock_type, children)
    
    # Ensure the __repr__ method is called and the output is as expected
    expected_repr = "MockNode(MockType, ['child1', 'child2'])"
    assert repr(node) == expected_repr
