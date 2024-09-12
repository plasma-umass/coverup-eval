# file: f034/__init__.py:1-3
# asked: {"lines": [1, 3], "branches": []}
# gained: {"lines": [1, 3], "branches": []}

import pytest
from f034 import unique

def test_unique():
    # Test with a list containing duplicates
    input_list = [3, 1, 2, 3, 2, 1]
    expected_output = [1, 2, 3]
    assert unique(input_list) == expected_output

    # Test with an empty list
    input_list = []
    expected_output = []
    assert unique(input_list) == expected_output

    # Test with a list with all unique elements
    input_list = [5, 3, 1, 4, 2]
    expected_output = [1, 2, 3, 4, 5]
    assert unique(input_list) == expected_output

    # Test with a list with one element
    input_list = [1]
    expected_output = [1]
    assert unique(input_list) == expected_output
