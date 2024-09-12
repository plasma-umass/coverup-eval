# file: py_backwards/utils/snippet.py:28-36
# asked: {"lines": [28, 29, 30, 31, 32, 33, 34, 36], "branches": [[30, 31], [30, 36], [31, 32], [31, 33], [33, 34], [33, 36]]}
# gained: {"lines": [28, 29, 30, 31, 32, 33, 34, 36], "branches": [[30, 31], [30, 36], [31, 32], [31, 33], [33, 34]]}

import ast
import pytest

from py_backwards.utils.snippet import VariablesReplacer

class TestVariablesReplacer:
    @pytest.fixture
    def replacer(self):
        class MockVariablesReplacer(VariablesReplacer):
            def __init__(self, variables):
                self._variables = variables

        return MockVariablesReplacer

    def test_replace_field_or_node_with_string(self, replacer):
        variables = {'test_field': 'new_value'}
        node = ast.Name(id='test_field')
        replacer_instance = replacer(variables)
        
        result = replacer_instance._replace_field_or_node(node, 'id')
        
        assert node.id == 'new_value'
        assert result == node

    def test_replace_field_or_node_with_node(self, replacer):
        variables = {'test_field': ast.Name(id='new_node')}
        node = ast.Name(id='test_field')
        replacer_instance = replacer(variables)
        
        result = replacer_instance._replace_field_or_node(node, 'id')
        
        assert result == variables['test_field']

    def test_replace_field_or_node_with_all_types(self, replacer):
        variables = {'test_field': ast.Constant(value=42)}
        node = ast.Name(id='test_field')
        replacer_instance = replacer(variables)
        
        result = replacer_instance._replace_field_or_node(node, 'id', all_types=True)
        
        assert result == variables['test_field']

    def test_replace_field_or_node_no_replacement(self, replacer):
        variables = {'other_field': 'new_value'}
        node = ast.Name(id='test_field')
        replacer_instance = replacer(variables)
        
        result = replacer_instance._replace_field_or_node(node, 'id')
        
        assert node.id == 'test_field'
        assert result == node
