# file: f103/__init__.py:1-8
# asked: {"lines": [1, 3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 5], [6, 7], [6, 8]]}
# gained: {"lines": [1, 3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 5], [6, 7], [6, 8]]}

import pytest
from f103 import rounded_avg

def test_rounded_avg_m_less_than_n():
    assert rounded_avg(5, 3) == -1

def test_rounded_avg_single_value():
    assert rounded_avg(3, 3) == bin(3)

def test_rounded_avg_multiple_values():
    assert rounded_avg(1, 5) == bin(round((1 + 2 + 3 + 4 + 5) / 5))

def test_rounded_avg_negative_values():
    assert rounded_avg(-3, -1) == bin(round((-3 + -2 + -1) / 3))
