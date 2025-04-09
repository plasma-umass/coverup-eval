# file: src/blib2to3/pytree.py:440-442
# asked: {"lines": [440, 442], "branches": []}
# gained: {"lines": [440, 442], "branches": []}

import pytest
from blib2to3.pytree import Leaf

class MockBase:
    def __init__(self, type, value):
        self.type = type
        self.value = value

@pytest.fixture
def leaf():
    return Leaf(type=1, value='a')

@pytest.fixture
def other_leaf():
    return Leaf(type=1, value='a')

@pytest.fixture
def different_leaf():
    return Leaf(type=2, value='b')

def test_leaf_eq_same(leaf, other_leaf):
    assert leaf._eq(other_leaf) == True

def test_leaf_eq_different(leaf, different_leaf):
    assert leaf._eq(different_leaf) == False
