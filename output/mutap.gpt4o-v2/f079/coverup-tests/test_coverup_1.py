# file: f079/__init__.py:1-3
# asked: {"lines": [1, 3], "branches": []}
# gained: {"lines": [1, 3], "branches": []}

import pytest
from f079 import decimal_to_binary

def test_decimal_to_binary():
    # Test with a positive integer
    result = decimal_to_binary(10)
    assert result == 'db1010db'
    
    # Test with zero
    result = decimal_to_binary(0)
    assert result == 'db0db'
    
    # Test with a negative integer
    result = decimal_to_binary(-10)
    assert result == 'dbb1010db'

    # Test with a large integer
    result = decimal_to_binary(1024)
    assert result == 'db10000000000db'
