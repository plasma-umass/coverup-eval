# file: string_utils/manipulation.py:598-608
# asked: {"lines": [598, 608], "branches": []}
# gained: {"lines": [598, 608], "branches": []}

import pytest
from string_utils.manipulation import decompress
from string_utils.manipulation import __StringCompressor

def test_decompress_valid_input():
    # Compress the string "test" to ensure we have a valid compressed string
    original_string = 'test'
    compressed_string = __StringCompressor.compress(original_string)
    expected_output = original_string
    
    result = decompress(compressed_string)
    assert result == expected_output

def test_decompress_invalid_base64():
    invalid_compressed_string = 'invalid_base64_string'
    
    with pytest.raises(Exception):
        decompress(invalid_compressed_string)

def test_decompress_invalid_zlib():
    # This is a valid base64 string but invalid zlib compressed data
    invalid_compressed_string = 'aW52YWxpZF96bGli'
    
    with pytest.raises(Exception):
        decompress(invalid_compressed_string)
