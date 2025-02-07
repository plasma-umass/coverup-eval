# file: py_backwards/utils/tree.py:48-55
# asked: {"lines": [48, 51, 52, 54, 55], "branches": [[51, 52], [51, 54], [54, 0], [54, 55]]}
# gained: {"lines": [48, 51, 52, 54, 55], "branches": [[51, 52], [51, 54], [54, 0], [54, 55]]}

import pytest
from typed_ast import ast3 as ast
from py_backwards.utils.tree import insert_at

def test_insert_at_single_node():
    parent = ast.Module(body=[])
    node = ast.Expr(value=ast.Str(s="test"))
    insert_at(0, parent, node)
    assert len(parent.body) == 1
    assert isinstance(parent.body[0], ast.Expr)
    assert parent.body[0].value.s == "test"

def test_insert_at_multiple_nodes():
    parent = ast.Module(body=[])
    nodes = [ast.Expr(value=ast.Str(s="test1")), ast.Expr(value=ast.Str(s="test2"))]
    insert_at(0, parent, nodes)
    assert len(parent.body) == 2
    assert isinstance(parent.body[0], ast.Expr)
    assert parent.body[0].value.s == "test1"
    assert isinstance(parent.body[1], ast.Expr)
    assert parent.body[1].value.s == "test2"

def test_insert_at_with_existing_body():
    parent = ast.Module(body=[ast.Expr(value=ast.Str(s="existing"))])
    node = ast.Expr(value=ast.Str(s="new"))
    insert_at(1, parent, node)
    assert len(parent.body) == 2
    assert isinstance(parent.body[0], ast.Expr)
    assert parent.body[0].value.s == "existing"
    assert isinstance(parent.body[1], ast.Expr)
    assert parent.body[1].value.s == "new"

def test_insert_at_reverse_order():
    parent = ast.Module(body=[])
    nodes = [ast.Expr(value=ast.Str(s="test1")), ast.Expr(value=ast.Str(s="test2"))]
    insert_at(0, parent, nodes)
    assert len(parent.body) == 2
    assert parent.body[0].value.s == "test1"
    assert parent.body[1].value.s == "test2"
