# file: string_utils/manipulation.py:561-595
# asked: {"lines": [561, 595], "branches": []}
# gained: {"lines": [561, 595], "branches": []}

import pytest
from string_utils.manipulation import compress

def test_compress_valid_input():
    original = ' '.join(['word n{}'.format(n) for n in range(20)])
    compressed = compress(original)
    assert isinstance(compressed, str)
    assert len(compressed) < len(original)

def test_compress_empty_input():
    with pytest.raises(ValueError):
        compress("")

def test_compress_invalid_compression_level():
    original = ' '.join(['word n{}'.format(n) for n in range(20)])
    with pytest.raises(ValueError):
        compress(original, compression_level=10)
    with pytest.raises(ValueError):
        compress(original, compression_level=-1)
    with pytest.raises(ValueError):
        compress(original, compression_level="high")

def test_compress_different_encodings():
    original = ' '.join(['word n{}'.format(n) for n in range(20)])
    compressed_utf16 = compress(original, encoding='utf-16')
    assert isinstance(compressed_utf16, str)
    assert len(compressed_utf16) < len(original)

    compressed_ascii = compress(original, encoding='ascii')
    assert isinstance(compressed_ascii, str)
    assert len(compressed_ascii) < len(original)
