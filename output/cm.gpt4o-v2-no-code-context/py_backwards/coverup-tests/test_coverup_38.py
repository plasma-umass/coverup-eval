# file: py_backwards/utils/snippet.py:72-74
# asked: {"lines": [72, 73, 74], "branches": []}
# gained: {"lines": [72, 73, 74], "branches": []}

import ast
import pytest

from py_backwards.utils.snippet import VariablesReplacer

@pytest.fixture
def replacer():
    # Provide a mock 'variables' argument to the VariablesReplacer constructor
    return VariablesReplacer(variables={})

def test_visit_import_from(replacer):
    # Create a mock ImportFrom node
    node = ast.ImportFrom(module='old_module', names=[], level=0)
    
    # Mock the _replace_module method to return a different module name
    replacer._replace_module = lambda x: 'new_module'
    
    # Visit the node
    new_node = replacer.visit_ImportFrom(node)
    
    # Assertions to verify the module name was replaced
    assert new_node.module == 'new_module'
    assert isinstance(new_node, ast.ImportFrom)
