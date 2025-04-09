# file: py_backwards/utils/snippet.py:38-40
# asked: {"lines": [38, 39, 40], "branches": []}
# gained: {"lines": [38, 39, 40], "branches": []}

import pytest
from typed_ast import ast3 as ast
from py_backwards.utils.snippet import VariablesReplacer

@pytest.fixture
def variables_replacer():
    variables = {'x': 'y'}
    return VariablesReplacer(variables)

def test_visit_name(variables_replacer, mocker):
    node = ast.Name(id='x', ctx=ast.Load())
    mocker.patch.object(variables_replacer, '_replace_field_or_node', return_value=node)
    mocker.patch.object(variables_replacer, 'generic_visit', return_value=node)
    
    result = variables_replacer.visit_Name(node)
    
    variables_replacer._replace_field_or_node.assert_called_once_with(node, 'id', True)
    variables_replacer.generic_visit.assert_called_once_with(node)
    assert result == node
