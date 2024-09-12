# file: f138/__init__.py:1-3
# asked: {"lines": [1, 3], "branches": []}
# gained: {"lines": [1, 3], "branches": []}

import pytest
from f138 import is_equal_to_sum_even

def test_is_equal_to_sum_even_even_and_greater_than_8():
    assert is_equal_to_sum_even(10) == True

def test_is_equal_to_sum_even_even_and_less_than_8():
    assert is_equal_to_sum_even(6) == False

def test_is_equal_to_sum_even_odd_and_greater_than_8():
    assert is_equal_to_sum_even(9) == False

def test_is_equal_to_sum_even_odd_and_less_than_8():
    assert is_equal_to_sum_even(5) == False
