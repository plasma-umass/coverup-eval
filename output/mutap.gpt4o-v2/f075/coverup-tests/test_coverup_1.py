# file: f075/__init__.py:1-19
# asked: {"lines": [1, 3, 4, 5, 6, 7, 12, 13, 14, 15, 16, 17, 18, 19], "branches": [[4, 5], [4, 7], [5, 4], [5, 6], [12, 13], [12, 19], [13, 13], [13, 14], [14, 12], [14, 15], [15, 15], [15, 16], [16, 14], [16, 17], [17, 17], [17, 18], [18, 16], [18, 18]]}
# gained: {"lines": [1, 3, 4, 5, 6, 7, 12, 13, 14, 15, 16, 17, 18, 19], "branches": [[4, 5], [4, 7], [5, 4], [5, 6], [12, 13], [12, 19], [13, 13], [13, 14], [14, 12], [14, 15], [15, 15], [15, 16], [16, 14], [16, 17], [17, 17], [17, 18], [18, 16], [18, 18]]}

import pytest
from f075 import is_multiply_prime

def test_is_multiply_prime_true():
    assert is_multiply_prime(30) == True  # 2 * 3 * 5

def test_is_multiply_prime_false():
    assert is_multiply_prime(31) == False  # 31 is a prime number, not a product of three primes

def test_is_multiply_prime_edge_case():
    assert is_multiply_prime(8) == True  # 8 is 2*2*2, and 2 is considered prime in this context

def test_is_multiply_prime_large_prime():
    assert is_multiply_prime(1000003) == False  # Large prime number, not a product of three primes

def test_is_multiply_prime_product_of_non_primes():
    assert is_multiply_prime(60) == False  # 60 is 2*2*3*5, not a product of exactly three primes
