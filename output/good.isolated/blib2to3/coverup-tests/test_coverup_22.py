# file src/blib2to3/pytree.py:229-238
# lines [229, 234, 235, 236, 237, 238]
# branches ['235->236', '235->237']

import pytest
from blib2to3.pytree import Base

class MockNode(Base):
    def __init__(self, next_sibling=None):
        self._next_sibling = next_sibling

    @property
    def next_sibling(self):
        return self._next_sibling

    @next_sibling.setter
    def next_sibling(self, value):
        self._next_sibling = value

class MockSiblingNode:
    def __init__(self, prefix):
        self.prefix = prefix

@pytest.fixture
def mock_node():
    return MockNode()

@pytest.fixture
def mock_sibling_node():
    return MockSiblingNode(prefix=" ")

def test_get_suffix_with_next_sibling(mock_node, mock_sibling_node):
    mock_node.next_sibling = mock_sibling_node
    suffix = mock_node.get_suffix()
    assert suffix == mock_sibling_node.prefix

def test_get_suffix_without_next_sibling(mock_node):
    mock_node.next_sibling = None
    suffix = mock_node.get_suffix()
    assert suffix == ""
