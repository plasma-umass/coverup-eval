# file src/blib2to3/pytree.py:440-442
# lines [442]
# branches []

import pytest
from blib2to3.pytree import Leaf

class MockBase:
    def __init__(self, type, value):
        self.type = type
        self.value = value

def test_leaf_eq():
    leaf1 = Leaf(1, 'value1')
    leaf2 = Leaf(1, 'value1')
    leaf3 = Leaf(2, 'value2')
    
    assert leaf1._eq(leaf2) == True, "Leaves with same type and value should be equal"
    assert leaf1._eq(leaf3) == False, "Leaves with different type and value should not be equal"
