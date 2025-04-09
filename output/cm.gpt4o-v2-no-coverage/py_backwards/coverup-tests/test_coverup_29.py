# file: py_backwards/utils/snippet.py:76-79
# asked: {"lines": [76, 77, 78, 79], "branches": []}
# gained: {"lines": [76, 77, 78, 79], "branches": []}

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

    def test_visit_alias(self, replacer):
        variables = {
            'old_module': 'new_module',
            'old_name': 'new_name'
        }
        replacer_instance = replacer(variables)
        alias_node = ast.alias(name='old_module', asname='old_name')

        result_node = replacer_instance.visit_alias(alias_node)

        assert result_node.name == 'new_module'
        assert result_node.asname == 'new_name'

    def test_replace_module(self, replacer):
        variables = {
            'old_module': 'new_module'
        }
        replacer_instance = replacer(variables)

        result = replacer_instance._replace_module('old_module')

        assert result == 'new_module'

    def test_replace_field_or_node(self, replacer):
        variables = {
            'old_name': 'new_name'
        }
        replacer_instance = replacer(variables)
        alias_node = ast.alias(name='module', asname='old_name')

        result_node = replacer_instance._replace_field_or_node(alias_node, 'asname')

        assert result_node.asname == 'new_name'
