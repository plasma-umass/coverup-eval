# file: py_backwards/transformers/dict_unpacking.py:46-57
# asked: {"lines": [46, 49, 50, 51, 52, 53, 54, 55, 56, 57], "branches": [[49, 0], [49, 50], [50, 51], [50, 55], [55, 49], [55, 56]]}
# gained: {"lines": [46, 49, 50, 51, 52, 53, 54, 55, 56, 57], "branches": [[49, 0], [49, 50], [50, 51], [50, 55], [55, 49], [55, 56]]}

import pytest
from typed_ast import ast3 as ast
from py_backwards.transformers.dict_unpacking import DictUnpackingTransformer, Splitted

class TestDictUnpackingTransformer:
    
    @pytest.fixture
    def transformer(self):
        return DictUnpackingTransformer(None)
    
    def test_prepare_splitted_with_non_list(self, transformer):
        # Test with a non-list element in splitted
        splitted = [ast.Str(s='test')]
        result = list(transformer._prepare_splitted(splitted))
        assert len(result) == 1
        assert isinstance(result[0], ast.Call)
        assert result[0].func.id == 'dict'
        assert result[0].args == [splitted[0]]
        assert result[0].keywords == []

    def test_prepare_splitted_with_empty_list(self, transformer):
        # Test with an empty list element in splitted
        splitted = [[]]
        result = list(transformer._prepare_splitted(splitted))
        assert len(result) == 0

    def test_prepare_splitted_with_non_empty_list(self, transformer):
        # Test with a non-empty list element in splitted
        key = ast.Str(s='key')
        value = ast.Str(s='value')
        splitted = [[(key, value)]]
        result = list(transformer._prepare_splitted(splitted))
        assert len(result) == 1
        assert isinstance(result[0], ast.Dict)
        assert result[0].keys == [key]
        assert result[0].values == [value]
