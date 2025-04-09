# file: string_utils/manipulation.py:561-595
# asked: {"lines": [561, 595], "branches": []}
# gained: {"lines": [561, 595], "branches": []}

import pytest
from string_utils.manipulation import compress
from string_utils.errors import InvalidInputError

def test_compress_valid_string():
    original = ' '.join(['word n{}'.format(n) for n in range(20)])
    compressed = compress(original)
    assert isinstance(compressed, str)
    assert len(compressed) < len(original)

def test_compress_empty_string():
    with pytest.raises(ValueError, match='Input string cannot be empty'):
        compress('')

def test_compress_invalid_input():
    with pytest.raises(InvalidInputError, match='Expected "str", received "int"'):
        compress(123)

def test_compress_invalid_encoding():
    with pytest.raises(ValueError, match='Invalid encoding'):
        compress('test', encoding=123)

def test_compress_invalid_compression_level():
    with pytest.raises(ValueError, match='Invalid compression_level: it must be an "int" between 0 and 9'):
        compress('test', compression_level=10)
    with pytest.raises(ValueError, match='Invalid compression_level: it must be an "int" between 0 and 9'):
        compress('test', compression_level=-1)
    with pytest.raises(ValueError, match='Invalid compression_level: it must be an "int" between 0 and 9'):
        compress('test', compression_level='high')
