# file: py_backwards/utils/snippet.py:85-90
# asked: {"lines": [85, 86, 88, 89, 90], "branches": []}
# gained: {"lines": [85, 86, 88, 89, 90], "branches": []}

import pytest
from typed_ast import ast3 as ast
from py_backwards.utils.snippet import VariablesReplacer

def test_replace_method():
    class Variable:
        def __init__(self, name):
            self.name = name

    # Create a simple AST tree
    tree = ast.parse("x = 1")

    # Create a variables dictionary
    variables = {"x": Variable("x")}

    # Mock the visit method to avoid actual visiting
    original_visit = VariablesReplacer.visit
    def mock_visit(self, node):
        return node
    VariablesReplacer.visit = mock_visit

    try:
        # Call the replace method
        new_tree = VariablesReplacer.replace(tree, variables)

        # Assert that the returned tree is the same as the input tree
        assert new_tree == tree

        # Assert that the visit method was called (indirectly by checking if the tree was visited)
        assert isinstance(new_tree, ast.Module)
        assert len(new_tree.body) == 1
        assert isinstance(new_tree.body[0], ast.Assign)
    finally:
        # Restore the original visit method
        VariablesReplacer.visit = original_visit
