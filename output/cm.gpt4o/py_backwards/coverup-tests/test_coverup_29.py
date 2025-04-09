# file py_backwards/transformers/starred_unpacking.py:74-82
# lines [74, 75, 76, 78, 80, 81, 82]
# branches ['75->76', '75->78']

import ast
import pytest
from py_backwards.transformers.starred_unpacking import StarredUnpackingTransformer
from py_backwards.transformers.base import BaseNodeTransformer
from typed_ast import ast3

class MockTree:
    pass

def test_starred_unpacking_transformer(mocker):
    # Mock the _has_starred method to return True
    mocker.patch.object(StarredUnpackingTransformer, '_has_starred', return_value=True)
    
    # Mock the _to_sum_of_lists method to return a list of arguments
    mocker.patch.object(StarredUnpackingTransformer, '_to_sum_of_lists', return_value=[ast3.Constant(value=1), ast3.Constant(value=2)])
    
    # Create a mock tree object
    mock_tree = MockTree()
    
    transformer = StarredUnpackingTransformer(mock_tree)
    
    # Create a sample AST node for testing
    node = ast3.Call(
        func=ast3.Name(id='func', ctx=ast3.Load()),
        args=[ast3.Constant(value=1), ast3.Constant(value=2)],
        keywords=[]
    )
    
    # Transform the node
    new_node = transformer.visit_Call(node)
    
    # Assertions to verify the transformation
    assert isinstance(new_node, ast3.Call)
    assert len(new_node.args) == 1
    assert isinstance(new_node.args[0], ast3.Starred)
    assert isinstance(new_node.args[0].value, list)
    assert len(new_node.args[0].value) == 2
    assert new_node.args[0].value[0].value == 1
    assert new_node.args[0].value[1].value == 2
    assert transformer._tree_changed

    # Clean up the mocks
    mocker.stopall()
