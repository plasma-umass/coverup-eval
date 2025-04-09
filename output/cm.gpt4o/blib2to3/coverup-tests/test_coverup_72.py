# file src/blib2to3/pytree.py:457-459
# lines [457, 459]
# branches []

import pytest
from blib2to3.pytree import Base
from typing import Iterator

class TestLeaf:
    def test_post_order(self):
        class Leaf(Base):
            def post_order(self) -> Iterator["Leaf"]:
                """Return a post-order iterator for the tree."""
                yield self

        leaf = Leaf()
        post_order_iterator = leaf.post_order()
        
        # Check that the iterator returns the leaf itself
        assert next(post_order_iterator) is leaf
        
        # Check that the iterator is exhausted
        with pytest.raises(StopIteration):
            next(post_order_iterator)
