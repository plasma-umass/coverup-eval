# file: f037/__init__.py:1-11
# asked: {"lines": [1, 3, 4, 5, 6, 7, 8, 9, 10, 11], "branches": [[7, 8], [7, 9], [9, 10], [9, 11]]}
# gained: {"lines": [1, 3, 4, 5, 6, 7, 8, 9, 10, 11], "branches": [[7, 8], [7, 9], [9, 10], [9, 11]]}

import pytest
from f037.__init__ import sort_even

def test_sort_even_even_length():
    input_list = [4, 3, 2, 1]
    expected_output = [2, 3, 4, 1]
    assert sort_even(input_list) == expected_output

def test_sort_even_odd_length():
    input_list = [4, 3, 2, 1, 0]
    expected_output = [0, 3, 2, 1, 4]
    assert sort_even(input_list) == expected_output

def test_sort_even_empty_list():
    input_list = []
    expected_output = []
    assert sort_even(input_list) == expected_output

def test_sort_even_single_element():
    input_list = [1]
    expected_output = [1]
    assert sort_even(input_list) == expected_output

def test_sort_even_two_elements():
    input_list = [2, 1]
    expected_output = [2, 1]
    assert sort_even(input_list) == expected_output
