# file: py_backwards/utils/tree.py:58-62
# asked: {"lines": [58, 61, 62], "branches": []}
# gained: {"lines": [58, 61, 62], "branches": []}

import pytest
from typed_ast import ast3 as ast
from py_backwards.utils.tree import replace_at

def test_replace_at_with_single_node():
    parent = ast.Module(body=[ast.Expr(value=ast.Constant(value=1)), ast.Expr(value=ast.Constant(value=2))])
    new_node = ast.Expr(value=ast.Constant(value=3))
    
    replace_at(1, parent, new_node)
    
    assert len(parent.body) == 2
    assert isinstance(parent.body[1], ast.Expr)
    assert parent.body[1].value.value == 3

def test_replace_at_with_multiple_nodes():
    parent = ast.Module(body=[ast.Expr(value=ast.Constant(value=1)), ast.Expr(value=ast.Constant(value=2))])
    new_nodes = [ast.Expr(value=ast.Constant(value=3)), ast.Expr(value=ast.Constant(value=4))]
    
    replace_at(1, parent, new_nodes)
    
    assert len(parent.body) == 3
    assert isinstance(parent.body[1], ast.Expr)
    assert parent.body[1].value.value == 3
    assert isinstance(parent.body[2], ast.Expr)
    assert parent.body[2].value.value == 4

def test_replace_at_with_empty_list():
    parent = ast.Module(body=[ast.Expr(value=ast.Constant(value=1)), ast.Expr(value=ast.Constant(value=2))])
    new_nodes = []
    
    replace_at(1, parent, new_nodes)
    
    assert len(parent.body) == 1
    assert isinstance(parent.body[0], ast.Expr)
    assert parent.body[0].value.value == 1
