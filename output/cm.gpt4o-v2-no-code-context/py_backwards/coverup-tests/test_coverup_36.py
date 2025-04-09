# file: py_backwards/utils/snippet.py:46-48
# asked: {"lines": [46, 47, 48], "branches": []}
# gained: {"lines": [46, 47, 48], "branches": []}

import ast
import pytest

from py_backwards.utils.snippet import VariablesReplacer

class TestVariablesReplacer:
    def test_visit_attribute(self, mocker):
        # Create a mock for the _replace_field_or_node method
        replacer = VariablesReplacer(variables={})
        mock_replace = mocker.patch.object(replacer, '_replace_field_or_node', return_value=ast.Attribute())

        # Create a sample Attribute node
        node = ast.Attribute(value=ast.Name(id='test', ctx=ast.Load()), attr='name', ctx=ast.Load())

        # Call the visit_Attribute method
        result = replacer.visit_Attribute(node)

        # Assertions to verify the behavior
        mock_replace.assert_called_once_with(node, 'name')
        assert isinstance(result, ast.Attribute)

        # Ensure the node was visited
        assert result is not node  # Ensure the node was transformed

        # Clean up
        mock_replace.stop()
