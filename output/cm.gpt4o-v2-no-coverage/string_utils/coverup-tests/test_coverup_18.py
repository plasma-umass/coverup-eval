# file: string_utils/manipulation.py:172-193
# asked: {"lines": [172, 173, 174, 176, 177, 180, 183, 188, 191, 193], "branches": [[176, 177], [176, 180]]}
# gained: {"lines": [172, 173, 174, 176, 177, 180, 183, 188, 191, 193], "branches": [[176, 177], [176, 180]]}

import pytest
from string_utils.manipulation import __StringCompressor
from string_utils.errors import InvalidInputError

def test_compress_valid_input():
    result = __StringCompressor.compress("test string")
    assert isinstance(result, str)
    assert result != ""

def test_compress_invalid_compression_level():
    with pytest.raises(ValueError, match='Invalid compression_level: it must be an "int" between 0 and 9'):
        __StringCompressor.compress("test string", compression_level=10)

def test_compress_invalid_input_string():
    with pytest.raises(InvalidInputError):
        __StringCompressor.compress(12345)

def test_compress_empty_input_string():
    with pytest.raises(ValueError, match='Input string cannot be empty'):
        __StringCompressor.compress("")

def test_compress_invalid_encoding():
    with pytest.raises(ValueError, match='Invalid encoding'):
        __StringCompressor.compress("test string", encoding=12345)
