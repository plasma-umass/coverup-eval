# file: f033/__init__.py:1-5
# asked: {"lines": [1, 3, 4, 5], "branches": []}
# gained: {"lines": [1, 3, 4, 5], "branches": []}

import pytest
from f033 import sort_third

def test_sort_third():
    # Test with a list of integers
    input_list = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    expected_output = [3, 8, 7, 6, 5, 4, 9, 2, 1]
    assert sort_third(input_list) == expected_output

    # Test with an empty list
    input_list = []
    expected_output = []
    assert sort_third(input_list) == expected_output

    # Test with a list of strings
    input_list = ['c', 'b', 'a', 'f', 'e', 'd']
    expected_output = ['c', 'b', 'a', 'f', 'e', 'd']
    assert sort_third(input_list) == expected_output

    # Test with a list of mixed types
    input_list = [3, 'b', 1, 'a', 2, 'c']
    with pytest.raises(TypeError):
        sort_third(input_list)
