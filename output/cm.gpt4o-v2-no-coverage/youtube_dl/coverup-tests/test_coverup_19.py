# file: youtube_dl/downloader/f4m.py:45-46
# asked: {"lines": [46], "branches": []}
# gained: {"lines": [46], "branches": []}

import io
import struct
import pytest
from youtube_dl.compat import compat_struct_unpack
from youtube_dl.downloader.f4m import FlvReader

def test_compat_struct_unpack():
    # Test compat_struct_unpack function
    result = compat_struct_unpack('!I', b'\x00\x00\x00\x01')
    assert result == (1,)

def test_flv_reader_read_unsigned_int():
    # Test read_unsigned_int method of FlvReader
    data = b'\x00\x00\x00\x01'
    reader = FlvReader(data)
    result = reader.read_unsigned_int()
    assert result == 1

@pytest.fixture
def flv_reader():
    data = b'\x00\x00\x00\x01'
    return FlvReader(data)

def test_flv_reader_read_unsigned_int_with_fixture(flv_reader):
    result = flv_reader.read_unsigned_int()
    assert result == 1
