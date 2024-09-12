# file: f059/__init__.py:1-14
# asked: {"lines": [1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], "branches": [[4, 5], [4, 6], [6, 7], [6, 9], [7, 6], [7, 8], [11, 12], [11, 14], [12, 11], [12, 13]]}
# gained: {"lines": [1, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14], "branches": [[4, 6], [6, 7], [6, 9], [7, 6], [7, 8], [11, 12], [11, 14], [12, 11], [12, 13]]}

import pytest
from f059 import largest_prime_factor

def test_largest_prime_factor():
    assert largest_prime_factor(10) == 5
    assert largest_prime_factor(15) == 5
    assert largest_prime_factor(21) == 7
    assert largest_prime_factor(1) == 1
    assert largest_prime_factor(0) == 1
    assert largest_prime_factor(-10) == 1
