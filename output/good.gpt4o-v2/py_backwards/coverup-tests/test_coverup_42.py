# file: py_backwards/utils/snippet.py:58-60
# asked: {"lines": [58, 59, 60], "branches": []}
# gained: {"lines": [58, 59, 60], "branches": []}

import pytest
from typed_ast import ast3 as ast
from py_backwards.utils.snippet import VariablesReplacer

def test_visit_arg():
    replacer = VariablesReplacer({})
    arg_node = ast.arg(arg='x', annotation=None)
    
    # Mock the _replace_field_or_node method to return the node as is
    replacer._replace_field_or_node = lambda node, field: node
    
    result = replacer.visit_arg(arg_node)
    
    assert isinstance(result, ast.arg)
    assert result.arg == 'x'
    assert result.annotation is None
