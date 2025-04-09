# file: string_utils/manipulation.py:598-608
# asked: {"lines": [598, 608], "branches": []}
# gained: {"lines": [598, 608], "branches": []}

import pytest
import base64
import zlib
from string_utils.manipulation import decompress
from string_utils.errors import InvalidInputError

def test_decompress_valid_input():
    original_string = "Hello, World!"
    compressed_bytes = zlib.compress(original_string.encode('utf-8'))
    compressed_string = base64.urlsafe_b64encode(compressed_bytes).decode('utf-8')
    
    result = decompress(compressed_string, 'utf-8')
    assert result == original_string

def test_decompress_invalid_input_not_string():
    with pytest.raises(InvalidInputError):
        decompress(12345, 'utf-8')

def test_decompress_empty_input():
    with pytest.raises(ValueError, match='Input string cannot be empty'):
        decompress('', 'utf-8')

def test_decompress_invalid_encoding():
    original_string = "Hello, World!"
    compressed_bytes = zlib.compress(original_string.encode('utf-8'))
    compressed_string = base64.urlsafe_b64encode(compressed_bytes).decode('utf-8')
    
    with pytest.raises(ValueError, match='Invalid encoding'):
        decompress(compressed_string, 12345)
