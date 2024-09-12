# file: f121/__init__.py:1-3
# asked: {"lines": [1, 3], "branches": []}
# gained: {"lines": [1, 3], "branches": []}

import pytest
from f121 import solution

def test_solution_all_odd_indices():
    assert solution([1, 2, 3, 4, 5, 6]) == 9  # 1 + 5

def test_solution_no_odd_indices():
    assert solution([2, 4, 6, 8, 10]) == 0

def test_solution_mixed_indices():
    assert solution([1, 3, 5, 7, 9, 11]) == 15  # 1 + 5 + 9

def test_solution_empty_list():
    assert solution([]) == 0

def test_solution_single_odd_element():
    assert solution([1]) == 1

def test_solution_single_even_element():
    assert solution([2]) == 0
