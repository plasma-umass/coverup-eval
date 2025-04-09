# file py_backwards/utils/snippet.py:28-36
# lines [28, 29, 30, 31, 32, 33, 34, 36]
# branches ['30->31', '30->36', '31->32', '31->33', '33->34', '33->36']

import ast
import pytest
from py_backwards.utils.snippet import VariablesReplacer

@pytest.fixture
def variables_replacer():
    return VariablesReplacer(variables={})

@pytest.fixture
def mock_variables(variables_replacer):
    return variables_replacer._variables

def test_replace_field_with_string(variables_replacer, mock_variables):
    mock_variables['old_value'] = 'new_value'
    node = ast.Name(id='old_value', ctx=ast.Load())
    result = variables_replacer._replace_field_or_node(node, 'id')
    assert result.id == 'new_value'

def test_replace_node_with_same_type(variables_replacer, mock_variables):
    new_node = ast.Name(id='new_value', ctx=ast.Load())
    mock_variables['old_value'] = new_node
    node = ast.Name(id='old_value', ctx=ast.Load())
    result = variables_replacer._replace_field_or_node(node, 'id', all_types=True)
    assert result is new_node

def test_replace_node_with_different_type_not_allowed(variables_replacer, mock_variables):
    new_node = ast.Str(s='new_value')
    mock_variables['old_value'] = new_node
    node = ast.Name(id='old_value', ctx=ast.Load())
    result = variables_replacer._replace_field_or_node(node, 'id')
    assert result is not new_node
    assert isinstance(result, ast.Name)
    assert result.id == 'old_value'

def test_replace_node_with_different_type_allowed(variables_replacer, mock_variables):
    new_node = ast.Str(s='new_value')
    mock_variables['old_value'] = new_node
    node = ast.Name(id='old_value', ctx=ast.Load())
    result = variables_replacer._replace_field_or_node(node, 'id', all_types=True)
    assert result is new_node
