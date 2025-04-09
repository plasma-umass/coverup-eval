# file: py_backwards/utils/snippet.py:46-48
# asked: {"lines": [46, 47, 48], "branches": []}
# gained: {"lines": [46, 47, 48], "branches": []}

import pytest
from typed_ast import ast3 as ast
from py_backwards.utils.snippet import VariablesReplacer

class TestVariablesReplacer:
    @pytest.fixture
    def replacer(self):
        class MockVariablesReplacer(VariablesReplacer):
            def __init__(self, variables):
                self._variables = variables

        return MockVariablesReplacer

    def test_visit_attribute(self, replacer):
        variables = {'test': ast.Name(id='new_test', ctx=ast.Load())}
        node = ast.Attribute(value=ast.Name(id='test', ctx=ast.Load()), attr='name', ctx=ast.Load())
        replacer_instance = replacer(variables)
        
        result_node = replacer_instance.visit_Attribute(node)
        
        assert result_node.value.id == 'new_test'
        assert isinstance(result_node, ast.Attribute)

    def test_replace_field_or_node(self, replacer):
        variables = {'name': 'new_name'}
        node = ast.Attribute(value=ast.Name(id='test', ctx=ast.Load()), attr='name', ctx=ast.Load())
        replacer_instance = replacer(variables)
        
        result_node = replacer_instance._replace_field_or_node(node, 'attr')
        
        assert result_node.attr == 'new_name'
        assert isinstance(result_node, ast.Attribute)
