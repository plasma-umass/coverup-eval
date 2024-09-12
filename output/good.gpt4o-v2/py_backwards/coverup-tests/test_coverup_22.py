# file: py_backwards/transformers/starred_unpacking.py:39-48
# asked: {"lines": [39, 41, 42, 43, 44, 45, 46, 47, 48], "branches": [[41, 0], [41, 42], [42, 43], [42, 47], [47, 41], [47, 48]]}
# gained: {"lines": [39, 41, 42, 43, 44, 45, 46, 47, 48], "branches": [[41, 0], [41, 42], [42, 43], [42, 47], [47, 41], [47, 48]]}

import pytest
from typed_ast import ast3 as ast
from py_backwards.transformers.starred_unpacking import StarredUnpackingTransformer

@pytest.fixture
def transformer():
    tree = ast.Module(body=[])
    return StarredUnpackingTransformer(tree)

def test_prepare_lists_with_starred(transformer):
    starred_node = ast.Starred(value=ast.Name(id='a'))
    result = list(transformer._prepare_lists([starred_node]))
    assert len(result) == 1
    assert isinstance(result[0], ast.Call)
    assert result[0].func.id == 'list'
    assert result[0].args[0].id == 'a'

def test_prepare_lists_with_non_empty_list(transformer):
    non_empty_list = [ast.Name(id='a'), ast.Name(id='b')]
    result = list(transformer._prepare_lists([non_empty_list]))
    assert len(result) == 1
    assert isinstance(result[0], ast.List)
    assert len(result[0].elts) == 2
    assert result[0].elts[0].id == 'a'
    assert result[0].elts[1].id == 'b'

def test_prepare_lists_with_empty_list(transformer):
    empty_list = []
    result = list(transformer._prepare_lists([empty_list]))
    assert len(result) == 0
