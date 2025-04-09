# file: py_backwards/transformers/starred_unpacking.py:50-58
# asked: {"lines": [50, 52, 53, 55, 56, 57, 58], "branches": [[52, 53], [52, 55], [56, 57], [56, 58]]}
# gained: {"lines": [50, 52, 53, 55, 56, 57, 58], "branches": [[52, 53], [52, 55], [56, 57], [56, 58]]}

import pytest
from typed_ast import ast3 as ast
from py_backwards.transformers.starred_unpacking import StarredUnpackingTransformer

@pytest.fixture
def transformer():
    return StarredUnpackingTransformer(None)

def test_merge_lists_single_element(transformer):
    xs = [ast.Constant(value=1)]
    result = transformer._merge_lists(xs)
    assert result == xs[0]

def test_merge_lists_multiple_elements(transformer):
    xs = [ast.Constant(value=1), ast.Constant(value=2), ast.Constant(value=3)]
    result = transformer._merge_lists(xs)
    assert isinstance(result, ast.BinOp)
    assert isinstance(result.left, ast.BinOp)
    assert result.left.left == xs[0]
    assert result.left.right == xs[1]
    assert result.right == xs[2]

def test_merge_lists_two_elements(transformer):
    xs = [ast.Constant(value=1), ast.Constant(value=2)]
    result = transformer._merge_lists(xs)
    assert isinstance(result, ast.BinOp)
    assert result.left == xs[0]
    assert result.right == xs[1]
