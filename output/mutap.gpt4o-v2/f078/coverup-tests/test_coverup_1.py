# file: f078/__init__.py:1-8
# asked: {"lines": [1, 3, 4, 5, 6, 7, 8], "branches": [[5, 6], [5, 8], [6, 5], [6, 7]]}
# gained: {"lines": [1, 3, 4, 5, 6, 7, 8], "branches": [[5, 6], [5, 8], [6, 5], [6, 7]]}

import pytest
from f078 import hex_key

def test_hex_key_all_primes():
    result = hex_key('2357BD')
    assert result == 6

def test_hex_key_no_primes():
    result = hex_key('04689A')
    assert result == 0

def test_hex_key_mixed():
    result = hex_key('1234567890ABCD')
    assert result == 6

def test_hex_key_empty():
    result = hex_key('')
    assert result == 0
