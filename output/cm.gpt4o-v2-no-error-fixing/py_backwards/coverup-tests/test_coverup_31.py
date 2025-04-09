# file: py_backwards/transformers/dict_unpacking.py:46-57
# asked: {"lines": [49, 50, 51, 52, 53, 54, 55, 56, 57], "branches": [[49, 0], [49, 50], [50, 51], [50, 55], [55, 49], [55, 56]]}
# gained: {"lines": [49, 50, 51, 52, 53, 54, 55, 56, 57], "branches": [[49, 0], [49, 50], [50, 51], [50, 55], [55, 49], [55, 56]]}

import pytest
from typed_ast import ast3 as ast
from py_backwards.transformers.dict_unpacking import DictUnpackingTransformer
from py_backwards.transformers.base import BaseNodeTransformer
from typing import Union, List, Tuple

Splitted = List[Union[List[Tuple[ast.expr, ast.expr]], ast.expr]]

@pytest.fixture
def transformer():
    tree = ast.Module(body=[])
    return DictUnpackingTransformer(tree)

def test_prepare_splitted_with_non_list(transformer):
    expr = ast.Str(s='test')
    splitted = [expr]
    result = list(transformer._prepare_splitted(splitted))
    assert len(result) == 1
    assert isinstance(result[0], ast.Call)
    assert result[0].func.id == 'dict'
    assert result[0].args == [expr]

def test_prepare_splitted_with_empty_list(transformer):
    splitted = [[]]
    result = list(transformer._prepare_splitted(splitted))
    assert len(result) == 0

def test_prepare_splitted_with_non_empty_list(transformer):
    key = ast.Str(s='key')
    value = ast.Str(s='value')
    group = [(key, value)]
    splitted = [group]
    result = list(transformer._prepare_splitted(splitted))
    assert len(result) == 1
    assert isinstance(result[0], ast.Dict)
    assert result[0].keys == [key]
    assert result[0].values == [value]
