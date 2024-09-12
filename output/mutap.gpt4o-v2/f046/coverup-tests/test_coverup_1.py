# file: f046/__init__.py:1-11
# asked: {"lines": [1, 3, 4, 5, 7, 8, 9, 11], "branches": [[4, 5], [4, 7], [7, 8], [7, 11]]}
# gained: {"lines": [1, 3, 4, 5, 7, 8, 9, 11], "branches": [[4, 5], [4, 7], [7, 8], [7, 11]]}

import pytest
from f046 import fib4

def test_fib4_base_cases():
    assert fib4(0) == 0
    assert fib4(1) == 0
    assert fib4(2) == 2
    assert fib4(3) == 0

def test_fib4_recursive_case():
    assert fib4(4) == 2
    assert fib4(5) == 4
    assert fib4(6) == 8
    assert fib4(7) == 14

def test_fib4_large_input():
    assert fib4(10) == 104
    assert fib4(15) == 2764
