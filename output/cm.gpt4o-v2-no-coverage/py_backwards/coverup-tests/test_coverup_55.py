# file: py_backwards/utils/snippet.py:146-157
# asked: {"lines": [146], "branches": []}
# gained: {"lines": [146], "branches": []}

import pytest
import ast
from py_backwards.utils.snippet import extend

def test_extend_with_assignments():
    code = """
x = 1
y = 2
"""
    tree = ast.parse(code)
    extend(tree)
    assert isinstance(tree, ast.Module)
    assert len(tree.body) == 2
    assert isinstance(tree.body[0], ast.Assign)
    assert isinstance(tree.body[1], ast.Assign)

def test_extend_without_assignments():
    code = """
print(x, y)
"""
    tree = ast.parse(code)
    extend(tree)
    assert isinstance(tree, ast.Module)
    assert len(tree.body) == 1
    assert isinstance(tree.body[0], ast.Expr)

def test_extend_mixed():
    code = """
x = 1
print(x, y)
"""
    tree = ast.parse(code)
    extend(tree)
    assert isinstance(tree, ast.Module)
    assert len(tree.body) == 2
    assert isinstance(tree.body[0], ast.Assign)
    assert isinstance(tree.body[1], ast.Expr)
