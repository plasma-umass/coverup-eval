# file: f039/__init__.py:1-18
# asked: {"lines": [1, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], "branches": [[6, 7], [6, 8], [8, 9], [8, 11], [9, 8], [9, 10], [13, 14], [15, 16], [15, 17], [17, 13], [17, 18]]}
# gained: {"lines": [1, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], "branches": [[6, 7], [6, 8], [8, 9], [8, 11], [9, 8], [9, 10], [13, 14], [15, 16], [15, 17], [17, 13], [17, 18]]}

import pytest
from f039 import prime_fib

def test_prime_fib():
    assert prime_fib(1) == 2
    assert prime_fib(2) == 3
    assert prime_fib(3) == 5
    assert prime_fib(4) == 13

def test_is_prime():
    from f039.__init__ import prime_fib
    import math

    def is_prime(p):
        if p < 2:
            return False
        for k in range(2, min(int(math.sqrt(p)) + 1, p - 1)):
            if p % k == 0:
                return False
        return True
    
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(4) == False
    assert is_prime(5) == True
    assert is_prime(9) == False
