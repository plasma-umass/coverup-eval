# file: src/blib2to3/pytree.py:421-430
# asked: {"lines": [421, 423, 425, 426, 427, 428, 429], "branches": []}
# gained: {"lines": [421, 423, 425, 426, 427, 428, 429], "branches": []}

import pytest
from unittest.mock import patch

def test_leaf_repr():
    from blib2to3.pytree import Leaf

    # Creating a Leaf instance with required attributes
    leaf = Leaf(1, 'test_value')

    # Mocking tok_name to control its behavior
    with patch('blib2to3.pgen2.token.tok_name', {1: 'MOCK_TOKEN'}):
        # Expected representation string
        expected_repr = "Leaf(MOCK_TOKEN, 'test_value')"

        # Asserting the __repr__ output
        assert repr(leaf) == expected_repr
