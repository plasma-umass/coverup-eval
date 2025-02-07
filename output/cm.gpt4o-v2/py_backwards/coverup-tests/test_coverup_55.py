# file: py_backwards/transformers/starred_unpacking.py:60-64
# asked: {"lines": [60, 62, 63, 64], "branches": []}
# gained: {"lines": [60, 62, 63, 64], "branches": []}

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
    assert isinstance(result.left.left, ast.List)
    assert isinstance(result.left.right, ast.Call)
    assert isinstance(result.right, ast.List)
