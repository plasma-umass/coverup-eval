# file: py_backwards/utils/snippet.py:42-44
# asked: {"lines": [42, 43, 44], "branches": []}
# gained: {"lines": [42, 43, 44], "branches": []}

import pytest
from typed_ast import ast3 as ast
from py_backwards.utils.snippet import VariablesReplacer

@pytest.fixture
def variables_replacer():
    variables = {'old_name': 'new_name'}
    replacer = VariablesReplacer(variables)
    return replacer

def test_visit_FunctionDef(variables_replacer):
    # Create a mock FunctionDef node
    func_def = ast.FunctionDef(name='old_name', args=None, body=[], decorator_list=[])
    
    # Visit the node
    new_node = variables_replacer.visit_FunctionDef(func_def)
    
    # Assert the name has been replaced
    assert new_node.name == 'new_name'

    # Assert the node is still a FunctionDef
    assert isinstance(new_node, ast.FunctionDef)
