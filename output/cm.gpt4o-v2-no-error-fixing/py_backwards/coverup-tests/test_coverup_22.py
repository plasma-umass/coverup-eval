# file: py_backwards/utils/snippet.py:58-60
# asked: {"lines": [58, 59, 60], "branches": []}
# gained: {"lines": [58, 59, 60], "branches": []}

import pytest
from typed_ast import ast3 as ast
from py_backwards.utils.snippet import VariablesReplacer

@pytest.fixture
def variables_replacer():
    return VariablesReplacer({})

def test_visit_arg(variables_replacer, mocker):
    node = ast.arg(arg='x', annotation=None)
    mocker.patch.object(variables_replacer, '_replace_field_or_node', return_value=node)
    mocker.patch.object(variables_replacer, 'generic_visit', return_value=node)
    
    result = variables_replacer.visit_arg(node)
    
    variables_replacer._replace_field_or_node.assert_called_once_with(node, 'arg')
    variables_replacer.generic_visit.assert_called_once_with(node)
    assert result == node
