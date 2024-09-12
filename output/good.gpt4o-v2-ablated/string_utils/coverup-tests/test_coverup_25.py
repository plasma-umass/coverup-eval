# file: string_utils/manipulation.py:598-608
# asked: {"lines": [598, 608], "branches": []}
# gained: {"lines": [598, 608], "branches": []}

import pytest
from string_utils.manipulation import decompress

class MockStringCompressor:
    @staticmethod
    def decompress(input_string, encoding):
        if input_string == "compressed_data":
            return "original_data"
        raise ValueError("Invalid input")

@pytest.fixture
def mock_string_compressor(monkeypatch):
    monkeypatch.setattr('string_utils.manipulation.__StringCompressor', MockStringCompressor)

def test_decompress_valid_data(mock_string_compressor):
    result = decompress("compressed_data")
    assert result == "original_data"

def test_decompress_invalid_data(mock_string_compressor):
    with pytest.raises(ValueError):
        decompress("invalid_data")
