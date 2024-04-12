# file youtube_dl/downloader/f4m.py:42-43
# lines [43]
# branches []

import pytest
from youtube_dl.downloader.f4m import FlvReader
from youtube_dl.compat import compat_struct_unpack

class TestFlvReader:
    def test_read_unsigned_long_long(self, mocker):
        # Mock the read_bytes method to return a specific 8-byte value
        mocker.patch.object(FlvReader, 'read_bytes', return_value=b'\x00\x00\x00\x00\x00\x00\x00\x01')

        # Create an instance of FlvReader
        flv_reader = FlvReader()

        # Call the method under test
        result = flv_reader.read_unsigned_long_long()

        # Assert that the result is the expected unsigned long long value
        assert result == 1, "The read_unsigned_long_long method should return the correct unsigned long long value"

        # Assert that read_bytes was called with the correct argument
        flv_reader.read_bytes.assert_called_once_with(8)
