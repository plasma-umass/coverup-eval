# file: src/blib2to3/pytree.py:421-430
# asked: {"lines": [421, 423, 425, 426, 427, 428, 429], "branches": []}
# gained: {"lines": [421, 423, 425, 426, 427, 428, 429], "branches": []}

import pytest
from blib2to3.pytree import Leaf
from blib2to3.pgen2.token import NAME

@pytest.fixture
def mock_leaf():
    return Leaf(type=NAME, value='test_value')

def test_leaf_repr(mock_leaf):
    repr_str = repr(mock_leaf)
    assert repr_str == "Leaf(NAME, 'test_value')"
