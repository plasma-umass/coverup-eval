# file: py_backwards/transformers/yield_from.py:34-41
# asked: {"lines": [34, 36, 37, 38, 39, 41], "branches": [[36, 37], [36, 41], [37, 38], [37, 41], [38, 37], [38, 39]]}
# gained: {"lines": [34, 36, 37, 38, 41], "branches": [[36, 37], [37, 38], [37, 41], [38, 37]]}

import pytest
from typed_ast import ast3 as ast
from py_backwards.transformers.yield_from import YieldFromTransformer

@pytest.fixture
def transformer():
    return YieldFromTransformer(None)

def test_get_yield_from_index_with_yield_from(transformer):
    class Holder:
        pass

    node = ast.FunctionDef(
        name="test",
        args=ast.arguments(args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
        body=[
            ast.Expr(value=ast.YieldFrom(value=ast.Name(id='x', ctx=ast.Load())))
        ],
        decorator_list=[]
    )

    index = transformer._get_yield_from_index(node, Holder)
    assert index is None

def test_get_yield_from_index_without_yield_from(transformer):
    class Holder:
        pass

    node = ast.FunctionDef(
        name="test",
        args=ast.arguments(args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
        body=[
            ast.Expr(value=ast.Yield(value=ast.Name(id='x', ctx=ast.Load())))
        ],
        decorator_list=[]
    )

    index = transformer._get_yield_from_index(node, Holder)
    assert index is None

def test_get_yield_from_index_with_different_node(transformer):
    class Holder:
        pass

    node = ast.ClassDef(
        name="TestClass",
        bases=[],
        keywords=[],
        body=[
            ast.Expr(value=ast.YieldFrom(value=ast.Name(id='x', ctx=ast.Load())))
        ],
        decorator_list=[]
    )

    index = transformer._get_yield_from_index(node, Holder)
    assert index is None
