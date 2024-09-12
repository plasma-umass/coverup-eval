# file: py_backwards/utils/snippet.py:76-79
# asked: {"lines": [76, 77, 78, 79], "branches": []}
# gained: {"lines": [76, 77, 78, 79], "branches": []}

import pytest
from typed_ast import ast3 as ast
from py_backwards.utils.snippet import VariablesReplacer

@pytest.fixture
def variables_replacer():
    variables = {}  # Add any necessary variable mappings here
    return VariablesReplacer(variables)

def test_visit_alias(variables_replacer, mocker):
    alias_node = ast.alias(name='original_name', asname='original_asname')
    
    mocker.patch.object(variables_replacer, '_replace_module', return_value='replaced_name')
    mocker.patch.object(variables_replacer, '_replace_field_or_node', return_value=alias_node)
    mocker.patch.object(variables_replacer, 'generic_visit', return_value=alias_node)
    
    result = variables_replacer.visit_alias(alias_node)
    
    variables_replacer._replace_module.assert_called_once_with('original_name')
    variables_replacer._replace_field_or_node.assert_called_once_with(alias_node, 'asname')
    variables_replacer.generic_visit.assert_called_once_with(alias_node)
    
    assert result == alias_node
