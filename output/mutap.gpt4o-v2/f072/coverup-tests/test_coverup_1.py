# file: f072/__init__.py:1-12
# asked: {"lines": [1, 3, 4, 6, 7, 8, 9, 10, 11, 12], "branches": [[3, 4], [3, 6], [7, 8], [7, 12], [8, 9], [8, 10]]}
# gained: {"lines": [1, 3, 4, 6, 7, 8, 9, 10, 11, 12], "branches": [[3, 4], [3, 6], [7, 8], [7, 12], [8, 9], [8, 10]]}

import pytest
from f072 import will_it_fly

def test_will_it_fly_sum_greater_than_w():
    assert not will_it_fly([1, 2, 3], 5)

def test_will_it_fly_not_palindrome():
    assert not will_it_fly([1, 2, 3, 4], 10)

def test_will_it_fly_palindrome():
    assert will_it_fly([1, 2, 2, 1], 10)

def test_will_it_fly_empty_list():
    assert will_it_fly([], 0)
