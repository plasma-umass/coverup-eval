# file: f008/__init__.py:4-12
# asked: {"lines": [4, 6, 7, 9, 10, 11, 12], "branches": [[9, 10], [9, 12]]}
# gained: {"lines": [4, 6, 7, 9, 10, 11, 12], "branches": [[9, 10], [9, 12]]}

import pytest
from f008 import sum_product

def test_sum_product_empty_list():
    result = sum_product([])
    assert result == (0, 1), f"Expected (0, 1) but got {result}"

def test_sum_product_single_element():
    result = sum_product([5])
    assert result == (5, 5), f"Expected (5, 5) but got {result}"

def test_sum_product_multiple_elements():
    result = sum_product([1, 2, 3, 4])
    assert result == (10, 24), f"Expected (10, 24) but got {result}"

def test_sum_product_with_zero():
    result = sum_product([0, 1, 2, 3])
    assert result == (6, 0), f"Expected (6, 0) but got {result}"

def test_sum_product_negative_numbers():
    result = sum_product([-1, -2, -3])
    assert result == (-6, -6), f"Expected (-6, -6) but got {result}"
