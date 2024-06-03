# file youtube_dl/downloader/f4m.py:214-215
# lines [215]
# branches []

import pytest
from io import BytesIO
from youtube_dl.downloader.f4m import write_unsigned_int_24
from youtube_dl.compat import compat_struct_pack

def test_write_unsigned_int_24():
    stream = BytesIO()
    val = 0x123456  # Example value to test
    write_unsigned_int_24(stream, val)
    
    # Verify the written value
    expected_bytes = compat_struct_pack('!I', val)[1:]
    assert stream.getvalue() == expected_bytes

    # Clean up
    stream.close()
