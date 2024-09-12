# file: string_utils/manipulation.py:195-209
# asked: {"lines": [195, 196, 197, 201, 204, 207, 209], "branches": []}
# gained: {"lines": [195, 196, 197, 201, 204, 207, 209], "branches": []}

import pytest
import base64
import zlib
from string_utils.manipulation import __StringCompressor
from string_utils.errors import InvalidInputError

def test_decompress_valid_input():
    original_string = "This is a test string"
    compressed_bytes = zlib.compress(original_string.encode('utf-8'))
    compressed_string = base64.urlsafe_b64encode(compressed_bytes).decode('utf-8')
    
    decompressed_string = __StringCompressor.decompress(compressed_string, 'utf-8')
    
    assert decompressed_string == original_string

def test_decompress_invalid_input_not_string():
    with pytest.raises(InvalidInputError):
        __StringCompressor.decompress(12345, 'utf-8')

def test_decompress_invalid_input_empty_string():
    with pytest.raises(ValueError, match='Input string cannot be empty'):
        __StringCompressor.decompress('', 'utf-8')

def test_decompress_invalid_encoding():
    original_string = "This is a test string"
    compressed_bytes = zlib.compress(original_string.encode('utf-8'))
    compressed_string = base64.urlsafe_b64encode(compressed_bytes).decode('utf-8')
    
    with pytest.raises(ValueError, match='Invalid encoding'):
        __StringCompressor.decompress(compressed_string, 12345)
