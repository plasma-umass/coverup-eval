# file: py_backwards/transformers/starred_unpacking.py:60-64
# asked: {"lines": [60, 62, 63, 64], "branches": []}
# gained: {"lines": [60, 62, 63, 64], "branches": []}

import pytest
import ast
from py_backwards.transformers.starred_unpacking import StarredUnpackingTransformer
from py_backwards.transformers.base import BaseNodeTransformer

class MockTree:
    pass

class TestStarredUnpackingTransformer:
    @pytest.fixture
    def transformer(self):
        return StarredUnpackingTransformer(MockTree())

    def test_to_sum_of_lists(self, transformer, mocker):
        # Mocking the methods _split_by_starred, _prepare_lists, and _merge_lists
        mock_split_by_starred = mocker.patch.object(transformer, '_split_by_starred', return_value=['a', 'b'])
        mock_prepare_lists = mocker.patch.object(transformer, '_prepare_lists', return_value=['c', 'd'])
        mock_merge_lists = mocker.patch.object(transformer, '_merge_lists', return_value='result')

        xs = [ast.Constant(value=1), ast.Constant(value=2)]
        result = transformer._to_sum_of_lists(xs)

        # Assertions to verify the correct execution and return value
        mock_split_by_starred.assert_called_once_with(xs)
        mock_prepare_lists.assert_called_once_with(['a', 'b'])
        mock_merge_lists.assert_called_once_with(['c', 'd'])
        assert result == 'result'
