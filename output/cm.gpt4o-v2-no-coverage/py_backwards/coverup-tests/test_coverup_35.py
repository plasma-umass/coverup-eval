# file: py_backwards/utils/snippet.py:38-40
# asked: {"lines": [38, 39, 40], "branches": []}
# gained: {"lines": [38, 39, 40], "branches": []}

import pytest
from typed_ast import ast3 as ast
from py_backwards.utils.snippet import VariablesReplacer

@pytest.fixture
def variables_replacer():
    variables = {'x': 'y', 'a': 'b'}
    return VariablesReplacer(variables)

def test_visit_name_replaces_variable(variables_replacer):
    node = ast.Name(id='x', ctx=ast.Load())
    new_node = variables_replacer.visit_Name(node)
    assert new_node.id == 'y'

def test_visit_name_does_not_replace_variable(variables_replacer):
    node = ast.Name(id='z', ctx=ast.Load())
    new_node = variables_replacer.visit_Name(node)
    assert new_node.id == 'z'
