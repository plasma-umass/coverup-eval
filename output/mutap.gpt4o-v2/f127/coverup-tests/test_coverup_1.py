# file: f127/__init__.py:1-18
# asked: {"lines": [1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18], "branches": [[4, 5], [4, 6], [6, 7], [6, 8], [8, 9], [8, 11], [9, 8], [9, 10], [16, 17], [16, 18]]}
# gained: {"lines": [1, 3, 4, 6, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18], "branches": [[4, 6], [6, 8], [8, 9], [8, 11], [9, 8], [9, 10], [16, 17], [16, 18]]}

import pytest
from f127 import intersection

def test_intersection_prime_length():
    assert intersection((1, 10), (5, 15)) == "YES"

def test_intersection_non_prime_length():
    assert intersection((1, 10), (6, 15)) == "NO"

def test_intersection_no_overlap():
    assert intersection((1, 5), (6, 10)) == "NO"

def test_intersection_zero_length():
    assert intersection((1, 5), (5, 10)) == "NO"
