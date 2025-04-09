# file src/blib2to3/pytree.py:444-452
# lines [444, 445, 446, 447, 448, 449, 450, 451]
# branches []

import pytest
from blib2to3.pytree import Leaf

class MockLeaf(Leaf):
    def __init__(self, type, value, context, fixers_applied=None):
        self.type = type
        self.value = value
        self.prefix, (self.lineno, self.column) = context
        self.fixers_applied = fixers_applied if fixers_applied is not None else []

@pytest.fixture
def mock_leaf():
    return MockLeaf(
        type=1,
        value="value",
        context=(" ", (1, 0)),
        fixers_applied=[]
    )

def test_leaf_clone(mock_leaf):
    cloned_leaf = mock_leaf.clone()
    assert cloned_leaf.type == mock_leaf.type
    assert cloned_leaf.value == mock_leaf.value
    assert cloned_leaf.prefix == mock_leaf.prefix
    assert cloned_leaf.lineno == mock_leaf.lineno
    assert cloned_leaf.column == mock_leaf.column
    assert cloned_leaf.fixers_applied == mock_leaf.fixers_applied
