# file: py_backwards/transformers/dict_unpacking.py:71-79
# asked: {"lines": [71, 72, 73, 75, 76, 77, 78, 79], "branches": [[72, 73], [72, 75]]}
# gained: {"lines": [71, 72, 73, 75, 76, 77, 78, 79], "branches": [[72, 73], [72, 75]]}

import pytest
from typed_ast import ast3 as ast
from py_backwards.transformers.dict_unpacking import DictUnpackingTransformer
from py_backwards.transformers.base import BaseNodeTransformer

@pytest.fixture
def transformer(mocker):
    tree = mocker.Mock()
    return DictUnpackingTransformer(tree)

def test_visit_dict_no_none_keys(transformer, mocker):
    node = ast.Dict(keys=[ast.Str(s='a'), ast.Str(s='b')], values=[ast.Num(n=1), ast.Num(n=2)])
    mocker.patch.object(transformer, 'generic_visit', return_value=node)
    
    result = transformer.visit_Dict(node)
    
    transformer.generic_visit.assert_called_once_with(node)
    assert result == node

def test_visit_dict_with_none_keys(transformer, mocker):
    node = ast.Dict(keys=[None, ast.Str(s='b')], values=[ast.Name(id='x'), ast.Num(n=2)])
    mocker.patch.object(transformer, '_split_by_None', return_value=[[], ast.Name(id='x'), [(ast.Str(s='b'), ast.Num(n=2))]])
    mocker.patch.object(transformer, '_prepare_splitted', return_value=[ast.Call(func=ast.Name(id='dict'), args=[ast.Name(id='x')], keywords=[]), ast.Dict(keys=[ast.Str(s='b')], values=[ast.Num(n=2)])])
    mocker.patch.object(transformer, '_merge_dicts', return_value=ast.Call(func=ast.Name(id='_py_backwards_merge_dicts'), args=[ast.List(elts=[])], keywords=[]))
    
    result = transformer.visit_Dict(node)
    
    transformer._split_by_None.assert_called_once()
    transformer._prepare_splitted.assert_called_once()
    transformer._merge_dicts.assert_called_once()
    assert isinstance(result, ast.Call)

def test_split_by_none(transformer):
    pairs = [(None, ast.Name(id='x')), (ast.Str(s='b'), ast.Num(n=2))]
    result = transformer._split_by_None(pairs)
    
    assert len(result) == 3
    assert result[0] == []
    assert isinstance(result[1], ast.Name)
    assert result[1].id == 'x'
    assert isinstance(result[2], list)
    assert len(result[2]) == 1
    assert isinstance(result[2][0], tuple)
    assert isinstance(result[2][0][0], ast.Str)
    assert result[2][0][0].s == 'b'
    assert isinstance(result[2][0][1], ast.Num)
    assert result[2][0][1].n == 2

def test_prepare_splitted(transformer):
    splitted = [[], ast.Name(id='x'), [(ast.Str(s='b'), ast.Num(n=2))]]
    result = list(transformer._prepare_splitted(splitted))
    
    assert len(result) == 2
    assert isinstance(result[0], ast.Call)
    assert isinstance(result[1], ast.Dict)

def test_merge_dicts(transformer):
    xs = [ast.Call(func=ast.Name(id='dict'), args=[ast.Name(id='x')], keywords=[]), ast.Dict(keys=[ast.Str(s='b')], values=[ast.Num(n=2)])]
    result = transformer._merge_dicts(xs)
    
    assert isinstance(result, ast.Call)
    assert result.func.id == '_py_backwards_merge_dicts'
    assert isinstance(result.args[0], ast.List)
    assert len(result.args[0].elts) == 2
