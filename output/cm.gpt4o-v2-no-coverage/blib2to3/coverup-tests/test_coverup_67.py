# file: src/blib2to3/pytree.py:457-459
# asked: {"lines": [457, 459], "branches": []}
# gained: {"lines": [457, 459], "branches": []}

import pytest
from blib2to3.pytree import Leaf

def test_leaf_post_order():
    leaf = Leaf(type=1, value='test')
    iterator = leaf.post_order()
    assert next(iterator) is leaf
    with pytest.raises(StopIteration):
        next(iterator)
