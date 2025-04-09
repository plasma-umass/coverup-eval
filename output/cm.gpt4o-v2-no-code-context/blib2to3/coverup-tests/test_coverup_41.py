# file: src/blib2to3/pytree.py:220-222
# asked: {"lines": [220, 221, 222], "branches": [[221, 0], [221, 222]]}
# gained: {"lines": [220, 221, 222], "branches": [[221, 0], [221, 222]]}

import pytest
from blib2to3.pytree import Base

class MockBase(Base):
    def __init__(self):
        self.children = []

class MockChild:
    def leaves(self):
        return iter(["leaf1", "leaf2"])

@pytest.fixture
def base_with_children():
    base = MockBase()
    base.children = [MockChild(), MockChild()]
    return base

def test_leaves(base_with_children):
    leaves = list(base_with_children.leaves())
    assert leaves == ["leaf1", "leaf2", "leaf1", "leaf2"]
