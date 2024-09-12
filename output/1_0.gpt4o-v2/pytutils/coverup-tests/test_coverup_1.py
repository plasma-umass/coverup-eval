# file: pytutils/rand.py:4-11
# asked: {"lines": [4, 11], "branches": []}
# gained: {"lines": [4, 11], "branches": []}

import pytest
import random
from pytutils.rand import rand_hex

def test_rand_hex_default_length():
    result = rand_hex()
    assert isinstance(result, str)
    assert len(result) == 8
    int(result, 16)  # Ensure it's a valid hex string

def test_rand_hex_custom_length():
    result = rand_hex(16)
    assert isinstance(result, str)
    assert len(result) == 16
    int(result, 16)  # Ensure it's a valid hex string

def test_rand_hex_zero_length():
    result = rand_hex(0)
    assert result == '0'

def test_rand_hex_negative_length():
    with pytest.raises(ValueError):
        rand_hex(-1)
