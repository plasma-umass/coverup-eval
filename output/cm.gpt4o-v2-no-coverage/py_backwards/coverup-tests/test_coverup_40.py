# file: py_backwards/transformers/yield_from.py:34-41
# asked: {"lines": [34, 36, 37, 38, 39, 41], "branches": [[36, 37], [36, 41], [37, 38], [37, 41], [38, 37], [38, 39]]}
# gained: {"lines": [34, 36, 37, 38, 39, 41], "branches": [[36, 37], [36, 41], [37, 38], [37, 41], [38, 37], [38, 39]]}

import pytest
from typed_ast import ast3 as ast
from py_backwards.transformers.yield_from import YieldFromTransformer

class Holder:
    def __init__(self, value):
        self.value = value

@pytest.fixture
def transformer():
    tree = ast.Module(body=[])
    return YieldFromTransformer(tree)

def test_get_yield_from_index_with_yield_from(transformer):
    node = ast.FunctionDef(
        name='test',
        args=ast.arguments(args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
        body=[Holder(ast.YieldFrom(value=ast.Name(id='x', ctx=ast.Load())))],
        decorator_list=[]
    )
    index = transformer._get_yield_from_index(node, Holder)
    assert index == 0

def test_get_yield_from_index_without_yield_from(transformer):
    node = ast.FunctionDef(
        name='test',
        args=ast.arguments(args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
        body=[Holder(ast.Expr(value=ast.Name(id='x', ctx=ast.Load())))],
        decorator_list=[]
    )
    index = transformer._get_yield_from_index(node, Holder)
    assert index is None

def test_get_yield_from_index_no_body(transformer):
    node = ast.FunctionDef(
        name='test',
        args=ast.arguments(args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
        body=None,
        decorator_list=[]
    )
    index = transformer._get_yield_from_index(node, Holder)
    assert index is None

def test_get_yield_from_index_body_not_list(transformer):
    node = ast.FunctionDef(
        name='test',
        args=ast.arguments(args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
        body=Holder(ast.YieldFrom(value=ast.Name(id='x', ctx=ast.Load()))),
        decorator_list=[]
    )
    index = transformer._get_yield_from_index(node, Holder)
    assert index is None
