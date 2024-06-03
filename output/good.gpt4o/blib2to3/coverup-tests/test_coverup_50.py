# file src/blib2to3/pytree.py:454-455
# lines [454, 455]
# branches []

import pytest
from blib2to3.pytree import Base

class TestLeaf:
    def test_leaves(self):
        class Leaf(Base):
            def leaves(self):
                yield self

        leaf_instance = Leaf()
        leaves = list(leaf_instance.leaves())
        
        assert len(leaves) == 1
        assert leaves[0] is leaf_instance
