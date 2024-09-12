# file: py_backwards/transformers/yield_from.py:34-41
# asked: {"lines": [39], "branches": [[36, 41], [38, 39]]}
# gained: {"lines": [39], "branches": [[36, 41], [38, 39]]}

import pytest
from typed_ast import ast3 as ast
from py_backwards.transformers.yield_from import YieldFromTransformer

@pytest.fixture
def transformer():
    tree = ast.Module(body=[])
    return YieldFromTransformer(tree)

def test_get_yield_from_index_with_yield_from(transformer):
    node = ast.FunctionDef(
        name="test_func",
        args=ast.arguments(args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
        body=[
            ast.Expr(value=ast.YieldFrom(value=ast.Name(id='a', ctx=ast.Load())))
        ],
        decorator_list=[]
    )
    index = transformer._get_yield_from_index(node, ast.Expr)
    assert index == 0

def test_get_yield_from_index_without_yield_from(transformer):
    node = ast.FunctionDef(
        name="test_func",
        args=ast.arguments(args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
        body=[
            ast.Expr(value=ast.Name(id='a', ctx=ast.Load()))
        ],
        decorator_list=[]
    )
    index = transformer._get_yield_from_index(node, ast.Expr)
    assert index is None

def test_get_yield_from_index_no_body(transformer):
    node = ast.FunctionDef(
        name="test_func",
        args=ast.arguments(args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
        body=None,
        decorator_list=[]
    )
    index = transformer._get_yield_from_index(node, ast.Expr)
    assert index is None
