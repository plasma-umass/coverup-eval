# file: src/blib2to3/pytree.py:440-442
# asked: {"lines": [440, 442], "branches": []}
# gained: {"lines": [440, 442], "branches": []}

import pytest
from blib2to3.pytree import Leaf

def test_leaf_eq():
    leaf1 = Leaf(type=1, value="value1")
    leaf2 = Leaf(type=1, value="value1")
    leaf3 = Leaf(type=2, value="value2")

    assert leaf1._eq(leaf2) is True
    assert leaf1._eq(leaf3) is False
    assert leaf2._eq(leaf3) is False
