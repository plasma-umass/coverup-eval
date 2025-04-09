# file youtube_dl/downloader/f4m.py:210-211
# lines [211]
# branches []

import pytest
from io import BytesIO
from youtube_dl.downloader.f4m import write_unsigned_int
from youtube_dl.compat import compat_struct_pack

def test_write_unsigned_int():
    stream = BytesIO()
    val = 1234567890
    write_unsigned_int(stream, val)
    
    # Verify the stream content
    expected_output = compat_struct_pack('!I', val)
    assert stream.getvalue() == expected_output

    # Clean up
    stream.close()
