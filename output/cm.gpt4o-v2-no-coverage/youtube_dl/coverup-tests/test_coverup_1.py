# file: youtube_dl/downloader/f4m.py:214-215
# asked: {"lines": [214, 215], "branches": []}
# gained: {"lines": [214, 215], "branches": []}

import pytest
from io import BytesIO
from youtube_dl.downloader.f4m import write_unsigned_int_24

def test_write_unsigned_int_24():
    stream = BytesIO()
    val = 0x123456
    write_unsigned_int_24(stream, val)
    result = stream.getvalue()
    assert result == b'\x12\x34\x56'
    stream.close()
