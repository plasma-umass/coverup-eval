# file pytutils/rand.py:4-11
# lines [4, 11]
# branches []

import pytest
from pytutils.rand import rand_hex

def test_rand_hex_default_length():
    hex_str = rand_hex()
    assert len(hex_str) == 8
    assert int(hex_str, 16) >= 0

def test_rand_hex_custom_length():
    custom_length = 16
    hex_str = rand_hex(custom_length)
    assert len(hex_str) == custom_length
    assert int(hex_str, 16) >= 0

def test_rand_hex_zero_length():
    hex_str = rand_hex(1)
    assert len(hex_str) == 1
    assert int(hex_str, 16) >= 0
