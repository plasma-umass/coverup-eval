# file src/blib2to3/pytree.py:421-430
# lines [423, 425, 426, 427, 428, 429]
# branches []

import pytest
from blib2to3.pytree import Leaf

def test_leaf_repr(mocker):
    # Mocking the tok_name dictionary
    mock_tok_name = mocker.patch('blib2to3.pgen2.token.tok_name', {1: 'MOCK_TOKEN'})
    
    # Creating a Leaf instance with type and value
    leaf = Leaf(1, 'test_value')
    
    # Calling the __repr__ method
    repr_result = repr(leaf)
    
    # Asserting the expected output
    assert repr_result == "Leaf(MOCK_TOKEN, 'test_value')"
    
    # Clean up
    del leaf
