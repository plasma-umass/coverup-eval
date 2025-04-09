# file: string_utils/manipulation.py:561-595
# asked: {"lines": [561, 595], "branches": []}
# gained: {"lines": [561, 595], "branches": []}

import pytest
from string_utils.manipulation import compress

def test_compress_valid_string():
    original = ' '.join(['word n{}'.format(n) for n in range(20)])
    compressed = compress(original)
    assert isinstance(compressed, str)
    assert len(compressed) < len(original)

def test_compress_empty_string():
    with pytest.raises(ValueError):
        compress('')

def test_compress_different_encoding():
    original = ' '.join(['word n{}'.format(n) for n in range(20)])
    compressed = compress(original, encoding='ascii')
    assert isinstance(compressed, str)
    assert len(compressed) < len(original)

def test_compress_no_compression():
    original = ' '.join(['word n{}'.format(n) for n in range(20)])
    compressed = compress(original, compression_level=0)
    assert isinstance(compressed, str)
    assert len(compressed) >= len(original)

def test_compress_best_compression():
    original = ' '.join(['word n{}'.format(n) for n in range(20)])
    compressed = compress(original, compression_level=9)
    assert isinstance(compressed, str)
    assert len(compressed) < len(original)
