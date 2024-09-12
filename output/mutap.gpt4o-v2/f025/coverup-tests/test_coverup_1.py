# file: f025/__init__.py:4-18
# asked: {"lines": [4, 6, 7, 8, 9, 10, 11, 12, 14, 16, 17, 18], "branches": [[9, 10], [9, 16], [10, 11], [10, 14], [16, 17], [16, 18]]}
# gained: {"lines": [4, 6, 7, 8, 9, 10, 11, 12, 14, 16, 17, 18], "branches": [[9, 10], [9, 16], [10, 11], [10, 14], [16, 17], [16, 18]]}

import pytest
from f025 import factorize

def test_factorize_prime():
    assert factorize(13) == [13]

def test_factorize_composite():
    assert factorize(28) == [2, 2, 7]

def test_factorize_one():
    assert factorize(1) == []

def test_factorize_large_prime():
    assert factorize(97) == [97]

def test_factorize_large_composite():
    assert factorize(100) == [2, 2, 5, 5]
