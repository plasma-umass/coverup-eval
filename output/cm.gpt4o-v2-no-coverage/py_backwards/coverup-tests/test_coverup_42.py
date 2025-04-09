# file: py_backwards/utils/snippet.py:81-83
# asked: {"lines": [81, 82, 83], "branches": []}
# gained: {"lines": [81, 82, 83], "branches": []}

import pytest
from typed_ast import ast3 as ast
from py_backwards.utils.snippet import VariablesReplacer

@pytest.fixture
def mock_replace_field_or_node(mocker):
    return mocker.patch.object(VariablesReplacer, '_replace_field_or_node', return_value=ast.ExceptHandler())

def test_visit_ExceptHandler(mock_replace_field_or_node):
    replacer = VariablesReplacer({})
    node = ast.ExceptHandler()
    result = replacer.visit_ExceptHandler(node)
    
    mock_replace_field_or_node.assert_called_once_with(node, 'name')
    assert isinstance(result, ast.ExceptHandler)
