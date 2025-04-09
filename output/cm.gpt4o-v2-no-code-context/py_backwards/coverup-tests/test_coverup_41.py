# file: py_backwards/transformers/dict_unpacking.py:59-65
# asked: {"lines": [59, 62, 63, 64, 65], "branches": []}
# gained: {"lines": [59, 62, 63, 64, 65], "branches": []}

import ast
import pytest
from py_backwards.transformers.dict_unpacking import DictUnpackingTransformer
from py_backwards.transformers.base import BaseNodeTransformer
from typed_ast import ast3

class MockTree:
    pass

@pytest.fixture
def transformer():
    tree = MockTree()
    return DictUnpackingTransformer(tree)

def test_merge_dicts_with_call(transformer):
    call_node = ast3.Call(func=ast3.Name(id='test_func'), args=[], keywords=[])
    result = transformer._merge_dicts([call_node])
    
    assert isinstance(result, ast3.Call)
    assert isinstance(result.func, ast3.Name)
    assert result.func.id == '_py_backwards_merge_dicts'
    assert isinstance(result.args[0], ast3.List)
    assert result.args[0].elts == [call_node]
    assert result.keywords == []

def test_merge_dicts_with_dict(transformer):
    dict_node = ast3.Dict(keys=[], values=[])
    result = transformer._merge_dicts([dict_node])
    
    assert isinstance(result, ast3.Call)
    assert isinstance(result.func, ast3.Name)
    assert result.func.id == '_py_backwards_merge_dicts'
    assert isinstance(result.args[0], ast3.List)
    assert result.args[0].elts == [dict_node]
    assert result.keywords == []

def test_merge_dicts_with_mixed_nodes(transformer):
    call_node = ast3.Call(func=ast3.Name(id='test_func'), args=[], keywords=[])
    dict_node = ast3.Dict(keys=[], values=[])
    result = transformer._merge_dicts([call_node, dict_node])
    
    assert isinstance(result, ast3.Call)
    assert isinstance(result.func, ast3.Name)
    assert result.func.id == '_py_backwards_merge_dicts'
    assert isinstance(result.args[0], ast3.List)
    assert result.args[0].elts == [call_node, dict_node]
    assert result.keywords == []
