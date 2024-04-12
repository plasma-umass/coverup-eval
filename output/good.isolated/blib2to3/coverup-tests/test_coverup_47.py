# file src/blib2to3/pytree.py:461-463
# lines [461, 463]
# branches []

import pytest
from blib2to3.pytree import Leaf

def test_leaf_pre_order():
    leaf = Leaf(type=0, value="")
    iterator = leaf.pre_order()
    assert next(iterator) is leaf  # Check that the first item from the iterator is the leaf itself

    with pytest.raises(StopIteration):
        next(iterator)  # Check that the iterator is exhausted after yielding the leaf
