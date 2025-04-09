# file py_backwards/transformers/starred_unpacking.py:60-64
# lines [62, 63, 64]
# branches []

import pytest
import ast
from py_backwards.transformers.starred_unpacking import StarredUnpackingTransformer

class DummyTree:
    pass

@pytest.fixture
def transformer(mocker):
    tree = DummyTree()
    transformer = StarredUnpackingTransformer(tree)
    return transformer

def test_to_sum_of_lists(transformer, mocker):
    # Mocking the methods _split_by_starred and _prepare_lists
    mock_split_by_starred = mocker.patch.object(transformer, '_split_by_starred', return_value=['mocked_split'])
    mock_prepare_lists = mocker.patch.object(transformer, '_prepare_lists', return_value=['mocked_prepared'])
    mock_merge_lists = mocker.patch.object(transformer, '_merge_lists', return_value='mocked_merged')

    # Creating a dummy list of ast.expr
    dummy_expr_list = [ast.Constant(value=1), ast.Constant(value=2)]

    result = transformer._to_sum_of_lists(dummy_expr_list)

    # Assertions to verify the correct execution and postconditions
    mock_split_by_starred.assert_called_once_with(dummy_expr_list)
    mock_prepare_lists.assert_called_once_with(['mocked_split'])
    mock_merge_lists.assert_called_once_with(['mocked_prepared'])
    assert result == 'mocked_merged'
