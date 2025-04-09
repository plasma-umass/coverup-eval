# file: src/blib2to3/pytree.py:421-430
# asked: {"lines": [423, 425, 426, 427, 428, 429], "branches": []}
# gained: {"lines": [423, 425, 426, 427, 428, 429], "branches": []}

import pytest
from blib2to3.pytree import Leaf

def test_leaf_repr(monkeypatch):
    # Mock tok_name to control its behavior
    mock_tok_name = {1: 'MOCK_TOKEN'}
    monkeypatch.setattr('blib2to3.pgen2.token.tok_name', mock_tok_name)

    # Create a Leaf instance with type and value
    leaf = Leaf(type=1, value='test_value')

    # Check the __repr__ output
    repr_output = repr(leaf)
    expected_output = "Leaf(MOCK_TOKEN, 'test_value')"
    assert repr_output == expected_output

    # Ensure the type is not None
    assert leaf.type is not None
