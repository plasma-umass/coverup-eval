# file string_utils/manipulation.py:172-193
# lines [177]
# branches ['176->177']

import pytest
from string_utils.manipulation import __StringCompressor

def test_compress_invalid_compression_level():
    with pytest.raises(ValueError, match='Invalid compression_level: it must be an "int" between 0 and 9'):
        __StringCompressor.compress("test", compression_level=-1)
    
    with pytest.raises(ValueError, match='Invalid compression_level: it must be an "int" between 0 and 9'):
        __StringCompressor.compress("test", compression_level=10)
    
    with pytest.raises(ValueError, match='Invalid compression_level: it must be an "int" between 0 and 9'):
        __StringCompressor.compress("test", compression_level="invalid")

def test_compress_valid_compression_level():
    result = __StringCompressor.compress("test", compression_level=5)
    assert isinstance(result, str)
    assert result != ""

    result = __StringCompressor.compress("test", compression_level=0)
    assert isinstance(result, str)
    assert result != ""

    result = __StringCompressor.compress("test", compression_level=9)
    assert isinstance(result, str)
    assert result != ""
