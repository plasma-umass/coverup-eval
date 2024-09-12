# file: string_utils/manipulation.py:195-209
# asked: {"lines": [195, 196, 197, 201, 204, 207, 209], "branches": []}
# gained: {"lines": [195, 196, 197, 201, 204, 207, 209], "branches": []}

import pytest
import base64
import zlib
from string_utils.manipulation import __StringCompressor

def test_decompress_valid_input():
    # Arrange
    original_string = "test string"
    compressed_bytes = zlib.compress(original_string.encode('utf-8'))
    compressed_string = base64.urlsafe_b64encode(compressed_bytes).decode('utf-8')
    
    # Act
    result = __StringCompressor.decompress(compressed_string)
    
    # Assert
    assert result == original_string

def test_decompress_invalid_base64():
    # Arrange
    invalid_base64_string = "invalid_base64"
    
    # Act & Assert
    with pytest.raises(base64.binascii.Error):
        __StringCompressor.decompress(invalid_base64_string)

def test_decompress_invalid_zlib():
    # Arrange
    invalid_zlib_string = base64.urlsafe_b64encode(b'invalid_zlib').decode('utf-8')
    
    # Act & Assert
    with pytest.raises(zlib.error):
        __StringCompressor.decompress(invalid_zlib_string)

def test_decompress_invalid_encoding():
    # Arrange
    original_string = "test string"
    compressed_bytes = zlib.compress(original_string.encode('utf-8'))
    compressed_string = base64.urlsafe_b64encode(compressed_bytes).decode('utf-8')
    
    # Act & Assert
    with pytest.raises(LookupError):
        __StringCompressor.decompress(compressed_string, encoding='invalid_encoding')
