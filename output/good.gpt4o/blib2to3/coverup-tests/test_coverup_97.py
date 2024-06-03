# file src/blib2to3/pytree.py:457-459
# lines [459]
# branches []

import pytest
from blib2to3.pytree import Leaf

def test_leaf_post_order():
    # Create a Leaf instance with required arguments
    leaf = Leaf(type=1, value='test')
    post_order_iterator = leaf.post_order()
    
    # Check that the iterator yields the leaf itself
    assert next(post_order_iterator) is leaf
    
    # Check that the iterator is exhausted
    with pytest.raises(StopIteration):
        next(post_order_iterator)
