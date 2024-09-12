# file: py_backwards/transformers/dict_unpacking.py:71-79
# asked: {"lines": [71, 72, 73, 75, 76, 77, 78, 79], "branches": [[72, 73], [72, 75]]}
# gained: {"lines": [71, 72, 73, 75, 76, 77, 78, 79], "branches": [[72, 73], [72, 75]]}

import pytest
from typed_ast import ast3 as ast
from py_backwards.transformers.dict_unpacking import DictUnpackingTransformer

@pytest.fixture
def transformer(mocker):
    tree = mocker.Mock(spec=ast.AST)
    return DictUnpackingTransformer(tree)

def test_visit_dict_no_none_keys(transformer, mocker):
    node = ast.Dict(keys=[ast.Str(s='key1'), ast.Str(s='key2')], values=[ast.Num(n=1), ast.Num(n=2)])
    mock_generic_visit = mocker.patch.object(DictUnpackingTransformer, 'generic_visit', return_value=node)
    
    result = transformer.visit_Dict(node)
    
    mock_generic_visit.assert_called_once_with(node)
    assert result == node

def test_visit_dict_with_none_keys(transformer, mocker):
    node = ast.Dict(keys=[ast.Str(s='key1'), None, ast.Str(s='key2')], values=[ast.Num(n=1), ast.Name(id='unpack'), ast.Num(n=2)])
    mock_split_by_None = mocker.patch.object(DictUnpackingTransformer, '_split_by_None', return_value=[[(ast.Str(s='key1'), ast.Num(n=1))], ast.Name(id='unpack'), [(ast.Str(s='key2'), ast.Num(n=2))]])
    mock_prepare_splitted = mocker.patch.object(DictUnpackingTransformer, '_prepare_splitted', return_value=[ast.Dict(keys=[ast.Str(s='key1')], values=[ast.Num(n=1)]), ast.Call(func=ast.Name(id='dict'), args=[ast.Name(id='unpack')], keywords=[]), ast.Dict(keys=[ast.Str(s='key2')], values=[ast.Num(n=2)])])
    mock_merge_dicts = mocker.patch.object(DictUnpackingTransformer, '_merge_dicts', return_value=ast.Call(func=ast.Name(id='_py_backwards_merge_dicts'), args=[ast.List(elts=[])], keywords=[]))
    
    result = transformer.visit_Dict(node)
    
    mock_split_by_None.assert_called_once()
    mock_prepare_splitted.assert_called_once()
    mock_merge_dicts.assert_called_once()
    assert isinstance(result, ast.Call)
    assert result.func.id == '_py_backwards_merge_dicts'
