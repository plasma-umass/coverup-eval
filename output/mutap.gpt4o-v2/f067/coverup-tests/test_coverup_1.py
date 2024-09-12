# file: f067/__init__.py:1-7
# asked: {"lines": [1, 3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}
# gained: {"lines": [1, 3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}

import pytest
from f067 import fruit_distribution

def test_fruit_distribution_all_digits():
    result = fruit_distribution("1 2 3", 10)
    assert result == 4

def test_fruit_distribution_some_non_digits():
    result = fruit_distribution("1 a 2 b 3", 10)
    assert result == 4

def test_fruit_distribution_no_digits():
    result = fruit_distribution("a b c", 10)
    assert result == 10

def test_fruit_distribution_empty_string():
    result = fruit_distribution("", 10)
    assert result == 10
