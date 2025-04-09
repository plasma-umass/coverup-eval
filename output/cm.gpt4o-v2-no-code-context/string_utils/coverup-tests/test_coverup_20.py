# file: string_utils/manipulation.py:195-209
# asked: {"lines": [195, 196, 197, 201, 204, 207, 209], "branches": []}
# gained: {"lines": [195, 196, 197, 201, 204, 207, 209], "branches": []}

import pytest
import base64
import zlib
from string_utils.manipulation import __StringCompressor

def test_decompress_valid_input():
    # Arrange
    original_string = "This is a test string."
    encoding = 'utf-8'
    
    # Compress the original string to create a valid input for decompression
    compressed_bytes = zlib.compress(original_string.encode(encoding))
    compressed_string = base64.urlsafe_b64encode(compressed_bytes).decode(encoding)
    
    # Act
    result = __StringCompressor.decompress(compressed_string, encoding)
    
    # Assert
    assert result == original_string

def test_decompress_invalid_base64(monkeypatch):
    # Arrange
    invalid_base64_string = "!!!invalid_base64!!!"
    encoding = 'utf-8'
    
    # Act & Assert
    with pytest.raises(Exception):
        __StringCompressor.decompress(invalid_base64_string, encoding)

def test_decompress_invalid_zlib(monkeypatch):
    # Arrange
    invalid_zlib_string = base64.urlsafe_b64encode(b"invalid_zlib").decode('utf-8')
    encoding = 'utf-8'
    
    # Act & Assert
    with pytest.raises(Exception):
        __StringCompressor.decompress(invalid_zlib_string, encoding)
