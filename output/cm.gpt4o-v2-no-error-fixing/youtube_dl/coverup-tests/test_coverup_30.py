# file: youtube_dl/downloader/f4m.py:42-43
# asked: {"lines": [43], "branches": []}
# gained: {"lines": [43], "branches": []}

import io
from youtube_dl.compat import compat_struct_unpack
from youtube_dl.downloader.f4m import FlvReader
import pytest

def test_read_unsigned_long_long():
    # Create a FlvReader instance with 8 bytes of data
    data = b'\x00\x00\x00\x00\x00\x00\x00\x01'
    reader = FlvReader(data)
    
    # Call the method and check the result
    result = reader.read_unsigned_long_long()
    assert result == 1

    # Clean up
    reader.close()
