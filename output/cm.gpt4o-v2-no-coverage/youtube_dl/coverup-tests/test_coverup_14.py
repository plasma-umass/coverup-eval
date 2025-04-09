# file: youtube_dl/downloader/f4m.py:42-43
# asked: {"lines": [43], "branches": []}
# gained: {"lines": [43], "branches": []}

import io
import struct
import pytest
from youtube_dl.downloader.f4m import FlvReader
from youtube_dl.compat import compat_struct_unpack

def test_read_unsigned_long_long():
    # Create a FlvReader instance with 8 bytes of data
    data = struct.pack('!Q', 1234567890123456789)
    reader = FlvReader(data)
    
    # Call the method and assert the result
    result = reader.read_unsigned_long_long()
    assert result == 1234567890123456789

    # Clean up
    reader.close()
