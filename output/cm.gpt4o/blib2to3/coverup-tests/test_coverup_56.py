# file src/blib2to3/pytree.py:440-442
# lines [440, 442]
# branches []

import pytest
from blib2to3.pytree import Base

class Leaf(Base):
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def _eq(self, other) -> bool:
        """Compare two nodes for equality."""
        return (self.type, self.value) == (other.type, other.value)

def test_leaf_eq():
    leaf1 = Leaf(type=1, value='a')
    leaf2 = Leaf(type=1, value='a')
    leaf3 = Leaf(type=2, value='b')

    assert leaf1._eq(leaf2) == True, "Leaves with same type and value should be equal"
    assert leaf1._eq(leaf3) == False, "Leaves with different type and value should not be equal"
    assert leaf2._eq(leaf3) == False, "Leaves with different type and value should not be equal"
