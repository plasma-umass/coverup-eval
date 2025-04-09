# file: py_backwards/transformers/starred_unpacking.py:27-37
# asked: {"lines": [27, 29, 30, 31, 32, 33, 35, 36, 37], "branches": [[30, 31], [30, 37], [31, 32], [31, 35]]}
# gained: {"lines": [27, 29, 30, 31, 32, 33, 35, 36, 37], "branches": [[30, 31], [30, 37], [31, 32], [31, 35]]}

import pytest
from typed_ast import ast3 as ast
from py_backwards.transformers.starred_unpacking import StarredUnpackingTransformer

@pytest.fixture
def transformer():
    return StarredUnpackingTransformer(None)

def test_split_by_starred_with_starred(transformer):
    xs = [ast.Num(n=1), ast.Starred(value=ast.Name(id='a', ctx=ast.Load())), ast.Num(n=2)]
    result = transformer._split_by_starred(xs)
    assert len(result) == 3
    assert isinstance(result[0], list) and len(result[0]) == 1 and isinstance(result[0][0], ast.Num)
    assert isinstance(result[1], ast.Starred)
    assert isinstance(result[2], list) and len(result[2]) == 1 and isinstance(result[2][0], ast.Num)

def test_split_by_starred_without_starred(transformer):
    xs = [ast.Num(n=1), ast.Num(n=2)]
    result = transformer._split_by_starred(xs)
    assert len(result) == 1
    assert isinstance(result[0], list) and len(result[0]) == 2
    assert all(isinstance(item, ast.Num) for item in result[0])

def test_split_by_starred_empty(transformer):
    xs = []
    result = transformer._split_by_starred(xs)
    assert len(result) == 1
    assert isinstance(result[0], list) and len(result[0]) == 0
