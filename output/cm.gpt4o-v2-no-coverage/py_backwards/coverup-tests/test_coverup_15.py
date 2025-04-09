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
    starred_node = ast.Starred(value=ast.Name(id='x'))
    result = list(transformer._prepare_lists([starred_node]))
    assert len(result) == 1
    assert isinstance(result[0], ast.Call)
    assert result[0].func.id == 'list'
    assert result[0].args[0].id == 'x'

def test_prepare_lists_with_non_empty_list(transformer):
    list_node = [ast.Name(id='x'), ast.Name(id='y')]
    result = list(transformer._prepare_lists([list_node]))
    assert len(result) == 1
    assert isinstance(result[0], ast.List)
    assert len(result[0].elts) == 2
    assert result[0].elts[0].id == 'x'
    assert result[0].elts[1].id == 'y'

def test_prepare_lists_with_empty_list(transformer):
    result = list(transformer._prepare_lists([[]]))
    assert len(result) == 0

def test_prepare_lists_with_mixed_nodes(transformer):
    starred_node = ast.Starred(value=ast.Name(id='x'))
    list_node = [ast.Name(id='y')]
    result = list(transformer._prepare_lists([starred_node, list_node, []]))
    assert len(result) == 2
    assert isinstance(result[0], ast.Call)
    assert result[0].func.id == 'list'
    assert result[0].args[0].id == 'x'
    assert isinstance(result[1], ast.List)
    assert len(result[1].elts) == 1
    assert result[1].elts[0].id == 'y'
