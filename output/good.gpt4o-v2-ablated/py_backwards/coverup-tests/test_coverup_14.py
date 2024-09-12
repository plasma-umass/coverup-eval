# file: py_backwards/utils/snippet.py:28-36
# asked: {"lines": [], "branches": [[33, 36]]}
# gained: {"lines": [], "branches": [[33, 36]]}

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
        node = ast.Name(id='x')
        variables = {'x': 'y'}
        replacer_instance = replacer(variables)
        result = replacer_instance._replace_field_or_node(node, 'id')
        assert node.id == 'y'
        assert result == node

    def test_replace_field_or_node_with_same_type(self, replacer):
        node = ast.Name(id='x')
        new_node = ast.Name(id='y')
        variables = {'x': new_node}
        replacer_instance = replacer(variables)
        result = replacer_instance._replace_field_or_node(node, 'id')
        assert result == new_node

    def test_replace_field_or_node_with_different_type_all_types_true(self, replacer):
        node = ast.Name(id='x')
        new_node = ast.Constant(value='y')
        variables = {'x': new_node}
        replacer_instance = replacer(variables)
        result = replacer_instance._replace_field_or_node(node, 'id', all_types=True)
        assert result == new_node

    def test_replace_field_or_node_with_different_type_all_types_false(self, replacer):
        node = ast.Name(id='x')
        new_node = ast.Constant(value='y')
        variables = {'x': new_node}
        replacer_instance = replacer(variables)
        result = replacer_instance._replace_field_or_node(node, 'id', all_types=False)
        assert result == node

    def test_replace_field_or_node_no_replacement(self, replacer):
        node = ast.Name(id='x')
        variables = {'y': 'z'}
        replacer_instance = replacer(variables)
        result = replacer_instance._replace_field_or_node(node, 'id')
        assert result == node
