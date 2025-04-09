# file string_utils/generation.py:63-85
# lines [63, 78, 79, 81, 82, 83, 85]
# branches ['78->79', '78->81']

import pytest
import os
import binascii
from string_utils.generation import secure_random_hex

def test_secure_random_hex_valid_input():
    byte_count = 9
    result = secure_random_hex(byte_count)
    assert isinstance(result, str)
    assert len(result) == byte_count * 2

def test_secure_random_hex_invalid_input():
    with pytest.raises(ValueError, match='byte_count must be >= 1'):
        secure_random_hex(0)
    with pytest.raises(ValueError, match='byte_count must be >= 1'):
        secure_random_hex(-1)
    with pytest.raises(ValueError, match='byte_count must be >= 1'):
        secure_random_hex('a')

def test_secure_random_hex_mocked(mocker):
    mock_urandom = mocker.patch('os.urandom', return_value=b'\x00' * 9)
    result = secure_random_hex(9)
    assert result == '00' * 9
    mock_urandom.assert_called_once_with(9)
