# file: f155/__init__.py:1-10
# asked: {"lines": [1, 3, 4, 5, 6, 7, 9, 10], "branches": [[5, 6], [5, 10], [6, 7], [6, 9]]}
# gained: {"lines": [1, 3, 4, 5, 6, 7, 9, 10], "branches": [[5, 6], [5, 10], [6, 7], [6, 9]]}

import pytest
from f155 import even_odd_count

def test_even_odd_count_all_even():
    result = even_odd_count(2468)
    assert result == (4, 0)

def test_even_odd_count_all_odd():
    result = even_odd_count(1357)
    assert result == (0, 4)

def test_even_odd_count_mixed():
    result = even_odd_count(123456)
    assert result == (3, 3)

def test_even_odd_count_negative():
    result = even_odd_count(-123456)
    assert result == (3, 3)

def test_even_odd_count_zero():
    result = even_odd_count(0)
    assert result == (1, 0)
