# file py_backwards/transformers/starred_unpacking.py:66-72
# lines [68]
# branches ['67->68']

import ast
import pytest
from py_backwards.transformers.starred_unpacking import StarredUnpackingTransformer
from py_backwards.transformers.base import BaseNodeTransformer

class MockTree:
    pass

def test_visit_list_no_starred(mocker):
    # Create a mock for the _has_starred method to return False
    mocker.patch.object(StarredUnpackingTransformer, '_has_starred', return_value=False)
    
    # Create a sample AST List node without starred elements
    node = ast.List(elts=[ast.Constant(value=1), ast.Constant(value=2)], ctx=ast.Load())
    
    # Create a mock tree object
    mock_tree = MockTree()
    
    # Initialize the transformer with the mock tree
    transformer = StarredUnpackingTransformer(mock_tree)
    
    # Visit the node
    result = transformer.visit_List(node)
    
    # Assert that the result is the same node, as _has_starred returned False
    assert result == node
