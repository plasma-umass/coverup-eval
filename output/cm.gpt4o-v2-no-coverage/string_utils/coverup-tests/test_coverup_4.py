# file: string_utils/generation.py:63-85
# asked: {"lines": [63, 78, 79, 81, 82, 83, 85], "branches": [[78, 79], [78, 81]]}
# gained: {"lines": [63, 78, 79, 81, 82, 83, 85], "branches": [[78, 79], [78, 81]]}

import pytest
import binascii
import os
from string_utils.generation import secure_random_hex

def test_secure_random_hex_valid_input(monkeypatch):
    # Mock os.urandom to return a predictable output
    def mock_urandom(n):
        return b'\x00' * n

    monkeypatch.setattr(os, 'urandom', mock_urandom)
    
    result = secure_random_hex(4)
    assert result == '00000000'
    assert len(result) == 8  # 4 bytes * 2 hex chars per byte

def test_secure_random_hex_invalid_input_type():
    with pytest.raises(ValueError, match='byte_count must be >= 1'):
        secure_random_hex('a')

def test_secure_random_hex_invalid_input_value():
    with pytest.raises(ValueError, match='byte_count must be >= 1'):
        secure_random_hex(0)

def test_secure_random_hex_minimum_valid_input(monkeypatch):
    # Mock os.urandom to return a predictable output
    def mock_urandom(n):
        return b'\x01' * n

    monkeypatch.setattr(os, 'urandom', mock_urandom)
    
    result = secure_random_hex(1)
    assert result == '01'
    assert len(result) == 2  # 1 byte * 2 hex chars per byte
