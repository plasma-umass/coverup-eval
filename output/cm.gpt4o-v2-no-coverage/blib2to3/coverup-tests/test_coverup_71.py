# file: src/blib2to3/pytree.py:421-430
# asked: {"lines": [421, 423, 425, 426, 427, 428, 429], "branches": []}
# gained: {"lines": [421, 423, 425, 426, 427, 428, 429], "branches": []}

import pytest
from unittest.mock import patch

# Assuming the necessary imports and the Leaf class definition are available
# from the blib2to3.pytree module

class TestLeaf:
    @patch('blib2to3.pgen2.token.tok_name', {1: 'TOKEN_NAME'})
    def test_repr(self):
        from blib2to3.pytree import Leaf

        # Create a Leaf instance with type and value
        leaf = Leaf(1, 'value')

        # Call the __repr__ method and check the result
        result = repr(leaf)
        assert result == "Leaf(TOKEN_NAME, 'value')"

        # Clean up
        del leaf

    @patch('blib2to3.pgen2.token.tok_name', {})
    def test_repr_no_tok_name(self):
        from blib2to3.pytree import Leaf

        # Create a Leaf instance with type and value
        leaf = Leaf(2, 'value')

        # Call the __repr__ method and check the result
        result = repr(leaf)
        assert result == "Leaf(2, 'value')"

        # Clean up
        del leaf
