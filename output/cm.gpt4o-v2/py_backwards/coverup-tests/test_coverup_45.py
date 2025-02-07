# file: py_backwards/transformers/python2_future.py:14-27
# asked: {"lines": [14, 15, 22, 24, 25, 26, 27], "branches": []}
# gained: {"lines": [14, 15, 22, 24, 25, 26, 27], "branches": []}

import pytest
from typed_ast import ast3 as ast
from py_backwards.transformers.python2_future import Python2FutureTransformer

@pytest.fixture
def transformer():
    tree = ast.Module(body=[])
    return Python2FutureTransformer(tree)

def test_visit_module(transformer, mocker):
    # Create a mock node
    node = ast.Module(body=[])
    
    # Mock the imports.get_body function
    mock_get_body = mocker.patch('py_backwards.transformers.python2_future.imports.get_body', return_value=[ast.ImportFrom(module='__future__', names=[ast.alias(name='absolute_import', asname=None)], level=0)])
    
    # Call the visit_Module method
    result = transformer.visit_Module(node)
    
    # Assertions to verify the behavior
    assert transformer._tree_changed is True
    assert len(result.body) == 1
    assert isinstance(result.body[0], ast.ImportFrom)
    assert result.body[0].module == '__future__'
    assert result.body[0].names[0].name == 'absolute_import'
    
    # Ensure the mock was called as expected
    mock_get_body.assert_called_once_with(future='__future__')
