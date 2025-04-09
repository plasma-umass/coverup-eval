# file: src/blib2to3/pytree.py:461-463
# asked: {"lines": [461, 463], "branches": []}
# gained: {"lines": [461, 463], "branches": []}

import pytest
from blib2to3.pytree import Leaf
from lib2to3.pgen2.token import NAME

def test_leaf_pre_order():
    leaf = Leaf(NAME, 'test')
    iterator = leaf.pre_order()
    assert next(iterator) is leaf
    with pytest.raises(StopIteration):
        next(iterator)
