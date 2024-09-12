# file: f094/__init__.py:1-16
# asked: {"lines": [1, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16], "branches": [[4, 5], [4, 8], [5, 4], [5, 6], [11, 12], [11, 15], [12, 13], [12, 14]]}
# gained: {"lines": [1, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16], "branches": [[4, 5], [4, 8], [5, 4], [5, 6], [11, 12], [11, 15], [12, 13], [12, 14]]}

import pytest
from f094 import skjkasdkd

def test_skjkasdkd_with_primes():
    lst = [2, 3, 5, 7, 11]
    result = skjkasdkd(lst)
    assert result == 2  # 11 is the largest prime, sum of digits is 1+1=2

def test_skjkasdkd_with_non_primes():
    lst = [4, 6, 8, 9, 10]
    result = skjkasdkd(lst)
    assert result == 0  # No primes, maxx remains 0, sum of digits is 0

def test_skjkasdkd_with_mixed():
    lst = [4, 6, 7, 8, 10]
    result = skjkasdkd(lst)
    assert result == 7  # 7 is the largest prime, sum of digits is 7

def test_skjkasdkd_with_empty_list():
    lst = []
    result = skjkasdkd(lst)
    assert result == 0  # Empty list, maxx remains 0, sum of digits is 0

def test_skjkasdkd_with_large_numbers():
    lst = [29, 15, 23, 19, 31]
    result = skjkasdkd(lst)
    assert result == 4  # 31 is the largest prime, sum of digits is 3+1=4
