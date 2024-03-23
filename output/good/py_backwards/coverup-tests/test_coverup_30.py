# file py_backwards/utils/snippet.py:58-60
# lines [58, 59, 60]
# branches []

import ast
from py_backwards.utils.snippet import VariablesReplacer
import pytest

# Test function to cover visit_arg method
def test_visit_arg(mocker):
    # Create a sample ast.arg node
    sample_arg = ast.arg(arg='x', annotation=None)

    # Mock the _replace_field_or_node method to check if it's called with correct arguments
    mock_replace_field_or_node = mocker.patch.object(
        VariablesReplacer, '_replace_field_or_node', return_value=sample_arg
    )

    # Create a VariablesReplacer instance with a dummy variables dictionary
    replacer = VariablesReplacer(variables={})

    # Visit the sample_arg node
    visited = replacer.visit_arg(sample_arg)

    # Assertions to ensure the visit_arg method is working as expected
    assert isinstance(visited, ast.arg), "The result should be an ast.arg instance"
    assert visited.arg == 'x', "The arg attribute should remain unchanged"

    # Assert that _replace_field_or_node was called correctly
    mock_replace_field_or_node.assert_called_once_with(sample_arg, 'arg')

    # Clean up by deleting the replacer instance
    del replacer

# Run the test
def test_variables_replacer(mocker):
    test_visit_arg(mocker)
