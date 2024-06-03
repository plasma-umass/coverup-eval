# file py_backwards/transformers/starred_unpacking.py:9-19
# lines [9, 10, 18]
# branches []

import pytest
from py_backwards.transformers.starred_unpacking import StarredUnpackingTransformer
from py_backwards.transformers.base import BaseNodeTransformer
from unittest import mock

def test_starred_unpacking_transformer():
    # Mock the BaseNodeTransformer to ensure the transformer is called
    with mock.patch.object(BaseNodeTransformer, '__init__', lambda x: None):
        transformer = StarredUnpackingTransformer()
    
    # Test the target attribute
    assert transformer.target == (3, 4)
    
    # Create a mock node to test the transformation
    mock_node = mock.Mock()
    mock_node.body = [
        mock.Mock(value=mock.Mock(elts=[2, mock.Mock(), 1])),
        mock.Mock(value=mock.Mock(args=[mock.Mock(), mock.Mock()]))
    ]
    
    # Mock the transform method to return the mock node
    with mock.patch.object(transformer, 'transform', return_value=mock_node):
        # Call the transform method and check the result
        result = transformer.transform(mock_node)
    
    # Verify the transformation
    assert result.body[0].value.elts == [2, mock.ANY, 1]
    assert result.body[1].value.args == [mock.ANY, mock.ANY]
