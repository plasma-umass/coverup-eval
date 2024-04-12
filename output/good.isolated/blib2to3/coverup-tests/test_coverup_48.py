# file src/blib2to3/pytree.py:457-459
# lines [457, 459]
# branches []

import pytest
from blib2to3.pytree import Leaf

def test_leaf_post_order():
    leaf = Leaf(type=0, value="")
    iterator = leaf.post_order()
    assert next(iterator) is leaf

    with pytest.raises(StopIteration):
        next(iterator)
