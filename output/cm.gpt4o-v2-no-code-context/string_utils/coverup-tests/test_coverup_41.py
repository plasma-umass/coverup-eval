# file: string_utils/manipulation.py:598-608
# asked: {"lines": [598, 608], "branches": []}
# gained: {"lines": [598, 608], "branches": []}

import pytest
import zlib
import base64
from string_utils.manipulation import decompress

def test_decompress_valid_input():
    original_string = "test"
    compressed_string = base64.urlsafe_b64encode(zlib.compress(original_string.encode('utf-8'))).decode('utf-8')
    expected_output = original_string
    assert decompress(compressed_string) == expected_output

def test_decompress_invalid_input():
    invalid_compressed_string = "invalid"
    with pytest.raises(Exception):
        decompress(invalid_compressed_string)

def test_decompress_with_encoding():
    original_string = "test"
    compressed_string = base64.urlsafe_b64encode(zlib.compress(original_string.encode('utf-8'))).decode('utf-8')
    expected_output = original_string
    assert decompress(compressed_string, encoding='utf-8') == expected_output
