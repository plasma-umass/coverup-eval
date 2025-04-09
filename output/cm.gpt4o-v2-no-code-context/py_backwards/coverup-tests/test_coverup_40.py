# file: py_backwards/utils/snippet.py:54-56
# asked: {"lines": [54, 55, 56], "branches": []}
# gained: {"lines": [54, 55, 56], "branches": []}

import ast
import pytest

from py_backwards.utils.snippet import VariablesReplacer

def test_visit_ClassDef(monkeypatch):
    class MockNode:
        def __init__(self, name):
            self.name = name

    def mock_replace_field_or_node(self, node, field_name):
        assert field_name == 'name'
        node.name = 'ReplacedName'
        return node

    monkeypatch.setattr(VariablesReplacer, '_replace_field_or_node', mock_replace_field_or_node)

    replacer = VariablesReplacer(variables={})
    class_node = ast.ClassDef(name='OriginalName', bases=[], keywords=[], body=[], decorator_list=[])
    result_node = replacer.visit_ClassDef(class_node)

    assert isinstance(result_node, ast.ClassDef)
    assert result_node.name == 'ReplacedName'
