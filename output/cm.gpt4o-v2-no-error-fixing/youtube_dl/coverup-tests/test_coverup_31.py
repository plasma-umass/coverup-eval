# file: youtube_dl/downloader/f4m.py:45-46
# asked: {"lines": [46], "branches": []}
# gained: {"lines": [46], "branches": []}

import pytest
from youtube_dl.downloader.f4m import FlvReader
from youtube_dl.compat import compat_struct_unpack

class TestFlvReader:
    def test_read_unsigned_int(self):
        # Create a FlvReader instance with 4 bytes of data
        data = b'\x00\x00\x00\x01'  # This represents the unsigned int 1
        reader = FlvReader(data)
        
        # Call read_unsigned_int and assert the result
        result = reader.read_unsigned_int()
        assert result == 1

    def test_read_unsigned_int_incomplete_data(self):
        # Create a FlvReader instance with less than 4 bytes of data
        data = b'\x00\x00\x00'  # This is incomplete data
        reader = FlvReader(data)
        
        # Call read_unsigned_int and expect an exception
        with pytest.raises(Exception) as excinfo:
            reader.read_unsigned_int()
        
        assert 'FlvReader error: need 4 bytes while only 3 bytes got' in str(excinfo.value)
