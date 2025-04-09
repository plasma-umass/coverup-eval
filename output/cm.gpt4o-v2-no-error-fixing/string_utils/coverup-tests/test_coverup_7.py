# file: string_utils/generation.py:63-85
# asked: {"lines": [63, 78, 79, 81, 82, 83, 85], "branches": [[78, 79], [78, 81]]}
# gained: {"lines": [63, 78, 79, 81, 82, 83, 85], "branches": [[78, 79], [78, 81]]}

import pytest
import binascii
import os
from string_utils.generation import secure_random_hex

def test_secure_random_hex_valid(monkeypatch):
    def mock_urandom(n):
        return b'\x00' * n

    monkeypatch.setattr(os, 'urandom', mock_urandom)
    result = secure_random_hex(4)
    assert result == '00000000'
    assert len(result) == 8

def test_secure_random_hex_invalid_type():
    with pytest.raises(ValueError, match='byte_count must be >= 1'):
        secure_random_hex('a')

def test_secure_random_hex_invalid_value():
    with pytest.raises(ValueError, match='byte_count must be >= 1'):
        secure_random_hex(0)
