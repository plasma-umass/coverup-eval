# file: py_backwards/utils/snippet.py:50-52
# asked: {"lines": [50, 51, 52], "branches": []}
# gained: {"lines": [50, 51, 52], "branches": []}

import ast
import pytest
from py_backwards.utils.snippet import VariablesReplacer

class TestVariablesReplacer:
    def test_visit_keyword(self):
        # Create a dummy variables dictionary to pass to the VariablesReplacer
        variables = {'test_var': 'replacement'}
        replacer = VariablesReplacer(variables)
        
        keyword_node = ast.keyword(arg='test_arg', value=ast.Constant(value=42))
        
        # Mock the _replace_field_or_node method to ensure it gets called
        original_replace_field_or_node = replacer._replace_field_or_node
        def mock_replace_field_or_node(node, field):
            assert node is keyword_node
            assert field == 'arg'
            return node
        replacer._replace_field_or_node = mock_replace_field_or_node
        
        # Visit the keyword node
        result_node = replacer.visit_keyword(keyword_node)
        
        # Ensure the result node is the same as the input node
        assert result_node is keyword_node
        
        # Restore the original method to avoid side effects
        replacer._replace_field_or_node = original_replace_field_or_node
