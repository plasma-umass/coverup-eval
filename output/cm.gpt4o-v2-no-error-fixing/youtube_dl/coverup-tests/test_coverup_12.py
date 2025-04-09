# file: youtube_dl/downloader/f4m.py:48-49
# asked: {"lines": [49], "branches": []}
# gained: {"lines": [49], "branches": []}

import pytest
from youtube_dl.downloader.f4m import FlvReader
from youtube_dl.compat import compat_struct_unpack

class TestFlvReader:
    
    def test_read_unsigned_char(self):
        # Create a FlvReader instance with known data
        data = b'\x01'
        reader = FlvReader(data)
        
        # Call the method and assert the result
        result = reader.read_unsigned_char()
        assert result == 1

    def test_read_bytes(self):
        # Create a FlvReader instance with known data
        data = b'\x01\x02\x03'
        reader = FlvReader(data)
        
        # Call the method and assert the result
        result = reader.read_bytes(2)
        assert result == b'\x01\x02'
        
        # Test for DataTruncatedError
        with pytest.raises(Exception) as excinfo:
            reader.read_bytes(4)
        assert 'FlvReader error: need 4 bytes while only 1 bytes got' in str(excinfo.value)
