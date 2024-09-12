# file: src/blib2to3/pytree.py:465-470
# asked: {"lines": [465, 466, 470], "branches": []}
# gained: {"lines": [465, 466, 470], "branches": []}

import pytest
from blib2to3.pytree import Leaf

class MockBase:
    def __init__(self, prefix):
        self._prefix = prefix

@pytest.fixture
def mock_leaf(monkeypatch):
    def mock_init(self, prefix):
        MockBase.__init__(self, prefix)
    monkeypatch.setattr(Leaf, "__init__", mock_init)
    return Leaf("mock_prefix")

def test_leaf_prefix(mock_leaf):
    assert mock_leaf.prefix == "mock_prefix"
