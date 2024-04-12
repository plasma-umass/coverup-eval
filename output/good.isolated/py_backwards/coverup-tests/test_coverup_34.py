# file py_backwards/utils/snippet.py:38-40
# lines [38, 39, 40]
# branches []

import ast
import pytest
from py_backwards.utils.snippet import VariablesReplacer

@pytest.fixture
def variables_replacer():
    return VariablesReplacer(variables={})

def test_visit_name_replacement(variables_replacer, mocker):
    # Mock the _replace_field_or_node method to control its behavior
    mocker.patch.object(variables_replacer, '_replace_field_or_node', side_effect=lambda node, field, is_identifier: ast.Name(id='replaced_name', ctx=node.ctx))

    # Create a simple Name node
    name_node = ast.Name(id='original_name', ctx=ast.Load())

    # Visit the node with the VariablesReplacer
    result_node = variables_replacer.visit_Name(name_node)

    # Assert that the _replace_field_or_node method was called correctly
    variables_replacer._replace_field_or_node.assert_called_once_with(name_node, 'id', True)

    # Assert that the result is an ast.Name instance and the id has been replaced
    assert isinstance(result_node, ast.Name)
    assert result_node.id == 'replaced_name'
