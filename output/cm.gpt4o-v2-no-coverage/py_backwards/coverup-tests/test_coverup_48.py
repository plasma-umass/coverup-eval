# file: py_backwards/transformers/dict_unpacking.py:33-44
# asked: {"lines": [33, 35, 36, 37, 38, 39, 41, 42, 44], "branches": [[36, 37], [36, 44], [37, 38], [37, 41]]}
# gained: {"lines": [33, 35, 36, 37, 38, 39, 41, 42, 44], "branches": [[36, 37], [36, 44], [37, 38], [37, 41]]}

import pytest
from typed_ast import ast3 as ast
from py_backwards.transformers.dict_unpacking import DictUnpackingTransformer
from py_backwards.transformers.base import BaseNodeTransformer
from typing import Optional, Tuple, List, Union

Pair = Tuple[Optional[ast.expr], ast.expr]
Splitted = List[Union[List[Tuple[ast.expr, ast.expr]], ast.expr]]

class TestDictUnpackingTransformer:
    @pytest.fixture
    def transformer(self):
        return DictUnpackingTransformer(None)

    def test_split_by_None_all_keys_none(self, transformer):
        pairs = [(None, ast.Constant(value=1)), (None, ast.Constant(value=2))]
        result = transformer._split_by_None(pairs)
        assert len(result) == 5
        assert isinstance(result[0], list) and result[0] == []
        assert isinstance(result[1], ast.Constant) and result[1].value == 1
        assert isinstance(result[2], list) and result[2] == []
        assert isinstance(result[3], ast.Constant) and result[3].value == 2
        assert isinstance(result[4], list) and result[4] == []

    def test_split_by_None_no_keys_none(self, transformer):
        pairs = [(ast.Constant(value='a'), ast.Constant(value=1)), (ast.Constant(value='b'), ast.Constant(value=2))]
        result = transformer._split_by_None(pairs)
        assert len(result) == 1
        assert isinstance(result[0], list)
        assert len(result[0]) == 2
        assert result[0][0][0].value == 'a' and result[0][0][1].value == 1
        assert result[0][1][0].value == 'b' and result[0][1][1].value == 2

    def test_split_by_None_mixed_keys(self, transformer):
        pairs = [(ast.Constant(value='a'), ast.Constant(value=1)), (None, ast.Constant(value=2)), (ast.Constant(value='b'), ast.Constant(value=3))]
        result = transformer._split_by_None(pairs)
        assert len(result) == 3
        assert isinstance(result[0], list)
        assert len(result[0]) == 1
        assert result[0][0][0].value == 'a' and result[0][0][1].value == 1
        assert isinstance(result[1], ast.Constant) and result[1].value == 2
        assert isinstance(result[2], list)
        assert len(result[2]) == 1
        assert result[2][0][0].value == 'b' and result[2][0][1].value == 3

    def test_split_by_None_empty_pairs(self, transformer):
        pairs = []
        result = transformer._split_by_None(pairs)
        assert result == [[]]
