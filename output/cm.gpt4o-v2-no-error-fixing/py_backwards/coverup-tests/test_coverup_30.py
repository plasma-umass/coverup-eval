# file: py_backwards/utils/snippet.py:46-48
# asked: {"lines": [47, 48], "branches": []}
# gained: {"lines": [47, 48], "branches": []}

import pytest
from typed_ast import ast3 as ast
from py_backwards.utils.snippet import VariablesReplacer

class MockVariable:
    def __init__(self, name):
        self.name = name

@pytest.fixture
def mock_variables():
    return {'mock_var': MockVariable('mock_var')}

def test_visit_attribute(mock_variables, mocker):
    replacer = VariablesReplacer(mock_variables)
    node = ast.Attribute(value=ast.Name(id='mock_var', ctx=ast.Load()), attr='mock_attr', ctx=ast.Load())

    mocker.patch.object(replacer, '_replace_field_or_node', return_value=node)
    mocker.patch.object(replacer, 'generic_visit', return_value=node)

    result = replacer.visit_Attribute(node)

    replacer._replace_field_or_node.assert_called_once_with(node, 'name')
    replacer.generic_visit.assert_called_once_with(node)
    assert result == node
