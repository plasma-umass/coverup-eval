# file: f092/__init__.py:1-8
# asked: {"lines": [1, 4, 5, 6, 7, 8], "branches": [[4, 5], [4, 8], [5, 6], [5, 7]]}
# gained: {"lines": [1, 4, 5, 6, 7, 8], "branches": [[4, 5], [4, 8], [5, 6], [5, 7]]}

import pytest
from f092 import any_int

def test_any_int_all_ints_sum_equal():
    assert any_int(1, 2, 3) == True
    assert any_int(3, 1, 2) == True
    assert any_int(2, 3, 1) == True

def test_any_int_all_ints_no_sum_equal():
    assert any_int(1, 2, 4) == False
    assert any_int(4, 1, 2) == False
    assert any_int(2, 4, 1) == False

def test_any_int_not_all_ints():
    assert any_int(1, 2, '3') == False
    assert any_int('1', 2, 3) == False
    assert any_int(1, '2', 3) == False
