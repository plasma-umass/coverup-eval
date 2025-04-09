# file: py_backwards/transformers/starred_unpacking.py:60-64
# asked: {"lines": [62, 63, 64], "branches": []}
# gained: {"lines": [62, 63, 64], "branches": []}

import pytest
from typed_ast import ast3 as ast
from py_backwards.transformers.starred_unpacking import StarredUnpackingTransformer

@pytest.fixture
def transformer():
    tree = ast.Module(body=[])
    return StarredUnpackingTransformer(tree)

def test_to_sum_of_lists_no_starred(transformer):
    xs = [ast.Constant(value=1), ast.Constant(value=2)]
    result = transformer._to_sum_of_lists(xs)
    assert isinstance(result, ast.List)
    assert len(result.elts) == 2
    assert isinstance(result.elts[0], ast.Constant)
    assert isinstance(result.elts[1], ast.Constant)

def test_to_sum_of_lists_with_starred(transformer):
    xs = [ast.Constant(value=1), ast.Starred(value=ast.Name(id='a')), ast.Constant(value=2)]
    result = transformer._to_sum_of_lists(xs)
    assert isinstance(result, ast.BinOp)
    assert isinstance(result.left, ast.BinOp)
    assert isinstance(result.right, ast.List)

def test_split_by_starred(transformer):
    xs = [ast.Constant(value=1), ast.Starred(value=ast.Name(id='a')), ast.Constant(value=2)]
    result = transformer._split_by_starred(xs)
    assert len(result) == 3
    assert isinstance(result[0], list)
    assert isinstance(result[1], ast.Starred)
    assert isinstance(result[2], list)

def test_prepare_lists(transformer):
    xs = [[ast.Constant(value=1)], ast.Starred(value=ast.Name(id='a')), [ast.Constant(value=2)]]
    result = list(transformer._prepare_lists(xs))
    assert len(result) == 3
    assert isinstance(result[0], ast.List)
    assert isinstance(result[1], ast.Call)
    assert isinstance(result[2], ast.List)

def test_merge_lists_single(transformer):
    xs = [ast.List(elts=[ast.Constant(value=1)])]
    result = transformer._merge_lists(xs)
    assert isinstance(result, ast.List)

def test_merge_lists_multiple(transformer):
    xs = [ast.List(elts=[ast.Constant(value=1)]), ast.List(elts=[ast.Constant(value=2)])]
    result = transformer._merge_lists(xs)
    assert isinstance(result, ast.BinOp)
    assert isinstance(result.left, ast.List)
    assert isinstance(result.right, ast.List)
