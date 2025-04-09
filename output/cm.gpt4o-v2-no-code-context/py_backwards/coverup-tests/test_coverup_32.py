# file: py_backwards/utils/snippet.py:42-44
# asked: {"lines": [42, 43, 44], "branches": []}
# gained: {"lines": [42, 43, 44], "branches": []}

import ast
import pytest

from py_backwards.utils.snippet import VariablesReplacer

def test_visit_functiondef_replaces_name(monkeypatch):
    class MockVariablesReplacer(VariablesReplacer):
        def __init__(self):
            pass

    replacer = MockVariablesReplacer()

    def mock_replace_field_or_node(self, node, field_name):
        if field_name == 'name':
            node.name = 'replaced_name'
        return node

    monkeypatch.setattr(MockVariablesReplacer, '_replace_field_or_node', mock_replace_field_or_node)

    func_def_node = ast.FunctionDef(name='original_name', args=None, body=[], decorator_list=[])
    result_node = replacer.visit_FunctionDef(func_def_node)

    assert isinstance(result_node, ast.FunctionDef)
    assert result_node.name == 'replaced_name'
