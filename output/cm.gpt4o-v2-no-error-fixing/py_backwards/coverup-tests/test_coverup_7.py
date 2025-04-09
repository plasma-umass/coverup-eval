# file: py_backwards/utils/snippet.py:9-16
# asked: {"lines": [9, 10, 12, 13, 14, 15, 16], "branches": [[12, 0], [12, 13], [13, 12], [13, 14]]}
# gained: {"lines": [9, 10, 12, 13, 14, 15, 16], "branches": [[12, 0], [12, 13], [13, 14]]}

import pytest
from typed_ast import ast3 as ast
from py_backwards.utils.snippet import find_variables

def test_find_variables_removes_let_calls_and_yields_variable_names():
    # Create a sample AST with a 'let' call
    tree = ast.parse("let(x)")
    
    # Call the function and collect results
    result = list(find_variables(tree))
    
    # Assert that the 'let' call was removed and 'x' was yielded
    assert result == ['x']
    
    # Assert that the 'let' call is no longer in the tree
    assert not any(isinstance(node, ast.Call) and node.func.id == 'let' for node in ast.walk(tree))

def test_find_variables_no_let_calls():
    # Create a sample AST without a 'let' call
    tree = ast.parse("y = 2")
    
    # Call the function and collect results
    result = list(find_variables(tree))
    
    # Assert that no variables were yielded
    assert result == []

    # Assert that the tree remains unchanged
    assert any(isinstance(node, ast.Assign) for node in ast.walk(tree))

@pytest.fixture(autouse=True)
def run_around_tests(monkeypatch):
    # Setup: (if needed, otherwise remove this fixture)
    yield
    # Teardown: (if needed, otherwise remove this fixture)
