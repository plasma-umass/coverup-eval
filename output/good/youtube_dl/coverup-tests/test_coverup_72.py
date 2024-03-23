# file youtube_dl/downloader/f4m.py:48-49
# lines [49]
# branches []

import pytest
from youtube_dl.downloader.f4m import FlvReader
from youtube_dl.compat import compat_struct_unpack

def test_read_unsigned_char():
    # Create a mock FlvReader with a single byte
    flv_reader = FlvReader(b'\x01')

    # Read the unsigned char and assert the correct value is returned
    result = flv_reader.read_unsigned_char()
    assert result == 1

    # Assert that the FlvReader is now at the end of the file
    assert flv_reader.read(1) == b''

    # Clean up by closing the FlvReader
    flv_reader.close()
