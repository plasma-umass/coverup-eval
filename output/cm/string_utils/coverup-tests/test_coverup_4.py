# file string_utils/manipulation.py:195-209
# lines [195, 196, 197, 201, 204, 207, 209]
# branches []

import pytest
import base64
import zlib
from string_utils.manipulation import __StringCompressor

def test_decompress():
    # Prepare a string to compress and then decompress
    original_string = "Test string for decompression"
    encoded_string = original_string.encode('utf-8')
    compressed_bytes = zlib.compress(encoded_string)
    base64_encoded_compressed_string = base64.urlsafe_b64encode(compressed_bytes).decode('utf-8')

    # Decompress and check if it matches the original string
    decompressed_string = __StringCompressor.decompress(base64_encoded_compressed_string, 'utf-8')
    assert decompressed_string == original_string
