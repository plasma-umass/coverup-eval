# file: py_backwards/utils/snippet.py:58-60
# asked: {"lines": [58, 59, 60], "branches": []}
# gained: {"lines": [58, 59, 60], "branches": []}

import pytest
from typed_ast import ast3 as ast
from py_backwards.utils.snippet import VariablesReplacer

class TestVariablesReplacer:
    @pytest.fixture
    def replacer(self):
        return VariablesReplacer(variables={})

    def test_visit_arg(self, replacer, mocker):
        node = ast.arg(arg='x', annotation=None)
        mocker.patch.object(replacer, '_replace_field_or_node', return_value=node)
        mocker.patch.object(replacer, 'generic_visit', return_value=node)
        
        result = replacer.visit_arg(node)
        
        replacer._replace_field_or_node.assert_called_once_with(node, 'arg')
        replacer.generic_visit.assert_called_once_with(node)
        assert result == node

    def test_replace_field_or_node(self, replacer):
        node = ast.arg(arg='x', annotation=None)
        replacer._variables = {'x': 'y'}
        
        result = replacer._replace_field_or_node(node, 'arg')
        
        assert node.arg == 'y'
        assert result == node

    def test_replace_field_or_node_with_type(self, replacer):
        node = ast.arg(arg='x', annotation=None)
        new_node = ast.arg(arg='y', annotation=None)
        replacer._variables = {'x': new_node}
        
        result = replacer._replace_field_or_node(node, 'arg')
        
        assert result == new_node
