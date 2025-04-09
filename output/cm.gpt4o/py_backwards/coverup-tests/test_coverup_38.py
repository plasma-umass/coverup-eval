# file py_backwards/utils/snippet.py:46-48
# lines [46, 47, 48]
# branches []

import ast
import pytest
from py_backwards.utils.snippet import VariablesReplacer

def test_visit_attribute(mocker):
    # Create a mock for the 'variables' argument required by VariablesReplacer
    mock_variables = mocker.Mock()
    
    replacer = VariablesReplacer(mock_variables)
    
    # Mock the _replace_field_or_node method to ensure it is called
    mock_replace = mocker.patch.object(replacer, '_replace_field_or_node', return_value=ast.Attribute())
    
    # Create a sample Attribute node
    node = ast.Attribute(value=ast.Name(id='test', ctx=ast.Load()), attr='name', ctx=ast.Load())
    
    # Call the visit_Attribute method
    result = replacer.visit_Attribute(node)
    
    # Assert that _replace_field_or_node was called with the correct arguments
    mock_replace.assert_called_once_with(node, 'name')
    
    # Assert that the result is an instance of ast.Attribute
    assert isinstance(result, ast.Attribute)

    # Assert that the generic_visit method was called
    assert result is not node  # Ensure the node was transformed
