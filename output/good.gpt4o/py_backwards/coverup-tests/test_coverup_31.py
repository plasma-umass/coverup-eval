# file py_backwards/utils/snippet.py:58-60
# lines [58, 59, 60]
# branches []

import ast
import pytest
from py_backwards.utils.snippet import VariablesReplacer

def test_visit_arg(mocker):
    # Mock the variables argument required by VariablesReplacer
    mock_variables = mocker.Mock()
    
    replacer = VariablesReplacer(mock_variables)
    
    # Mock the _replace_field_or_node method to ensure it is called
    mock_replace = mocker.patch.object(replacer, '_replace_field_or_node', return_value=ast.arg(arg='replaced', annotation=None))
    
    # Create a sample ast.arg node
    node = ast.arg(arg='original', annotation=None)
    
    # Call visit_arg
    result = replacer.visit_arg(node)
    
    # Assertions to verify the behavior
    mock_replace.assert_called_once_with(node, 'arg')
    assert isinstance(result, ast.arg)
    assert result.arg == 'replaced'
    assert result.annotation is None
