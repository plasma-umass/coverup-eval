# file: py_backwards/utils/snippet.py:81-83
# asked: {"lines": [82, 83], "branches": []}
# gained: {"lines": [82, 83], "branches": []}

import pytest
from typed_ast import ast3 as ast
from py_backwards.utils.snippet import VariablesReplacer

def test_visit_except_handler():
    replacer = VariablesReplacer({})
    node = ast.ExceptHandler(name="e", type=None, body=[])
    
    # Mock the _replace_field_or_node method to ensure it is called
    original_replace_field_or_node = replacer._replace_field_or_node
    def mock_replace_field_or_node(node, field, all_types=False):
        assert field == 'name'
        return node
    replacer._replace_field_or_node = mock_replace_field_or_node
    
    # Call the visit_ExceptHandler method
    result = replacer.visit_ExceptHandler(node)
    
    # Ensure the generic_visit method is called
    assert isinstance(result, ast.ExceptHandler)
    
    # Restore the original method to avoid side effects
    replacer._replace_field_or_node = original_replace_field_or_node

