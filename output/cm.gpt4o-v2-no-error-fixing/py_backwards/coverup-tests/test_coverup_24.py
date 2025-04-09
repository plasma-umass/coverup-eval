# file: py_backwards/utils/snippet.py:42-44
# asked: {"lines": [42, 43, 44], "branches": []}
# gained: {"lines": [42, 43, 44], "branches": []}

import pytest
from typed_ast import ast3 as ast
from py_backwards.utils.snippet import VariablesReplacer

@pytest.fixture
def mock_replace_field_or_node(mocker):
    return mocker.patch.object(VariablesReplacer, '_replace_field_or_node', return_value=ast.FunctionDef(name='mocked_name', args=None, body=[], decorator_list=[]))

def test_visit_FunctionDef(mock_replace_field_or_node):
    replacer = VariablesReplacer({})
    node = ast.FunctionDef(name='test', args=None, body=[], decorator_list=[])
    result = replacer.visit_FunctionDef(node)
    
    mock_replace_field_or_node.assert_called_once_with(node, 'name')
    assert isinstance(result, ast.FunctionDef)
    assert result.name == 'mocked_name'
