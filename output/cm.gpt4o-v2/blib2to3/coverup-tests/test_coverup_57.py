# file: src/blib2to3/pytree.py:461-463
# asked: {"lines": [461, 463], "branches": []}
# gained: {"lines": [461, 463], "branches": []}

import pytest
from blib2to3.pytree import Leaf

def test_leaf_pre_order():
    leaf = Leaf(type=1, value="test")
    iterator = leaf.pre_order()
    assert next(iterator) is leaf

