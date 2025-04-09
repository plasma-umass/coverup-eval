# file: py_backwards/utils/snippet.py:28-36
# asked: {"lines": [28, 29, 30, 31, 32, 33, 34, 36], "branches": [[30, 31], [30, 36], [31, 32], [31, 33], [33, 34], [33, 36]]}
# gained: {"lines": [28, 29, 30, 31, 32, 33, 34, 36], "branches": [[30, 31], [31, 32], [31, 33], [33, 34], [33, 36]]}

import ast
import pytest

from py_backwards.utils.snippet import VariablesReplacer

class TestVariablesReplacer:
    @pytest.fixture
    def replacer(self):
        class MockReplacer(VariablesReplacer):
            def __init__(self, variables):
                self._variables = variables

        return MockReplacer

    def test_replace_field_or_node_with_string(self, replacer):
        node = ast.Name(id='x')
        variables = {'x': 'y'}
        replacer_instance = replacer(variables)
        new_node = replacer_instance._replace_field_or_node(node, 'id')
        assert new_node.id == 'y'

    def test_replace_field_or_node_with_same_type(self, replacer):
        node = ast.Name(id='x')
        new_node = ast.Name(id='y')
        variables = {'x': new_node}
        replacer_instance = replacer(variables)
        result_node = replacer_instance._replace_field_or_node(node, 'id')
        assert result_node == new_node

    def test_replace_field_or_node_with_different_type_all_types(self, replacer):
        node = ast.Name(id='x')
        new_node = ast.Constant(value='y')
        variables = {'x': new_node}
        replacer_instance = replacer(variables)
        result_node = replacer_instance._replace_field_or_node(node, 'id', all_types=True)
        assert result_node == new_node

    def test_replace_field_or_node_with_different_type_no_all_types(self, replacer):
        node = ast.Name(id='x')
        new_node = ast.Constant(value='y')
        variables = {'x': new_node}
        replacer_instance = replacer(variables)
        result_node = replacer_instance._replace_field_or_node(node, 'id', all_types=False)
        assert result_node == node
