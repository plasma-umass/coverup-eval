# file: f031/__init__.py:1-8
# asked: {"lines": [1, 3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 5], [5, 6], [5, 8], [6, 5], [6, 7]]}
# gained: {"lines": [1, 3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 5], [5, 6], [5, 8], [6, 5], [6, 7]]}

import pytest
from f031 import is_prime

def test_is_prime_with_less_than_2():
    assert is_prime(0) == False
    assert is_prime(1) == False

def test_is_prime_with_prime_numbers():
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(5) == True
    assert is_prime(7) == True

def test_is_prime_with_non_prime_numbers():
    assert is_prime(4) == False
    assert is_prime(6) == False
    assert is_prime(8) == False
    assert is_prime(9) == False
    assert is_prime(10) == False
