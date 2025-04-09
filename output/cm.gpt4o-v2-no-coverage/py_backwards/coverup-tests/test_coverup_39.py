# file: py_backwards/utils/snippet.py:85-90
# asked: {"lines": [85, 86, 88, 89, 90], "branches": []}
# gained: {"lines": [85, 86, 88, 89, 90], "branches": []}

import pytest
from typed_ast import ast3 as ast
from py_backwards.utils.snippet import VariablesReplacer

class Variable:
    def __init__(self, name):
        self.name = name

def test_replace():
    # Create a simple AST tree
    tree = ast.parse("x = 1")
    variables = {"x": "y"}

    # Replace variables in the tree
    new_tree = VariablesReplacer.replace(tree, variables)

    # Assert that the tree is still an AST node
    assert isinstance(new_tree, ast.AST)

    # Assert that the variable name has been replaced
    assert new_tree.body[0].targets[0].id == "y"

    # Clean up
    del tree
    del variables
    del new_tree
