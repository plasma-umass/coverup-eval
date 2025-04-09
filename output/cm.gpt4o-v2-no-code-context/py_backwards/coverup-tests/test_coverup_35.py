# file: py_backwards/utils/snippet.py:58-60
# asked: {"lines": [58, 59, 60], "branches": []}
# gained: {"lines": [58, 59, 60], "branches": []}

import ast
import pytest

from py_backwards.utils.snippet import VariablesReplacer

def test_visit_arg():
    replacer = VariablesReplacer(variables={})
    arg_node = ast.arg(arg='x', annotation=None)
    
    # Mock the _replace_field_or_node method to ensure it gets called
    original_replace_field_or_node = replacer._replace_field_or_node
    def mock_replace_field_or_node(node, field_name):
        assert field_name == 'arg'
        return node
    replacer._replace_field_or_node = mock_replace_field_or_node
    
    result_node = replacer.visit_arg(arg_node)
    
    # Ensure the node returned is the same as the one passed in
    assert result_node is arg_node
    
    # Restore the original method to avoid side effects
    replacer._replace_field_or_node = original_replace_field_or_node
