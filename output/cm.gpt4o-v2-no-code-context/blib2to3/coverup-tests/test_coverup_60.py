# file: src/blib2to3/pytree.py:457-459
# asked: {"lines": [457, 459], "branches": []}
# gained: {"lines": [457, 459], "branches": []}

import pytest
from blib2to3.pytree import Leaf
from blib2to3.pgen2.token import NAME

def test_leaf_post_order():
    leaf = Leaf(NAME, 'test')
    post_order_iterator = leaf.post_order()
    assert list(post_order_iterator) == [leaf]
