# file py_backwards/transformers/starred_unpacking.py:74-82
# lines [76]
# branches ['75->76']

import ast
import pytest
from py_backwards.transformers.starred_unpacking import StarredUnpackingTransformer
from py_backwards.transformers.base import BaseNodeTransformer

class MockTree:
    pass

def test_visit_call_no_starred(mocker):
    # Create a mock node without starred arguments
    node = ast.Call(func=ast.Name(id='func', ctx=ast.Load()), args=[ast.Constant(value=1)], keywords=[])
    
    # Mock the _has_starred method to return False
    transformer = StarredUnpackingTransformer(MockTree())
    mocker.patch.object(transformer, '_has_starred', return_value=False)
    
    # Mock the generic_visit method to return the node itself
    mocker.patch.object(transformer, 'generic_visit', return_value=node)
    
    # Call visit_Call and assert the return value
    result = transformer.visit_Call(node)
    assert result == node
