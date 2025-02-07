# file: src/blib2to3/pytree.py:220-222
# asked: {"lines": [221, 222], "branches": [[221, 0], [221, 222]]}
# gained: {"lines": [221, 222], "branches": [[221, 0], [221, 222]]}

import pytest
from unittest.mock import MagicMock
from blib2to3.pytree import Base

class MockChild:
    def leaves(self):
        yield "leaf"

class TestBase:
    def test_leaves(self):
        base = object.__new__(Base)
        base.children = [MockChild(), MockChild()]
        
        leaves = list(base.leaves())
        
        assert leaves == ["leaf", "leaf"]

        # Clean up
        base.children = []
