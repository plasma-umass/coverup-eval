# file: py_backwards/transformers/dict_unpacking.py:71-79
# asked: {"lines": [72, 73, 75, 76, 77, 78, 79], "branches": [[72, 73], [72, 75]]}
# gained: {"lines": [72, 73, 75, 76, 77, 78, 79], "branches": [[72, 73], [72, 75]]}

import pytest
from typed_ast import ast3 as ast
from py_backwards.transformers.dict_unpacking import DictUnpackingTransformer

@pytest.fixture
def transformer():
    tree = ast.parse("")
    return DictUnpackingTransformer(tree)

def test_visit_dict_with_none_key(transformer, mocker):
    node = ast.Dict(keys=[None], values=[ast.Constant(value=1)])
    
    mock_split_by_None = mocker.patch.object(transformer, '_split_by_None', return_value=[[(None, ast.Constant(value=1))]])
    mock_prepare_splitted = mocker.patch.object(transformer, '_prepare_splitted', return_value=[ast.Dict(keys=[None], values=[ast.Constant(value=1)])])
    mock_merge_dicts = mocker.patch.object(transformer, '_merge_dicts', return_value=ast.Call(func=ast.Name(id='_py_backwards_merge_dicts', ctx=ast.Load()), args=[], keywords=[]))
    
    result = transformer.visit_Dict(node)
    
    assert result.func.id == '_py_backwards_merge_dicts'
    mock_split_by_None.assert_called_once()
    mock_prepare_splitted.assert_called_once()
    mock_merge_dicts.assert_called_once()

def test_visit_dict_without_none_key(transformer, mocker):
    node = ast.Dict(keys=[ast.Constant(value=1)], values=[ast.Constant(value=1)])
    
    mock_generic_visit = mocker.patch.object(transformer, 'generic_visit', return_value=node)
    
    result = transformer.visit_Dict(node)
    
    assert result == node
    mock_generic_visit.assert_called_once()
