# file: src/blib2to3/pytree.py:461-463
# asked: {"lines": [461, 463], "branches": []}
# gained: {"lines": [461, 463], "branches": []}

import pytest
from blib2to3.pytree import Leaf

def test_leaf_pre_order():
    # Create a Leaf instance
    leaf = Leaf(type=1, value="test")

    # Get the pre-order iterator
    iterator = leaf.pre_order()

    # Assert that the iterator yields the leaf itself
    assert next(iterator) is leaf

    # Assert that the iterator is exhausted
    with pytest.raises(StopIteration):
        next(iterator)
