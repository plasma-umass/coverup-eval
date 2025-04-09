# file: string_utils/manipulation.py:172-193
# asked: {"lines": [172, 173, 174, 176, 177, 180, 183, 188, 191, 193], "branches": [[176, 177], [176, 180]]}
# gained: {"lines": [172, 173, 174, 176, 177, 180, 183, 188, 191, 193], "branches": [[176, 177], [176, 180]]}

import pytest
import zlib
import base64
from string_utils.manipulation import __StringCompressor

def test_compress_valid_input():
    input_string = "This is a test string"
    result = __StringCompressor.compress(input_string)
    assert isinstance(result, str)
    assert result != input_string

def test_compress_invalid_compression_level(monkeypatch):
    input_string = "This is a test string"
    with pytest.raises(ValueError, match='Invalid compression_level: it must be an "int" between 0 and 9'):
        __StringCompressor.compress(input_string, compression_level=10)

def test_compress_invalid_compression_level_negative(monkeypatch):
    input_string = "This is a test string"
    with pytest.raises(ValueError, match='Invalid compression_level: it must be an "int" between 0 and 9'):
        __StringCompressor.compress(input_string, compression_level=-1)

def test_compress_invalid_compression_level_non_int(monkeypatch):
    input_string = "This is a test string"
    with pytest.raises(ValueError, match='Invalid compression_level: it must be an "int" between 0 and 9'):
        __StringCompressor.compress(input_string, compression_level="high")

def test_compress_different_encoding():
    input_string = "This is a test string"
    result = __StringCompressor.compress(input_string, encoding='utf-16')
    assert isinstance(result, str)
    assert result != input_string

def test_compress_empty_string():
    input_string = ""
    with pytest.raises(ValueError, match='Input string cannot be empty'):
        __StringCompressor.compress(input_string)

@pytest.fixture(autouse=True)
def cleanup():
    yield
    # Add any necessary cleanup code here
