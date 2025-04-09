# file string_utils/manipulation.py:172-193
# lines [172, 173, 174, 176, 177, 180, 183, 188, 191, 193]
# branches ['176->177', '176->180']

import pytest
import zlib
import base64
from string_utils.manipulation import __StringCompressor

def test_string_compressor_invalid_compression_level():
    with pytest.raises(ValueError) as excinfo:
        __StringCompressor.compress("test string", compression_level=10)
    assert "Invalid compression_level: it must be an \"int\" between 0 and 9" in str(excinfo.value)

def test_string_compressor_invalid_compression_level_negative():
    with pytest.raises(ValueError) as excinfo:
        __StringCompressor.compress("test string", compression_level=-1)
    assert "Invalid compression_level: it must be an \"int\" between 0 and 9" in str(excinfo.value)

def test_string_compressor_invalid_compression_level_not_int():
    with pytest.raises(ValueError) as excinfo:
        __StringCompressor.compress("test string", compression_level="high")
    assert "Invalid compression_level: it must be an \"int\" between 0 and 9" in str(excinfo.value)
