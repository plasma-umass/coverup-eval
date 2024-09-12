# file: f065/__init__.py:1-7
# asked: {"lines": [1, 3, 4, 5, 7], "branches": [[4, 5], [4, 7]]}
# gained: {"lines": [1, 3, 4, 5, 7], "branches": [[4, 5], [4, 7]]}

import pytest
from f065 import circular_shift

def test_circular_shift_no_shift():
    assert circular_shift(12345, 0) == '12345'

def test_circular_shift_less_than_length():
    assert circular_shift(12345, 2) == '45123'

def test_circular_shift_equal_to_length():
    assert circular_shift(12345, 5) == '12345'

def test_circular_shift_more_than_length():
    assert circular_shift(12345, 6) == '54321'

def test_circular_shift_string_input():
    assert circular_shift('abcdef', 2) == 'efabcd'

def test_circular_shift_string_more_than_length():
    assert circular_shift('abcdef', 7) == 'fedcba'
