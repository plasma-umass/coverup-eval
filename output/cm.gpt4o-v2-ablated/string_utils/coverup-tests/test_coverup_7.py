# file: string_utils/generation.py:63-85
# asked: {"lines": [63, 78, 79, 81, 82, 83, 85], "branches": [[78, 79], [78, 81]]}
# gained: {"lines": [63, 78, 79, 81, 82, 83, 85], "branches": [[78, 79], [78, 81]]}

import os
import binascii
import pytest
from string_utils.generation import secure_random_hex

def test_secure_random_hex_valid_input():
    result = secure_random_hex(4)
    assert isinstance(result, str)
    assert len(result) == 8  # 4 bytes * 2 hex chars per byte

def test_secure_random_hex_invalid_input_negative():
    with pytest.raises(ValueError, match='byte_count must be >= 1'):
        secure_random_hex(-1)

def test_secure_random_hex_invalid_input_zero():
    with pytest.raises(ValueError, match='byte_count must be >= 1'):
        secure_random_hex(0)

def test_secure_random_hex_invalid_input_non_integer():
    with pytest.raises(ValueError, match='byte_count must be >= 1'):
        secure_random_hex('a')

def test_secure_random_hex_randomness(monkeypatch):
    def mock_urandom(byte_count):
        return b'\x00' * byte_count

    monkeypatch.setattr(os, 'urandom', mock_urandom)
    result = secure_random_hex(4)
    assert result == '00000000'
