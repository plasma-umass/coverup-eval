# file py_backwards/transformers/starred_unpacking.py:66-72
# lines [66, 67, 68, 70, 72]
# branches ['67->68', '67->70']

import ast
import pytest
from py_backwards.transformers.starred_unpacking import StarredUnpackingTransformer

class MockTree:
    pass

def test_starred_unpacking_transformer(mocker):
    mock_tree = MockTree()
    transformer = StarredUnpackingTransformer(mock_tree)

    # Mocking the _has_starred method to return True
    mocker.patch.object(transformer, '_has_starred', return_value=True)
    
    # Mocking the _to_sum_of_lists method to return a new AST node
    mocker.patch.object(transformer, '_to_sum_of_lists', return_value=ast.List(elts=[], ctx=ast.Load()))

    # Creating a sample AST node with a list
    node = ast.List(elts=[ast.Starred(value=ast.Name(id='a', ctx=ast.Load()), ctx=ast.Load())], ctx=ast.Load())

    # Visit the node
    result = transformer.visit_List(node)

    # Assertions to verify the postconditions
    assert isinstance(result, ast.List)
    assert transformer._tree_changed is True

    # Clean up by unpatching
    mocker.stopall()
