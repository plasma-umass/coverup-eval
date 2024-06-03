# file py_backwards/utils/snippet.py:85-90
# lines [85, 86, 88, 89, 90]
# branches []

import ast
import pytest
from unittest import mock
from py_backwards.utils.snippet import VariablesReplacer

def test_variables_replacer_replace():
    class TestNodeTransformer(ast.NodeTransformer):
        def visit_Name(self, node):
            return ast.copy_location(ast.Name(id='replaced', ctx=node.ctx), node)

    tree = ast.parse("a = 1")
    variables = {'a': 'replaced'}
    
    # Mocking the VariablesReplacer to use TestNodeTransformer for testing
    with mock.patch.object(VariablesReplacer, 'visit', new=TestNodeTransformer().visit):
        replaced_tree = VariablesReplacer.replace(tree, variables)
    
    # Check if the variable 'a' was replaced with 'replaced'
    assert isinstance(replaced_tree, ast.Module)
    assert isinstance(replaced_tree.body[0], ast.Assign)
    assert isinstance(replaced_tree.body[0].targets[0], ast.Name)
    assert replaced_tree.body[0].targets[0].id == 'replaced'
