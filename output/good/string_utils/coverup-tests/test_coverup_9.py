# file string_utils/generation.py:63-85
# lines [63, 78, 79, 81, 82, 83, 85]
# branches ['78->79', '78->81']

import pytest
import os
from string_utils.generation import secure_random_hex

def test_secure_random_hex_valid_input():
    # Test with valid input
    hex_str = secure_random_hex(8)
    assert len(hex_str) == 16  # Should be double the byte_count
    assert all(c in '0123456789abcdef' for c in hex_str.lower())

def test_secure_random_hex_invalid_input():
    # Test with invalid input
    with pytest.raises(ValueError) as exc_info:
        secure_random_hex(0)
    assert str(exc_info.value) == 'byte_count must be >= 1'

    with pytest.raises(ValueError) as exc_info:
        secure_random_hex(-1)
    assert str(exc_info.value) == 'byte_count must be >= 1'

    with pytest.raises(ValueError) as exc_info:
        secure_random_hex('invalid')
    assert str(exc_info.value) == 'byte_count must be >= 1'
