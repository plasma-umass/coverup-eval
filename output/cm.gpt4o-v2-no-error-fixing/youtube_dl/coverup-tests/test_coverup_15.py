# file: youtube_dl/downloader/f4m.py:214-215
# asked: {"lines": [215], "branches": []}
# gained: {"lines": [215], "branches": []}

import io
from youtube_dl.downloader.f4m import write_unsigned_int_24

def test_write_unsigned_int_24():
    stream = io.BytesIO()
    val = 0x123456  # Example value

    write_unsigned_int_24(stream, val)

    # Verify the written value
    result = stream.getvalue()
    expected = b'\x12\x34\x56'
    assert result == expected, f"Expected {expected}, but got {result}"

    # Clean up
    stream.close()
