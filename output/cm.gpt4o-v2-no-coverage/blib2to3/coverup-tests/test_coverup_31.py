# file: src/blib2to3/pytree.py:220-222
# asked: {"lines": [220, 221, 222], "branches": [[221, 0], [221, 222]]}
# gained: {"lines": [220, 221, 222], "branches": [[221, 0], [221, 222]]}

import pytest
from unittest.mock import MagicMock

from blib2to3.pytree import Base

class MockLeaf:
    def leaves(self):
        yield self

class MockNode(Base):
    def __init__(self, children):
        self.children = children

def test_leaves():
    leaf1 = MockLeaf()
    leaf2 = MockLeaf()
    node = MockNode([leaf1, leaf2])

    leaves = list(node.leaves())
    assert leaves == [leaf1, leaf2]

    # Clean up
    del leaf1
    del leaf2
    del node
