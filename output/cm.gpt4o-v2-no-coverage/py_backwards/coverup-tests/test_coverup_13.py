# file: py_backwards/utils/snippet.py:9-16
# asked: {"lines": [9, 10, 12, 13, 14, 15, 16], "branches": [[12, 0], [12, 13], [13, 12], [13, 14]]}
# gained: {"lines": [9, 10, 12, 13, 14, 15, 16], "branches": [[12, 0], [12, 13], [13, 14]]}

import pytest
from typed_ast import ast3 as ast
from py_backwards.utils.snippet import find_variables

def test_find_variables_removes_let_calls(monkeypatch):
    # Create a sample AST with a 'let' call
    tree = ast.parse("let(x)")
    
    # Mock the find function to return the 'let' call node
    def mock_find(tree, type_):
        for node in ast.walk(tree):
            if isinstance(node, type_):
                yield node

    monkeypatch.setattr('py_backwards.utils.tree.find', mock_find)
    
    # Mock the get_non_exp_parent_and_index function to return the parent and index
    def mock_get_non_exp_parent_and_index(tree, node):
        return tree.body[0], 0

    monkeypatch.setattr('py_backwards.utils.tree.get_non_exp_parent_and_index', mock_get_non_exp_parent_and_index)
    
    # Call the function and collect the variables
    variables = find_variables(tree)
    
    # Assert that the 'let' call was removed and the variable 'x' was found
    assert variables == ['x']
    assert len(tree.body) == 0

def test_find_variables_no_let_calls(monkeypatch):
    # Create a sample AST without a 'let' call
    tree = ast.parse("y = 1")
    
    # Mock the find function to return no nodes
    def mock_find(tree, type_):
        return iter([])

    monkeypatch.setattr('py_backwards.utils.tree.find', mock_find)
    
    # Call the function and collect the variables
    variables = find_variables(tree)
    
    # Assert that no variables were found
    assert variables == []
    assert len(tree.body) == 1
