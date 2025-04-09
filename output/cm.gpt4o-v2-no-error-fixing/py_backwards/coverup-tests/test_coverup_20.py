# file: py_backwards/utils/snippet.py:85-90
# asked: {"lines": [85, 86, 88, 89, 90], "branches": []}
# gained: {"lines": [85, 86, 88, 89, 90], "branches": []}

import pytest
from typed_ast import ast3 as ast
from py_backwards.utils.snippet import VariablesReplacer

def test_replace_method():
    # Create a simple AST tree
    tree = ast.parse("x = 1")
    
    # Define variables to replace
    variables = {"x": "y"}
    
    # Call the replace method
    new_tree = VariablesReplacer.replace(tree, variables)
    
    # Assert the tree is the same instance (since replace method returns the same tree)
    assert new_tree is tree
    
    # Assert the tree has been visited and modified
    assert isinstance(new_tree, ast.Module)
    assert isinstance(new_tree.body[0], ast.Assign)
    assert isinstance(new_tree.body[0].targets[0], ast.Name)
    assert new_tree.body[0].targets[0].id == "y"

