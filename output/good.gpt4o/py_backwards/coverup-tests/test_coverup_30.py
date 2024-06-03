# file py_backwards/utils/snippet.py:38-40
# lines [38, 39, 40]
# branches []

import ast
import pytest
from py_backwards.utils.snippet import VariablesReplacer

def test_variables_replacer_visit_name(mocker):
    # Create a mock for the _replace_field_or_node method
    replacer = VariablesReplacer(variables={})
    mock_replace = mocker.patch.object(replacer, '_replace_field_or_node', return_value=ast.Name(id='replaced', ctx=ast.Load()))

    # Create a sample AST node
    node = ast.Name(id='original', ctx=ast.Load())

    # Visit the node
    result = replacer.visit_Name(node)

    # Assertions to verify the behavior
    mock_replace.assert_called_once_with(node, 'id', True)
    assert isinstance(result, ast.Name)
    assert result.id == 'replaced'

    # Ensure the node was visited
    assert result is not node
