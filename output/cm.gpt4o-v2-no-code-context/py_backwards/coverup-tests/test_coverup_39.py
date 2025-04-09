# file: py_backwards/utils/snippet.py:81-83
# asked: {"lines": [81, 82, 83], "branches": []}
# gained: {"lines": [81, 82, 83], "branches": []}

import ast
import pytest

from py_backwards.utils.snippet import VariablesReplacer

def test_visit_ExceptHandler(monkeypatch):
    # Create a sample AST node for ExceptHandler
    except_handler_node = ast.ExceptHandler(name='e', type=None, body=[])
    
    # Mock the _replace_field_or_node method to ensure it gets called
    def mock_replace_field_or_node(self, node, field):
        assert node is except_handler_node
        assert field == 'name'
        return node
    
    # Apply the monkeypatch to replace the method
    monkeypatch.setattr(VariablesReplacer, "_replace_field_or_node", mock_replace_field_or_node)
    
    # Create an instance of VariablesReplacer with a dummy 'variables' argument
    replacer = VariablesReplacer(variables={})
    
    # Visit the ExceptHandler node
    result_node = replacer.visit_ExceptHandler(except_handler_node)
    
    # Ensure the result node is the same as the input node
    assert result_node is except_handler_node
