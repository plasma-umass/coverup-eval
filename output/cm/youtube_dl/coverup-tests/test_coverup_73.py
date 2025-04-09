# file youtube_dl/downloader/f4m.py:45-46
# lines [46]
# branches []

import pytest
from youtube_dl.downloader.f4m import FlvReader
from youtube_dl.compat import compat_struct_unpack

@pytest.fixture
def flv_reader():
    # Create a FlvReader instance with 4 bytes of data
    data = b'\x00\x00\x00\x01'
    reader = FlvReader(data)
    return reader

def test_read_unsigned_int(flv_reader):
    # Test the read_unsigned_int method
    result = flv_reader.read_unsigned_int()
    expected = 1  # The unsigned int representation of b'\x00\x00\x00\x01'
    assert result == expected, "The read_unsigned_int method did not return the expected value"
