# file: f096/__init__.py:1-12
# asked: {"lines": [1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], "branches": [[4, 5], [4, 12], [6, 7], [6, 10], [7, 6], [7, 8], [10, 4], [10, 11]]}
# gained: {"lines": [1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], "branches": [[4, 5], [4, 12], [6, 7], [6, 10], [7, 6], [7, 8], [10, 4], [10, 11]]}

import pytest
from f096 import count_up_to

def test_count_up_to_no_primes():
    assert count_up_to(2) == []

def test_count_up_to_single_prime():
    assert count_up_to(3) == [2]

def test_count_up_to_multiple_primes():
    assert count_up_to(10) == [2, 3, 5, 7]

def test_count_up_to_no_primes_in_range():
    assert count_up_to(4) == [2, 3]

def test_count_up_to_large_number():
    primes = count_up_to(20)
    assert primes == [2, 3, 5, 7, 11, 13, 17, 19]
