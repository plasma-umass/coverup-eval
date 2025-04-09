# file string_utils/manipulation.py:598-608
# lines [598, 608]
# branches []

import pytest
from string_utils.manipulation import decompress

class MockStringCompressor:
    @staticmethod
    def decompress(input_string, encoding):
        assert input_string == "compressed_data"
        assert encoding == "utf-8"
        return "decompressed_data"

@pytest.fixture
def mock_string_compressor(mocker):
    mocker.patch('string_utils.manipulation.__StringCompressor', new=MockStringCompressor)

def test_decompress(mock_string_compressor):
    result = decompress("compressed_data")
    assert result == "decompressed_data"
