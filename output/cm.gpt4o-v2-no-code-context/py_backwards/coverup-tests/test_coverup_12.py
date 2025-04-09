# file: py_backwards/transformers/dict_unpacking.py:71-79
# asked: {"lines": [71, 72, 73, 75, 76, 77, 78, 79], "branches": [[72, 73], [72, 75]]}
# gained: {"lines": [71, 72, 73, 75, 76, 77, 78, 79], "branches": [[72, 73], [72, 75]]}

import ast
import pytest
from py_backwards.transformers.dict_unpacking import DictUnpackingTransformer
from py_backwards.transformers.base import BaseNodeTransformer

class MockTree:
    pass

class TestDictUnpackingTransformer:
    @pytest.fixture
    def transformer(self):
        return DictUnpackingTransformer(MockTree())

    def test_visit_dict_no_none_keys(self, transformer):
        node = ast.Dict(keys=[ast.Constant(value='a'), ast.Constant(value='b')], values=[ast.Constant(value=1), ast.Constant(value=2)])
        result = transformer.visit_Dict(node)
        assert isinstance(result, ast.Dict)
        assert result.keys == node.keys
        assert result.values == node.values

    def test_visit_dict_with_none_key(self, transformer, mocker):
        node = ast.Dict(keys=[ast.Constant(value='a'), None], values=[ast.Constant(value=1), ast.Constant(value=2)])
        
        mocker.patch.object(transformer, '_split_by_None', return_value=[([('a', 1)], [(None, 2)])])
        mocker.patch.object(transformer, '_prepare_splitted', return_value=[ast.Dict(keys=[ast.Constant(value='a')], values=[ast.Constant(value=1)]), ast.Dict(keys=[None], values=[ast.Constant(value=2)])])
        mocker.patch.object(transformer, '_merge_dicts', return_value=ast.Call(func=ast.Name(id='dict', ctx=ast.Load()), args=[], keywords=[]))
        
        result = transformer.visit_Dict(node)
        
        assert transformer._tree_changed is True
        assert isinstance(result, ast.Call)
        assert result.func.id == 'dict'
