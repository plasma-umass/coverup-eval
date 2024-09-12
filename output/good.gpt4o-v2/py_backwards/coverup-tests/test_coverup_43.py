# file: py_backwards/utils/snippet.py:50-52
# asked: {"lines": [50, 51, 52], "branches": []}
# gained: {"lines": [50, 51, 52], "branches": []}

import pytest
from typed_ast import ast3 as ast
from py_backwards.utils.snippet import VariablesReplacer

class TestVariablesReplacer:
    
    def test_visit_keyword(self, mocker):
        # Arrange
        variables = {}
        replacer = VariablesReplacer(variables)
        node = ast.keyword(arg='test', value=ast.Constant(value=42))
        
        # Mock _replace_field_or_node to return the node unmodified
        mocker.patch.object(replacer, '_replace_field_or_node', return_value=node)
        
        # Act
        result = replacer.visit_keyword(node)
        
        # Assert
        replacer._replace_field_or_node.assert_called_once_with(node, 'arg')
        assert result == node
