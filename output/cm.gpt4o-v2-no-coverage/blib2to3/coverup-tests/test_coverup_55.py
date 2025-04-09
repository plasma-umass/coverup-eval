# file: src/blib2to3/pytree.py:440-442
# asked: {"lines": [440, 442], "branches": []}
# gained: {"lines": [440, 442], "branches": []}

import pytest
from blib2to3.pytree import Leaf

class MockBase:
    pass

class MockLeaf(Leaf, MockBase):
    def __init__(self, type, value):
        self.type = type
        self.value = value

def test_eq():
    leaf1 = MockLeaf(1, 'value1')
    leaf2 = MockLeaf(1, 'value1')
    leaf3 = MockLeaf(2, 'value2')

    assert leaf1._eq(leaf2) == True
    assert leaf1._eq(leaf3) == False
