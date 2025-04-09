# file: src/blib2to3/pytree.py:229-238
# asked: {"lines": [229, 234, 235, 236, 237, 238], "branches": [[235, 236], [235, 237]]}
# gained: {"lines": [229, 234, 235, 236, 237, 238], "branches": [[235, 236], [235, 237]]}

import pytest
from blib2to3.pytree import Base

class MockNode:
    def __init__(self, prefix=None):
        self.prefix = prefix

class MockBase(Base):
    def __init__(self, next_sibling=None):
        self._next_sibling = next_sibling

    @property
    def next_sibling(self):
        return self._next_sibling

@pytest.fixture
def mock_base_with_sibling():
    sibling = MockNode(prefix="suffix")
    return MockBase(next_sibling=sibling)

@pytest.fixture
def mock_base_without_sibling():
    return MockBase(next_sibling=None)

def test_get_suffix_with_sibling(mock_base_with_sibling):
    result = mock_base_with_sibling.get_suffix()
    assert result == "suffix"

def test_get_suffix_without_sibling(mock_base_without_sibling):
    result = mock_base_without_sibling.get_suffix()
    assert result == ""
