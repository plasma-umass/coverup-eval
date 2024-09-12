# file: string_utils/manipulation.py:561-595
# asked: {"lines": [561, 595], "branches": []}
# gained: {"lines": [561, 595], "branches": []}

import pytest
from string_utils.manipulation import compress

class MockStringCompressor:
    @staticmethod
    def compress(input_string, encoding, compression_level):
        if not input_string:
            raise ValueError("Input string must not be empty")
        if not (0 <= compression_level <= 9):
            raise ValueError("Compression level must be between 0 and 9")
        return f"compressed({input_string})"

@pytest.fixture
def mock_compressor(monkeypatch):
    monkeypatch.setattr('string_utils.manipulation.__StringCompressor', MockStringCompressor)

def test_compress_valid_input(mock_compressor):
    original = ' '.join(['word n{}'.format(n) for n in range(20)])
    compressed = compress(original)
    assert compressed == f"compressed({original})"

def test_compress_empty_string(mock_compressor):
    with pytest.raises(ValueError, match="Input string must not be empty"):
        compress("")

def test_compress_invalid_compression_level(mock_compressor):
    original = ' '.join(['word n{}'.format(n) for n in range(20)])
    with pytest.raises(ValueError, match="Compression level must be between 0 and 9"):
        compress(original, compression_level=10)
    with pytest.raises(ValueError, match="Compression level must be between 0 and 9"):
        compress(original, compression_level=-1)

def test_compress_different_encoding(mock_compressor):
    original = ' '.join(['word n{}'.format(n) for n in range(20)])
    compressed = compress(original, encoding='ascii')
    assert compressed == f"compressed({original})"

def test_compress_no_compression(mock_compressor):
    original = ' '.join(['word n{}'.format(n) for n in range(20)])
    compressed = compress(original, compression_level=0)
    assert compressed == f"compressed({original})"
