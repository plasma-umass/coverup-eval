# file: py_backwards/utils/snippet.py:38-40
# asked: {"lines": [38, 39, 40], "branches": []}
# gained: {"lines": [38, 39, 40], "branches": []}

import ast
import pytest

from py_backwards.utils.snippet import VariablesReplacer

class TestVariablesReplacer:
    def test_visit_name(self, mocker):
        # Mock the variables argument required by VariablesReplacer
        mock_variables = mocker.MagicMock()
        replacer = VariablesReplacer(mock_variables)
        
        # Mock the _replace_field_or_node method to ensure it is called
        mock_replace = mocker.patch.object(replacer, '_replace_field_or_node', return_value=ast.Name(id='replaced', ctx=ast.Load()))
        
        # Create a sample ast.Name node
        node = ast.Name(id='original', ctx=ast.Load())
        
        # Call the visit_Name method
        result = replacer.visit_Name(node)
        
        # Assert that _replace_field_or_node was called with the correct arguments
        mock_replace.assert_called_once_with(node, 'id', True)
        
        # Assert that the result is an ast.Name node with the id 'replaced'
        assert isinstance(result, ast.Name)
        assert result.id == 'replaced'
