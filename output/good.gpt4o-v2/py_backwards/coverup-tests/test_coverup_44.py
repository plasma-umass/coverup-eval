# file: py_backwards/utils/snippet.py:72-74
# asked: {"lines": [72, 73, 74], "branches": []}
# gained: {"lines": [72, 73, 74], "branches": []}

import pytest
from typed_ast import ast3 as ast
from py_backwards.utils.snippet import VariablesReplacer

def test_visit_importfrom():
    replacer = VariablesReplacer({})
    
    # Create a mock ImportFrom node
    node = ast.ImportFrom(module='old_module', names=[], level=0)
    
    # Mock the _replace_module method to return a different module name
    replacer._replace_module = lambda module: 'new_module'
    
    # Visit the node
    new_node = replacer.visit_ImportFrom(node)
    
    # Assert the module name was replaced
    assert new_node.module == 'new_module'
    # Assert the node was visited generically
    assert isinstance(new_node, ast.ImportFrom)
