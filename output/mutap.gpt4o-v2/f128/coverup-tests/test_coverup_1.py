# file: f128/__init__.py:1-6
# asked: {"lines": [1, 3, 4, 5, 6], "branches": [[3, 4], [3, 5]]}
# gained: {"lines": [1, 3, 4, 5, 6], "branches": [[3, 4], [3, 5]]}

import pytest
from f128.__init__ import prod_signs

def test_prod_signs_empty_array():
    assert prod_signs([]) is None

def test_prod_signs_with_zero():
    assert prod_signs([0, 1, -2]) == 0

def test_prod_signs_all_positive():
    assert prod_signs([1, 2, 3]) == 6

def test_prod_signs_all_negative():
    assert prod_signs([-1, -2, -3]) == -6

def test_prod_signs_mixed_signs():
    assert prod_signs([-1, 2, -3, 4]) == 10
