# file: py_backwards/utils/snippet.py:93-97
# asked: {"lines": [], "branches": [[95, 94]]}
# gained: {"lines": [], "branches": [[95, 94]]}

import pytest
from typed_ast import ast3 as ast
from py_backwards.utils.snippet import extend_tree
from py_backwards.utils.tree import find, get_non_exp_parent_and_index, replace_at

class Variable:
    def __init__(self, id):
        self.id = id

def test_extend_tree_with_extend_function_call(monkeypatch):
    # Create a mock tree with an 'extend' function call
    tree = ast.Module(body=[
        ast.Expr(value=ast.Call(
            func=ast.Name(id='extend', ctx=ast.Load()),
            args=[ast.Name(id='var', ctx=ast.Load())],
            keywords=[]
        ))
    ])

    variables = {'var': Variable(id='new_var')}

    # Mock the functions from py_backwards.utils.tree
    def mock_find(tree, type_):
        for node in ast.walk(tree):
            if isinstance(node, type_):
                yield node

    def mock_get_non_exp_parent_and_index(tree, node):
        return tree, 0

    def mock_replace_at(index, parent, nodes):
        parent.body[index] = nodes

    monkeypatch.setattr('py_backwards.utils.tree.find', mock_find)
    monkeypatch.setattr('py_backwards.utils.tree.get_non_exp_parent_and_index', mock_get_non_exp_parent_and_index)
    monkeypatch.setattr('py_backwards.utils.tree.replace_at', mock_replace_at)

    extend_tree(tree, variables)

    # Assert that the tree has been modified correctly
    assert isinstance(tree.body[0], Variable)
    assert tree.body[0].id == 'new_var'

def test_extend_tree_without_extend_function_call(monkeypatch):
    # Create a mock tree without an 'extend' function call
    tree = ast.Module(body=[
        ast.Expr(value=ast.Call(
            func=ast.Name(id='other_func', ctx=ast.Load()),
            args=[ast.Name(id='var', ctx=ast.Load())],
            keywords=[]
        ))
    ])

    variables = {'var': Variable(id='new_var')}

    # Mock the functions from py_backwards.utils.tree
    def mock_find(tree, type_):
        for node in ast.walk(tree):
            if isinstance(node, type_):
                yield node

    def mock_get_non_exp_parent_and_index(tree, node):
        return tree, 0

    def mock_replace_at(index, parent, nodes):
        parent.body[index] = nodes

    monkeypatch.setattr('py_backwards.utils.tree.find', mock_find)
    monkeypatch.setattr('py_backwards.utils.tree.get_non_exp_parent_and_index', mock_get_non_exp_parent_and_index)
    monkeypatch.setattr('py_backwards.utils.tree.replace_at', mock_replace_at)

    extend_tree(tree, variables)

    # Assert that the tree has not been modified
    assert isinstance(tree.body[0], ast.Expr)
    assert isinstance(tree.body[0].value, ast.Call)
    assert tree.body[0].value.func.id == 'other_func'
