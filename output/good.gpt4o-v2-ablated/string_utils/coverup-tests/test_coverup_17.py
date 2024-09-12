# file: string_utils/manipulation.py:172-193
# asked: {"lines": [172, 173, 174, 176, 177, 180, 183, 188, 191, 193], "branches": [[176, 177], [176, 180]]}
# gained: {"lines": [172, 173, 174, 176, 177, 180, 183, 188, 191, 193], "branches": [[176, 177], [176, 180]]}

import pytest
import zlib
import base64
from string_utils.manipulation import __StringCompressor

def test_compress_valid_input():
    input_string = "test string"
    encoding = "utf-8"
    compression_level = 5

    result = __StringCompressor.compress(input_string, encoding, compression_level)
    
    # Verify that the result is a base64 encoded string
    decoded_bytes = base64.urlsafe_b64decode(result.encode(encoding))
    decompressed_bytes = zlib.decompress(decoded_bytes)
    decompressed_string = decompressed_bytes.decode(encoding)
    
    assert decompressed_string == input_string

def test_compress_invalid_compression_level():
    input_string = "test string"
    encoding = "utf-8"
    invalid_compression_level = 10

    with pytest.raises(ValueError, match='Invalid compression_level: it must be an "int" between 0 and 9'):
        __StringCompressor.compress(input_string, encoding, invalid_compression_level)

def test_compress_invalid_compression_level_negative():
    input_string = "test string"
    encoding = "utf-8"
    invalid_compression_level = -1

    with pytest.raises(ValueError, match='Invalid compression_level: it must be an "int" between 0 and 9'):
        __StringCompressor.compress(input_string, encoding, invalid_compression_level)

def test_compress_invalid_compression_level_non_int():
    input_string = "test string"
    encoding = "utf-8"
    invalid_compression_level = "high"

    with pytest.raises(ValueError, match='Invalid compression_level: it must be an "int" between 0 and 9'):
        __StringCompressor.compress(input_string, encoding, invalid_compression_level)
