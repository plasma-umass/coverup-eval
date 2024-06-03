# file py_backwards/transformers/return_from_generator.py:15-28
# lines [15, 16, 27]
# branches []

import pytest
from py_backwards.transformers.return_from_generator import ReturnFromGeneratorTransformer
from py_backwards.transformers.base import BaseNodeTransformer

def test_return_from_generator_transformer(mocker):
    # Mock the tree argument required by BaseNodeTransformer
    mock_tree = mocker.Mock()

    # Ensure the transformer class is correctly defined and inherits from BaseNodeTransformer
    assert issubclass(ReturnFromGeneratorTransformer, BaseNodeTransformer)
    
    # Ensure the target version is correctly set
    assert ReturnFromGeneratorTransformer.target == (3, 2)

    # Create an instance of the transformer with the mocked tree
    transformer = ReturnFromGeneratorTransformer(mock_tree)
    
    # Ensure the instance is of the correct type
    assert isinstance(transformer, ReturnFromGeneratorTransformer)
    
    # Ensure the instance has the correct target attribute
    assert transformer.target == (3, 2)
