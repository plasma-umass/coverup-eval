# file: py_backwards/transformers/dict_unpacking.py:59-65
# asked: {"lines": [59, 62, 63, 64, 65], "branches": []}
# gained: {"lines": [59, 62, 63, 64, 65], "branches": []}

import pytest
from typed_ast import ast3 as ast
from py_backwards.transformers.dict_unpacking import DictUnpackingTransformer

@pytest.fixture
def transformer():
    tree = ast.Module(body=[])
    return DictUnpackingTransformer(tree)

def test_merge_dicts_with_call(transformer):
    call_node = ast.Call(func=ast.Name(id='func'), args=[], keywords=[])
    result = transformer._merge_dicts([call_node])
    assert isinstance(result, ast.Call)
    assert result.func.id == '_py_backwards_merge_dicts'
    assert isinstance(result.args[0], ast.List)
    assert result.args[0].elts == [call_node]

def test_merge_dicts_with_dict(transformer):
    dict_node = ast.Dict(keys=[], values=[])
    result = transformer._merge_dicts([dict_node])
    assert isinstance(result, ast.Call)
    assert result.func.id == '_py_backwards_merge_dicts'
    assert isinstance(result.args[0], ast.List)
    assert result.args[0].elts == [dict_node]

def test_merge_dicts_with_mixed_nodes(transformer):
    call_node = ast.Call(func=ast.Name(id='func'), args=[], keywords=[])
    dict_node = ast.Dict(keys=[], values=[])
    result = transformer._merge_dicts([call_node, dict_node])
    assert isinstance(result, ast.Call)
    assert result.func.id == '_py_backwards_merge_dicts'
    assert isinstance(result.args[0], ast.List)
    assert result.args[0].elts == [call_node, dict_node]
