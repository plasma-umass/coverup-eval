# file src/blib2to3/pytree.py:461-463
# lines [461, 463]
# branches []

import pytest
from blib2to3.pytree import Leaf
from blib2to3.pgen2.token import NAME

def test_leaf_pre_order():
    # Create an instance of Leaf with required arguments
    leaf = Leaf(type=NAME, value="test")
    
    # Get the pre-order iterator
    iterator = leaf.pre_order()
    
    # Convert the iterator to a list and check its contents
    result = list(iterator)
    
    # Assert that the result contains only the leaf itself
    assert result == [leaf]
