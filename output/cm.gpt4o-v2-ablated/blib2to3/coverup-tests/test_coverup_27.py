# file: src/blib2to3/pytree.py:440-442
# asked: {"lines": [440, 442], "branches": []}
# gained: {"lines": [440, 442], "branches": []}

import pytest
from blib2to3.pytree import Leaf, Base

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

def test_eq_same_type_value(leaf, other_leaf):
    assert leaf._eq(other_leaf) is True

def test_eq_different_type_value(leaf, different_leaf):
    assert leaf._eq(different_leaf) is False

def test_eq_different_type_same_value(leaf):
    other = MockBase(type=2, value='a')
    assert leaf._eq(other) is False

def test_eq_same_type_different_value(leaf):
    other = MockBase(type=1, value='b')
    assert leaf._eq(other) is False
