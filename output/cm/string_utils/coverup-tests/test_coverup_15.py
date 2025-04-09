# file string_utils/manipulation.py:561-595
# lines [561, 595]
# branches []

import pytest
from string_utils.manipulation import compress

def test_compress_empty_string_raises_value_error():
    with pytest.raises(ValueError):
        compress('')

def test_compress_with_different_compression_levels():
    original = 'This is a test string to be compressed'
    compressed_level_9 = compress(original, compression_level=9)
    compressed_level_0 = compress(original, compression_level=0)

    assert len(compressed_level_9) <= len(compressed_level_0)
    assert compressed_level_9 != original
    assert compressed_level_0 != original

def test_compress_with_non_default_encoding():
    original = 'This is a test string to be compressed'
    compressed_utf16 = compress(original, encoding='utf-16')

    assert compressed_utf16 != original
