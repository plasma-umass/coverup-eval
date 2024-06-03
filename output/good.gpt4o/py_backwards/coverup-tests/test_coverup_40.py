# file py_backwards/utils/snippet.py:50-52
# lines [50, 51, 52]
# branches []

import ast
import pytest
from py_backwards.utils.snippet import VariablesReplacer

def test_visit_keyword(mocker):
    # Create a mock for the variables argument required by VariablesReplacer
    mock_variables = mocker.Mock()
    
    replacer = VariablesReplacer(mock_variables)
    
    # Mock the _replace_field_or_node method to ensure it is called
    mocker.patch.object(replacer, '_replace_field_or_node', return_value=ast.keyword(arg='test', value=None))
    
    # Create a sample ast.keyword node
    node = ast.keyword(arg='original', value=None)
    
    # Call the visit_keyword method
    result = replacer.visit_keyword(node)
    
    # Assert that _replace_field_or_node was called with the correct arguments
    replacer._replace_field_or_node.assert_called_once_with(node, 'arg')
    
    # Assert that the result is an ast.keyword node and the arg has been replaced
    assert isinstance(result, ast.keyword)
    assert result.arg == 'test'
