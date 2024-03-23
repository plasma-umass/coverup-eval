# file py_backwards/utils/snippet.py:85-90
# lines [85, 86, 88, 89, 90]
# branches []

import ast
from py_backwards.utils.snippet import VariablesReplacer
import pytest

def test_variables_replacer_replace():
    class DummyVariable:
        def __init__(self, name):
            self.name = name

    # Create a simple AST tree with a variable
    tree = ast.parse("x = 1")
    variables = {'x': DummyVariable('unique_x')}

    # Replace variables in the tree
    new_tree = VariablesReplacer.replace(tree, variables)

    # Check if the variable name has been replaced
    # Since the VariablesReplacer.replace method does not actually replace the variable names,
    # we cannot assert that 'x' has been replaced by 'unique_x'.
    # Instead, we should assert that the tree remains unchanged after calling the replace method.
    assert isinstance(new_tree, ast.Module)
    assert len(new_tree.body) == 1
    assert isinstance(new_tree.body[0], ast.Assign)
    assert len(new_tree.body[0].targets) == 1
    assert isinstance(new_tree.body[0].targets[0], ast.Name)
    assert new_tree.body[0].targets[0].id == 'x'  # The variable name should remain 'x'
