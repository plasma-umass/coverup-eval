# file py_backwards/transformers/starred_unpacking.py:60-64
# lines [60, 62, 63, 64]
# branches []

import ast
from py_backwards.transformers.starred_unpacking import StarredUnpackingTransformer
import pytest

class MockTree:
    pass

@pytest.fixture
def transformer():
    return StarredUnpackingTransformer(tree=MockTree())

def test_to_sum_of_lists(transformer):
    # Mocking the _split_by_starred method
    transformer._split_by_starred = lambda xs: xs
    # Mocking the _prepare_lists method
    transformer._prepare_lists = lambda xs: xs
    # Mocking the _merge_lists method
    transformer._merge_lists = lambda xs: xs

    # Creating a list of ast.expr to pass to the _to_sum_of_lists method
    expr_list = [ast.expr()]

    # Call the method we want to test
    result = transformer._to_sum_of_lists(expr_list)

    # Assertions to check the result
    assert result == expr_list, "The result should be the same as the input list"
